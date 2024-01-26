import sys
from functools import partial

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *

from variables import v, el_format
import yaml
import os


class Window(QWidget):
    def __init__(self, elem):
        super().__init__(None)

        self.elem = elem
        self.buses = v[elem]['top']['conn']
        self.cat = v[elem]['category']

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

        self.i = 0

        self.mainWidget = QWidget()
        self.mainVBL = QVBoxLayout(self.mainWidget)
        self.mainVBL.setContentsMargins(5, 5, 5, 40)
        self.mainWidget.setMaximumWidth(200)    # Deve avere il valore della larghezza del settore scorrevole

        self.bbWidget = QWidget()
        self.bbWidget.setStyleSheet(u"background-color: rgb(0, 0, 31); border-radius: 10px;")
        self.bbWidget.setMaximumWidth(180)

        self.parWidget = QWidget()
        self.parWidget.setStyleSheet(u"background-color: rgb(0, 31, 0); border-radius: 10px;")
        self.parWidget.setMaximumWidth(180)

        self.bottomWidget = QWidget()
        self.bottomWidget.setMaximumWidth(180)

        self.mainVBL.addWidget(self.bbWidget)
        self.mainVBL.addWidget(self.parWidget)
        self.mainVBL.addWidget(self.bottomWidget, 0, Qt.AlignBottom)
        self.parWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)

        self.bbGL = QGridLayout(self.bbWidget)
        self.parGL = QGridLayout(self.parWidget)
        self.bottomHBL = QHBoxLayout(self.bottomWidget)


        self.bbFont = QFont()
        self.bbFont.setPointSize(9)
        self.bbFont.setBold(True)

        self.no_LBL = QLabel()
        self.no_LBL.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        # self.no_LBL.setStyleSheet(u"background-color: rgb(0, 255, 31);")

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

        for i in range(len(v[elem]['top']['conn'])):
            # print(elem)
            node = v[elem]['top']['conn'][i]

            # self.__setattr__('node' + str(i) + '_LBL', QLabel('Node ' + str(i)))
            self.__setattr__('node' + str(i) + '_LBL', QLabel(node_labels[i]))

            self.bbGL.addWidget(self.__getattribute__('node' + str(i) + '_LBL'), i, 0)
            self.__getattribute__('node' + str(i) + '_LBL').setMinimumSize(QSize(0, 25))

            self.__setattr__('node' + str(i) + '_BTN', QPushButton())
            self.__setattr__('node' + str(i) + '_CB', QComboBox())
            # self.__getattribute__('node' + str(i) + '_BTN').setText(node)
            self.bbGL.addWidget(self.__getattribute__('node' + str(i) + '_BTN'), i, 1)
            self.__getattribute__('node' + str(i) + '_BTN').setFont(self.bbFont)
            self.__getattribute__('node' + str(i) + '_BTN').setStyleSheet(u"text-align: left;")
            self.__getattribute__('node' + str(i) + '_BTN').clicked.connect(partial(self.bb_selected, i))

            self.bbGL.addWidget(self.no_LBL, i, 2)

            # nodes = []
            #
            # for el in v:
            #     if v[el]['category'] == 'Node' and el != node:
            #         nodes.append(el)
            # nodes.sort()
            # nodes = [node] + nodes

            # self.__getattribute__('node' + str(i) + '_CB').clear()
            # self.__getattribute__('node' + str(i) + '_CB').addItems(nodes)
            self.bbGL.addWidget(self.__getattribute__('node' + str(i) + '_CB'), i, 1)
            self.__getattribute__('node' + str(i) + '_CB').activated.connect(partial(self.bb_changed, i, None))

            # self.__getattribute__('node' + str(i) + '_CB').hide()

            # self.__getattribute__('node' + str(i) + '_CB').activated.connect(partial(self.bb_changed, i))
            # TODO generalizzare le funzioni self.bb_changed e self.bb_selected

        for i in range(len(v[elem]['top']['conn'])):
            node = v[elem]['top']['conn'][i]
            self.bb_changed(i=i, node=node)

        # self.node0_cap_LBL = QLabel('Node 0: ')
        # # self.node0_LBL = QLabel(v[elem]['top']['conn'][0])
        # self.bbGL.addWidget(self.node0_cap_LBL, 0, 0)
        # # self.bbGL.addWidget(self.node0_LBL, 0,1)
        # # self.node0_LBL.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        # # self.node0_LBL.setFont(self.bbFont)
        # # self.bbWidget.mouseDoubleClickEvent = partial(self.bb_selected, 'node0')
        # #
        # #
        # self.node0_BTN = QPushButton()
        # self.node0_BTN.setText('mod.')
        # self.bbGL.addWidget(self.node0_BTN, 0, 1)
        # # self.node0_BTN.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        # self.node0_BTN.setFont(self.bbFont)
        # # self.node0_BTN.ali
        #
        # self.node0_BTN.clicked.connect(partial(self.bb_selected, 'node0'))
        # # self.node0_BTN.mouseDoubleClickEvent = partial(self.bb_selected)
        # self.no_LBL = QLabel()
        # self.no_LBL.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        # self.no_LBL.setStyleSheet(u"background-color: rgb(0, 255, 31);")
        #
        # self.bbGL.addWidget(self.no_LBL, 0, 2)
        # #
        # # if len(v[elem]['top']['conn']) == 2:
        # #     self.bbGL.addItem(QSpacerItem(10, 10))
        # #     self.node1_cap_LBL = QLabel('Node 1: ')
        # #     self.node1_LBL = QLabel(v[elem]['top']['conn'][1])
        # #     self.bbGL.addWidget(self.node1_cap_LBL, 2, 0)
        # #     self.bbGL.addWidget(self.node1_LBL, 2, 1)
        # #     self.node1_LBL.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        # #     self.node1_LBL.setFont(self.bbFont)
        # #     # self.node1_LBL.mouseDoubleClickEvent = partial(self.bb_selected, 'node1')

        i = 0

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
                self.__getattribute__('v' + str(b) + '_DSB').setValue(v[self.buses[b]]['par']['Vn'])
                self.__getattribute__('v' + str(b) + '_DSB').setDisabled(True)
                self.__getattribute__('v' + str(b) + '_DSB').setStyleSheet(u"background-color: rgb(95, 95, 95)")

                self.__getattribute__('v' + str(b) + '_LBL').setAlignment(Qt.AlignRight |
                                                                          Qt.AlignTrailing | Qt.AlignVCenter)
                # a = QDoubleSpinBox()
                # a.setDisabled(True)

            spacer1 = QSpacerItem(20, 20, QSizePolicy.Fixed)
            self.parGL.addItem(spacer1, i, 0)
            i += 1

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
            self.__getattribute__(par + '_DSB').setValue(v[elem]['par'][par])

            self.__getattribute__(par + '_LBL').setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        # creazione della parte dei profili, se previsto
        if self.cat in ['AC-Load', 'DC-Load', 'AC-Wind', 'DC-Wind', 'BESS', 'PV']:
            # distanziatore
            spacer1 = QSpacerItem(20, 20, QSizePolicy.Fixed)
            self.parGL.addItem(spacer1, i, 0)
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
                self.scale_DSB.setValue(v[elem]['par']['profile']['curve'])
                self.scale_RB.setChecked(True)
            else:
                self.scale_DSB.setDisabled(True)
                self.profile_RB.setChecked(True)
            # -----------------------------------------------

        # distanziatore
        spacer1 = QSpacerItem(20, 20, QSizePolicy.Fixed)
        self.parGL.addItem(spacer1, i, 0)
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

        # creazione dei pulsanti
        self.save_BTN = QPushButton('Salva')
        self.cancel_BTN = QPushButton('Annulla')
        self.pb_format(self.save_BTN, min_h=25)
        self.pb_format(self.cancel_BTN, min_h=25)
        self.save_BTN.clicked.connect(self.save_par)

        self.bottomHBL.addWidget(self.save_BTN)
        spacer2 = QSpacerItem(20, 20, QSizePolicy.Fixed)
        self.bottomHBL.addItem(spacer2)
        self.bottomHBL.addWidget(self.cancel_BTN)

        # creazione della scrollbar, se il settore fosse troppo lungo
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.mainWidget)
        self.scroll.setWidgetResizable(True)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.scroll)
        self.setLayout(self.layout)

    def bb_selected(self, i=0, event2=None):
        # print('clicked ', i)
        # node = self.__getattribute__(side + '_BTN').text()
        # print('bb_selected')
        # self.node0_BTN.deleteLater()
        self.__getattribute__('node' + str(i) + '_BTN').hide()
        # self.__getattribute__(side + '_BTN').deleteLater()
        # self.no_LBL.deleteLater()

        # nodes = [self.node0_BTN.text()]
        # nodes = []
        # for el in v:
        #     if v[el]['category'] == 'Node' and el != node:
        #         nodes.append(el)
        #
        # print('list: ', nodes)
        # nodes.sort()
        #
        # nodes = [node] + nodes
        #
        # print('list: ', nodes)

        # self.node0_CB = QComboBox()
        self.__getattribute__('node' + str(i) + '_CB').show()
        # self.node0_CB.clear()
        # self.node0_CB.addItems(nodes)
        # self.bbGL.addWidget(self.node0_CB, 0, 1)

        # self.__getattribute__('node' + str(i) + '_CB').activated.connect(partial(self.bb_changed, i, None))
        # self.node0_CB.item
        pass

    def bb_changed(self, i=0, node=None, event=None):
        if not node:
            node = self.__getattribute__('node' + str(i) + '_CB').currentText()

        self.buses[i] = node

        if self.cat in ['AC-Line', 'DC-Line']:
            if i == 0 and v[self.buses[0]]['par']['Vn'] != v[self.buses[1]]['par']['Vn']:
                self.buses[1] = None
                self.__getattribute__('node1_BTN').setText('-')
                pass

        self.__getattribute__('node' + str(i) + '_BTN').setText(node)
        self.__getattribute__('node' + str(i) + '_BTN').show()

        for j in range(len(self.buses)):
            nodes = self.bb_list(j, node)

            try:
                self.__getattribute__('node' + str(j) + '_CB').clear()
                self.__getattribute__('node' + str(j) + '_CB').addItems(nodes)
                self.__getattribute__('node' + str(j) + '_CB').hide()
            except AttributeError:
                pass

        try:
            self.__getattribute__('v' + str(i) + '_DSB').setValue(v[node]['par']['Vn'])
        except AttributeError:
            pass

    def bb_list(self, i, node):
        nodes = []

        if self.cat in ['2W-Transformer']:
            if i == 0:
                for el in v:
                    if (v[el]['category'] == 'AC-Node' and el not in self.buses and
                            v[el]['par']['Vn'] > v[self.buses[1]]['par']['Vn']):
                        nodes.append(el)
            else:
                for el in v:
                    if (v[el]['category'] == 'AC-Node' and el not in self.buses and
                            v[el]['par']['Vn'] < v[self.buses[0]]['par']['Vn']):
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
                            v[el]['par']['Vn'] > v[self.buses[1]]['par']['Vn']):
                        nodes.append(el)
            else:
                for el in v:
                    if (v[el]['category'] == 'DC-Node' and el not in self.buses and
                            v[el]['par']['Vn'] < v[self.buses[0]]['par']['Vn']):
                        nodes.append(el)

        elif self.cat in ['AC-Load', 'AC-Wind', 'Diesel-Motor', 'AC-Line']:
            for el in v:
                if v[el]['category'] == 'AC-Node' and el not in self.buses:
                    nodes.append(el)

        elif self.cat in ['DC-Load', 'DC-Wind', 'BESS', 'PV', 'DC-Line']:
            for el in v:
                if v[el]['category'] == 'DC-Node' and el not in self.buses:
                    nodes.append(el)

        nodes.sort()
        nodes = [self.buses[i]] + nodes

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

        # print(node, nodes)
        return nodes

    # salvataggio dei dati
    def save_par(self):
        for par in el_format[self.cat]:
            v[self.elem]['par'][par] = self.__getattribute__(par + '_DSB').value()
            # print(par + ': ' + str(v[self.elem]['par'][par]))

        if self.cat in ['AC-Load', 'DC-Load', 'AC-Wind', 'DC-Wind', 'BESS', 'PV']:
            if self.scale_RB.isChecked():
                v[self.elem]['par']['profile']['name'] = None
                v[self.elem]['par']['profile']['curve'] = self.scale_DSB.value()
                # print('scale' + ': ' + str(v[self.elem]['par']['profile']['curve']))
            else:
                pass
        v[self.elem]['par']['out-of-service'] = self.out_of_service_CkB.isChecked()

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
                           u"background-color: rgb(0, 0, 0); border: solid;" # border-style: outset;"
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
