import copy

import py_dss_interface
from variables import *
import yaml
import os
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
        self.dss.text(f"Save Circuit dir=cartella")     # scrittura della cartella degli elementi

        # Dato il nome dell'elemento (e.g. "transformer.WPG_TR"), vengono definite:
        # - le categorie dal suffisso del nome dell'elemento, dopo l'ultimo "_" (e.g. "TR")
        # - le macrocategorie (viene definito in DSS la paete prima del punto (e.g. "transformer")
        # - il nome dell'elemento (in DSS è la parte dopo il punto e.g. "WPG_TR")
        for item in self.dss.circuit.elements_names:
            [tag, el] = item.split('.')
            if tag == 'Vsource':
                cat = 'ExternalGrid'
            else:
                des = item.split('_')[len(item.split('_')) - 1].lower()
                if des in dsstag[tag.lower()]:
                    cat = dsstag[tag.lower()][des]
                else:
                    cat = dsstag[tag.lower()]['default']
                # cat = c[item.split('_')[len(item.split('_')) - 1]]

            # viene inizializzato il sotto-dizionario dell'elemento
            dict_initialize(el, cat)
            # dict_initialize(el)
            # print(el, cat)
            # v[el]['category'] = c[cat]  # la nomenclatira esatta della categoria deriva dal dizonario "variables.c"
            # rel_initialize(el)     # Todo: forse va spostato in self.dict_initialize
            # lf_initialize(el)      # Todo: forse va spostato in self.dict_initialize

            # self.read(el)           # vengono letti i parametri e la topologia dell'elemento
            self.read_new(el)       # lettura di parametri e topologia degli elementi dalla cartella degli elementi
        self.node_solve()           # risoluzione delle tensioni dei nodi non definiti

        # In OpenDSS non è possibile ricavare la tensione delle busbar non sottese a trasformatori,
        # o non connesse a elementi terminali.
        # La funzione self.node_define serve a definire le tensioni HV dei trasformatori delle busbar a monte di essi
        # self.node_define()    # TODO: Probabilmente deve essere riattivata
        # print('none')
        # self.save()

    # def save(self):
    #     with open('CityArea.yml', 'w') as file:
    #         yaml.dump(v, file)
    #         file.close()
    #     # print('end')

    def read_new(self, el):
        mcat = mcat_find(el)
        cat = v[el]['category']

        if mcat not in mc['Node']:
            self.dss.circuit.set_active_element(mcat + '.' + el)  # viene richiamato l'elemento in OpenDSS
            v[el]['par']['out-of-service'] = not self.dss.cktelement.is_enabled  # verifica se l'elemento è "enabled"

            # lettura dei parametri dalle righe di dss
            par = self.readline(el)     # TODO: vedi commento in self.readline

            for p in new_par_dict[cat]['par'].keys() - ['others', 'linecode']:  # todo: forse da modificare in base al TODO precedente
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
            # print('done')

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
                        # print( new_par_dict[linecat]['par'][p]['label'])
                        v[el]['par'][p] = par[new_par_dict[linecat]['par'][p]['label']]
                    v.pop(linetype)                     # Non serve più

        # Imposto inizlalmente il profilo puntuale per carichi e generatori
        if cat in mc['Load'] + mc['Generator']:
            create_profile(el)
            if cat in mc['Generator']:
                v[el]['par']['eff'] = 1
                if cat == 'BESS':   # Si ipotizza che la capacità delle batterie sia inizalmente 0
                    v[el]['par']['cap'] = 0

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
    def writeline(self, el):
        mcat = mcat_find(el)
        cat = v[el]['category']

        par = ''
        buses = ''
        # line = ''
        serv = ''

        # Scrittura della parte dei parametri
        for p in new_par_dict[cat]['par']['others']:
            par = par + p + '=' + new_par_dict[cat]['par']['others'][p] + ' '
        for p in new_par_dict[cat]['par'].keys() - ['others']:
            if p == 'Vn' and mcat != 'Transformer':     # La tensione è memorizzata come array anche se è singola
                par = par + new_par_dict[cat]['par'][p]['label'] + '=' + str(v[el]['par'][p][0]) + ' '
            else:
                par = par + new_par_dict[cat]['par'][p]['label'] + '=' + str(v[el]['par'][p]) + ' '

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
            # buses = buses.replace("'", "")
        # print(new_par_dict[cat]['top']['conn']['label'])
        # print(v[el]['top']['conn'])

        if mcat == 'Vsource':
            line = 'Edit "Vsource.' + el + ' '
        else:
            line = 'New "' + mcat + '.' + el + '" '

        # Nel caso delle linee, bisogna definire anche il LineType
        line0 = ''
        if 'type' in new_par_dict[cat]['top'].keys():
            print(el)
            line = line + 'linecode=' + v[el]['top']['linetype'] + ' '

            linetype = cat.split('-')[0] + '-LineCode'
            for p in new_par_dict[linetype]['par']['others']:
                line0 = line0 + p + '=' + new_par_dict[linetype]['par']['others'][p] + ' '

            for p in new_par_dict[linetype]['par'].keys() - ['others']:
                line0 = line0 + new_par_dict[linetype]['par'][p]['label'] + '=' + str(v[el]['par'][p]) + ' '

            line0 = 'New "LineCode.' + v[el]['top']['linetype'] + '" ' + line0
            dss_cat['LineCode'].append(line0)   # Memorizzazione del LineType
            # print(line0)

            line = line + 'linecode=' + v[el]['top']['linetype'] + ' '

        line = line + buses + par + serv

        dss_cat[mcat].append(line)              # Memorizzazione dell'elemento

        # print(line)
        return line     # TODO: Perchè?

    # Scrittura di tutti gli elementi in OpenDSS
    def full_parse_to_dss(self):
        # # self.dss.dssinterface.clear_all()
        # self.dss.text('Clear')
        #
        # # self.dss.solution.solve()
        # self.dss.text('New object=circuit.dss_grid basekv=' + str(v['source']['par']['Vn'][0]))

        self.dss.text('Clear')
        self.dss.text('New object=circuit.dss_grid basekv=' + str(v['source']['par']['Vn'][0])
                      + ' bus1=' + str(v['source']['top']['conn'][0]))
        # self.dss.text(f"Save Circuit dir=cartella")

        # Popolamento dei comandi pero ogni macrocategoria di OpenDSS
        for key in dss_cat.keys():
            dss_cat[key] = []

        open('lista.txt', 'w').close()
        f = open('lista.txt', 'a')
        for el in v:
            mcat = mcat_find(el)
            if mcat in dss_cat:
                f.write(self.writeline(el) + '\n')
        f.close()

        # Scrittura dei comandi in OpenDSS
        print('scrittura')
        for mcat in dss_cat:
            # print('\n' + mcat)
            for r in dss_cat[mcat]:
                self.dss.text(r)
                # print(r)

        self.solve()
        # self.save()

        self.dss.text(f"Save Circuit dir=cartella")

        # print(list(self.dss.loads.))
        # for el in self.dss.loads.names:
        #     self.dss.loads.name = el
        #     print(el + ': ', self.dss.loads.kw)

    #  TODO: Procedura da dismettere
    # def read(self, el):
    #     mcat = mcat_find(el)
    #     v1 = None   # indica la tensione a cui sono connessi i terminali, o la tensione di bassa dei trasformatori
    #     #
    #     # # Viene identificata la macrocategoria a partire dal dizionario "variables.mc"
    #     # for m in mc.keys():
    #     #     if v[el]['category'] in mc[m]:
    #     #         mcat = m
    #     #         break
    #
    #     self.dss.circuit.set_active_element(mcat + '.' + el)    # viene richiamato l'elemento in OpenDSS
    #
    #     v[el]['par']['out-of-service'] = not self.dss.cktelement.is_enabled     # verifica se l'elemento è "enabled"
    #
    #     if mcat == 'Vsource':
    #         v[el]['par']['Vn'] = self.dss.vsources.base_kv
    #
    #     elif mcat == 'Generator':
    #         self.dss.generators.name = el
    #         v1 = self.dss.generators.kv
    #
    #         # Caratteristiche globali degli elementi nella macrocategoria "Generator"
    #         v[el]['par']['P'] = self.dss.generators.kw
    #         v[el]['par']['Vn'] = self.dss.generators.kv
    #
    #         if v[el]['category'] == 'PV':
    #             create_profile(el)
    #
    #         elif v[el]['category'] == 'BESS':   # inizialmente, si ipotizzano i valori per gli elementi BESS
    #             v[el]['par']['cap'] = 100
    #             v[el]['par']['eff'] = 1
    #             create_profile(el)
    #
    #         elif v[el]['category'] == 'AC-Wind':
    #             v[el]['par']['Q'] = self.dss.generators.kvar
    #             v[el]['par']['cosPhi'] = self.dss.generators.pf
    #             v[el]['par']['eff'] = 1
    #             create_profile(el)
    #
    #         elif v[el]['category'] == 'DC-Wind':
    #             v[el]['par']['eff'] = 1
    #             create_profile(el)
    #
    #     elif mcat == 'Transformer':
    #         self.unr_conv.append(el)
    #         self.dss.transformers.name = el
    #         v1 = self.dss.transformers.kv
    #
    #         # Caratteristiche globali degli elementi nella macrocategoria "Transformer"
    #         v[el]['par']['Vn1'] = self.dss.transformers.kv
    #         v[el]['par']['Sr'] = self.dss.transformers.kva
    #         v[el]['par']['XHL'] = self.dss.transformers.xhl
    #         v[el]['par']['Rs'] = self.dss.transformers.r
    #         # v[el]['par']['imag'] = self.dss.cktelement.losses
    #
    #     elif mcat == 'Load':
    #         self.dss.loads.name = el
    #         v1 = self.dss.loads.kv
    #
    #         # Caratteristiche globali degli elementi nella macrocategoria "Load"
    #         v[el]['par']['P'] = self.dss.loads.kw
    #         v[el]['par']['Vn'] = self.dss.loads.kv
    #         create_profile(el)
    #
    #         if v[el]['category'] == 'AC-Load':
    #             v[el]['par']['Q'] = self.dss.loads.kvar
    #             v[el]['par']['cosPhi'] = self.dss.loads.pf
    #
    #     elif mcat == 'Line':
    #         self.unr_lines.append(el)
    #         self.dss.lines.name = el
    #
    #         # Caratteristiche globali degli elementi nella macrocategoria "Line"
    #         v[el]['par']['length'] = self.dss.lines.length
    #         v[el]['par']['R1'] = self.dss.lines.r1
    #         v[el]['par']['X1'] = self.dss.lines.x1
    #         v[el]['par']['In'] = self.dss.lines.norm_amps
    #
    #         if v[el]['category'] == 'AC-Line':
    #             v[el]['par']['R0'] = self.dss.lines.r0
    #             v[el]['par']['X0'] = self.dss.lines.x0
    #             v[el]['par']['C0'] = self.dss.lines.c0
    #             v[el]['par']['C1'] = self.dss.lines.c1
    #
    #     nodes = self.dss.cktelement.bus_names   # Lista dei nodi a cui l'elemento è connesso
    #
    #     for node in nodes:
    #         if node not in v.keys():            # se il nodo non è stato già aggiunto al dizionario
    #             dict_initialize(node)      # viene inizializzato
    #             if node.split('_')[len(node.split('_')) - 1] in ['dc-node', 'dc-bb']:
    #                 v[node]['category'] = 'DC-Node'  # ""
    #             else:
    #                 v[node]['category'] = 'AC-Node'  # ""
    #             rel_initialize(node)       # ""
    #             lf_initialize(node)        # ""
    #             v[node]['par']['Vn'] = None     # ""
    #
    #         v[node]['top']['conn'].append(el)   # nella topologia del nodo, viene indicato che è connesso all'elemento
    #         v[el]['top']['conn'].append(node)   # nella topologia dell'elemento, viene indicato che è connesso al nodo
    #
    #         # il nodo viene impostato come "Enabled" di default
    #         self.dss.circuit.set_active_element(node)
    #         v[node]['par']['out-of-service'] = not self.dss.cktelement.is_enabled
    #
    #         # se è possibile leggere la tensione v1 dell'elemento
    #         # e l'elemento è terminale (esiste un solo nodo) o se ni tratta del secondo nodo di un convertitore...
    #         if v1 and (len(nodes) == 1 or nodes.index(node) == 1):
    #             v[node]['par']['Vn'] = v1   # ... Il nodo assume la tensione "v1"

    # TODO: non più usato
    # def node_define(self):
    #     # l'OpenDSS connette il "source" a monte con un nodo con desinenza ".0.0.0" (che si vuole eliminare)
    #     # e a valle con un nodo che deve avere la stessa tensione del source
    #     sourcebus = v['source']['top']['conn'][0]
    #     v['source']['top']['conn'] = [sourcebus]
    #     v[sourcebus]['par']['Vn'] = v['source']['par']['Vn']
    #     v.pop(sourcebus + '.0.0.0')
    #
    #     # Questo ciclo deve definire le tensioni degli elementi di conversione e di linea non risolti,
    #     # verificando la tensione delle busbar a partire dal feeder in poi.
    #     # Si ripete questo ciclo finché ci sono convertitori e nodi non risolti
    #     while self.unr_conv + self.unr_lines != []:
    #         for el in self.unr_conv:
    #             if v[el]['top']['conn'][0] in v.keys():             # se il nodo a monte dell'elemento è nel dizionario
    #                 bus = v[el]['top']['conn'][0]
    #                 if v[bus]['par']['Vn']:                         # e se ne è stata identificata la tensione
    #                     v[el]['par']['Vn0'] = v[bus]['par']['Vn']   # tale valore è la tensione a monte del converitore
    #                     self.unr_conv.remove(el)                    # il convertitore è risolto: si elimina dalla lista
    #
    #         for el in self.unr_lines:
    #             vn = None       # tensione di linea (e dei nodi a essa connessi)
    #             bus2 = None     # bus a monte o a valle della linea
    #             if v[el]['top']['conn'][0] in v.keys():             # se il nodo a monte della linea è nel dizionario
    #                 bus = v[el]['top']['conn'][0]
    #                 if v[bus]['par']['Vn']:                         # e se ne è stata identificata la tensione
    #                     vn = v[bus]['par']['Vn']                    # la tensione di linea è pari a tale valore
    #                     bus2 = v[el]['top']['conn'][1]              # bus2 sarà il nodo a valle
    #
    #             elif v[el]['top']['conn'][1] in v.keys():           # se il nodo a valle della linea è nel dizionario
    #                 bus = v[el]['top']['conn'][1]
    #                 if v[bus]['par']['Vn']:                         # e se ne è stata identificata la tensione
    #                     vn = v[bus]['par']['Vn']                    # la tensione di linea è pari a tale valore
    #                     bus2 = v[el]['top']['conn'][0]              # bus2 sarà il nodo a valle
    #
    #             if vn:                                              # se è stato possibile valutarela tensione di linea
    #                 v[el]['par']['Vn'] = vn                         # si inserisce nel sotto-dizionario della linea
    #                 v[bus2]['par']['Vn'] = vn                       # si inserisce nel sotto-dizionario del nodo "bus2"
    #                 self.unr_lines.remove(el)                       # la linea è risolta: si elimina dalla lista

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

    # Aggiornamento del dizionario con i profili dei risultati di uno studio temporale. TODO Ridefinire
    def results_append(self, el):
        if v[el]['category'] != 'Node':     # per tutti gli elementi tranne che per i Nodi
            # mcat = ''
            # for m in mc.keys():
            #     if v[el]['category'] in mc[m]:
            #         mcat = m
            #         break
            mcat = mcat_find(el)

            # Le parti DC sono in pratica porzioni AC, di cui si considera la fase globale.
            # Per questo, per la corrente bisogna usare un fattore di correzione "cf"
            cf0, cf1 = 1, 1     # fattore di correzione per le parti AC
            if v[el]['category'] in ['DC-Line', 'DC-DC-Converter', 'DC-Load', 'BESS', 'PV', 'DC-Wind']:
                cf0 = 3**0.5    # fattore di correzione per le porzioni DC a monte
            if v[el]['category'] in ['DC-Line', 'DC-DC-Converter', 'DC-Load', 'BESS', 'PV', 'DC-Wind', 'PWM']:
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

                # Accodamento nel vettore dei risultati nel dizionario, per ogni lato,
                # dei valori di P, Q, V, i con i relativi fattori di correzione
                v[el]['lf']['p'][0].append(p0)
                v[el]['lf']['q'][0].append(q0)
                v[el]['lf']['p'][1].append(p1)
                v[el]['lf']['q'][1].append(q1)
                v[el]['lf']['v'][0].append(self.dss.cktelement.voltages_mag_ang[0] * 3**0.5)
                v[el]['lf']['v'][1].append(self.dss.cktelement.voltages_mag_ang[j] * 3**0.5)
                v[el]['lf']['i'][0].append(self.dss.cktelement.currents_mag_ang[0] * cf0)
                v[el]['lf']['i'][1].append(self.dss.cktelement.currents_mag_ang[j] * cf1)

        else:                               # per i nodi
            self.dss.circuit.set_active_bus(el)
            v[el]['lf']['v'].append(self.dss.cktelement.voltages_mag_ang[0] * 3 ** 0.5)

    # Aggiornamento del dizionario dei risultati di uno studio singolo. TODO: Ridefinire
    def results_store(self, el):
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
                if v[el]['category'] in ['DC-Line', 'DC-DC-Converter', 'DC-Load', 'BESS', 'PV', 'DC-Wind']:
                    cf0 = 3 ** 0.5    # fattore di correzione per le porzioni DC a monte
                if v[el]['category'] in ['DC-Line', 'DC-DC-Converter', 'DC-Load', 'BESS', 'PV', 'DC-Wind', 'PWM']:
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
                    v[el]['lf']['p'] = p
                    v[el]['lf']['q'] = q
                    v[el]['lf']['v'] = self.dss.cktelement.voltages_mag_ang[0] * 3**0.5
                    v[el]['lf']['i'] = self.dss.cktelement.currents_mag_ang[0] * cf0

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
                    v[el]['lf']['p'][0] = p0
                    v[el]['lf']['q'][0] = q0
                    v[el]['lf']['p'][1] = p1
                    v[el]['lf']['q'][1] = q1
                    v[el]['lf']['v'][0] = self.dss.cktelement.voltages_mag_ang[0] * 3**0.5
                    v[el]['lf']['v'][1] = self.dss.cktelement.voltages_mag_ang[j] * 3**0.5
                    v[el]['lf']['i'][0] = self.dss.cktelement.currents_mag_ang[0] * cf0
                    v[el]['lf']['i'][1] = self.dss.cktelement.currents_mag_ang[j] * cf1

            else:                                   # se l'elemento non è in servizio
                if v[el]['category'] not in mc['Line'] + mc['Transformer']:     # per gli elemnenti terminali
                    v[el]['lf']['p'] = 0
                    v[el]['lf']['q'] = 0
                    v[el]['lf']['v'] = 0
                    v[el]['lf']['i'] = 0
                else:                                                           # per linee e trasformatori
                    v[el]['lf']['p'][0] = 0
                    v[el]['lf']['q'][0] = 0
                    v[el]['lf']['p'][1] = 0
                    v[el]['lf']['q'][1] = 0
                    v[el]['lf']['v'][0] = 0
                    v[el]['lf']['v'][1] = 0
                    v[el]['lf']['i'][0] = 0
                    v[el]['lf']['i'][1] = 0

        else:                               # per i nodi e per il Source
            self.dss.circuit.set_active_bus(el)
            v[el]['lf']['v'] = self.dss.cktelement.voltages_mag_ang[0] * 3 ** 0.5
    # TODO: verificare se è possibile rendere self.results_append e self.results_store come un'unica funzione

    # Esecuzione del loadflow puntuale. Restituisce un Booleano che indica se il sistema va a convegenza.
    # TODO: Forse non più necessario, sostituito da "self.full_parse_to_dss". Almeno da riconfigurare
    def solve(self):
        try:
            self.dss.topology.all_isolated_branches.clear()     # TODO: capire se necessario
            self.dss.solution.clean_up()
            # print(self.dss.topology.all_isolated_loads)
            # print('clear done')
        except:
            print('clear error')
            pass

        self.dss.solution.solve()       # richiesta di risoluzione del sistema
        fn['lf'] = True
        # print(self.dss.circuit.total_power)
        # print(bool(self.dss.solution.converged))
        self.dss.text(f"Save Circuit dir=cartella")

        # scrittura dei risultati nel dizionario per ogni elemento
        for el in v.keys():
            self.results_store(el)

        # # self.dss.circuit.set_active_element('line.EV-Charge_Line')
        # self.dss.circuit.set_active_element('transformer.UGS_PWM')
        # print(self.dss.cktelement.name)
        # print('N. terminals: ' + str(self.dss.cktelement.num_terminals))
        # print('Terminal opened: ' + str(bool(self.dss.cktelement.is_terminal_open)))
        # print(self.dss.cktelement.currents_mag_ang)
        # print(self.dss.cktelement.powers)
        #
        return bool(self.dss.solution.converged)

    # Esecuzione del loadFlow per un intervallo temporale di 24 ore TODO: ridefinire
    def solve_profile(self):
        for t in range(0, 96):  # viene ipotizzato un timestep di 15 minuti
            self.write_all(t/4)         # si aggiornano puntualmente i valori degli elementi in OpenDSS
            self.dss.solution.solve()   # richiesta di risoluzione del sistema

            # accodamento dei risultati nel dizionario degli elementi
            for el in v.keys():
                self.results_append(el)
        pass

    def test(self):
        # print(self.dss.topology.all_isolated_branches)
        # self.dss.text(f"show isolated")
        # print(self.dss.topology.active_branch)
        # print(self.dss.topology.all_isolated_loads)
        pass

    # def losses_calc(self):
    #     for el in v.keys():
    #         if v[el]['category'] in mc['Transformer']:
    #             self.dss.transformers.name = el
    #             self.dss.circuit.set_active_element('transformer.' + el)

    # def compile_element(self, el):
    #     mcat = mcat_find(el)
    #     if mcat == 'Vsource':
    #         text = 'New object=circuit.' + self.network_name + ' baekv=' + str(v[el]['par']['Vn'])
    #     elif mcat == 'Transformer':
    #         if v[el]['category'] == '2W-Transformer':
    #             Rs = 'Rs=[' + ''
    #
    #     pass

    # Lettura dei parametri dell'elemento el mediante analisi del testo del codice
    def readline(self, el):
        mcat = mcat_find(el)
        cat = v[el]['category']

        # if mcat == 'Line':
        #     print('Line')

        par = dict()
        # if mcat in ['Generator', 'Line', 'Load', 'Transformer', 'Vsource']:
        if cat in new_par_dict:
            # -- creo l'elenco delle voci da ricercare nella stringa di codice DSS --------
            params = []     # Elenco delle voci da ricercare
            for p in (new_par_dict[cat]['par'].keys() - ['others']):
                # print(p)
                params.append(new_par_dict[cat]['par'][p]['label'])
            for p in new_par_dict[cat]['top'].keys():
                params = params + new_par_dict[cat]['top'][p]['label']

            # params = (params + list(new_par_dict[cat]['par']['others'].keys()) +
            #           new_par_dict[cat]['top']['conn']['label'])

            # print('parametri:', params)
            # -----------------------------------------------------------------------------

            file = open('cartella/' + mcat + '.dss', 'r')

            # -- ricerca dei parametri dell'elemento selezionato -----------------------------------------------------
            while True:
                line = file.readline()
                if line == '':  # se la linea è una linea vuota, allora il file è finito TODO: è vero????
                    break

                # Il nome dell'elemento è riportato tra due "" (e.g. New "Load.ug_dc-load" bus1=ug_dc-bb...).
                # Quindi il nome sarà la seconda voce dell'array derivato dalla stringa divisa per l'elemento '"'.
                elements = line.split('"')
                if elements[1].lower() == (mcat + '.' + el).lower():
                    # print(line)
                    # la stringa di riferimento è data solo dalle proprietà dell'elemento
                    line = line.replace('New "' + mcat + '.' + el.lower() + '" ', '').replace('\n', '')
                    line = line.replace(', ', ',')  # elimino lo spazio dopo le virgole
                    # print('fatto', line)
                    datas = line.split(' ')     # Array delle propietà: e.g. [proprietà=valore, ...]
                    # print(datas)
                    # print('\n')

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
                            # print(d[0], val)
                            par[d[0]] = val     # scrittura del valore ottenuto nel dizionario "par"
                            # TODO: perché mi memorizzo tutti i parametri, anche quello che non sono in params???
                    break

            # le tensioni degli elementi devono essere scritte come array, anche se sono singole
            if mcat == 'Generator':
                par['kv'] = [par['kv']]
            elif mcat == 'Load':
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
    elif v[el]['category'] == 'PV':
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
