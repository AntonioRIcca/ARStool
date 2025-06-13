import os

import math
from math import modf
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import random as rand
import numpy as np

from variables import v, grid, mainpath


class Adeguatezza:
    def __init__(self):
        self.graphs = dict()

        self.MC_years = 10  # anni monte carlo ovvero numero di stati casuali del sistema da generare
        self.statesampling = 4000   # stati del sistema per ogni anno monte carlo
        # estraiamo tutti i componenti di rete presenti nel dizionario
        self.buss = [componente for componente in v.keys() if v[componente]['category'] != 'ExternalGrid' if v[componente]['category'] == 'AC-Node']
        self.trasformatori = [componente for componente in v.keys() if v[componente]['category'] == '2W-Transformer' and v[componente]['par']['out-of-service'] == False]
        self.convertitori_dc = [componente for componente in v.keys() if v[componente]['category'] == 'DC-DC-Converter' and v[componente]['par']['out-of-service'] == False]
        self.pwm = [componente for componente in v.keys() if v[componente]['category'] == 'Inverter' and v[componente]['par']['out-of-service'] == False]
        self.carichi_ac = [componente for componente in v.keys() if v[componente]['category'] == 'AC-Load' and v[componente]['par']['out-of-service'] == False]
        self.carichi_dc = [componente for componente in v.keys() if v[componente]['category'] == 'DC-Load' and v[componente]['par']['out-of-service'] == False]
        self.link_dc = [componente for componente in v.keys() if v[componente]['category'] == 'DC-Line' and v[componente]['par']['out-of-service'] == False]
        self.link_ac = [componente for componente in v.keys() if v[componente]['category'] == 'AC-Line' and v[componente]['par']['out-of-service'] == False]
        self.PV_AC = [componente for componente in v.keys() if v[componente]['category'] == 'AC-PV' and v[componente]['par']['out-of-service'] == False]
        self.PV_DC = [componente for componente in v.keys() if v[componente]['category'] == 'DC-PV' and v[componente]['par']['out-of-service'] == False]
        self.BESS_AC = [componente for componente in v.keys() if v[componente]['category'] == 'AC-BESS' and v[componente]['par']['out-of-service'] == False]
        self.BESS_DC = [componente for componente in v.keys() if v[componente]['category'] == 'DC-BESS' and v[componente]['par']['out-of-service'] == False]
        self.WIND_AC = [componente for componente in v.keys() if v[componente]['category'] == 'AC-Wind' and v[componente]['par']['out-of-service'] == False]
        self.WIND_DC = [componente for componente in v.keys() if v[componente]['category'] == 'DC-Wind'and v[componente]['par']['out-of-service'] == False]
        self.ext_grid = [componente for componente in v.keys() if v[componente]['category'] == 'ExternalGrid']
        self.generazione_distribuita_senza_BESS = self.PV_DC +self.PV_AC + self.WIND_AC + self.WIND_DC
        self.domanda = self.carichi_ac + self.carichi_dc
        self.BESS = self.BESS_AC + self.BESS_DC
        self.generazione_distribuita_con_BESS = self.generazione_distribuita_senza_BESS + self.BESS
        self.PV = self.PV_AC + self.PV_DC
        # verifico l'orizzonte temporale delle curve di previsione e carico leggendo l'output
        # di un componente qualsiasi
        self.horizon_time = len(v[self.generazione_distribuita_senza_BESS[0]]['lf']['p'])

    def somma(self,v1, v2):
        n = len(v1)
        w = []
        for i in range(n):
            w.append(v1[i] + v2[i])
        return w

    def prodotto(self,v1, v2):
        n = len(v1)
        w = []
        for i in range(n):
            w.append(v1[i] * v2[i])
        return w

    def differenza(self,v1, v2):
        n = len(v1)
        w = []
        for i in range(n):
            w.append(v1[i] - v2[i])
        return w

    def generation_adequacy(self):
        generazione_distribuita_senza_BESS = np.zeros(self.horizon_time)
        generazione_da_external_grid = np.zeros(self.horizon_time)
        domanda_load = np.zeros(self.horizon_time)
        Pbess_generazione_totale = np.zeros(self.horizon_time)
        Pbess_domanda_totale = np.zeros(self.horizon_time)
        DNS = np.zeros(self.horizon_time)
        DNS_somma = 0
        LOLP = 0
        EDNS = 0
        LOLE = 0

        for bess in self.BESS:
            Pbess = np.array(v[bess]['lf']['p'])
            Pbess1 = Pbess.copy()
            Pbess2 = Pbess.copy()
            index0 = np.where(Pbess > 0)  # nei timestep dove la batteria assorbe (Pbess>0) pongo il valore uguale a zer
            # perchè devo considerare solo la potenza immessa in rete
            index1 = np.where(Pbess < 0)  # nei timestep dove la batteria eroga (Pbess<0) pongo il valore uguale a zer
            # perchè devo considerare solo la potenza erogata in rete
            for i in range(0, len(index0[0])):
                Pbess1[index0[0][i]] = 0  # Pbess1 contiene valori negativi ovvero la batteria eroga
            for i in range(0, len(index1[0])):
                Pbess2[index1[0][i]] = 0 # Pbess2 contiene valori positivi ovvero la batteria assorbe
            Pbess_generazione_totale = self.somma(np.abs(Pbess1), Pbess_generazione_totale)
            Pbess_domanda_totale = self.somma(np.abs(Pbess2), Pbess_domanda_totale)
        for generatore in self.generazione_distribuita_senza_BESS:
            generazione_distribuita_senza_BESS = (self.somma(np.abs(v[generatore]['lf']['p']),generazione_distribuita_senza_BESS))
        for domanda in self.domanda:
            domanda_load = self.somma(np.abs(v[domanda]['lf']['p']), domanda_load)

        generazione_totale_distribuita = self.somma(Pbess_generazione_totale, generazione_distribuita_senza_BESS)
        domanda_totale = self.somma(Pbess_domanda_totale, domanda_load)

        external_grid = v['source']['lf']['p'].copy()

        print(external_grid)

        for i in range(len(external_grid)):
            external_grid[i] = -external_grid[i] # Se la potenza arriva dalla rete esterna deve essere positiva. Nel dizionario il segno è invertito.
            if external_grid[i] > 0:
                generazione_da_external_grid[i] = external_grid[i]
        # per generazione interna totale intendo la somma di tutta la potenza prodotta ed iniettata nella microgrid. Quindi considera sia la potenza generata dalla
        # generazione distribuita che la potenza proveninente dalla rete esterna
        generazione_interna_totale = self.somma(generazione_da_external_grid, generazione_totale_distribuita)
        # per generazione totale intendo il bilancio della potenza entrante ed uscente dalla microrete
        bilancio_potenza = self.somma(external_grid, generazione_totale_distribuita)
        for i in range(0, len(generazione_interna_totale)):
            if generazione_interna_totale[i] < domanda_totale[i]:
                DNS[i] = 1
                DNS_somma = domanda_totale[i] - generazione_interna_totale[i] + DNS_somma

        LOLP = sum(DNS) * 100 / self.horizon_time  # Loss of Load Probability (probabilità di avere un load shedding involontario)
        EDNS = DNS_somma / self.horizon_time  # [valore in potenza]Expected Demand Not Supplied
        LOLE = (LOLP / 100) * self.horizon_time  # [ore/anno] Loss of load expectation
        # è la durata totale degli incrementi in cui è prevista la perdita di carico

        return generazione_totale_distribuita, domanda_totale, DNS_somma, LOLP, EDNS, LOLE, DNS, generazione_interna_totale,  external_grid, bilancio_potenza

    def State_Sampling(self, generazione_totale_distribuita, domanda_totale):
        durata_timestep = 1     # durata timestep in ore
        timehorizon = len(generazione_totale_distribuita) # orizzonte temporale in ore
        numerotimestep = int(timehorizon/durata_timestep)
        SAIDI = 2.5     # ORE DI INTERRUZIONE MEDIE ANNUE PREVISTE DA ENEL NEL 2025
        LOLE = np.zeros(self.statesampling)
        LOLE_medio = np.zeros(self.statesampling)
        EENS = np.zeros(self.statesampling)
        EENS_medio = np.zeros(self.statesampling)
        LOLE_anomalies = np.zeros(self.statesampling)
        LOLE_medio_anomalies = np.zeros(self.statesampling)
        EENS_anomalies = np.zeros(self.statesampling)
        EENS_medio_anomalies = np.zeros(self.statesampling)
        LOLE_medio_anno_MC = np.zeros(self.MC_years)
        EENS_medio_anno_MC = np.zeros(self.MC_years)
        LOLE_medio_anomalies_anno_MC = np.zeros(self.MC_years)
        EENS_medio_anomalies_anno_MC = np.zeros(self.MC_years)
        generazione_totale_distribuita_copy = generazione_totale_distribuita.copy()
        for i in range(0,self.MC_years):
            timestep_estratti = []
            for j in range(0,self.statesampling):
                CV_LOLE = 0  # coefficiente di variazione
                CV_LOLE_anomalies = 0  # coefficiente di variazione
                CV_EENS = 0  # coefficiente di variazione
                LOLE_carico = 0
                EENS_carico = 0
                LOLE_carico_anomalies = 0
                EENS_carico_anomalies = 0
                LOLE_carico_degrado = 0
                EENS_carico_degrado = 0
                timestep = rand.randrange(0, numerotimestep-1)  # estraggo il time step nell'orizzonte temporale che sto analizzando
                # #quando disponibili previsioni estrarre anno fornito da Gianluca
                # Valuto LOLE ed ENS considerando la sola affidabilità della fornitura
                for carico in self.domanda :
                    u = rand.uniform(0, 1)
                    ttr = (-1/SAIDI) * math.log(u) # tempo di ripristino in ore
                    fraz, intero = modf(ttr / durata_timestep)
                    if v[self.PV[0]]['lf']['p'][timestep] > 0 : # siamo in ore diurne
                        load_rel = v[carico]['rel']['results']['load_rel']
                    else:
                        # quando sarà inserito puntare a load_rel1
                        load_rel = v[carico]['rel']['results']['load_rel1']
                    if u > load_rel: # il carico non è alimentato
                        #calcolo le ore di mancata fornitura al carico

                        # TODO Da ripristinare
                        # try:
                        if timestep+round(intero) < numerotimestep:
                            LOLE_carico = LOLE_carico + ttr
                        else:
                            LOLE_carico = LOLE_carico + numerotimestep-timestep
                        # calcolo l'energia non fornita al carico
                        if ttr <= durata_timestep:
                            EENS_carico = EENS_carico + v[carico]['lf']['p'][timestep]*ttr
                        else:
                            if timestep + round(intero)< numerotimestep:
                                for t in range(0,round(intero)):
                                    EENS_carico = EENS_carico + v[carico]['lf']['p'][timestep+t] * durata_timestep
                                EENS_carico = EENS_carico + v[carico]['lf']['p'][timestep + round(intero)] * fraz
                            else:
                                for t in range(0, numerotimestep - 1):
                                    print('numerotimestep', numerotimestep)
                                    t_obs = min(timestep + t, numerotimestep - 1)
                                    # EENS_carico = EENS_carico + v[carico]['lf']['p'][timestep + t] * durata_timestep
                                    EENS_carico = EENS_carico + v[carico]['lf']['p'][t_obs] * durata_timestep
                        # except:
                        #     print('Carico', carico)
                        #     print("v[carico]['lf']['p']", v[carico]['lf']['p'])
                        #     print("len(v[carico]['lf']['p'])", len(v[carico]['lf']['p']))
                        #     print('timestep', timestep)
                        #     print('t', t)

                ##Valuto LOLE ed ENS considerando sia l'affidabilità della fornitura che le anomalie presenti
                LOLE_carico_anomalies = LOLE_carico
                EENS_carico_anomalies = EENS_carico

                for generatore in self.generazione_distribuita_con_BESS:
                    # print(generatore)
                    a_dict = v[generatore]['anom']['res']['a_dict']
                    a_vct = v[generatore]['anom']['res']['a_vct']
                    xi = v[generatore]['anom']['res']['xi']
                    betai = v[generatore]['anom']['res']['beta']
                    if (v[generatore]['anom']['par'].get('Hourly_Degradation') and a_vct[timestep] == 'normal' and timestep not in timestep_estratti) or (a_vct[timestep] != 'normal' and timestep not in timestep_estratti):
                        timestep_estratti.append(timestep)
                        # leggo le informazioni sull'evento anomalo transitorio tipo partial shading
                        # non sto considerando il degrado dei generatori PV che è un'anomalia permanente già contenuta
                        # nel segnale di partenza
                        generazione_totale_distribuita_copy[timestep] = generazione_totale_distribuita[timestep]-abs(v[generatore]['lf']['p'][timestep])+(abs(v[generatore]['lf']['p'][timestep])*xi[timestep] + betai[timestep] )
                        if generazione_totale_distribuita_copy[timestep] < domanda_totale[timestep] and a_vct[timestep] == 'normal' : # dobbiamo considerare il naturale degrado
                            EENS_carico_degrado = abs(v[generatore]['lf']['p'][timestep])-(abs(v[generatore]['lf']['p'][timestep])*xi[timestep] + betai[timestep]) + EENS_carico_degrado
                            LOLE_carico_degrado = LOLE_carico_degrado + 1 # il degrado dura tutto il timestep cha vale 1 ora

                        if generazione_totale_distribuita_copy[timestep] < domanda_totale[timestep] and a_vct[timestep] != 'normal': # a causa delle anomalie la generazione distribuita totale non è piu adeguata
                            for evento in range(0,len(a_dict.keys())):
                                print('len(a_vct):', len(a_vct))
                                print('timestamp:', timestep, '\tevento:', evento, 'event' + str(evento+1))
                                print('a_dict[a_vct[timestep]]:', len(a_dict[a_vct[timestep]]))
                                if timestep in a_dict[a_vct[timestep]][evento]['event' + str(evento+1)]['idx']:
                                    orig_start = a_dict[a_vct[timestep]][evento]['event' + str(evento + 1)]['orig_start']
                                    orig_end = a_dict[a_vct[timestep]][evento]['event' + str(evento + 1)]['orig_end']
                                    if timestep == math.floor(orig_start): # il timestep coincide con il punto di partenza dell'evento
                                        # EENS_carico_anomalies = EENS_carico_anomalies + abs(v[generatore]['lf']['p'][timestep]*v[generatore]['anomaly']['anomalies']['degradation']-v[generatore]['anomaly']['p'][timestep]) * (orig_start-min(orig_end, math.ceil(orig_start))) * durata_timestep
                                        # il segnale contiene già il degrado dovuto all'usura quindi non serve piu il campo degradation
                                        EENS_carico_anomalies = EENS_carico_anomalies + abs(v[generatore]['lf']['p'][timestep] - (abs(v[generatore]['lf']['p'][timestep])*xi[timestep] + betai[timestep])) * (orig_start - min(orig_end, math.ceil(orig_start))) * durata_timestep
                                        LOLE_carico_anomalies = LOLE_carico_anomalies + (orig_start-min(orig_end, math.ceil(orig_start))) * durata_timestep
                                    if timestep > orig_start and timestep < math.floor(orig_end):
                                        # EENS_carico_anomalies = EENS_carico_anomalies + abs(v[generatore]['lf']['p'][timestep]*v[generatore]['anomaly']['anomalies']['degradation'] - v[generatore]['anomaly']['p'][timestep]) * durata_timestep
                                        # il segnale contiene già il degrado dovuto all'usura quindi non serve piu il campo degradation
                                        EENS_carico_anomalies = EENS_carico_anomalies + abs(v[generatore]['lf']['p'][timestep]  - abs(v[generatore]['lf']['p'][timestep])*xi[timestep] + betai[timestep]) * durata_timestep
                                        LOLE_carico_anomalies = LOLE_carico_anomalies + durata_timestep
                                    if timestep == math.floor(orig_end):
                                        # EENS_carico_anomalies = EENS_carico_anomalies + abs(v[generatore]['lf']['p'][timestep]*v[generatore]['anomaly']['anomalies']['degradation'] - v[generatore]['anomaly']['p'][timestep]) * (orig_end-timestep) * durata_timestep
                                        # il segnale contiene già il degrado dovuto all'usura quindi non serve piu il campo degradation
                                        EENS_carico_anomalies = EENS_carico_anomalies + abs(v[generatore]['lf']['p'][timestep] - (v[generatore]['lf']['p'][timestep])*xi[timestep] + betai[timestep]) * (orig_end-timestep) * durata_timestep
                                        LOLE_carico_anomalies = LOLE_carico_anomalies + (orig_end-timestep) * durata_timestep

                LOLE_degrado_anomalie = LOLE_carico_degrado + LOLE_carico_anomalies
                EENS_degrado_anomalie = EENS_carico_degrado + EENS_carico_anomalies

                LOLE[j] = LOLE_carico
                EENS[j] = EENS_carico
                LOLE_anomalies[j] = LOLE_degrado_anomalie
                EENS_anomalies[j] = EENS_degrado_anomalie

            LOLE_medio_anno_MC[i] =  sum(LOLE)/self.statesampling
            EENS_medio_anno_MC[i] = sum(EENS)/self.statesampling
            LOLE_medio_anomalies_anno_MC[i] = sum(LOLE_anomalies)/self.statesampling
            EENS_medio_anomalies_anno_MC[i] = sum(EENS_anomalies)/self.statesampling
        # calcolo il coefficiente di variazione (CV) che rappresenta
        # la distanza della deviazione standard rispetto al valore medio

        CV_LOLE = 0
        CV_LOLE_anomalies = 0

        generazione_totale_distribuita_copy.clear()
        return LOLE_medio_anno_MC, CV_LOLE, EENS_medio_anno_MC, LOLE_medio_anomalies_anno_MC, CV_LOLE_anomalies, EENS_medio_anomalies_anno_MC

    def generation_adequacy_plot(self, adequacy_result, i0=0, i1=23):
        (generazione_totale_distribuita, domanda_totale, DNS_somma, LOLP, EDNS, LOLE, DNS, generazione_interna_totale,
         external_grid, bilancio_potenza) = adequacy_result

        # ##PLOTTO LO STUDIO SULLA GENERATION ADEQUACY
        sample = np.zeros(len(generazione_interna_totale))
        for i in range(0, len(generazione_interna_totale[0:23])):
            sample[i] = i
        figure, axis = plt.subplots(2, 1)
        axis[0].plot(sample[i0:i1],generazione_totale_distribuita[i0:i1], color="yellow", label ="GENERAZIONE DISTRIBUITA")
        axis[0].plot(sample[i0:i1],generazione_interna_totale[i0:i1], color="red", label ="GENERAZIONE INTERNA TOTALE")
        axis[0].plot(sample[i0:i1],domanda_totale[i0:i1], color="blue", label ="DOMANDA")
        axis[0].plot(sample[i0:i1],external_grid[i0:i1], color="black", label ="GENERAZIONE ESTERNA")
        axis[0].plot(sample[i0:i1],bilancio_potenza[i0:i1], color="green", label ="BILANCIO DI POTENZA")
        axis[0].set_title("ADEQUACY")
        axis[0].legend(frameon=False, loc='upper left', fontsize=5)
        axis[0].set_xlabel('Tempo [h]', fontsize=5)
        axis[0].set_ylabel('Potenza [kW]', fontsize=5)

        axis[0].text(15, 250, "% Gen.distr./Gen. interna tot.:" + str(round(sum(generazione_totale_distribuita)*100/sum(generazione_interna_totale),2)) +"%", style='italic')
        plt.xlabel('ADEQUACY')

        axis[1].plot(sample[i0:i1],DNS[i0:i1], color="red", label ="DNS")
        axis[1].set_title("DNS")
        axis[1].legend()

        strFile = "generation_adequacy.png"

        savepath = mainpath + '/_temp/Functionalities/Adequacy/__images__/'

        if os.path.isfile(savepath + strFile):
            os.remove(savepath + strFile)   # Opt.: os.system("rm "+strFile)
        filename1 = os.path.join(savepath, strFile)
        plt.savefig(filename1)
        plt.close()

        figure1, ax1 = plt.subplots()

        self.graphs[0] = {
            'title': '',
            'x-axis': 'Tempo [h]',
            'y-axis': 'Potenza [kW]',
            'ratio': 1.5,
            'x': sample[i0:i1],
            'y': {
                0: generazione_totale_distribuita[i0:i1],
                1: generazione_interna_totale[i0:i1],
                2: domanda_totale[i0:i1],
                3: external_grid[i0:i1],
                4: bilancio_potenza[i0:i1],
            },
            'colors': {
                0: 'yellow',
                1: 'red',
                2: '#00ffdd',
                3: 'white',
                4: 'green',
            },
            'labels': {
                0: 'GENERAZIONE DISTRIBUITA',
                1: 'GENERAZIONE INTERNA TOTALE',
                2: 'DOMANDA',
                3: 'GENERAZIONE ESTERNA',
                4: 'BILANCIO DI POTENZA',
            },
        }

        ax1.plot(sample[i0:i1], generazione_totale_distribuita[i0:i1], color="yellow",
                     label="GENERAZIONE DISTRIBUITA")
        ax1.plot(sample[i0:i1], generazione_interna_totale[i0:i1], color="red", label="GENERAZIONE INTERNA TOTALE")
        ax1.plot(sample[i0:i1], domanda_totale[i0:i1], color="blue", label="DOMANDA")
        ax1.plot(sample[i0:i1], external_grid[i0:i1], color="black", label="GENERAZIONE ESTERNA")
        ax1.plot(sample[i0:i1], bilancio_potenza[i0:i1], color="green", label="BILANCIO DI POTENZA")
        ax1.set_title("ADEQUACY")
        ax1.legend(frameon=False, loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=2,
                   fontsize=8)
        ax1.set_xlabel('Tempo [h]', fontsize=10)
        ax1.set_ylabel('Potenza [kW]', fontsize=10)

        box = ax1.get_position()
        ax1.set_position([box.x0, box.y0 + box.height * 0.15, box.width, box.height * 0.85])
        box1 = ax1.get_position()

        grid['adeq']['x_gen_est'] = sum(generazione_totale_distribuita) * 100 / sum(generazione_interna_totale)

        strFile = "1.png"
        if os.path.isfile(savepath + strFile):
            os.remove(savepath + strFile)   # Opt.: os.system("rm "+strFile)

        #  -------

        figure2, ax2 = plt.subplots()

        self.graphs[1] = {
            'title': '',
            'x-axis': 'Tempo [h]',
            'y-axis': 'DNS [kW]',
            'ratio': 1.5,
            'x': sample[i0:i1],
            'y': {
                0: DNS[i0:i1],
            },
            'colors': {
                0: 'red',
            },
            'labels': {
                0: 'DNS',
            },
        }

        ax2.plot(sample[i0:i1],DNS[i0:i1], color="red", label="DNS")
        ax2.set_title("DNS")
        ax2.legend(fontsize=8)
        ax2.set_xlabel('Tempo [h]', fontsize=10)
        ax2.set_ylabel('Potenza [kW]', fontsize=10)

        strFile = "2.png"
        if os.path.isfile(savepath + strFile):
            os.remove(savepath + strFile)   # Opt.: os.system("rm "+strFile)

    def state_sampling_plot(self, generazione_totale_distribuita, domanda_totale):

        (LOLE_medio_anno_MC, CV_LOLE, EENS_medio_anno_MC, LOLE_medio_anomalies_anno_MC, CV_LOLE_anomalies,
         EENS_medio_anomalies_anno_MC) = self.State_Sampling(generazione_totale_distribuita, domanda_totale)

        print(LOLE_medio_anno_MC)
        print(LOLE_medio_anomalies_anno_MC)

        ##PLOTTO LO STUDIO DELL'ADEQUACY CONSIDERANDO L'AFFIDABILITà DELLA FORNITURA E LE ANOMALIE

        sample = np.zeros(self.MC_years)
        for i in range(0, len(sample)):
            sample[i] = i
        figure1, axis1 = plt1.subplots(1, 2)
        figure1.suptitle('ADEGUATEZZA')

        self.graphs[2] = {
            'title': 'Adeguatezza',
            'x-axis': 'Anni Monte Carlo',
            'y-axis': 'LOLE [ore/anno]',
            'ratio': 0.8,
            'x': sample,
            'y': {
                0: LOLE_medio_anno_MC,
                1: LOLE_medio_anomalies_anno_MC,
            },
            'colors': {
                0: 'green',
                1: 'red',
            },
            'labels': {
                0: "con Affidabilità dei componenti",
                1: "con Affidabilità e Anomalie",
            },
        }

        axis1[0].plot(sample,LOLE_medio_anno_MC, color="blue")
        axis1[0].plot(sample,LOLE_medio_anomalies_anno_MC, color="red")

        # Shrink current axis's height by 10% on the bottom
        box = axis1[0].get_position()
        axis1[0].set_position([box.x0, box.y0 + box.height * 0.1, box.width*0.9, box.height * 0.9])

        print('x0', plt.axis()[2])

        axis1[0].text(2.5, 0.000625, "% LOLE con affidabilità fornitura:" + str(LOLE_medio_anno_MC[-1]), style='italic')
        axis1[0].text(2000, 0.4, "% LOLE con affidabilità fornitura e anomalie:" + str(LOLE_medio_anomalies_anno_MC[-1]), style='italic')
        axis1[0].yaxis.set_label_position("right")
        axis1.flat[0].set(xlabel='ANNI MONTE CARLO', ylabel='LOLE[ore/anno]')



        axis1[1].plot(sample,EENS_medio_anno_MC, color="blue")
        axis1[1].plot(sample,EENS_medio_anomalies_anno_MC, color="red")
        axis1[1].yaxis.set_label_position("right")
        axis1.flat[1].set(xlabel='ANNI MONTE CARLO', ylabel='EENS[KWh]')

        # Shrink current axis's height by 10% on the bottom
        box = axis1[1].get_position()
        axis1[1].set_position([box.x0*1.1, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

        # Put a legend below current axis
        figure1.legend(labels=["CONSIDERANDO L'AFFIDABILITA' DEI COMPONENTI","CONSIDERANDO L'AFFIDABILITA' E ANOMALIE DEI COMPONENTI"], loc="lower center", ncol=2)

        strFile = "LOLE&EENS.png"

        savepath = mainpath + '/_temp/Functionalities/Adequacy/__images__/'

        if os.path.isfile(savepath + strFile):
            os.remove(savepath + strFile)   # Opt.: os.system("rm "+strFile)

        filename1 = os.path.join(savepath, strFile)
        plt1.savefig(filename1, dpi=1200)
        plt1.close()



        # -- New -- @AR
        figure1 = plt.Figure(figsize=(4, 5))
        ax1 = figure1.add_subplot()

        ax1.plot(sample, LOLE_medio_anno_MC, color="blue", label='con Affidabilità dei componenti')
        ax1.plot(sample, LOLE_medio_anomalies_anno_MC, color="red", label='con Affidabilità e Anomalie')

        box = ax1.get_position()
        ax1.set_position([box.x0 + box.width * 0.05, box.y0 + box.height * 0.05, box.width, box.height * 1])

        ax1.set_xlabel('Anni Monte Carlo [y]', fontsize=10)
        ax1.set_ylabel('Lole [h/y]', fontsize=10)
        ax1.legend(frameon=False, loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=1,
                   fontsize=8)

        grid['adeq']['av_lole_funr_rel'] = LOLE_medio_anno_MC[-1]
        grid['adeq']['av_lole_anom'] = LOLE_medio_anomalies_anno_MC[-1]
        grid['adeq']['av_eens_furn_rel'] = EENS_medio_anno_MC[-1]
        grid['adeq']['av_eens_anom'] = EENS_medio_anomalies_anno_MC[-1]

        strFile = "3.png"
        if os.path.isfile(savepath + strFile):
            os.remove(savepath + strFile)   # Opt.: os.system("rm "+strFile)
        #  ------------

        figure2 = plt.Figure(figsize=(4, 5))
        ax2 = figure2.add_subplot()

        self.graphs[3] = {
            'title': '',
            'x-axis': 'Anni Monte Carlo [y]',
            'y-axis': 'EENS [kWh]',
            'ratio': 0.8,
            'x': sample,
            'y': {
                0: EENS_medio_anno_MC,
                1: EENS_medio_anomalies_anno_MC,
            },
            'colors': {
                0: 'green',
                1: 'red',
            },
            'labels': {
                0: "con Affidabilità dei componenti",
                1: "con Affidabilità e Anomalie",
            },
        }

        ax2.plot(sample, EENS_medio_anno_MC, color="blue", label='con Affidabilità dei componenti')
        ax2.plot(sample, EENS_medio_anomalies_anno_MC, color="red", label='con Affidabilità e Anomalie')

        box = ax1.get_position()
        ax2.set_position([box.x0 + box.width * 0.05, box.y0 + box.height * 0.05, box.width, box.height * 1])

        ax2.set_xlabel('Anni Monte Carlo [y]', fontsize=10)
        ax2.set_ylabel('EENS [kWh]', fontsize=10)
        ax2.legend(frameon=False, loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=1,
                   fontsize=8)

        strFile = "4.png"
        if os.path.isfile(savepath + strFile):
            os.remove(savepath + strFile)
