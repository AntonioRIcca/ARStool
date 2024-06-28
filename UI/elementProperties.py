import copy
import sys
from functools import partial

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *

from PySide2.QtCharts import *

from variables import v, el_format, mc
import yaml
import os
from datetime import datetime

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class Window(QWidget):
    def __init__(self, elem):
        super().__init__(None)

        self.elem = elem
        self.old_buses = copy.deepcopy(v[elem]['top']['conn'])
        self.buses = copy.deepcopy(v[elem]['top']['conn'])
        self.cat = v[elem]['category']

        if self.cat in mc['Node']:
            self.bb_link(self.elem)

        spacer = QSpacerItem(20, 20, QSizePolicy.Fixed)
        bottomSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # print(v[elem]['top']['conn'])

        # Creare widget busbar
        # creare elementi busbar
        # settare le azioni degli elementi
        # popolare caselle busbar
        # popolare le liste delle busbar alternative
        #   - Libere per i carichi, i generatori e le BESS, ma devono rispettare le caratteristiche di AC e DC
        #   - Per i trasformatori, devono essere AC e le HV devono avere tensione maggiore delle LV
        #   - Per i convertitori DC-DC, devono essere DC e le HV devono avere tensione maggiore delle LV
        #   - Per i PWM, bisogna rispettare i lati AC e DC
        #   - Per le linee, devono rispettare le caratteristiche AC e DC; il primo nodo è libero, il secondo deve avere
        #       la stessa tensione del primo. Se quella del primo è cambiata, bisogna riscegliere anche il secondo

        # Creazione del widget principale
        self.mainWidget = QWidget()
        self.mainVBL = QVBoxLayout(self.mainWidget)
        self.mainVBL.setContentsMargins(5, 5, 5, 40)
        self.mainWidget.setMaximumWidth(200)    # Deve avere il valore della larghezza del settore scorrevole

        # Creare widget busbar
        self.bbWidget = QWidget()
        self.bbWidget.setStyleSheet(u"background-color: rgb(0, 0, 31); border-radius: 10px;")
        self.bbWidget.setMaximumWidth(180)
        self.bbGL = QGridLayout(self.bbWidget)

        # Creare widget Parametri
        self.parWidget = QWidget()
        self.parWidget.setStyleSheet(u"background-color: rgb(0, 31, 0); border-radius: 10px;")
        self.parWidget.setMaximumWidth(180)
        self.parGL = QGridLayout(self.parWidget)

        # # Creare Widget immagine Profilo
        # profile = False
        # if 'profile' in v[self.elem]['par']:
        #     if v[self.elem]['par']['profile']['name']:
        #         profile = True
        #         self.profileWidget = QWidget()
        #         self.profileWidget.setStyleSheet(u"background-color: rgb(31, 0, 0); border-radius: 10px;")
        #         self.profileWidget.setMaximumHeight(180)
        #         self.profileWidget.setMaximumWidth(180)
        #         self.profWgtVBL = QVBoxLayout(self.profileWidget)
        #         self.profileLbl = QLabel()
        #         self.profilePlotWgtCreate()
        #         self.profileLbl.setPixmap(QPixmap("a.jpg"))
        #         self.profWgtVBL.addWidget(self.profileLbl)
        #         # self.profWgtVBL.addWidget(self.canvas1)
        #
        #         self.profileBtn = QPushButton('Apri profilo')
        #         self.pb_format(self.profileBtn, min_h=20)
        #
        #         self.profWgtVBL.addWidget(self.profileBtn)
        #         print('done')
        # else:
        #     print(1, v[self.elem]['category'])
        #     print(2, mc['Load'] + mc['Generator'])


        # self.profileLbl.setPixmap(QPixmap("_benchmark/grid_models/images/OtherGrid.png"))

        # Creare widget dei pulsanti di fondo
        self.bottomWidget = QWidget()
        self.bottomWidget.setMaximumWidth(180)
        self.bottomHBL = QHBoxLayout(self.bottomWidget)

        # Aggiunta dei widget al widget principale
        self.mainVBL.addWidget(self.bbWidget)
        self.mainVBL.addWidget(self.parWidget)
        if 'profile' in v[self.elem]['par']:
            if v[self.elem]['par']['profile']['name']:
                self.profilePlotWgtCreate()
                print('inserted')
                self.mainVBL.addWidget(self.profileWidget)
        # else:
        #     print(3, v[self.elem]['category'])
        #     print(4, mc['Load'] + mc['Generator'])
        self.mainVBL.addWidget(self.bottomWidget, 0, Qt.AlignBottom)
        self.mainVBL.addItem(bottomSpacer)
        # self.parWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)

        # Scrittura dei parametri
        i = 0
        # -- Preparazione delle caselle V0 e V1 quando serve ---------------------------------------------------------
        if self.cat not in ['AC-Node', 'DC-Node', 'ExternalGrid']:
            for b in range(len(self.buses)):
                self.__setattr__('v' + str(b) + '_LBL', QLabel('V' + str(b)))
                self.__setattr__('v' + str(b) + '_DSB', QDoubleSpinBox(None))
                self.__setattr__('v' + str(b) + '_unit_LBL', QLabel('kV'))

                self.parGL.addWidget(self.__getattribute__('v' + str(b) + '_LBL'), i, 0)
                self.parGL.addWidget(self.__getattribute__('v' + str(b) + '_DSB'), i, 1)
                self.parGL.addWidget(self.__getattribute__('v' + str(b) + '_unit_LBL'), i, 2)
                i += 1

                # formattazione e popolazione dei campi
                self.dsb_format(self.__getattribute__('v' + str(b) + '_DSB'), decimals=3)
                self.__getattribute__('v' + str(b) + '_LBL').setAlignment(Qt.AlignRight |
                                                                          Qt.AlignTrailing | Qt.AlignVCenter)
                self.__getattribute__('v' + str(b) + '_DSB').setValue(v[self.buses[b]]['par']['Vn'][0])

                # Le caselle devono essere disabilitata
                self.__getattribute__('v' + str(b) + '_DSB').setDisabled(True)
                self.__getattribute__('v' + str(b) + '_DSB').setStyleSheet(u"background-color: rgb(95, 95, 95)")
        # ------------------------------------------------------------------------------------------------------------

            self.parGL.addItem(spacer, i, 0)
            i += 1

        # -- Preparazione delle caselle dei paramerti ------ ---------------------------------------------------------
        for par in el_format[self.cat]:
            self.__setattr__(par + '_LBL', QLabel(par))
            self.__setattr__(par + '_DSB', QDoubleSpinBox(None))
            self.__setattr__(par + '_unit_LBL', QLabel(el_format[self.cat][par]['unit']))

            self.parGL.addWidget(self.__getattribute__(par + '_LBL'), i, 0)
            self.parGL.addWidget(self.__getattribute__(par + '_DSB'), i, 1)
            self.parGL.addWidget(self.__getattribute__(par + '_unit_LBL'), i, 2)
            i += 1

            # formattazione e popolazione dei campi
            self.dsb_format(self.__getattribute__(par + '_DSB'), minimum=el_format[self.cat][par]['min'],
                            maximum=el_format[self.cat][par]['max'], decimals=el_format[self.cat][par]['decimal'])
            self.__getattribute__(par + '_LBL').setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

            if isinstance(v[elem]['par'][par], list):
                self.__getattribute__(par + '_DSB').setValue(v[elem]['par'][par][0])
            else:
                self.__getattribute__(par + '_DSB').setValue(v[elem]['par'][par])
        # ------------------------------------------------------------------------------------------------------------

        # -- creazione della parte dei profili, se previsto ----------------------------------------------------------
        if self.cat in ['AC-Load', 'DC-Load', 'AC-Wind', 'DC-Wind', 'BESS', 'PV']:
            # distanziatore
            # spacer1 = QSpacerItem(20, 20, QSizePolicy.Fixed)
            self.parGL.addItem(spacer, i, 0)
            i += 1

            # -- creazione ed inserimento degli elementi ----
            self.scale_LBL = QLabel('Scala')
            self.scale_DSB = QDoubleSpinBox()
            self.scale_RB = QRadioButton('Costante')

            self.profile_RB = QRadioButton('Profilo')

            self.parGL.addWidget(self.scale_LBL, i, 0)
            self.parGL.addWidget(self.scale_DSB, i, 1)
            i += 1

            self.parGL.addWidget(self.scale_RB, i, 1)
            i += 1

            self.parGL.addWidget(self.profile_RB, i, 1)
            i += 1

            # formattazione e popolazione degli elementi del profilo
            self.dsb_format(self.scale_DSB, 0, 1, 4)
            self.scale_LBL.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

            if v[elem]['par']['profile']['name'] is None:
                # print(v[elem]['par']['profile']['curve'])
                self.scale_DSB.setValue(v[elem]['par']['profile']['curve'])
                self.scale_RB.setChecked(True)
                self.scale_DSB.setStyleSheet(u"background-color: rgb(255, 255, 255);"
                                             u"color: rgb(0, 0, 0);")
            else:
                self.scale_DSB.setDisabled(True)
                self.profile_RB.setChecked(True)

                time = datetime.now().hour * 4 + int(datetime.now().minute/15)
                # print('Time = ', time)
                self.scale_DSB.setValue(v[elem]['par']['profile']['curve'][time])
                self.scale_DSB.setStyleSheet(u"background-color: rgb(95, 95, 95)")
        # ------------------------------------------------------------------------------------------------------------

        # distanziatore
        # spacer1 = QSpacerItem(20, 20, QSizePolicy.Fixed)
        self.parGL.addItem(spacer, i, 0)
        i += 1

        # casella Out-of-service
        self.out_of_service_LBL = QLabel('OutOfServ')
        self.out_of_service_CkB = QCheckBox()
        self.parGL.addWidget(self.out_of_service_LBL, i, 0)
        self.parGL.addWidget(self.out_of_service_CkB, i, 1)
        self.out_of_service_CkB.setChecked(v[elem]['par']['out-of-service'])
        i += 1

        # distanziatore necessario per riempire il vuoto tra i parametri e i pulsanti
        spacer_wgt = QWidget()
        self.parGL.addWidget(spacer_wgt, i, 0)
        i += 1

        # -- creazione della sezione dei pulsanti --------------------------------------------------------------------
        self.save_BTN = QPushButton('Salva')
        self.cancel_BTN = QPushButton('Annulla')
        self.pb_format(self.save_BTN, min_h=25)
        self.pb_format(self.cancel_BTN, min_h=25)
        self.save_BTN.clicked.connect(self.save_par)

        self.bottomHBL.addWidget(self.save_BTN)
        spacer2 = QSpacerItem(20, 20, QSizePolicy.Fixed)
        self.bottomHBL.addItem(spacer2)
        self.bottomHBL.addWidget(self.cancel_BTN)
        # ------------------------------------------------------------------------------------------------------------

        # -- creazione della sezione delle BusBar --------------------------------------------------------------------
        self.bbFont = QFont()
        self.bbFont.setPointSize(9)
        self.bbFont.setBold(True)

        self.no_LBL = QLabel()
        self.no_LBL.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)

        # definizione dei Label delle busbar
        node_labels = []
        if v[elem]['category'] == 'PWM':
            node_labels = ['AC Node', 'DC Node']
        elif v[elem]['category'] in ['2W-Transformer', 'DC-DC-Converter']:
            node_labels = ['HV Node', 'LV Node']
        elif v[elem]['category'] in ['AC-Line', 'DC-Line', 'AC-Node', 'DC-Node']:
            for i in range(len(v[elem]['top']['conn'])):
                node_labels.append('Node ' + str(i))
        else:
            node_labels = ['Node', '']

        # -- Settaggio dei campi della sezione Busbar  ------------------------------------
        for i in range(len(v[elem]['top']['conn'])):
            self.__setattr__('node' + str(i) + '_LBL', QLabel(node_labels[i]))

            self.bbGL.addWidget(self.__getattribute__('node' + str(i) + '_LBL'), i, 0)
            self.__getattribute__('node' + str(i) + '_LBL').setMinimumSize(QSize(0, 25))

            self.__setattr__('node' + str(i) + '_BTN', QPushButton())
            self.__setattr__('node' + str(i) + '_CB', QComboBox())

            self.bbGL.addWidget(self.__getattribute__('node' + str(i) + '_BTN'), i, 1)
            self.__getattribute__('node' + str(i) + '_BTN').setFont(self.bbFont)
            self.__getattribute__('node' + str(i) + '_BTN').setStyleSheet(u"text-align: left;")

            self.bbGL.addWidget(self.no_LBL, i, 2)

            self.bbGL.addWidget(self.__getattribute__('node' + str(i) + '_CB'), i, 1)
        # ---------------------------------------------------------------------------------

            # settare le azioni degli elementi (se non sono Node o Source)
            if self.cat not in mc['Node'] + mc['Vsource']:
                self.__getattribute__('node' + str(i) + '_BTN').clicked.connect(partial(self.bb_clicked, i))
                self.__getattribute__('node' + str(i) + '_CB').activated.connect(partial(self.bb_changed, i,
                                                                                         None))

        # Scrittura dei campi node0 e node1
        for i in range(len(v[elem]['top']['conn'])):
            self.bb_changed(i=i, node=v[elem]['top']['conn'][i])
        # ------------------------------------------------------------------------------------------------------------

        # creazione della scrollbar, se il settore fosse troppo lungo
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.mainWidget)
        self.scroll.setWidgetResizable(True)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.scroll)
        self.setLayout(self.layout)

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
        self.profileWidget.setStyleSheet(u"background-color: rgb(31, 0, 0); border-radius: 10px;")
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
            self.__getattribute__('v' + str(i) + '_DSB').setValue(v[node]['par']['Vn'][0])
        # except AttributeError:
        #     pass

        if self.cat in mc['Line']:
            self.save_BTN.setEnabled(self.__getattribute__('node1_BTN').text() != '-')
            if self.save_BTN.isEnabled():
                # self.save_BTN.setStyleSheet(u"background-color: rgb(255, 255, 255)")
                self.pb_format(self.save_BTN, min_h=25)

            else:
                # self.save_BTN.setStyleSheet(u"background-color: rgb(95, 95, 95)")
                self.pb_disabled(self.save_BTN, min_h=25)

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

    # salvataggio dei dati dall'interfaccia al dizionario
    def save_par(self):
        self.bb_fix(self.elem)
        # TODO: nel caso di variazione di tensione a busbar correlate, bisogna mettere un alert

        for par in el_format[self.cat]:
            v[self.elem]['par'][par] = self.__getattribute__(par + '_DSB').value()

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
                           u"background-color: rgb(0, 0, 0); border: solid;" # border-style: outset;"
                           u"border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)"
                           u"}"
                           u"QPushButton:pressed {"
                           u"background-color: rgb(64, 64, 64); border-style: inset"
                           u"}")
        item.setMinimumSize(QSize(min_w, min_h))

    def pb_disabled(self, item, min_w=0, min_h=0):
        item.setStyleSheet(u"QPushButton {"
                           u"color: rgb(63, 63, 63);"
                           u"background-color: rgb(31, 31, 31); border: solid;" # border-style: outset;"
                           u"border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)"
                           u"}"
                           u"QPushButton:pressed {"
                           u"background-color: rgb(64, 64, 64); border-style: inset"
                           u"}")
        item.setMinimumSize(QSize(min_w, min_h))

if __name__ == '__main__':
    v = yaml.safe_load(open('C:/Users/anton/PycharmProjects/ARStool/CityArea.yml'))

    App = QApplication()
    window = Window('rs_line')
    window.show()
    sys.exit(App.exec_())
