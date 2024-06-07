try:
    from UI.ui_test_elementeProperties import *
except:
    from ui_test_elementeProperties import *

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

from variables import v, el_format, mc, el_lfresults


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

        self.ui.relWgt.setMaximumHeight(20)

        self.fillLfPar()

    def fillLfPar(self):
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
                self.dsb_format(self.__getattribute__('v' + str(b) + 'Dsb'), decimals=3)
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

        # -- Preparazione delle caselle dei paramerti -----------------------------------------------------------------
        for par in el_format[self.cat]:
            self.__setattr__(par + 'Lbl', QLabel(par))
            self.__setattr__(par + 'Dsb', QDoubleSpinBox(None))
            self.__setattr__(par + 'UnitLbl', QLabel(el_format[self.cat][par]['unit']))

            self.ui.lfParGL.addWidget(self.__getattribute__(par + 'Lbl'), line, 0)
            self.ui.lfParGL.addWidget(self.__getattribute__(par + 'Dsb'), line, 1)
            self.ui.lfParGL.addWidget(self.__getattribute__(par + 'UnitLbl'), line, 2)
            i += 1

            # formattazione e popolazione dei campi
            self.dsb_format(self.__getattribute__(par + 'Dsb'), minimum=el_format[self.cat][par]['min'],
                            maximum=el_format[self.cat][par]['max'], decimals=el_format[self.cat][par]['decimal'])
            self.__getattribute__(par + 'Lbl').setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

            if isinstance(v[self.elem]['par'][par], list):
                self.__getattribute__(par + 'Dsb').setValue(v[self.elem]['par'][par][0])
            else:
                self.__getattribute__(par + 'Dsb').setValue(v[self.elem]['par'][par])

            line += 1
        # -------------------------------------------------------------------------------------------------------------

        # -- creazione della parte dei profili, se previsto ----------------------------------------------------------
        if self.cat in ['AC-Load', 'DC-Load', 'AC-Wind', 'DC-Wind', 'BESS', 'PV']:
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
            self.dsb_format(self.scale_DSB, 0, 1, 4)
            self.scale_LBL.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

            if v[self.elem]['par']['profile']['name'] is None:
                print(v[self.elem]['par']['profile']['curve'])
                self.scale_DSB.setValue(v[self.elem]['par']['profile']['curve'])
                self.scale_RB.setChecked(True)
                self.scale_DSB.setStyleSheet(u"background-color: rgb(255, 255, 255);"
                                             u"color: rgb(0, 0, 0);")
            else:
                self.scale_DSB.setDisabled(True)
                self.profile_RB.setChecked(True)

                time = datetime.now().hour * 4 + int(datetime.now().minute / 15)
                print('Time = ', time)
                self.scale_DSB.setValue(v[self.elem]['par']['profile']['curve'][time])
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
                print('profile')
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
                self.__getattribute__('node' + str(i) + '_BTN').clicked.connect(partial(self.bb_clicked, i))
                self.__getattribute__('node' + str(i) + '_CB').activated.connect(partial(self.bb_changed, i,
                                                                                         None))

        # Scrittura dei campi node0 e node1
        for i in range(len(v[self.elem]['top']['conn'])):
            self.bb_changed(i=i, node=v[self.elem]['top']['conn'][i])
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

        self.ui.savePLS.clicked.connect(self.save_par)

        pass

    def profileCheck(self):
        self.dsb_format(self.scale_DSB, 0, 1, 4)
        self.scale_LBL.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        if isinstance(v[self.elem]['par']['profile']['curve'], list):
            time = datetime.now().hour * 4 + int(datetime.now().minute / 15)
            value = v[self.elem]['par']['profile']['curve'][time]
        else:
            value = v[self.elem]['par']['profile']['curve']
        self.scale_DSB.setValue(value)

        # if v[self.elem]['par']['profile']['name'] is None or self.scale_RB.isChecked():
        if self.scale_RB.isChecked():
            # print(v[self.elem]['par']['profile']['curve'])
            # self.scale_DSB.setValue(v[self.elem]['par']['profile']['curve'])
            # self.scale_RB.setChecked(True)
            self.scale_DSB.setStyleSheet(u"background-color: rgb(255, 255, 255);"
                                         u"color: rgb(0, 0, 0);")
            self.scale_DSB.setDisabled(False)
        else:
            self.scale_DSB.setDisabled(True)
            # self.profile_RB.setChecked(True)

            # time = datetime.now().hour * 4 + int(datetime.now().minute / 15)
            # print('Time = ', time)
            # self.scale_DSB.setValue(v[self.elem]['par']['profile']['curve'][time])
            self.scale_DSB.setStyleSheet(u"background-color: rgb(95, 95, 95)")
        #
        # # self.profile_RB.toggled.disconnect()
        # # self.scale_RB.toggled.disconnect()
        # if self.profile_RB.isChecked():
        #     if not v[self.elem]['par']['profile']['name']:
        #         print('apri selezione profilo')
        #
        #     # if 'profile' in v[self.elem]['par']:
        #     #     if v[self.elem]['par']['profile']['name']:
        #     else:
        #         self.profilePlotWgtCreate()
        #         # self.ui.lfVL.addWidget(self.profileWidget)
        #         self.ui.lfVL.insertWidget(3, self.profileWidget)
        #         print('profile')
        # else:
        #     # self.ui.lfVL.removeWidget(self.profileWidget)
        #
        #     # check = self.ui.lfVL.itemAt(3).widget() == self.profileWidget
        #     # print(self.profileWidget)
        #     # print(self.ui.lfVL.itemAt(3))
        #     # print(self.ui.lfVL.itemAt(3).widget())
        #     # print(self.ui.lfVL.itemAt(3).widget)
        #     #
        #     try:
        #         self.profileWidget.deleteLater()
        #     except AttributeError:
        #         pass
        #     # print('verifica profile widget', check)
        #     # if self.profileWidget in self():
        #     #     self.ui.lfVL.itemAt(3).widget().deleteLater()
        #     #     self.profileWidget.deleteLater()
        #     # print('Scale')
        #
        #     # try:
        #     #     # self.profileWidget.deleteLater()
        #     #     self.ui.lfVL.removeWidget(3)
        #     # except:
        #     #     print('non riesco a cancellare')
        #     #     pass
        # # self.profile_RB.toggled.connect(self.profileCheck)
        # # self.scale_RB.toggled.connect(self.profileCheck)

    def profilePlotWgtCreate(self):
        font = {
            'weight': 'normal',
            'size': 4
        }

        matplotlib.rc('font', **font)
        self.canvas1 = FigureCanvas(plt.Figure(figsize=(1.7, 1.4)))
        self.ax = self.canvas1.figure.subplots()

        # a = range(0, 24)
        # b = a/4
        # print('operazione')
        # print([a/4 for a in range(0, 96)])
        # print(v[self.elem]['par']['profile']['curve'])
        self.ax.plot([a/4 for a in range(0, 96)], v[self.elem]['par']['profile']['curve'])  # TODO: da correggere: inserire i dati reali

        self.ax.set_title('Profilo')
        self.ax.set_ylim([0, 1.05])
        self.ax.set_xlim([0, 24])
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
        self.pb_format(self.profileBtn, min_h=20)

        self.profWgtVBL.addWidget(self.profileBtn)

    def profileWgtRefresh(self):
        self.ui.lfVL.itemAt(3).widget().deleteLater()
        self.profileWidget.deleteLater()
        self.profilePlotWgtCreate()
        self.ui.lfVL.insertWidget(3, self.profileWidget)

    # azioni da eseguire alla richiesta di modifica del nodo di connessione
    def bb_clicked(self, i=0, event2=None):
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

    def bb_changed(self, i=0, node=None, event=None):
        if not node:
            node = self.__getattribute__('node' + str(i) + '_CB').currentText()

        self.buses[i] = node

        # Se cambio la prima busbar di una linea, verifico se la tensione della seconda busbar è coerente,
        #     altrimenti deve essere cambiata
        if self.cat in ['AC-Line', 'DC-Line'] and self.buses[1]:
            if i == 0 and v[self.buses[0]]['par']['Vn'] != v[self.buses[1]]['par']['Vn']:
                self.buses[1] = None
                self.__getattribute__('node1_BTN').setText('-')

        self.__getattribute__('node' + str(i) + '_BTN').setText(node)
        self.__getattribute__('node' + str(i) + '_BTN').show()

        # aggiornamento della lista delle busbar coerenti per ogni nodo
        for j in range(len(self.buses)):
            nodes = self.bb_list(j, node)
            self.__getattribute__('node' + str(j) + '_CB').clear()
            self.__getattribute__('node' + str(j) + '_CB').addItems(nodes)
            self.__getattribute__('node' + str(j) + '_CB').hide()

        # Scrittura del voltaggio dell'elemento, in base al Nodo a cui è connesso
        # try:
        if self.cat not in mc['Vsource'] + mc['Node']:
            print(self.elem, i, self.buses)
            self.__getattribute__('v' + str(i) + 'Dsb').setValue(v[node]['par']['Vn'][0])
        # except AttributeError:
        #     pass

        if self.cat in mc['Line']:
            self.ui.savePLS.setEnabled(self.__getattribute__('node1_BTN').text() != '-')
            if self.ui.savePLS.isEnabled():
                # self.save_BTN.setStyleSheet(u"background-color: rgb(255, 255, 255)")
                self.pb_format(self.ui.savePLS, min_h=25)

            else:
                # self.save_BTN.setStyleSheet(u"background-color: rgb(95, 95, 95)")
                self.pb_disabled(self.ui.savePLS, min_h=25)

    # Definizione dell'elenco delle BusBar ammissibili
    def bb_list(self, i, node):
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

        elif self.cat in ['AC-Load', 'AC-Wind', 'Diesel-Motor', 'AC-Line']:
            for el in v:
                if v[el]['category'] == 'AC-Node' and el not in self.buses:
                    nodes.append(el)

        elif self.cat in ['DC-Load', 'DC-Wind', 'BESS', 'PV', 'DC-Line']:
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

    def fillLfRes(self):
        spacer = QSpacerItem(10, 10, QSizePolicy.Fixed)
        line = 0
        # -- Preparazione delle caselle dei paramerti -----------------------------------------------------------------
        for par in el_lfresults[self.cat]:
            self.__setattr__(par + 'Lbl', QLabel(par))
            self.__setattr__(par + 'Dsb', QDoubleSpinBox(None))
            self.__setattr__(par + 'UnitLbl', QLabel(el_format[self.cat][par]['unit']))

            self.ui.lfParGL.addWidget(self.__getattribute__(par + 'Lbl'), line, 0)
            self.ui.lfParGL.addWidget(self.__getattribute__(par + 'Dsb'), line, 1)
            self.ui.lfParGL.addWidget(self.__getattribute__(par + 'UnitLbl'), line, 2)
            # i += 1

            # formattazione e popolazione dei campi
            self.dsb_format(self.__getattribute__(par + 'Dsb'), minimum=el_format[self.cat][par]['min'],
                            maximum=el_format[self.cat][par]['max'], decimals=el_format[self.cat][par]['decimal'])
            self.__getattribute__(par + 'Lbl').setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

            if isinstance(v[self.elem]['par'][par], list):
                self.__getattribute__(par + 'Dsb').setValue(v[self.elem]['par'][par][0])
            else:
                self.__getattribute__(par + 'Dsb').setValue(v[self.elem]['par'][par])

            line += 1
        # -------------------------------------------------------------------------------------------------------------
        pass


    # formattazione dei DoubleSPinBox
    def dsb_format(self, item, minimum=0, maximum=9999.99, decimals=2, step=0.1):
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
    def pb_format(self, item, min_w=0, min_h=0):
        item.setStyleSheet(u"QPushButton {"
                           u"color: rgb(255, 255, 255);"
                           u"background-color: rgb(0, 0, 0); border: solid;"  # border-style: outset;"
                           u"border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)"
                           u"}"
                           u"QPushButton:pressed {"
                           u"background-color: rgb(64, 64, 64); border-style: inset"
                           u"}")
        item.setMinimumSize(QSize(min_w, min_h))

    def pb_disabled(self, item, min_w=0, min_h=0):
        item.setStyleSheet(u"QPushButton {"
                           u"color: rgb(63, 63, 63);"
                           u"background-color: rgb(31, 31, 31); border: solid;"  # border-style: outset;"
                           u"border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)"
                           u"}"
                           u"QPushButton:pressed {"
                           u"background-color: rgb(64, 64, 64); border-style: inset"
                           u"}")
        item.setMinimumSize(QSize(min_w, min_h))

    def bb_fix(self, elem):
        # Se si modifica la tensione della busbar,
        # bisogna modificare la tensione nominale degli elementi a essa connessa

        # Se l'elemento è un nodo o la rete esterna, e se è cambiata la tensione nomnale
        if self.cat in mc['Node'] + mc['Vsource'] and v[elem]['par']['Vn'] != self.Vn_DSB.value():
            for el in self.bb_link(elem):
                for bb in self.buses:
                    if v[bb]['category'] in mc['Transformer']:
                        for i in range(len(v[bb]['top']['conn'])):
                            if v[bb]['top']['conn'][i] == elem:
                                v[bb]['par']['Vn' + str(i)] = self.Vn_DSB.value()
                        pass
                    else:
                        v[el]['par']['Vn'] = self.Vn_DSB.value()
                        pass

        # Se si modifica la busbar connessa,
        # bisogna modificare anche l'elenco delle connessioni nella vecchia e nella nuova busbar
        elif self.buses != self.old_buses:
            print('Modifica BusBar')
            for b in range(len(self.buses)):
                if self.buses[b] != self.old_buses[b]:
                    v[elem]['par']['Vn' + str(b)] = self.__getattribute__('v' + str(b) + '_DSB').value()
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

    def bb_link(self, busbar):
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
            print(buses)
            print(bb_solved)
        # bb_solved.remove(busbar)
        print(bb_solved, lines_solved)
        return bb_solved

    # salvataggio dei dati dall'interfaccia al dizionario
    def save_par(self):
        self.bb_fix(self.elem)
        # TODO: nel caso di variazione di tensione a busbar correlate, bisogna mettere un alert

        for par in el_format[self.cat]:
            v[self.elem]['par'][par] = self.__getattribute__(par + 'Dsb').value()

        # Salvataggio del profilo, dove previsto
        if self.cat in ['AC-Load', 'DC-Load', 'AC-Wind', 'DC-Wind', 'BESS', 'PV']:
            if self.scale_RB.isChecked():
                v[self.elem]['par']['profile']['name'] = None
                v[self.elem]['par']['profile']['curve'] = self.scale_DSB.value()
                # print('scale' + ': ' + str(v[self.elem]['par']['profile']['curve']))
            else:
                # TODO: Impostare il salvataggio del profilo
                pass
        v[self.elem]['par']['out-of-service'] = self.out_of_service_CkB.isChecked()
        print('salvato')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # mw = QMainWindow()
    window = ElementProperties()
    # window.ui.setupUi(mw)
    window.show()

    sys.exit(app.exec_())