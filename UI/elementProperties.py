import yaml

try:
    from UI.ui_elementProperties import *
except:
    from ui_elementProperties import *

from UI.anomWgt import AnomWgt

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import sys
import copy
from datetime import datetime
from functools import partial
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

import variables
from variables import *

import datetime as dt


class ElementProperties(QMainWindow):
    def __init__(self, elem):
        super(ElementProperties, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # self.ui.startWgt.setStyleSheet(u"QPushButton {"
        #                                u"text-align: left;"
        #                                u"padding: 10px 40px;"
        #                                u"color: rgb(255, 255, 255);"
        #                                u"background-color: rgb(31, 31, 31); border: solid;" # border-style: outset;"
        #                                u"border-width: 3px; border-radius: 30px; border-color: rgb(127, 127, 127)"
        #                                u"}"
        #                                u"QPushButton:pressed {"
        #                                u"background-color: rgb(64, 64, 64); border-style: inset"
        #                                u"}")
        self.elem = elem
        self.cat = v[self.elem]['category']
        self.old_buses = copy.deepcopy(v[elem]['top']['conn'])
        self.buses = copy.deepcopy(v[elem]['top']['conn'])
        self.n_anom = 0
        self.anomWgt = []

        # self.ui.relWgt.setMaximumHeight(20)

        all_an_def = yaml.safe_load(open(mainpath + '/_temp/Functionalities/Anomalies/default.yml'))

        if self.cat in all_an_def.keys():
            self.anom_def = all_an_def[self.cat]
            self.aging_rate_def = all_an_def[self.cat]['Hourly_Degradation']['rate']
            self.anom_def.pop('Hourly_Degradation')

            self.anom_avail = list(self.anom_def.keys())

            self.anomalies = dict()

        else:
            self.anom_def, self.anom_avail = None, []

        try:
            self.__getattribute__(variables.visualpar + 'Show')()   # TODO: dA RIATTIVARE
        except:
            self.lfShow()

        self.ui.lfPls.clicked.connect(self.lfShow)
        self.ui.relPls.clicked.connect(self.relShow)
        self.ui.anomPls.clicked.connect(self.anomShow)
        self.ui.anomAddPls.clicked.connect(self.anomAdd)
        self.ui.agingCkB.clicked.connect(self.anomAging)

        self.lfParFill()

        self.relParFill()

        if self.cat in ['AC-PV', 'DC-PV', 'AC-Wind', 'DC-Wind', 'AC-BESS', 'DC-BESS']:
            self.anomParFill()
        # if v[self.elem]['lf']['p']:
        #     if 0 in v[self.elem]['lf']['p'].keys():
        #         if
        #         self.fillLfRes()
        self.ui.lfResMainWgt.setVisible(grid['studies']['lf'])
        # self.ui.relResMainWgt.setVisible(grid['studies']['rel'])
        self.ui.agingParWgt.setVisible(False)

        if grid['studies']['lf']:
            self.formatLfRes()

        if grid['studies']['rel']:
            self.relResFill()
        self.ui.relResMainWgt.setVisible(grid['studies']['rel'])
        self.ui.relWgt.setVisible(False)

        self.funcCheck()

    def funcCheck(self):
        # for f in fn_en:
        #     self.ui.__getattribute__(f + 'Wgt').setVisible(fn_en[f])
        self.ui.anomWgt.setVisible(self.anom_def is not None and fn_en['anom'])
        self.ui.relWgt.setVisible((self.cat not in mc['Node'] + mc['Vsource']) and fn_en['rel'])

    def lfShow(self):
        self.ui.lfWgt.setMaximumHeight(1500)
        self.ui.relWgt.setMaximumHeight(20)
        self.ui.anomWgt.setMaximumHeight(20)
        variables.visualpar = 'lf'

    def relShow(self):
        self.ui.lfWgt.setMaximumHeight(20)
        self.ui.relWgt.setMaximumHeight(1500)
        self.ui.anomWgt.setMaximumHeight(20)
        variables.visualpar = 'rel'

    def anomShow(self):
        self.ui.lfWgt.setMaximumHeight(20)
        self.ui.relWgt.setMaximumHeight(20)
        self.ui.anomWgt.setMaximumHeight(1500)
        variables.visualpar = 'anom'

        for i in v[self.elem]['anom']['par']['anomalies']:
            for a in v[self.elem]['anom']['par']['anomalies'][i]:
                if a in self.anom_avail:
                    self.anom_avail.remove(a)

        # print('anom avail: ', self.anom_avail)
        self.ui.anomAddPls.setVisible(self.anom_avail != [])

    def relParFill(self):
        # -- Preparazione delle caselle dei paramerti -----------------------------------------------------------------
        if self.cat != 'ExternalGrid':
            for par in ['t_preg', 'alfa', 'beta', 'Pi_E', 'Pi_Q']:
                try:
                    self.ui.__getattribute__(par + 'Dsb').setValue(v[self.elem]['rel']['par'][par])
                except KeyError:    # TODO: da abolire
                    if par == 't_preg':
                        self.ui.t_pregDsb.setValue(87600)
                        v[self.elem]['rel']['par'][par] = 87600
        else:
            self.ui.relWgt.setVisible(False)

    def relParSave(self):
        # -- Preparazione delle caselle dei paramerti -----------------------------------------------------------------
        if self.cat != 'ExternalGrid':
            for par in ['t_preg', 'alfa', 'beta', 'Pi_E', 'Pi_Q']:
                v[self.elem]['rel']['par'][par] = self.ui.__getattribute__(par + 'Dsb').value()
        # else:
        #     self.ui.relWgt.setVisible(False)

    def relResFill(self):
        self.ui.relResMainWgt.setVisible(grid['studies']['rel'])

        self.ui.relFurnWgt.setVisible(self.cat in mc['Load'])
        self.ui.relResWgt.setVisible(not self.cat in mc['Load'])

        if self.cat in mc['Load']:
            self.ui.rDayRelDsb.setValue(v[self.elem]['rel']['results']['load_rel'])
            self.ui.rNightRelDsb.setValue(v[self.elem]['rel']['results']['load_rel1'])
        elif self.cat not in mc['Node'] + mc['Vsource']:
            self.ui.lbdRelDsb.setValue(v[self.elem]['rel']['results']['lambda'])
            self.ui.rRelDsb.setValue(v[self.elem]['rel']['results']['R'])
            self.ui.piSiRelDsb.setValue(v[self.elem]['rel']['results']['Pi_Si'])
            self.ui.mtbfHrsDsb.setValue(v[self.elem]['rel']['results']['MTBF_ore'])
            self.ui.mtbfYrDsb.setValue(v[self.elem]['rel']['results']['MTBF_anni'])

    def lfParFill(self):
        for i in range(self.ui.lfParGL.count()):
            self.ui.lfParGL.itemAt(i).widget().deleteLater()

        spacer = QSpacerItem(10,10, QSizePolicy.Fixed)
        line = 0

        if self.cat not in ['AC-Node', 'DC-Node', 'ExternalGrid']:
            # -- Preparazione delle caselle V0 e V1 quando serve ------------------------------------------------------
            for b in range(len(self.buses)):
                self.__setattr__('v' + str(b) + 'Lbl', QLabel('V' + str(b)))
                self.__setattr__('v' + str(b) + 'Dsb', QDoubleSpinBox(None))
                self.__setattr__('v' + str(b) + 'UnitLbl', QLabel('kV'))

                self.ui.lfParGL.addWidget(self.__getattribute__('v' + str(b) + 'Lbl'), b, 0)
                self.ui.lfParGL.addWidget(self.__getattribute__('v' + str(b) + 'Dsb'), b, 1)
                self.ui.lfParGL.addWidget(self.__getattribute__('v' + str(b) + 'UnitLbl'), b, 2)

                # formattazione e popolazione dei campi
                self.dsbFormat(self.__getattribute__('v' + str(b) + 'Dsb'), decimals=3)
                self.__getattribute__('v' + str(b) + 'Lbl').setAlignment(Qt.AlignRight |
                                                                         Qt.AlignTrailing | Qt.AlignVCenter)
                self.__getattribute__('v' + str(b) + 'Dsb').setValue(v[self.buses[b]]['par']['Vn'][0])

                # Le caselle devono essere disabilitata
                self.__getattribute__('v' + str(b) + 'Dsb').setDisabled(True)
                self.__getattribute__('v' + str(b) + 'Dsb').setStyleSheet(u"background-color: rgb(95, 95, 95)")

                line += 1
            # ---------------------------------------------------------------------------------------------------------

            self.ui.lfParGL.addItem(spacer, line, 0)
            line += 1

        # -- Preparazione delle caselle dei parametri -----------------------------------------------------------------
        for par in el_format[self.cat]:
            self.__setattr__(par + 'Lbl', QLabel(par))
            self.__setattr__(par + 'Dsb', QDoubleSpinBox(None))
            self.__setattr__(par + 'UnitLbl', QLabel(el_format[self.cat][par]['unit']))

            self.ui.lfParGL.addWidget(self.__getattribute__(par + 'Lbl'), line, 0)
            self.ui.lfParGL.addWidget(self.__getattribute__(par + 'Dsb'), line, 1)
            self.ui.lfParGL.addWidget(self.__getattribute__(par + 'UnitLbl'), line, 2)
            i += 1

            # formattazione e popolazione dei campi
            self.dsbFormat(self.__getattribute__(par + 'Dsb'), minimum=el_format[self.cat][par]['min'],
                           maximum=el_format[self.cat][par]['max'], decimals=el_format[self.cat][par]['decimal'])
            self.__getattribute__(par + 'Lbl').setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

            if isinstance(v[self.elem]['par'][par], list):
                self.__getattribute__(par + 'Dsb').setValue(v[self.elem]['par'][par][0])
            else:
                self.__getattribute__(par + 'Dsb').setValue(v[self.elem]['par'][par])

            line += 1

            if self.cat in (mc['Load'] + mc['Generator']) and par == 'P':
                self.PeffDSB = QDoubleSpinBox()
                self.PeffDSB.setEnabled(True)
                self.dsbFormat(self.PeffDSB, decimals=3)
                self.PeffDSB.setStyleSheet(u"background-color: rgb(95, 95, 95)")

                self.PeffunitLbl = QLabel('kW')

                self.ui.lfParGL.addWidget(self.PeffDSB, line, 1)
                self.ui.lfParGL.addWidget(self.PeffunitLbl, line, 2)

                line += 1
                pass

        print(self.cat)
        self.ui.lfParWgt.setEnabled(not (self.cat == 'ExternalGrid' or self.elem=='sourcebus'))
        # -------------------------------------------------------------------------------------------------------------

        # -- creazione della parte dei profili, se previsto ----------------------------------------------------------
        if self.cat in prof_elem:
            # distanziatore
            spacer1 = QSpacerItem(10, 10, QSizePolicy.Fixed)
            self.ui.lfParGL.addItem(spacer1, line, 0)
            line += 1

            # -- creazione ed inserimento degli elementi ----
            self.scale_LBL = QLabel('Scala')
            self.scale_DSB = QDoubleSpinBox()
            self.scale_RB = QRadioButton('Costante')

            self.profile_RB = QRadioButton('Profilo')

            self.ui.lfParGL.addWidget(self.scale_LBL, i, 0)
            self.ui.lfParGL.addWidget(self.scale_DSB, i, 1)
            i += 1

            self.ui.lfParGL.addWidget(self.scale_RB, i, 1)
            i += 1

            self.ui.lfParGL.addWidget(self.profile_RB, i, 1)
            i += 1

            # formattazione e popolazione degli elementi del profilo
            self.dsbFormat(self.scale_DSB, 0, 1, 4)
            self.scale_LBL.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

            if v[self.elem]['par']['profile']['name'] is None:
                self.scale_DSB.setValue(v[self.elem]['par']['profile']['curve'])
                self.scale_RB.setChecked(True)
                self.scale_DSB.setStyleSheet(u"background-color: rgb(255, 255, 255);"
                                             u"color: rgb(0, 0, 0);")
            else:
                if grid['current']:
                    timestart = dt.datetime(grid['profile']['start'][0], grid['profile']['start'][1],
                                            grid['profile']['start'][2], grid['profile']['start'][3],
                                            grid['profile']['start'][4])
                    currenttime = dt.datetime(grid['current'][0], grid['current'][1], grid['current'][2],
                                              grid['current'][3], grid['current'][4])
                    t = int((currenttime - timestart).total_seconds() / (60 * grid['profile']['step']))
                else:
                    t = 0

                self.scale_DSB.setDisabled(True)
                self.profile_RB.setChecked(True)

                self.scale_DSB.setValue(v[self.elem]['par']['profile']['curve'][t])

                self.PeffDSB.setValue(v[self.elem]['par']['profile']['curve'][t] * v[self.elem]['par']['P'])

                self.scale_DSB.setStyleSheet(u"background-color: rgb(95, 95, 95)")

            # self.profile_RB.toggled.connect(self.profileCheck)

        # ------------------------------------------------------------------------------------------------------------

        spacer2 = QSpacerItem(10, 10, QSizePolicy.Fixed)
        self.ui.lfParGL.addItem(spacer2, line, 0)

        # casella Out-of-service
        self.out_of_service_LBL = QLabel('OutOfServ')
        self.out_of_service_CkB = QCheckBox()
        self.ui.lfParGL.addWidget(self.out_of_service_LBL, i, 0)
        self.ui.lfParGL.addWidget(self.out_of_service_CkB, i, 1)
        self.out_of_service_CkB.setChecked(v[self.elem]['par']['out-of-service'])
        i += 1

        # distanziatore necessario per riempire il vuoto tra i parametri e i pulsanti
        spacer_wgt = QWidget()
        self.ui.lfParGL.addWidget(spacer_wgt, i, 0)
        i += 1

        # -- verifica esistanza profili ------------------------------------------------------------------------------
        if 'profile' in v[self.elem]['par']:
            if v[self.elem]['par']['profile']['name']:
                self.profilePlotWgtCreate()
                # self.ui.lfVL.addWidget(self.profileWidget)
                self.ui.lfVL.insertWidget(3, self.profileWidget)
        # ------------------------------------------------------------------------------------------------------------

        # # -- creazione della sezione dei pulsanti --------------------------------------------------------------------
        # self.save_BTN = QPushButton('Salva')
        # self.cancel_BTN = QPushButton('Annulla')
        # self.pb_format(self.save_BTN, min_h=25)
        # self.pb_format(self.cancel_BTN, min_h=25)
        # self.save_BTN.clicked.connect(self.save_par)
        #
        # self.bottomHBL.addWidget(self.save_BTN)
        # spacer2 = QSpacerItem(20, 20, QSizePolicy.Fixed)
        # self.bottomHBL.addItem(spacer2)
        # self.bottomHBL.addWidget(self.cancel_BTN)
        # ------------------------------------------------------------------------------------------------------------

        # -- creazione della sezione delle BusBar --------------------------------------------------------------------
        self.bbFont = QFont()
        self.bbFont.setPointSize(9)
        self.bbFont.setBold(True)

        self.no_LBL = QLabel()
        self.no_LBL.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)

        # definizione dei Label delle busbar
        node_labels = []
        if v[self.elem]['category'] == 'PWM':
            node_labels = ['AC Node', 'DC Node']
        elif v[self.elem]['category'] in ['2W-Transformer', 'DC-DC-Converter']:
            node_labels = ['HV Node', 'LV Node']
        elif v[self.elem]['category'] in ['AC-Line', 'DC-Line', 'AC-Node', 'DC-Node']:
            for i in range(len(v[self.elem]['top']['conn'])):
                node_labels.append('Node ' + str(i))
        else:
            node_labels = ['Node', '']

        # -- Settaggio dei campi della sezione Busbar  ------------------------------------
        for i in range(len(v[self.elem]['top']['conn'])):
            self.__setattr__('node' + str(i) + '_LBL', QLabel(node_labels[i]))

            self.ui.lfNodeGL.addWidget(self.__getattribute__('node' + str(i) + '_LBL'), i, 0)
            self.__getattribute__('node' + str(i) + '_LBL').setMinimumSize(QSize(0, 25))

            self.__setattr__('node' + str(i) + '_BTN', QPushButton())
            self.__setattr__('node' + str(i) + '_CB', QComboBox())

            self.ui.lfNodeGL.addWidget(self.__getattribute__('node' + str(i) + '_BTN'), i, 1)
            self.__getattribute__('node' + str(i) + '_BTN').setFont(self.bbFont)
            self.__getattribute__('node' + str(i) + '_BTN').setStyleSheet(u"text-align: left; border-width: 0px;")

            self.ui.lfNodeGL.addWidget(self.no_LBL, i, 2)

            self.ui.lfNodeGL.addWidget(self.__getattribute__('node' + str(i) + '_CB'), i, 1)
            # ---------------------------------------------------------------------------------

            # settare le azioni degli elementi (se non sono Node o Source)
            if self.cat not in mc['Node'] + mc['Vsource']:
                self.__getattribute__('node' + str(i) + '_BTN').clicked.connect(partial(self.bbClicked, i))
                self.__getattribute__('node' + str(i) + '_CB').activated.connect(partial(self.bbChanged, i,
                                                                                         None))

        # Scrittura dei campi node0 e node1
        for i in range(len(v[self.elem]['top']['conn'])):
            self.bbChanged(i=i, node=v[self.elem]['top']['conn'][i])
        # ------------------------------------------------------------------------------------------------------------

        # creazione della scrollbar, se il settore fosse troppo lungo
        # self.scroll = QScrollArea()
        # self.scroll.setWidget(self.ui.propertiesWgt)
        # self.scroll.setWidgetResizable(True)
        # self.layout = QVBoxLayout()
        # self.layout.addWidget(self.scroll)
        # self.setLayout(self.layout)

        # self.profile_RB.clicked.connect(self.profileCheck)
        # self.scale_RB.toggled.connect(self.profileCheck)

        self.ui.savePLS.clicked.connect(self.parSave)

        pass

    def anomParFill(self):
        self.ui.agingParWgt.setVisible('Hourly_Degradation'in list(v[self.elem]['anom']['par'].keys()))
        self.ui.agingCkB.setChecked('Hourly_Degradation'in list(v[self.elem]['anom']['par'].keys()))
        if self.ui.agingCkB.isChecked():
            self.ui.agingRateDsb.setValue(v[self.elem]['anom']['par']['Hourly_Degradation']['rate'])

        for n in v[self.elem]['anom']['par']['anomalies']:
            for cat in v[self.elem]['anom']['par']['anomalies'][n]:
                for typol in v[self.elem]['anom']['par']['anomalies'][n][cat]:
                    self.anomWgt.append(AnomWgt(self.cat))  # creazione della classe dell'anomalia, aggiunta all'elenco
                    # n = len(self.anomWgt) - 1  # la sua posizione sarà l'ultima

                    self.ui.anomListVL.insertWidget(1 + n, self.anomWgt[n].ui.anomWgt)  # viene inserito il widget
                    self.anomWgt[n].ui.catCB.insertItems(1, self.anom_avail)
                    # self.anomWgt[n].ui_actions()
                    self.anomWgt[n].ui.catCB.setCurrentText(cat)
                    self.anomWgt[n].ui.typeCB.setCurrentText(typol)

                    col = 39 + 16 * n
                    self.anomWgt[n].ui.anomWgt.setStyleSheet('*{background-color: rgb(' + str(col) + ', 0, 0);'
                                                             'border-radius: 10px;}'
                                                             'QPushButton, QDoubleSpinBox {'
                                                             'color: rgb(255, 255, 255); '
                                                             'background-color: rgb(0, 0, 0);'
                                                             'border: solid;border-width: 1px; border-radius: 5px; '
                                                             'border-color: rgb(127, 127, 127)}'
                                                             'QPushButton:pressed {background-color: rgb(64, 64, 64); '
                                                             'border-style: inset}')

                    self.anom_avail = list(self.anom_def.keys())
                    for an in self.anomWgt:
                        if an != self.anomWgt[n]:
                            self.anom_avail.remove(an.ui.catCB.currentText())
                    self.anomWgt[n].ui.catCB.clear()
                    self.anomWgt[n].ui.catCB.insertItems(1, self.anom_avail)
                    self.anomWgt[n].ui_actions()
                    self.anomWgt[n].ui.catCB.setCurrentText(cat)
                    self.anomWgt[n].cat_changed()
                    self.anomWgt[n].ui.typeCB.setCurrentText(typol)

        for n in range(len(self.anomWgt)):
            cat = self.anomWgt[n].ui.catCB.currentText()
            cat = list(v[self.elem]['anom']['par']['anomalies'][n].keys())[0]
            typol = self.anomWgt[n].ui.typeCB.currentText()
            typol = list(v[self.elem]['anom']['par']['anomalies'][n][cat].keys())[0]
            # anom_typol_par = {
            #     'scale': 'value',
            #     '(1-exp) decrease': 'alpha',
            #     '(-x+1) decrease': 'alpha'
            # }
            # print('n:', n)
            # print('cat:', cat)
            # print('typol:', typol)

            self.anomWgt[n].ui.lbdaDsb.setValue(
                v[self.elem]['anom']['par']['anomalies'][n][cat][typol]['lambda_a'])
            self.anomWgt[n].ui.lbddurDsb.setValue(
                v[self.elem]['anom']['par']['anomalies'][n][cat][typol]['lambda_duration'])
            self.anomWgt[n].ui.fixCkb.setChecked(
                v[self.elem]['anom']['par']['anomalies'][n][cat][typol]['is_fixed'])
            self.anomWgt[n].ui.parDsb.setValue(
                v[self.elem]['anom']['par']['anomalies'][n][cat][typol][anom_typol_par[typol]])

            # vengono compresse le altre anomaliem e resa vilibile solo quella corrente
            self.anomViewUpdate(n)

            # Inizializzazione delle azioni sui pulsanti
            self.anomWgt[n].ui.detailsPb.clicked.connect(partial(self.anomViewUpdate, n))
            self.anomWgt[n].ui.upPb.clicked.connect(partial(self.anomMove, n, 'up'))
            self.anomWgt[n].ui.downPb.clicked.connect(partial(self.anomMove, n, 'down'))
            self.anomWgt[n].ui.cancPb.clicked.connect(partial(self.anomDel, n))

            # pulsante "up" disabilitato per il primo widget
            self.anomWgt[n].ui.upPb.setEnabled(n != 0)
            # pulsante "down" disabilitato per l'ultimo widget
            self.anomWgt[n].ui.downPb.setEnabled(n != len(self.anomWgt) - 1)

        # # Aggiorno l'elenco delle anomalie disponibili in self.anom_avail
        # for anomaly in self.anomWgt:
        #     cat = anomaly.ui.catCB.currentText()
        #     typol = anomaly.ui.typeCB.currentText()
        #     self.anom_avail = list(self.anom_def.keys())
        #     for an in self.anomWgt:
        #         if an != anomaly:
        #             self.anom_avail.remove(an.ui.catCB.currentText())
        #     anomaly.ui.catCB.clear()
        #     anomaly.ui.catCB.insertItems(1, self.anom_avail)
        #     anomaly.ui_actions()
        #     anomaly.ui.catCB.setCurrentText(cat)
        #     anomaly.cat_changed()
        #     anomaly.ui.typeCB.setCurrentText(typol)

    def profileCheck(self):
        self.dsbFormat(self.scale_DSB, 0, 1, 4)
        self.scale_LBL.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        if isinstance(v[self.elem]['par']['profile']['curve'], list):
            # TODO: Da cambiare sulla base della nuova definizione dei profili temporali
            # time = datetime.now().hour * 4 + int(datetime.now().minute / 15)
            value = v[self.elem]['par']['profile']['curve'][0]
        else:
            value = v[self.elem]['par']['profile']['curve']
        self.scale_DSB.setValue(value)

        # if v[self.elem]['par']['profile']['name'] is None or self.scale_RB.isChecked():
        if self.scale_RB.isChecked():
            self.scale_DSB.setStyleSheet(u"background-color: rgb(255, 255, 255);"
                                         u"color: rgb(0, 0, 0);")
            self.scale_DSB.setDisabled(False)
        else:
            self.scale_DSB.setDisabled(True)
            self.scale_DSB.setStyleSheet(u"background-color: rgb(95, 95, 95)")

    def profilePlotWgtCreate(self):
        font = {
            'weight': 'normal',
            'size': 4
        }

        matplotlib.rc('font', **font)
        self.canvas1 = FigureCanvas(plt.Figure(figsize=(1.7, 1.4)))
        self.ax = self.canvas1.figure.subplots()

        self.ax.plot([a for a in range(0, grid['profile']['points'])], v[self.elem]['par']['profile']['curve'])  # TODO: da correggere: inserire i dati reali

        self.ax.set_title('Profilo')
        self.ax.set_ylim([0, 1.05])
        self.ax.set_xlim([0, grid['profile']['points']])
        self.ax.set_xlabel('Tempo [h]', fontsize=4)
        self.ax.set_ylabel('Profilo [p.u.]', fontsize=2)

        self.canvas1.draw()
        self.canvas1.flush_events()
        self.canvas1.print_jpeg('a.jpg')
        # self.par_wgt.mainVBL.insertWidget(2, self.canvas)
        # self.profWgtVBL.addWidget(self.canvas1)

        # Creazione del widget
        self.profileWidget = QWidget()
        self.profileWidget.setStyleSheet(u"background-color: rgb(0, 0, 48); border-radius: 10px;")
        self.profileWidget.setMaximumHeight(180)
        self.profileWidget.setMaximumWidth(180)
        self.profWgtVBL = QVBoxLayout(self.profileWidget)
        self.profileLbl = QLabel()

        self.profileLbl.setPixmap(QPixmap("a.jpg"))
        self.profWgtVBL.addWidget(self.profileLbl)
        # self.profWgtVBL.addWidget(self.canvas1)

        self.profileBtn = QPushButton('Apri profilo')
        self.pbFormat(self.profileBtn, min_h=20)

        self.profWgtVBL.addWidget(self.profileBtn)

    def profileWgtRefresh(self):
        self.ui.lfVL.itemAt(3).widget().deleteLater()
        self.profileWidget.deleteLater()
        self.profilePlotWgtCreate()
        self.ui.lfVL.insertWidget(3, self.profileWidget)

    # azioni da eseguire alla richiesta di modifica del nodo di connessione
    def bbClicked(self, i=0, event2=None):
        # Se è ancora attiva la selezione sull'altra busbar, deve essere ripristinata la casella
        if len(self.buses) > 1:
            j = int(not i)
            if self.__getattribute__('node' + str(j) + '_CB').isVisible():
                self.__getattribute__('node' + str(j) + '_BTN').setText(self.buses[j])
                self.__getattribute__('node' + str(j) + '_BTN').show()
                self.__getattribute__('node' + str(j) + '_CB').hide()

        # Nascodno il bottone, e mostro la lista di selezione
        self.__getattribute__('node' + str(i) + '_BTN').hide()
        self.__getattribute__('node' + str(i) + '_CB').show()

    def bbChanged(self, i=0, node=None, event=None):
        if not node:
            node = self.__getattribute__('node' + str(i) + '_CB').currentText()

        self.buses[i] = node

        # Se cambio la prima busbar di una linea, verifico se la tensione della seconda busbar è coerente,
        #     altrimenti deve essere cambiata
        if self.cat in ['AC-Line', 'DC-Line'] and self.buses[1]:
        # if self.cat in ['AC-Line', 'DC-Line'] and len(self.buses) >1:
            if i == 0 and v[self.buses[0]]['par']['Vn'] != v[self.buses[1]]['par']['Vn']:
                self.buses[1] = None
                self.__getattribute__('node1_BTN').setText('-')

        self.__getattribute__('node' + str(i) + '_BTN').setText(node)
        self.__getattribute__('node' + str(i) + '_BTN').show()

        # aggiornamento della lista delle busbar coerenti per ogni nodo
        for j in range(len(self.buses)):
            nodes = self.bbList(j, node)
            self.__getattribute__('node' + str(j) + '_CB').clear()
            self.__getattribute__('node' + str(j) + '_CB').addItems(nodes)
            self.__getattribute__('node' + str(j) + '_CB').hide()

        # Scrittura del voltaggio dell'elemento, in base al Nodo a cui è connesso
        # try:
        if self.cat not in mc['Vsource'] + mc['Node']:
            self.__getattribute__('v' + str(i) + 'Dsb').setValue(v[node]['par']['Vn'][0])
        # except AttributeError:
        #     pass

        if self.cat in mc['Line']:
            self.ui.savePLS.setEnabled(self.__getattribute__('node1_BTN').text() != '-')
            if self.ui.savePLS.isEnabled():
                # self.save_BTN.setStyleSheet(u"background-color: rgb(255, 255, 255)")
                self.pbFormat(self.ui.savePLS, min_h=25)

            else:
                # self.save_BTN.setStyleSheet(u"background-color: rgb(95, 95, 95)")
                self.pbDisabled(self.ui.savePLS, min_h=25)

    # Definizione dell'elenco delle BusBar ammissibili
    def bbList(self, i, node):
        nodes = []

        if self.cat in ['2W-Transformer']:
            if i == 0:
                for el in v:
                    if (v[el]['category'] == 'AC-Node' and el not in self.buses and
                            v[el]['par']['Vn'][0] > v[self.buses[1]]['par']['Vn'][0]):
                        nodes.append(el)
            else:
                for el in v:
                    if (v[el]['category'] == 'AC-Node' and el not in self.buses and
                            v[el]['par']['Vn'][0] < v[self.buses[0]]['par']['Vn'][0]):
                        nodes.append(el)

        elif self.cat in ['PWM']:
            if i == 0:
                for el in v:
                    if v[el]['category'] == 'AC-Node' and el not in self.buses:
                        nodes.append(el)
            else:
                for el in v:
                    if v[el]['category'] == 'DC-Node' and el not in self.buses:
                        nodes.append(el)

        elif self.cat in ['DC-DC-Converter']:
            if i == 0:
                for el in v:
                    if (v[el]['category'] == 'DC-Node' and el not in self.buses and
                            v[el]['par']['Vn'][0] > v[self.buses[1]]['par']['Vn'][0]):
                        nodes.append(el)
            else:
                for el in v:
                    if (v[el]['category'] == 'DC-Node' and el not in self.buses and
                            v[el]['par']['Vn'][0] < v[self.buses[0]]['par']['Vn'][0]):
                        nodes.append(el)

        elif self.cat in ['AC-Load', 'AC-Wind', 'Diesel-Motor', 'AC-Line', 'AC-BESS', 'AC-PV', 'Turbine']:
            for el in v:
                try:
                    if v[el]['category'] == 'AC-Node' and el not in self.buses:
                        nodes.append(el)
                except:
                    print('Errore elemento', el)

        elif self.cat in DC_elem:
            for el in v:
                if v[el]['category'] == 'DC-Node' and el not in self.buses:
                    nodes.append(el)

        nodes.sort()                        # Nodi in ordine alfabetico
        nodes = [self.buses[i]] + nodes     # Il primo nodo dovrà essere il nodo corrente

        # Nel caso in cui l'elemento è una linea, e si tratta del nodo secondario dopo la variazione della busabar
        # primaria, la lista è composta dai soli nodi che hanno la stessa tensione nominale
        if i == 1:
            for cat in ['AC', 'DC']:
                if self.cat in [cat + '-Line'] and self.__getattribute__('node1_BTN').text() == '-':
                    nodes = []
                    for el in v:
                        if (v[el]['category'] == cat + '-Node' and
                                v[el]['par']['Vn'] == v[self.buses[0]]['par']['Vn'] and
                                el not in self.buses):
                            nodes.append(el)
                            pass
        return nodes

    def formatLfRes(self):
        spacer = QSpacerItem(10, 10, QSizePolicy.Fixed)
        line = 0
        oldtag = None
        # -- Preparazione delle caselle dei paramerti -----------------------------------------------------------------
        for par in el_lfresults[self.cat]:
            tag = el_lfresults[self.cat][par]['tag']
            i = el_lfresults[self.cat][par]['i']

            if tag != oldtag and line != 0:
                self.ui.lfResGL.addItem(spacer, line, 0)
                line += 1

            self.__setattr__(par + 'ResLbl', QLabel(par))
            self.__setattr__(par + 'ResDsb', QDoubleSpinBox(None))
            self.__setattr__(par + 'ResUnitLbl', QLabel(el_lfresults[self.cat][par]['unit']))

            self.ui.lfResGL.addWidget(self.__getattribute__(par + 'ResLbl'), line, 0)
            self.ui.lfResGL.addWidget(self.__getattribute__(par + 'ResDsb'), line, 1)
            self.ui.lfResGL.addWidget(self.__getattribute__(par + 'ResUnitLbl'), line, 2)

            oldtag = tag
            # i += 1

            # formattazione e popolazione dei campi
            self.dsbFormat(self.__getattribute__(par + 'ResDsb'), decimals=el_lfresults[self.cat][par]['decimal'],
                           minimum=-9999999.999, maximum=9999999.999)
            self.__getattribute__(par + 'ResLbl').setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

            line += 1
        # -------------------------------------------------------------------------------------------------------------
        self.lfResFill()
        pass

    def lfResFill(self, t=0):
        for par in el_lfresults[self.cat]:
            tag = el_lfresults[self.cat][par]['tag']
            i = el_lfresults[self.cat][par]['i']
            if i in [0, 1]:
                self.__getattribute__(par + 'ResDsb').setValue(v[self.elem]['lf'][tag][i][t])
            else:
                self.__getattribute__(par + 'ResDsb').setValue(v[self.elem]['lf'][tag][t])
        pass

    # formattazione dei DoubleSPinBox
    def dsbFormat(self, item, minimum=0.00, maximum=9999.99, decimals=2, step=0.1):
        item.setMinimum(minimum)
        item.setMaximum(maximum)
        item.setDecimals(decimals)
        item.setSingleStep(step)

        item.setButtonSymbols(QAbstractSpinBox.NoButtons)
        item.setStyleSheet(u"background-color: rgb(255, 255, 255);"
                           u"color: rgb(0, 0, 0);"
                           u"border: solid;"
                           u"border-width: 1px;"
                           u"border-color: rgb(223, 223, 223);")
        item.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

    # formattazione dei pushbutton
    def pbFormat(self, item, min_w=0, min_h=0):
        item.setStyleSheet(u"QPushButton {"
                           u"color: rgb(255, 255, 255);"
                           u"background-color: rgb(0, 0, 0); border: solid;"  # border-style: outset;"
                           u"border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)"
                           u"}"
                           u"QPushButton:pressed {"
                           u"background-color: rgb(64, 64, 64); border-style: inset"
                           u"}")
        item.setMinimumSize(QSize(min_w, min_h))

    def pbDisabled(self, item, min_w=0, min_h=0):
        item.setStyleSheet(u"QPushButton {"
                           u"color: rgb(63, 63, 63);"
                           u"background-color: rgb(31, 31, 31); border: solid;"  # border-style: outset;"
                           u"border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)"
                           u"}"
                           u"QPushButton:pressed {"
                           u"background-color: rgb(64, 64, 64); border-style: inset"
                           u"}")
        item.setMinimumSize(QSize(min_w, min_h))

    def bbFix(self, elem):
        # Se si modifica la tensione della busbar,
        # bisogna modificare la tensione nominale degli elementi a essa connessa

        # Se l'elemento è un nodo o la rete esterna, e se è cambiata la tensione nomnale
        if self.cat in mc['Node'] + mc['Vsource'] and v[elem]['par']['Vn'] != self.VnDsb.value():
        # if self.cat in mc['Node'] + mc['Vsource'] and v[elem]['par']['Vn'] != self.Vn_DSB.value():
            for el in self.bbLink(elem):
                for bb in self.buses:
                    if v[bb]['category'] in mc['Transformer']:
                        for i in range(len(v[bb]['top']['conn'])):
                            if v[bb]['top']['conn'][i] == elem:
                                v[bb]['par']['Vn'][i] = self.VnDsb.value()
                                # v[bb]['par']['Vn' + str(i)] = self.VnDsb.value()
                                # v[bb]['par']['Vn' + str(i)] = self.Vn_DSB.value()
                        pass
                    else:
                        v[el]['par']['Vn'][0] = self.VnDsb.value()
                        # v[el]['par']['Vn'] = self.Vn_DSB.value()
                        pass

        # Se si modifica la busbar connessa,
        # bisogna modificare anche l'elenco delle connessioni nella vecchia e nella nuova busbar
        elif self.buses != self.old_buses:
            for b in range(len(self.buses)):
                if self.buses[b] != self.old_buses[b]:
                    v[elem]['par']['Vn' + str(b)] = self.__getattribute__('v' + str(b) + 'Dsb').value()
                    v[elem]['top']['conn'][b] = self.buses[b]

                    v[self.buses[b]]['top']['conn'].append(elem)

                    i = v[self.old_buses[b]]['top']['conn'].index(elem)
                    v[self.old_buses[b]]['top']['conn'].pop(i)

                    # for i in v[self.buses[b]]['top']['conn']:
                    #     pass
        #     if self.cat in mc['Node'] + mc['Vsource']:
        #         for el in self.buses:
        #             if el not in self.old_buses:
        #                 if v[el]['category'] in mc['Transformer']:
        #                     pass
        #                 else:
        #                     v[el]['par']['Vn'] = v[self.elem]['par']['Vn']
        #
        #         pass

    def bbLink(self, busbar):
        buses = [busbar]
        bb_solved = []
        lines_solved = []
        while buses != []:
            for bb in buses:
                for conn in v[bb]['top']['conn']:
                    if v[conn]['category'] in mc['Line'] and conn not in lines_solved:
                        for b in v[conn]['top']['conn']:
                            if b != bb and b not in bb_solved:
                                buses.append(b)
                        lines_solved.append(conn)
                bb_solved.append(bb)
                buses.pop(buses.index(bb))
        return bb_solved

    def anomAging(self):
        self.ui.agingParWgt.setVisible(self.ui.agingCkB.isChecked())
        if 'Hourly_Degradation' in list(v[self.elem]['anom']['par'].keys()):
            self.ui.agingRateDsb.setValue(v[self.elem]['anom']['par']['Hourly_Degradation']['rate'])
        else:
            self.ui.agingRateDsb.setValue(self.aging_rate_def)

    def anomAdd(self):
        # Aggiorno l'elenco delle anomalie disponibili in self.anom_avail
        self.anom_avail = list(self.anom_def.keys())
        for an in self.anomWgt:
            self.anom_avail.remove(an.ui.anomLbl.text())

        # Se l'elenco delle anomalie disponibile contiene almeno una voce, sarà possibile aggiungere una nuova anomalia
        self.ui.anomAddPls.setVisible(len(self.anom_avail) > 1)

        self.anomWgt.append(AnomWgt(self.cat))  # viene creata la classe della nuova anomalia, ed aggiunta all'elenco
        n = len(self.anomWgt) - 1               # la sua posizione sarà l'ultima

        self.ui.anomListVL.insertWidget(1 + n, self.anomWgt[n].ui.anomWgt)  # viene inserito il widget
        self.anomWgt[n].ui_actions()                                        # attivazione delle azioni sui combo-box
        # viene aggiornato il Combobox delle anomalie disponibili
        self.anomWgt[n].ui.catCB.insertItems(1, self.anom_avail)

        # Formattazione Widget
        col = 39 + 16 * n
        self.anomWgt[n].ui.anomWgt.setStyleSheet('*{background-color: rgb(' + str(col) + ', 0, 0);'
                                                 'border-radius: 10px;}'
                                                 'QPushButton, QDoubleSpinBox {'
                                                 'color: rgb(255, 255, 255);background-color: rgb(0, 0, 0); '
                                                 'border: solid;border-width: 1px; border-radius: 5px; '
                                                 'border-color: rgb(127, 127, 127)}'
                                                 'QPushButton:pressed {background-color: rgb(64, 64, 64); '
                                                 'border-style: inset}')
        self.anomWgt[n].ui.detailsWgt.setStyleSheet('*{background-color: rgb(' + str(col) + ', 0, 0);'
                                                    'border-radius: 10px;}'
                                                    'QPushButton, QDoubleSpinBox {'
                                                    'color: rgb(255, 255, 255);background-color: rgb(0, 0, 0); '
                                                    'border: solid;border-width: 1px; border-radius: 5px; '
                                                    'border-color: rgb(127, 127, 127)}'
                                                    'QPushButton:pressed {background-color: rgb(64, 64, 64); '
                                                    'border-style: inset}')

        # vengono compresse le altre anomaliem e resa vilibile solo quella corrente
        self.anomViewUpdate(n)

        # Inizializzazione delle azioni sui pulsanti
        self.anomWgt[n].ui.detailsPb.clicked.connect(partial(self.anomViewUpdate, n))
        self.anomWgt[n].ui.upPb.clicked.connect(partial(self.anomMove, n, 'up'))
        self.anomWgt[n].ui.downPb.clicked.connect(partial(self.anomMove, n, 'down'))
        self.anomWgt[n].ui.cancPb.clicked.connect(partial(self.anomDel, n))

    def anomViewUpdate(self, n):
        # Viene esploso il dettaglio dell'anomalia "n", le altre sono nascoste
        for i in range(len(self.anomWgt)):
            self.anomWgt[i].ui.detailsWgt.setVisible(i == n)
            self.anomWgt[i].ui.detailsPbWgt.setVisible(i != n)

    def anomMove(self, n, move):
        anom_temp = []      # variabile d'apoggio dei widget delle anomalie

        for i in range(len(self.anomWgt)):
            anom_temp.append(None)      # l'array anom_temp deve avere la stessa dimensione di self.anomWgt
            # # disattivo momentaneamente tutti i pulsanti del widget
            # self.anomWgt[i].ui.detailsPb.clicked.disconnect()
            # self.anomWgt[i].ui.upPb.clicked.disconnect()
            # self.anomWgt[i].ui.downPb.clicked.disconnect()
            # self.anomWgt[i].ui.cancPb.clicked.disconnect()

        # Riordino i widget mediante l'array d'appoggio
        for i in range(len(self.anomWgt)):
            if i == n:
                # Per il widget selezionato,
                # se l'azione è "up", devo salire di una posizione (-1), se è "down" devo scendere (+1)
                new_i = i - int(move == 'up') + int(move == 'down')

            elif i == n - int(move == 'up') + int(move == 'down'):
                # ... e l'altro deve prendere il psoto del selezionato
                new_i = i + int(move == 'up') - int(move == 'down')

            else: # altrimenti non deve cambiare niente
                new_i = i
            anom_temp[new_i] = self.anomWgt[i]  # riscrivo i widget nell'array temporaneo con le nuove posizioni
        self.anomWgt = anom_temp                # riporto tutto nellarray dei widget effettivo

        self.anomPopulate()

    def anomPopulate(self):
        # Cancellazione di tutti i widget dei dettagloi delle anomalie
        for i in range(self.ui.anomListVL.count() - 1, -1, -1):
            self.ui.anomListVL.removeWidget(self.ui.anomListVL.itemAt(i).widget())

            # disattivo momentaneamente tutti i pulsanti del widget
            self.anomWgt[i].ui.detailsPb.clicked.disconnect()
            self.anomWgt[i].ui.upPb.clicked.disconnect()
            self.anomWgt[i].ui.downPb.clicked.disconnect()
            self.anomWgt[i].ui.cancPb.clicked.disconnect()

        # Riscrittura Widget dei dettagli delle anomalie
        for n in range(len(self.anomWgt)):
            self.ui.anomListVL.insertWidget(n, self.anomWgt[n].ui.anomWgt)
            self.anomWgt[n].ui.upPb.clicked.connect(partial(self.anomMove, n, 'up'))
            self.anomWgt[n].ui.downPb.clicked.connect(partial(self.anomMove, n, 'down'))
            self.anomWgt[n].ui.detailsPb.clicked.connect(partial(self.anomViewUpdate, n))
            self.anomWgt[n].ui.cancPb.clicked.connect(partial(self.anomDel, n))

            col = 39 + 16 * n
            self.anomWgt[n].ui.anomWgt.setStyleSheet('*{background-color: rgb(' + str(col) + ', 0, 0);'
                                                     'border-radius: 10px;}'
                                                     'QPushButton, QDoubleSpinBox {'
                                                     'color: rgb(255, 255, 255);background-color: rgb(0, 0, 0); '
                                                     'border: solid;border-width: 1px; border-radius: 5px; '
                                                     'border-color: rgb(127, 127, 127)}'                                   
                                                     'QPushButton:pressed {background-color: rgb(64, 64, 64); '
                                                     'border-style: inset}')

            # pulsante "up" disabilitato per il primo widget
            self.anomWgt[n].ui.upPb.setEnabled(n != 0)
            # pulsante "down" disabilitato per l'ultimo widget
            self.anomWgt[n].ui.downPb.setEnabled(n != len(self.anomWgt) - 1)

    def anomDel(self, n):
        # anon_temp = self.anomWgt
        # self.anom_avail.append(self.anomWgt[n].ui.anomLbl.text())

        self.ui.anomListVL.removeWidget(self.ui.anomListVL.itemAt(n).widget())

        self.anomWgt[n].ui.anomWgt.deleteLater()
        # self.ui.anomListVL.update()
        self.anomWgt.pop(n)
        self.anomPopulate()
        self.ui.anomAddPls.setVisible(True)

    def anomSave(self):
        if self.ui.agingCkB.isChecked():
            v[self.elem]['anom']['par']['Hourly_Degradation'] = {'rate': self.ui.agingRateDsb.value()}
        elif 'Hourly_Degradation' in list(v[self.elem]['anom']['par'].keys()):
            v[self.elem]['anom']['par'].pop('Hourly_Degradation')

        i = 0
        v[self.elem]['anom']['par']['anomalies'] = dict()
        for anomaly in self.anomWgt:
            cat = anomaly.ui.catCB.currentText()
            typol = anomaly.ui.typeCB.currentText()
            v[self.elem]['anom']['par']['anomalies'][i] = {cat: {typol: {}}}

            int_par = {
                'scale': 'value',
                '(1-exp) decrease': 'alpha',
                '(-x+1) decrease': 'alpha'
            }
            v[self.elem]['anom']['par']['anomalies'][i][cat][typol]['lambda_a'] = anomaly.ui.lbdaDsb.value()
            v[self.elem]['anom']['par']['anomalies'][i][cat][typol]['lambda_duration'] = anomaly.ui.lbddurDsb.value()
            v[self.elem]['anom']['par']['anomalies'][i][cat][typol]['is_fixed'] = anomaly.ui.fixCkb.isChecked()
            v[self.elem]['anom']['par']['anomalies'][i][cat][typol][int_par[typol]] = anomaly.ui.parDsb.value()
            i += 1

                # a = QVBoxLayout()
        # a.upda

    def test(self):
        self.anomWgt1.type_changed()
        print('cliccato')

        # an_dict = {'mainWgt': QWidget(), 'mainGL': QGridLayout(),
        #            'catCB': QComboBox(), 'catLbl': QLabel('Cat.:'),
        #            'typeCB': QComboBox(), 'typeLbl': QLabel('Tipol.:')}
        # an_dict['mainWgt'].setLayout(an_dict['mainGL'])
        # self.ui.anomVL.insertWidget(1, an_dict['mainWgt'])
        #
        # an_dict['mainGL'].addWidget(an_dict['catLbl'], 0, 0)
        # an_dict['mainGL'].addWidget(an_dict['catCB'], 0, 1)
        # an_dict['catCB'].insertItems(0, self.anom_avail)
        #
        # an_dict['mainGL'].addWidget(an_dict['typeLbl'], 1, 0)
        # an_dict['mainGL'].addWidget(an_dict['typeCB'], 1, 1)
        # an_dict['typeCB'].insertItems(0, ['uno', 'due', 'tre'])
        #
        # an_dict['parWgt'] = QWidget()
        # an_dict['parGL'] = QGridLayout()
        # an_


        # a = QGridLayout()
        # a.

        # a = QComboBox()
        # a.insertItems(0, self.anom_avail)
        # # a.layou

        print('done')
        pass

    # salvataggio dei dati dall'interfaccia al dizionario
    def parSave(self):
        self.bbFix(self.elem)
        # TODO: nel caso di variazione di tensione a busbar correlate, bisogna mettere un alert

        for par in el_format[self.cat]:
            v[self.elem]['par'][par] = self.__getattribute__(par + 'Dsb').value()

        if self.cat in mc['Load'] + mc['Generator']:
            v[self.elem]['par']['Vn'] = [self.v0Dsb.value()]
        elif self.cat in mc['Transformer']:
            v[self.elem]['par']['Vn'] = [self.v0Dsb.value(), self.v1Dsb.value()]
        elif self.cat in mc['Node']:
            v[self.elem]['par']['Vn'] = [self.VnDsb.value()]

        # Salvataggio del profilo, dove previsto
        if self.cat in prof_elem:
            if self.scale_RB.isChecked():
                v[self.elem]['par']['profile']['name'] = None
                v[self.elem]['par']['profile']['curve'] = self.scale_DSB.value()
            else:
                # TODO: Impostare il salvataggio del profilo
                pass
        v[self.elem]['par']['out-of-service'] = self.out_of_service_CkB.isChecked()

        self.relParSave()

        # salvataggio dei dati di anomalia
        if self.cat in ['AC-PV', 'DC-PV', 'AC-Wind', 'DC-Wind', 'AC-BESS', 'DC-BESS']:
            self.anomSave()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # mw = QMainWindow()
    window = ElementProperties()
    # window.ui.setupUi(mw)
    window.show()

    sys.exit(app.exec_())