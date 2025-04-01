import math
from Functionalities.Adequacy.__plugins__.fiabilipy import Component, System
from sympy import Symbol
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from variables import v, grid

# dizionario di prova Antonio
#Leggo le informazioni ricavate all'istante t0
#Troverò il dizionario popolato con tutte le informazioni sui componenti
# v = yaml.safe_load(open(os.getcwd() + '/__shared__/CityArea_LFres_AnRes - 1year-Profile.yml'))
# try:
#     del v['_grid_']
# except:
#     pass
#
# filename = os.path.join(os.getcwd() + '/__shared__/CityArea_LFres_AnRes - 1year-Profile.yml')

class Affidabilità:
    def __init__(self):
        #
        # self.Ta = Ta
        # self.T0 = T0

        # estraiamo tutti i componenti di rete presenti nel dizionario
        self.buss_AC = [componente for componente in v.keys() if v[componente]['category'] != 'ExternalGrid' if v[componente]['category'] == 'AC-Node']
        self.buss_DC = [componente for componente in v.keys() if v[componente]['category'] != 'ExternalGrid' if v[componente]['category'] == 'DC-Node']
        self.trasformatori = [componente for componente in v.keys() if v[componente]['category'] == '2W-Transformer' and v[componente]['par']['out-of-service'] == False]
        self.convertitori_dc = [componente for componente in v.keys() if v[componente]['category'] == 'DC-DC-Converter' and v[componente]['par']['out-of-service'] == False]
        self.pwm = [componente for componente in v.keys() if v[componente]['category'] == 'Inverter' and v[componente]['par']['out-of-service'] == False]
        self.carichi_ac = [componente for componente in v.keys() if v[componente]['category'] == 'AC-Load' and v[componente]['par']['out-of-service'] == False]
        self.carichi_dc = [componente for componente in v.keys() if v[componente]['category'] == 'DC-Load' and v[componente]['par']['out-of-service'] == False]
        self.link_dc = [componente for componente in v.keys() if v[componente]['category'] == 'DC-Line' and v[componente]['par']['out-of-service'] == False]
        self.link_ac = [componente for componente in v.keys() if v[componente]['category'] == 'AC-Line' and v[componente]['par']['out-of-service'] == False]
        self.PV_AC = [componente for componente in v.keys() if v[componente]['category'] == 'AC-PV' and v[componente]['par']['out-of-service'] == False]
        self.PV_DC = [componente for componente in v.keys() if v[componente]['category'] == 'DC-PV' and v[componente]['par']['out-of-service'] == False]
        self.BESS = [componente for componente in v.keys() if v[componente]['category'] == 'AC-BESS' and v[componente]['par']['out-of-service'] == False]
        self.BESS_DC = [componente for componente in v.keys() if v[componente]['category'] == 'DC-BESS' and v[componente]['par']['out-of-service'] == False]
        self.WIND_AC = [componente for componente in v.keys() if v[componente]['category'] == 'AC-Wind' and v[componente]['par']['out-of-service'] == False]
        self.WIND_DC = [componente for componente in v.keys() if v[componente]['category'] == 'DC-Wind' and v[componente]['par']['out-of-service'] == False]
        self.ext_grid = [componente for componente in v.keys() if v[componente]['category'] == 'ExternalGrid']
        self.generazione = self.PV_AC + self.PV_DC  + self.WIND_AC + self.WIND_DC ##al momento non considero  i BESS perchè l'output non mi convince
        self.domanda = self.carichi_ac + self.carichi_dc
        self.buss = self.buss_AC + self.buss_DC
        #verifico l'orizzonte temporale delle curve di previsione e carico leggendo l'output
        #di un componente qualsiasi
        self.horizon_time = len(v[self.generazione[0]]['lf']['p'])
        self.timestep_MC = 1000
        self.LOLE_MC = np.zeros(self.timestep_MC)

    # def write_dict(self, element, alfa, beta, Pi_E, Pi_Q):
    #     #funzione creata solo per ovviare agli input utente mancanti
    #     v[element]['rel']['par']['alfa'] = alfa
    #     v[element]['rel']['par']['beta'] = beta
    #     v[element]['rel']['par']['Pi_E'] =Pi_E
    #     v[element]['rel']['par']['Pi_Q'] = Pi_Q
    #     v[element]['rel']['results']['lambda'] = 0.000004
    #     v[element]['rel']['results']['MTBF_anni'] = 40
    #
    #
    def cicli_termici(self, Ta):
        start = 0
        stop = 1
        start_cre = 0
        stop_cre = 1
        start_decr = 0
        stop_decr = 1
        cicli_cre = {}
        cicli_decre = {}
        ΔTcycling_cre = []
        ΔTcycling_decre = []
        Tmax_cre = []
        Tmax_decr = []
        i = 1
        j = 1
        trend = [b - a for a, b in zip(Ta[start:stop], Ta[start + 1::1])]
        while stop_decr < len(Ta)  and stop_cre < len(Ta):
            if trend[-1] >= 0 or trend[-1] >= -0.05:
                while trend[-1] >= -0.05 and stop_cre <len(Ta)  and stop_decr < len(Ta):
                    if stop_decr > start_decr + 1 and stop_cre < stop_decr:
                        start_cre = stop_decr - 1
                        stop_cre = start_cre + 1

                    trend = [b - a for a, b in zip(Ta[start_cre:stop_cre], Ta[start_cre + 1::1])]
                    stop_cre = stop_cre + 1
                cicli_cre[i] = (start_cre, stop_cre - 2, stop_cre - start_cre - 1,max(Ta[start_cre:stop_cre - 1]) -
                                min(Ta[start_cre:stop_cre - 1]),max(Ta[start_cre:stop_cre - 1]))
                i = i + 1
            if trend[-1] <= 0 or trend[-1] <= 0.05:
                while trend[-1] <= 0.05 and stop_decr < len(Ta) and stop_cre < len(Ta):
                    if stop_cre > start_cre + 1 and stop_decr < stop_cre:
                        start_decr = stop_cre - 1
                        stop_decr = start_decr + 1
                    trend = [b - a for a, b in zip(Ta[start_decr:stop_decr], Ta[start_decr + 1::1])]
                    stop_decr = stop_decr + 1
                cicli_decre[j] = (start_decr, stop_decr - 2, stop_decr - start_decr - 1,
                                  max(Ta[start_decr:stop_decr - 1]) - min(Ta[start_decr:stop_decr - 1]),
                                  max(Ta[start_decr:stop_decr - 1]))
                j = j + 1

        cicli_cre_tmp = dict(cicli_cre)
        cicli_decre_tmp = dict(cicli_decre)
        for key, value in cicli_cre_tmp.items():
            if value[3] < 2:  ## non considero i cicli con delta inferiore a 2
                del cicli_cre[key]

        for key, value in cicli_decre_tmp.items():
            if value[3] < 2:  ## non considero i cicli con delta inferiore a 2
                del cicli_decre[key]

        for key, value in cicli_cre.items():
            ΔTcycling_cre.append(value[3])
        ΔTcycling_cre_max = max(ΔTcycling_cre)

        for key, value in cicli_cre.items():
            Tmax_cre.append(value[3])
        Tmax1 = max(Tmax_cre)

        for key, value in cicli_decre.items():
            ΔTcycling_decre.append(value[4])
        ΔTcycling_decre_max = max(ΔTcycling_decre)

        for key, value in cicli_decre.items():
            Tmax_decr.append(value[4])
        Tmax2 = max(Tmax_decr)

        Tmax = max(Tmax1, Tmax2)
        ΔTcycling_max = max(ΔTcycling_cre_max, ΔTcycling_decre_max)
        num_cicli = len(cicli_cre)+len(cicli_decre)     # numero cicli in un giorno

        return num_cicli



    #t = ore per il calcolo dell'affidabilità'
    def Norris_Landzberg(self, element, t, T0, Ta):
        ####CALCOLO AFFIDABILITA' DEL COMPONENTE E SCRIVO IL RISULTATO NEL DIZIONARIO ELEMENTS CAMPO RESULTS
        ##For PF>2019
        #calcolo formula Norris-Landzberg:


        ###
        tannual=24*365 #[ore]
        #####SARA' UTILIZZATO PER TUTTI I COMPONENTI
        print('lunghezza Ta', len(Ta))
        num_cicli = self.cicli_termici(Ta)
        print('numero di cicli:', num_cicli)
        Nannualcy=num_cicli * 8760 / len(Ta)
        print('N. Cicli/Anno', Nannualcy)

        ##NOTA BENE: NON VALUTIAMO L'AFFIDABILITA' DEL CARICO IN QUANTO VALUTIAMO L'AFFIDABILITA' DELLA FORNITURA.
        ##STESSA COSA PER LE BUSBAR

        if v[element]['category'] == 'AC-Load' or v[element]['category'] == 'DC-Load' or v[element]['category'] == 'AC-Node' or v[element]['category'] == 'DC-Node':
            v[element]['rel']['results']['lambda'] = 0

        if v[element]['category'] == 'AC-Line' or v[element]['category'] == 'DC-Line':
            # Calcolo affidabilità  linee elettriche  aeree_AG

            # Lunghezza linee  #in alternativa valore suggerito in rosso solo per rete benchmark
            #lungh_linea1 = 10  # []
            lungh_linea1 = v[element]['par']['length']

            ##La sezione del cavo, se non presente, deve essere settata nel modello di rete e riportata nel dizionario
            # A = Sezione cavi  # in alternativa valore suggerito in rosso solo per rete benchmark
            #A = v.elements[element]['parameters']['sez']
            A=0.000012
            # temperatura massima funzionamento cavo
            TMAX0_linea = 90 ##valore preso da catalogo prysmian

            #t va letto nel dizionario ed inserito dall'utente
            # input: parametri da aggiungere al sottodizionario "parameter" del dizionario "linee"
            #resistività rame-> ipotesi di tutti i cavi in rame
            rho_20 = 1.68 * math.pow(10, -8)

            # calore specifico del materiale [J/Kg°C] del rame
            C = 385
            # densita del materilae cavo Kg/m3c del rame
            density = 8900
            Karm_linee = 1  # ipotizzo lo stesso valore per tutte le linee, in prima approssimazione pari a 1
            Kis_linee = 1  # ipotizzo lo stesso valore per tutte le linee, in prima approssimazione pari a 1

            Airr = 0.5 * A  # l'area irradiata dalla radiazione solare sia pari alla metà della sezione del cavo
            Epsilon_isolinea = 0.91  # emissività del PVC: essa diminuisce all'aumentare della temperatura
            Sigma_isolinea = pow(10, -10)  # conducibilità elettrica di un polimero
            Deltai = 0
            # Per ogni linea della rete elettrica considerata:
            # Per ogni timestep:
            # inizio ciclo su timestep
            Top_linea_vector = []


            i = 0
            ##nota: il vettore Ta deve avere lo stesso orizzonte temporale dei vettori di generazione e carico
            for h in range(0, int(len(Ta)/1)): #sto ipotizzando un timestep di 15 minuti quindi in un'ora ho 4 valori @AR Corretto 1 ora
                for m in range(0, 60, grid['profile']['step']):
                    rho = rho_20 * ((234.5 + Ta[i]) / (234.5 + 20))     # resistenza di ogni linea

                    # calcolo a partire da ro lunghezza e sezione cavi e resisitività (temeperatura)
                    R_linea = rho * lungh_linea1 / A
                    Deltaz = TMAX0_linea - Ta[i]  # ver z-Tamb
                    ##leggo il valore della corrente Ic nel dizionario
                    Ic = v[element]['lf']['i'][0][i] # [A]
                    ##leggo il valore della corrente nominale Iz nel dizionario
                    Iz = v[element]['par']['In']

                    # costante di tempo termica
                    T = C * density * Deltaz * pow((A / Iz), 2) / rho

                    Deltac = Deltaz * Karm_linee * Kis_linee * pow((Ic / Iz), 2)
                    Deltaf = Deltac - (Deltac - Deltai) * math.exp(-t / T)
                    Top_linea = Ta[i] + Deltaf # temperatura operativa linea
                    Deltai = Deltaf
                    Top_linea_vector.append(Top_linea)
                    if i<len(Ta):
                        i = i + 1


            Top_MAX_linea = max(Top_linea_vector)
            Top_min_linea = min(Top_linea_vector)
            Delta_Tcycling = Top_MAX_linea - Top_min_linea
            tannual = 24*365  # [ore]

            m = 1  # in prima approssimazione m=1

            alfa, beta, pi_e, pi_q = v[element]['rel']['par']['alfa'], v[element]['rel']['par']['beta'], v[element]['rel']['par']['Pi_E'], v[element]['rel']['par']['Pi_Q']

            # calcolo formula Norris-Landzberg:
            # Ho inserito To pari a 30° (Prysmian)
            lambda_wear_out = (v[element]['rel']['par']['beta'] / v[element]['rel']['par']['alfa']) * pow((t / v[element]['rel']['par']['alfa']), (v[element]['rel']['par']['beta'] - 1))  ### Weibull [guasti/ore]
            # lambda_prot_linea da inserire nel dizionario delle "linee" e di tutti gli altri elementi delle rete
            lambda_prot_linea = 1 # protezione assente; se protezione presente inserire il valore corretto
            m_line=1 # numero linee
            #stress termico dovuto alle condizioni operative di funzionamento (corrente che circola)
            print('Delta Cycling:', Delta_Tcycling)
            print('Top_Max_linea:', Top_MAX_linea)
            print()
            Pi_Si_linea = (12 * Nannualcy / tannual) * pow((Delta_Tcycling / T0),m_line) * \
                          (math.exp(1414 * ((1 / (323)) - (1 / (Top_MAX_linea + 273.15)))))
            Pi_Se_linea = 0 # stress termico dovuto all'irraggiamento
            Lambda = lambda_prot_linea * lambda_wear_out * (Pi_Si_linea + Pi_Se_linea + v[element]['rel']['par']['Pi_E'] + v[element]['rel']['par']['Pi_Q'])  # [guasti/ore]
            MTBF_ore = (1 / Lambda)  # [ore]
            MTBF_anni = MTBF_ore / 8760  # [anni]
            R_comp = math.exp(-(Lambda / v[element]['rel']['par']['beta']) * t)
            v[element]['rel']['results']['lambda'] = Lambda
            v[element]['rel']['results']['MTBF_ore'] = MTBF_ore
            v[element]['rel']['results']['MTBF_anni'] = MTBF_anni
            v[element]['rel']['results']['R'] = R_comp
            v[element]['rel']['results']['Pi_Si'] = Pi_Si_linea





        if v[element]['category'] == 'PWM' or v[element]['category'] == 'AC-Wind':
            Top_MAX_Conv = 60  # ipotizzata in base a valore massimo da datasheet di inverter trifase
            Top_min_Conv = min(Ta)

            ΔTcycling_max = Top_MAX_Conv - Top_min_Conv

            lambda_wear_out = (v[element]['rel']['par']['beta'] / v[element]['rel']['par']['alfa']) * pow((t / v[element]['rel']['par']['alfa']), (v[element]['rel']['par']['beta'] - 1))  ### Weibull [guasti/ore]
            #####DAB PER I CARICHI DC, PV, BATERIA, eolico DC calcolo formula  Norris - Landzberg:
            lambda0_sw = 0.01  # [guasti/10^6 ORE] tasso di guasto base per iGBT in FIDES 2009 PAG 241

            m = 1
            Pi_S_sw_ON = (12 * Nannualcy / tannual) * pow(ΔTcycling_max / T0, m) * \
                         (math.exp(1414 * ((1 / 333) - (1 / (Top_MAX_Conv + 273.15)))))
            Pi_S_sw_OFF = 0
            lambdaON = lambda_wear_out * (Pi_S_sw_ON + v[element]['rel']['par']['Pi_E'] + v[element]['rel']['par']['Pi_Q'])  # [guasti/ORE] # commentato in data 17-11-2022
            lambdaOFF = lambda_wear_out * (Pi_S_sw_OFF + v[element]['rel']['par']['Pi_E'] + v[element]['rel']['par']['Pi_Q'])  # [guasti/ORE] # commentato in data 17-11-2022
            Lambda = 2 * lambdaON + 2 * lambdaOFF  # [guasti/ore] il 2 dipende nal numero di interruttori presenti nel converter
            MTBF_ore = (1 / Lambda)  # [ore]
            MTBF_anni = MTBF_ore / 8760  # [anni]
            R_comp = math.exp(-(Lambda / v[element]['rel']['par']['beta']) * t)
            v[element]['rel']['results']['lambda'] = Lambda
            v[element]['rel']['results']['MTBF_ore'] = MTBF_ore
            v[element]['rel']['results']['MTBF_anni'] = MTBF_anni
            v[element]['rel']['results']['R'] = R_comp
            v[element]['rel']['results']['Pi_Si'] = Pi_S_sw_ON

        if v[element]['category'] == 'AC-PV' or v[element]['category'] == 'DC-PV' or v[element]['category'] == 'DC-DC-Converter' or v[element]['category'] == 'AC-BESS' or v[element]['category'] == 'DC-BESS' or v[element]['category'] == 'DC-Wind':

            Top_MAX_Conv = 60 #ipotizzata in base a valore massimo da datasheet di inverter trifase
            Top_min_Conv = min(Ta)

            ΔTcycling_max = Top_MAX_Conv - Top_min_Conv


            lambda_wear_out = (v[element]['rel']['par']['beta'] / v[element]['rel']['par']['alfa']) * pow((t / v[element]['rel']['par']['alfa']), (v[element]['rel']['par']['beta'] - 1))  ### Weibull [guasti/ore]
            #####DAB PER I CARICHI DC, PV, BATERIA, eolico DC calcolo formula  Norris - Landzberg:
            lambda0_sw = 0.01  # [guasti/10^6 ORE] tasso di guasto base per iGBT in FIDES 2009 PAG 241

            m = 1
            Pi_S_sw_ON = (12 * Nannualcy / tannual) * pow(ΔTcycling_max / T0, m) * \
                         (math.exp(1414 * ((1 / 333) - (1 / (Top_MAX_Conv + 273.15)))))
            Pi_S_sw_OFF = 0
            lambdaON = lambda_wear_out * (Pi_S_sw_ON + v[element]['rel']['par']['Pi_E'] + v[element]['rel']['par']['Pi_Q'])  # [guasti/ORE] # commentato in data 17-11-2022
            lambdaOFF = lambda_wear_out * (Pi_S_sw_OFF + v[element]['rel']['par']['Pi_E'] + v[element]['rel']['par']['Pi_Q'])  # [guasti/ORE] # commentato in data 17-11-2022
            Lambda = 2 * lambdaON + 2 * lambdaOFF  # [guasti/ore] il 2 dipende nal numero di filari/interruttori presenti nel converter
            MTBF_ore = (1 / Lambda)  # [ore]
            MTBF_anni = MTBF_ore / 8760  # [anni]
            R_comp = math.exp(-(Lambda / v[element]['rel']['par']['beta']) * t)
            v[element]['rel']['results']['lambda'] = Lambda
            v[element]['rel']['results']['MTBF_ore'] = MTBF_ore
            v[element]['rel']['results']['MTBF_anni'] = MTBF_anni
            v[element]['rel']['results']['R'] = R_comp
            v[element]['rel']['results']['Pi_Si'] = Pi_S_sw_ON

        if v[element]['category'] == '2W-Transformer':
            ##TRASFORMATORE
            Tmax_tr=110 #°C dalla normativa dei trasformatori vedere LA1.1 par. 4.1
            Tmin_tr=30 #°C dalla normativa dei trasformatori vedere LA1.1 par. 4.1
            ΔTcycling_max = Tmax_tr - Tmin_tr
            lambda_wear_out = (v[element]['rel']['par']['beta'] / v[element]['rel']['par']['alfa']) * pow((t / v[element]['rel']['par']['alfa']), (v[element]['rel']['par']['beta'] - 1))  ### Weibull [guasti/ore]
            m_tr=1
            Pi_S_sw_ON=(12*Nannualcy/tannual) * pow(ΔTcycling_max/T0,m_tr) * \
                       (math.exp(1414*((1/(323)) - (1/(Tmax_tr+273.15)))))

            lambdaON = lambda_wear_out*(Pi_S_sw_ON + v[element]['rel']['par']['Pi_E'] + v[element]['rel']['par']['Pi_Q'])  #[guasti/ore]
            Lambda= lambdaON # lambdaOFF #[guasti/ore]
            MTBF_ore= (1/Lambda) #[ore]
            MTBF_anni= MTBF_ore/8760 #[ anni]
            R_comp = math.exp(-(Lambda / v[element]['rel']['par']['beta']) * t)
            v[element]['rel']['results']['lambda'] = Lambda
            v[element]['rel']['results']['MTBF_ore'] = MTBF_ore
            v[element]['rel']['results']['MTBF_anni'] = MTBF_anni
            v[element]['rel']['results']['R'] = R_comp
            v[element]['rel']['results']['Pi_Si'] = Pi_S_sw_ON



    def raggruppa(self):
        gruppi = {}
        gruppo = []
        for carico in self.domanda:
            if v[carico]['top']['conn'][0] not in gruppi.keys():
                gruppi.setdefault(v[carico]['top']['conn'][0])
        for bus in gruppi.keys():
            for carico in self.domanda:
                if v[carico]['top']['conn'][0] == bus:
                    gruppo.append(carico)
            gruppi[bus] = gruppo
            gruppo = []
        return gruppi

    def RBD(self, time, gruppi):
        self.graph = nx.Graph()
        #creo il grafo della rete
        [self.graph.add_edge(componente, nodo) for componente in v.keys() if componente != 'ExternalGrid' for nodo in v[componente]['top']['conn']]
        self.id_obj = {}  # contiene gli id dei componenti
        self.extend_list = []
        self.last_node = []
        self.first_node = []
        self.Rel = []
        #possibile generatori attivi sia di giorno che di notte
        self.generatori_diurni = self.BESS + self.BESS_DC +self.PV_AC + self.PV_DC + self.WIND_AC + self.WIND_DC
        #possibili generatori attivi solo di notte
        self.generatori_notturni = self.BESS + self.BESS_DC + self.WIND_AC + self.WIND_DC


        self.carichi = self.carichi_dc + self.carichi_ac
        t = Symbol('t', positive=True)  # t in ore
        timerange = range(0, 1000, 1)

        for bus in gruppi.keys():
            self.first_node = []
            self.S = ''
            reliability = 0
            F = 1 # inaffidabilità
            R = 0 # affidabilità
            if gruppi[bus][0] in self.graph.nodes() :
                #print('inizio ' + carico + '...')
                self.S = System()
                self.path = []
                self.path_tmp = []
                self.blocchi = []
                #CALCOLO AFFIDABLITA' ORE DIURNE
                for generatore in self.generatori_diurni:
                    if generatore in self.graph.nodes() : #aggiungere verifica di fuori servizio quando Antonio aggiornera il DB
                        if len(gruppi[bus])==1:
                            self.path.append(nx.shortest_path(self.graph, generatore, gruppi[bus][0]))
                        else:
                            for i in range(0,len(gruppi[bus])):
                                self.path.append(nx.shortest_path(self.graph, generatore, gruppi[bus][i]))

                        self.blocchi = self.path.copy()  # blocchi del RDB

                        for i in range(0, len(self.path)):
                            self.blocchi[i] = [Component(self.path[i][j],
                                                         v[self.path[i][j]]['rel']['results']['lambda'],
                                                         v[self.path[i][j]]['rel']['par']['beta'])
                                               for j in range(0, len(self.path[i]))]

                        # creo dizionario con gli id dei componenti
                        for componente in self.blocchi:
                            for k in range(0, len(componente)):
                                self.id_obj[id(componente[k])] = componente[k]
                        for i in range(0, len(self.blocchi)):
                            if i == 0:
                                self.S['E'] = self.blocchi[i][0]
                                self.first_node.append(self.blocchi[i][0].name)
                            if i > 0 and self.blocchi[i][0].name not in self.first_node:
                                self.S['E'] = self.blocchi[i][0]
                                self.first_node.append(self.blocchi[i][0].name)
                                # self.S['E'] = self.blocchi[i][0]
                            num_nodi = len(self.blocchi[i]) - 1
                            chek1 = 'false'
                            chek2 = 'false'
                            for j in range(0, num_nodi):
                                for componente in self.S.components:
                                    if self.blocchi[i][j + 1].name == componente.name and id(self.blocchi[i][j + 1]) != id(
                                            componente):
                                        comp_succ = componente
                                        chek1 = 'true'

                                    if self.blocchi[i][j].name == componente.name and id(self.blocchi[i][j]) != id(componente):
                                        if i > 0 and j == 0:
                                            self.S['E'] = componente
                                        comp_prec = componente
                                        chek2 = 'true'

                                if chek1 == 'false' and chek2 == 'false':
                                    self.S[self.blocchi[i][j]] = self.blocchi[i][j + 1]
                                if chek1 == 'true' and chek2 == 'false':
                                    self.S[self.blocchi[i][j]] = comp_succ
                                    chek1 = 'false'
                                if chek1 == 'false' and chek2 == 'true':
                                    self.S[comp_prec] = self.blocchi[i][j + 1]
                                    chek2 = 'false'
                                if chek1 == 'true' and chek2 == 'true':
                                    if comp_prec != comp_succ:
                                        self.S[comp_prec] = comp_succ
                                    chek1 = 'false'
                                    chek2 = 'false'
                            if i == 0:
                                self.S[self.blocchi[0][len(self.blocchi[0]) - 2]] = 'S'
                                self.last_node.append(self.blocchi[0][len(self.blocchi[0]) - 2].name)
                            if i > 0 and self.blocchi[i][len(self.blocchi[i]) - 2].name not in self.last_node:
                                self.S[self.blocchi[i][len(self.blocchi[i]) - 2]] = 'S'
                                self.last_node.append(self.blocchi[i][len(self.blocchi[i]) - 2].name)

                        if len(self.generatori_diurni) > 1:
                            F = F * (1 - self.S.reliability(time))
                        else:
                            R = self.S.reliability(time)

                    # plt.figure(figsize=(15, 10))
                    # plt.tick_params(labelsize=3)
                    # plt.rc('font', size=1)
                    #
                    # self.S.draw()
                    # filename1 = os.path.join(os.getcwd(), 'reliability', 'Affidabilità fornitura','diurna', generatore + '.png')
                    # if os.path.isfile(os.getcwd() + '/reliability/Affidabilità fornitura/diurna/' + generatore + '.png'):
                    #     os.remove(os.getcwd() + '/reliability/Affidabilità fornitura/diurna/' + generatore + '.png')  # Opt.: os.system("rm "+strFile)
                    # plt.savefig(filename1)
                    # plt.close()
                if len(self.generatori_diurni) > 1:
                    reliability = 1 - F
                else:
                    reliability = R
                #scrivere nel dizionario il valore dell'affidabilità della fornitura
                if len(gruppi[bus])==1:
                    v[gruppi[bus][0]]['rel']['results']['load_rel'] = float(reliability)
                else:
                    for i in range(0,len(gruppi[bus])):
                        v[gruppi[bus][i]]['rel']['results']['load_rel'] = float(reliability)


                #CALCOLO AFFIDABLITA' ORE NOTTURNE
                self.first_node = []
                self.S = ''
                reliability = 0
                self.S = System()
                self.path = []
                self.path_tmp = []
                self.blocchi = []
                F = 1  # inaffidabilità
                R = 0  # affidabilità
                for generatore in self.generatori_notturni:
                    if generatore in self.graph.nodes() : #aggiungere verifica di fuori servizio quando Antonio aggiornera il DB
                        if len(gruppi[bus])==1:
                            self.path.append(nx.shortest_path(self.graph, generatore, gruppi[bus][0]))
                        else:
                            for i in range(0,len(gruppi[bus])):
                                self.path.append(nx.shortest_path(self.graph, generatore, gruppi[bus][i]))

                        self.blocchi = self.path.copy()  # blocchi del RDB

                        for i in range(0, len(self.path)):
                            self.blocchi[i] = [Component(self.path[i][j],
                                                         v[self.path[i][j]]['rel']['results']['lambda'],
                                                         v[self.path[i][j]]['rel']['par']['beta'])
                                               for j in range(0, len(self.path[i]))]

                        # creo dizionario con gli id dei componenti
                        for componente in self.blocchi:
                            for k in range(0, len(componente)):
                                self.id_obj[id(componente[k])] = componente[k]
                        for i in range(0, len(self.blocchi)):
                            if i == 0:
                                self.S['E'] = self.blocchi[i][0]
                                self.first_node.append(self.blocchi[i][0].name)
                            if i > 0 and self.blocchi[i][0].name not in self.first_node:
                                self.S['E'] = self.blocchi[i][0]
                                self.first_node.append(self.blocchi[i][0].name)
                                # self.S['E'] = self.blocchi[i][0]
                            num_nodi = len(self.blocchi[i]) - 1
                            chek1 = 'false'
                            chek2 = 'false'
                            for j in range(0, num_nodi):
                                for componente in self.S.components:
                                    if self.blocchi[i][j + 1].name == componente.name and id(self.blocchi[i][j + 1]) != id(
                                            componente):
                                        comp_succ = componente
                                        chek1 = 'true'

                                    if self.blocchi[i][j].name == componente.name and id(self.blocchi[i][j]) != id(componente):
                                        if i > 0 and j == 0:
                                            self.S['E'] = componente
                                        comp_prec = componente
                                        chek2 = 'true'

                                if chek1 == 'false' and chek2 == 'false':
                                    self.S[self.blocchi[i][j]] = self.blocchi[i][j + 1]
                                if chek1 == 'true' and chek2 == 'false':
                                    self.S[self.blocchi[i][j]] = comp_succ
                                    chek1 = 'false'
                                if chek1 == 'false' and chek2 == 'true':
                                    self.S[comp_prec] = self.blocchi[i][j + 1]
                                    chek2 = 'false'
                                if chek1 == 'true' and chek2 == 'true':
                                    if comp_prec != comp_succ:
                                        self.S[comp_prec] = comp_succ
                                    chek1 = 'false'
                                    chek2 = 'false'
                            if i == 0:
                                self.S[self.blocchi[0][len(self.blocchi[0]) - 2]] = 'S'
                                self.last_node.append(self.blocchi[0][len(self.blocchi[0]) - 2].name)
                            if i > 0 and self.blocchi[i][len(self.blocchi[i]) - 2].name not in self.last_node:
                                self.S[self.blocchi[i][len(self.blocchi[i]) - 2]] = 'S'
                                self.last_node.append(self.blocchi[i][len(self.blocchi[i]) - 2].name)

                        if len(self.generatori_notturni) > 1:
                            F = F * (1 - self.S.reliability(time))
                        else:
                            R = self.S.reliability(time)

                    # plt.figure(figsize=(15, 10))
                    # plt.tick_params(labelsize=3)
                    # plt.rc('font', size=1)
                    #
                    # self.S.draw()
                    # filename1 = os.path.join(os.getcwd(), 'reliability', 'Affidabilità fornitura', 'notturna', generatore + '.png')
                    # if os.path.isfile(os.getcwd() + '/reliability/Affidabilità fornitura/notturna/' + generatore + '.png'):
                    #     os.remove(os.getcwd() + '/reliability/Affidabilità fornitura/notturna/' + generatore + '.png')  # Opt.: os.system("rm "+strFile)
                    # plt.savefig(filename1)
                    # plt.close()
                if len(self.generatori_notturni) > 1:
                    reliability = 1 - F
                else:
                    reliability = R
                #scrivere nel dizionario il valore dell'affidabilità della fornitura
                if len(gruppi[bus])==1:
                    #sostituire load_rel con load_rel1
                    v[gruppi[bus][0]]['rel']['results']['load_rel1'] = float(reliability)
                else:
                    for i in range(0,len(gruppi[bus])):
                        # sostituire load_rel con load_rel1
                        v[gruppi[bus][i]]['rel']['results']['load_rel1'] = float(reliability)

#
#
# a = Affidabilità()
#
# t = 1000
# T0=25
# Ta = [20,24,26,21,18,15,25,28,31]
# for element in v.keys():
#     if element != '_grid_' :
#         a.Norris_Landzberg(element,t, T0, Ta)
# #salvo il dizionario aggiornato
# print('salvo2')
# with open(filename, 'w') as file:
#     yaml.dump(v, file)
#     file.close()
#
# gruppi = a.raggruppa()
# a.RBD(t, gruppi)
# #salvo il dizionario aggiornato
# print('salvo3')
# with open(filename, 'w') as file:
#     yaml.dump(v, file)
# file.close()
#
# #
#
#







