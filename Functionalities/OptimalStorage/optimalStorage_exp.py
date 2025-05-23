import math

try:
    from UI.ui_optimalStorage_wgt import *
except:
    from .UI.ui_optimalStorage_wgt import *

from PySide2 import QtGui, QtCore, QtWidgets

from PySide2.QtCharts import *


class OptStorWGT(QMainWindow):
    def __init__(self):
        super(OptStorWGT, self).__init__(None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.resultsWgt.setVisible(False)

        # Popolazione della tendina "Anno"
        self.ui.yearScenCb.clear()
        self.ui.yearScenCb.addItems(list(s.keys()))

        self.year_selected()    # azioni conseguenti alla selezione dell'anno
        self.scen_selected()    # azioni conseguenti alla selezione dello scenario

        # -- Azioni dei pulsanti e dei menu a tendina --------------------------------
        self.ui.yearScenCb.currentTextChanged.connect(self.year_selected)
        self.ui.scenCb.currentTextChanged.connect(self.scen_selected)
        self.ui.calcPb.clicked.connect(self.calculation)
        # ----------------------------------------------------------------------------

    # Calcolo dei risultati
    def calculation(self):
        # lettura dei dati di input e scrittura nelle variabili
        for p in ['electrLev', 'enConsGrow', 'ferGen', 'h2Cons', 'solarFer']:
            self.__setattr__(p + 'Input', self.ui.__getattribute__(p + 'InputDsb').value())

        self.ui.resultsWgt.setVisible(True)     # Rendo visibile il Widget dei risultati

        # -- Calcolo delle variabili dei risultati --------------------------------------------
        self.totEnConsMtep = self.totEnConsMtepScen * (1 + self.enConsGrowInput / 100) ** 8
        self.totEnCons = self.totEnConsMtep / 0.086
        self.h2Cons = self.h2ConsInput * self.totEnCons / 100
        self.enDuty = self.totEnCons * self.electrLevInput / 100
        self.enImport = 52
        self.enProd = self.enDuty - self.enImport
        self.ferGen = self.enProd * self.ferGenInput / 100
        self.ferGenPerc = self.ferGenInput
        self.solarGen = (self.ferGen - self.otherGenScen) * self.solarFerInput / 100
        self.windGen = (self.ferGen - self.otherGenScen) * (1 - self.solarFerInput / 100)
        self.otherGen = self.ferGen - self.solarGen - self.windGen
        self.solarCap = self.solarGen / 1.35
        self.windCap = self.windGen / 2.51
        self.otherCap = self.otherCapScen
        self.ferCap = self.solarCap + self.windCap + self.otherCap
        self.co2Emis = (self.enProd - self.ferGen) * 0.5
        self.co2EmisRed = self.co2EmisScen - self.co2Emis

        self.hiOvergen = (self.solarGen + self.windGen) * 0.05
        self.lowOvergen = (self.solarGen + self.windGen) * 0.027

        self.sysStor = self.sysStor_calc()  # calcolata con la funzione self.sysStor_calc

        self.maxHiH2 = self.lowOvergen * 0.7
        self.maxLowH2 = self.hiOvergen * 0.7
        self.toprodHiH2 = self.h2Cons - self.maxHiH2
        self.toprodLowH2 = self.h2Cons - self.maxLowH2

        self.frnpCosts = (800 * self.solarCap + 900 * self.windCap)
        self.capexCosts = 0
        self.h2Costs = 0
        # -------------------------------------------------------------------------------------

        # -- Calcolo delle variabili delle percentuali dei risultati --------------------------
        for c in ['Gen', 'Cap']:
            for p in ['solar', 'wind', 'other']:
                self.__setattr__(p + c + 'Perc',
                                 self.__getattribute__(p + c) / self.__getattribute__('fer' + c) * 100)
        # -------------------------------------------------------------------------------------

        # -- Scrittura dei risultati nelle caselle --------------------------------------------
        # --- Scrittura dei risultati presenti come scenario che come risultato -----------
        for p in ['totEnConsMtep', 'totEnCons', 'h2Cons', 'enDuty', 'enImport', 'enProd', 'ferGen', 'ferGenPerc',
                  'solarGen', 'solarGenPerc', 'windGen', 'windGenPerc', 'otherGen', 'otherGenPerc', 'ferCap',
                  'solarCap', 'solarCapPerc', 'windCap', 'windCapPerc', 'otherCap', 'otherCapPerc', 'co2Emis']:
            self.ui.__getattribute__(p + 'ResPerspDsb').setValue(self.__getattribute__(p))
            self.ui.__getattribute__(p + 'ResActDsb').setValue(self.__getattribute__(p + 'Scen'))
        # ---------------------------------------------------------------------------------

        # --- Scrittura dei risultati presenti solo come risultato ------------------------
        for p in ['co2EmisRed', 'hiOvergen', 'lowOvergen', 'sysStor', 'maxHiH2', 'maxLowH2', 'toprodHiH2',
                  'toprodLowH2', 'frnpCosts', 'capexCosts', 'h2Costs']:
            self.ui.__getattribute__(p + 'ResPerspDsb').setValue(self.__getattribute__(p))
        # ---------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------

        self.barchart()     # creazione dei diagrammi

    # Azioni conseguenti alla selezione dell'anno: popolazione della tendina dello scenario
    def year_selected(self):
        self.ui.scenCb.clear()
        self.ui.scenCb.addItems(list(s[self.ui.yearScenCb.currentText()].keys()))

    # Azioni conseguenti alla selezione delo scenario
    def scen_selected(self):
        year = self.ui.yearScenCb.currentText()
        scen = self.ui.scenCb.currentText()

        if scen:    # evita azioni inutili durante la popolazione della tendina scenario
            for k in s[year][scen]:
                # Scrittura delle variabili di scenario
                self.__setattr__(k + 'Scen', s[year][scen][k])
                # Scrittura delle caselle di scenario
                self.ui.__getattribute__(k + 'ScenDsb').setValue(s[year][scen][k])

            # -- Calcolo e scrittura nelle caaselledi alcune variabili non presenti nello scenario ---
            self.otherGenScen = self.ferGenScen - self.solarGenScen - self.windGenScen
            self.otherCapScen = self.ferCapScen - self.solarCapScen - self.windCapScen
            self.co2EmisScen = (self.enProdScen - self.solarGenScen - self.windGenScen) * 0.33

            for p in ['otherGen', 'otherCap', 'co2Emis']:
                self.ui.__getattribute__(p + 'ScenDsb').setValue(self.__getattribute__(p + 'Scen'))
            # ----------------------------------------------------------------------------------------

            # -- Calcolo delle variabili delle percentuali dei dari di scenario ----------------------
            for c in ['Gen', 'Cap']:
                self.__setattr__('fer' + c + 'PercScen',
                                 self.__getattribute__('fer' + c + 'Scen') / self.enDutyScen * 100)
                for p in ['solar', 'wind', 'other']:
                    self.__setattr__(p + c + 'PercScen',
                                     self.__getattribute__(p + c + 'Scen') /
                                     self.__getattribute__('fer' + c + 'Scen') * 100)
            # ----------------------------------------------------------------------------------------

    # Calcolo dello storage
    def sysStor_calc(self):
        # Verifica dela linea corrispondente alla percentuale di input
        for i in range(len(storage[0])):
            x = storage[0][i]
            if self.ferGenInput / 100 <= x:
                break

        # Calcolo dell'interpolazione del valore corrispondente nell'intorno dell'input
        y = (storage[1][i - 1] + (self.ferGenInput / 100 - storage[0][i - 1]) *
             (storage[1][i] - storage[1][i - 1]) / (storage[0][i] - storage[0][i - 1]))

        return (self.solarGen + self.windGen) * y

    # Creazione dei diagrammi dei risultati
    def barchart(self):
        # Inizializzazione dei dizionari dei grafici
        self.graph = {
            '': {
                'title': 'Fabbisogno',
                'barSeries': QtCharts.QBarSeries(),
                'chart': QtCharts.QChart(),
                'axis_x': QtCharts.QBarCategoryAxis(),
                'axis_y': QtCharts.QValueAxis(),
                'y_title': 'Energia [TWh]',
                'hi': 0,
                'y_scale': 0,
                'series': {
                    # 'totEnCons': 'Consumi finali di energia',
                    'h2Cons': 'Consumi\nper la produzione\ndi H2',
                    'enDuty': 'Fabbisogno\ndi energia\nelettrica',
                    'enProd': 'Energia\nprodotta',
                }
            },
            'Gen': {
                'title': 'Generazione',
                'barSeries': QtCharts.QBarSeries(),
                'chart': QtCharts.QChart(),
                'axis_x': QtCharts.QBarCategoryAxis(),
                'axis_y': QtCharts.QValueAxis(),
                'y_title': 'Energia [TWh]',
                'hi': 0,
                'y_scale': 0,
                'series': {
                    'solar': 'Solare',
                    'wind': 'Eolico',
                    'other': 'Altro',
                }
            },
            'Cap': {
                'title': 'Capacità',
                'barSeries': QtCharts.QBarSeries(),
                'chart': QtCharts.QChart(),
                'axis_x': QtCharts.QBarCategoryAxis(),
                'axis_y': QtCharts.QValueAxis(),
                'y_title': 'Potenza installata [GW]',
                'hi': 0,
                'y_scale': 0,
                'series': {
                    'solar': 'Solare',
                    'wind': 'Eolico',
                    'other': 'Altro',
                }
            },
        }

        # Elimino il widget dei grafici
        try:
            self.ui.graphWgt.deleteLater()
        except:
            pass

        self.ui.graphWgt = QtWidgets.QWidget()                  # Ricreo il widget dei grafici
        self.ui.optStorHL.insertWidget(2, self.ui.graphWgt)     # e lo inserisco nel layout

        # Calcolo la dimensione del widget dei grafici sulla base della dimensione degli altri widget
        graphsize = self.ui.optStorWgt.width() - self.ui.leftWgt.width() - self.ui.resultsWgt.width() - 40

        # Creazione del layout verticale dei grafici
        self.ui.graphVL = QtWidgets.QVBoxLayout(self.ui.graphWgt)
        self.ui.graphVL.setContentsMargins(0, 0, 0, 0)

        # I grafici dovranno avere un valore compreso tra 200 e 500, e pari al valore calcolato
        self.ui.graphWgt.setFixedSize(max(200, min(graphsize, 500)), self.ui.optStorWgt.height())

        # Creazione dei grafici mediante il dizionario
        for c in self.graph:
            self.__setattr__('set' + c + 'Act', QtCharts.QBarSet('Valori attuali'))
            self.__setattr__('set' + c + 'Persp', QtCharts.QBarSet('Valori prospettici'))

            for p in self.graph[c]['series']:
                self.graph[c]['axis_x'].append([self.graph[c]['series'][p]])

                self.__getattribute__('set' + c + 'Act').append(self.__getattribute__(p + c + 'Scen'))
                self.__getattribute__('set' + c + 'Persp').append(self.__getattribute__(p + c))

                if self.__getattribute__(p + c + 'Scen') > self.graph[c]['hi']:
                    self.graph[c]['hi'] = self.__getattribute__(p + c + 'Scen')
                if self.__getattribute__(p + c) > self.graph[c]['hi']:
                    self.graph[c]['hi'] = self.__getattribute__(p + c)

                mag = math.log10(self.graph[c]['hi']) // 1
                self.graph[c]['y_scale'] = 10 ** mag * (1 + round(self.graph[c]['hi'] / (10 ** mag)))

            self.graph[c]['barSeries'].append(self.__getattribute__('set' + c + 'Act'))
            self.graph[c]['barSeries'].append(self.__getattribute__('set' + c + 'Persp'))

            self.graph[c]['chart'].addSeries(self.graph[c]['barSeries'])

            self.graph[c]['chart'].setTitle(self.graph[c]['title'])
            self.graph[c]['chart'].setAnimationOptions(QtCharts.QChart.SeriesAnimations)

            self.graph[c]['chart'].addAxis(self.graph[c]['axis_x'], Qt.AlignBottom)
            self.graph[c]['barSeries'].attachAxis(self.graph[c]['axis_x'])

            self.graph[c]['axis_y'].setRange(0, self.graph[c]['y_scale'])
            self.graph[c]['axis_y'].setTitleText(self.graph[c]['y_title'])

            self.graph[c]['chart'].addAxis(self.graph[c]['axis_y'], Qt.AlignLeft)
            self.graph[c]['barSeries'].attachAxis(self.graph[c]['axis_y'])

            self.graph[c]['chart'].legend().setVisible(True)
            self.graph[c]['chart'].legend().setAlignment(Qt.AlignBottom)

            self.graph[c]['barGraph'] = QtCharts.QChartView(self.graph[c]['chart'])
            # L'altezza del grafico deve essere tale da permettere 3 gradici nel layout
            self.graph[c]['barGraph'].setMaximumHeight((self.ui.leftWgt.height() - 20) / 3)

            self.graph[c]['chart'].setBackgroundBrush(QtGui.QBrush(QtGui.QColor('transparent')))
            self.graph[c]['chart'].legend().setLabelColor(QtGui.QColor('white'))
            self.graph[c]['chart'].setTitleBrush(QtGui.QColor(255, 255, 255))
            self.graph[c]['chart'].setTitleFont(QtGui.QFont("Arial", 12))
            self.graph[c]['chart'].axisX().setLabelsColor(QtGui.QColor(255, 255, 255))
            self.graph[c]['chart'].axisY().setLabelsColor(QtGui.QColor(255, 255, 255))
            self.graph[c]['chart'].axisY().setTitleBrush(QtGui.QColor(255, 255, 255))
            self.graph[c]['chart'].axisY().setLabelFormat("%.0f")
            self.graph[c]['chart'].legend().setFont(QtGui.QFont("Arial", 10))

            self.ui.graphVL.addWidget(self.graph[c]['barGraph'])    # Aggiunta dei grafici nel layout

        # Inserimentdo ti duno spaziatore sotto i grafici
        bm_spacer = QSpacerItem(20, 10)
        self.ui.graphVL.addItem(bm_spacer)


# Dizionario degli scenari  TODO: Capire se deve essere impostato dall'esterno
s = {
    '2019': {
        'Consuntivo': {
            'totEnConsMtep': 112,
            'totEnCons': 1302.3,
            'h2Cons': 0,
            'enDuty': 320,
            'enImport': 51,
            'enProd': 269,
            'ferGen': 113,
            'solarGen': 23,
            'windGen': 20,
            'ferCap': 55,
            'solarCap': 21,
            'windCap': 11,
        },
    },
    '2030': {
        'FF55': {
            'totEnConsMtep': 112,
            'totEnCons': 1302.3,
            'h2Cons': 9,
            'enDuty': 366,
            'enImport': 52,
            'enProd': 314,
            'ferGen': 239,
            'solarGen': 101,
            'windGen': 68,
            'ferCap': 122,
            'solarCap': 75,
            'windCap': 27,
        },
        'LT': {
            'totEnConsMtep': 112,
            'totEnCons': 1302.3,
            'h2Cons': 0,
            'enDuty': 331,
            'enImport': 91,
            'enProd': 260,
            'ferGen': 187,
            'solarGen': 69,
            'windGen': 46,
            'ferCap': 91,
            'solarCap': 52,
            'windCap': 19,
        },
    },
    '2040': {
        'DE-IT': {
            'totEnConsMtep': 112,
            'totEnCons': 1302.3,
            'h2Cons': 18,
            'enDuty': 418,
            'enImport': 54,
            'enProd': 364,
            'ferGen': 325,
            'solarGen': 157,
            'windGen': 108,
            'ferCap': 175,
            'solarCap': 114,
            'windCap': 42,
        },
        'GA-IT': {
            'totEnConsMtep': 112,
            'totEnCons': 1302.3,
            'h2Cons': 16,
            'enDuty': 396,
            'enImport': 49,
            'enProd': 347,
            'ferGen': 302,
            'solarGen': 138,
            'windGen': 99,
            'ferCap': 160,
            'solarCap': 102,
            'windCap': 39,
        },
        'LT': {
            'totEnConsMtep': 112,
            'totEnCons': 1302.3,
            'h2Cons': 9,
            'enDuty': 389,
            'enImport': 52,
            'enProd': 337,
            'ferGen': 244,
            'solarGen': 102,
            'windGen': 71,
            'ferCap': 123,
            'solarCap': 75,
            'windCap': 28,
        },
    },
}


# Lettura del dizionario della curva di riferimento dello storage
storage = [[], []]
with open('./Functionalities/OptimalStorage/StorageTerna.csv', mode='r') as csv_file:
    for line in csv_file:
        storage[0].append(float(line.rstrip().split(';')[0]))
        storage[1].append(float(line.rstrip().split(';')[1]))
    csv_file.close()
