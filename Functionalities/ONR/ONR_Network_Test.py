## OPTIMAL NETWORK RECONFIGURATION FOR DN RELIABILITY (Topology Constrained)

# Importazione delle librerie:
import sys
import re
from math import pi, sqrt, cos, sin, tan, atan2
import numpy as np
import pandas as pd
import pandapower as pp
import pandapower.networks as pn
import plotly.graph_objects as go
import networkx as nx
import graphviz
from pyomo.environ import *
import random
from timeit import default_timer as timer
from itertools import chain
import collections
from collections import OrderedDict
import copy
from IPython.display import HTML
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib import rc
import os
import warnings
import time
import opendssdirect as dss
import win32com.client

warnings.filterwarnings("ignore")
pd.options.mode.chained_assignment = None 

#%% Setto l'interfaccia tra OpenDSS e Python 

dssObj= win32com.client.Dispatch("OpenDSSEngine.DSS")
dssText = dssObj.Text 
dssCircuit = dssObj.ActiveCircuit 
dssSolution = dssCircuit.Solution 
dssElem = dssCircuit.ActiveCktElement 
dssBus = dssCircuit.ActiveBus
dssLines = dssCircuit.Lines
dssXfmr = dssCircuit.Transformers
dssLoads = dssCircuit.Loads
dssActiveClass = dssCircuit.ActiveClass
dssActiveBus = dssCircuit.ActiveBus

# Pulisco tutta la cache di OpenDSS:
dssText.Command = 'Clear all'

# CARICAMENTO DATI RETE:
    
dssText.Command = f"compile 'C:/Users/anton/Desktop/NetworkTEST.DSS'"

# Liste e dizionari degli elementi di rete:

buses = []
 
linee = []
linee_bus_from_to = {}
linee_stato = {}
linee_lungh = {}

switch = []

transformers = []
trafi_bus_from_to = {}

loads = []
bus_loads = {}

for el in dssCircuit.AllElementNames:
    
    dssCircuit.SetActiveElement(el)
    Nome_elemento = dssElem.Name
    Bus_elemento = dssElem.BusNames
    
    if el.startswith('Transformer'):
        transformers.append(Nome_elemento)
        trafi_bus_from_to[Nome_elemento] = Bus_elemento 
       
    if el.startswith('Load'):
        loads.append(Nome_elemento)
        bus_loads[Nome_elemento] = Bus_elemento
           
    if el.startswith('Line'):
        linee.append(Nome_elemento)
        linee_bus_from_to[Nome_elemento] = Bus_elemento
        linee_lungh[Nome_elemento] = dssLines.Length
        linee_stato[Nome_elemento] = dssElem.IsOpen(2,0)                       # (Se IsOpen = False, allora la linea è chiusa)

# Riconosco gli switch dalla lista delle linee (il loro nome ha una "s" come ultimo carattere letterale):
switch = [el for el in linee if re.compile(r'\ds', re.IGNORECASE).search(el)]

# Ottengo la lista completa di tutti i branches:
branches = linee + transformers
branches_bus_from_to = dict(chain(linee_bus_from_to.items(),trafi_bus_from_to.items()))
Nbranches = len(branches)
Nswitch = len(switch)
        
# Effettuo la risoluzione della rete prima di ricavare i nomi dei bus e le altre grandezze elettriche:

dssSolution.Solve()
for i in dssCircuit.AllBusNames: 
    dssCircuit.SetActiveBus(i)
    buses.append(i)    
Nbus = len(buses)


#%% Informazioni topologiche sulla rete completamente connessa:
    
# Matrici di adiacenza e incidenza:
def Matrice_di_adiacenza(Nbus,branches):
    matrice_adiacenza = pd.DataFrame(np.zeros((Nbus,Nbus)),index=buses,columns=buses) 
    for b in branches:
        bus1 = branches_bus_from_to[b][0]
        bus2 = branches_bus_from_to[b][1]
        matrice_adiacenza.loc[bus1,bus2] = 1
        matrice_adiacenza.loc[bus2,bus1] = 1
    return matrice_adiacenza
adiacenza_pre = Matrice_di_adiacenza(Nbus,branches)

def Matrice_di_incidenza(Nbranches,Nbus):
    matrice_incidenza = pd.DataFrame(np.zeros((Nbranches,Nbus)),index=branches,columns=buses)
    for b in branches:
        bus1 = branches_bus_from_to[b][0]
        bus2 = branches_bus_from_to[b][1]       
        matrice_incidenza.loc[b,bus1] = 1
        matrice_incidenza.loc[b,bus2] = -1
    return matrice_incidenza            
incidenza_pre = Matrice_di_incidenza(Nbranches,Nbus)

# Ricavo il set di bus connessi con ciascun bus i:
busconnessi = {(i):[] for i in buses}
for i in buses:
    for j in buses:
        if adiacenza_pre.loc[i,j] == 1:
            busconnessi[i].append(j)
            
# Ricavo il set di branches connessi a ciascun bus i:    
BranchesConnessiPerBus = {(i):[] for i in buses}
for i in buses:
    connections = []
    for b in branches:
        if (branches_bus_from_to[b][0] == i) or (branches_bus_from_to[b][1] == i):
            connections.append(b)
    BranchesConnessiPerBus[i] = connections
        
# Ricavo il set dei possibili "nodi foglia" e il set di linee connesse a un nodo foglia (linee non switchabili):
LeafNodes = [] ; BranchesToLeaves = []
for i in buses:
    if len(busconnessi[i]) == 1:
        LeafNodes.append(i)
    if len(BranchesConnessiPerBus[i]) == 1:
        BranchesToLeaves.append(BranchesConnessiPerBus[i][0])
        
#%% Suddivisione zonale della rete secondo gli switch:
    
print('Suddivisione zonale della rete - START')
def Suddivisione_Zonale(buses, branches, switch):
    
    zone = []
    zone_bus = {}
    
    # Creazione delle zone:
    for b in branches:
        if b not in switch:
            i, j = branches_bus_from_to[b]
            # print('*) Branch:',b,'|',i,'|',j)
            i_presente=j_presente=False
            for n in zone_bus.values():
                if i in n:
                    i_presente=True
                if j in n:
                    j_presente=True
         
            # Se entrambi i nodi sono presenti nella stessa zona, continua al prossimo ramo:
            if i_presente and j_presente:
                # print(i,j,'sono nella stessa zona.')
                for z, buses_in_zone in zone_bus.items():
                    if i in buses_in_zone:
                        z_i = z
                    if j in buses_in_zone:
                        z_j = z
                if z_i != z_j:
                    zone_bus[z_i].extend(zone_bus[z_j])
                    zone_bus[z_j] = []
                continue
            # Se solo i è presente, aggiungo j alla stessa zona:
            if i_presente and not j_presente:
                # print('Solo i è presente:',i)
                for z, buses_in_zone in zone_bus.items():
                    if i in buses_in_zone:
                        zone_bus[z].append(j)
                        break
            # Se solo j è presente, aggiungo i alla stessa zona:
            elif j_presente and not i_presente:
                # print('Solo i è presente:',j)
                for z, buses_in_zone in zone_bus.items():
                    if j in buses_in_zone:
                        zone_bus[z].append(i)
                        break
            # Se nessuno dei due è presente, creo una nuova zona con entrambi:
            elif not i_presente and not j_presente:
                # print(i,j,'non sono presenti.')
                nuova_zona = "Z" + str(len(zone))
                zone.append(nuova_zona)
                zone_bus[nuova_zona] = [i, j]
                # print('>> La zona', nuova_zona, 'è stata creata.')
    
    # Controllo se ci sono bus non assegnati ad alcuna zona:
    for i in buses:
        trovato = False
        for z in zone:
            if i in zone_bus[z]:
                trovato = True
        if not trovato:
            # print(i,'non è stato assegnato a nessuna zona.')
            # Se il bus i risulta non assegnato, viene inserito in una nuova zona:
            nuova_zona = "Z" + str(len(zone))
            zone.append(nuova_zona)
            zone_bus[nuova_zona] = [i]
            # print('>> La zona', nuova_zona, 'è stata creata. Il bus',i,'è stato assegnato a',nuova_zona)
    
    # Rilevo eventuali zone vuote, le elimino e aggiorno la numerazione di zone e zone_bus:
    zone_bus = {k: v for k, v in zone_bus.items() if v}
    zone_bus = {f'Z{i}': v for i, (k, v) in enumerate(zone_bus.items(), start=0)}
    zone = list(zone_bus.keys())
    
    return zone, zone_bus

# Applico la funzione creata:
zone, zone_bus = Suddivisione_Zonale(buses, branches, switch)
print('Suddivisione zonale della rete - END')
print('Le zone ottenute sono:',len(zone)); print(''); Nzone = len(zone)

# Zona-from e Zona-to per ciascuno switch:    
switch_zone_from_to = {(sw):[] for sw in switch}
for sw in switch:
    i, j = branches_bus_from_to[sw]
    for z in zone:
        if i in zone_bus[z]:
            z_fr = z
        if j in zone_bus[z]:
            z_to = z
    switch_zone_from_to[sw].append(z_fr)
    switch_zone_from_to[sw].append(z_to)
    
# Zona-from e Zona-to per ciascun branch:  
branch_zone_from_to = {(b):[] for b in branches}
for b in branches:
    i, j = branches_bus_from_to[b]
    for z in zone:
        if i in zone_bus[z]:
            z_fr = z
        if j in zone_bus[z]:
            z_to = z
    branch_zone_from_to[b].append(z_fr)
    branch_zone_from_to[b].append(z_to)
    
# Ricavo il set di zone connesse con ciascuna zona z:  
def Matrice_di_adiacenza_zone_zone(Nzone,switch):
    matrice_adiacenza = pd.DataFrame(np.zeros((Nzone,Nzone)),index=zone,columns=zone) 
    for sw in switch:
        z1 = switch_zone_from_to[sw][0]
        z2 = switch_zone_from_to[sw][1]
        matrice_adiacenza.loc[z1,z2] = 1
        matrice_adiacenza.loc[z2,z1] = 1
    return matrice_adiacenza
adiacenza_zone_pre = Matrice_di_adiacenza_zone_zone(Nzone,switch)

zoneconnesse = {(z):[] for z in zone}
for i in zone:
    for j in zone:
        if adiacenza_zone_pre.loc[i,j] == 1:
            zoneconnesse[i].append(j)
            
# Ricavo le zone a capo feeder:
zone_capo_feeder = zoneconnesse['Z0']
# Lista delle zone senza la zona Z0:
zonenosource = zone[1:]

# Ricavo l'insieme dei branch in ciascuna zona:
zone_branch = {(z):[] for z in zone}
for b in branches:
    i, j = branches_bus_from_to[b]
    for z in zone:
        if i in zone_bus[z] and j in zone_bus[z]:
            zone_branch[z].append(b)

# Rappresentazione del grafo orientato zonale con graphviz:
ZonalGraph = graphviz.Digraph(comment='Distribution Network Zonal Graph')
# Imposta le dimensioni della pagina e altre opzioni di visualizzazione:
ZonalGraph.attr(size='8,8!', orientation='portrait', layout='dot', seed='927')
# Imposta la qualità massima per l'esportazione in formato PNG
ZonalGraph.attr(graphattr='dpi=600')
# Imposta il font
ZonalGraph.attr(fontname='Times New Roman')
# Costruzione del grafo:
for z in range(len(zone)):
    if zone[z] == 'Z0':
        ZonalGraph.node(str(z), label=f'{z}', shape='circle', color='black', fillcolor='deepskyblue', style='filled', fixedsize='true', width='0.3', height='0.3', fontsize='14', pos='c', penwidth='1.0')
    elif zone[z] in zone_capo_feeder:
        ZonalGraph.node(str(z), label=f'{z}', shape='circle', color='black', fillcolor='green', style='filled', fixedsize='true', width='0.3', height='0.3', fontsize='14', pos='c', penwidth='1.0')
    else:
        ZonalGraph.node(str(z), label=f'{z}', shape='circle', color='black', fillcolor='white', style='filled', fixedsize='true', width='0.3', height='0.3', fontsize='14', pos='c', penwidth='1.0')
for sw in range(len(switch)):
    z_fr = zone.index(switch_zone_from_to[switch[sw]][0])
    z_to = zone.index(switch_zone_from_to[switch[sw]][1])
    ZonalGraph.edge(str(z_fr), str(z_to), color='black', constraint='true')   
# Visualizzazione:
ZonalGraph.render(filename='Distribution Network Zonal Graph', format='png', cleanup=True)
ZonalGraph.view()

#%% PARAMETRI PER IL PROBLEMA DI OTTIMIZZAZIONE:
    
# Potenza attiva e reattiva richiesta dai carichi:
P_loads = {}
Q_loads = {}
for l in loads:
    dssCircuit.SetActiveElement(l)
    P_Q_3fasi = list(dssElem.Powers)
    P_loads[l] = P_Q_3fasi[0] + P_Q_3fasi[2] + P_Q_3fasi[4] # kW
    Q_loads[l] = P_Q_3fasi[1] + P_Q_3fasi[3] + P_Q_3fasi[5] # kvar

# Potenza attiva e reattiva richiesta dai carichi a livello zonale:
PDz = {(z):0 for z in zone}
QDz = {(z):0 for z in zone}
for z in zone:
    PDz[z] = sum(P_loads[l] for l in loads if bus_loads[l][0] in zone_bus[z])
    QDz[z] = sum(Q_loads[l] for l in loads if bus_loads[l][0] in zone_bus[z])

# Numero di clienti:
    
# Definisco la funzione gaussiana per determinare il numero di clienti in maniera randomica:
def Gaussian_Function(x, mu, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# Fisso il seed per la riproducibilità del codice, in maniera tale da ottenere sempre gli stessi valori randomici:
random_seed = 89 # (numero grande dispari)
random.seed(random_seed)
np.random.seed(random_seed)

# Parametri della funzione gaussiana:
mu = 1       # media
sigma = 1/3  # deviazione standard

# Creo un array di valori casuali da una distribuzione gaussiana:
valori_randomici = np.random.normal(mu, sigma, len(loads))
fgauss = Gaussian_Function(valori_randomici, mu, sigma)

# Moltiplico ogni potenza attiva richiesta dal carico per il valore gaussiano corrispondente:
g = {(d): P_loads[d]*fgauss[loads.index(d)] for d in loads} 

# Imposto un valore massimo ai risultati altrimenti ottengo dei risultati anche maggiori di mille:
valore_massimo = 60  
g = {(d): np.minimum(g[d], valore_massimo) for d in loads} 

# Normalizzo i valori in modo che la somma sia pari a 30000:
g_normalized = {(d):0 for d in loads}
N_customers = {(d):0 for d in loads}
sum_customers = sum(g.values())
for d in loads:
    if sum_customers != 0:    
            g_normalized[d] = np.clip(g[d], 1, np.inf)
            scale_factor = 30000 / sum_customers
            g_normalized[d] = (g_normalized[d] * scale_factor).astype(int)
    else:
        g_normalized[d] = g[d]
    # Tronco i risultati a valori interi:
    N_customers[d] = np.trunc(g_normalized[d]).astype(int)    
    
# Parametri per la Reliability:
BusesReliability = pd.DataFrame(np.zeros((len(buses),3)),columns=['Zona','Lambda_i','R_i'],index=buses)    
BranchesReliability = pd.DataFrame(np.zeros((len(linee),8)),columns=['Bus_from','Bus_to','Zona_from','Zona_to','Type','Length','Lambda_l','R_l'],index=linee)
ZoneReliability = pd.DataFrame(np.zeros((Nzone,6)),columns=['N_branches','Lambda_z','Lambda_z_1','Lambda_z_2','R_z','Customers'],index=zone)

for i in buses:
    for z in zone:
        if i in zone_bus[z]:
            BusesReliability.Zona[i] = z

        BusesReliability.Lambda_i[i] = 0.001129
        BusesReliability.R_i[i] = 261
       
for l in linee:   
    
    BranchesReliability.Bus_from[l] = branches_bus_from_to[l][0]
    BranchesReliability.Bus_to[l] = branches_bus_from_to[l][1]
    BranchesReliability.Zona_from[l] = branch_zone_from_to[l][0]
    BranchesReliability.Zona_to[l] = branch_zone_from_to[l][1]

    BranchesReliability.Type[l] = 'L'
    BranchesReliability.Length[l] = linee_lungh[l]
    if l in switch:
        BranchesReliability.Type[l] = 'S'
        BranchesReliability.Length[l] = linee_lungh[l]
    
    
    BranchesReliability.Lambda_l[l] = 3*BranchesReliability.Length[l]*(0.00336/0.3048)
    BranchesReliability.R_l[l] = 16

for z in zone:
    ZoneReliability.N_branches[z] = len(zone_branch[z])  
     
    ZoneReliability.Lambda_z[z] = sum(BranchesReliability.Lambda_l[l] for l in linee if l in zone_branch[z]) + sum(BusesReliability.Lambda_i[i] for i in zone_bus[z])   
    ZoneReliability.Lambda_z_2[z] = (1/3)*ZoneReliability.Lambda_z[z] #guasti non monofase
    ZoneReliability.Lambda_z_1[z] = (2/3)*ZoneReliability.Lambda_z[z] #guasti monofase a terra
    ZoneReliability.R_z[z] = (sum(BranchesReliability.R_l[l]*BranchesReliability.Lambda_l[l] for l in linee if l in zone_branch[z]) + sum(BusesReliability.R_i[i]*BusesReliability.Lambda_i[i] for i in zone_bus[z]))/ZoneReliability.Lambda_z[z] 
    ZoneReliability.Customers[z] = sum(N_customers[d] for d in loads if bus_loads[d][0] in zone_bus[z])
       
#%% Assegno alla rete una topologia radiale iniziale e la confronto con quella in cui tutti gli switch sono chiusi:
    
statoinizialeswitch = [1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1]

statoinizialeswitch = {(sw): si for sw, si in zip(switch, statoinizialeswitch)}
switch_aperti_SI = sum(1 for valore in statoinizialeswitch.values() if valore == 0)
switch_chiusi_SI = sum(1 for valore in statoinizialeswitch.values() if valore == 1)
transizioni_da_0_a_1 = 0
transizioni_da_1_a_0 = 0
switch_rimasti_a_0 = 0
switch_rimasti_a_1 = 0
for sw in switch:   
    # Valuto le transizioni:
    if statoinizialeswitch[sw] == 0:
        transizioni_da_1_a_0 += 1    
    # Valuto gli switch rimasti a 1:
    if statoinizialeswitch[sw] == 1:
        switch_rimasti_a_1 += 1
print('Rispetto alla topologia in cui tutti gli switch sono chiusi:')
print('N° switch aperti:',switch_aperti_SI)
print('N° switch chiusi:',switch_chiusi_SI)
print("N° switch 0 -> 1:", transizioni_da_0_a_1)
print("N° switch 1 -> 0:", transizioni_da_1_a_0)
print("N° switch rimasti aperti:", switch_rimasti_a_0)
print("N° switch rimasti chiusi:", switch_rimasti_a_1); print('')



# =============================================================================
# ASSEGNAZIONE STATI SWITCH SU OPENDSS PER CONFIGURAZIONE RADIALE
# =============================================================================
# Trovo le potenze attive e reattive dei vari elementi e le correnti delle linee

dssLoads.First
for i in range(dssLoads.Count):
    # if 'c_' in dssLoads.Name:
    # print(dssLoads.Name)
    dssLoads.kW=dssLoads.kW*1.2
    dssLoads.Next
    
for s in switch:
    dssCircuit.SetActiveElement(s)
    if statoinizialeswitch[s] == 0:
            dssElem.Open(2, 0)
            # statofinaleswitch[s] = 0
    else:
        dssElem.Close(2,0)
        # statofinaleswitch[s] = 1
    
# =============================================================================
# LOAD FLOW STATO INIZIALE CON STATO SWITCH PER RADIALITÀ
# =============================================================================
dssSolution.Solve()

P_slack_pre = {}
Q_slack_pre = {}

P_gen = {}
Q_gen = {}

P_loads = {}
Q_loads = {}

P_linee_busfrom = {}
P_linee_busto = {}
Q_linee_busfrom = {}
Q_linee_busto = {}
Perdite_linee_kw = {}
Perdite_linee_kvar = {}
Correnti_linee_modulo = {}
Portata_linee = {}
Sijmax = {}  #portata dei branches in KVA

P_trafi_busfrom = {}
P_trafi_busto = {}
Q_trafi_busfrom = {}
Q_trafi_busto = {}
Perdite_trafi_kw = {}
Perdite_trafi_kvar = {}

P_switch_busfrom = {}
P_switch_busto = {}
Q_switch_busfrom = {}
Q_switch_busto = {}
Perdite_switch_kw = {}
Perdite_switch_kvar = {}


for m in dssCircuit.AllElementNames:
    dssCircuit.SetActiveElement(m)
    P = dssElem.Powers
    Losses = dssElem.Losses
    Correnti = dssElem.CurrentsMagAng
    if m.startswith('Vsource'):
        P_slack_pre[m] = -(P[0]+P[2]+P[4])
        Q_slack_pre[m] = -(P[1]+P[3]+P[5])
    elif m.startswith('Line'):
        if m in switch:
            Normalamps = dssLines.NormAmps
            P_switch_busfrom[m] = P[0]+ P[2]+P[4]
            P_switch_busto[m] =  P[6]+P[8]+P[10]
            Q_switch_busfrom[m] =  P[1]+P[3]+P[5]
            Q_switch_busto[m] = P[7]+P[9]+P[11]
            Perdite_switch_kw[m] = Losses[0]/1000
            Perdite_switch_kvar[m] = Losses[1]/1000
            Correnti_linee_modulo[m] = Correnti[0]
            Portata_linee[m] = Normalamps
        else:
            Normalamps = dssLines.NormAmps
            P_linee_busfrom[m] = P[0]+ P[2]+P[4]
            P_linee_busto[m] =  P[6]+P[8]+P[10]
            Q_linee_busfrom[m] =  P[1]+P[3]+P[5]
            Q_linee_busto[m] = P[7]+P[9]+P[11]
            Perdite_linee_kw[m] = Losses[0]/1000
            Perdite_linee_kvar[m] = Losses[1]/1000
            Correnti_linee_modulo[m] = Correnti[0]
            Portata_linee[m] = Normalamps
    elif  m.startswith('Transformer'):
          P_trafi_busfrom[m] = P[0]+ P[2]+P[4]
          P_trafi_busto[m] =  P[8]+P[10]+P[12]
          Q_trafi_busfrom[m] =  P[1]+P[3]+P[5]
          Q_trafi_busto[m] = P[9]+P[11]+P[13] 
          Perdite_trafi_kw[m] = Losses[0]/1000
          Perdite_trafi_kvar[m] = Losses[1]/1000         
    elif    m.startswith('Load'):
            P_loads[m] = P[0]+P[2]+P[4]
            Q_loads[m] = P[1]+P[3]+P[5]
    elif m.startswith('Generator'): 
         P_gen[m]= -(P[0]+P[2]+P[4])
         Q_gen[m]= (P[1]+P[3]+P[5])


perdite_totali_kw_pre = dssCircuit.Losses[0]/1000 
perdite_totali_kvar_pre = dssCircuit.Losses[1]/1000 


         
if len(P_gen) == 0:
    print("Non ci sono generatori")
    P_gen = 0
    Q_gen = 0                

print(''); print('Analisi delle potenze (ACLF) con la topologia iniziale:')
print('')    
# print('Generazione:',round(sum(P_gen.values()),2), 'KW', ';', round(sum(Q_gen.values()),2),'Kvar')
print('Carico:',round(sum(P_loads.values()),2) , 'KW', ';', round(sum(Q_loads.values()),2),'Kvar') 
print('Slack Bus active power:',round(sum(P_slack_pre.values()),2) , 'KW')
print('Slack Bus reactive power:',round(sum(Q_slack_pre.values()),2) , 'Kvar')
print('Active power losses:',round(perdite_totali_kw_pre,2) , 'KW' )
print('Reactive power losses:',round(perdite_totali_kvar_pre,2) , 'Kvar' )
print('')


# Controllo se ci sono linee in sovraccarico:

sovraccarichi_iniziali ={}
for b in linee:   
  if  Correnti_linee_modulo[b] > Portata_linee[b]:
     print(b, 'in sovraccarico:',round((Correnti_linee_modulo[b]/ Portata_linee[b])*100,0), '%')
     sovraccarichi_iniziali[b] = round((Correnti_linee_modulo[b]/ Portata_linee[b])*100,0)
print('')


# Tensioni base
Vnbus = {}  #kv
for b in buses:
    if b == 'sourcebus' or b=='bus_n1' or b=='bus_n2':
       Vnbus[b] = 150
    else:
        Vnbus[b] = 20

# Trovo gli switch:
switch = []
bus_from_to_sw = {}
bus_switch_from = {}
bus_switch_to = {}
rl_switch = {}  #ohm/km
xl_switch = {}   #ohm/km
cl_switch = {}  #nanoFarad/km
L_km_switch = {}


for m in dssCircuit.AllElementNames:
    dssCircuit.SetActiveElement(m)
    Nomi = dssElem.Name
    Bus_elemento = dssElem.BusNames
    if m.startswith('Line') and 's' in m and 'sb' not in m:
        switch.append(Nomi)
        bus_from_to_sw[m] = Bus_elemento
        bus_switch_from[m] = Bus_elemento[0]
        bus_switch_to[m] = Bus_elemento[1]
        myR1 = dssLines.R1
        myX1 = dssLines.X1
        myC1 = dssLines.C1 
        myLen = dssLines.Length
        rl_switch[m] = myR1
        xl_switch[m] = myX1
        cl_switch[m] = myC1 
        L_km_switch[m] = myLen


source = []
linee = []
trafi = []
loads = []
generatori = []
slack_bus = {} 
bus_trafi = {} ; bus_trafi_from = {} ; bus_trafi_to = {}
bus_load = {}
bus_linee = {} ; bus_linee_from = {} ; bus_linee_to = {}
bus_gen = {}
tensione_source = {}
rl = {}  #ohm/km
xl = {}   #ohm/km
cl = {}  #nanoFarad/km
L_km = {}
R_l = {}  #tempo di riparazione linea
lambda_l = {}  #tasso di guasto linea
xcc_pu = {}  
rcc_pu = {}
tap = {}
Sn = {}  #kva

i = dssXfmr.First
for m in dssCircuit.AllElementNames:
    dssCircuit.SetActiveElement(m)
    Nomi = dssElem.Name
    Bus_elemento = dssElem.BusNames
    Tensione = dssElem.VoltagesMagAng
    
    if m.startswith('Vsource'):
        source.append(Nomi)
        slack_bus[m] = Bus_elemento[0]
        tensione_source[m] = Tensione
    elif m.startswith('Line'):
        if m in switch:
            continue
        linee.append(Nomi)
        bus_linee[m] = Bus_elemento
        bus_linee_from[m] = Bus_elemento[0]
        bus_linee_to[m] = Bus_elemento[1]
        myR1 = dssLines.R1
        myX1 = dssLines.X1
        myC1 = dssLines.C1 
        myLen = dssLines.Length
        rl[m] = myR1
        xl[m] = myX1
        cl[m] = myC1 
        L_km[m] = myLen  
        R_l[m] = float(dssElem.Properties('repair').Val)
        lambda_l[m] = round(float(dssElem.Properties('faultrate').Val) * L_km[m],6)
    elif  m.startswith('Transformer'):
          trafi.append(Nomi)
          bus_trafi[m] = Bus_elemento
          bus_trafi_from[m] = Bus_elemento[0]
          bus_trafi_to[m] = Bus_elemento[1]
          myXHL = dssXfmr.xhl
          xcc_pu[m] = myXHL
          rcc_pu[m] = dssXfmr.R*2
          tap[m] = dssXfmr.Tap
          Sn[m] = dssXfmr.kva
          i = dssXfmr.Next
    elif    m.startswith('Load'):
            loads.append(Nomi)
            bus_load[m] = Bus_elemento[0]
    elif   m.startswith('Generator'):
           generatori.append(Nomi)
           bus_gen[m] = Bus_elemento[0]

slack_bus_lista = list(slack_bus.values())

Nlinee = len(linee)
Ntrafi = len(trafi)

# Trovo tutti i branches e i busfrom e busto di ogni elemento

           
branches = linee + trafi + switch
Nbranches = len(branches)


busfrom = dict(**bus_linee_from, **bus_trafi_from, **bus_switch_from)
busto = dict(**bus_linee_to, **bus_trafi_to, **bus_switch_to)



# Trovo le tensioni sui bus in modulo e fase e verifico se violano qualche limite
    
tensioni_bus_modulo = {}
theta0 = {}  #in rad
for b in buses:
    dssCircuit.SetActiveBus(b)
    myVolt = dssActiveBus.VMagAngle
    tensioni_bus_modulo[b] = myVolt[0]/1000
    theta0[b] = myVolt[1]*pi/180

# Modulo della tensione concatenata in p.u.:    
V0 = {} 

for a,b in tensioni_bus_modulo.items():
    if a == 'sourcebus' or a =='bus_n1' or a =='bus_n2':
        V0[a] = b*sqrt(3)/150
    else:
        V0[a] = b*sqrt(3)/20

# Ricavo la portata dei branches in KVA:
Sijmax = {(b):0 for b in branches}
Sijpre = {(b):0 for b in branches}


for b in branches:
    if b in linee or b in switch:
        Sijmax[b] = round(Vnbus[busfrom[b]]*Portata_linee[b],2)
        Sijpre[b] = round(sqrt(3)*tensioni_bus_modulo[busfrom[b]]*Correnti_linee_modulo[b],2)

    else:
        Sijmax[b] = Sn[b]

Vmax=1.05
Vmin=0.95

violazioni_tensioni = {}
for a,b in V0.items():
    if b<=Vmin or b>=Vmax:
        print('Violazione di tensione sul nodo',a ,'- Vi =',round(b,4),'p.u.')
        violazioni_tensioni[a] = b
print('')          
  

# Modulo delle tensioni in pu
plt.figure(3, figsize=(15, 6))
plt.axhline(1, color='black', linestyle='--', linewidth=1)
plt.plot(buses, V0.values(), linewidth=0.5, marker='o', markersize=1, color='dodgerblue', label='Pre ONR')
# plt.plot(buses, V1.values(), linewidth=1, marker='o',markersize=1, color='orange', label='ONR risultati')
# plt.plot(buses, Vi.values(), linewidth=1, marker='o',markersize=1, color='forestgreen', label='Post ONR')
plt.plot('sourcebus',V0['sourcebus'], marker='D', markersize=5, color='red',label='Slack Bus')
plt.axhline(Vmax, color='red', linestyle='--', linewidth=1, label='$V_{\\mathrm{max}}$' )
plt.axhline(Vmin, color='blue', linestyle='--', linewidth=1, label='$V_{\\mathrm{min}}$')
plt.ylim(0.85, 1.2)
plt.xticks([]) 
plt.xlabel('Nodi', fontsize=20 )
plt.ylabel(r'$V_{i} \, [\mathrm{pu}]$', fontsize=20)
plt.legend(loc='best', fontsize=12,  frameon=False, ncol=2)
plt.show()

from matplotlib.lines import Line2D
      
# Flussi di potenza apparente sui branches in sovraccarico:
Sij_plot = {}
for b in linee+trafi:
    if Sijpre[b] > Sijmax[b]:
        Sij_plot[b] = Sijpre[b]
        
plt.figure(2, figsize=(15, 6))
for b in Sij_plot.keys():
    plt.bar(b, Sijmax[b], linewidth=1, color='salmon')
    plt.stem(b, Sijpre[b], linefmt='darkred', markerfmt='v', basefmt=' ')    
plt.xticks(range(0, len(Sij_plot.keys())), [f'{br} ' for br in Sij_plot.keys()], rotation=45)  # Ruota le etichette di 45 gradi
plt.xlabel('Rami in sovraccarico', fontsize=20)
plt.ylabel(r'$S_{ij} \, [\mathrm{kVA}]$', fontsize=20)
legend_elements = [Line2D([0], [0], color='salmon', linewidth=10, label=r'$S_{ij}^{max}$'), Line2D([0], [0], color='darkred', marker='v', linestyle='None', label=r'$S_{ij}^{pre}$')]
plt.legend(handles=legend_elements,  fontsize=12)
plt.show()     


# =============================================================================
# FINE PARTE LOAD FLOW INIZIALE
# =============================================================================

# Creazione del grafo zonale radiale con NetworkX:
NX_ZonalGraph = nx.Graph()  
NX_ZonalGraph.add_nodes_from(zone)
for sw in switch:
    if statoinizialeswitch[sw] == 1:
        i,j = switch_zone_from_to[sw]
        NX_ZonalGraph.add_edge(i,j)
print('Il grafo zonale radiale con la topologia iniziale ha',nx.number_of_nodes(NX_ZonalGraph),'nodi e',nx.number_of_edges(NX_ZonalGraph),'rami connessi.')
# Connectivity Check:
is_connected = nx.is_connected(NX_ZonalGraph)
print(f'La rete è ancora connessa? {is_connected}'); print('')
# Impostazioni per la figura:
plt.figure(1, figsize=(18,12))
# pos = nx.drawing.nx_pydot.graphviz_layout(NX_ZonalGraph, prog='dot', root=zone[0])
# pos = nx.drawing.nx_agraph.graphviz_layout(NX_ZonalGraph, prog='dot', root=zone[0])
pos = nx.kamada_kawai_layout(NX_ZonalGraph)
node_border_colors = 'black'
node_fill_colors = ['lightblue' if node == 'Z0' else 'lightgreen' if node in zone_capo_feeder else 'white' for node in NX_ZonalGraph.nodes()]
nx.draw(NX_ZonalGraph, pos, with_labels=True, font_weight='bold', node_size=400, node_color=node_fill_colors, edgecolors=node_border_colors, font_color='black', font_size=8)
plt.axis('off')
plt.show()

# Rappresentazione del grafo orientato zonale radiale con graphviz:
ZonalGraphRadial = graphviz.Digraph(comment='AMET Distribution Network Zonal Graph - Radial Initial Topology')
# Imposto le dimensioni della pagina e altre opzioni di visualizzazione:
ZonalGraphRadial.attr(size='8,10!', orientation='portrait', layout='dot', seed='927')
# Imposta la qualità massima per l'esportazione in formato PNG
ZonalGraphRadial.attr(graphattr='dpi=600')
# Imposta il font
ZonalGraph.attr(fontname='Times New Roman')
# Costruzione del grafo:
for z in range(len(zone)):
    if zone[z] == 'Z0':
        ZonalGraphRadial.node(str(z), label=f'{z}', shape='circle', color='black', fillcolor='deepskyblue', style='filled', fixedsize='true', width='0.3', height='0.3', fontsize='14', pos='c', penwidth='1.0')
    elif zone[z] in zone_capo_feeder:
        ZonalGraphRadial.node(str(z), label=f'{z}', shape='circle', color='black', fillcolor='green', style='filled', fixedsize='true', width='0.3', height='0.3', fontsize='14', pos='c', penwidth='1.0')
    else:
        ZonalGraphRadial.node(str(z), label=f'{z}', shape='circle', color='black', fillcolor='white', style='filled', fixedsize='true', width='0.3', height='0.3', fontsize='14', pos='c', penwidth='1.0')
for sw in range(len(switch)):
    z_fr = zone.index(switch_zone_from_to[switch[sw]][0])
    z_to = zone.index(switch_zone_from_to[switch[sw]][1])
    if statoinizialeswitch[switch[sw]] == 1:
        ZonalGraphRadial.edge(str(z_fr), str(z_to), color='black', constraint='true')   
    # else:
    #     ZonalGraphRadial.edge(str(z_fr), str(z_to), color='red', style='dashed', constraint='true')         
# Visualizzazione:
ZonalGraphRadial.render(filename='Distribution Network Zonal Graph - Radial Initial Topology', format='png', cleanup=True)
ZonalGraphRadial.view()



input_optimization = input('> Eseguire ONR stato iniziale? (y/n):'); print('')
if input_optimization.lower() != 'y':
    sys.exit()

tecnica = ['FRG','FNC','SFS']

SI_ReliabilityIndices = pd.DataFrame(np.zeros((3,3)), index=tecnica, columns= ['ENS','SAIDI','SAIFI'])
SI_ReliabilityIndices_Normalized = pd.DataFrame(np.zeros((3,3)), index=tecnica, columns= ['ENS','SAIDI','SAIFI'])

for tec in tecnica:

    # Creazione del modello:
    SI = ConcreteModel(name = "(Optimal Network Reconfiguration - STATO INIZIALE)")
    
    # VARIABILI CONTINUE
    SI.fs = Var(zone, within=Reals)
    SI.fzs = Var(zone, switch, within=Reals)
    
    SI.lamb_z = Var(zone, within=NonNegativeReals)
    SI.ENS_PRE = Var(within=NonNegativeReals)
    SI.U_z = Var(zone, within=NonNegativeReals)
    SI.y_SAIDI = Var(zone, within=NonNegativeReals)
    SI.y_SAIFI = Var(zone, within=NonNegativeReals)
    SI.SAIDI_PRE = Var(within=NonNegativeReals)
    SI.SAIFI_PRE = Var(within=NonNegativeReals)
    
    # VARIABILI BINARIE
    SI.x_ij = Var(switch, within=Binary)
    SI.Z_up = Var(zone, zone, within=Binary)
    SI.w_mk = Var(zonenosource, zonenosource, within=Binary)
    SI.Z_f = Var(zone_capo_feeder, zonenosource, zonenosource, within=Binary)
     
    # VARIABILI FISSATE:  
    for sw in switch:
        SI.x_ij[sw].fix(statoinizialeswitch[sw])
        
    # VINCOLI:
        
    def FlussiArtificiali_rule(SI,m,k):
        
        membroA = 0
        membroB = 0
        
        if m == k:
            membroB = 1
        
        for sw in switch:
            
            i = switch_zone_from_to[sw][0]
            j = switch_zone_from_to[sw][1]
            
            if i == k:
                membroA = membroA - SI.fzs[m,sw]
    
            if j == k:
                membroA = membroA + SI.fzs[m,sw] 
                        
        if k == "Z0":
            membroA = membroA + SI.fs[m]
                
        return membroA == membroB
    SI.FlussiArtificiali = Constraint(zone,zone,rule=FlussiArtificiali_rule)
    
    def stato_flusso_ij_switch_UB_rule(SI, sw, z): 
        return SI.fzs[z, sw] <= SI.x_ij[sw]
    SI.stato_flusso_ij_switch_UB = Constraint(switch, zone, rule=stato_flusso_ij_switch_UB_rule)
    
    def stato_flusso_ij_switch_LB_rule(SI, sw, z):
        return SI.fzs[z, sw] >= - SI.x_ij[sw]
    SI.stato_flusso_ij_switch_LB = Constraint(switch, zone, rule=stato_flusso_ij_switch_LB_rule)
    
    def zona_attiva_i_UB_rule(SI, k, sw):
        i = switch_zone_from_to[sw][0]
        return SI.Z_up[i, k] >= SI.fzs[k, sw] 
    SI.zona_attiva_i_UB = Constraint(zone, switch, rule=zona_attiva_i_UB_rule)
    
    def zona_attiva_j_UB_rule(SI, k, sw):
        j = switch_zone_from_to[sw][1]
        return SI.Z_up[j, k] >= SI.fzs[k, sw] 
    SI.zona_attiva_j_UB = Constraint(zone, switch, rule=zona_attiva_j_UB_rule)
    
    def zona_attiva_i_LB_rule(SI,k, sw):
        i = switch_zone_from_to[sw][0]
        return - SI.Z_up[i, k] <= SI.fzs[k, sw] 
    SI.zona_attiva_i_LB = Constraint(zone, switch, rule=zona_attiva_i_LB_rule)
    
    def zona_attiva_j_LB_rule(SI, k, sw):
        j = switch_zone_from_to[sw][1]
        return - SI.Z_up[j, k] <= SI.fzs[k, sw] 
    SI.zona_attiva_j_LB = Constraint(zone, switch, rule=zona_attiva_j_LB_rule)
    
    if tec == 'FRG' or tec == 'FNC':
        def zona_feeder_rule(SI, qi, m, k):
            return SI.Z_f[qi, m, k] >= SI.Z_up[qi, m] + SI.Z_up[qi, k] - 1 
        SI.zona_feeder = Constraint(zone_capo_feeder, zonenosource, zonenosource, rule=zona_feeder_rule)
        
        def Z_cug_rule(SI, m, k):
            return SI.w_mk[m, k] >= sum(SI.Z_f[qi, m, k] for qi in zone_capo_feeder)
        SI.Z_cug = Constraint(zonenosource, zonenosource, rule=Z_cug_rule)
    
    if tec == 'FRG':
        def Average_failure_FRG_rule(SI, z):
            sommatoria = 0
            if z == 'Z0':  
                return SI.lamb_z[z] == 0
            else:
                for k in zonenosource:
                    sommatoria += (SI.w_mk[k,z]) * (ZoneReliability.Lambda_z[k])
                return SI.lamb_z[z] == sommatoria    
        SI.Average_failure_FRG = Constraint(zone, rule=Average_failure_FRG_rule)
    
        def FRG_rule(SI, z):
            if z == 'Z0':
                return SI.U_z[z] == 0
            else:       
                return SI.U_z[z] == sum((SI.Z_up[k,z] * ZoneReliability.Lambda_z[k] * ZoneReliability.R_z[k]) + ((SI.w_mk[k,z] - SI.Z_up[k,z]) * ZoneReliability.Lambda_z[k] * 0.05) for k in zonenosource)
        SI.FRG = Constraint(zone, rule=FRG_rule)
        
    if tec == 'FNC':
        def Average_failure_FNC_rule(SI, z):
            sommatoria = 0
            if z == 'Z0':  
                return SI.lamb_z[z] == 0
            else:
                for k in zonenosource:
                    sommatoria += ((SI.Z_up[k,z]*ZoneReliability.Lambda_z_1[k]) + (SI.w_mk[k,z]*ZoneReliability.Lambda_z_2[k])) 
                return SI.lamb_z[z] == sommatoria    
        SI.Average_failure_FNC = Constraint(zone, rule=Average_failure_FNC_rule)
        
        def FNC_rule(SI, z):
            if z == 'Z0':
                return SI.U_z[z] == 0 
            else:
                return SI.U_z[z] == sum((SI.Z_up[k,z] * (ZoneReliability.Lambda_z_1[k] + ZoneReliability.Lambda_z_2[k]) * ZoneReliability.R_z[k]) + ((SI.w_mk[k,z] - SI.Z_up[k,z]) * ZoneReliability.Lambda_z_2[k] * 0.05) for k in zonenosource)
        SI.FNC = Constraint(zone, rule=FNC_rule)
        
    if tec == 'SFS':
        def Average_failure_SFS_rule(SI, z):
            sommatoria = 0
            if z == 'Z0':  
                return SI.lamb_z[z] == 0
            else:
                for k in zonenosource:
                    sommatoria += (SI.Z_up[k,z]*ZoneReliability.Lambda_z[k]) 
                return SI.lamb_z[z] == sommatoria    
        SI.Average_failure_SFS = Constraint(zone, rule=Average_failure_SFS_rule)
        
        def SFS_rule(SI, z):  
            if z == 'Z0':
                return SI.U_z[z] == 0
            else:
                return SI.U_z[z] == sum((SI.Z_up[k,z] * ZoneReliability.Lambda_z[k] * ZoneReliability.R_z[k]) for k in zonenosource) 
        SI.SFS = Constraint(zone, rule=SFS_rule)
    
    def EnergiaNonServita_rule(SI):    
        return SI.ENS_PRE == sum(PDz[z]*SI.U_z[z] for z in zone)
    SI.EnergiaNonServita = Constraint(rule=EnergiaNonServita_rule)
    
    def SAIDI_definition_rule(SI):
        return SI.SAIDI_PRE == sum(ZoneReliability.Customers[z] * SI.U_z[z] for z in zone)/sum(ZoneReliability.Customers)
    SI.SAIDI_definition = Constraint(rule = SAIDI_definition_rule)
    
    def SAIFI_definition_rule(SI):
        return SI.SAIFI_PRE == sum(ZoneReliability.Customers[z] * SI.lamb_z[z] for z in zone)/sum(ZoneReliability.Customers)
    SI.SAIFI_definition = Constraint(rule = SAIFI_definition_rule)
    
    def ObjectiveFunctionSI_rule(SI):
        return sum(SI.w_mk[m,k] for m in zonenosource for k in zonenosource) + sum(SI.Z_up[m,k] for m in zonenosource for k in zonenosource)
    SI.ObjectiveFunctionSI = Objective(rule=ObjectiveFunctionSI_rule)
    
    # RISOLUZIONE ONR STATO INIZIALE:
    # solver = SolverFactory('glpk') 
    solver = SolverFactory('gurobi') 
    # solver = SolverFactory("gurobi", solver_io="python")
    
    # Impostazioni del solver Gurobi:
    # solver.options['IterationLimit'] = 2000
    # solver.options['TimeLimit'] = 600
    solver.options['mipgap'] = 0.5 
    # solver.options['Heuristics'] = 0
    
    SIresults = solver.solve(SI,tee=False)
    SI.solutions.load_from(SIresults)
    
    # SI.display()  
    
    if SIresults.solver.termination_condition == TerminationCondition.optimal:
        print("SI è stato risolto con successo e tutti i vincoli sono rispettati!")
        SI.solutions.load_from(SIresults)
        # SI.display()  
        
        # RISULTATI ONR - STATO INIZIALE:
        ObjF_SI = value(SI.ObjectiveFunctionSI)
           
    elif SIresults.solver.termination_condition == TerminationCondition.infeasible:
        print("SI è irrealizzabile, alcuni vincoli non sono rispettati.")
        sys.exit()
    else:
        print("Il solver ha terminato con uno stato diverso da 'ottimale', è bene verificare il modello e i vincoli.")  
    print('')
    
    f_ijk_PRE = SI.fzs.extract_values()
    f_zs_PRE = SI.fs.extract_values()
    x_ij_PRE = SI.x_ij.extract_values()
    Z_PRE = SI.Z_up.extract_values()
    w_PRE = SI.w_mk.extract_values()
    w_i_PRE = SI.Z_f.extract_values()
    
    # print(value(SI.U_z['Z28']))
    # print(value(SI.U_z['Z29']))
    # print(value(SI.U_z['Z30']))
    # print(value(SI.U_z['Z31']))
    # print(value(SI.U_z['Z32']))
    # print(value(SI.U_z['Z33']))
    # print(value(SI.U_z['Z34']))
    # print(value(SI.U_z['Z35']))
    # print(value(SI.U_z['Z36']))
    # print(value(SI.U_z['Z37']))
    # print(value(SI.U_z['Z38']))
    
    SI_ReliabilityIndices.loc[tec,'ENS'] = value(SI.ENS_PRE)
    SI_ReliabilityIndices.loc[tec,'SAIDI'] = value(SI.SAIDI_PRE)
    SI_ReliabilityIndices.loc[tec,'SAIFI'] = value(SI.SAIFI_PRE)
    
    # Per lo stato iniziale normalizzo gli indici rispetto a FRG (che è il caso peggiore):
    SI_ReliabilityIndices_Normalized.loc[tec,'ENS'] = (1/3)*value(SI.ENS_PRE)/SI_ReliabilityIndices.loc['FRG','ENS']
    SI_ReliabilityIndices_Normalized.loc[tec,'SAIDI'] = (1/3)*value(SI.SAIDI_PRE)/SI_ReliabilityIndices.loc['FRG','SAIDI']
    SI_ReliabilityIndices_Normalized.loc[tec,'SAIFI'] = (1/3)*value(SI.SAIFI_PRE)/SI_ReliabilityIndices.loc['FRG','SAIFI']
                                               
print('INDICI DI RELIABILITY ALLO STATO INIZIALE:')
print(round(SI_ReliabilityIndices,4))
print('')
print('INDICI DI RELIABILITY ALLO STATO INIZIALE - Valori normalizzati rispetto a FRG:')
print(round(SI_ReliabilityIndices_Normalized,4))
print('')

#%% ## CONCRETE OPTIMIZATION MODEL 2 - OPTIMAL NETWORK RECONFIGURATION ##

cycles=1
cycles_opt=input('vuoi eseguire tutte le tecniche?: ')
if cycles_opt=='y':
   # QUESTO SERVE SOLAMENTE PER PLOTTAREI GRAFICI DI CONFRONTO DEGLI INDICI TRA LE TRE TECNICHE
   cycles=3 
   indexcycle=np.zeros((cycles,4))

for i in range(cycles):
    input_optimization = input('> Eseguire ONR? (y/n):'); print('')
    if input_optimization.lower() != 'y':
        sys.exit()
            
    # Decido se applicare FRG - FNC - SFS:
    choice = input('>> Per eseguire FRG, digitare: a\n>> Per eseguire FNC, digitare: b\n>> Per eseguire SFS, digitare: c\n>> Scelta: ')
    
    if choice == 'a':
        print(''); print('Eseguo FRG...'); print('')
    if choice == 'b':
        print(''); print('Eseguo FNC...'); print('')
    if choice == 'c':
        print(''); print('Eseguo SFS...'); print('')
        
    # Creazione del modello:
    ONR = ConcreteModel(name = "(Reliability Optimal Network Reconfiguration)")
    
    # VARIABILI CONTINUE
    ONR.fs = Var(zone, within=Reals) 
    ONR.fzs = Var(zone, switch, within=Reals)
    ONR.lamb_z = Var(zone, within=NonNegativeReals) 
    ONR.ENS = Var(within=NonNegativeReals) 
    ONR.U_z = Var(zone, within=NonNegativeReals)
    ONR.SAIDI_POST = Var(within=NonNegativeReals)
    ONR.SAIFI_POST = Var(within=NonNegativeReals)
    
    # VARIABILI BINARIE
    ONR.x_ij = Var(switch, within=Binary, initialize=statoinizialeswitch)
    ONR.Z_up = Var(zone, zone, within=Binary)
    # ONR.Z_up = Var(zone, zone, within=NonNegativeReals) #prova con GLPK per FRG e FNC
    ONR.w_mk = Var(zonenosource, zonenosource, within=Binary)
    ONR.Z_f = Var(zone_capo_feeder, zonenosource, zonenosource, within=Binary)
     
    # VARIABILI FISSATE (si fissano chiusi eventuali branch connessi alle "zone-foglia" e/o che creino antennizzazioni):  
    for b in BranchesToLeaves:
        if b in switch:
            ONR.x_ij[b].fix(1)
        
    # VINCOLI:
        
    def RadialityCondition_rule(ONR):
        return sum(ONR.x_ij[sw] for sw in switch) == Nzone - 1 
    ONR.RadialityCondition = Constraint(rule=RadialityCondition_rule)
    
    def FlussiArtificiali_rule(ONR,m,k):
        
        membroA = 0
        membroB = 0
        
        if m == k:
            membroB = 1
        
        for sw in switch:
            
            i = switch_zone_from_to[sw][0]
            j = switch_zone_from_to[sw][1]
                   
            if i == k:
                membroA = membroA - ONR.fzs[m,sw]
    
            if j == k:
                membroA = membroA + ONR.fzs[m,sw] 
                        
        if k == "Z0":
            membroA = membroA + ONR.fs[m]
                
        return membroA == membroB
    ONR.FlussiArtificiali = Constraint(zone,zone,rule=FlussiArtificiali_rule)
    
    def stato_flusso_ij_switch_UB_rule(ONR, sw, z): 
        return ONR.fzs[z, sw] <= ONR.x_ij[sw]
    ONR.stato_flusso_ij_switch_UB = Constraint(switch, zone, rule=stato_flusso_ij_switch_UB_rule)
    
    def stato_flusso_ij_switch_LB_rule(ONR, sw, z):
        return ONR.fzs[z, sw] >= - ONR.x_ij[sw]
    ONR.stato_flusso_ij_switch_LB = Constraint(switch, zone, rule=stato_flusso_ij_switch_LB_rule)
    
    def zona_attiva_i_UB_rule(ONR, k, sw):
        i = switch_zone_from_to[sw][0]
        return ONR.Z_up[i, k] >= ONR.fzs[k, sw] 
    ONR.zona_attiva_i_UB = Constraint(zone, switch, rule=zona_attiva_i_UB_rule)
    
    def zona_attiva_j_UB_rule(ONR,k, sw):
        j = switch_zone_from_to[sw][1]
        return ONR.Z_up[j, k] >= ONR.fzs[k, sw] 
    ONR.zona_attiva_j_UB = Constraint(zone, switch, rule=zona_attiva_j_UB_rule)
    
    def zona_attiva_i_LB_rule(ONR,k, sw):
        i = switch_zone_from_to[sw][0]
        return - ONR.Z_up[i, k] <= ONR.fzs[k, sw] 
    ONR.zona_attiva_i_LB = Constraint(zone, switch, rule=zona_attiva_i_LB_rule)
    
    def zona_attiva_j_LB_rule(ONR, k, sw):
        j = switch_zone_from_to[sw][1]
        return - ONR.Z_up[j, k] <= ONR.fzs[k, sw] 
    ONR.zona_attiva_j_LB = Constraint(zone, switch, rule=zona_attiva_j_LB_rule)
    
    if choice == 'a' or choice == 'b':
        def zona_feeder_rule(ONR, qi, m, k):
            return ONR.Z_f[qi, m, k] >= ONR.Z_up[qi, m] + ONR.Z_up[qi, k] - 1 
        ONR.zona_feeder = Constraint(zone_capo_feeder, zonenosource, zonenosource, rule=zona_feeder_rule)
        
        def Z_cug_rule(ONR, m, k):
            return ONR.w_mk[m, k] >= sum(ONR.Z_f[qi, m, k] for qi in zone_capo_feeder)
        ONR.Z_cug = Constraint(zonenosource, zonenosource, rule=Z_cug_rule)
    
    if choice == 'a':
        def Average_failure_FRG_rule(ONR, z):
            sommatoria = 0
            if z == 'Z0':  
                return ONR.lamb_z[z] == 0
            else:
                for k in zonenosource:
                    sommatoria += (ONR.w_mk[k,z]) * (ZoneReliability.Lambda_z[k])
                return ONR.lamb_z[z] == sommatoria    
        ONR.Average_failure_FRG = Constraint(zone, rule=Average_failure_FRG_rule)
    
        def FRG_rule(ONR, z):
            if z == 'Z0':
                return ONR.U_z[z] == 0
            else:       
                return ONR.U_z[z] == sum((ONR.Z_up[k,z] * ZoneReliability.Lambda_z[k] * ZoneReliability.R_z[k]) + ((ONR.w_mk[k,z] - ONR.Z_up[k,z]) * ZoneReliability.Lambda_z[k] * 0.05) for k in zonenosource)
        ONR.FRG = Constraint(zone, rule=FRG_rule)
        
    if choice == 'b':
        def Average_failure_FNC_rule(ONR, z):
            sommatoria = 0
            if z == 'Z0':  
                return ONR.lamb_z[z] == 0
            else:
                for k in zonenosource:
                    sommatoria += ((ONR.Z_up[k,z]*ZoneReliability.Lambda_z_1[k]) + (ONR.w_mk[k,z]*ZoneReliability.Lambda_z_2[k])) 
                return ONR.lamb_z[z] == sommatoria    
        ONR.Average_failure_FNC = Constraint(zone, rule=Average_failure_FNC_rule)
        
        def FNC_rule(ONR, z):
            if z == 'Z0':
                return ONR.U_z[z] == 0 
            else:
                return ONR.U_z[z] == sum((ONR.Z_up[k,z] * (ZoneReliability.Lambda_z_1[k] + ZoneReliability.Lambda_z_2[k]) * ZoneReliability.R_z[k]) + ((ONR.w_mk[k,z] - ONR.Z_up[k,z]) * ZoneReliability.Lambda_z_2[k] * 0.05) for k in zonenosource)
        ONR.FNC = Constraint(zone, rule=FNC_rule)
        
    if choice == 'c':
        def Average_failure_SFS_rule(ONR, z):
            sommatoria = 0
            if z == 'Z0':  
                return ONR.lamb_z[z] == 0
            else:
                for k in zonenosource:
                    sommatoria += (ONR.Z_up[k,z]*ZoneReliability.Lambda_z[k]) 
                return ONR.lamb_z[z] == sommatoria    
        ONR.Average_failure_SFS = Constraint(zone, rule=Average_failure_SFS_rule)
        
        def SFS_rule(ONR, z):  
            if z == 'Z0':
                return ONR.U_z[z] == 0
            else:
                return ONR.U_z[z] == sum((ONR.Z_up[k,z] * ZoneReliability.Lambda_z[k] * ZoneReliability.R_z[k]) for k in zonenosource) 
        ONR.SFS = Constraint(zone, rule=SFS_rule)
    
    def EnergiaNonServita_rule(ONR):    
        return ONR.ENS == sum(PDz[z]*ONR.U_z[z] for z in zone)
    ONR.EnergiaNonServita = Constraint(rule=EnergiaNonServita_rule)
    
    def SAIDI_definition_rule(ONR):
        return ONR.SAIDI_POST == sum(ZoneReliability.Customers[z] * ONR.U_z[z] for z in zone)/sum(ZoneReliability.Customers)
    ONR.SAIDI_definition = Constraint(rule = SAIDI_definition_rule)
    
    def SAIFI_definition_rule(ONR):
        return ONR.SAIFI_POST == sum(ZoneReliability.Customers[z] * ONR.lamb_z[z] for z in zone)/sum(ZoneReliability.Customers)
    ONR.SAIFI_definition = Constraint(rule = SAIFI_definition_rule)
    
    def ObjectiveFunctionONR_rule(ONR):
        alfa_ENS = (1/3)/SI_ReliabilityIndices.loc['FRG','ENS']
        alfa_SAIDI = (1/3)/SI_ReliabilityIndices.loc['FRG','SAIDI']
        alfa_SAIFI = (1/3)/SI_ReliabilityIndices.loc['FRG','SAIFI']
        return alfa_ENS * ONR.ENS + alfa_SAIDI * ONR.SAIDI_POST + alfa_SAIFI * ONR.SAIFI_POST
    ONR.ObjectiveFunctionONR = Objective(rule=ObjectiveFunctionONR_rule)                # Minimizzazione della funzione obiettivo
    # ONR.ObjectiveFunctionONR = Objective(rule=ObjectiveFunctionONR_rule,sense=maximize) # Massimizzazione della funzione obiettivo (caso peggiore)
    
    # RISOLUZIONE ONR:
    # solver = SolverFactory('glpk') 
    solver = SolverFactory('gurobi') 
    # solver = SolverFactory("gurobi", solver_io="python")
    
    # Impostazioni del solver Gurobi:
    # solver.options['IterationLimit'] = 2000
    # solver.options['TimeLimit'] = 300           # Gurobi
    # solver.options['tmlim'] = 300               # GLPK
    solver.options['mipgap'] = 0.1
    # solver.options['Heuristics'] = 0
    
    results = solver.solve(ONR,tee=True)
    ONR.solutions.load_from(results)
    # SI.display()  
    
    if results.solver.termination_condition == TerminationCondition.optimal:
        print("ONR è stato risolto con successo e tutti i vincoli sono rispettati!")
        ONR.solutions.load_from(results)
        # ONR.display()  
        
        # RISULTATI ONR - STATO FINALE:
        ObjF_ONR = value(ONR.ObjectiveFunctionONR)
           
    elif results.solver.termination_condition == TerminationCondition.infeasible:
        print("ONR è irrealizzabile, alcuni vincoli non sono rispettati.")
        sys.exit()
    else:
        print("Il solver ha terminato con uno stato diverso da 'ottimale', è bene verificare il modello e i vincoli.")  
    print('')
    
    print('INDICI DI RELIABILITY NELLA CONFIGURAZIONE FINALE:')
    print('ENS =',round(value(ONR.ENS),4))
    print('SAIDI =',round(value(ONR.SAIDI_POST),4))
    print('SAIFI =',round(value(ONR.SAIFI_POST),4))
    print(''); print('FUNZIONE OBIETTIVO ONR:',round(ObjF_ONR,4)); print('')
    
    ENS_POST = value(ONR.ENS); SAIDI_POST = value(ONR.SAIDI_POST); SAIFI_POST = value(ONR.SAIFI_POST)
    print(ENS_POST ,SAIDI_POST, SAIFI_POST)
    if cycles==3:
        indexcycle[i,0]=ENS_POST
        indexcycle[i,1]=SAIDI_POST
        indexcycle[i,2]=SAIFI_POST
        indexcycle[i,3]=ObjF_ONR

# il ciclo serve solamente per il grafico di confronto tra le tre tecniche

f_ijk_POST = ONR.fzs.extract_values()
f_zs_POST = ONR.fs.extract_values()
x_ij_POST = ONR.x_ij.extract_values()
lamb_POST = ONR.lamb_z.extract_values()
U_z_POST = ONR.U_z.extract_values()
Z_POST = ONR.Z_up.extract_values()
w_POST = ONR.w_mk.extract_values()
w_i_POST = ONR.Z_f.extract_values()

df_fijk_POST = pd.DataFrame(list(f_ijk_POST.values()), index=list(f_ijk_POST.keys()), columns= ['post-ONR']) 
df_f_zs_POST = pd.DataFrame(list(f_zs_POST.values()), index=list(f_zs_POST.keys()), columns= ['post-ONR']) 
df_x_ij_POST = pd.DataFrame(list(x_ij_POST.values()), index=list(x_ij_POST.keys()), columns= ['post-ONR']) 
df_lamb_POST = pd.DataFrame(list(lamb_POST.values()), index=list(lamb_POST.keys()), columns= ['post-ONR']) 
df_U_z_POST = pd.DataFrame(list(U_z_POST.values()), index=list(U_z_POST.keys()), columns= ['post-ONR']) 
df_Z_POST = pd.DataFrame(list(Z_POST.values()), index=list(Z_POST.keys()), columns= ['post-ONR']) 
df_w_POST = pd.DataFrame(list(w_POST.values()), index=list(w_POST.keys()), columns= ['post-ONR'])  
df_w_i_POST = pd.DataFrame(list(w_i_POST.values()), index=list(w_i_POST.keys()), columns= ['post-ONR']) 

# Vedo come cambia la topologia della rete a seguito della ONR:
statofinaleswitch = {(sw):round(value(ONR.x_ij[sw])) for sw in switch}
switch_aperti_ONR = sum(1 for valore in statofinaleswitch.values() if valore == 0)
switch_chiusi_ONR = sum(1 for valore in statofinaleswitch.values() if valore == 1)
transizioni_da_0_a_1 = 0
transizioni_da_1_a_0 = 0
switch_rimasti_a_0 = 0
switch_rimasti_a_1 = 0
for sw, stato_iniziale in statoinizialeswitch.items():
    stato_finale = statofinaleswitch[sw]
    
    # Valuto le transizioni:
    if stato_iniziale == 0 and stato_finale == 1:
        transizioni_da_0_a_1 += 1
    elif stato_iniziale == 1 and stato_finale == 0:
        transizioni_da_1_a_0 += 1
    
    # Valuto gli switch rimasti a 0 o 1:
    if stato_iniziale == 0 and stato_finale == 0:
        switch_rimasti_a_0 += 1
    elif stato_iniziale == 1 and stato_finale == 1:
        switch_rimasti_a_1 += 1
print('N° switch aperti:',switch_aperti_ONR)
print('N° switch chiusi:',switch_chiusi_ONR)
print("N° switch 0 -> 1:", transizioni_da_0_a_1)
print("N° switch 1 -> 0:", transizioni_da_1_a_0)
print("N° switch rimasti aperti:", switch_rimasti_a_0)
print("N° switch rimasti chiusi:", switch_rimasti_a_1)
                  
# Creazione del grafo zonale associato alla rete e verifica della connettività dopo ONR:
NX_ZonalGraph_ONR = nx.Graph()  
NX_ZonalGraph_ONR.add_nodes_from(zone)
for sw in switch:
    if statofinaleswitch[sw] == 1:
        i,j = switch_zone_from_to[sw]
        NX_ZonalGraph_ONR.add_edge(i,j)
print('Il grafo zonale ha',nx.number_of_nodes(NX_ZonalGraph_ONR),'nodi e',nx.number_of_edges(NX_ZonalGraph_ONR),'rami connessi.')
# Connectivity Check:
is_connected = nx.is_connected(NX_ZonalGraph_ONR)
print(f'La rete è ancora connessa? {is_connected}')
# Impostazioni per la figura:
plt.figure(1, figsize=(18,12))
# pos = nx.drawing.nx_pydot.graphviz_layout(NX_ZonalGraph, prog='dot', root=zone[0])
# pos = nx.drawing.nx_agraph.graphviz_layout(NX_ZonalGraph, prog='dot', root=zone[0])
pos = nx.kamada_kawai_layout(NX_ZonalGraph_ONR)
node_border_colors = 'black'
node_fill_colors = ['lightblue' if node == 'Z0' else 'lightgreen' if node in zone_capo_feeder else 'white' for node in NX_ZonalGraph_ONR.nodes()]
nx.draw(NX_ZonalGraph_ONR, pos, with_labels=True, font_weight='bold', node_size=400, node_color=node_fill_colors, edgecolors=node_border_colors, font_color='black', font_size=8)
plt.axis('off')
plt.show()

# Rappresentazione del grafo orientato zonale con graphviz:
if choice == 'a':
    ZonalGraph2 = graphviz.Digraph(comment='Distribution Network Zonal Graph - ONR Topology - FRG')  
if choice == 'b':
    ZonalGraph2 = graphviz.Digraph(comment='Distribution Network Zonal Graph - ONR Topology - FNC')        
if choice == 'c':
    ZonalGraph2 = graphviz.Digraph(comment='Distribution Network Zonal Graph - ONR Topology - SFS')
# Imposta le dimensioni della pagina e altre opzioni di visualizzazione:
ZonalGraph2.attr(size='8,8!', orientation='portrait', layout='dot', seed='927')
# Imposta la qualità massima per l'esportazione in formato PNG
ZonalGraph2.attr(graphattr='dpi=600')
# Imposta il font
ZonalGraph.attr(fontname='Times New Roman')
# Costruzione del grafo:
for z in range(len(zone)):
    if zone[z] == 'Z0':
        ZonalGraph2.node(str(z), label=f'{z}', shape='circle', color='black', fillcolor='deepskyblue', style='filled', fixedsize='true', width='0.3', height='0.3', fontsize='14', pos='c', penwidth='1.0')
    elif zone[z] in zone_capo_feeder:
        ZonalGraph2.node(str(z), label=f'{z}', shape='circle', color='black', fillcolor='green', style='filled', fixedsize='true', width='0.3', height='0.3', fontsize='14', pos='c', penwidth='1.0')
    else:
        ZonalGraph2.node(str(z), label=f'{z}', shape='circle', color='black', fillcolor='white', style='filled', fixedsize='true', width='0.3', height='0.3', fontsize='14', pos='c', penwidth='1.0')
for sw in range(len(switch)):
    z_fr = zone.index(switch_zone_from_to[switch[sw]][0])
    z_to = zone.index(switch_zone_from_to[switch[sw]][1])
    if statoinizialeswitch[switch[sw]] == 1 and statofinaleswitch[switch[sw]] == 1:
        ZonalGraph2.edge(str(z_fr), str(z_to), color='black', constraint='true')  
    if statoinizialeswitch[switch[sw]] == 1 and statofinaleswitch[switch[sw]] == 0:
        ZonalGraph2.edge(str(z_fr), str(z_to), color='red', style='dashed', constraint='true') 
    if statoinizialeswitch[switch[sw]] == 0 and statofinaleswitch[switch[sw]] == 1:
        ZonalGraph2.edge(str(z_fr), str(z_to), color='darkblue', constraint='true')        
# Visualizzazione:
if choice == 'a':
    ZonalGraph2.render(filename='Distribution Network Zonal Graph - ONR Topology - FRG', format='png', cleanup=True)
if choice == 'b':
    ZonalGraph2.render(filename='Distribution Network Zonal Graph - ONR Topology - FNC', format='png', cleanup=True)     
if choice == 'c':
    ZonalGraph2.render(filename='Distribution Network Zonal Graph - ONR Topology - SFS', format='png', cleanup=True)
ZonalGraph2.view()

# Rappresentazione del grafo orientato zonale con graphviz:
if choice == 'a':
    ZonalGraph2 = graphviz.Digraph(comment='Distribution Network Zonal Graph - ONR Topology - FRG')  
if choice == 'b':
    ZonalGraph2 = graphviz.Digraph(comment='Distribution Network Zonal Graph - ONR Topology - FNC')        
if choice == 'c':
    ZonalGraph2 = graphviz.Digraph(comment='Distribution Network Zonal Graph - ONR Topology - SFS')
# Imposta le dimensioni della pagina e altre opzioni di visualizzazione:
ZonalGraph2.attr(size='8,8!', orientation='portrait', layout='dot', seed='927')
# Imposta la qualità massima per l'esportazione in formato PNG
ZonalGraph2.attr(graphattr='dpi=600')
# Imposta il font
ZonalGraph.attr(fontname='Times New Roman')
# Costruzione del grafo:
for z in range(len(zone)):
    if zone[z] == 'Z0':
        ZonalGraph2.node(str(z), label=f'{z}', shape='circle', color='black', fillcolor='deepskyblue', style='filled', fixedsize='true', width='0.3', height='0.3', fontsize='14', pos='c', penwidth='1.0')
    elif zone[z] in zone_capo_feeder:
        ZonalGraph2.node(str(z), label=f'{z}', shape='circle', color='black', fillcolor='green', style='filled', fixedsize='true', width='0.3', height='0.3', fontsize='14', pos='c', penwidth='1.0')
    else:
        ZonalGraph2.node(str(z), label=f'{z}', shape='circle', color='black', fillcolor='white', style='filled', fixedsize='true', width='0.3', height='0.3', fontsize='14', pos='c', penwidth='1.0')
for sw in range(len(switch)):
    z_fr = zone.index(switch_zone_from_to[switch[sw]][0])
    z_to = zone.index(switch_zone_from_to[switch[sw]][1])
    if statoinizialeswitch[switch[sw]] == 1 and statofinaleswitch[switch[sw]] == 1:
        ZonalGraph2.edge(str(z_fr), str(z_to), color='black', constraint='true')  
    # if statoinizialeswitch[switch[sw]] == 1 and statofinaleswitch[switch[sw]] == 0:
    #     ZonalGraph2.edge(str(z_fr), str(z_to), color='red', style='dashed', constraint='true') 
    if statoinizialeswitch[switch[sw]] == 0 and statofinaleswitch[switch[sw]] == 1:
        ZonalGraph2.edge(str(z_fr), str(z_to), color='black', constraint='true')        
# Visualizzazione:
if choice == 'a':
    ZonalGraph2.render(filename='Distribution Network Zonal Graph - ONR Topology - FRG', format='png', cleanup=True)
if choice == 'b':
    ZonalGraph2.render(filename='Distribution Network Zonal Graph - ONR Topology - FNC', format='png', cleanup=True)     
if choice == 'c':
    ZonalGraph2.render(filename='Distribution Network Zonal Graph - ONR Topology - SFS', format='png', cleanup=True)
ZonalGraph2.view()

#%% PLOTS:
    
# Domanda di carico zonale e numero di clienti:
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(20, 10))
ax1.bar(zone, PDz.values())
ax1.set_xticks(np.arange(len(zone)))
ax1.set_xticklabels(list(range(0, len(zone))))
ax1.set_xlim(-0.5, len(zone) - 0.5)
ax1.set_xlabel("Zones", fontsize=14)
ax1.set_ylabel("Active power load demand [kW]", fontsize=14)
ax2.bar(zone, ZoneReliability.Customers, color='darkorange')
ax2.set_xticks(np.arange(len(zone)))
ax2.set_xticklabels(list(range(0, len(zone))))
ax2.set_xlim(-0.5, len(zone) - 0.5)
ax2.set_xlabel("Zones", fontsize=14)
ax2.set_ylabel("N° of customers", fontsize=14)
plt.tight_layout()
plt.show()

# Tasso di guasto e tasso di riparazione zonali:
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(20, 10))
ax1.bar(zone, ZoneReliability.Lambda_z, color='forestgreen')
ax1.set_xticks(np.arange(len(zone)))
ax1.set_xticklabels(list(range(0, len(zone))))
ax1.set_xlim(-0.5, len(zone) - 0.5)
ax1.set_xlabel("Zones", fontsize=14)
ax1.set_ylabel("Failure rate [faults/year]", fontsize=14)
ax2.bar(zone, ZoneReliability.R_z, color='red')
ax2.set_xticks(np.arange(len(zone)))
ax2.set_xticklabels(list(range(0, len(zone))))
ax2.set_xlim(-0.5, len(zone) - 0.5)
ax2.set_xlabel("Zones", fontsize=14)
ax2.set_ylabel("Restoration time [h]", fontsize=14)
plt.tight_layout()
plt.show()
        

from matplotlib.ticker import ScalarFormatter
 
labels = ['ENS', 'SAIDI', 'SAIFI']

if choice=='a':
    x=0
if choice=='b':
    x=1
if choice=='c':
    x=2

o=SI_ReliabilityIndices.values
oo=SI_ReliabilityIndices_Normalized.values

objf_pre=sum(oo[x,:])
objf_post=ENS_POST/o[x,0]*oo[x,0]+ SAIDI_POST/o[x,1]*oo[x,1] + SAIFI_POST/o[x,2]*oo[x,2]

values_post = [(ENS_POST/o[x,0])*oo[x,0], (SAIDI_POST/o[x,1])*oo[x,1], (SAIFI_POST/o[x,2])*oo[x,2],objf_post]
values_init = [oo[x,0],oo[x,1],oo[x,2],objf_pre]

indici = ['EENS[kwh/year]', 'SAIDI[hours/year]', 'SAIFI[faults/year]','F.OBJ [adim]']

bar_width = 0.2
gap = 0.02  # Spazio tra le barre dello stesso gruppo
group_gap = 0.3  # Spazio tra i diversi gruppi di barre

# Genera la posizione delle barre
r1 = np.arange(len(values_post)) * (2 * bar_width + group_gap)
r2 = [x + bar_width + gap for x in r1]

plt.figure(3, figsize=(10, 6))

# Crea le barre per i valori post e init
plt.bar(r1, values_init, width=bar_width, color='#FF7F50', edgecolor='black', label='Pre')
plt.bar(r2, values_post, width=bar_width, color='#FFA07A', edgecolor='black', label='Post')

plt.title('ONR index comparison (Normalized)', fontsize=18)

# Aggiunge le etichette alle posizioni corrette
plt.xticks([r + bar_width/2 + gap/2 for r in r1], indici)

# Aggiunge la legenda
plt.legend()

# Configura l'asse y per visualizzare i numeri in notazione scientifica
formatter = ScalarFormatter()
formatter.set_scientific(True)
formatter.set_powerlimits((0, 3))
plt.gca().yaxis.set_major_formatter(formatter)

# Aggiusta il numero di tick sull'asse y
plt.locator_params(axis='y', nbins=15)

# Mostra il grafico
plt.show()



if cycles==3:
    
    #  grafici paper
    
    objf_pre_norm=np.zeros((3,1))
    for i in range(3):
        objf_pre_norm[i,0]=sum(oo[i,:])
    
    indici = ['FRG', 'FNC', 'SFS']
    
    bar_width = 0.2
    gap = 0.02  # Spazio tra le barre dello stesso gruppo
    group_gap = 0.3  # Spazio tra i diversi gruppi di barre
    
    # Genera la posizione delle barre
    r1 = np.arange(len(o[:,0])) * (2 * bar_width + group_gap)
    r2 = [x + bar_width + gap for x in r1]
    
    plt.figure(3, figsize=(10, 6))
    
    # Crea le barre per i valori post e init
    plt.bar(r1,  o[:,0], width=bar_width, color='#FF7F50', edgecolor='black', label='Pre')
    plt.bar(r2, indexcycle[:,0], width=bar_width, color='#FFA07A', edgecolor='black', label='Post')
    
    plt.title('EENS index comparison', fontsize=18)
    plt.ylabel('EENS [kWh/year]')
    # Aggiunge le etichette alle posizioni corrette
    plt.xticks([r + bar_width/2 + gap/2 for r in r1], indici)
    
    # Aggiunge la legenda
    plt.legend()
    
    # Configura l'asse y per visualizzare i numeri in notazione scientifica
    formatter = ScalarFormatter()
    formatter.set_scientific(True)
    formatter.set_powerlimits((0, 3))
    plt.gca().yaxis.set_major_formatter(formatter)
    
    # Aggiusta il numero di tick sull'asse y
    plt.locator_params(axis='y', nbins=15)
    
    # Mostra il grafico
    plt.show()


    bar_width = 0.2
    gap = 0.02  # Spazio tra le barre dello stesso gruppo
    group_gap = 0.3  # Spazio tra i diversi gruppi di barre
    
    # Genera la posizione delle barre
    r1 = np.arange(len(o[:,1])) * (2 * bar_width + group_gap)
    r2 = [x + bar_width + gap for x in r1]
    
    plt.figure(3, figsize=(10, 6))
    
    # Crea le barre per i valori post e init
    plt.bar(r1,  o[:,1], width=bar_width, color='#FF7F50', edgecolor='black', label='Pre')
    plt.bar(r2, indexcycle[:,1], width=bar_width, color='#FFA07A', edgecolor='black', label='Post')
    
    plt.title('SAIDI index comparison', fontsize=18)
    plt.ylabel('SAIDI [h/year]')
    # Aggiunge le etichette alle posizioni corrette
    plt.xticks([r + bar_width/2 + gap/2 for r in r1], indici)
    
    # Aggiunge la legenda
    plt.legend()
    
    # Configura l'asse y per visualizzare i numeri in notazione scientifica
    formatter = ScalarFormatter()
    formatter.set_scientific(True)
    formatter.set_powerlimits((0, 3))
    plt.gca().yaxis.set_major_formatter(formatter)
    
    # Aggiusta il numero di tick sull'asse y
    plt.locator_params(axis='y', nbins=15)
    
    # Mostra il grafico
    plt.show()

    bar_width = 0.2
    gap = 0.02  # Spazio tra le barre dello stesso gruppo
    group_gap = 0.3  # Spazio tra i diversi gruppi di barre
    
    # Genera la posizione delle barre
    r1 = np.arange(len(o[:,2])) * (2 * bar_width + group_gap)
    r2 = [x + bar_width + gap for x in r1]
    
    plt.figure(3, figsize=(10, 6))
    
    # Crea le barre per i valori post e init
    plt.bar(r1,  o[:,2], width=bar_width, color='#FF7F50', edgecolor='black', label='Pre')
    plt.bar(r2, indexcycle[:,2], width=bar_width, color='#FFA07A', edgecolor='black', label='Post')
    
    plt.title('SAIFI index comparison', fontsize=18)
    plt.ylabel('SAIFI [faults/year]')
    # Aggiunge le etichette alle posizioni corrette
    plt.xticks([r + bar_width/2 + gap/2 for r in r1], indici)
    
    # Aggiunge la legenda
    plt.legend()
    
    # Configura l'asse y per visualizzare i numeri in notazione scientifica
    formatter = ScalarFormatter()
    formatter.set_scientific(True)
    formatter.set_powerlimits((0, 3))
    plt.gca().yaxis.set_major_formatter(formatter)
    
    # Aggiusta il numero di tick sull'asse y
    plt.locator_params(axis='y', nbins=15)
    
    # Mostra il grafico
    plt.show()

    bar_width = 0.2
    gap = 0.02  # Spazio tra le barre dello stesso gruppo
    group_gap = 0.3  # Spazio tra i diversi gruppi di barre
    
    # Genera la posizione delle barre
    r1 = np.arange(len(o[:,2])) * (2 * bar_width + group_gap)
    r2 = [x + bar_width + gap for x in r1]
    
    plt.figure(3, figsize=(10, 6))
    
    # Crea le barre per i valori post e init
    plt.bar(r1, objf_pre_norm[:,0], width=bar_width, color='#FF7F50', edgecolor='black', label='Pre')
    plt.bar(r2, indexcycle[:,3], width=bar_width, color='#FFA07A', edgecolor='black', label='Post')
    
    plt.title('Objective function index comparison (Normalized)', fontsize=18)
    plt.ylabel('Objective function')
    # Aggiunge le etichette alle posizioni corrette
    plt.xticks([r + bar_width/2 + gap/2 for r in r1], indici)
    
    # Aggiunge la legenda
    plt.legend()
    
    # Configura l'asse y per visualizzare i numeri in notazione scientifica
    formatter = ScalarFormatter()
    formatter.set_scientific(True)
    formatter.set_powerlimits((0, 3))
    plt.gca().yaxis.set_major_formatter(formatter)
    
    # Aggiusta il numero di tick sull'asse y
    plt.locator_params(axis='y', nbins=15)
    
    # Mostra il grafico
    plt.show()
    
    
    
# statofinaleswitch = {(s): statinizialeswitch[s] for s in switch}

# =============================================================================
# ASSEGNAZIONE STATI SWITCH SU OPENDSS DOPO ONR
# =============================================================================

for s in switch:
    dssCircuit.SetActiveElement(s)
    if statofinaleswitch[s] == 0:
            dssElem.Open(2, 0)
            # statofinaleswitch[s] = 0
    else:
        dssElem.Close(2,0)
        # statofinaleswitch[s] = 1

# =============================================================================
# LOAD FLOW POST ONR
# =============================================================================

dssSolution.Solve()

# Trovo le potenze attive e reattive dei vari elementi e le correnti delle linee

P_slack_pre = {}
Q_slack_pre = {}

P_gen = {}
Q_gen = {}

P_loads = {}
Q_loads = {}

P_linee_busfrom = {}
P_linee_busto = {}
Q_linee_busfrom = {}
Q_linee_busto = {}
Perdite_linee_kw = {}
Perdite_linee_kvar = {}
Correnti_linee_modulo = {}
Portata_linee = {}
Sijmax = {}  #portata dei branches in KVA

P_trafi_busfrom = {}
P_trafi_busto = {}
Q_trafi_busfrom = {}
Q_trafi_busto = {}
Perdite_trafi_kw = {}
Perdite_trafi_kvar = {}

P_switch_busfrom = {}
P_switch_busto = {}
Q_switch_busfrom = {}
Q_switch_busto = {}
Perdite_switch_kw = {}
Perdite_switch_kvar = {}


for m in dssCircuit.AllElementNames:
    dssCircuit.SetActiveElement(m)
    P = dssElem.Powers
    Losses = dssElem.Losses
    Correnti = dssElem.CurrentsMagAng
    if m.startswith('Vsource'):
        P_slack_pre[m] = -(P[0]+P[2]+P[4])
        Q_slack_pre[m] = -(P[1]+P[3]+P[5])
    elif m.startswith('Line'):
        if m in switch:
            Normalamps = dssLines.NormAmps
            P_switch_busfrom[m] = P[0]+ P[2]+P[4]
            P_switch_busto[m] =  P[6]+P[8]+P[10]
            Q_switch_busfrom[m] =  P[1]+P[3]+P[5]
            Q_switch_busto[m] = P[7]+P[9]+P[11]
            Perdite_switch_kw[m] = Losses[0]/1000
            Perdite_switch_kvar[m] = Losses[1]/1000
            Correnti_linee_modulo[m] = Correnti[0]
            Portata_linee[m] = Normalamps
        else:
            Normalamps = dssLines.NormAmps
            P_linee_busfrom[m] = P[0]+ P[2]+P[4]
            P_linee_busto[m] =  P[6]+P[8]+P[10]
            Q_linee_busfrom[m] =  P[1]+P[3]+P[5]
            Q_linee_busto[m] = P[7]+P[9]+P[11]
            Perdite_linee_kw[m] = Losses[0]/1000
            Perdite_linee_kvar[m] = Losses[1]/1000
            Correnti_linee_modulo[m] = Correnti[0]
            Portata_linee[m] = Normalamps
    elif  m.startswith('Transformer'):
          P_trafi_busfrom[m] = P[0]+ P[2]+P[4]
          P_trafi_busto[m] =  P[8]+P[10]+P[12]
          Q_trafi_busfrom[m] =  P[1]+P[3]+P[5]
          Q_trafi_busto[m] = P[9]+P[11]+P[13] 
          Perdite_trafi_kw[m] = Losses[0]/1000
          Perdite_trafi_kvar[m] = Losses[1]/1000         
    elif    m.startswith('Load'):
            P_loads[m] = P[0]+P[2]+P[4]
            Q_loads[m] = P[1]+P[3]+P[5]
    elif m.startswith('Generator'): 
         P_gen[m]= -(P[0]+P[2]+P[4])
         Q_gen[m]= (P[1]+P[3]+P[5])


perdite_totali_kw_pre = dssCircuit.Losses[0]/1000 
perdite_totali_kvar_pre = dssCircuit.Losses[1]/1000 

# Tensioni base
Vnbus = {}  #kv
for b in buses:
    if b == 'sourcebus' or b=='bus_n1' or b=='bus_n2':
       Vnbus[b] = 150
    else:
        Vnbus[b] = 20

if len(P_gen) == 0:
    print("Non ci sono generatori")
    P_gen = 0
    Q_gen = 0                

print(''); print('Analisi delle potenze (ACLF) con la topologia finale:')
print('')    
# print('Generazione:',round(sum(P_gen.values()),2), 'KW', ';', round(sum(Q_gen.values()),2),'Kvar')
print('Carico:',round(sum(P_loads.values()),2) , 'KW', ';', round(sum(Q_loads.values()),2),'Kvar') 
print('Slack Bus active power:',round(sum(P_slack_pre.values()),2) , 'KW')
print('Slack Bus reactive power:',round(sum(Q_slack_pre.values()),2) , 'Kvar')
print('Active power losses:',round(perdite_totali_kw_pre,2) , 'KW' )
print('Reactive power losses:',round(perdite_totali_kvar_pre,2) , 'Kvar' )
print('')


# Trovo le tensioni sui bus in modulo e fase e verifico se violano qualche limite
    
tensioni_bus_modulo = {}
theta0 = {}  #in rad
for b in buses:
    dssCircuit.SetActiveBus(b)
    myVolt = dssActiveBus.VMagAngle
    tensioni_bus_modulo[b] = myVolt[0]/1000
    theta0[b] = myVolt[1]*pi/180

# Modulo della tensione concatenata in p.u.:    
V1= {} 

for a,b in tensioni_bus_modulo.items():
    if a == 'sourcebus' or a =='bus_n1' or a =='bus_n2':
        V1[a] = b*sqrt(3)/150
    else:
        V1[a] = b*sqrt(3)/20

# Ricavo la portata dei branches in KVA:
Sijmax = {(b):0 for b in branches}
Sijpost = {(b):0 for b in branches}

for b in branches:
    if b in linee or b in switch:
        Sijmax[b] = round(Vnbus[busfrom[b]]*Portata_linee[b],2)
        Sijpost[b] = round(sqrt(3)*tensioni_bus_modulo[busfrom[b]]*Correnti_linee_modulo[b],2)
    else:
        Sijmax[b] = Sn[b]

Vmax=1.05
Vmin=0.95

violazioni_tensioni = {}
for a,b in V1.items():
    if b<=Vmin or b>=Vmax:
        print('Violazione di tensione sul nodo',a ,'- Vi =',round(b,4),'p.u.')
        violazioni_tensioni[a] = b
print('')          
        

# Controllo se ci sono linee in sovraccarico:

sovraccarichi_finali ={}
for b in linee:   
  if  Correnti_linee_modulo[b] > Portata_linee[b]:
     print(b, 'in sovraccarico:',round((Correnti_linee_modulo[b]/ Portata_linee[b])*100,0), '%')
     sovraccarichi_finali[b] = round((Correnti_linee_modulo[b]/ Portata_linee[b])*100,0)
print('')


# Modulo delle tensioni in pu
plt.figure(3, figsize=(15, 6))
plt.axhline(1, color='black', linestyle='--', linewidth=1)
plt.plot(buses, V0.values(), linewidth=0.5, marker='o', markersize=1, color='dodgerblue', label='Pre ONR')
plt.plot(buses, V1.values(), linewidth=1, marker='o',markersize=1, color='orange', label='ONR risultati')
# plt.plot(buses, Vi.values(), linewidth=1, marker='o',markersize=1, color='forestgreen', label='Post ONR')
plt.plot('sourcebus',V0['sourcebus'], marker='D', markersize=5, color='red',label='Slack Bus')
plt.axhline(Vmax, color='red', linestyle='--', linewidth=1, label='$V_{\\mathrm{max}}$' )
plt.axhline(Vmin, color='blue', linestyle='--', linewidth=1, label='$V_{\\mathrm{min}}$')
plt.ylim(0.85, 1.2)
plt.xticks([]) 
plt.xlabel('Nodi', fontsize=20 )
plt.ylabel(r'$V_{i} \, [\mathrm{pu}]$', fontsize=20)
plt.legend(loc='best', fontsize=12,  frameon=False, ncol=2)
plt.show()

# # Flussi di potenza apparente sui branches che erano sovraccarico after ONR: 
plt.figure(4, figsize=(15, 6))
for b in Sij_plot.keys():
    plt.bar(b, Sijmax[b], linewidth=1, color='salmon')
    plt.stem(b, Sijpre[b], linefmt='darkred', markerfmt='v', basefmt=' ')
    plt.stem(b, Sijpost[b], linefmt='blue', markerfmt='o', basefmt=' ', label='$S_{ij}$') 
plt.xticks(range(0, len(Sij_plot.keys())),[f'{br} ' for br in Sij_plot.keys()], rotation=45)
plt.xlabel('Rami in sovraccarico pre e post ONR', fontsize=15)
plt.ylabel(r'$S_{ij} \, [\mathrm{kVA}]$', fontsize=15)
legend_elements = [Line2D([0], [0], color='salmon', linewidth=10,  label=r'$S_{ij}^{max}$'), Line2D([0], [0], color='darkred', marker='v', linestyle='None',  label=r'$S_{ij}^{pre}$'), Line2D([0], [0], color='blue', marker='o', linestyle='None',  label=r'$S_{ij}^{post}$')]
plt.legend(handles=legend_elements,fontsize=12)
plt.show()  
 

# Flussi di potenza apparente su eventuali nuovi branches in sovraccarico after ONR: 
Sij_post_plot = {}
for b in linee+trafi:
    if Sijpost[b] > Sijmax[b]:
        Sij_post_plot[b] = Sijpost[b]                  
plt.figure(4, figsize=(10, 6))
for b in Sij_post_plot.keys():
    plt.bar(b, Sijmax[b], linewidth=1, color='salmon')
    plt.stem(b, Sijpost[b], linefmt='darkred', markerfmt='v', basefmt=' ')    
plt.xticks(range(0, len(Sij_post_plot.keys())),[f'{br} ' for br in Sij_post_plot.keys()], rotation=45)
plt.xlabel('Nuovi branches in sovraccarico', fontsize=10, fontweight='bold')
plt.ylabel(r'$\mathbf{S_{ij} [kVA]}$', fontsize=10)
legend_elements = [Line2D([0], [0], color='salmon', linewidth=10, label=r'$\mathbf{S_{ij}^{max}}$'), Line2D([0], [0], color='darkred', marker='v', linestyle='None', label=r'$\mathbf{S_{ij}^{post}}$')]
plt.legend(handles=legend_elements)
plt.show()  

# =============================================================================
# FINE PARTE LOAD FLOW POST - ONR
# =============================================================================
