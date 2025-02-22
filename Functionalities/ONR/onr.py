# %% IMPORT LIBRERIE
# =============================================================================
import matplotlib.pyplot

from variables import v, new_par_dict, mc
from opendss import OpenDSS
import sys
from math import pi, sqrt, cos, sin, tan, atan2, exp
import numpy as np
import pandas as pd
# import plotly.graph_objects as go
import networkx as nx
import graphviz
from pyomo.environ import *

# # from pyomo.core import Reals       # ,TODO da verificare
# from pyomo.environ import within
# from pyomo.opt import SolverFactory
# from pyomo.core import *
# from pyomo.gdp import *

import random
from timeit import default_timer as timer
from itertools import chain
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib import rc
from matplotlib.lines import Line2D
from matplotlib.ticker import ScalarFormatter
import copy
import os
from itertools import combinations
from collections import defaultdict
from pprint import pprint
import re
import warnings
import time
# import win32com.client
import yaml

from variables import v

import dictInitialize


class ONR:
    def __init__(self):
        self.ONR_initialize()
        self.dss = OpenDSS()
        self.indexes = dict()
        self.indexes_post = dict()
        self.filedir = 'C:/Users/anton/PycharmProjects/ARStool/Functionalities/ONR/__images__/'
        self.log_pre_grafos = ''
        self.log_pre_solver = ''
        self.log_pre_viol = ''
        self.log_post_solver = ''
        self.log_post_switch = ''
        self.log_post_viol = ''

    def ONR_PRE(self):
        # with open('C:/Users/velin/OneDrive - Politecnico di Bari/Desktop/ENEA_PORTICI_12_2024/ONR_ENEA_PORTICI_class/ENEA_PORTICI_dict_.yml', 'r') as file:
        #     v = yaml.safe_load(file)

        warnings.filterwarnings("ignore")
        pd.options.mode.chained_assignment = None

        switch = []
        bus_from_to_sw = {}
        bus_switch_from = {}
        bus_switch_to = {}
        L_km_switch = {}

        for m in v.keys():
            # dssCircuit.SetActiveElement(m)
            Nomi = m
            Bus_elemento = v[m]['top']['conn']
            if '_s' in m or '_m' in m:
                switch.append(Nomi)
                bus_from_to_sw[m] = Bus_elemento
                bus_switch_from[m] = Bus_elemento[0]
                bus_switch_to[m] = Bus_elemento[1]
                # print(m, v[m]['category'])
                # myLen = v[m]['par']['length']
                L_km_switch[m] = 0.0001

        Nswitch = len(switch)

        # Trovo i bus

        bus = []
        k = 0
        for i in v.keys():
            if v[i]['category'] == 'AC-Node':
                bus.append(i)

        # TODO: da commentare se si importa reta da DSS
        if 'sourcebus' in bus:
            bus_ultimo = bus.pop()
            bus.insert(0, bus_ultimo)

        trbus = []
        for i in v.keys():
            if v[i]['category'] == '2W-Transformer':
                bustransformer = v[i]['top']['conn']
                trbus.append(bustransformer[0])

        Nbus = len(bus)

        # Potenza base
        Sbase = 100  # Mva

        # PARAMETRI RELIABILITY DEI BUS:
        lambda_b = {}  # tasso di guasto bus
        R_b = {}  # tempo di riparazione bus
        bbbb = {}
        for i in bus:
            lambda_b[i] = 0.001129
            R_b[i] = 28
            bbbb[i] = 0

        # Trovo gli altri elementi (linee, trafi)...in partciolar modo come tassi di guasto e tempi di riparazione si è preso dal goldenbook per linee aeree: 0.014370 guasti/1000ft-anno e 5.3 ore, mentper linee in cavo: 0.003360 guasti/1000ft-anno e 16 ore. I tassi di guasto sono stati convertiti in km moltiplicati per 3(num.fasi) e i valori sono stati caricati su openDSS

        source = []
        linee = []
        trafi = []
        loads = []
        generatori = []
        slack_bus = {}
        bus_trafi = {};
        bus_trafi_from = {};
        bus_trafi_to = {}
        bus_load = {}
        bus_linee = {};
        bus_linee_from = {};
        bus_linee_to = {}
        bus_gen = {}

        L_km = {}
        R_l = {}  # tempo di riparazione linea
        lambda_l = {}  # tasso di guasto linea
        lista_ug = []

        import random

        for m in v.keys():
            Nomi = m
            Bus_elemento = v[m]['top']['conn']
            if m == 'Vsource':
                source.append(Nomi)
                slack_bus[m] = v[m]['top']['conn']
            elif m.startswith('l_'):
                if 's_' in m or '_m' in m:
                    continue
                linee.append(Nomi)
                bus_linee[m] = Bus_elemento
                bus_linee_from[m] = Bus_elemento[0]
                bus_linee_to[m] = Bus_elemento[1]
                myLen = v[m]['par']['length']
                L_km[m] = myLen
                R_l[m] = 3
                lambda_l[m] = 0.1 * L_km[m]
            elif v[m]['category'] == '2W-Transformer':
                trafi.append(Nomi)
                bus_trafi[m] = Bus_elemento
                bus_trafi_from[m] = Bus_elemento[0]
                bus_trafi_to[m] = Bus_elemento[1]
                myXHL = v[m]['par']['XHL']
            elif m.startswith('load'):
                loads.append(Nomi)
                bus_load[m] = Bus_elemento[0]
            elif m.startswith('pv'):
                generatori.append(Nomi)
                bus_gen[m] = Bus_elemento[0]

        slack_bus_lista = list(slack_bus.values())

        Nlinee = len(linee)
        Ntrafi = len(trafi)

        # Trovo tutti i branches e i busfrom e busto di ogni elemento

        branches = trafi + linee + switch
        Nbranches = len(branches)

        busfrom = dict(**bus_trafi_from, **bus_linee_from, **bus_switch_from)
        busto = dict(**bus_trafi_to, **bus_linee_to, **bus_switch_to)

        busfrom_linee_trafi = dict(**bus_trafi_from,
                                   **bus_linee_from)  # dizionari utili per la ricerca zone che contengono bus from e to di tutti i branches che non sono switch
        busto_linee_trafi = dict(**bus_trafi_to, **bus_linee_to)

        # Trovo potenze attive e reattive nominali dei generatori

        P_gen_nom = {}

        if not generatori:
            print('')
            print("Non ci sono generatori.")
            P_gen = 0
            # Q_gen = 0
        else:
            for i in v.keys():
                if i.startswith('pv'):
                    P_gen_nom[i] = v[i]['par']['P']

                    # Trovo potenze attive e reattive nominali dei carichi

        P_loads_nom = {}

        for i in v.keys():
            if i.startswith('load'):
                mykW = v[i]['par']['P']
                P_loads_nom[i] = mykW

        def calcolo_indici_reliability(zone_connesse_allo_stesso_feeder, zone_upstream, scelta):
            # Frequenze di guasto

            f_z_FRG = {}
            f_z_FRG['z0'] = 0
            for z, lista in zone_connesse_allo_stesso_feeder.items():
                somma = sum([lambda_z[elem] for elem in lista])
                f_z_FRG[z] = somma
            # print(f_z_FRG)
            f_z_FNC = {}
            f_z_FNC['z0'] = 0
            somma1 = {};
            somma2 = {}
            for z, lista in zone_connesse_allo_stesso_feeder.items():
                somma1[z] = sum(lambda_z_2[elem] for elem in lista)
            for z, lista in zone_upstream.items():
                somma2[z] = sum(lambda_z_1[elem] for elem in lista)
            for z in zonenosource:
                f_z_FNC[z] = somma1[z] + somma2[z]
            # print(f_z_FNC)

            f_z_SFS = {}
            f_z_SFS['z0'] = 0
            for z, lista in zone_upstream.items():
                somma = sum([lambda_z[elem] for elem in lista])
                f_z_SFS[z] = somma
            # print(f_z_SFS)

            # Indisponibilità

            U_z_FRG = {}
            U_z_FRG['z0'] = 0
            for z, lista in zone_connesse_allo_stesso_feeder.items():
                somma = 0  # Inizializza la somma a zero per ogni zona
                for elem in lista:
                    if elem in zone_upstream[z]:
                        somma += lambda_z[elem] * R_z[elem]
                    elif elem in zone_connesse_allo_stesso_feeder[z] and elem not in zone_upstream[z]:
                        somma += lambda_z[elem] * 0.05
                U_z_FRG[z] = somma

            U_z_FNC = {}
            U_z_FNC['z0'] = 0
            for z, lista in zone_connesse_allo_stesso_feeder.items():
                somma = 0  # Inizializza la somma a zero per ogni zona
                for elem in lista:
                    if elem in zone_upstream[z]:
                        somma += (lambda_z_1[elem] + lambda_z_2[elem]) * R_z[elem]
                    elif elem in zone_connesse_allo_stesso_feeder[z] and elem not in zone_upstream[z]:
                        somma += lambda_z_2[elem] * 0.05
                U_z_FNC[z] = somma

            U_z_SFS = {}
            U_z_SFS['z0'] = 0
            for z, lista in zone_upstream.items():
                somma = sum([lambda_z[elem] * R_z[elem] for elem in lista])
                U_z_SFS[z] = somma

            if scelta == 'a':
                ENS = sum(PDz[z] * U_z_FRG[z] for z in lista_zone)

                SAIDI = sum(num_clienti_per_zona[z] * U_z_FRG[z] for z in lista_zone) / sum(
                    list(num_clienti_per_zona.values()))

                SAIFI = sum(num_clienti_per_zona[z] * f_z_FRG[z] for z in lista_zone) / sum(
                    list(num_clienti_per_zona.values()))

            if scelta == 'b':
                ENS = sum(PDz[z] * U_z_FNC[z] for z in lista_zone)

                SAIDI = sum(num_clienti_per_zona[z] * U_z_FNC[z] for z in lista_zone) / sum(
                    list(num_clienti_per_zona.values()))

                SAIFI = sum(num_clienti_per_zona[z] * f_z_FNC[z] for z in lista_zone) / sum(
                    list(num_clienti_per_zona.values()))

            if scelta == 'c':
                ENS = sum(PDz[z] * U_z_SFS[z] for z in lista_zone)

                SAIDI = sum(num_clienti_per_zona[z] * U_z_SFS[z] for z in lista_zone) / sum(
                    list(num_clienti_per_zona.values()))

                SAIFI = sum(num_clienti_per_zona[z] * f_z_SFS[z] for z in lista_zone) / sum(
                    list(num_clienti_per_zona.values()))

            return ENS, SAIDI, SAIFI

        def calcolo_funzione_obiettivo(stati_switch, scelta, stampa_a_video=True):

            adiacenza_zone_radiale = Matrice_di_adiacenza_zone_zone2(Nzone, switch, stati_switch)

            zoneconnesse_radiali = {(z): [] for z in lista_zone}
            for i in lista_zone:
                for j in lista_zone:
                    if adiacenza_zone_radiale.loc[i, j] == 1:
                        zoneconnesse_radiali[i].append(j)

            NX_grafo_zonale_smagliato = Creazione_grafo_zonale2(lista_zone, stati_switch, stampa_a_video=False)

            #### Dizionario per memorizzare i percorsi più brevi da ciascuna zona capo feeder verso tutte le zone
            percorsi_più_brevi = {}

            # Calcola i percorsi più brevi per ciascun nodo sorgente
            for sorgente in zone_capo_feeder:
                percorsi_più_brevi[sorgente] = nx.single_source_shortest_path(NX_grafo_zonale_smagliato, sorgente)

            zone_connesse_allo_stesso_feeder = crea_dizionario_zone_connesse(zoneconnesse_radiali, zonenosource)

            # Trovo il capo feeder per ogni zona
            capo_feeder_per_zona = {}
            for chiave, zone in zone_connesse_allo_stesso_feeder.items():
                for zona in zone:
                    if zona in zone_capo_feeder:
                        capo_feeder_per_zona[chiave] = zona

            # Trovo le zone upstream

            zone_upstream = {}

            for chiave, capo_feeder in capo_feeder_per_zona.items():
                zone_upstream[chiave] = percorsi_più_brevi[capo_feeder][chiave]
                # zone_upstream[chiave].insert(0, 'z0')

            ENS, SAIDI, SAIFI = calcolo_indici_reliability(zone_connesse_allo_stesso_feeder, zone_upstream, scelta)

            # Calcolo funzione obiettivo
            alfa_ENS = (1 / 3) / ENS_PRE_FRG
            alfa_SAIDI = (1 / 3) / SAIDI_PRE_FRG
            alfa_SAIFI = (1 / 3) / SAIFI_PRE_FRG

            ObjectiveFunction = alfa_ENS * ENS + alfa_SAIDI * SAIDI + alfa_SAIFI * SAIFI  # + alfa_P_slack * P_slack['Vsource.source']

            return ObjectiveFunction, ENS, SAIDI, SAIFI

        # Definisco la funzione gaussiana per determinare il numero di clienti in maniera randomica:
        def Gaussian_Function(x, mu, sigma):
            return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

        # Fisso il seed per la riproducibilità del codice, in maniera tale da ottenere sempre gli stessi valori randomici:
        random_seed = 327  # (numero grande dispari)
        random.seed(random_seed)
        np.random.seed(random_seed)

        # Parametri della funzione gaussiana:
        mu = 1  # media
        sigma = 1 / 3  # deviazione standard

        # Creo un array di valori casuali da una distribuzione gaussiana:
        valori_randomici = np.random.normal(mu, sigma, len(loads))
        fgauss = Gaussian_Function(valori_randomici, mu, sigma)

        # Moltiplico ogni potenza attiva richiesta dal carico per il valore gaussiano corrispondente:
        g = {(d): P_loads_nom[d] * fgauss[loads.index(d)] for d in loads}

        # Imposto un valore massimo ai risultati altrimenti ottengo dei risultati anche maggiori di mille:
        valore_massimo = 60
        g = {(d): np.minimum(g[d], valore_massimo) for d in loads}

        # Normalizzo i valori in modo che la somma sia pari a 30000:
        g_normalized = {(d): 0 for d in loads}
        num_clienti_per_bus = {(d): 0 for d in loads}
        cli = 0
        for i in g.keys():
            cli = cli + g[i]
        # sum_customers = sum(g.values())
        sum_customers = cli
        for d in loads:
            if sum_customers != 0:
                g_normalized[d] = np.clip(g[d], 1, np.inf)
                scale_factor = 30000 / sum_customers
                g_normalized[d] = (g_normalized[d] * scale_factor).astype(int)
            else:
                g_normalized[d] = g[d]
            # Tronco i risultati a valori interi:
            num_clienti_per_bus[d] = np.trunc(g_normalized[d]).astype(int)

        # Trovo gli stati degli switch e dei branches che saranno inizialmente tutti chiusi

        stati_switch_iniziali = {}

        for m in v.keys():
            if '_s' in m or '_m' in m:
                v[m]['par']['out-of-service'] = False
                if v[m]['par']['out-of-service'] == False:
                    # stato = dssElem.IsOpen(2, 0)
                    # Converte True in 0 e False in 1 e assegna il valore al dizionario
                    stati_switch_iniziali[m] = 1
                else:
                    stati_switch_iniziali[m] = 1

        stati_branch_iniziali = {}
        for elem in branches:
            if elem in switch:
                stati_branch_iniziali[elem] = stati_switch_iniziali[elem]
            else:
                stati_branch_iniziali[elem] = 1

        # Matrice di adiacenza buses/buses:
        def Matrice_di_adiacenza(Nbus, branches):
            matrice_adiacenza = pd.DataFrame(np.zeros((Nbus, Nbus)), index=bus, columns=bus)
            for b in branches:
                bus1 = busfrom[b]
                bus2 = busto[b]
                matrice_adiacenza.loc[bus1, bus2] = 1 * stati_branch_iniziali[b]
                matrice_adiacenza.loc[bus2, bus1] = 1 * stati_branch_iniziali[b]
            return matrice_adiacenza

        Matrice_adiacenza = Matrice_di_adiacenza(Nbus, branches)

        # Matrice di incidenza branches/buses:
        def Matrice_di_incidenza(Nbranches, Nbus):
            matrice_incidenza = pd.DataFrame(np.zeros((Nbranches, Nbus)), index=branches, columns=bus)
            for b in branches:
                bus1 = busfrom[b]
                bus2 = busto[b]
                matrice_incidenza.loc[b, bus1] = 1 * stati_branch_iniziali[b]
                matrice_incidenza.loc[b, bus2] = -1 * stati_branch_iniziali[b]
            return matrice_incidenza

        Matrice_incidenza = Matrice_di_incidenza(Nbranches, Nbus)

        # Ricavo il set di bus connessi con ciascun bus i:
        busconnessi = {(i): [] for i in bus}
        for i in bus:
            for j in bus:
                if Matrice_adiacenza.loc[i, j] == 1:
                    busconnessi[i].append(j)

        # Ricavo il set di branches connessi a ciascun bus i:
        BranchesConnessiPerBus = {(i): [] for i in bus}
        for i in bus:
            connections = []
            for b in branches:
                if (busfrom[b] == i) or (busto[b] == i):
                    connections.append(b)
            BranchesConnessiPerBus[i] = connections

        LineeConessePerBus = {(i): [] for i in bus}
        for i in bus:
            connections = []
            for b in linee:
                if (busfrom[b] == i) or (busto[b] == i):
                    connections.append(b)
            LineeConessePerBus[i] = connections

        # Ricavo il set dei possibili "nodi foglia" e il set di linee connesse a un nodo foglia (linee non switchabili):
        LeafNodes = [];
        BranchesToLeaves = []
        for i in bus:
            if len(busconnessi[i]) == 1:
                LeafNodes.append(i)
            if len(BranchesConnessiPerBus[i]) == 1:
                BranchesToLeaves.append(BranchesConnessiPerBus[i][0])

        # SUDDIVISIONE ZONALE

        def Suddivisione_Zonale(bus, branches, switch):
            lista_zone = []
            zone_bus = {}

            # Creazione delle zone:

            for b in branches:
                # print(b)
                if b not in switch:
                    i = busfrom[b]
                    j = busto[b]

                    i_presente = j_presente = False
                    for n in zone_bus.values():
                        if i in n:
                            i_presente = True
                        if j in n:
                            j_presente = True

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
                        nuova_zona = "z" + str(len(lista_zone))
                        # print(nuova_zona)
                        lista_zone.append(nuova_zona)
                        zone_bus[nuova_zona] = [i, j]
                        # print('>> La zona', nuova_zona, 'è stata creata.')

            # Controllo se ci sono bus non assegnati ad alcuna zona:

            for i in bus:
                trovato = False
                for z in lista_zone:
                    if i in zone_bus[z]:
                        trovato = True
                if not trovato:
                    # print(i,'non è stato assegnato a nessuna zona.')
                    # Se il bus i risulta non assegnato, viene inserito in una nuova zona:
                    nuova_zona = "z" + str(len(lista_zone))
                    # print(nuova_zona)
                    lista_zone.append(nuova_zona)
                    zone_bus[nuova_zona] = [i]
                    # print('>> La zona', nuova_zona, 'è stata creata. Il bus',i,'è stato assegnato a',nuova_zona)

            # Rilevo eventuali zone vuote, le elimino e aggiorno la numerazione di zone e zone_bus:

            zone_bus = {k: vv for k, vv in zone_bus.items() if vv}
            zone_bus = {f'z{i}': vv for i, (k, vv) in enumerate(zone_bus.items(), start=0)}
            lista_zone = list(zone_bus.keys())
            return lista_zone, zone_bus

        # Applico la funzione creata:

        lista_zone, zone_bus = Suddivisione_Zonale(bus, branches, switch)

        # zone_bus=zone_bus[0:84]
        # print('Suddivisione zonale - END.')
        # print('Le zone ottenute sono:', len(lista_zone));
        self.log_pre_grafos += 'Le zone ottenute sono ' + str(len(lista_zone))
        Nzone = len(lista_zone)

        # Zona-from e Zona-to per ciascuno switch:
        switch_zone_from_to = {(sw): [] for sw in switch}
        switch_zone_from = {}
        switch_zone_to = {}

        for sw in switch:
            i, j = bus_from_to_sw[sw]
            for z in lista_zone:
                if i in zone_bus[z]:
                    z_fr = z
                if j in zone_bus[z]:
                    z_to = z
            switch_zone_from_to[sw].append(z_fr)
            switch_zone_from_to[sw].append(z_to)
            switch_zone_from[sw] = z_fr
            switch_zone_to[sw] = z_to

        switch_zone_from_to_ripetute = {}
        for chiave1, valore1 in switch_zone_from_to.items():
            for chiave2, valore2 in switch_zone_from_to.items():
                # Evita di confrontare una lista con se stessa
                if chiave1 != chiave2:
                    # Controlla se i due valori sono uguali anche in ordine scambiato
                    if set(valore1) == set(valore2):
                        switch_zone_from_to_ripetute[chiave1] = valore1
                        switch_zone_from_to_ripetute[chiave2] = valore2

        # Trovo maglie costituite da switches in prallelo che NetworkX non troverà mai

        maglie_da_aggiungere = [value for value in switch_zone_from_to_ripetute.values()]
        # Conteggio delle occorrenze delle liste
        conteggio_liste = defaultdict(int)
        # Conteggio delle liste duplicate
        liste_duplicate = defaultdict(int)
        # Lista per le liste senza duplicati
        maglie_da_aggiungere_indipendenti = []
        # Ciclo sulle liste originali
        for lista in maglie_da_aggiungere:
            # Converti la lista in una stringa ordinata per poterla usare come chiave nel dizionario
            chiave = str(sorted(lista))
            # Incrementa il conteggio delle occorrenze di questa lista
            conteggio_liste[chiave] += 1
            # Se questa lista è stata vista più di una volta, ma non è ancora stata aggiunta alle liste senza duplicati in eccesso, aggiungila
            if conteggio_liste[chiave] > 1 and liste_duplicate[chiave] < conteggio_liste[chiave] - 1:
                maglie_da_aggiungere_indipendenti.append(lista)
                liste_duplicate[chiave] += 1

        # Ricavo il set di zone connesse con ciascuna zona z:
        Nzone = len(lista_zone)

        def Matrice_di_adiacenza_zone_zone(Nzone, switch):
            matrice_adiacenza = pd.DataFrame(np.zeros((Nzone, Nzone)), index=lista_zone, columns=lista_zone)
            for s in switch:
                z1 = switch_zone_from_to[s][0]
                z2 = switch_zone_from_to[s][1]
                matrice_adiacenza.loc[z1, z2] = 1
                matrice_adiacenza.loc[z2, z1] = 1
            return matrice_adiacenza

        adiacenza_zone_pre = Matrice_di_adiacenza_zone_zone(Nzone, switch)

        zoneconnesse = {(z): [] for z in lista_zone}
        for i in lista_zone:
            for j in lista_zone:
                if adiacenza_zone_pre.loc[i, j] == 1:
                    zoneconnesse[i].append(j)

        # Ricavo il set di switch connessi a ciascuna zona z:
        SwitchConnessiPerZona = {(z): [] for z in lista_zone}
        for z in lista_zone:
            connections = []
            for s in switch:
                if (switch_zone_from[s] == z) or (switch_zone_to[s] == z):
                    connections.append(s)
            SwitchConnessiPerZona[z] = connections

        # Ricavo il set dei possibili "zone foglia" e il set di switches connessi a un nodo foglia (linee non switchabili):
        LeafZones = [];
        SwitchToLeafZones = []
        for z in lista_zone:
            if len(zoneconnesse[z]) == 1:
                LeafZones.append(z)
            if len(SwitchConnessiPerZona[z]) == 1:
                SwitchToLeafZones.append(SwitchConnessiPerZona[z][0])

        # Ricavo le zone a capo feeder:
        zone_capo_feeder = zoneconnesse['z0']

        # Lista delle zone senza la zona Z0:
        zonenosource = lista_zone[1:]

        # Ricavo l'insieme dei branches in ciascuna zona:
        zone_branches = {(z): [] for z in lista_zone}
        for b in branches:
            i = busfrom[b]
            j = busto[b]
            for z in lista_zone:
                if i in zone_bus[z] and j in zone_bus[z]:
                    zone_branches[z].append(b)

        zone_loads = {(z): [] for z in lista_zone}
        for b in loads:
            i = bus_load[b]
            for z in lista_zone:
                if i in zone_bus[z]:
                    zone_loads[z].append(b)

                    # RICAVO PARAMETRI DI RELIABILITY ZONALI

        # Tassi di guasto, tempi di riparazione e numeri di utenti serviti delle relative zone:

        lambda_z = {}
        lambda_z_2 = {}
        lambda_z_1 = {}
        R_z = {}
        num_clienti_per_zona = {}

        for z in lista_zone:
            lambda_z[z] = round(
                sum(lambda_l[l] for l in linee if l in zone_branches[z]) + sum(lambda_b[i] for i in zone_bus[z]), 6)
            lambda_z_2[z] = round((1 / 3) * lambda_z[z], 6)  # guasti non monofase
            lambda_z_1[z] = round((2 / 3) * lambda_z[z], 6)  # guasti monofase a terra
            R_z[z] = round((sum(R_l[l] * lambda_l[l] for l in linee if l in zone_branches[z]) + sum(
                R_b[i] * lambda_b[i] for i in zone_bus[z])) / lambda_z[z], 1)
            num_clienti_per_zona[z] = sum(num_clienti_per_bus[d] for d in loads if bus_load[d] in zone_bus[z])

        # Potenza attiva e reattiva richiesta dai carichi a livello zonale:
        PDz = {(z): 0 for z in lista_zone}
        PGz = {(z): 0 for z in lista_zone}

        # QDz = {(z):0 for z in lista_zone}
        for z in lista_zone:
            PDz[z] = round(sum(P_loads_nom[l] for l in loads if bus_load[l] in zone_bus[z]), 3)
            PGz[z] = round(sum(P_gen_nom[l] for l in generatori if bus_gen[l] in zone_bus[z]), 3)

            # QDz[z] = round(sum(Q_loads_nom[l] for l in loads if bus_load_senza123[l] in zone_bus[z]),3)
            if PDz[z] == 0:
                PDz[z] = 1

        # Ricavo DataFrame riassuntivo con tutti i parametri di reliability zonali
        ZoneReliability = pd.DataFrame(np.zeros((Nzone, 7)),
                                       columns=['N_branches', 'Lambda_z', 'Lambda_z_1', 'Lambda_z_2', 'R_z', 'P [kW]',
                                                'Clienti'], index=lista_zone)

        for z in lista_zone:
            ZoneReliability.at[z, 'N_branches'] = len(zone_branches[z])
            ZoneReliability.at[z, 'Lambda_z'] = lambda_z[z]
            ZoneReliability.at[z, 'Lambda_z_2'] = lambda_z_2[z]
            ZoneReliability.at[z, 'Lambda_z_1'] = lambda_z_1[z]
            ZoneReliability.at[z, 'R_z'] = R_z[z]
            ZoneReliability.at[z, 'P [kW]'] = PDz[z]
            # ZoneReliability.at[z, 'Q [kVAR]'] = QDz[z]
            ZoneReliability.at[z, 'Clienti'] = num_clienti_per_zona[z]

        # GRAFI ORIENTATI E SMAGLIATURA INIZIALE

        #### Grafo nodale magliato con NetworkX
        def Creazione_grafo_nodale(bus, branches):
            G = nx.Graph()
            # Aggiunta dei nodi al grafo
            G.add_nodes_from(bus)
            # Aggiunta degli archi al grafo
            for b in branches:
                if (b not in switch) or (b in switch and stati_switch_iniziali[b] == 1):
                    i = busfrom[b]
                    j = busto[b]
                    G.add_edge(i, j, label=branches)
            # Connectivity Check:
            is_connected = nx.is_connected(G)
            # print('')
            # print('Il grafo della rete ha', nx.number_of_nodes(G), 'nodi e', nx.number_of_edges(G), 'rami connessi.')
            # print(f'La rete è inizialmente connessa? {is_connected}')

            if is_connected:
                str_conn = ''
            else:
                str_conn = 'non '

            self.log_pre_grafos = (self.log_pre_grafos + 'Il grafo della rete ha ' + str(nx.number_of_nodes(G)) +
                                   ' nodi e ' + str(nx.number_of_edges(G)) + ' rami connessi.\n' +
                                   'La rete ' + str_conn + 'è inizialmente connessa\n\n')
            return G

        NX_grafo_nodale = Creazione_grafo_nodale(bus, branches)

        vedi_grafi = 'no'

        ### Grafo nodale magliato con Graphviz

        Grafo_nodale = graphviz.Digraph(comment='Grafo nodale')
        # Imposta le dimensioni della pagina e altre opzioni di visualizzazione:
        # Costruzione del grafo:
        for i in range(Nbus):
            Grafo_nodale.node(str(i), label=f'{bus[i]}', shape='circle', color='black', fixedsize='true', width='0.8',
                              height='0.8')
        for r in busfrom.keys():
            if (r not in switch) or (r in switch and stati_switch_iniziali[r] == 1):
                from_zone = busfrom[r]
                to_zone = busto[r]
                ind_from = bus.index(from_zone)
                ind_to = bus.index(to_zone)
                Grafo_nodale.edge(str(ind_from), str(ind_to), label=f'{r}', color='dimgray', constraint='true')

        Grafo_nodale.render(filename=self.filedir + 'Grafo Rete nodale e magliato', format='png', cleanup=True)
        # if vedi_grafi=='y':
        # Grafo_nodale.view()

        ### Grafo zonale e magliato con NeworkX
        def Creazione_grafo_zonale(lista_zone, switch):
            G = nx.MultiGraph()
            # Aggiunta dei nodi al grafo
            G.add_nodes_from(lista_zone)
            # Aggiunta degli archi al grafo
            for s in switch:
                if stati_switch_iniziali[s] == 1:
                    i = switch_zone_from[s]
                    j = switch_zone_to[s]
                    G.add_edge(i, j, label=switch)
            # Connectivity Check:
            is_connected = nx.is_connected(G)
            # print('')
            # print('Il grafo zonale della rete ha', nx.number_of_nodes(G), 'nodi e', nx.number_of_edges(G),
            #       'rami connessi.')
            # print(f'La rete zonale è inizialmente connessa? {is_connected}')

            if is_connected:
                str_conn = ''
            else:
                str_conn = 'non '

            self.log_pre_grafos = (self.log_pre_grafos + 'Il grafo zonale della rete ha ' + str(nx.number_of_nodes(G)) +
                                   ' nodi e ' + str(nx.number_of_edges(G)) + ' rami connessi.\n' +
                                   'La rete zonale ' + str_conn + 'è inizialmente connessa\n\n')

            Grafo = nx.Graph(G)
            return Grafo

        NX_grafo_zonale = Creazione_grafo_zonale(lista_zone, switch)

        ### Grafo zonale magliato con Graphviz

        Grafo_zone = graphviz.Digraph(comment='Grafo zone')
        # Imposta le dimensioni della pagina e altre opzioni di visualizzazione:
        # Costruzione del grafo:
        for i in range(Nzone):
            if lista_zone[i] == 'z0':
                Grafo_zone.node(str(i), label=f'{lista_zone[i]}', shape='circle', color='black', fillcolor='#FF6347',
                                style='filled', fixedsize='true', width='0.5', height='0.5', fontsize='14', pos='c',
                                penwidth='1.0')
            elif lista_zone[i] in zone_capo_feeder:
                Grafo_zone.node(str(i), label=f'{lista_zone[i]}', shape='circle', color='black', fillcolor='#FFA07A',
                                style='filled', fixedsize='true', width='0.5', height='0.5', fontsize='14', pos='c',
                                penwidth='1.0')
            else:
                Grafo_zone.node(str(i), label=f'{lista_zone[i]}', shape='circle', color='black', fillcolor='white',
                                style='filled', fixedsize='true', width='0.5', height='0.5', fontsize='14', pos='c',
                                penwidth='1.0')
        for r in switch:
            if stati_switch_iniziali[r] == 1:
                from_zone = switch_zone_from_to[r][0]
                to_zone = switch_zone_from_to[r][1]
                ind_from = lista_zone.index(from_zone)
                ind_to = lista_zone.index(to_zone)
                Grafo_zone.edge(str(ind_from), str(ind_to), color='dimgray', constraint='true')
            Grafo_zone.render(filename='Grafo Rete zonale e magliato', format='png', cleanup=True)
        # if vedi_grafi=='y':
        # Grafo_zone.view()

        ############ RICERCA MAGLIE INDIPENDENTI #############

        # Maglie indipendenti bus-branches
        independent_loops = list(nx.cycle_basis(NX_grafo_nodale))
        independent_meshes_with_buses = {(m): [] for m in range(len(independent_loops))}
        independent_meshes_with_branches_ij = {}
        independent_meshes_with_branches_b = {(m): [] for m in range(len(independent_loops))}

        for m in range(len(independent_loops)):
            for i in independent_loops[m]:
                independent_meshes_with_buses[m].append(i)

        for m, mm in enumerate(independent_loops):
            branches_in_a_mesh = [(mm[j], mm[j + 1]) for j in range(len(mm) - 1)]
            branches_in_a_mesh.append((mm[-1], mm[0]))  # Aggiungo l'arco di chiusura
            independent_meshes_with_branches_ij[m] = branches_in_a_mesh
            for br in branches_in_a_mesh:
                fr = br[0]
                to = br[1]
                for b in branches:
                    if (busfrom[b] == fr and busto[b] == to) or (busfrom[b] == to and busto[b] == fr):
                        independent_meshes_with_branches_b[m].append(b)

                        # Maglie indipendenti zone-switches
        independent_loops_zone = list(nx.cycle_basis(NX_grafo_zonale))
        independent_loops_zone.extend(maglie_da_aggiungere_indipendenti)
        independent_meshes_with_zones = {(m): [] for m in range(len(independent_loops_zone))}
        independent_meshes_with_switch_ij = {}
        independent_meshes_with_switch_s = {(m): [] for m in range(len(independent_loops_zone))}

        for m in range(len(independent_loops_zone)):
            for i in independent_loops_zone[m]:
                independent_meshes_with_zones[m].append(i)

        for m, mm in enumerate(independent_loops_zone):
            switches_in_a_mesh = [(mm[j], mm[j + 1]) for j in range(len(mm) - 1)]
            switches_in_a_mesh.append((mm[-1], mm[0]))  # Aggiungo l'arco di chiusura
            independent_meshes_with_switch_ij[m] = switches_in_a_mesh
            for a in switches_in_a_mesh:
                fr = a[0]
                to = a[1]
                for s in switch:
                    if (switch_zone_from[s] == fr and switch_zone_to[s] == to) or (
                            switch_zone_from[s] == to and switch_zone_to[s] == fr):
                        independent_meshes_with_switch_s[m].append(s)

                        ###### APERTURA SWITCHES #######

        # Partendo dalle maglie zone-switches
        dictionary_switch_apribili = copy.deepcopy(independent_meshes_with_switch_s)

        # Elimino switch collegati alla zona z0:

        for lista in dictionary_switch_apribili.values():
            lista[:] = [elemento for elemento in lista if not switch_zone_from[elemento] == 'z0']

        # Trovo switch apribili e non (non apribili saranno quelli che non fanno parte di maglie indipendenti)

        switch_non_apribili = []
        switch_apribili_set = set()

        for s in switch:
            for lista in dictionary_switch_apribili.values():
                # print(lista)
                if s in lista:
                    # print(s)
                    switch_apribili_set.add(s)

        # Converti l'insieme in una lista
        switch_apribili = list(switch_apribili_set)

        for s in switch:
            if s not in switch_apribili:
                switch_non_apribili.append(s)

        # Tra tutti gli switch apribili rimasti che formano una maglia, prendo uno casuale per ogni maglia)

        switch_da_aprire = []

        # Inizializza un set per tenere traccia delle stringhe già prese
        stringhe_usate = set()

        # # Itera attraverso le liste nel dizionario
        for lista in dictionary_switch_apribili.values():
            # Itera attraverso gli elementi della lista
            for elemento in lista:
                # Se l'elemento non è già stato usato, aggiungilo a switch_da_aprire e al set delle stringhe usate
                if elemento not in stringhe_usate:
                    switch_da_aprire.append(elemento)
                    stringhe_usate.add(elemento)
                    break  # Esci dal ciclo interno una volta aggiunto l'elemento

        # Apro gli switch su opendss
        for element in v.keys():
            if ('_s' in element or '_m' in element):
                if element in switch_da_aprire:
                    # dssCircuit.SetActiveElement(element)
                    # dssElem.Open(2, 0)  # 2 indica il lato da cui aprire lo switch, 0 indica la fase (nel caso di uno switch monofase)
                    v[element]['par']['out-of-service'] = True
                # print(v[element]['par']['out-of-service'], element)  # 2 indica il lato da cui aprire lo switch, 0 indica la fase (nel caso di uno switch monofase)

        # Trovo gli stati degli switches e dei branches

        stati_switch_iniziali = {}

        for m in v.keys():
            if '_s' in m or '_m' in m:
                if v[m]['par']['out-of-service'] == False:
                    # stato = dssElem.IsOpen(2, 0)
                    # Converte True in 0 e False in 1 e assegna il valore al dizionario
                    stati_switch_iniziali[m] = 1

                else:
                    stati_switch_iniziali[m] = 0

        stati_branch_iniziali = {}
        for elem in branches:
            if elem in switch:
                stati_branch_iniziali[elem] = stati_switch_iniziali[elem]
            else:
                stati_branch_iniziali[elem] = 1

        # Creo DataFrame con gli switch, zonefrom, zoneto e stati switch iniziali
        StatiSwitchesIniziali = pd.DataFrame(np.zeros((Nswitch, 3)), columns=['Zona from', 'Zona to', 'Stato iniziale'],
                                             index=switch)

        for s in switch:
            StatiSwitchesIniziali.at[s, 'Zona from'] = switch_zone_from[s]
            StatiSwitchesIniziali.at[s, 'Zona to'] = switch_zone_to[s]
            if stati_switch_iniziali[s] == 0:
                StatiSwitchesIniziali.at[s, 'Stato iniziale'] = 'aperto'
            elif stati_switch_iniziali[s] == 1:
                StatiSwitchesIniziali.at[s, 'Stato iniziale'] = 'chiuso'

        # statoo=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0]
        # stati_switch_iniziali = {}
        # k=0
        # Trovo solo gli switch rimasti chiusi
        # for m in switch:
        #     stati_switch_iniziali[m] = statoo[k]
        #     k+=1

        # for i in branches:
        #     if i in zone_branches['z1']:
        #         lambda_l[i]=lambda_l[i]*3
        #         # print(i)

        switch_chiusi = []

        for chiave, stato in stati_switch_iniziali.items():
            if stato == 1:
                switch_chiusi.append(chiave)

                # =============================================================================
        # LOAD FLOW STATO INIZIALE CON STATO SWITCH PER RADIALITÀ
        # =============================================================================

        # lambda_b=BranchesReliability['Lambda_l']
        # R_b=BranchesReliability['R_l']

        # lambda_c=BusesReliability['Lambda_i']
        # R_c=BusesReliability['R_i']

        self.ONR_PAR(zone_bus, stati_switch_iniziali, lambda_b, R_b, lambda_l, R_l, num_clienti_per_bus)

        # Ricavo il set di zone connesse con ciascuna zona z dopo l'apertura degli switch:

        def Matrice_di_adiacenza_zone_zone2(Nzone, switch, stati_switch):
            matrice_adiacenza = pd.DataFrame(np.zeros((Nzone, Nzone)), index=lista_zone, columns=lista_zone)
            for s in switch:
                z1 = switch_zone_from_to[s][0]
                z2 = switch_zone_from_to[s][1]
                if stati_switch[s] == 1:
                    matrice_adiacenza.loc[z1, z2] = 1
                    matrice_adiacenza.loc[z2, z1] = 1
            return matrice_adiacenza

        adiacenza_zone_radiale = Matrice_di_adiacenza_zone_zone2(Nzone, switch, stati_switch_iniziali)

        zoneconnesse_radiali = {(z): [] for z in lista_zone}
        for i in lista_zone:
            for j in lista_zone:
                if adiacenza_zone_radiale.loc[i, j] == 1:
                    zoneconnesse_radiali[i].append(j)

        #### Grafo nodale e smagliato con NetworkX
        def Creazione_grafo_nodale2(bus, branches):
            G = nx.Graph()
            # Aggiunta dei nodi al grafo
            G.add_nodes_from(bus)
            # Aggiunta degli archi al grafo
            for b in branches:
                if b in linee or b in trafi or b in switch_chiusi:
                    i = busfrom[b]
                    j = busto[b]
                    G.add_edge(i, j, label=branches)
            # Connectivity Check:
            is_connected = nx.is_connected(G)
            # print('')
            # print('Il grafo della rete senza maglie ha', nx.number_of_nodes(G), 'nodi e', nx.number_of_edges(G),
            #       'rami connessi.')
            # print(f'La rete smagliata è connessa? {is_connected}')

            if is_connected:
                str_conn = ''
            else:
                str_conn = 'non '

            self.log_pre_grafos = (self.log_pre_grafos + 'Il grafo della rete senza maglie ha ' +
                                   str(nx.number_of_nodes(G)) + ' nodi e ' + str(nx.number_of_edges(G)) +
                                   ' rami connessi.\n' +
                                   'La rete smagliata ' + str_conn + 'è connessa\n\n')

            return G

        NX_grafo_nodale_smagliato = Creazione_grafo_nodale2(bus, branches)

        # Visualizzazione del grafo
        # pos = nx.spring_layout(NX_grafo_nodale_smagliato)  # Posizionamento dei nodi
        # nx.draw(NX_grafo_nodale_smagliato, pos, with_labels=False, node_color='skyblue', node_size=10, edge_color='gray')

        # # Mostra il grafo
        # plt.show()

        ### Grafo nodale smagliato con Graphviz

        # Grafo_nodale_radiale = graphviz.Digraph(comment='Grafo nodale')
        # # Imposta le dimensioni della pagina e altre opzioni di visualizzazione:
        # # Costruzione del grafo:
        # for i in range(Nbus):
        #     Grafo_nodale_radiale.node(str(i), label=f'{i}', shape='circle', color='black', fixedsize='true', width='0.5', height='0.5')
        # for r in branches:
        #     from_zone = busfrom[r]
        #     to_zone = busto[r]
        #     ind_from = bus.index(from_zone)
        #     ind_to = bus.index(to_zone)
        #     if r in switch and r not in switch_chiusi:
        #         colore_ramo = 'red'
        #         stile = 'dashed'
        #     else:
        #         colore_ramo = 'dimgray'
        #         stile = 'solid'
        #     Grafo_nodale_radiale.edge(str(ind_from), str(ind_to), label=f'{r}'   ,color=colore_ramo, style=stile ,constraint='true')
        # Grafo_nodale_radiale.render(filename='Grafo Rete nodale e smagliato', format='pdf', cleanup=True)
        # Grafo_nodale_radiale.view()

        ### Grafo zonale e smagliato con NeworkX
        def Creazione_grafo_zonale2(lista_zone, stati_switch, stampa_a_video=True):
            G = nx.MultiGraph()
            # Aggiunta dei nodi al grafo
            G.add_nodes_from(lista_zone)
            # Aggiunta degli archi al grafo
            for s in switch:
                if stati_switch_iniziali[s] == 1:
                    i = switch_zone_from[s]
                    j = switch_zone_to[s]
                    G.add_edge(i, j, label=switch)
            # Connectivity Check:
            is_connected = nx.is_connected(G)
            if stampa_a_video:
                # print('')
                # print('Il grafo della rete zonale senza maglie ha', nx.number_of_nodes(G), 'nodi e',
                #       nx.number_of_edges(G), 'rami connessi.')
                # print(f'La rete zonale smagliata è connessa? {is_connected}')

                if is_connected:
                    str_conn = ''
                else:
                    str_conn = 'non '

                self.log_pre_grafos = (self.log_pre_grafos + 'Il grafo della rete zonale senza maglie ha ' +
                                       str(nx.number_of_nodes(G)) + ' nodi e ' + str(nx.number_of_edges(G)) +
                                       ' rami connessi.\n' +
                                       'La rete zonale smagliata ' + str_conn + 'è connessa\n\n')

            grafo = nx.Graph(G)
            return grafo

        NX_grafo_zonale_smagliato = Creazione_grafo_zonale2(lista_zone, stati_switch_iniziali)

        #### Dizionario per memorizzare i percorsi più brevi da ciascuna zona capo feeder verso tutte le zone
        percorsi_più_brevi = {}

        # Calcola i percorsi più brevi per ciascun nodo sorgente
        for sorgente in zone_capo_feeder:
            percorsi_più_brevi[sorgente] = nx.single_source_shortest_path(NX_grafo_zonale_smagliato, sorgente)

        ### Grafo zonale smagliato con Graphviz

        # Grafo_zone_radiale = graphviz.Digraph(comment='Grafo zone radiali')
        # # Imposta le dimensioni della pagina e altre opzioni di visualizzazione:
        # # Costruzione del grafo:
        # for i in range(Nzone):
        #     if lista_zone[i] == 'z0':
        #         Grafo_zone_radiale.node(str(i), label=f'{i}', shape='circle', color='black', fillcolor='#FF6347', style='filled', fixedsize='true', width='0.5', height='0.5', fontsize='14', pos='c', penwidth='1.0')
        #     elif lista_zone[i] in zone_capo_feeder:
        #         Grafo_zone_radiale.node(str(i), label=f'{i}', shape='circle', color='black', fillcolor='#FFA07A', style='filled', fixedsize='true', width='0.5', height='0.5', fontsize='14', pos='c', penwidth='1.0')
        #     else:
        #         Grafo_zone_radiale.node(str(i), label=f'{i}', shape='circle', color='black', fillcolor='white', style='filled', fixedsize='true', width='0.5', height='0.5', fontsize='14', pos='c', penwidth='1.0')

        # for r in switch:
        #     from_zone = switch_zone_from_to[r][0]
        #     to_zone = switch_zone_from_to[r][1]
        #     ind_from = lista_zone.index(from_zone)
        #     ind_to = lista_zone.index(to_zone)
        #     if r in switch_chiusi:
        #         colore_ramo = 'black'
        #         stile = 'solid'
        #     else:
        #         colore_ramo = 'red'
        #         stile = 'dashed'
        #     Grafo_zone_radiale.edge(str(ind_from), str(ind_to), label=f'{r}'   ,color=colore_ramo, style=stile,  constraint='true')
        # Grafo_zone_radiale.render(filename='Grafo Rete zonale e smagliato', format='pdf', cleanup=True)
        # # if vedi_grafi=='y':
        # Grafo_zone_radiale.view()

        # Grafo_zone_radiale = graphviz.Digraph(comment='Grafo zone radiali')
        # # Imposta le dimensioni della pagina e altre opzioni di visualizzazione:
        # Grafo_zone_radiale.attr(size='8.27,11.69!', orientation='portrait', splines='true', layout='dot', overlap='false', nodesep='1', margin='0.05', seed='42') # FORMATO A4
        # # Costruzione del grafo:

        # for i in range(Nzone):
        #     if lista_zone[i] == 'z0':
        #         Grafo_zone_radiale.node(str(i), label=f'{i}', shape='circle', color='black', fillcolor='#FF6347', style='filled', fixedsize='true', width='0.5', height='0.5', fontsize='14', pos='c', penwidth='1.0')
        #     elif lista_zone[i] in zone_capo_feeder:
        #         Grafo_zone_radiale.node(str(i), label=f'{i}', shape='circle', color='black', fillcolor='#FFA07A', style='filled', fixedsize='true', width='0.5', height='0.5', fontsize='14', pos='c', penwidth='1.0')

        # for i in range(Nzone):
        #     if lista_zone[i] != 'z0' and lista_zone[i] not in zone_capo_feeder:
        #         # for j in zonegraph:
        #         #     if lista_zone[i] in zonegraph[j]:
        #         Grafo_zone_radiale.node(str(i), label=f'{i}', shape='circle', color='black', fillcolor='white', style='filled', fixedsize='true', width='0.5', height='0.5', fontsize='14', pos='c', penwidth='1.0')

        # for r in switch_chiusi:
        #     from_zone = switch_zone_from_to[r][0]
        #     to_zone = switch_zone_from_to[r][1]
        #     ind_from = lista_zone.index(from_zone)
        #     ind_to = lista_zone.index(to_zone)
        #     Grafo_zone_radiale.edge(str(ind_from), str(ind_to), label=f'{r}',color='black' , arrowhead='none', constraint='true')

        # Grafo_zone_radiale.render(filename='Grafo Rete zonale e radiale', format='pdf', cleanup=True)
        # if vedi_grafi=='y':
        #     Grafo_zone_radiale.view()

        independent_loops_zone2 = list(nx.cycle_basis(NX_grafo_zonale_smagliato))
        independent_loops2 = list(nx.cycle_basis(NX_grafo_nodale_smagliato))
        if len(independent_loops_zone2) != 0 or len(independent_loops2) != 0:
            print('Ci sono ancora delle maglie')

        # =============================================================================
        # SCRITTURA NEL DIZIONARIO DELLO STATO DEGLI SWITCH E DELLE ZONE
        # ONR STATO INIZIALE

        # input_optimization = input('> Valutare gli indici di qualità allo stato iniziale? (y/n):');
        # print('')
        # if input_optimization.lower() != 'y':
        #     sys.exit()

        # Trovo zone che appartengono allo stesso feeder
        def crea_dizionario_zone_connesse(dizionario, chiavi_desiderate):
            risultato = {}

            def aggiungi_connessi(chiave, lista):
                if chiave not in risultato:
                    risultato[chiave] = []

                if chiave != 'z0' and chiave not in lista:
                    lista.append(chiave)

                for elemento in dizionario[chiave]:
                    if elemento != 'z0' and elemento not in lista:
                        lista.append(elemento)
                        aggiungi_connessi(elemento, lista)

            for chiave in chiavi_desiderate:
                lista_connessi = []
                aggiungi_connessi(chiave, lista_connessi)
                # lista_connessi.append('z0')
                risultato[chiave] = lista_connessi

            return risultato

        zone_connesse_allo_stesso_feeder = crea_dizionario_zone_connesse(zoneconnesse_radiali, zonenosource)

        # Trovo il capo feeder per ogni zona
        capo_feeder_per_zona = {}
        for chiave, zone in zone_connesse_allo_stesso_feeder.items():
            for zona in zone:
                if zona in zone_capo_feeder:
                    capo_feeder_per_zona[chiave] = zona

        # Trovo le zone upstream

        zone_upstream = {}

        for chiave, capo_feeder in capo_feeder_per_zona.items():
            zone_upstream[chiave] = percorsi_più_brevi[capo_feeder][chiave]
            # zone_upstream[chiave].insert(0, 'z0')

        # %% GRAFO NODALE PRE ONR

        scrittee = ['white', 'black', 'black', 'black']
        colori = ['red', 'orange', 'yellow', 'green']

        scritte = dict()
        colordict = dict()
        zonegraph = dict()
        busgraph = dict()
        corr = dict()
        corr2 = dict()
        k = 0
        for i in zoneconnesse_radiali:
            if i in zone_capo_feeder:
                busgraph[i] = []
                zonegraph[i] = zone_connesse_allo_stesso_feeder[i]
                for kk in range(len(zonegraph[i])):
                    busgraph[i] += zone_bus[zonegraph[i][kk]]
                    kk += 1
                for kkk in bus:
                    for kkkk in busgraph.keys():
                        if kkk in busgraph[kkkk]:
                            corr[kkk] = kkkk
                for kkk in lista_zone:
                    for kkkk in zonegraph.keys():
                        if kkk in zonegraph[kkkk]:
                            corr2[kkk] = kkkk
                colordict[i] = colori[k]
                scritte[i] = scrittee[k]
                k += 1

        nodi_source = zone_bus['z0']
        nodi_capo_feeder = []
        for i in zone_bus.keys():
            if i in zone_capo_feeder:
                nodi_capo_feeder.append(zone_bus[i][0])

        # TODO: Da riattivare
        Grafo_nodale_radiale = graphviz.Digraph(comment='Grafo nodale')
        # Grafo_nodale_radiale.attr(size='100,40', orientation='landscape', layout='dot')
        Grafo_nodale_radiale.attr(graphattr='dpi=600')
        Grafo_nodale_radiale.attr(fontname='Times New Roman')
        # Imposta le dimensioni della pagina e altre opzioni di visualizzazione:
        # Costruzione del grafo:
        for i in range(len(bus)):
            if bus[i] == 'sourcebus':
                Grafo_nodale_radiale.node(str(i), label=f'{bus[i]}', shape='circle', color='black',
                                          fontname='Arial Bold', fixedsize='true', width='1.1', height='1.1',
                                          penwidth='5.0')
            elif bus[i] in nodi_source:
                Grafo_nodale_radiale.node(str(i), label=f'{bus[i]}', shape='circle', color='black',
                                          fontname='Arial Bold', fixedsize='true', width='0.7', height='0.7',
                                          penwidth='5.0')
            elif bus[i] in nodi_capo_feeder and bus[i] in bus_gen.values():
                Grafo_nodale_radiale.node(str(i), label=f'{bus[i]}', shape='triangle', color='black',
                                          fontname='Arial Bold', fillcolor=colordict[corr[bus[i]]],
                                          fontcolor=scritte[corr[bus[i]]], style='filled', fixedsize='true',
                                          width='0.9', height='0.9', penwidth='3.0')
            elif bus[i] in nodi_capo_feeder:
                Grafo_nodale_radiale.node(str(i), label=f'{bus[i]}', shape='circle', color='black',
                                          fontname='Arial Bold', fillcolor=colordict[corr[bus[i]]],
                                          fontcolor=scritte[corr[bus[i]]], style='filled', fixedsize='true',
                                          width='0.7', height='0.7', penwidth='3.0')
            elif bus[i] in bus_gen.values():
                Grafo_nodale_radiale.node(str(i), label=f'{bus[i]}', shape='triangle', color='black',
                                          fontname='Arial Bold', fillcolor=colordict[corr[bus[i]]],
                                          fontcolor=scritte[corr[bus[i]]], style='filled', fixedsize='true',
                                          width='0.9', height='0.9', penwidth='3.0')
            else:
                Grafo_nodale_radiale.node(str(i), label=f'{bus[i]}', shape='circle', color='black',
                                          fontname='Arial Bold', fillcolor=colordict[corr[bus[i]]],
                                          fontcolor=scritte[corr[bus[i]]], style='filled', fixedsize='true',
                                          width='0.7', height='0.7', penwidth='3.0')

        fromzone = []
        tozone = []
        indfrom = []
        indto = []
        indice = []
        indicesw = []
        for r in branches:
            if r not in switch or r in switch_chiusi:
                from_zone = busfrom[r]
                to_zone = busto[r]
                ind_from = bus.index(from_zone)
                ind_to = bus.index(to_zone)
                indice.append((ind_from, ind_to))
                # print(r, ind_from,ind_to)
                indfrom.append(bus.index(from_zone))
                indto.append(bus.index(to_zone))
                if r in switch_chiusi:
                    indicesw.append((ind_from, ind_to))
                else:
                    indicesw.append((0, 0))

        indice = sorted(indice, key=lambda x: x[0])
        indicesw = sorted(indicesw, key=lambda x: x[0])

        indfromo = []
        indtoto = []
        index = []
        indexsw = []
        for i in range(len(indice)):
            if indice[i][0] == 0:
                index.append(indice[i][:])
                indexsw.append(indicesw[i][:])
                indfromo.append(indice[i][0])
                indtoto.append(indice[i][1])

        while len(index) < len(bus) - 1:

            for i in range(len(indice)):
                for j in range(len(index)):
                    if indice[i][0] in index[j] and indice[i][0] != 0 and indice[i][:] not in index:
                        index.append(indice[i][:])
                        indexsw.append(indicesw[i][:])
                        indfromo.append(indice[i][0])
                        indtoto.append(indice[i][1])

            for i in range(len(indice)):
                for j in range(len(index)):
                    if ((indice[i][1] in index[j]) and indice[i][1] != 0) and (indice[i][:] not in index):
                        index.append(indice[i][:])
                        indexsw.append(indicesw[i][:])

                        indfromo.append(indice[i][1])
                        indtoto.append(indice[i][0])
        print('non si è bloccato!')

        for i in range(len(index)):
            p = 0
            for j in bus_from_to_sw.keys():
                if bus.index(bus_from_to_sw[j][0]) == index[i][0] and bus.index(bus_from_to_sw[j][1]) == index[i][
                    1] or bus.index(bus_from_to_sw[j][0]) == index[i][1] and bus.index(bus_from_to_sw[j][1]) == \
                        index[i][0]:
                    Grafo_nodale_radiale.edge(str(indfromo[i]), str(indtoto[i]), label=f'{j}', color='red',
                                              arrowhead='none', constraint='true', penwidth='2.0')
                    p += 1
                    break
            if p == 0:
                Grafo_nodale_radiale.edge(str(indfromo[i]), str(indtoto[i]), color='black', arrowhead='none',
                                          constraint='true', penwidth='2.0')

        Grafo_nodale_radiale.render(filename=self.filedir + 'grafo_nodale_pre_ONR', format='png', cleanup=True)
        # Grafo_nodale_radiale.view()

        # %% GRAFO ZONALE PRE ONR

        Grafo_zone_radiale = graphviz.Digraph(comment='Grafo zone radiali')
        # Imposta le dimensioni della pagina e altre opzioni di visualizzazione:
        Grafo_zone_radiale.attr(size='8,10!', orientation='portrait', layout='dot', seed='927')
        Grafo_zone_radiale.attr(graphattr='dpi=600')

        # Costruzione del grafo:
        for i in range(Nzone):
            if lista_zone[i] == 'z0':
                Grafo_zone_radiale.node(str(i), label=f'{lista_zone[i]}', shape='circle', fontname='Arial Bold',
                                        color='black', fillcolor='white', style='filled', fixedsize='true', width='0.5',
                                        height='0.5', fontsize='14', pos='c', penwidth='3.0')
            elif lista_zone[i] in zone_capo_feeder and PGz[lista_zone[i]] == 0:
                Grafo_zone_radiale.node(str(i), label=f'{lista_zone[i]}', shape='circle', fontname='Arial Bold',
                                        color='black', fontcolor=scritte[lista_zone[i]],
                                        fillcolor=colordict[lista_zone[i]], style='filled', fixedsize='true',
                                        width='0.5', height='0.5', fontsize='14', pos='c', penwidth='1.2')
            elif lista_zone[i] in zone_capo_feeder and PGz[lista_zone[i]] != 0:
                Grafo_zone_radiale.node(str(i), label=f'{lista_zone[i]}', shape='triangle', fontname='Arial Bold',
                                        color='black', fontcolor=scritte[lista_zone[i]],
                                        fillcolor=colordict[lista_zone[i]], style='filled', fixedsize='true',
                                        width='0.6', height='0.6', fontsize='14', pos='c', penwidth='1.2')

            else:
                for j in zonegraph:
                    if lista_zone[i] in zonegraph[j] and PGz[lista_zone[i]] == 0:
                        Grafo_zone_radiale.node(str(i), label=f'{lista_zone[i]}', shape='circle', fontname='Arial Bold',
                                                color='black', fontcolor=scritte[j], fillcolor=colordict[j],
                                                style='filled', fixedsize='true', width='0.5', height='0.5',
                                                fontsize='14', pos='c', penwidth=('1.2'))
                    if lista_zone[i] in zonegraph[j] and PGz[lista_zone[i]] != 0:
                        Grafo_zone_radiale.node(str(i), label=f'{lista_zone[i]}', shape='triangle',
                                                fontname='Arial Bold', color='black', fontcolor=scritte[j],
                                                fillcolor=colordict[j], style='filled', fixedsize='true', width='0.6',
                                                height='0.6', fontsize='14', pos='c', penwidth=('1.2'))

                        # Aggiungere i rank per organizzare i nodi sotto i nodi della zona_capo_feeder

        fromzone = []
        tozone = []
        indfrom = []
        indto = []
        indice = []
        for r in switch_chiusi:
            fromzone.append(switch_zone_from_to[r][0])
            tozone.append(switch_zone_from_to[r][1])
            from_zone = switch_zone_from_to[r][0]
            to_zone = switch_zone_from_to[r][1]
            ind_from = lista_zone.index(from_zone)
            ind_to = lista_zone.index(to_zone)
            indice.append((ind_from, ind_to))
            indfrom.append(lista_zone.index(from_zone))
            indto.append(lista_zone.index(to_zone))

        indice = sorted(indice, key=lambda x: x[0])
        indfromo = []
        indtoto = []
        index = []
        for i in range(len(indice)):
            if indice[i][0] == 0:
                index.append(indice[i][:])
                indfromo.append(indice[i][0])
                indtoto.append(indice[i][1])
        while len(index) < len(lista_zone) - 1:

            for i in range(len(indice)):
                for j in range(len(index)):
                    if indice[i][0] in index[j] and indice[i][0] != 0 and indice[i][:] not in index:
                        index.append(indice[i][:])
                        indfromo.append(indice[i][0])
                        indtoto.append(indice[i][1])

            for i in range(len(indice)):
                for j in range(len(index)):
                    if ((indice[i][1] in index[j]) and indice[i][1] != 0) and (indice[i][:] not in index):
                        index.append(indice[i][:])
                        indfromo.append(indice[i][1])
                        indtoto.append(indice[i][0])

                    # Grafo_zone_radiale.edge(str(ind_from), str(ind_to), color='black' ,arrowhead='none', constraint='true', penwidth='2.0')
        for i in range(len(index)):
            for j in switch_zone_from_to.keys():
                if lista_zone.index(switch_zone_from_to[j][0]) == index[i][0] and lista_zone.index(
                        switch_zone_from_to[j][1]) == index[i][1] or lista_zone.index(switch_zone_from_to[j][0]) == \
                        index[i][1] and lista_zone.index(switch_zone_from_to[j][1]) == index[i][0]:
                    Grafo_zone_radiale.edge(str(indfromo[i]), str(indtoto[i]), label=f'{j}', color='red',
                                            arrowhead='none', constraint='true', penwidth='2.0')

        Grafo_zone_radiale.render(filename=self.filedir + 'grafo_zonale_pre_ONR', format='png', cleanup=True)
        # Grafo_zone_radiale.view()

        # %% Trovo indici di reliability utilizzando la funzione calcolo_indici_reliability

        ENS_PRE_FRG, SAIDI_PRE_FRG, SAIFI_PRE_FRG = calcolo_indici_reliability(zone_connesse_allo_stesso_feeder,
                                                                               zone_upstream, 'a')

        ENS_PRE_FNC, SAIDI_PRE_FNC, SAIFI_PRE_FNC = calcolo_indici_reliability(zone_connesse_allo_stesso_feeder,
                                                                               zone_upstream, 'b')

        ENS_PRE_SFS, SAIDI_PRE_SFS, SAIFI_PRE_SFS = calcolo_indici_reliability(zone_connesse_allo_stesso_feeder,
                                                                               zone_upstream, 'c')

        Indici_di_Reliability_pre = pd.DataFrame(np.zeros((3, 3)), index=['FRG', 'FNC', 'SFS'],
                                                 columns=['ENS', 'SAIDI', 'SAIFI'])
        Indici_di_Reliability_pre_norm = pd.DataFrame(np.zeros((3, 3)), index=['FRG', 'FNC', 'SFS'],
                                                      columns=['ENS', 'SAIDI', 'SAIFI'])

        Indici_di_Reliability_pre.loc['FRG', 'ENS'] = ENS_PRE_FRG
        Indici_di_Reliability_pre.loc['FRG', 'SAIDI'] = SAIDI_PRE_FRG
        Indici_di_Reliability_pre.loc['FRG', 'SAIFI'] = SAIFI_PRE_FRG

        Indici_di_Reliability_pre.loc['FNC', 'ENS'] = ENS_PRE_FNC
        Indici_di_Reliability_pre.loc['FNC', 'SAIDI'] = SAIDI_PRE_FNC
        Indici_di_Reliability_pre.loc['FNC', 'SAIFI'] = SAIFI_PRE_FNC

        Indici_di_Reliability_pre.loc['SFS', 'ENS'] = ENS_PRE_SFS
        Indici_di_Reliability_pre.loc['SFS', 'SAIDI'] = SAIDI_PRE_SFS
        Indici_di_Reliability_pre.loc['SFS', 'SAIFI'] = SAIFI_PRE_SFS

        Indici_di_Reliability_pre_norm.loc['FRG', 'ENS'] = ENS_PRE_FRG / ENS_PRE_FRG
        Indici_di_Reliability_pre_norm.loc['FRG', 'SAIDI'] = SAIDI_PRE_FRG / SAIDI_PRE_FRG
        Indici_di_Reliability_pre_norm.loc['FRG', 'SAIFI'] = SAIFI_PRE_FRG / SAIFI_PRE_FRG

        Indici_di_Reliability_pre_norm.loc['FNC', 'ENS'] = ENS_PRE_FNC / ENS_PRE_FRG
        Indici_di_Reliability_pre_norm.loc['FNC', 'SAIDI'] = SAIDI_PRE_FNC / SAIDI_PRE_FRG
        Indici_di_Reliability_pre_norm.loc['FNC', 'SAIFI'] = SAIFI_PRE_FNC / SAIFI_PRE_FRG

        Indici_di_Reliability_pre_norm.loc['SFS', 'ENS'] = ENS_PRE_SFS / ENS_PRE_FRG
        Indici_di_Reliability_pre_norm.loc['SFS', 'SAIDI'] = SAIDI_PRE_SFS / SAIDI_PRE_FRG
        Indici_di_Reliability_pre_norm.loc['SFS', 'SAIFI'] = SAIFI_PRE_SFS / SAIFI_PRE_FRG

        # print('')
        # print('INDICI DI RELIABILITY ALLO STATO INIZIALE:')
        # print(round(Indici_di_Reliability_pre, 4))
        # print('')
        #
        # print('')
        # print('INDICI DI RELIABILITY ALLO STATO INIZIALE NORM:')
        # print(round(Indici_di_Reliability_pre_norm, 4))
        # print('')

        # FRG INIZIALE
        f_z_FRG = {}
        f_z_FRG['z0'] = 0
        for z, lista in zone_connesse_allo_stesso_feeder.items():
            somma = sum([lambda_z[elem] for elem in lista])
            f_z_FRG[z] = somma

        U_z_FRG = {}
        U_z_FRG['z0'] = 0
        for z, lista in zone_connesse_allo_stesso_feeder.items():
            somma = 0  # Inizializza la somma a zero per ogni zona
            for elem in lista:
                if elem in zone_upstream[z]:
                    somma += lambda_z[elem] * R_z[elem]
                elif elem in zone_connesse_allo_stesso_feeder[z] and elem not in zone_upstream[z]:
                    somma += lambda_z[elem] * 0.05
            U_z_FRG[z] = somma

        # FNC INIZIALE
        f_z_FNC = {}
        f_z_FNC['z0'] = 0
        somma1 = {};
        somma2 = {}
        for z, lista in zone_connesse_allo_stesso_feeder.items():
            somma1[z] = sum(lambda_z_2[elem] for elem in lista)
        for z, lista in zone_upstream.items():
            somma2[z] = sum(lambda_z_1[elem] for elem in lista)
        for z in zonenosource:
            f_z_FNC[z] = somma1[z] + somma2[z]

        U_z_FNC = {}
        U_z_FNC['z0'] = 0
        for z, lista in zone_connesse_allo_stesso_feeder.items():
            somma = 0  # Inizializza la somma a zero per ogni zona
            for elem in lista:
                if elem in zone_upstream[z]:
                    somma += (lambda_z_1[elem] + lambda_z_2[elem]) * R_z[elem]
                elif elem in zone_connesse_allo_stesso_feeder[z] and elem not in zone_upstream[z]:
                    somma += lambda_z_2[elem] * 0.05
            U_z_FNC[z] = somma

        # SFS INIZIALE

        f_z_SFS = {}
        f_z_SFS['z0'] = 0
        for z, lista in zone_upstream.items():
            somma = sum([lambda_z[elem] for elem in lista])
            f_z_SFS[z] = somma

        U_z_SFS = {}
        U_z_SFS['z0'] = 0
        for z, lista in zone_upstream.items():
            somma = sum([lambda_z[elem] * R_z[elem] for elem in lista])
            U_z_SFS[z] = somma

        # Funzione obiettivo allo stato iniziale
        funzione_obiettivo_pre_FRG = calcolo_funzione_obiettivo(stati_switch_iniziali, 'a', stampa_a_video=False)[0]
        funzione_obiettivo_pre_FNC = calcolo_funzione_obiettivo(stati_switch_iniziali, 'b', stampa_a_video=False)[0]
        funzione_obiettivo_pre_SFS = calcolo_funzione_obiettivo(stati_switch_iniziali, 'c', stampa_a_video=False)[0]

        Funzioni_obiettivo_pre = pd.DataFrame(np.zeros((3, 1)), index=['FRG', 'FNC', 'SFS'],
                                              columns=['Funzione obiettivo'])

        Funzioni_obiettivo_pre.loc['FRG', 'Funzione obiettivo'] = funzione_obiettivo_pre_FRG
        Funzioni_obiettivo_pre.loc['FNC', 'Funzione obiettivo'] = funzione_obiettivo_pre_FNC
        Funzioni_obiettivo_pre.loc['SFS', 'Funzione obiettivo'] = funzione_obiettivo_pre_SFS

        # print('')
        # print('FUNZIONI OBIETTIVO ALLO STATO INIZIALE:')
        # print(round(Funzioni_obiettivo_pre, 4))
        # print('')

        self.indexes = {
            'Abs': {
                'FRG': {
                    'EENS': ENS_PRE_FRG,
                    'SAIDI': SAIDI_PRE_FRG,
                    'SAIFI': SAIFI_PRE_FRG,
                },
                'FNC': {
                    'EENS': ENS_PRE_FNC,
                    'SAIDI': SAIDI_PRE_FNC,
                    'SAIFI': SAIFI_PRE_FNC,
                },
                'SFS': {
                    'EENS': ENS_PRE_SFS,
                    'SAIDI': SAIDI_PRE_SFS,
                    'SAIFI': SAIFI_PRE_SFS,
                },
            },
            'Norm': {
                'FRG': {
                    'EENS': ENS_PRE_FRG / ENS_PRE_FRG,
                    'SAIDI': SAIDI_PRE_FRG / SAIDI_PRE_FRG,
                    'SAIFI': SAIFI_PRE_FRG / SAIFI_PRE_FRG,
                },
                'FNC': {
                    'EENS': ENS_PRE_FNC / ENS_PRE_FRG,
                    'SAIDI': SAIDI_PRE_FNC / SAIDI_PRE_FRG,
                    'SAIFI': SAIFI_PRE_FNC / SAIFI_PRE_FRG,
                },
                'SFS': {
                    'EENS': ENS_PRE_SFS / ENS_PRE_FRG,
                    'SAIDI': SAIDI_PRE_SFS / SAIDI_PRE_FRG,
                    'SAIFI': SAIFI_PRE_SFS / SAIFI_PRE_FRG,
                },
            },
            'Fob': {
                'FRG': {'fob': funzione_obiettivo_pre_FRG},
                'FNC': {'fob': funzione_obiettivo_pre_FNC},
                'SFS': {'fob': funzione_obiettivo_pre_SFS},
            },
        }

        # Grafici ENS, SAIDI, SAIFI

        eens_fig = plt.figure(3, figsize=(6, 6))
        plt.bar(Indici_di_Reliability_pre_norm.index, Indici_di_Reliability_pre_norm['ENS'].values, width=0.5,
                color=['#FFA07A', '#FF7F50', '#FF6347'], edgecolor='black')
        plt.locator_params(axis='y', nbins=15)
        plt.xlabel('Automation logics', fontsize=15)
        plt.ylabel('EENS [kWh/year]', fontsize=15)
        formatter = ScalarFormatter()
        formatter.set_scientific(True)
        formatter.set_powerlimits((0, 3))
        plt.gca().yaxis.set_major_formatter(formatter)
        # plt.show()
        # plt.savefig(self.filedir + 'EENS.png')
        eens_fig.savefig(self.filedir + 'EENS.png')

        saidi_fig = plt.figure(3, figsize=(6, 6))
        plt.bar(Indici_di_Reliability_pre_norm.index, Indici_di_Reliability_pre_norm['SAIDI'].values, width=0.5,
                color=['#FFA07A', '#FF7F50', '#FF6347'], edgecolor='black')
        plt.locator_params(axis='y', nbins=10)
        plt.xlabel('Automation logics', fontsize=15)
        plt.ylabel('SAIDI [hours/year]', fontsize=15)
        # plt.show(
        # plt.savefig(self.filedir + 'SAIDI.png')
        saidi_fig.savefig(self.filedir + 'SAIDI.png')

        saifi_fig = plt.figure(3, figsize=(6, 6))
        plt.bar(Indici_di_Reliability_pre_norm.index, Indici_di_Reliability_pre_norm['SAIFI'].values, width=0.5,
                color=['#FFA07A', '#FF7F50', '#FF6347'], edgecolor='black')
        plt.xlabel('Automation logics', fontsize=15)
        plt.ylabel('SAIFI [faults/year]', fontsize=15)
        # plt.show()
        # plt.savefig(self.filedir + 'SAIFI.png')
        saifi_fig.savefig(self.filedir + 'SAIFI.png')

        fob_fig = plt.figure(3, figsize=(6, 6))
        plt.bar(Funzioni_obiettivo_pre.index, Funzioni_obiettivo_pre['Funzione obiettivo'].values, width=0.5,
                color=['#FFA07A', '#FF7F50', '#FF6347'], edgecolor='black')
        plt.locator_params(axis='y', nbins=15)
        plt.xlabel('Automation logics', fontsize=15)
        plt.ylabel('Objective function', fontsize=15)
        # plt.show()
        # plt.savefig(self.filedir + 'obj_funct.png')
        fob_fig.savefig(self.filedir + 'obj_funct.png')

        # kw=[]
        # kvar=[]
        # dssLoads.First
        # for i in range(dssLoads.Count):
        #     kw.append(dssLoads.kW)
        #     kvar.append(dssLoads.kvar)
        #     dssLoads.Next

        ONR_GLOBALE = {'Adiacenza': {'Nodi_Nodi': Matrice_adiacenza, 'Zone_Zone': adiacenza_zone_radiale},
                       'Incidenza': {'Branch_Nodi': Matrice_incidenza}}

        o = Indici_di_Reliability_pre.values
        oo = Indici_di_Reliability_pre_norm.values

        values_init = pd.DataFrame((), index=('FRG', 'FNC', 'SFS'), columns=['ENS', 'SAIDI', 'SAIFI', 'F.OBIETTIVO'])
        values_init_nonorm = pd.DataFrame((), index=('FRG', 'FNC', 'SFS'),
                                          columns=['ENS', 'SAIDI', 'SAIFI', 'F.OBIETTIVO'])

        ONR_GLOBALE['Tecniche'] = dict()

        for i in ['FRG', 'FNC', 'SFS']:
            ONR_GLOBALE['Tecniche'][i] = dict()
            objf_pre = sum(Indici_di_Reliability_pre.loc[i][:])
            for j in ['ENS', 'SAIDI', 'SAIFI']:
                ONR_GLOBALE['Tecniche'][i][j] = dict()
                ONR_GLOBALE['Tecniche'][i][j]['indici_pre'] = dict()
                ONR_GLOBALE['Tecniche'][i][j]['indici_pre']['norm'] = dict()
                ONR_GLOBALE['Tecniche'][i][j]['indici_pre']['abs'] = dict()

                values_init.loc[i][j] = Indici_di_Reliability_pre_norm.loc[i][j]
                values_init_nonorm.loc[i][j] = Indici_di_Reliability_pre.loc[i][j]

                ONR_GLOBALE['Tecniche'][i][j]['indici_pre']['norm'] = values_init.loc[i][j]
                ONR_GLOBALE['Tecniche'][i][j]['indici_pre']['abs'] = values_init_nonorm.loc[i][j]

            ONR_GLOBALE['Tecniche'][i]['F.OBIETTIVO'] = dict()
            ONR_GLOBALE['Tecniche'][i]['F.OBIETTIVO']['indici_pre'] = dict()
            ONR_GLOBALE['Tecniche'][i]['F.OBIETTIVO']['indici_pre']['norm'] = dict()
            ONR_GLOBALE['Tecniche'][i]['F.OBIETTIVO']['indici_pre']['abs'] = dict()
            values_init.loc[i]['F.OBIETTIVO'] = 1 / 3 * sum(Indici_di_Reliability_pre_norm.loc[i][:])
            values_init_nonorm.loc[i]['F.OBIETTIVO'] = sum(Indici_di_Reliability_pre.loc[i][:])
            ONR_GLOBALE['Tecniche'][i]['F.OBIETTIVO']['indici_pre']['norm'] = values_init.loc[i]['F.OBIETTIVO']
            ONR_GLOBALE['Tecniche'][i]['F.OBIETTIVO']['indici_pre']['abs'] = values_init_nonorm.loc[i]['F.OBIETTIVO']

            ONR_ZONALE = dict()

            for i in lista_zone:
                ONR_ZONALE[i] = dict()
                ONR_ZONALE[i]['Topology'] = dict()
                ONR_ZONALE[i]['Topology']['Zone_connesse'] = zoneconnesse[i]
                ONR_ZONALE[i]['Topology']['Linee_contenute'] = zone_branches[i]
                ONR_ZONALE[i]['Topology']['Carichi_contenuti'] = zone_loads[i]
                ONR_ZONALE[i]['Topology']['Nodi_contenuti'] = zone_bus[i]
                if i in zone_capo_feeder:
                    ONR_ZONALE[i]['Topology']['Luogo'] = 'capo_feeder'
                elif i not in zone_capo_feeder and i in zonenosource:
                    ONR_ZONALE[i]['Topology']['Luogo'] = 'dorsale_feeder'
                elif i not in zone_capo_feeder and i not in zonenosource:
                    ONR_ZONALE[i]['Topology']['Luogo'] = 'source'

                ONR_ZONALE[i]['Reliability_par'] = dict()
                ONR_ZONALE[i]['Reliability_par']['f_z'] = dict()
                ONR_ZONALE[i]['Reliability_par']['U_z'] = dict()

                ONR_ZONALE[i]['Reliability_par']['f_z']['pre'] = f_z_FRG[i]
                ONR_ZONALE[i]['Reliability_par']['U_z']['pre'] = U_z_FRG[i]

                ONR_ZONALE[i]['Reliability_par']['f_z']['pre'] = f_z_FNC[i]
                ONR_ZONALE[i]['Reliability_par']['U_z']['pre'] = U_z_FNC[i]

                ONR_ZONALE[i]['Reliability_par']['f_z']['pre'] = f_z_SFS[i]
                ONR_ZONALE[i]['Reliability_par']['U_z']['pre'] = U_z_SFS[i]

        x = {
            "busfrom": busfrom,
            "linee": linee,
            "trafi": trafi,
            "branches": branches,
            "zone": lista_zone,
            "switch": switch,
            "zonenosource": zonenosource,
            "zoneconnesse_radiali": zoneconnesse_radiali,
            "zone_capo_feeder": zone_capo_feeder,
            "zone_connesse_allo_stesso_feeder": zone_connesse_allo_stesso_feeder,
            "statoinizialeswitch": stati_switch_iniziali,
            "switch_zone_from_to": switch_zone_from_to,
            "switch_zone_from": switch_zone_from,
            "switch_zone_to": switch_zone_to,
            "switch_non_apribili": switch_non_apribili,
            "ZoneReliability": ZoneReliability,
            "lambda_z_1": lambda_z_1,
            "lambda_z_2": lambda_z_2,
            "Zone_branch": zone_branches,
            "Zone_bus": zone_bus,
            "PDz": PDz,
            "PGz": PGz,
            "BranchesToLeaves": BranchesToLeaves,
            "Nzone": Nzone,
            # "ZonalGraph": ZonalGraph,
            'Indici_di_Reliability_pre': Indici_di_Reliability_pre,
            'Indici_di_Reliability_pre_norm': Indici_di_Reliability_pre_norm,
            'funzioniobiettivopre': Funzioni_obiettivo_pre,
            # 'f_zs_PRE':f_zs_PRE,
            'linee': linee,
            'bus': bus,
            'colordict': colordict,
            'scritte': scritte,
            'zonegraph': zonegraph,
        }

        V0 = self.LFviolations_pre(x, 'lf_pre', busfrom, linee, trafi)

        self.V0 = V0
        self.ONR_GLOBALE = ONR_GLOBALE
        self.ONR_ZONALE = ONR_ZONALE
        self.xx = x

        return V0, bus, x, ONR_GLOBALE, ONR_ZONALE

    def ONR(self, choice):

        V0, xx, ONR_GLOBALE, ONR_ZONALE = self.V0, self.xx, self.ONR_GLOBALE, self.ONR_ZONALE

        # choiche = (a, b, c) TODO: Ricorda!!!

        # %% ONR

        # CONCRETE OPTIMIZATION MODEL 2 - OPTIMAL NETWORK RECONFIGURATION ##

        # dssObj = win32com.client.Dispatch("OpenDSSEngine.DSS")
        # dssText = dssObj.Text
        # dssCircuit = dssObj.ActiveCircuit
        # dssSolution = dssCircuit.Solution
        # dssElem = dssCircuit.ActiveCktElement
        # dssBus = dssCircuit.ActiveBus
        # dssLines = dssCircuit.Lines
        # dssXfmr = dssCircuit.Transformers
        # dssLoads = dssCircuit.Loads
        # dssActiveClass = dssCircuit.ActiveClass
        # dssActiveBus = dssCircuit.ActiveBus

        busfrom = xx['busfrom']
        linee = xx['linee']
        trafi = xx['trafi']
        Funzioni_obiettivo_pre = xx['funzioniobiettivopre']
        lista_zone = xx['zone']
        switch = xx['switch']
        zonenosource = xx['zonenosource']
        zoneconnesse_radiali = xx['zoneconnesse_radiali']
        zone_connesse_allo_stesso_feeder = xx['zone_connesse_allo_stesso_feeder']
        zone_capo_feeder = xx['zone_capo_feeder']
        stati_switch_iniziali = xx['statoinizialeswitch']
        switch_zone_from_to = xx['switch_zone_from_to']
        switch_zone_from = xx['switch_zone_from']
        switch_non_apribili = xx['switch_non_apribili']
        switch_zone_to = xx['switch_zone_to']
        ZoneReliability = xx['ZoneReliability']
        lambda_z_1 = xx['lambda_z_1']
        lambda_z_2 = xx['lambda_z_2']
        zone_branches = xx['Zone_branch']
        zone_bus = xx['Zone_bus']
        PDz = xx['PDz']
        PGz = xx['PGz']
        BranchesToLeaves = xx['BranchesToLeaves']
        Nzone = xx['Nzone']
        # ZonalGraph=xx['ZonalGraph']
        Indici_di_Reliability_pre = xx['Indici_di_Reliability_pre']
        Indici_di_Reliability_pre_norm = xx['Indici_di_Reliability_pre_norm']
        colordict = xx['colordict']
        scritte = xx['scritte']
        zonegraph = xx['zonegraph']
        ENS_PRE_FRG = Indici_di_Reliability_pre.loc['FRG'][0]
        SAIDI_PRE_FRG = Indici_di_Reliability_pre.loc['FRG'][1]
        SAIFI_PRE_FRG = Indici_di_Reliability_pre.loc['FRG'][2]
        ENS_PRE_FNC = Indici_di_Reliability_pre.loc['FNC'][0]
        SAIDI_PRE_FNC = Indici_di_Reliability_pre.loc['FNC'][1]
        SAIFI_PRE_FNC = Indici_di_Reliability_pre.loc['FNC'][2]
        ENS_PRE_SFS = Indici_di_Reliability_pre.loc['SFS'][0]
        SAIDI_PRE_SFS = Indici_di_Reliability_pre.loc['SFS'][1]
        SAIFI_PRE_SFS = Indici_di_Reliability_pre.loc['SFS'][2]

        solverino = 'appsi_highs'
        solver = SolverFactory(solverino)

        if choice == 'a':
            tecnica_utilizzata = 'FRG'
        if choice == 'b':
            tecnica_utilizzata = 'FNC'
        if choice == 'c':
            tecnica_utilizzata = 'SFS'

        # print('');
        # print('Eseguo', tecnica_utilizzata, 'con solver', solverino, '...');
        # print('')
        self.log_post_solver = 'Eseguito ' + tecnica_utilizzata + ' con solver ' + solverino + '\n'

        tempo_iniziale = time.time()

        # Creazione del modello:
        ONR = ConcreteModel(name="(Optimal Network Reconfiguration)")

        #                  VARIABILI CONTINUE

        # ONR.teta = Var(bus, within=Reals, bounds=lambda ONR, i: (-pi/2,0),initialize={(i):theta0[i] for i in bus})

        prova = []
        for qi in zone_capo_feeder:
            for m in zonenosource:
                for k in zonenosource:
                    if int(k[1:]) <= int(m[1:]):
                        prova.append((qi, m, k))
        prova2 = []
        provarule = []
        for m in zonenosource:
            for k in zonenosource:
                if int(k[1:]) <= int(m[1:]):
                    prova2.append((m, k))
                    provarule.append(m)

        prova3 = []
        for m in lista_zone:
            for k in lista_zone:
                if int(k[1:]) <= int(m[1:]):
                    prova3.append((m, k))

        provaz_up = []
        for k in lista_zone:
            for l in switch_zone_from_to:
                i = switch_zone_from_to[l][0]
                # print(i,k)
                if int(i[1:]) <= int(k[1:]):
                    provaz_up.append((k, i))

        lista = []
        for i in switch_zone_from_to:
            if switch_zone_from_to[i][0] not in lista:
                lista.append(switch_zone_from_to[i][0])

        # IMPORTANTE LA FS

        ONR.fs = Var(lista_zone, within=Reals)
        ONR.fzs = Var(lista_zone, switch, within=Reals)
        ONR.lamb_z = Var(lista_zone, within=NonNegativeReals)
        ONR.ENS_POST = Var(within=NonNegativeReals)
        ONR.U_z = Var(lista_zone, within=NonNegativeReals)
        ONR.SAIDI_POST = Var(within=NonNegativeReals)
        ONR.SAIFI_POST = Var(within=NonNegativeReals)

        #                   VARIABILI BINARIE:
        # ONR.x_ij = Var(switch, within=Binary) #nessuna inizializzazione
        # ONR.x_ij = Var(switch, within=Binary,initialize={(s):1 for s in switch}) #stato iniziale tutto chiuso
        ONR.x_ij = Var(switch, within=Binary, initialize=stati_switch_iniziali)  # stato iniziale radiale
        # ONR.x_ij = Var(switch, within=Binary,initialize=stati_switch_best) #stato iniziale del Simulated Annealing

        ONR.Z_up = Var(lista_zone, lista_zone, within=Binary)
        # ONR.Z_up = Var(lista,lista_zone, within=Binary)

        # ONR.w_mk = Var(lista_zone,lista_zone, within=Binary)
        ONR.Z_f = Var(prova, within=Binary)

        # prova
        # ONR.Z_up = Var(matricione,within=Binary)
        ONR.w_mk = Var(prova2, within=Binary)

        # ONR.Z_f = Var(zone_capo_feeder, zonenosource, zonenosource,within=Binary)
        # fine prova
        #                   VARIABILI FISSATE:

        #                         VINCOLI:

        def Radialita_rule(ONR):
            # return sum(ONR.x_ij[s] for s in switch) + Nlinee + Ntrafi - Nzone + 1 == 0
            return sum(ONR.x_ij[s] for s in switch) - Nzone + 1 == 0

        ONR.Radialita = Constraint(rule=Radialita_rule)

        def FlussiArtificiali_rule(ONR, m, k):

            membroA = 0
            membroB = 0

            if m == k:
                membroB = 1

            for s in switch:

                i = switch_zone_from_to[s][0]
                j = switch_zone_from_to[s][1]

                if i == k:
                    membroA = membroA - ONR.fzs[m, s]

                if j == k:
                    membroA = membroA + ONR.fzs[m, s]

            if k == "z0":
                membroA = membroA + ONR.fs[m]
            # print('memA',membroA,'memB',membroB)
            return membroA == membroB

        ONR.FlussiArtificiali = Constraint(lista_zone, zonenosource, rule=FlussiArtificiali_rule)

        def stato_flusso_ij_switch_UB_rule(ONR, s, z):
            return ONR.fzs[z, s] <= ONR.x_ij[s]

        ONR.stato_flusso_ij_switch_UB = Constraint(switch, lista_zone, rule=stato_flusso_ij_switch_UB_rule)

        def stato_flusso_ij_switch_LB_rule(ONR, s, z):
            return ONR.fzs[z, s] >= - ONR.x_ij[s]

        ONR.stato_flusso_ij_switch_LB = Constraint(switch, lista_zone, rule=stato_flusso_ij_switch_LB_rule)

        pippo = []

        def zona_attiva_i_UB_rule(ONR, k, s):
            i = switch_zone_from_to[s][0]
            # if i==k:
            # #    return ONR.Z_up[i,k]==1
            # # # if (i, k) in pippo and :
            #     return Constraint.Skip  # Correctly return Constraint.Skip
            # else:
            # pippo.append((i,k))
            return ONR.Z_up[i, k] >= (ONR.fzs[k, s])

        ONR.zona_attiva_i_UB = Constraint(lista_zone, switch, rule=zona_attiva_i_UB_rule)

        pippo2 = []

        def zona_attiva_j_UB_rule(ONR, k, s):
            j = switch_zone_from_to[s][1]
            # if j==k:
            #    return ONR.Z_up[j,k]==1

            # if (j, k) in pippo:
            #     return Constraint.Skip  # Correctly return Constraint.Skip
            # else:
            # pippo2.append((k,s))
            return ONR.Z_up[j, k] >= (ONR.fzs[k, s])

        ONR.zona_attiva_j_UB = Constraint(lista_zone, switch, rule=zona_attiva_j_UB_rule)

        pippo = []

        def zona_attiva_i_LB_rule(ONR, k, s):
            i = switch_zone_from_to[s][0]
            # if i==k:
            #    return ONR.Z_up[i,k]==1

            # # print(i,k,s)
            # if (i, k) in pippo:
            # return Constraint.Skip  # Correctly return Constraint.Skip
            # else:
            # pippo.append((i,k))
            return ONR.Z_up[i, k] >= - ONR.fzs[k, s]

        ONR.zona_attiva_i_LB = Constraint(lista_zone, switch, rule=zona_attiva_i_LB_rule)

        def zona_attiva_j_LB_rule(ONR, k, s):
            j = switch_zone_from_to[s][1]
            # if j==k:
            #    return ONR.Z_up[j,k]==1

            # if (j, k) in pippo:
            #     return Constraint.Skip  # Correctly return Constraint.Skip
            # else:
            return ONR.Z_up[j, k] >= - ONR.fzs[k, s]

        ONR.zona_attiva_j_LB = Constraint(lista_zone, switch, rule=zona_attiva_j_LB_rule)

        # if scelta == 'a' or scelta == 'b':

        #     def zona_feeder_rule(ONR, qi, m, k):
        #         return (ONR.Z_f[qi, m, k] >= ONR.Z_up[qi, m] + ONR.Z_up[qi, k] - 1)
        #     ONR.zona_feeder = Constraint(zone_capo_feeder, zonenosource, zonenosource, rule=zona_feeder_rule)

        #     def Z_cug_rule(ONR, m, k):
        #         return ONR.w_mk[m, k] >= sum(ONR.Z_f[qi, m, k] for qi in zone_capo_feeder)
        #     ONR.Z_cug = Constraint(zonenosource, zonenosource, rule=Z_cug_rule)

        # =============================================================================
        # PROVA
        # =============================================================================

        if choice == 'a' or choice == 'b':
            # Definire la regola del vincolo
            def zona_feeder_rule(ONR, qi, m, k):
                return ONR.Z_f[qi, m, k] >= ONR.Z_up[qi, m] + ONR.Z_up[qi, k] - 1

            ONR.zona_feeder = Constraint(prova, rule=zona_feeder_rule)

            def Z_cug_rule(ONR, m, k):
                return ONR.w_mk[m, k] >= sum(ONR.Z_f[qi, m, k] for qi in zone_capo_feeder)

            ONR.Z_cug = Constraint(prova2, rule=Z_cug_rule)

        # =============================================================================
        # FINE ROVA
        # =============================================================================

        if choice == 'a':
            # FRG:
            def Average_failure_FRG_rule(ONR, z):
                sommatoria = 0
                if z == 'z0':
                    return ONR.lamb_z[z] == 0
                else:
                    for k in zonenosource:
                        if (k, z) in prova2:
                            sommatoria += (ONR.w_mk[k, z] * ZoneReliability.Lambda_z[k])
                        else:
                            sommatoria += (ONR.w_mk[z, k] * ZoneReliability.Lambda_z[k])
                    return ONR.lamb_z[z] == sommatoria

            ONR.Average_failure_FRG = Constraint(lista_zone, rule=Average_failure_FRG_rule)

            def FRG_rule(ONR, z):
                somma = 0
                if z == 'z0':
                    return ONR.U_z[z] == 0
                else:
                    for k in zonenosource:
                        if (k, z) in prova2:
                            somma += ((ONR.Z_up[k, z] * ZoneReliability.Lambda_z[k] * ZoneReliability.R_z[k]) + (
                                    (ONR.w_mk[k, z] - ONR.Z_up[k, z]) * ZoneReliability.Lambda_z[k] * 0.05))
                        else:
                            somma += ((ONR.Z_up[k, z] * ZoneReliability.Lambda_z[k] * ZoneReliability.R_z[k]) + (
                                    (ONR.w_mk[z, k] - ONR.Z_up[k, z]) * ZoneReliability.Lambda_z[k] * 0.05))
                    return ONR.U_z[z] == somma

            ONR.FRG = Constraint(lista_zone, rule=FRG_rule)

        if choice == 'b':
            # FNC:
            # =============================================================================
            #     DA VEDERE L'AVERAGE
            # =============================================================================
            def Average_failure_FNC_rule(ONR, z):
                sommatoria = 0
                if z == 'z0':
                    return ONR.lamb_z[z] == 0
                else:
                    for k in zonenosource:
                        if (k, z) in prova2:
                            sommatoria += ((ONR.Z_up[k, z] * ZoneReliability.Lambda_z_1[k]) + (
                                    ONR.w_mk[k, z] * ZoneReliability.Lambda_z_2[k]))
                        else:
                            sommatoria += ((ONR.Z_up[k, z] * ZoneReliability.Lambda_z_1[k]) + (
                                    ONR.w_mk[z, k] * ZoneReliability.Lambda_z_2[k]))

                    return ONR.lamb_z[z] == sommatoria

            ONR.Average_failure_FNC = Constraint(lista_zone, rule=Average_failure_FNC_rule)

            def FNC_rule(ONR, z):
                somma = 0
                if z == 'z0':
                    return ONR.U_z[z] == 0
                else:
                    for k in zonenosource:
                        if (k, z) in prova2:
                            somma += ((ONR.Z_up[k, z] * (lambda_z_1[k] + ZoneReliability.Lambda_z_2[k]) *
                                       ZoneReliability.R_z[k]) + (
                                              (ONR.w_mk[k, z] - ONR.Z_up[k, z]) * ZoneReliability.Lambda_z_2[
                                          k] * 0.05))
                        else:
                            somma += ((ONR.Z_up[k, z] * (lambda_z_1[k] + ZoneReliability.Lambda_z_2[k]) *
                                       ZoneReliability.R_z[k]) + (
                                              (ONR.w_mk[z, k] - ONR.Z_up[k, z]) * ZoneReliability.Lambda_z_2[
                                          k] * 0.05))
                    return ONR.U_z[z] == somma

            ONR.FNC = Constraint(lista_zone, rule=FNC_rule)

        if choice == 'c':
            # SFS:
            def Average_failure_SFS_rule(ONR, z):
                sommatoria = 0
                if z == 'z0':
                    return ONR.lamb_z[z] == 0
                else:
                    for k in zonenosource:
                        sommatoria += (ONR.Z_up[k, z] * ZoneReliability.Lambda_z[k])
                    return ONR.lamb_z[z] == sommatoria

            ONR.Average_failure_SFS = Constraint(lista_zone, rule=Average_failure_SFS_rule)

            def SFS_rule(ONR, z):
                if z == 'z0':
                    return ONR.U_z[z] == 0
                else:
                    return ONR.U_z[z] == sum(
                        (ONR.Z_up[k, z] * ZoneReliability.Lambda_z[k] * ZoneReliability.R_z[k]) for k in zonenosource)

            ONR.SFS = Constraint(lista_zone, rule=SFS_rule)

        def EnergiaNonServita_rule(ONR):
            return ONR.ENS_POST == sum(PDz[z] * ONR.U_z[z] for z in lista_zone)

        ONR.EnergiaNonServita = Constraint(rule=EnergiaNonServita_rule)

        def SAIDI_definition_rule(ONR):
            return ONR.SAIDI_POST == sum(ZoneReliability.Clienti[z] * ONR.U_z[z] for z in lista_zone) / sum(
                ZoneReliability.Clienti)

        ONR.SAIDI_definition = Constraint(rule=SAIDI_definition_rule)

        def SAIFI_definition_rule(ONR):
            return ONR.SAIFI_POST == sum(ZoneReliability.Clienti[z] * ONR.lamb_z[z] for z in lista_zone) / sum(
                ZoneReliability.Clienti)

        ONR.SAIFI_definition = Constraint(rule=SAIFI_definition_rule)

        #                           FUNZIONE OBIETTIVO:

        def ObjectiveFunctionONR_rule(ONR):
            alfa_ENS = (1 / 3) / ENS_PRE_FRG
            alfa_SAIDI = (1 / 3) / SAIDI_PRE_FRG
            alfa_SAIFI = (1 / 3) / SAIFI_PRE_FRG
            return alfa_ENS * ONR.ENS_POST + alfa_SAIDI * ONR.SAIDI_POST + alfa_SAIFI * ONR.SAIFI_POST

        ONR.ObjectiveFunction = Objective(rule=ObjectiveFunctionONR_rule, sense=minimize)

        # %% RISULTATI
        # =============================================================================

        results = solver.solve(ONR)  # tee=True
        print(results)
        self.log_post_solver = self.log_post_solver + str(results) + '\n'

        if results.solver.termination_condition == TerminationCondition.optimal:
            # print('')
            # print("ONR è stato risolto con successo e tutti i vincoli sono rispettati!")
            self.log_post_solver = self.log_post_solver + "ONR è stato risolto con successo e tutti i vincoli sono rispettati!\n\n"
            ONR.solutions.load_from(results)
            # RISULTATI ONR:
            ObjF_ONR = ONR.ObjectiveFunction()
            tempo_finale = time.time()
            tempo_trascorso = tempo_finale - tempo_iniziale
            # print('')
            # print(f"Tempo trascorso per il metodo analitico con solver {solverino}:", tempo_trascorso, "secondi")
            # print('')
            # print('Funzione Obiettivo pre-ONR:', Funzioni_obiettivo_pre.loc[tecnica_utilizzata, 'Funzione obiettivo'])
            # print('Funzione Obiettivo post-ONR:', ObjF_ONR)
            # print('');
            # print('ENS pre-ONR:', Indici_di_Reliability_pre.loc[tecnica_utilizzata, 'ENS'], 'kWh/anno')
            # print('ENS post-ONR:', ONR.ENS_POST.value, 'kwh/anno')
            # print('');
            # print('SAIDI pre-ONR:', Indici_di_Reliability_pre.loc[tecnica_utilizzata, 'SAIDI'], 'ore/anno')
            # print('SAIDI post-ONR:', ONR.SAIDI_POST.value, 'ore/anno')
            # print('');
            # print('SAIFI pre-ONR:', Indici_di_Reliability_pre.loc[tecnica_utilizzata, 'SAIFI'], 'guasti/anno')
            # print('SAIFI post-ONR:', ONR.SAIFI_POST.value, 'guasti/anno')
            # self.log_post_solver = self.log_post_solver + (f"Tempo trascorso per il metodo analitico con solver {solverino}:" + tempo_trascorso + "secondi\n")

            self.indexes_post = {
                'pre': {
                    'EENS': Indici_di_Reliability_pre.loc[tecnica_utilizzata, 'ENS'],
                    'SAIDI': Indici_di_Reliability_pre.loc[tecnica_utilizzata, 'SAIDI'],
                    'SAIFI': Indici_di_Reliability_pre.loc[tecnica_utilizzata, 'SAIFI'],
                    'FOB': Funzioni_obiettivo_pre.loc[tecnica_utilizzata, 'Funzione obiettivo'],
                },
                'post': {
                    'EENS': ONR.ENS_POST.value,
                    'SAIDI': ONR.SAIDI_POST.value,
                    'SAIFI': ONR.SAIFI_POST.value,
                    'FOB': ObjF_ONR,
                },
            }

        elif results.solver.termination_condition == TerminationCondition.infeasible:
            # print("ONR è irrealizzabile, alcuni vincoli non sono rispettati.")
            self.log_pre_solver += "ONR è irrealizzabile, alcuni vincoli non sono rispettati.\n"
            sys.exit()
        else:
            # print(
            #     "Il solver ha terminato con uno stato diverso da 'ottimale', è bene verificare il modello e i vincoli.")
            self.log_pre_solver += ("OIl solver ha terminato con uno stato diverso da 'ottimale', è bene verificare il "
                                    "modello e i vincoli.\n")
        # print('')

        if choice == 'a':
            ENS_POST_FRG = ONR.ENS_POST.value
            SAIFI_POST_FRG = ONR.SAIFI_POST.value
            SAIDI_POST_FRG = ONR.SAIDI_POST.value
            funzione_obiettivo_post_FRG = ObjF_ONR

            Indici_di_Reliability_post = pd.DataFrame(np.zeros((1, 4)), index=[tecnica_utilizzata],
                                                      columns=['ENS', 'SAIDI', 'SAIFI', 'F.obj'])
            Indici_di_Reliability_post.loc[tecnica_utilizzata, 'ENS'] = ENS_POST_FRG
            Indici_di_Reliability_post.loc[tecnica_utilizzata, 'SAIDI'] = SAIDI_POST_FRG
            Indici_di_Reliability_post.loc[tecnica_utilizzata, 'SAIFI'] = SAIFI_POST_FRG
            Indici_di_Reliability_post.loc[tecnica_utilizzata, 'F.obj'] = ObjF_ONR

            Indici_di_Reliability_post_norm = pd.DataFrame(np.zeros((1, 4)), index=[tecnica_utilizzata],
                                                           columns=['ENS', 'SAIDI', 'SAIFI', 'F.obj'])
            Indici_di_Reliability_post_norm.loc[tecnica_utilizzata, 'ENS'] = ENS_POST_FRG / ENS_PRE_FRG
            Indici_di_Reliability_post_norm.loc[tecnica_utilizzata, 'SAIDI'] = SAIDI_POST_FRG / SAIDI_PRE_FRG
            Indici_di_Reliability_post_norm.loc[tecnica_utilizzata, 'SAIFI'] = SAIFI_POST_FRG / SAIFI_PRE_FRG
            Indici_di_Reliability_post_norm.loc[tecnica_utilizzata, 'F.obj'] = ObjF_ONR / Funzioni_obiettivo_pre.loc[
                'FRG', 'Funzione obiettivo']

            Indici_di_Reliability_pre_norm_graph = pd.DataFrame(np.zeros((1, 4)), index=[tecnica_utilizzata],
                                                                columns=['ENS', 'SAIDI', 'SAIFI', 'F.obj'])
            Indici_di_Reliability_pre_norm_graph.loc[tecnica_utilizzata, 'ENS'] = ENS_PRE_FRG / ENS_PRE_FRG
            Indici_di_Reliability_pre_norm_graph.loc[tecnica_utilizzata, 'SAIDI'] = SAIDI_PRE_FRG / SAIDI_PRE_FRG
            Indici_di_Reliability_pre_norm_graph.loc[tecnica_utilizzata, 'SAIFI'] = SAIFI_PRE_FRG / SAIFI_PRE_FRG
            Indici_di_Reliability_pre_norm_graph.loc[tecnica_utilizzata, 'F.obj'] = Funzioni_obiettivo_pre.loc[
                tecnica_utilizzata, 'Funzione obiettivo']

        if choice == 'b':
            ENS_POST_FNC = ONR.ENS_POST.value
            SAIFI_POST_FNC = ONR.SAIFI_POST.value
            SAIDI_POST_FNC = ONR.SAIDI_POST.value
            funzione_obiettivo_post_FNC = ObjF_ONR

            Indici_di_Reliability_post = pd.DataFrame(np.zeros((1, 4)), index=[tecnica_utilizzata],
                                                      columns=['ENS', 'SAIDI', 'SAIFI', 'F.obj'])
            Indici_di_Reliability_post.loc[tecnica_utilizzata, 'ENS'] = ENS_POST_FNC
            Indici_di_Reliability_post.loc[tecnica_utilizzata, 'SAIDI'] = SAIDI_POST_FNC
            Indici_di_Reliability_post.loc[tecnica_utilizzata, 'SAIFI'] = SAIFI_POST_FNC
            Indici_di_Reliability_post.loc[tecnica_utilizzata, 'F.obj'] = ObjF_ONR

            Indici_di_Reliability_post_norm = pd.DataFrame(np.zeros((1, 4)), index=[tecnica_utilizzata],
                                                           columns=['ENS', 'SAIDI', 'SAIFI', 'F.obj'])
            Indici_di_Reliability_post_norm.loc[tecnica_utilizzata, 'ENS'] = ENS_POST_FNC / ENS_PRE_FRG
            Indici_di_Reliability_post_norm.loc[tecnica_utilizzata, 'SAIDI'] = SAIDI_POST_FNC / SAIDI_PRE_FRG
            Indici_di_Reliability_post_norm.loc[tecnica_utilizzata, 'SAIFI'] = SAIFI_POST_FNC / SAIFI_PRE_FRG
            Indici_di_Reliability_post_norm.loc[tecnica_utilizzata, 'F.obj'] = ObjF_ONR / Funzioni_obiettivo_pre.loc[
                'FRG', 'Funzione obiettivo']

            Indici_di_Reliability_pre_norm_graph = pd.DataFrame(np.zeros((1, 4)), index=[tecnica_utilizzata],
                                                                columns=['ENS', 'SAIDI', 'SAIFI', 'F.obj'])
            Indici_di_Reliability_pre_norm_graph.loc[tecnica_utilizzata, 'ENS'] = ENS_PRE_FNC / ENS_PRE_FRG
            Indici_di_Reliability_pre_norm_graph.loc[tecnica_utilizzata, 'SAIDI'] = SAIDI_PRE_FNC / SAIDI_PRE_FRG
            Indici_di_Reliability_pre_norm_graph.loc[tecnica_utilizzata, 'SAIFI'] = SAIFI_PRE_FNC / SAIFI_PRE_FRG
            Indici_di_Reliability_pre_norm_graph.loc[tecnica_utilizzata, 'F.obj'] = Funzioni_obiettivo_pre.loc[
                tecnica_utilizzata, 'Funzione obiettivo']

        if choice == 'c':
            ENS_POST_SFS = ONR.ENS_POST.value
            SAIFI_POST_SFS = ONR.SAIFI_POST.value
            SAIDI_POST_SFS = ONR.SAIDI_POST.value
            funzione_obiettivo_post_SFS = ObjF_ONR

            Indici_di_Reliability_post = pd.DataFrame(np.zeros((1, 4)), index=[tecnica_utilizzata],
                                                      columns=['ENS', 'SAIDI', 'SAIFI', 'F.obj'])
            Indici_di_Reliability_post.loc[tecnica_utilizzata, 'ENS'] = ENS_POST_SFS
            Indici_di_Reliability_post.loc[tecnica_utilizzata, 'SAIDI'] = SAIDI_POST_SFS
            Indici_di_Reliability_post.loc[tecnica_utilizzata, 'SAIFI'] = SAIFI_POST_SFS
            Indici_di_Reliability_post.loc[tecnica_utilizzata, 'F.obj'] = ObjF_ONR

            Indici_di_Reliability_post_norm = pd.DataFrame(np.zeros((1, 4)), index=[tecnica_utilizzata],
                                                           columns=['ENS', 'SAIDI', 'SAIFI', 'F.obj'])
            Indici_di_Reliability_post_norm.loc[tecnica_utilizzata, 'ENS'] = ENS_POST_SFS / ENS_PRE_FRG
            Indici_di_Reliability_post_norm.loc[tecnica_utilizzata, 'SAIDI'] = SAIDI_POST_SFS / SAIDI_PRE_FRG
            Indici_di_Reliability_post_norm.loc[tecnica_utilizzata, 'SAIFI'] = SAIFI_POST_SFS / SAIFI_PRE_FRG
            Indici_di_Reliability_post_norm.loc[tecnica_utilizzata, 'F.obj'] = ObjF_ONR / Funzioni_obiettivo_pre.loc[
                'FRG', 'Funzione obiettivo']

            Indici_di_Reliability_pre_norm_graph = pd.DataFrame(np.zeros((1, 4)), index=[tecnica_utilizzata],
                                                                columns=['ENS', 'SAIDI', 'SAIFI', 'F.obj'])
            Indici_di_Reliability_pre_norm_graph.loc[tecnica_utilizzata, 'ENS'] = ENS_PRE_SFS / ENS_PRE_FRG
            Indici_di_Reliability_pre_norm_graph.loc[tecnica_utilizzata, 'SAIDI'] = SAIDI_PRE_SFS / SAIDI_PRE_FRG
            Indici_di_Reliability_pre_norm_graph.loc[tecnica_utilizzata, 'SAIFI'] = SAIFI_PRE_SFS / SAIFI_PRE_FRG
            Indici_di_Reliability_pre_norm_graph.loc[tecnica_utilizzata, 'F.obj'] = Funzioni_obiettivo_pre.loc[
                tecnica_utilizzata, 'Funzione obiettivo']

        f_ijk_POST = ONR.fzs.extract_values()
        f_zs_POST = ONR.fs.extract_values()
        x_ij_POST = ONR.x_ij.extract_values()
        lamb_POST = ONR.lamb_z.extract_values()
        U_z_POST = ONR.U_z.extract_values()
        Z_POST = ONR.Z_up.extract_values()
        w_POST = ONR.w_mk.extract_values()
        w_i_POST = ONR.Z_f.extract_values()

        # %% Grafici POST ONR ENS, SAIDI, SAIFI

        post_indexes_fig = plt.figure(3, figsize=(6, 6))
        positions = np.arange(len(Indici_di_Reliability_post_norm.columns))
        plt.bar(Indici_di_Reliability_pre_norm_graph.columns,
                Indici_di_Reliability_pre_norm_graph.loc[tecnica_utilizzata], width=0.4,
                color=['#FFA07A', '#FF7F50', '#FF6347', 'red'], edgecolor='black', label='pre ONR')
        plt.bar(positions + 0.5, Indici_di_Reliability_post_norm.loc[tecnica_utilizzata], width=0.4,
                color=['#ADD8E6', '#87CEEB', '#4682B4', '#1E3A5F'], edgecolor='black', label='post ONR')

        plt.ylim(0, 1.2)
        plt.locator_params(axis='y', nbins=15)
        plt.xlabel('Power supply quality indices', fontsize=15)
        plt.ylabel('Normalized Values', fontsize=15)
        plt.xticks(positions + 0.25, Indici_di_Reliability_post_norm.columns)

        formatter = ScalarFormatter()
        formatter.set_scientific(True)
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.legend(loc='best')

        # plt.show()
        post_indexes_fig.savefig(self.filedir + 'indexes_post.png')

        # %%DIZIONARIO CON I VALORI DEI VINCOLI
        # Crea un dizionario vuoto per memorizzare i valori delle espressioni di vincolo
        constraint_values = defaultdict(dict)

        # Scorrere tutti gli oggetti Constraint attivi in ONR
        for c in ONR.component_objects(Constraint, active=True):
            for index in c:
                # Calcola il valore dell'espressione del vincolo
                value_of_constraint = value(c[index])
                # Aggiungi il valore all'elenco di valori associato all'espressione di vincolo nel dizionario
                constraint_values[c][index] = value_of_constraint

        # Creo e riempio i dizionari con i risultati delle variabili di ottimizzazione:

        x_ij_opt = {(s): 0 for s in switch}

        for s in switch:
            x_ij_opt[s] = round(value(ONR.x_ij[s]), 1)

        # cug_POST = ONR.Z_cug.extract_values()

        w_POST = ONR.w_mk.extract_values()
        w_i_POST = ONR.Z_f.extract_values()
        U_z_POST = ONR.U_z.extract_values()
        Z_up_POST = ONR.Z_up.extract_values()
        fzs_POST = ONR.fzs.extract_values()

        # RISULTATI OTTIMIZZAZIONE E TOPOLOGIA FINALE

        # Topologia ottenuta dall'ottimizzazione:

        stati_switch_finale = {(s): stati_switch_iniziali[s] for s in switch}
        for s in switch:
            if x_ij_opt[s] == 0:
                # print(v[s])
                v[s]['par']['out-of-service'] = True
                stati_switch_finale[s] = 0
            else:
                # print(v[s])
                v[s]['par']['out-of-service'] = False
                stati_switch_finale[s] = 1

        Nswitch = len(stati_switch_iniziali)

        # Creo DataFrame con gli switch, zonefrom, zoneto e stati switch iniziali e finali
        StatiSwitchesFinali = pd.DataFrame(np.zeros((Nswitch, 4)),
                                           columns=['Zona from', 'Zona to', 'Stato iniziale', 'Stato finale'],
                                           index=switch)

        for s in switch:
            StatiSwitchesFinali.at[s, 'Zona from'] = switch_zone_from[s]
            StatiSwitchesFinali.at[s, 'Zona to'] = switch_zone_to[s]
            if stati_switch_iniziali[s] == 0:
                StatiSwitchesFinali.at[s, 'Stato iniziale'] = 'aperto'
            elif stati_switch_iniziali[s] == 1:
                StatiSwitchesFinali.at[s, 'Stato iniziale'] = 'chiuso'
            if stati_switch_finale[s] == 0:
                StatiSwitchesFinali.at[s, 'Stato finale'] = 'aperto'
            elif stati_switch_finale[s] == 1:
                StatiSwitchesFinali.at[s, 'Stato finale'] = 'chiuso'

        # with pd.ExcelWriter(r'C:\Users\gaeta\Politecnico di Bari\COMETA ROBERTO - Gaetano Pascale\\Excel\Stati Switch finali.xlsx') as writer:
        #     StatiSwitchesFinali.to_excel(writer)

        # Conto quante aperture e chiusure di linea sono avvenute rispetto alla topologia radiale iniziale:

        aperture = 0;
        chiusure = 0
        switch_che_si_aprono_post_ONR = []
        switch_che_si_chiudono_post_ONR = []
        for s in switch:
            if stati_switch_iniziali[s] == 1 and stati_switch_finale[s] == 0:
                aperture = aperture + 1
                # print('Lo switch ' + s + ' si è aperto')
                self.log_post_switch += 'Lo switch ' + s + ' si è aperto\n'
                switch_che_si_aprono_post_ONR.append(s)
            if stati_switch_iniziali[s] == 0 and stati_switch_finale[s] == 1:
                chiusure = chiusure + 1
                # print('Lo switch ' + s + ' si è chiuso')
                self.log_post_switch += 'Lo switch ' + s + ' si è chiuso\n'
                switch_che_si_chiudono_post_ONR.append(s)

        # print('')
        # print('Il numero di aperture effettuate è', aperture)
        self.log_post_switch += '\nIl numero di aperture effettuate è ' + str(aperture)

        # print('Il numero di chiusure effettuate è', chiusure)
        self.log_post_switch += '\nIl numero di chiusure effettuate è ' + str(chiusure)

        # Conto i rami aperti e chiusi:
        Nramiaperti = round(sum(1 - x_ij_opt[s] for s in switch))
        self.log_post_switch + "\n\nIl numero di rami aperti è " + str(Nramiaperti)
        # print('Il numero di rami aperti è', Nramiaperti)
        Nramichiusi = Nswitch - Nramiaperti
        # print('Il numero di rami chiusi è', Nramichiusi)
        self.log_post_switch + "\nIl numero di rami chiusi è " + str(Nramichiusi)

        switch_chiusi_post_ONR = []

        for chiave, stato in stati_switch_finale.items():
            if stato == 1:
                switch_chiusi_post_ONR.append(chiave)

        ssss = {}
        for i in switch:
            if i in switch_chiusi_post_ONR:
                ssss[i] = 1
            else:
                ssss[i] = 0

        # Trovo gli switch che hanno stati differenti tra il MISOCP e Simuated Annealing:
        # switch_con_stati_diversi = []
        # for s in switch:
        #     if stati_switch_finale[s] != stati_switch_best[s]:
        #         switch_con_stati_diversi.append(s)
        # print('')
        # print('Gli switch con stati diversi tra MISOCP e SA sono',len(switch_con_stati_diversi))

        ### Grafo zonale post ONR con NetworkX
        def Creazione_grafo_zonale3(lista_zone, switch_chiusi_post_ONR):
            G = nx.MultiGraph()
            # Aggiunta dei nodi al grafo
            G.add_nodes_from(lista_zone)
            # Aggiunta degli archi al grafo
            for s in switch_chiusi_post_ONR:
                i = switch_zone_from[s]
                j = switch_zone_to[s]
                G.add_edge(i, j, label=switch)
            # Connectivity Check:
            is_connected = nx.is_connected(G)
            # print('')
            # print('Il grafo della rete zonale post ONR ha', nx.number_of_nodes(G), 'nodi e', nx.number_of_edges(G),
            #       'rami connessi.')
            # print(f'La rete zonale post ONR è connessa? {is_connected}')

            self.log_post_switch += ('\n\nIl grafo della rete zonale post ONR ha ' + str(nx.number_of_nodes(G)) +
                                     ' nodi e ' + str(nx.number_of_edges(G)) + ' rami connessi.')
            if is_connected: conn = ''
            else: conn = 'non'
            self.log_post_switch += '\nLa rete zonale post ONR ' + conn + ' è connessa.'

            grafo = nx.Graph(G)
            return grafo

        NX_grafo_zonale_post_ONR = Creazione_grafo_zonale3(lista_zone, switch_chiusi_post_ONR)

        # Check presenza di maglie
        loops_zone_afterONR = list(nx.simple_cycles(NX_grafo_zonale_post_ONR))
        if not loops_zone_afterONR:
            # print('')
            # print("Il grafo post ONR non contiene maglie.")
            self.log_post_switch += "\n\nIl grafo post ONR non contiene maglie."
        else:
            # print("Il grafo post ONR contiene ALMENO una maglia.")
            self.log_post_switch += "\n\nIl grafo post ONR contiene ALMENO una maglia."


        # %% GRAFO FINALE POST_ONR ZONALE

        if tecnica_utilizzata == 'FRG':
            scelta = 'a'
        if tecnica_utilizzata == 'FNC':
            scelta = 'b'
        if tecnica_utilizzata == 'SFS':
            scelta = 'c'

        if scelta == 'a':
            Grafo_zone_radiale = graphviz.Digraph(comment='Grafo zone radiali - ONR Topology - FRG')
        if scelta == 'b':
            Grafo_zone_radiale = graphviz.Digraph(comment='Grafo zone radiali - ONR Topology - FNC')
        if scelta == 'c':
            Grafo_zone_radiale = graphviz.Digraph(comment='Grafo zone radiali - ONR Topology - SFS')
        # Imposta le dimensioni della pagina e altre opzioni di visualizzazione:
        Grafo_zone_radiale.attr(size='8,10!', orientation='portrait', layout='dot', seed='927')
        # Costruzione del grafo:
        for i in range(Nzone):
            if lista_zone[i] == 'z0':
                Grafo_zone_radiale.node(str(i), label=f'{lista_zone[i]}', shape='circle', fontname='Arial Bold',
                                        color='black', fillcolor='white', style='filled', fixedsize='true', width='0.5',
                                        height='0.5', fontsize='14', pos='c', penwidth='3.0')
            elif lista_zone[i] in zone_capo_feeder and PGz[lista_zone[i]] != 0:
                Grafo_zone_radiale.node(str(i), label=f'{lista_zone[i]}', shape='triangle', fontname='Arial Bold',
                                        color='black', fontcolor=scritte[lista_zone[i]],
                                        fillcolor=colordict[lista_zone[i]], style='filled', fixedsize='true',
                                        width='0.6', height='0.6', fontsize='14', pos='c', penwidth='1.2')
            elif lista_zone[i] in zone_capo_feeder:
                Grafo_zone_radiale.node(str(i), label=f'{lista_zone[i]}', shape='circle', fontname='Arial Bold',
                                        color='black', fontcolor=scritte[lista_zone[i]],
                                        fillcolor=colordict[lista_zone[i]], style='filled', fixedsize='true',
                                        width='0.5', height='0.5', fontsize='14', pos='c', penwidth='1.2')
            else:
                for j in zonegraph:
                    if lista_zone[i] in zonegraph[j] and PGz[lista_zone[i]] == 0:
                        Grafo_zone_radiale.node(str(i), label=f'{lista_zone[i]}', shape='circle', fontname='Arial Bold',
                                                color='black', fontcolor=scritte[j], fillcolor=colordict[j],
                                                style='filled', fixedsize='true', width='0.5', height='0.5',
                                                fontsize='14', pos='c', penwidth=('1.2'))
                    if lista_zone[i] in zonegraph[j] and PGz[lista_zone[i]] != 0:
                        Grafo_zone_radiale.node(str(i), label=f'{lista_zone[i]}', shape='triangle',
                                                fontname='Arial Bold', color='black', fontcolor=scritte[j],
                                                fillcolor=colordict[j], style='filled', fixedsize='true', width='0.6',
                                                height='0.6', fontsize='14', pos='c', penwidth=('1.2'))

        fromzone = []
        tozone = []
        indfrom = []
        indto = []
        indice = []
        for r in switch_chiusi_post_ONR:
            # if r not in switch_che_si_chiudono_post_ONR:
            fromzone.append(switch_zone_from_to[r][0])
            tozone.append(switch_zone_from_to[r][1])
            from_zone = switch_zone_from_to[r][0]
            to_zone = switch_zone_from_to[r][1]
            ind_from = lista_zone.index(from_zone)
            ind_to = lista_zone.index(to_zone)
            indice.append((ind_from, ind_to))
            indfrom.append(lista_zone.index(from_zone))
            indto.append(lista_zone.index(to_zone))
        indice = sorted(indice, key=lambda x: x[
            0])  # Grafo_zone_radiale.edge(str(ind_from), str(ind_to), color='black' ,arrowhead='none', constraint='true', penwidth='2.0')
        indfrom = sorted(indfrom)
        indto = sorted(indto)

        indfromo = []
        indtoto = []
        index = []
        for i in range(len(indice)):
            if indice[i][0] == 0:
                index.append(indice[i][:])
                indfromo.append(indice[i][0])
                indtoto.append(indice[i][1])
        while len(index) < len(lista_zone) - 1:

            for i in range(len(indice)):
                for j in range(len(index)):
                    if indice[i][0] in index[j] and indice[i][0] != 0 and indice[i][:] not in index:
                        index.append(indice[i][:])
                        indfromo.append(indice[i][0])
                        indtoto.append(indice[i][1])

            for i in range(len(indice)):
                for j in range(len(index)):
                    if ((indice[i][1] in index[j]) and indice[i][1] != 0) and (indice[i][:] not in index):
                        index.append(indice[i][:])
                        indfromo.append(indice[i][1])
                        indtoto.append(indice[i][0])

        for i in range(len(indice)):
            for j in range(len(index)):
                if ((indice[i][1] in index[j]) and indice[i][1] != 0) and (indice[i][:] not in index):
                    index.append(indice[i][:])
                    indfromo.append(indice[i][1])
                    indtoto.append(indice[i][0])

        c = []
        for i in switch_che_si_chiudono_post_ONR:
            c.append((switch_zone_from_to[i][0], switch_zone_from_to[i][1]))

        # Z=0
        for i in range(len(index)):
            for j in switch_zone_from_to.keys():
                if lista_zone.index(switch_zone_from_to[j][0]) == index[i][0] and lista_zone.index(
                        switch_zone_from_to[j][1]) == index[i][1] or lista_zone.index(switch_zone_from_to[j][0]) == \
                        index[i][1] and lista_zone.index(switch_zone_from_to[j][1]) == index[i][0]:
                    Grafo_zone_radiale.edge(str(indfromo[i]), str(indtoto[i]), label=f'{j}', color='red',
                                            arrowhead='none', constraint='true', penwidth='2.0')

        # TODO: perché serve questo "if"?
        if scelta == 'a':
            Grafo_zone_radiale.render(filename=self.filedir + 'Grafo_zonale_post_ONR', format='png', cleanup=True)
        if scelta == 'b':
            Grafo_zone_radiale.render(filename=self.filedir + 'Grafo_zonale_post_ONR', format='png', cleanup=True)
        if scelta == 'c':
            Grafo_zone_radiale.render(filename=self.filedir + 'Grafo_zonale_post_ONR', format='png', cleanup=True)
        # Grafo_zone_radiale.view()

        for i in switch_non_apribili:
            if (StatiSwitchesFinali.loc[i]['Stato finale']) != 'chiuso':
                print('ATTENZIONEEEEEEEEEEE')

        for i, j in Z_up_POST.keys():
            if i == j and round(Z_up_POST[i, j], 1) != 1:
                print('ATTENZIONE, ij NON COINCIDONO')

        for i in zone_capo_feeder:
            for j in lista_zone:
                if Z_up_POST[j, i] == 1 and i != j and j != 'z0':
                    print('OH NO', j, i)

        valori_iniziali = list(stati_switch_iniziali.values())
        valori_finali = list(stati_switch_finale.values())
        transition = [i - f for i, f in zip(valori_iniziali, valori_finali)]
        transizione = pd.DataFrame(transition, index=switch, columns=['STATO'])
        transizionee = transizione['STATO']

        self.ONR_POST(transizionee)
        self.ONR_SF()

        ONR_GLOBALE['Tecniche']['Tecnica_utilizzata'] = tecnica_utilizzata

        ENS_POST = ONR.ENS_POST.value

        SAIDI_POST = ONR.SAIDI_POST.value

        SAIFI_POST = ONR.SAIFI_POST.value

        if choice == 'a':
            x = 0
        if choice == 'b':
            x = 1
        if choice == 'c':
            x = 2

        o = Indici_di_Reliability_pre.values
        oo = Indici_di_Reliability_pre_norm.values

        objf_pre = sum(oo[x, :])
        objf_post = ENS_POST / o[x, 0] * oo[x, 0] + SAIDI_POST / o[x, 1] * oo[x, 1] + SAIFI_POST / o[x, 2] * oo[x, 2]

        objf_post_nonorm = ENS_POST + SAIDI_POST + SAIFI_POST

        values_init_nonorm = [o[x, 0], o[x, 1], o[x, 2], sum(o[x, :])]
        values_post_nonorms = [ENS_POST, SAIDI_POST, SAIFI_POST, objf_post_nonorm]

        objf_pre = sum(oo[x, :])
        objf_post = 1 / 3 * (
                ENS_POST / o[x, 0] * oo[x, 0] + SAIDI_POST / o[x, 1] * oo[x, 1] + SAIFI_POST / o[x, 2] * oo[x, 2])

        values_posts = [(ENS_POST / o[x, 0]) * oo[x, 0], (SAIDI_POST / o[x, 1]) * oo[x, 1],
                        (SAIFI_POST / o[x, 2]) * oo[x, 2], objf_post]
        values_inits = [oo[x, 0], oo[x, 1], oo[x, 2], objf_pre]

        values_post = pd.DataFrame((values_posts), index=('ENS', 'SAIDI', 'SAIFI', 'F.OBIETTIVO'),
                                   columns=[tecnica_utilizzata])
        values_post_nonorm = pd.DataFrame((values_post_nonorms), index=('ENS', 'SAIDI', 'SAIFI', 'F.OBIETTIVO'),
                                          columns=[tecnica_utilizzata])
        values_post = values_post.T
        values_post_nonorm = values_post_nonorm.T

        for j in ['ENS', 'SAIDI', 'SAIFI']:
            ONR_GLOBALE['Tecniche'][tecnica_utilizzata][j]['indici_post'] = dict()
            ONR_GLOBALE['Tecniche'][tecnica_utilizzata][j]['indici_post']['norm'] = dict()
            ONR_GLOBALE['Tecniche'][tecnica_utilizzata][j]['indici_post']['abs'] = dict()

            ONR_GLOBALE['Tecniche'][tecnica_utilizzata][j]['indici_post']['norm'] = values_post.loc[tecnica_utilizzata][
                j]
            ONR_GLOBALE['Tecniche'][tecnica_utilizzata][j]['indici_post']['abs'] = \
                values_post_nonorm.loc[tecnica_utilizzata][j]

        ONR_GLOBALE['Tecniche'][tecnica_utilizzata]['F.OBIETTIVO']['indici_post'] = dict()
        ONR_GLOBALE['Tecniche'][tecnica_utilizzata]['F.OBIETTIVO']['indici_post']['norm'] = dict()
        ONR_GLOBALE['Tecniche'][tecnica_utilizzata]['F.OBIETTIVO']['indici_post']['abs'] = dict()
        values_post.loc[tecnica_utilizzata]['F.OBIETTIVO'] = objf_post
        values_post_nonorm.loc[tecnica_utilizzata]['F.OBIETTIVO'] = objf_post_nonorm
        ONR_GLOBALE['Tecniche'][tecnica_utilizzata]['F.OBIETTIVO']['indici_post']['norm'] = \
            values_post.loc[tecnica_utilizzata]['F.OBIETTIVO']
        ONR_GLOBALE['Tecniche'][tecnica_utilizzata]['F.OBIETTIVO']['indici_post']['abs'] = \
            values_post_nonorm.loc[tecnica_utilizzata]['F.OBIETTIVO']

        for i in lista_zone:
            ONR_ZONALE[i]['Reliability_par']['f_z']['post'] = lamb_POST[i]
            ONR_ZONALE[i]['Reliability_par']['U_z']['post'] = U_z_POST[i]
            ONR_ZONALE[i]['Reliability_par']['N_customers'] = ZoneReliability.loc[i]['Clienti']
            ONR_ZONALE[i]['Reliability_par']['PDz'] = PDz[i]
            ONR_ZONALE[i]['Reliability_par']['PGz'] = PGz[i]

        self.LFviolations_post(V0, xx, 'lf_post', busfrom, linee, trafi, switch)

        return ONR_GLOBALE, ONR_ZONALE

    def ONR_initialize(self):
        for i in v.keys():
            v[i]['ONR'] = dict()
            v[i]['ONR']['par'] = dict()
            v[i]['ONR']['lf_post'] = dict()
            v[i]['ONR']['lf_pre'] = dict()

            # voce parametri e load flow pre, post

            for p in ['lambda', 'mu', 'numcust', 'zone']:
                if 'Switch' in v[i]['category'] and ('_s' in i or '_m' in i):
                    if p == 'zone':
                        v[i]['ONR']['par'][p] = dict()
                        v[i]['ONR']['par'][p]['from'] = None
                        v[i]['ONR']['par'][p]['to'] = None
                    else:
                        v[i]['ONR']['par'][p] = None
                else:
                    v[i]['ONR']['par'][p] = None
            params = ['i', 'v', 'p', 'q']
            if 'Transformer' in v[i]['category'] or 'Line' in v[i]['category'] or 'Switch' in v[i]['category']:
                for p in params:
                    v[i]['ONR']['lf_pre'][p] = dict()
                    v[i]['ONR']['lf_pre'][p][0] = []
                    v[i]['ONR']['lf_pre'][p][1] = []

                    v[i]['ONR']['lf_post'][p] = dict()
                    v[i]['ONR']['lf_post'][p][0] = []
                    v[i]['ONR']['lf_post'][p][1] = []
            else:
                for p in params:
                    v[i]['ONR']['lf_pre'][p] = []

                    v[i]['ONR']['lf_post'][p] = []

            # voce per informazioni sullo switch
            if 's_' in i or '_m' in i:
                v[i]['ONR']['info_switch'] = dict()
                for p in ['stato_pre', 'stato_post', 'transition']:
                    v[i]['ONR']['info_switch'][p] = None

    def Stato_Switch(self, stati_switch_iniziali):
        for i in v.keys():
            if ('s_' in i or '_m' in i) and stati_switch_iniziali[i] == 0:
                v[i]['par']['out-of-service'] = True
                v[i]['ONR']['info_switch']['stato_pre'] = 'Aperto'
            if ('s_' in i or '_m' in i) and stati_switch_iniziali[i] == 1:
                v[i]['ONR']['info_switch']['stato_pre'] = 'Chiuso'


    def Rel_Bus(self, lambda_b, R_b, lambda_l, R_l, num_clienti_per_bus):
        for i in v.keys():
            if 'l_' in i:
                v[i]['ONR']['par']['lambda'] = lambda_l[i]
                v[i]['ONR']['par']['mu'] = R_l[i]
            if 'n_' in i and 'sourcebus' not in i:
                v[i]['ONR']['par']['lambda'] = lambda_b[i]
                v[i]['ONR']['par']['mu'] = R_b[i]
            if 'sourcebus' in i:
                v[i]['ONR']['par']['lambda'] = lambda_b[i]
                v[i]['ONR']['par']['mu'] = R_b[i]
            if 'load' in i:
                v[i]['ONR']['par']['numcust'] = float(num_clienti_per_bus[i])

    def ONR_par_del(self):
        for i in v.keys():
            if 'Load' in v[i]['category'] or 'switch' in v[i]['category']:
                del v[i]['ONR']['par']['lambda']
                del v[i]['ONR']['par']['mu']
            if 'Line' in v[i]['category'] or 'Node' in v[i]['category'] or 'switch' in v[i]['category']:
                del v[i]['ONR']['par']['numcust']

    def ONR_PAR(self, zone_bus, stati_switch_iniziali, lambda_b, R_b, lambda_l, R_l, num_clienti_per_bus):
        for i in (v.keys()):
            if 'AC-Line' or 'AC-Load' or 'ExternalGrid' in v[i]['category']:
                buss = v[i]['top']['conn'][0]
                if len(v[i]['top']['conn']) > 1:
                    buss2 = v[i]['top']['conn'][1]
            if 'AC-Node' in v[i]['category']:
                buss = i
                # print(buss)
            for z in zone_bus.keys():
                # print(z)
                for n in zone_bus[z]:
                    # print(z,n)
                    # print(i)
                    # if 'switch' in v[i]['category'] and buss2 == n and ('_s' in i or '_m' in i):
                    #     v[i]['ONR']['par']['zone']['to'] = z
                    # if buss == n and ('_s' in i or '_m' in i):
                    #     v[i]['ONR']['par']['zone']['from'] = z
                    if buss == n and ('AC-Line' or 'AC-Load' in v[i]['category']):
                        v[i]['ONR']['par']['zone'] = z
                    elif buss == n and 'AC-Node' in v[i]['category']:
                        v[i]['ONR']['par']['zone'] = z
                    elif buss == n and 'ExternaleGrid' in v[i]['category']:
                        v[i]['ONR']['par']['zone'] = z

        self.Stato_Switch(stati_switch_iniziali)
        self.Rel_Bus(lambda_b, R_b, lambda_l, R_l, num_clienti_per_bus)
        self.ONR_par_del()

    def LFviolations_pre(self, x, pre_post, busfrom, linee, trafi):

        # OpenDSS().full_parse_to_dss()
        # print('Grid power: P = %.1f\tQ = %.1f' % (
        # OpenDSS().dss.circuit.total_power[0], OpenDSS().dss.circuit.total_power[1]))

        for el in v:
            dictInitialize.lf_initialize(el)

        self.dss.full_parse_to_dss()
        self.dss.solve()
        self.dss.results_store_all()

        # print('Grid power: P = %.1f\tQ = %.1f' % (
        #       self.dss.dss.circuit.total_power[0], self.dss.dss.circuit.total_power[1]))

        self.results_store(pre_post)

        switch = x['switch']
        linee = x['linee']
        buses = x['bus']
        branches = x['branches']

        P_slack_pre = {}
        Q_slack_pre = {}

        P_gen = {}
        Q_gen = {}

        P_loads = {}
        Q_loads = {}

        Correnti_linee_modulo = {}
        Portata_linee = {}
        Sijmax = {}  # portata dei branches in KVA

        p1 = 0;
        p2 = 0;
        q1 = 0;
        q2 = 0
        for i in v.keys():
            if 'Line' in v[i]['category'] or 'Transformer' in v[i]['category'] or 'Switch' in v[i]['category']:
                p1 += v[i]['ONR']['lf_pre']['p'][0]
                p2 += -v[i]['ONR']['lf_pre']['p'][1]
                q1 += v[i]['ONR']['lf_pre']['q'][0]
                q2 += -v[i]['ONR']['lf_pre']['q'][1]

        P_loads2 = {}
        Q_loads2 = {}
        P_slack_pre2 = {}
        Q_slack_pre2 = {}
        Correnti_linee_modulo2 = {}
        Portata_linee2 = {}
        for m in v.keys():
            if 'ExternalGrid' in v[m]['category']:
                P_slack_pre2[m] = -v[m]['ONR']['lf_pre']['p']
                Q_slack_pre2[m] = -v[m]['ONR']['lf_pre']['q']
            if m.startswith('load'):
                P_loads2[m] = v[m]['ONR']['lf_pre']['p']
                Q_loads2[m] = v[m]['ONR']['lf_pre']['q']
            if 'Line' in v[m]['category']:
                Correnti_linee_modulo2[m] = v[m]['ONR']['lf_pre']['i'][0]
                Portata_linee2[m] = v[m]['par']['In']
            # if 'Switch' in v[m]['category']:
            #     Correnti_linee_modulo2[m] = v[m]['ONR']['lf_pre']['i'][0]



        if len(P_gen) == 0:
            print("Non ci sono generatori")
            P_gen = 0
            Q_gen = 0

        # print('');
        # print('Analisi delle potenze (ACLF) con la topologia iniziale:')
        # print('')
        # # print('Generazione:',round(sum(P_gen.values()),2), 'KW', ';', round(sum(Q_gen.values()),2),'Kvar')
        # print('Carico:', round(sum(P_loads2.values()), 2), 'KW', ';', round(sum(Q_loads2.values()), 2), 'Kvar')
        # print('Slack Bus active power:', round(sum(P_slack_pre2.values()), 2), 'KW')
        # print('Slack Bus reactive power:', round(sum(Q_slack_pre2.values()), 2), 'Kvar')
        # print('Active power losses:', round(p1 + p2, 2), 'KW')
        # print('Reactive power losses:', round(q1 + q2, 2), 'Kvar')
        # print('')

        self.log_pre_solver = (self.log_pre_solver + 'Analisi delle potenze (ACLF) con la topologia iniziale:\n\n' +
                               'Carico: ' + str(round(sum(P_loads2.values()), 2)) + ' KW ; ' +
                               str(round(sum(Q_loads2.values()), 2)) + ' Kvar\n' +
                               'Slack Bus active power: ' + str(round(sum(P_slack_pre2.values()), 2)) + ' KW\n' +
                               'Slack Bus reactive power: ' + str(round(sum(Q_slack_pre2.values()), 2)) + ' Kvar\n' +
                               'Active power losses: ' + str(round(p1 + p2, 2)) + ' KW\n' +
                               'Reactive power losses: ' + str(round(q1 + q2, 2)) + ' Kvar\n\n')

        # Controllo se ci sono linee in sovraccarico:

        sovraccarichi_iniziali = {}
        for b in linee:
            # print(Correnti_linee_modulo2[b])
            # print(Portata_linee2[b])
            if Correnti_linee_modulo2[b] > Portata_linee2[b]:
                # print(b, 'in sovraccarico:', round((Correnti_linee_modulo2[b] / Portata_linee2[b]) * 100, 0), '%')
                # sovraccarichi_iniziali[b] = round((Correnti_linee_modulo2[b] / Portata_linee2[b]) * 100, 0)

                self.log_pre_solver += (b + ' in sovraccarico: ' +
                                        str(round((Correnti_linee_modulo2[b] / Portata_linee2[b]) * 100, 0)) + '%\n')
        # print('')

        # Tensioni base
        Vnbus = {}  # kv
        for b in buses:
            if b == 'sourcebus':
                Vnbus[b] = 150
            else:
                Vnbus[b] = 20

        # Trovo le tensioni sui bus in modulo e fase e verifico se violano qualche limite

        tensioni_bus_modulo2 = {}
        for b in buses:
            tensioni_bus_modulo2[b] = v[b]['ONR']['lf_pre']['v'][0] / (sqrt(3) * 1000)

        # Modulo della tensione concatenata in p.u.:
        V0 = {}

        for a, b in tensioni_bus_modulo2.items():
            if a == 'sourcebus':
                V0[a] = b * sqrt(3) / 150
            else:
                V0[a] = b * sqrt(3) / 20

        Sijmax = {(b): 0 for b in branches}
        Sijpre = {(b): 0 for b in branches}

        for b in branches:
            if b in linee:
                # print(b, busfrom)
                # print([Portata_linee2])
                Sijmax[b] = round(Vnbus[busfrom[b]] * Portata_linee2[b.replace('Line.', '')], 2)
                Sijpre[b] = round(
                    sqrt(3) * tensioni_bus_modulo2[busfrom[b]] * Correnti_linee_modulo2[b.replace('Line.', '')], 2)
            else:
                Sijmax[b] = 25000

        Vmax = 1.1
        Vmin = 0.9

        violazioni_tensioni = {}
        for a, b in V0.items():
            if b <= Vmin or b >= Vmax:
                # print('Violazione di tensione sul nodo', a, '- Vi =', round(b, 4), 'p.u.')
                violazioni_tensioni[a] = b
                self.log_pre_viol += 'Violazione di tensione sul nodo ' + a + ' - Vi =' + str(round(b, 4)) + ' p.u.\n'

        if self.log_pre_viol == '':
            self.log_pre_viol = 'Nessuna violazione sui nodi'

        newV0 = []
        newbus = []
        for i in range(len(buses)):
            if buses[i] == 'sourcebus':
                newbus.append('slack')
                newV0.append(V0[buses[i]])
            else:
                newbus.append(buses[i])
                newV0.append(V0[buses[i]])

        # Modulo delle tensioni in pu
        plt.cla()

        nv_fig = plt.figure(figsize=(20, 6))
        # nv_fig = plt.figure(3, figsize=(30, 6))
        plt.axhline(1, color='black', linestyle='--', linewidth=1)
        plt.plot(buses, V0.values(), linewidth=1.5, marker='o', markersize=2.5, color='dodgerblue', label='Pre ONR')
        # plt.plot(buses, V1.values(), linewidth=1, marker='o',markersize=1, color='orange', label='ONR risultati')
        # plt.plot(buses, Vi.values(), linewidth=1, marker='o',markersize=1, color='forestgreen', label='Post ONR')
        plt.plot('sourcebus', V0['sourcebus'], marker='D', markersize=5, color='red', label='Slack Bus')
        plt.axhline(Vmax, color='red', linestyle='--', linewidth=1, label='$V_{max}$')
        plt.axhline(Vmin, color='blue', linestyle='--', linewidth=1, label='$V_{min}$')
        plt.ylim(0.85, 1.2)
        plt.xlim(0, (len(buses)))
        xtick_colors = ['red' if (val > Vmax or val < Vmin) else 'black' for val in newV0]
        # Impostazioni degli assi x e y
        plt.xticks(fontsize=12, rotation=90)

        # print('newV0: ', len(newV0))
        # print('V0: ', len(V0))
        # print('labels: ', len(plt.gca().get_xticklabels()))

        for i, label in enumerate(plt.gca().get_xticklabels()):
            # print(i, label)

            label.set_color(xtick_colors[i])
        plt.xlabel('Buses', fontsize=20)
        plt.ylabel(r'$V_{i} [pu]$', fontsize=20)
        plt.legend(loc='best', fontsize=12, frameon=False, ncol=2)
        plt.tight_layout()
        # plt.show()
        # plt.savefig(self.filedir + 'nodes_violations_pre.png')
        nv_fig.savefig(self.filedir + 'nodes_violations_pre.png')

        from matplotlib.lines import Line2D

        # Flussi di potenza apparente sui branches in sovraccarico:
        Sij_plot = {}
        for b in linee + trafi:
            if Sijpre[b] > Sijmax[b]:
                Sij_plot[b] = Sijpre[b]

        plt.cla()
        plt.figure(2, figsize=(15, 6))
        for b in Sij_plot.keys():
            plt.bar(b, Sijmax[b], linewidth=1, color='salmon')
            plt.stem(b, Sijpre[b], linefmt='darkred', markerfmt='v', basefmt=' ')
        plt.xticks(range(0, len(Sij_plot.keys())), [f'{br} ' for br in Sij_plot.keys()],
                   fontsize=20)  # Ruota le etichette di 45 gradi
        plt.xlabel('Overloaded branches', fontsize=20)
        plt.ylabel(r'$S_{ij} [kVA]$', fontsize=20)
        legend_elements = [Line2D([0], [0], color='salmon', linewidth=10, label=r'$S_{ij}^{max}$'),
                           Line2D([0], [0], color='darkred', marker='v', linestyle='None', label=r'$S_{ij}^{pre}$')]
        plt.legend(handles=legend_elements, fontsize=12)
        plt.tight_layout()
        # plt.show()
        plt.savefig(self.filedir + 'lines_overload.png')

        return V0

    def LFviolations_post(self, V0, x, pre_post, busfrom, linee, trafi, switch):
        # print('\n\n\n\n\n\n\n----- Calcolo POST -----------------')

        # OpenDSS().full_parse_to_dss()
        # OpenDSS().solve()

        for el in v:
            dictInitialize.lf_initialize(el)

        self.dss.full_parse_to_dss()
        self.dss.solve()
        self.dss.results_store_all()
        #
        # print('Grid power: P = %.1f\tQ = %.1f' % (
        #       OpenDSS().dss.circuit.total_power[0], OpenDSS().dss.circuit.total_power[1]))

        self.log_post_solver += ('Grid power: P = %.1f\tQ = %.1f\n\n' %
                                 (OpenDSS().dss.circuit.total_power[0], OpenDSS().dss.circuit.total_power[1]))

        self.results_store(pre_post)

        linee = x['linee']
        buses = x['bus']
        branches = x['branches']

        P_slack_pre = {}
        Q_slack_pre = {}

        P_gen = {}
        Q_gen = {}

        P_loads = {}
        Q_loads = {}

        Correnti_linee_modulo = {}
        Portata_linee = {}
        Sijmax = {}  # portata dei branches in KVA

        p1 = 0;
        p2 = 0;
        q1 = 0;
        q2 = 0
        for i in v.keys():
            if 'Line' in v[i]['category'] or 'Transformer' in v[i]['category'] or 'switch' in v[i]['category']:
                p1 += v[i]['ONR']['lf_post']['p'][0]
                p2 += -v[i]['ONR']['lf_post']['p'][1]
                q1 += v[i]['ONR']['lf_post']['q'][0]
                q2 += -v[i]['ONR']['lf_post']['q'][1]

        P_loads2 = {}
        Q_loads2 = {}
        P_slack_pre2 = {}
        Q_slack_pre2 = {}
        Correnti_linee_modulo2 = {}
        Portata_linee2 = {}
        for m in v.keys():
            if 'ExternalGrid' in v[m]['category']:
                P_slack_pre2[m] = -v[m]['ONR']['lf_post']['p']
                Q_slack_pre2[m] = -v[m]['ONR']['lf_post']['q']
            if m.startswith('load'):
                P_loads2[m] = v[m]['ONR']['lf_post']['p']
                Q_loads2[m] = v[m]['ONR']['lf_post']['q']
            if 'Line' in v[m]['category'] or 'switch' in v[m]['category']:
                Correnti_linee_modulo2[m] = v[m]['ONR']['lf_post']['i'][0]
                Portata_linee2[m] = v[m]['par']['In']

        if len(P_gen) == 0:
            # print("Non ci sono generatori")
            P_gen = 0
            Q_gen = 0

        # print('')
        # print('Analisi delle potenze (ACLF) con la topologia iniziale:')
        # print('')
        # # print('Generazione:',round(sum(P_gen.values()),2), 'KW', ';', round(sum(Q_gen.values()),2),'Kvar')
        # print('Carico:', round(sum(P_loads2.values()), 2), 'KW', ';', round(sum(Q_loads2.values()), 2), 'Kvar')
        # print('Slack Bus active power:', round(sum(P_slack_pre2.values()), 2), 'KW')
        # print('Slack Bus reactive power:', round(sum(Q_slack_pre2.values()), 2), 'Kvar')
        # print('Active power losses:', round(p1 + p2, 2), 'KW')
        # print('Reactive power losses:', round(q1 + q2, 2), 'Kvar')
        # print('')
        self.log_post_viol += 'Analisi delle potenze (ACLF) con la topologia iniziale:\n\n'
        self.log_post_viol += ('Carico: ' + str(round(sum(P_loads2.values()), 2)) + 'KW | ' +
                               str(round(sum(Q_loads2.values()), 2)) + 'Kvar\n\n')
        self.log_post_viol += 'Slack Bus active power: ' + str(round(sum(P_slack_pre2.values()), 2)) + 'KW\n'
        self.log_post_viol += 'Slack Bus reactive power: ' + str(round(sum(Q_slack_pre2.values()), 2)) + 'Kvar\n\n'
        self.log_post_viol += 'Active power losses: ' + str(round(p1 + p2, 2)) + 'KW\n'
        self.log_post_viol += 'Reactive power losses: ' + str(round(q1 + q2, 2)) + 'Kvar\n'
        self.log_post_viol += '\n\nAnalisi delle potenze (ACLF) con la topologia iniziale:\n\n'

        # Controllo se ci sono linee in sovraccarico:

        sovraccarichi_iniziali = {}
        for b in linee:
            if Correnti_linee_modulo2[b] > Portata_linee2[b]:
                # print(b, 'in sovraccarico:', round((Correnti_linee_modulo2[b] / Portata_linee2[b]) * 100, 0), '%\n')
                self.log_post_viol += (b + ' in sovraccarico: ' +
                                       str(round((Correnti_linee_modulo2[b] / Portata_linee2[b]) * 100, 0)) + '%\n')
                sovraccarichi_iniziali[b] = round((Correnti_linee_modulo2[b] / Portata_linee2[b]) * 100, 0)
        # print('')
        self.log_post_viol += '\n'

        # Tensioni base
        Vnbus = {}  # kv
        for b in buses:
            if b == 'sourcebus':
                Vnbus[b] = 150
            else:
                Vnbus[b] = 20

        # Trovo le tensioni sui bus in modulo e fase e verifico se violano qualche limite

        tensioni_bus_modulo_post2 = {}
        for b in buses:

            # print('pre', v[b]['ONR']['lf_post']['v'])
            # print('post', v[b]['ONR']['lf_post']['v'])
            # print(b, 'pre =', v[b]['ONR']['lf_pre']['v'], '\tpost =', v[b]['ONR']['lf_post']['v'],
            #       '\tchange =', v[b]['ONR']['lf_pre']['v'] != v[b]['ONR']['lf_post']['v'])

            tensioni_bus_modulo_post2[b] = v[b]['ONR']['lf_post']['v'][0] / (sqrt(3) * 1000)

        # Modulo della tensione concatenata in p.u.:
        V0_post = {}

        for a, b in tensioni_bus_modulo_post2.items():
            if a == 'sourcebus':
                V0_post[a] = b * sqrt(3) / 150
            else:
                V0_post[a] = b * sqrt(3) / 20

        # Ricavo la portata dei branches in KVA:
        Sijmax = {(b): 0 for b in branches}
        Sijpre = {(b): 0 for b in branches}

        for b in branches:
            if b in linee:
                Sijmax[b] = round(Vnbus[busfrom[b]] * Portata_linee2[b.replace('Line.', '')], 2)
                Sijpre[b] = round(
                    sqrt(3) * tensioni_bus_modulo_post2[busfrom[b]] * Correnti_linee_modulo2[b.replace('Line.', '')], 2)
            else:
                Sijmax[b] = 25000

        Vmax = 1.1
        Vmin = 0.9

        violazioni_tensioni = {}
        for a, b in V0_post.items():
            if b <= Vmin or b >= Vmax:
                # print('Violazione di tensione sul nodo', a, '- Vi =', round(b, 4), 'p.u.')
                violazioni_tensioni[a] = b
                self.log_post_viol += 'Violazione di tensione sul nodo ' + a + ' - Vi = ' + str(round(b, 4)) + ' p.u.\n'
        # print('')

        newV0_post = []
        newV0 = []
        newbus = []
        for i in range(len(buses)):
            if buses[i] == 'sourcebus':
                newbus.append('slack')
                newV0_post.append(V0_post[buses[i]])
                newV0.append(V0[buses[i]])
            else:
                newbus.append(buses[i])
                newV0_post.append(V0_post[buses[i]])
                newV0.append(V0[buses[i]])

        Vmin = 0.9
        Vmax = 1.1
        # Modulo delle tensioni in pu
        plt.cla()

        nv_fig = plt.figure(figsize=(20, 6))
        plt.axhline(1, color='black', linestyle='--', linewidth=1)
        plt.plot(newbus, V0.values(), linewidth=1.5, marker='o', markersize=2.5, color='dodgerblue', label='Pre ONR')
        plt.plot(newbus, V0_post.values(), linewidth=1.5, marker='o', markersize=2.5, color='orange', label='Post ONR')
        plt.plot('slack', V0['sourcebus'], marker='D', markersize=5, color='red', label='Slack Bus')
        plt.axhline(Vmax, color='red', linestyle='--', linewidth=1, label='$V_{max}$')
        plt.axhline(Vmin, color='blue', linestyle='--', linewidth=1, label='$V_{min}$')
        plt.ylim(0.85, 1.2)
        plt.xlim(0, (len(buses)))
        xtick_colors = ['red' if (val > Vmax or val < Vmin) else 'black' for val in newV0_post]
        # Impostazioni degli assi x e y
        plt.xticks(fontsize=12, rotation=90)
        # Modifica del colore delle etichette sull'asse x
        for i, label in enumerate(plt.gca().get_xticklabels()):
            # print(i, label)
            label.set_color(xtick_colors[i])
        plt.xlabel('Buses', fontsize=20)
        plt.ylabel(r'$V_{i} [pu]$', fontsize=20)
        plt.legend(loc='best', fontsize=12, frameon=False, ncol=2)
        plt.tight_layout()
        # plt.show()
        nv_fig.savefig(self.filedir + 'nodes_violations_post.png')

        from matplotlib.lines import Line2D
        # Flussi di potenza apparente sui branches in sovraccarico:
        Sij_plot = {}
        for b in linee + trafi:
            if Sijpre[b] > Sijmax[b]:
                Sij_plot[b] = Sijpre[b]
        print('\n\n')
        print(Sij_plot.keys())
        print('\n\n')

        plt.cla()
        # plt.close()
        # plt.show()
        lv_fig = plt.figure(10, figsize=(15, 6))
        for b in Sij_plot.keys():
            # plt.bar(b, 0, linewidth=1, color='salmon')
            plt.bar(b, Sijmax[b], linewidth=1, color='salmon')
            plt.stem(b, Sijpre[b], linefmt='darkred', markerfmt='v', basefmt=' ')
        plt.xticks(range(0, len(Sij_plot.keys())), [f'{br} ' for br in Sij_plot.keys()],
                   fontsize=20)  # Ruota le etichette di 45 gradi
        plt.xlabel('Overloaded branches________', fontsize=20)
        plt.ylabel(r'$S_{ij} [kVA]$', fontsize=20)
        legend_elements = [Line2D([0], [0], color='salmon', linewidth=10, label=r'$S_{ij}^{max}$'),
                           Line2D([0], [0], color='darkred', marker='v', linestyle='None', label=r'$S_{ij}^{post}$')]
        plt.legend(handles=legend_elements, fontsize=12)
        plt.tight_layout()
        # plt.show()
        lv_fig.savefig(self.filedir + 'lines_overload_post.png')

    def results_store(self, pre_post):

        for el in v.keys():
            if v[el]['category'] != 'AC-Node':
                # print(el)
                # per tutti gli elementi tranne che per i Nodi
                # print(el)
                if not v[el]['par']['out-of-service']:  # Se l'elemento è in servizio
                    mcat = mcat_find(el)

                    # Le parti DC sono in pratica porzioni AC, di cui si considera la fase globale.
                    # Per questo, per la corrente bisogna usare un fattore di correzione "cf"
                    cf0, cf1 = 1, 1  # fattore di correzione per le parti AC
                    if v[el]['category'] in ['DC-Line', 'DC-DC-Converter', 'DC-Load', 'BESS', 'PV', 'DC-Wind']:
                        cf0 = 3 ** 0.5  # fattore di correzione per le porzioni DC a monte
                    if v[el]['category'] in ['DC-Line', 'DC-DC-Converter', 'DC-Load', 'BESS', 'PV', 'DC-Wind', 'PWM']:
                        cf1 = 3 ** 0.5  # fattore di correzione per pe porzioni DC a valle

                    if v[el]['category'] not in mc['Line'] + mc['Transformer']:  # per gli elemnenti terminali

                        # le potenza globali sono date dalla somma delle potenze delle singole fasi
                        # Accodamento nel vettore dei risultati nel dizionario
                        # dei valori di P, Q, V, i con i relativi fattori di correzione
                        v[el]['ONR'][pre_post]['p'] = v[el]['lf']['p'][0]
                        v[el]['ONR'][pre_post]['q'] = v[el]['lf']['q'][0]
                        v[el]['ONR'][pre_post]['v'] = v[el]['lf']['v'][0]
                        v[el]['ONR'][pre_post]['i'] = v[el]['lf']['i'][0]

                    else:  # per le linee

                        # Inserimento nel dizionario, per ogni lato,
                        # dei valori di P, Q, V, i con i relativi fattori di correzione
                        v[el]['ONR'][pre_post]['p'][0] = v[el]['lf']['p'][0][0]
                        v[el]['ONR'][pre_post]['q'][0] = v[el]['lf']['q'][0][0]
                        v[el]['ONR'][pre_post]['p'][1] = v[el]['lf']['p'][1][0]
                        v[el]['ONR'][pre_post]['q'][1] = v[el]['lf']['q'][1][0]
                        v[el]['ONR'][pre_post]['v'][0] = v[el]['lf']['v'][0][0]
                        v[el]['ONR'][pre_post]['v'][1] = v[el]['lf']['v'][1][0]
                        v[el]['ONR'][pre_post]['i'][0] = v[el]['lf']['i'][0][0]
                        v[el]['ONR'][pre_post]['i'][1] = v[el]['lf']['i'][1][0]


                else:  # se l'elemento non è in servizio
                    if v[el]['category'] not in mc['Line'] + mc['Transformer']:  # per gli elemnenti terminali
                        v[el]['ONR'][pre_post]['p'] = v[el]['lf']['p'][0]
                        v[el]['ONR'][pre_post]['q'] = v[el]['lf']['q'][0]
                        v[el]['ONR'][pre_post]['v'] = v[el]['lf']['v'][0]
                        v[el]['ONR'][pre_post]['i'] = v[el]['lf']['i'][0]
                    else:  # per linee e trasformatori
                        v[el]['ONR'][pre_post]['p'][0] = v[el]['lf']['p'][0][0]
                        v[el]['ONR'][pre_post]['q'][0] = v[el]['lf']['q'][0][0]
                        v[el]['ONR'][pre_post]['p'][1] = v[el]['lf']['p'][1][0]
                        v[el]['ONR'][pre_post]['q'][1] = v[el]['lf']['q'][1][0]
                        v[el]['ONR'][pre_post]['v'][0] = v[el]['lf']['v'][0][0]
                        v[el]['ONR'][pre_post]['v'][1] = v[el]['lf']['v'][1][0]
                        v[el]['ONR'][pre_post]['i'][0] = v[el]['lf']['i'][0][0]
                        v[el]['ONR'][pre_post]['i'][1] = v[el]['lf']['i'][1][0]

            else:  # per i nodi e per il Source

                v[el]['ONR'][pre_post]['v'] = copy.deepcopy(v[el]['lf']['v'])

                # v[el]['ONR'][pre_post]['v'] = v[el]['lf']['v']

    def ONR_POST(self, transizionee):
        for i in v.keys():
            if 's_' in i or '_m' in i:
                v[i]['ONR']['info_switch']['transition'] = float(transizionee[i])

    def ONR_SF(self):
        for i in v.keys():
            if ('s_' in i or '_m' in i) and ('Line' in v[i]['category'] or 'Switch' in v[i]['category']):
                if (v[i]['ONR']['info_switch']['transition']) == -1:
                    v[i]['par']['out-of-service'] = False
                    v[i]['ONR']['info_switch']['stato_post'] = 'Chiuso'
                if (v[i]['ONR']['info_switch']['transition']) == 1:
                    v[i]['par']['out-of-service'] = True
                    v[i]['ONR']['info_switch']['stato_post'] = 'Aperto'
                if (v[i]['ONR']['info_switch']['transition']) == 0:
                    v[i]['ONR']['info_switch']['stato_post'] = v[i]['ONR']['info_switch']['stato_pre']


def mcat_find(el):
    mcat = ''
    for m in mc.keys():
        if v[el]['category'] in mc[m]:
            mcat = m
            break
    return mcat
