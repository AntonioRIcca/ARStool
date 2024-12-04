import copy

import py_dss_interface

import dictInitialize
from variables import *
import yaml
import os
import pandas as pd
import polars as pl
import numpy as np
import csv
from decimal import Decimal, InvalidOperation

from dictInitialize import *


class OpenDSS:
    def __init__(self):
        self.dss = py_dss_interface.DSS()   # sostituisce self.dss = None

        self.unr_nodes = []

        # TODO: non più necessari
        self.unr_conv = []                  # lista dei convertitori non risolti tramite self.node_define
        self.unr_lines = []                 # lista delle linee non risolte tramite self.node_define

        mainpath = 'papap'

    # Procedura di connessione con il file di OpenDSS
    def open(self, filename):
        self.dss = py_dss_interface.DSS(r"C:\Program Files\OpenDSS")
        # TODO: da sostituire con la variabile di configurazione del percorso di OpenDSS
        self.dss.text(f"compile [{filename}]")
        # txt =
        self.dss.text(f"Save Circuit dir=" + mainpath + "/cartella")     # scrittura della cartella degli elementi



        # Dato il nome dell'elemento (e.g. "transformer.WPG_TR"), vengono definite:
        # - le categorie dal suffisso del nome dell'elemento, dopo l'ultimo "_" (e.g. "TR")
        # - le macrocategorie (viene definito in DSS la paete prima del punto (e.g. "transformer")
        # - il nome dell'elemento (in DSS è la parte dopo il punto e.g. "WPG_TR")
        for item in self.dss.circuit.elements_names:
            [tag, el] = item.split('.')
            if tag.lower() != 'energymeter':
                if tag == 'Vsource':
                    cat = 'ExternalGrid'
                else:
                    rad = el.split('_')[0].lower()
                    des = item.split('_')[len(item.split('_')) - 1].lower()
                    if des in dsstag[tag.lower()]:
                        cat = dsstag[tag.lower()][des]
                    elif rad in dsstag[tag.lower()]:
                        cat = dsstag[tag.lower()][rad]
                    else:
                        cat = dsstag[tag.lower()]['default']

                # viene inizializzato il sotto-dizionario dell'elemento
                dict_initialize(el, cat)

                # self.read(el)           # vengono letti i parametri e la topologia dell'elemento
                self.read_new(el)       # lettura di parametri e topologia degli elementi dalla cartella degli elementi
        self.node_solve()           # risoluzione delle tensioni dei nodi non definiti

        # In OpenDSS non è possibile ricavare la tensione delle busbar non sottese a trasformatori,
        # o non connesse a elementi terminali.
        # La funzione self.node_define serve a definire le tensioni HV dei trasformatori delle busbar a monte di essi
        # self.node_define()    # TODO: Probabilmente deve essere riattivata
        # self.save()

    # def save(self):
    #     with open('CityArea.yml', 'w') as file:
    #         yaml.dump(v, file)
    #         file.close()
    #     print('meters', self.dss.meters.names)

        # -- Metodo per definire le zone -----------------------------------------------------------------------
        if self.dss.meters.names != ['NONE']:
            for i in range(len(self.dss.meters.names)):
                meter = self.dss.meters.names[i]
                # print(meter)
                self.dss.meters.name = meter
                # print(self.dss.meters.all_pce_in_zone)
                # print(self.dss.meters.all_branches_in_zone)
                # print()

    def read_new(self, el):
        mcat = mcat_find(el)
        cat = v[el]['category']

        # if cat == 'AC-BESS':
        #     print('Stop')

        if mcat not in mc['Node']:
            self.dss.circuit.set_active_element(mcat + '.' + el)  # viene richiamato l'elemento in OpenDSS
            v[el]['par']['out-of-service'] = not self.dss.cktelement.is_enabled  # verifica se l'elemento è "enabled"

            # lettura dei parametri dalle righe di dss
            par = self.readline(el)     # TODO: vedi commento in self.readline

            for p in new_par_dict[cat]['par'].keys() - ['others', 'linecode']:  # todo: forse da modificare in base al TODO precedente
                # print(cat, p, new_par_dict[cat]['par'])
                try:
                    v[el]['par'][p] = par[new_par_dict[cat]['par'][p]['label']]
                except:
                    v[el]['par'][p] = new_par_dict[cat]['par'][p]['default']

            # definisco la connessione degli elementi come array
            if mcat == 'Line':
                v[el]['top']['conn'] = [par['bus1'].lower(), par['bus2'].lower()]
            elif mcat == 'Transformer':
                v[el]['top']['conn'] = par['buses']
            else:
                v[el]['top']['conn'] = [par['bus1'].lower()]

            # Definizione delle busbar
            for i in range(len(v[el]['top']['conn'])):
                node = v[el]['top']['conn'][i].lower()  # i nomi devono essere in minuscolo

                if node not in v.keys():    # se il nodo non è stato già configurato
                    tag = node.split('_')[len(node.split('_')) - 1]
                    if tag in ['dc-bb' or 'dc-node']:
                        node_cat = 'DC-Node'
                    else:
                        node_cat = 'AC-Node'
                    # node_cat = c[tag]
                    dict_initialize(node, node_cat)  # viene inizializzato
                    # la tipologia del nodo dipende dalla desinenza del nome.
                    if node.split('_')[len(node.split('_')) - 1] in ['dc-node', 'dc-bb']:
                        v[node]['category'] = 'DC-Node'  # ""
                    else:
                        v[node]['category'] = 'AC-Node'  # ""

                    rel_initialize(node)    # inizializzazione del sottodizionario "rel" del nodo
                    lf_initialize(node)     # inizializzazione del sottodizionario "lf" del nodo
                    v[node]['par']['out-of-service'] = False    # il nodo è in servizio di default

                v[node]['top']['conn'].append(el)   # viene aggiunto l'elemento corrente al nodo

                # Scrivo la tensione del nodo, solo se l'elemento di partenza non è una linea
                if mcat not in ['Line']:
                    v[node]['par']['Vn'] = [v[el]['par']['Vn'][i]]

                # TODO: IMPORTANTE: Definire la tensione delle busbar connesse solo a delle linee.
                #  Probabilmente sarebbe utile creare una "coda" di busbar non risolte, e risolverle singolarmente
                # elif node not in self.unr_nodes:
                #     self.unr_nodes.append(node)

            # Per le linee, bisogna importare i parametri da LineCode.dss
            if cat in mc['Line']:
                if 'linecode' in par:
                    linecat = cat.split('-')[0] + '-LineCode'   # AC-LineCode o DC-LineCode
                    linetype = par['linecode']
                    v[linetype] = dict()                # Necessario per self.readline. Poi verrà elimiato
                    v[linetype]['category'] = linecat   # Necessario per self.readline. Poi verrà elimiato
                    v[el]['top']['linetype'] = linetype
                    par = self.readline(linetype)
                    for p in new_par_dict[linecat]['par'].keys() - ['others']:
                        v[el]['par'][p] = par[new_par_dict[linecat]['par'][p]['label']]
                    v.pop(linetype)                     # Non serve più

        # Imposto inizlalmente il profilo per carichi e generatori
        if cat in mc['Load'] + mc['Generator']:
            # create_profile(el)  # Se si vuole creare un profilo in apertura

            v[el]['par']['profile']['curve'] = 1
            v[el]['par']['profile']['name'] = None

            if cat in mc['Generator']:
                v[el]['par']['eff'] = 1
                if cat in ['AC-BESS', 'DC-BESS']:   # Si ipotizza che la capacità delle batterie sia inizalmente 0
                    v[el]['par']['cap'] = 2 * v[el]['par']['P']
                    v[el]['par']['profile']['curve'] = 0
                    v[el]['par']['SOC'] = 50
                    # print('BESS', el)

    def node_solve(self):
        for el in v:
            if v[el]['category'] in mc['Node']:
                if 'Vn' not in v[el]['par']:
                    self.unr_nodes.append(el)

        while self.unr_nodes:
            solv_nodes = []
            for node in self.unr_nodes:
                lines = []
                for conn in v[node]['top']['conn']:
                    if v[conn]['category'] in mc['Line']:
                        buses = copy.deepcopy(v[conn]['top']['conn'])
                        # buses = []
                        buses.remove(node)
                        bus = buses[0]
                        if bus not in self.unr_nodes:
                            v[node]['par']['Vn'] =[0]
                            v[node]['par']['Vn'][0] = v[bus]['par']['Vn'][0]
                            solv_nodes.append(node)
                            break
            for node in solv_nodes:
                self.unr_nodes.remove(node)

        pass

    # Scrittura della definizione dell'elemento in OpenDSS
    def writeline(self, el, time):
        mcat = mcat_find(el)
        cat = v[el]['category']

        par = ''
        buses = ''

        # Scrittura della parte dei parametri
        for p in new_par_dict[cat]['par']['others']:
            par = par + p + '=' + new_par_dict[cat]['par']['others'][p] + ' '
        for p in new_par_dict[cat]['par'].keys() - ['others']:
            if p == 'Vn' and mcat != 'Transformer':     # La tensione è memorizzata come array anche se è singola
                par = par + new_par_dict[cat]['par'][p]['label'] + '=' + str(v[el]['par'][p][0]) + ' '
            elif p == 'P':
                if v[el]['par']['profile']['name']:
                    f = v[el]['par']['profile']['curve'][time]
                else:
                    f = v[el]['par']['profile']['curve']
                par = par + new_par_dict[cat]['par'][p]['label'] + '=' + str(v[el]['par'][p] * f) + ' '
            elif p != 'cap':
                par = par + new_par_dict[cat]['par'][p]['label'] + '=' + str(v[el]['par'][p]) + ' '
        #     TODO: da implementare la gestione della capacità della batteria

        # Verifica se l'elemento è in servizio
        serv = ''
        if 'out-of-service' in v[el]['par'].keys():
            serv = 'enabled=' + str(not bool(v[el]['par']['out-of-service']))

        # Verifica sel le connessioni sono memorizzzate come array o come due voci singole
        if len(new_par_dict[cat]['top']['conn']['label']) == len(v[el]['top']['conn']):
            for i in range(len(new_par_dict[cat]['top']['conn']['label'])):
                buses = buses + new_par_dict[cat]['top']['conn']['label'][i] + '=' + v[el]['top']['conn'][i] + ' '
        else:
            buses = buses + new_par_dict[cat]['top']['conn']['label'][0] + '=' + str(v[el]['top']['conn']) + ' '

        if mcat == 'Vsource':
            line = 'Edit "Vsource.' + el + ' '
        else:
            line = 'New "' + mcat + '.' + el + '" '

        # Nel caso delle linee, bisogna definire anche il LineType
        line0 = ''
        if 'type' in new_par_dict[cat]['top'].keys():
            line = line + 'linecode=' + v[el]['top']['linetype'] + ' '

            linetype = cat.split('-')[0] + '-LineCode'
            for p in new_par_dict[linetype]['par']['others']:
                line0 = line0 + p + '=' + new_par_dict[linetype]['par']['others'][p] + ' '

            for p in new_par_dict[linetype]['par'].keys() - ['others']:
                line0 = line0 + new_par_dict[linetype]['par'][p]['label'] + '=' + str(v[el]['par'][p]) + ' '

            line0 = 'New "LineCode.' + v[el]['top']['linetype'] + '" ' + line0
            dss_cat['LineCode'].append(line0)   # Memorizzazione del LineType

            line = line + 'linecode=' + v[el]['top']['linetype'] + ' '

        line = line + buses + par + serv

        dss_cat[mcat].append(line)              # Memorizzazione dell'elemento

        return line     # TODO: Perchè?

    def full_parse_profil_to_dss(self, t0=None, steps=None):
        # print('start')
        for el in v:
            self.__setattr__(el + '_pd', pd.DataFrame(index=list(range(steps)),
                                                      columns=['i0', 'p0', 'q0', 'v0', 'i1', 'p1', 'q1', 'v1']))

        for i in range(steps):
            self.full_parse_to_dss(t0 + i)

            for el in v:
                self.results_store_pd(el, i)

    def full_parse_profil_to_dss_polars(self, t0=None, steps=None):
        # print('start')
        for el in v:
            self.__setattr__(el + '_pl', pl.DataFrame({
                'i0': list(float(0) for i in range(steps)),
                'p0': list(float(0) for i in range(steps)),
                'q0': list(float(0) for i in range(steps)),
                'v0': list(float(0) for i in range(steps)),
                'i1': list(float(0) for i in range(steps)),
                'p1': list(float(0) for i in range(steps)),
                'q1': list(float(0) for i in range(steps)),
                'v1': list(float(0) for i in range(steps))
            }))
            # 'p0', 'q0', 'v0', 'i1', 'p1', 'q1', 'v1']))

        for i in range(steps):
            self.full_parse_to_dss(t0 + i)
            self.solve()

            # TODO: da riattivare -----------------
            for el in v:
                self.results_store_pl(el, i)

        path = str(mainpath) + '/_temp/elements/'
        for el in v:
            self.__getattribute__(el + '_pl').write_csv(path + el + '.csv', separator='\t')
        # TODO ---------------------------------

        # print(self.__getattribute__('a_24_ac-load_pl'))

    def full_parse_profil_to_dss_csv(self, t0=None, steps=None):
        # print('start')
        path = str(mainpath) + '/_temp/elements/'

        for el in v:
            # for p in ['i0', 'p0', 'q0', 'v0', 'i1', 'p1', 'q1', 'v1']:
            self.__setattr__(el + '_csv', open(path + el + '.csv', 'w', newline=''))
            self.__setattr__(el + 'csv_writer', csv.writer(self.__getattribute__(el + '_csv'), delimiter='\t'))
            self.__getattribute__(el + 'csv_writer').writerow(['i0', 'p0', 'q0', 'v0', 'i1', 'p1', 'q1', 'v1'])
            # self.__setattr__(el + '_pd', pd.DataFrame(index=list(range(steps)),
            #                                           columns=['i0', 'p0', 'q0', 'v0', 'i1', 'p1', 'q1', 'v1']))

        for i in range(steps):
            self.full_parse_to_dss(t0 + i)
            self.solve()

            for el in v:
                self.results_store_csv(el, i)

        for el in v:
            self.__getattribute__(el + '_csv').close()

        # path = str(mainpath) + '/_temp/elements/'
        # for el in v:
        #     np.savetxt(path + el + '.csv', self.__getattribute__(el + '_np'), delimiter='\t')
        #     # self.__getattribute__(el + '_np').savetxt(path + el + '.csv', separator='\t')

    def full_parse_profil_to_dss_numpy(self, t0=None, steps=None):
        # print('start')
        for el in v:
            # for p in ['i0', 'p0', 'q0', 'v0', 'i1', 'p1', 'q1', 'v1']:
            self.__setattr__(el + '_np', np.zeros((steps, 8)))

            # self.load_np = np.zeros((steps, 8))
            # self.__setattr__(el + '_pd', pd.DataFrame(index=list(range(steps)),
            #                                           columns=['i0', 'p0', 'q0', 'v0', 'i1', 'p1', 'q1', 'v1']))

        for i in range(steps):
            self.full_parse_to_dss(t0 + i)
            self.solve()

            for el in v:
                self.results_store_np(el, i)

        path = str(mainpath) + '/_temp/elements/'
        for el in v:
            np.savetxt(path + el + '.csv', self.__getattribute__(el + '_np'), delimiter='\t')
            # self.__getattribute__(el + '_np').savetxt(path + el + '.csv', separator='\t')

        # for el in v:
        #     for p in ['i0', 'p0', 'q0', 'v0', 'i1', 'p1', 'q1', 'v1']:
        #         if self.__getattribute__(el + '_' + p):
        #             # print(el, p)
        #             self.__getattribute__(el + '_pd')[p] = self.__getattribute__(el + '_' + p)

    def full_parse_profil_to_dss_numpy_chatGPT(self, t0=None, steps=None):
        # print('start')
        for el in v:
            # for p in ['i0', 'p0', 'q0', 'v0', 'i1', 'p1', 'q1', 'v1']:
            self.__setattr__(el + '_np', np.zeros((steps, 8)))

            # self.load_np = np.zeros((steps, 8))
            # self.__setattr__(el + '_pd', pd.DataFrame(index=list(range(steps)),
            #                                           columns=['i0', 'p0', 'q0', 'v0', 'i1', 'p1', 'q1', 'v1']))

        for i in range(steps):
            self.full_parse_to_dss(t0 + i)
            self.solve()

            for el in v:
                self.results_store_np_chatGPT(el, i)

        path = str(mainpath) + '/_temp/elements/'
        for el in v:
            np.savetxt(path + el + '.csv', self.__getattribute__(el + '_np'), delimiter='\t')
            # self.__getattribute__(el + '_np').savetxt(path + el + '.csv', separator='\t')

        # for el in v:
        #     for p in ['i0', 'p0', 'q0', 'v0', 'i1', 'p1', 'q1', 'v1']:
        #         if self.__getattribute__(el + '_' + p):
        #             # print(el, p)
        #             self.__getattribute__(el + '_pd')[p] = self.__getattribute__(el + '_' + p)

    def full_parse_profil_to_dss_numpy_chatGPT_nodata(self, t0=None, steps=None):
        # print('start')
        for el in v:
            # for p in ['i0', 'p0', 'q0', 'v0', 'i1', 'p1', 'q1', 'v1']:
            self.__setattr__(el + '_np', np.zeros((steps, 8)))

            # self.load_np = np.zeros((steps, 8))
            # self.__setattr__(el + '_pd', pd.DataFrame(index=list(range(steps)),
            #                                           columns=['i0', 'p0', 'q0', 'v0', 'i1', 'p1', 'q1', 'v1']))

        for i in range(steps):
            self.full_parse_to_dss(t0 + i)
            self.solve()

            for el in v:
                self.results_store_np_chatGPT_nodata(el, i)

        path = str(mainpath) + '/_temp/elements/'
        for el in v:
            np.savetxt(path + el + '.csv', self.__getattribute__(el + '_np'), delimiter='\t')
            # self.__getattribute__(el + '_np').savetxt(path + el + '.csv', separator='\t')

        # for el in v:
        #     for p in ['i0', 'p0', 'q0', 'v0', 'i1', 'p1', 'q1', 'v1']:
        #         if self.__getattribute__(el + '_' + p):
        #             # print(el, p)
        #             self.__getattribute__(el + '_pd')[p] = self.__getattribute__(el + '_' + p)

    def full_parse_profil_to_dss_array(self, t0=None, steps=None):
        # print('start')
        for el in v:
            for p in ['i0', 'p0', 'q0', 'v0', 'i1', 'p1', 'q1', 'v1']:
                self.__setattr__(el + '_' + p, [])
            self.__setattr__(el + '_pd', pd.DataFrame(index=list(range(steps)),
                                                      columns=['i0', 'p0', 'q0', 'v0', 'i1', 'p1', 'q1', 'v1']))

        for i in range(steps):
            self.full_parse_to_dss(t0 + i)

            for el in v:
                self.results_store_arr(el, i)

        for el in v:
            for p in ['i0', 'p0', 'q0', 'v0', 'i1', 'p1', 'q1', 'v1']:
                if self.__getattribute__(el + '_' + p):
                    # print(el, p)
                    self.__getattribute__(el + '_pd')[p] = self.__getattribute__(el + '_' + p)

        # print(self.__getattribute__('a_24_ac-load_pd'))
        # print(self.__getattribute__('a_24_ac-load_p0'))

    # Scrittura di tutti gli elementi in OpenDSS
    def full_parse_to_dss(self, time=None):

        self.dss.text('Clear')
        self.dss.text('New object=circuit.dss_grid basekv=' + str(v['source']['par']['Vn'][0])
                      + ' bus1=' + str(v['source']['top']['conn'][0]))

        # Popolamento dei comandi pero ogni macrocategoria di OpenDSS
        for key in dss_cat.keys():
            dss_cat[key] = []

        open('lista.txt', 'w').close()
        f = open('lista.txt', 'a')
        for el in v:
            mcat = mcat_find(el)
            if mcat in dss_cat:
                # myline = self.writeline(el, time)
                f.write(self.writeline(el, time) + '\n')
                # print('done')
        f.close()

        # Scrittura dei comandi in OpenDSS
        for mcat in dss_cat:
            for r in dss_cat[mcat]:
                self.dss.text(r)

        # self.solve()

        # print(v['a_10_ac-load']['lf']['i'])

        self.dss.text(f"Save Circuit dir=" + mainpath + "/cartella")

    # Compilazione di tutti gli elementi in OpenDSS
    def write_all(self, t=None):
        for el in v.keys():
            self.write(el=el, t=t)

    # Compilazione di un elemento in OpenDSS. TODO: Da ridefinire in base alla nuova modalità di scrittura
    def write(self, el, t=None):    # t è il tempo da considerare nel profilo dell'elemento (se presente)

        # Viene definita la macrocategoria
        mcat = None
        cat = v[el]['category']
        for m in mc.keys():
            if cat in mc[m]:
                mcat = m
                break

        self.dss.circuit.set_active_element(mcat + '.' + el)    # richiamo dell'elemento in OpenDSS

        # Se gli elementi sono diversi da connessioni (linee o trasformatori=, possono essere impostati conme
        # "Out-Of-Service"
        if cat not in ['AC-Line', 'DC-Line', '2W-Transformer', 'PWM', 'DC-DC-Converter']:
            self.dss.cktelement.enabled(not v[el]['par']['out-of-service'])

        # altrimenti, bisogna settare i terminali come "Open"
        elif v[el]['par']['out-of-service']:
            self.dss.text('Open object=' + mcat + '.' + el + ' term=1')
            self.dss.text('Open object=' + mcat + '.' + el + ' term=2')
        else:
            self.dss.text('Close object=' + mcat + '.' + el + ' term=1')
            self.dss.text('Close object=' + mcat + '.' + el + ' term=2')
        # Todo: bisogna gestire il caso del Source (se si vuole rendere Out-Of-Service)

        f = 1   # indica il fattore di scala della potenza
        # Se viene impostato un tempo "t", e l'elemento è un generatore o un carico, ed esiste un profilo:
        if t is not None and cat in mc['Generator'] + mc['Load'] and v[el]['par']['profile']['curve'] is not None:
            self.dss.__getattribute__(mcat.lower() + 's').__setattr__('name', el)   # richiamo dell'elemento
            # e.g. self.dss.transformers.name = 'WPG_TR'
            # "mcat.lower() + 's'" indica la macrocategoria in OpenDSS (e.g. "generators" o "loads").
            # La macrocategoria ("mcat") deve essere scritta in minuscolo (".lower") e al plurale ("+ 's'")
            f = v[el]['par']['profile']['curve'][int(t)]    # il fattore di scala è il punto del profilo relativo a t

        # Scrittura dei parametri dell'elemento
        if cat not in ['ExternalGrid', 'AC-Node', 'DC-Node']:     # Solo se non sono Source o Nodi
            self.dss.__getattribute__(mcat.lower() + 's').__setattr__('name', el)   # richiamo dell'elemento
            for par in par_dict[cat].keys():
                if par in ['P', 'Q']:   # solo se il parametro è P o Q bisogna considerare il fattore di scala
                    self.dss.__getattribute__(mcat.lower() + 's').__setattr__(par_dict[cat][par], v[el]['par'][par] * f)
                else:
                    self.dss.__getattribute__(mcat.lower() + 's').__setattr__(par_dict[cat][par], v[el]['par'][par])
        # TODO: da definire come gestire le variazioni su Source e sui Nodi

    # Aggiornamento del dizionario dei risultati di uno studio singolo. TODO: Ridefinire
    def results_store(self, el):
        # if v[el]['category'] in mc['BESS']:
        #     print('break')

        if v[el]['category'] != 'Node':     # per tutti gli elementi tranne che per i Nodi

            if not v[el]['par']['out-of-service']:  # Se l'elemento è in servizio
                # mcat = ''
                # for m in mc.keys():
                #     if v[el]['category'] in mc[m]:
                #         mcat = m
                #         break
                mcat = mcat_find(el)

                # Le parti DC sono in pratica porzioni AC, di cui si considera la fase globale.
                # Per questo, per la corrente bisogna usare un fattore di correzione "cf"
                cf0, cf1 = 1, 1     # fattore di correzione per le parti AC
                if v[el]['category'] in DC_elem:
                    cf0 = 3 ** 0.5    # fattore di correzione per le porzioni DC a monte
                if v[el]['category'] in DC_elem + ['PWM']:
                    cf1 = 3 ** 0.5  # fattore di correzione per pe porzioni DC a valle

                self.dss.circuit.set_active_element(mcat + '.' + el)    # l'elemento è selezionato

                if v[el]['category'] not in mc['Line'] + mc['Transformer']:     # per gli elemnenti terminali

                    # le potenza globali sono date dalla somma delle potenze delle singole fasi
                    p, q = 0, 0
                    for i in range(0, 3):
                        p = p + self.dss.cktelement.powers[2 * i]
                        q = q + self.dss.cktelement.powers[2 * i + 1]

                    # Accodamento nel vettore dei risultati nel dizionario
                    # dei valori di P, Q, V, i con i relativi fattori di correzione
                    v[el]['lf']['p'].append(p)
                    v[el]['lf']['q'].append(q)
                    v[el]['lf']['v'].append(self.dss.cktelement.voltages_mag_ang[0] * 3**0.5)
                    v[el]['lf']['i'].append(self.dss.cktelement.currents_mag_ang[0] * cf0)

                else:                           # per le linee
                    if v[el]['category'] in mc['Line']:     # per le linee
                        j = 6
                    else:                                   # per i Transformer
                        j = 8

                    # le potenza globali sono date dalla somma delle potenze delle singole fasi
                    p0, q0, p1, q1 = 0, 0, 0, 0
                    for i in range(0, 3):
                        p0 = p0 + self.dss.cktelement.powers[2 * i]
                        q0 = q0 + self.dss.cktelement.powers[2 * i + 1]
                        p1 = p1 - self.dss.cktelement.powers[2 * i + j]
                        q1 = q1 - self.dss.cktelement.powers[2 * i + j + 1]

                    # Inserimento nel dizionario, per ogni lato,
                    # dei valori di P, Q, V, i con i relativi fattori di correzione
                    v[el]['lf']['p'][0].append(p0)
                    v[el]['lf']['q'][0].append(q0)
                    v[el]['lf']['p'][1].append(p1)
                    v[el]['lf']['q'][1].append(q1)
                    v[el]['lf']['v'][0].append(self.dss.cktelement.voltages_mag_ang[0] * 3**0.5)
                    v[el]['lf']['v'][1].append(self.dss.cktelement.voltages_mag_ang[j] * 3**0.5)
                    v[el]['lf']['i'][0].append(self.dss.cktelement.currents_mag_ang[0] * cf0)
                    v[el]['lf']['i'][1].append(self.dss.cktelement.currents_mag_ang[j] * cf1)

            else:                                   # se l'elemento non è in servizio
                if v[el]['category'] not in mc['Line'] + mc['Transformer']:     # per gli elemnenti terminali
                    v[el]['lf']['p'].append(0)
                    v[el]['lf']['q'].append(0)
                    v[el]['lf']['v'].append(0)
                    v[el]['lf']['i'].append(0)
                else:                                                           # per linee e trasformatori
                    v[el]['lf']['p'][0].append(0)
                    v[el]['lf']['q'][0].append(0)
                    v[el]['lf']['p'][1].append(0)
                    v[el]['lf']['q'][1].append(0)
                    v[el]['lf']['v'][0].append(0)
                    v[el]['lf']['v'][1].append(0)
                    v[el]['lf']['i'][0].append(0)
                    v[el]['lf']['i'][1].append(0)

        else:                               # per i nodi e per il Source
            self.dss.circuit.set_active_bus(el)
            v[el]['lf']['v'].append(self.dss.cktelement.voltages_mag_ang[0] * 3 ** 0.5)

        # if v[el]['category'] == 'ExternalGrid':
        #     v[el]['lf']['p'] = -1 * v[el]['lf']['p']
        #     v[el]['lf']['q'] = -1 * v[el]['lf']['q']

    # TODO: verificare se è possibile rendere self.results_append e self.results_store come un'unica funzione

    def results_store_opt(self, el):
        sqrt3 = 3 ** 0.5

        if v[el]['category'] != 'Node':     # per tutti gli elementi tranne che per i Nodi
            if not v[el]['par']['out-of-service']:  # Se l'elemento è in servizio
                mcat = mcat_find(el)

                # Le parti DC sono in pratica porzioni AC, di cui si considera la fase globale.
                # Per questo, per la corrente bisogna usare un fattore di correzione "cf"
                cf0, cf1 = 1, 1     # fattore di correzione per le parti AC
                if v[el]['category'] in DC_elem:
                    cf0 = sqrt3     # fattore di correzione per le porzioni DC a monte
                if v[el]['category'] in DC_elem + ['PWM']:
                    cf1 = sqrt3     # fattore di correzione per pe porzioni DC a valle

                self.dss.circuit.set_active_element(mcat + '.' + el)    # l'elemento è selezionato

                if v[el]['category'] not in mc['Line'] + mc['Transformer']:     # per gli elemnenti terminali
                    powers = self.dss.cktelement.powers

                    # le potenza globali sono date dalla somma delle potenze delle singole fasi
                    p = sum(powers[2 + i] for i in range(3))
                    q = sum(powers[2 + i + 1] for i in range(3))
                    # p, q = 0, 0
                    # for i in range(0, 3):
                    #     p = p + self.dss.cktelement.powers[2 * i]
                    #     q = q + self.dss.cktelement.powers[2 * i + 1]

                    # Accodamento nel vettore dei risultati nel dizionario
                    # dei valori di P, Q, V, i con i relativi fattori di correzione
                    v[el]['lf']['p'].append(p)
                    v[el]['lf']['q'].append(q)
                    v[el]['lf']['v'].append(self.dss.cktelement.voltages_mag_ang[0] * 3**0.5)
                    v[el]['lf']['i'].append(self.dss.cktelement.currents_mag_ang[0] * cf0)

                else:                           # per le linee
                    j = 6 if v[el]['category'] in mc['Line'] else 8
                    # if v[el]['category'] in mc['Line']:     # per le linee
                    #     j = 6
                    # else:                                   # per i Transformer
                    #     j = 8

                    powers = self.dss.cktelement.powers

                    # le potenza globali sono date dalla somma delle potenze delle singole fasi
                    p0 = sum(powers[2 * i] for i in range(3))
                    q0 = sum(powers[2 * i + 1] for i in range(3))
                    p1 = sum(powers[2 * i + j] for i in range(3))
                    q1 = sum(powers[2 * i + j + 1] for i in range(3))

                    # p0, q0, p1, q1 = 0, 0, 0, 0
                    # for i in range(0, 3):
                    #     p0 = p0 + self.dss.cktelement.powers[2 * i]
                    #     q0 = q0 + self.dss.cktelement.powers[2 * i + 1]
                    #     p1 = p1 - self.dss.cktelement.powers[2 * i + j]
                    #     q1 = q1 - self.dss.cktelement.powers[2 * i + j + 1]

                    # Inserimento nel dizionario, per ogni lato,
                    # dei valori di P, Q, V, i con i relativi fattori di correzione
                    v[el]['lf']['p'][0].append(p0)
                    v[el]['lf']['q'][0].append(q0)
                    v[el]['lf']['p'][1].append(p1)
                    v[el]['lf']['q'][1].append(q1)
                    v[el]['lf']['v'][0].append(self.dss.cktelement.voltages_mag_ang[0] * 3**0.5)
                    v[el]['lf']['v'][1].append(self.dss.cktelement.voltages_mag_ang[j] * 3**0.5)
                    v[el]['lf']['i'][0].append(self.dss.cktelement.currents_mag_ang[0] * cf0)
                    v[el]['lf']['i'][1].append(self.dss.cktelement.currents_mag_ang[j] * cf1)

            else:                                   # se l'elemento non è in servizio
                if v[el]['category'] not in mc['Line'] + mc['Transformer']:     # per gli elemnenti terminali
                    v[el]['lf'][['p', 'q', 'v', 'i']].append(0)
                    # v[el]['lf']['p'].append(0)
                    # v[el]['lf']['q'].append(0)
                    # v[el]['lf']['v'].append(0)
                    # v[el]['lf']['i'].append(0)
                else:                                                           # per linee e trasformatori
                    v[el]['lf'][['p', 'q', 'v', 'i']][0, 1].append(0)
                    # v[el]['lf']['p'][0].append(0)
                    # v[el]['lf']['q'][0].append(0)
                    # v[el]['lf']['p'][1].append(0)
                    # v[el]['lf']['q'][1].append(0)
                    # v[el]['lf']['v'][0].append(0)
                    # v[el]['lf']['v'][1].append(0)
                    # v[el]['lf']['i'][0].append(0)
                    # v[el]['lf']['i'][1].append(0)

        else:                               # per i nodi e per il Source
            self.dss.circuit.set_active_bus(el)
            v[el]['lf']['v'].append(self.dss.cktelement.voltages_mag_ang[0] * 3 ** 0.5)
    # TODO: verificare se è possibile rendere self.results_append e self.results_store come un'unica funzione

    # Test storing con Pandas
    def results_store_pd(self, el, row):
        if v[el]['category'] != 'Node':     # per tutti gli elementi tranne che per i Nodi

            if not v[el]['par']['out-of-service']:  # Se l'elemento è in servizio
                mcat = mcat_find(el)

                # Le parti DC sono in pratica porzioni AC, di cui si considera la fase globale.
                # Per questo, per la corrente bisogna usare un fattore di correzione "cf"
                cf0, cf1 = 1, 1     # fattore di correzione per le parti AC
                if v[el]['category'] in DC_elem:
                    cf0 = 3 ** 0.5    # fattore di correzione per le porzioni DC a monte
                if v[el]['category'] in DC_elem + ['PWM']:
                    cf1 = 3 ** 0.5  # fattore di correzione per pe porzioni DC a valle

                self.dss.circuit.set_active_element(mcat + '.' + el)    # l'elemento è selezionato

                if v[el]['category'] not in mc['Line'] + mc['Transformer']:     # per gli elemnenti terminali

                    # le potenza globali sono date dalla somma delle potenze delle singole fasi
                    p, q = 0, 0
                    for i in range(0, 3):
                        p = p + self.dss.cktelement.powers[2 * i]
                        q = q + self.dss.cktelement.powers[2 * i + 1]

                    # Accodamento nel vettore dei risultati nel dizionario
                    # dei valori di P, Q, V, i con i relativi fattori di correzione
                    self.__getattribute__(el + '_pd').loc[row, 'p0'] = p
                    self.__getattribute__(el + '_pd').loc[row, 'q0'] = q
                    self.__getattribute__(el + '_pd').loc[row, 'v0'] = self.dss.cktelement.voltages_mag_ang[0] * 3**0.5
                    self.__getattribute__(el + '_pd').loc[row, 'i0'] = self.dss.cktelement.currents_mag_ang[0] * cf0

                else:                           # per le linee
                    if v[el]['category'] in mc['Line']:     # per le linee
                        j = 6
                    else:                                   # per i Transformer
                        j = 8

                    # le potenza globali sono date dalla somma delle potenze delle singole fasi
                    p0, q0, p1, q1 = 0, 0, 0, 0
                    for i in range(0, 3):
                        p0 = p0 + self.dss.cktelement.powers[2 * i]
                        q0 = q0 + self.dss.cktelement.powers[2 * i + 1]
                        p1 = p1 - self.dss.cktelement.powers[2 * i + j]
                        q1 = q1 - self.dss.cktelement.powers[2 * i + j + 1]

                    # Inserimento nel dizionario, per ogni lato,
                    # dei valori di P, Q, V, i con i relativi fattori di correzione
                    self.__getattribute__(el + '_pd').loc[row, 'p0'] = p0
                    self.__getattribute__(el + '_pd').loc[row, 'q0'] = q0
                    self.__getattribute__(el + '_pd').loc[row, 'p1'] = p1
                    self.__getattribute__(el + '_pd').loc[row, 'q1'] = q1
                    self.__getattribute__(el + '_pd').loc[row, 'v0'] = self.dss.cktelement.voltages_mag_ang[0] * 3**0.5
                    self.__getattribute__(el + '_pd').loc[row, 'v1'] = self.dss.cktelement.voltages_mag_ang[j] * 3**0.5
                    self.__getattribute__(el + '_pd').loc[row, 'i0'] = self.dss.cktelement.currents_mag_ang[0] * cf0
                    self.__getattribute__(el + '_pd').loc[row, 'i1'] = self.dss.cktelement.currents_mag_ang[j] * cf1

            else:                                   # se l'elemento non è in servizio
                if v[el]['category'] not in mc['Line'] + mc['Transformer']:     # per gli elemnenti terminali
                    self.__getattribute__(el + '_pd').loc[row, 'p0'] = 0
                    self.__getattribute__(el + '_pd').loc[row, 'q0'] = 0
                    self.__getattribute__(el + '_pd').loc[row, 'v0'] = 0
                    self.__getattribute__(el + '_pd').loc[row, 'i0'] = 0
                else:                                                           # per linee e trasformatori
                    self.__getattribute__(el + '_pd').loc[row, 'p0'] = 0
                    self.__getattribute__(el + '_pd').loc[row, 'q0'] = 0
                    self.__getattribute__(el + '_pd').loc[row, 'p1'] = 0
                    self.__getattribute__(el + '_pd').loc[row, 'q1'] = 0
                    self.__getattribute__(el + '_pd').loc[row, 'v0'] = 0
                    self.__getattribute__(el + '_pd').loc[row, 'v1'] = 0
                    self.__getattribute__(el + '_pd').loc[row, 'i0'] = 0
                    self.__getattribute__(el + '_pd').loc[row, 'i1'] = 0

        else:                               # per i nodi e per il Source
            self.dss.circuit.set_active_bus(el)
            v[el]['lf']['v'].append(self.dss.cktelement.voltages_mag_ang[0] * 3 ** 0.5)
    # TODO: verificare se è possibile rendere self.results_append e self.results_store come un'unica funzione

    # Test storing con Polars
    def results_store_pl(self, el, row):
        if v[el]['category'] != 'Node':     # per tutti gli elementi tranne che per i Nodi

            if not v[el]['par']['out-of-service']:  # Se l'elemento è in servizio
                mcat = mcat_find(el)

                # Le parti DC sono in pratica porzioni AC, di cui si considera la fase globale.
                # Per questo, per la corrente bisogna usare un fattore di correzione "cf"
                cf0, cf1 = 1, 1     # fattore di correzione per le parti AC
                if v[el]['category'] in DC_elem:
                    cf0 = 3 ** 0.5    # fattore di correzione per le porzioni DC a monte
                if v[el]['category'] in DC_elem + ['PWM']:
                    cf1 = 3 ** 0.5  # fattore di correzione per pe porzioni DC a valle

                self.dss.circuit.set_active_element(mcat + '.' + el)    # l'elemento è selezionato

                if v[el]['category'] not in mc['Line'] + mc['Transformer']:     # per gli elemnenti terminali

                    # le potenza globali sono date dalla somma delle potenze delle singole fasi
                    p, q = 0, 0
                    for i in range(0, 3):
                        p = p + self.dss.cktelement.powers[2 * i]
                        q = q + self.dss.cktelement.powers[2 * i + 1]

                    # Accodamento nel vettore dei risultati nel dizionario
                    # dei valori di P, Q, V, i con i relativi fattori di correzione
                    self.__getattribute__(el + '_pl')[row, 'p0'] = p
                    self.__getattribute__(el + '_pl')[row, 'q0'] = q
                    self.__getattribute__(el + '_pl')[row, 'v0'] = self.dss.cktelement.voltages_mag_ang[0] * 3**0.5
                    self.__getattribute__(el + '_pl')[row, 'i0'] = self.dss.cktelement.currents_mag_ang[0] * cf0

                else:                           # per le linee
                    if v[el]['category'] in mc['Line']:     # per le linee
                        j = 6
                    else:                                   # per i Transformer
                        j = 8

                    # le potenza globali sono date dalla somma delle potenze delle singole fasi
                    p0, q0, p1, q1 = 0, 0, 0, 0
                    for i in range(0, 3):
                        p0 = p0 + self.dss.cktelement.powers[2 * i]
                        q0 = q0 + self.dss.cktelement.powers[2 * i + 1]
                        p1 = p1 - self.dss.cktelement.powers[2 * i + j]
                        q1 = q1 - self.dss.cktelement.powers[2 * i + j + 1]

                    # Inserimento nel dizionario, per ogni lato,
                    # dei valori di P, Q, V, i con i relativi fattori di correzione
                    self.__getattribute__(el + '_pl')[row, 'p0'] = p0
                    self.__getattribute__(el + '_pl')[row, 'q0'] = q0
                    self.__getattribute__(el + '_pl')[row, 'p1'] = p1
                    self.__getattribute__(el + '_pl')[row, 'q1'] = q1
                    self.__getattribute__(el + '_pl')[row, 'v0'] = self.dss.cktelement.voltages_mag_ang[0] * 3**0.5
                    self.__getattribute__(el + '_pl')[row, 'v1'] = self.dss.cktelement.voltages_mag_ang[j] * 3**0.5
                    self.__getattribute__(el + '_pl')[row, 'i0'] = self.dss.cktelement.currents_mag_ang[0] * cf0
                    self.__getattribute__(el + '_pl')[row, 'i1'] = self.dss.cktelement.currents_mag_ang[j] * cf1

            else:                                   # se l'elemento non è in servizio
                if v[el]['category'] not in mc['Line'] + mc['Transformer']:     # per gli elemnenti terminali
                    self.__getattribute__(el + '_pl')[row, 'p0'] = 0
                    self.__getattribute__(el + '_pl')[row, 'q0'] = 0
                    self.__getattribute__(el + '_pl')[row, 'v0'] = 0
                    self.__getattribute__(el + '_pl')[row, 'i0'] = 0
                else:                                                           # per linee e trasformatori
                    self.__getattribute__(el + '_pl')[row, 'p0'] = 0
                    self.__getattribute__(el + '_pl')[row, 'q0'] = 0
                    self.__getattribute__(el + '_pl')[row, 'p1'] = 0
                    self.__getattribute__(el + '_pl')[row, 'q1'] = 0
                    self.__getattribute__(el + '_pl')[row, 'v0'] = 0
                    self.__getattribute__(el + '_pl')[row, 'v1'] = 0
                    self.__getattribute__(el + '_pl')[row, 'i0'] = 0
                    self.__getattribute__(el + '_pl')[row, 'i1'] = 0

        else:                               # per i nodi e per il Source
            self.dss.circuit.set_active_bus(el)
            v[el]['lf']['v'].append(self.dss.cktelement.voltages_mag_ang[0] * 3 ** 0.5)
    # TODO: verificare se è possibile rendere self.results_append e self.results_store come un'unica funzione

    def results_store_np(self, el, row):
        if v[el]['category'] != 'Node':     # per tutti gli elementi tranne che per i Nodi

            if not v[el]['par']['out-of-service']:  # Se l'elemento è in servizio
                mcat = mcat_find(el)

                # Le parti DC sono in pratica porzioni AC, di cui si considera la fase globale.
                # Per questo, per la corrente bisogna usare un fattore di correzione "cf"
                cf0, cf1 = 1, 1     # fattore di correzione per le parti AC
                if v[el]['category'] in DC_elem:
                    cf0 = 3 ** 0.5    # fattore di correzione per le porzioni DC a monte
                if v[el]['category'] in DC_elem + ['PWM']:
                    cf1 = 3 ** 0.5  # fattore di correzione per pe porzioni DC a valle

                self.dss.circuit.set_active_element(mcat + '.' + el)    # l'elemento è selezionato

                if v[el]['category'] not in mc['Line'] + mc['Transformer']:     # per gli elemnenti terminali

                    # le potenza globali sono date dalla somma delle potenze delle singole fasi
                    p, q = 0, 0
                    for i in range(0, 3):
                        p = p + self.dss.cktelement.powers[2 * i]
                        q = q + self.dss.cktelement.powers[2 * i + 1]

                    x = ['i0', 'p0', 'q0', 'v0', 'i1', 'p1', 'q1', 'v1']
                    # Accodamento nel vettore dei risultati nel dizionario
                    # dei valori di P, Q, V, i con i relativi fattori di correzione
                    self.__getattribute__(el + '_np')[row, 1] = p
                    self.__getattribute__(el + '_np')[row, 2] = q
                    self.__getattribute__(el + '_np')[row, 3] = self.dss.cktelement.voltages_mag_ang[0] * 3**0.5
                    self.__getattribute__(el + '_np')[row, 0] = self.dss.cktelement.currents_mag_ang[0] * cf0

                else:                           # per le linee
                    if v[el]['category'] in mc['Line']:     # per le linee
                        j = 6
                    else:                                   # per i Transformer
                        j = 8

                    # le potenza globali sono date dalla somma delle potenze delle singole fasi
                    p0, q0, p1, q1 = 0, 0, 0, 0
                    for i in range(0, 3):
                        p0 = p0 + self.dss.cktelement.powers[2 * i]
                        q0 = q0 + self.dss.cktelement.powers[2 * i + 1]
                        p1 = p1 - self.dss.cktelement.powers[2 * i + j]
                        q1 = q1 - self.dss.cktelement.powers[2 * i + j + 1]

                    # Inserimento nel dizionario, per ogni lato,
                    # dei valori di P, Q, V, i con i relativi fattori di correzione
                    self.__getattribute__(el + '_np')[row, 1] = p0
                    self.__getattribute__(el + '_np')[row, 2] = q0
                    self.__getattribute__(el + '_np')[row, 5] = p1
                    self.__getattribute__(el + '_np')[row, 6] = q1
                    self.__getattribute__(el + '_np')[row, 3] = self.dss.cktelement.voltages_mag_ang[0] * 3**0.5
                    self.__getattribute__(el + '_np')[row, 7] = self.dss.cktelement.voltages_mag_ang[j] * 3**0.5
                    self.__getattribute__(el + '_np')[row, 0] = self.dss.cktelement.currents_mag_ang[0] * cf0
                    self.__getattribute__(el + '_np')[row, 4] = self.dss.cktelement.currents_mag_ang[j] * cf1

            else:                                   # se l'elemento non è in servizio
                if v[el]['category'] not in mc['Line'] + mc['Transformer']:     # per gli elemnenti terminali
                    self.__getattribute__(el + '_np')[row, 1] = 0
                    self.__getattribute__(el + '_np')[row, 2] = 0
                    self.__getattribute__(el + '_np')[row, 3] = 0
                    self.__getattribute__(el + '_np')[row, 0] = 0
                else:                                                           # per linee e trasformatori
                    self.__getattribute__(el + '_np')[row, 1] = 0
                    self.__getattribute__(el + '_np')[row, 2] = 0
                    self.__getattribute__(el + '_np')[row, 5] = 0
                    self.__getattribute__(el + '_np')[row, 6] = 0
                    self.__getattribute__(el + '_np')[row, 3] = 0
                    self.__getattribute__(el + '_np')[row, 7] = 0
                    self.__getattribute__(el + '_np')[row, 0] = 0
                    self.__getattribute__(el + '_np')[row, 4] = 0

        else:                               # per i nodi e per il Source
            self.dss.circuit.set_active_bus(el)
            v[el]['lf']['v'].append(self.dss.cktelement.voltages_mag_ang[0] * 3 ** 0.5)
    # TODO: verificare se è possibile rendere self.results_append e self.results_store come un'unica funzione

    def results_store_np_chatGPT(self, el, row):
        sqrt3 = 3 ** 0.5  # Precompute sqrt(3)
        el_np = self.__getattribute__(el + '_np')  # Cache access to the numpy array

        if v[el]['category'] != 'Node':  # For all elements except Nodes
            if not v[el]['par']['out-of-service']:  # If the element is in service
                mcat = mcat_find(el)
                cf0, cf1 = 1, 1  # Correction factor for AC parts

                if v[el]['category'] in DC_elem:
                    cf0 = sqrt3  # Correction factor for DC portions upstream
                if v[el]['category'] in DC_elem + ['PWM']:
                    cf1 = sqrt3  # Correction factor for DC portions downstream

                self.dss.circuit.set_active_element(mcat + '.' + el)  # Activate the element


                if v[el]['category'] not in mc['Line'] + mc['Transformer']:  # For terminal elements
                    powers = self.dss.cktelement.powers  # Cache access to powers

                    p = sum(powers[2 * i] for i in range(3))  # Sum powers for p
                    q = sum(powers[2 * i + 1] for i in range(3))  # Sum powers for q

                    # Update numpy array with P, Q, V, I values
                    el_np[row, 1] = p
                    el_np[row, 2] = q
                    el_np[row, 3] = self.dss.cktelement.voltages_mag_ang[0] * sqrt3
                    el_np[row, 0] = self.dss.cktelement.currents_mag_ang[0] * cf0

                else:  # For lines or transformers
                    j = 6 if v[el]['category'] in mc['Line'] else 8  # Set offset for line/transformer

                    powers = self.dss.cktelement.powers  # Cache access to powers

                    # Calculate power for each side
                    p0 = sum(powers[2 * i] for i in range(3))
                    q0 = sum(powers[2 * i + 1] for i in range(3))
                    p1 = sum(-powers[2 * i + j] for i in range(3))
                    q1 = sum(-powers[2 * i + j + 1] for i in range(3))

                    # Update numpy array with side-specific values
                    el_np[row, 1] = p0
                    el_np[row, 2] = q0
                    el_np[row, 5] = p1
                    el_np[row, 6] = q1
                    el_np[row, 3] = self.dss.cktelement.voltages_mag_ang[0] * sqrt3
                    el_np[row, 7] = self.dss.cktelement.voltages_mag_ang[j] * sqrt3
                    el_np[row, 0] = self.dss.cktelement.currents_mag_ang[0] * cf0
                    el_np[row, 4] = self.dss.cktelement.currents_mag_ang[j] * cf1

            else:  # If the element is not in service
                # Set all relevant numpy array values to 0 for non-service elements
                if v[el]['category'] not in mc['Line'] + mc['Transformer']:  # For terminal elements
                    el_np[row, 1:4] = 0
                    el_np[row, 0] = 0
                else:  # For lines and transformers
                    el_np[row, [1, 2, 5, 6, 3, 7, 0, 4]] = 0

        else:  # For nodes and sources
            self.dss.circuit.set_active_bus(el)
            v[el]['lf']['v'].append(self.dss.cktelement.voltages_mag_ang[0] * sqrt3)
    # TODO: verificare se è possibile rendere self.results_append e self.results_store come un'unica funzione

    def results_store_np_chatGPT_nodata(self, el, row):
        sqrt3 = 3 ** 0.5  # Precompute sqrt(3)
        el_np = self.__getattribute__(el + '_np')  # Cache access to the numpy array

        el_np[row, 1] = 1
        el_np[row, 2] = 2
        el_np[row, 5] = 3
        el_np[row, 6] = 4
        el_np[row, 3] = 5
        el_np[row, 7] = 6
        el_np[row, 0] = 7
        el_np[row, 4] = 8

    # TODO: verificare se è possibile rendere self.results_append e self.results_store come un'unica funzione


    def results_store_csv(self, el, row):
        if v[el]['category'] != 'Node':     # per tutti gli elementi tranne che per i Nodi

            if not v[el]['par']['out-of-service']:  # Se l'elemento è in servizio
                mcat = mcat_find(el)

                # Le parti DC sono in pratica porzioni AC, di cui si considera la fase globale.
                # Per questo, per la corrente bisogna usare un fattore di correzione "cf"
                cf0, cf1 = 1, 1     # fattore di correzione per le parti AC
                if v[el]['category'] in DC_elem:
                    cf0 = 3 ** 0.5    # fattore di correzione per le porzioni DC a monte
                if v[el]['category'] in DC_elem + ['PWM']:
                    cf1 = 3 ** 0.5  # fattore di correzione per pe porzioni DC a valle

                self.dss.circuit.set_active_element(mcat + '.' + el)    # l'elemento è selezionato

                if v[el]['category'] not in mc['Line'] + mc['Transformer']:     # per gli elemnenti terminali

                    # le potenza globali sono date dalla somma delle potenze delle singole fasi
                    p, q = 0, 0
                    for i in range(0, 3):
                        p = p + self.dss.cktelement.powers[2 * i]
                        q = q + self.dss.cktelement.powers[2 * i + 1]

                    x = ['i0', 'p0', 'q0', 'v0', 'i1', 'p1', 'q1', 'v1']
                    # Accodamento nel vettore dei risultati nel dizionario
                    # dei valori di P, Q, V, i con i relativi fattori di correzione
                    p0 = p
                    q0 = q
                    v0 = self.dss.cktelement.voltages_mag_ang[0] * 3**0.5
                    i0 = self.dss.cktelement.currents_mag_ang[0] * cf0

                    p1, q1, v1, i1 = 0, 0, 0, 0

                else:                           # per le linee
                    if v[el]['category'] in mc['Line']:     # per le linee
                        j = 6
                    else:                                   # per i Transformer
                        j = 8

                    # le potenza globali sono date dalla somma delle potenze delle singole fasi
                    p0, q0, p1, q1 = 0, 0, 0, 0
                    for i in range(0, 3):
                        p0 = p0 + self.dss.cktelement.powers[2 * i]
                        q0 = q0 + self.dss.cktelement.powers[2 * i + 1]
                        p1 = p1 - self.dss.cktelement.powers[2 * i + j]
                        q1 = q1 - self.dss.cktelement.powers[2 * i + j + 1]

                    # Inserimento nel dizionario, per ogni lato,
                    # dei valori di P, Q, V, i con i relativi fattori di correzione
                    # self.__getattribute__(el + '_np')[row, 1] = p0
                    # self.__getattribute__(el + '_np')[row, 2] = q0
                    # self.__getattribute__(el + '_np')[row, 5] = p1
                    # self.__getattribute__(el + '_np')[row, 6] = q1
                    v0 = self.dss.cktelement.voltages_mag_ang[0] * 3**0.5
                    v1 = self.dss.cktelement.voltages_mag_ang[j] * 3**0.5
                    i0 = self.dss.cktelement.currents_mag_ang[0] * cf0
                    i1 = self.dss.cktelement.currents_mag_ang[j] * cf1

            else:                                   # se l'elemento non è in servizio
                p0, q0, v0, i0, p1, q1, v1, i1 = 0, 0, 0, 0, 0, 0, 0, 0

            self.__getattribute__(el + 'csv_writer').writerow([i0, p0, q0, v0, i1, p1, q1, v1])

        else:                               # per i nodi e per il Source
            self.dss.circuit.set_active_bus(el)
            v[el]['lf']['v'].append(self.dss.cktelement.voltages_mag_ang[0] * 3 ** 0.5)
    # TODO: verificare se è possibile rendere self.results_append e self.results_store come un'unica funzione



    # Test storing con Pandas
    def results_store_arr(self, el, row):
        if v[el]['category'] != 'Node':     # per tutti gli elementi tranne che per i Nodi

            if not v[el]['par']['out-of-service']:  # Se l'elemento è in servizio
                mcat = mcat_find(el)

                # Le parti DC sono in pratica porzioni AC, di cui si considera la fase globale.
                # Per questo, per la corrente bisogna usare un fattore di correzione "cf"
                cf0, cf1 = 1, 1     # fattore di correzione per le parti AC
                if v[el]['category'] in DC_elem:
                    cf0 = 3 ** 0.5    # fattore di correzione per le porzioni DC a monte
                if v[el]['category'] in DC_elem + ['PWM']:
                    cf1 = 3 ** 0.5  # fattore di correzione per pe porzioni DC a valle

                self.dss.circuit.set_active_element(mcat + '.' + el)    # l'elemento è selezionato

                if v[el]['category'] not in mc['Line'] + mc['Transformer']:     # per gli elemnenti terminali

                    # le potenza globali sono date dalla somma delle potenze delle singole fasi
                    p, q = 0, 0
                    for i in range(0, 3):
                        p = p + self.dss.cktelement.powers[2 * i]
                        q = q + self.dss.cktelement.powers[2 * i + 1]

                    # Accodamento nel vettore dei risultati nel dizionario
                    # dei valori di P, Q, V, i con i relativi fattori di correzione
                    self.__getattribute__(el + '_p0').append(p)
                    self.__getattribute__(el + '_q0').append(q)
                    self.__getattribute__(el + '_v0').append(self.dss.cktelement.voltages_mag_ang[0] * 3**0.5)
                    self.__getattribute__(el + '_i0').append(self.dss.cktelement.currents_mag_ang[0] * cf0)

                else:                           # per le linee
                    if v[el]['category'] in mc['Line']:     # per le linee
                        j = 6
                    else:                                   # per i Transformer
                        j = 8

                    # le potenza globali sono date dalla somma delle potenze delle singole fasi
                    p0, q0, p1, q1 = 0, 0, 0, 0
                    for i in range(0, 3):
                        p0 = p0 + self.dss.cktelement.powers[2 * i]
                        q0 = q0 + self.dss.cktelement.powers[2 * i + 1]
                        p1 = p1 - self.dss.cktelement.powers[2 * i + j]
                        q1 = q1 - self.dss.cktelement.powers[2 * i + j + 1]

                    # Inserimento nel dizionario, per ogni lato,
                    # dei valori di P, Q, V, i con i relativi fattori di correzione
                    self.__getattribute__(el + '_p0').append(p0)
                    self.__getattribute__(el + '_q0').append(q0)
                    self.__getattribute__(el + '_p1').append(p1)
                    self.__getattribute__(el + '_q1').append(q1)
                    self.__getattribute__(el + '_v0').append(self.dss.cktelement.voltages_mag_ang[0] * 3**0.5)
                    self.__getattribute__(el + '_v1').append(self.dss.cktelement.voltages_mag_ang[j] * 3**0.5)
                    self.__getattribute__(el + '_i0').append(self.dss.cktelement.currents_mag_ang[0] * cf0)
                    self.__getattribute__(el + '_i1').append(self.dss.cktelement.currents_mag_ang[j] * cf1)

            else:                                   # se l'elemento non è in servizio
                if v[el]['category'] not in mc['Line'] + mc['Transformer']:     # per gli elemnenti terminali
                    self.__getattribute__(el + '_p0').append(0)
                    self.__getattribute__(el + '_q0').append(0)
                    self.__getattribute__(el + '_v0').append(0)
                    self.__getattribute__(el + '_i0').append(0)
                else:                                                           # per linee e trasformatori
                    self.__getattribute__(el + '_p0').append(0)
                    self.__getattribute__(el + '_q0').append(0)
                    self.__getattribute__(el + '_p1').append(0)
                    self.__getattribute__(el + '_q1').append(0)
                    self.__getattribute__(el + '_v0').append(0)
                    self.__getattribute__(el + '_v1').append(0)
                    self.__getattribute__(el + '_i0').append(0)
                    self.__getattribute__(el + '_i1').append(0)

        else:                               # per i nodi e per il Source
            self.dss.circuit.set_active_bus(el)
            v[el]['lf']['v'].append(self.dss.cktelement.voltages_mag_ang[0] * 3 ** 0.5)
    # TODO: verificare se è possibile rendere self.results_append e self.results_store come un'unica funzione

    # Esecuzione del loadflow puntuale. Restituisce un Booleano che indica se il sistema va a convegenza.
    # TODO: Forse non più necessario, sostituito da "self.full_parse_to_dss". Almeno da riconfigurare
    def solve(self):
        try:
            self.dss.topology.all_isolated_branches.clear()     # TODO: capire se necessario
            self.dss.solution.clean_up()
        except:
            pass

        self.dss.solution.solve()       # richiesta di risoluzione del sistema
        grid['studies']['lf'] = True

        for el in v:
            if v[el]['category'] in mc['Load']:
                self.dss.circuit.set_active_element('load.' + el)

                # print(el, self.dss.cktelement.powers)


        self.dss.text(f"Save Circuit dir=cartella")

        # self.results_store_all()

        return bool(self.dss.solution.converged)

    # scrittura dei risultati nel dizionario per ogni elemento
    def results_store_all(self):
        # print('store all')
        for el in v.keys():
            self.results_store(el)

    def test(self):
        pass

    # Lettura dei parametri dell'elemento el mediante analisi del testo del codice
    def readline(self, el):
        mcat = mcat_find(el)
        cat = v[el]['category']

        par = dict()
        if cat in new_par_dict:
            # -- creo l'elenco delle voci da ricercare nella stringa di codice DSS --------
            params = []     # Elenco delle voci da ricercare
            for p in (new_par_dict[cat]['par'].keys() - ['others']):
                params.append(new_par_dict[cat]['par'][p]['label'])
            for p in new_par_dict[cat]['top'].keys():
                params = params + new_par_dict[cat]['top'][p]['label']
            # -----------------------------------------------------------------------------
            file = open(mainpath + '/cartella/' + mcat + '.dss', 'r')
            # file = open(mainpath + '/cartella/' + mcat + '.dss', 'r')

            # -- ricerca dei parametri dell'elemento selezionato -----------------------------------------------------
            while True:
                line = file.readline()
                if line == '':  # se la linea è una linea vuota, allora il file è finito TODO: è vero????
                    break

                # Il nome dell'elemento è riportato tra due "" (e.g. New "Load.ug_dc-load" bus1=ug_dc-bb...).
                # Quindi il nome sarà la seconda voce dell'array derivato dalla stringa divisa per l'elemento '"'.
                elements = line.split('"')
                if elements[1].lower() == (mcat + '.' + el).lower():
                    line = line.replace('New "' + mcat + '.' + el.lower() + '" ', '').replace('\n', '')
                    line = line.replace(', ', ',')  # elimino lo spazio dopo le virgole
                    datas = line.split(' ')     # Array delle propietà: e.g. [proprietà=valore, ...]

                    # procedura di estrazione delle singole proprietà
                    for d_comp in datas:
                        d = d_comp.split('=')   # d = [proprietà, valore]
                        if d[0] in params:      # considreo le sole propietà elencate in params
                            if d[1][0] == '[':      # se il valore è un insieme di valori tra [], lo scrivo come array
                                val = []
                                d[1] = d[1].replace('[', '').replace(']', '')
                                for single in d[1].split(','):
                                    if single:
                                        try:            # converto il valore in formato decimale, se possibile
                                            Decimal(single)
                                            single = float(single)
                                        except InvalidOperation:
                                            pass
                                        val.append(single)
                            else:
                                try:
                                    Decimal(d[1])
                                    val = float(d[1])
                                except InvalidOperation:
                                    val = d[1]
                            par[d[0]] = val     # scrittura del valore ottenuto nel dizionario "par"
                            # TODO: perché mi memorizzo tutti i parametri, anche quello che non sono in params???
                    break

            # le tensioni degli elementi devono essere scritte come array, anche se sono singole
            if mcat == 'Generator':
                par['kv'] = [par['kv']]
            elif mcat == 'Load':
                # print(el)
                par['kV'] = [par['kV']]
            elif mcat == 'Vsource':
                par['basekv'] = [par['basekv']]
        return par


def mcat_find(el):
    mcat = ''
    for m in mc.keys():
        if v[el]['category'] in mc[m]:
            mcat = m
            break
    return mcat


# # Inizializzazione dei sottodizionari per l'elemento "el"
# def dict_initialize(el):
#     v[el] = dict()
#     for sub in ['top', 'par', 'lf', 'rel']:
#         v[el][sub] = dict()
#     v[el]['top']['conn'] = []
#
#
# # Inizializzazione del sottodizionario rella Reliability ("rel") per l'elemento "el"
# def rel_initialize(el):
#     v[el]['rel']['par'] = dict()
#     for p in ['Pi_E', 'Pi_Q', 'alfa', 'beta']:
#         v[el]['rel']['par'][p] = None
#
#     v[el]['rel']['results'] = dict()
#     if v[el]['category'] in mc['Load']:
#         v[el]['rel']['results']['load_rel'] = None
#     for p in ['lambda', 'MTBF_ore', 'MTBF_anni', 'Pi_Si']:
#         v[el]['rel']['results'][p] = None
#
#
# # Inizializzazione del sottodizionario del loadFLow ("lf") per l'elemento "el"
# def lf_initialize(el):
#     params = ['i', 'v', 'p', 'q']
#
#     if v[el]['category'] in mc['Transformer'] + mc['Line']:
#         for p in params:
#             v[el]['lf'][p] = dict()
#             v[el]['lf'][p][0] = []
#             v[el]['lf'][p][1] = []
#     else:
#         for p in params:
#             v[el]['lf'][p] = []


# importazione del profill caratteristico di carichi e generatori
def create_profile(el):
    v[el]['par']['profile'] = dict()
    # inizialmente si ipotizza l'assenza di profilo, con fattore di scala unitario
    v[el]['par']['profile']['name'] = None
    v[el]['par']['profile']['curve'] = 1

    # definizione del profilo da caricare
    profile = None      # Nome del profilo da caricare
    if v[el]['category'] == 'AC-Load':
        profile = 'AC-Load'
    elif v[el]['category'] == 'DC-Load':
        profile = 'DC-Load'
    elif v[el]['category'] in ['AC-Wind', 'DC-Wind']:
        profile = 'Wind'
    elif v[el]['category'] in ['AC-PV', 'DC-PV']:
        profile = 'PV'

    if profile:     # se l'elemento prevede il profilo viene importato dal relativo file
        filename = mainpath + '/_benchmark/_data/_profiles/' + profile + '.yml'
        d = yaml.safe_load(open(filename))

        # viene memorizzato nel dizionario
        v[el]['par']['profile']['name'] = d['name']
        v[el]['par']['profile']['curve'] = d['profile']
    # else:
    #     v[el]['par']['profile']['name'] = None
    #     v[el]['par']['profile']['curve'] = 1


# OpenDSS()
