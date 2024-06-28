# from ui_elementsProfile_dlg import Ui_mainDlg
# from UI.ui_elementsProfile_dlg import Ui_mainDlg
import os
from UI.ui_newItem_Dlg import Ui_Dialog
from UI.elementsProfile import ElementsProfile

from PySide2 import QtGui, QtCore, QtWidgets
# from PyQt5 import QtWidgets, QtGui, QtCore

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from variables import *
from dictInitialize import *
import copy
from functools import partial


class NewItem(QtWidgets.QDialog):
    def __init__(self):
        super(NewItem, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.created = False

        self.ui.nameLE.setVisible(False)
        for w in ['node', 'par', 'pictureProf', 'scaleProf', 'serv']:
            self.ui.__getattribute__(w + 'Wgt').setVisible(False)

        self.ui.nameLBL.mouseDoubleClickEvent = self.rename
        self.ui.nameLE.installEventFilter(self)
        self.ui.node1CB.currentIndexChanged.connect(partial(self.bb_changed, j=1))
        self.ui.node2CB.currentIndexChanged.connect(partial(self.bb_changed, j=2))
        self.ui.profScaleProfRB.toggled.connect(self.prof_selected)
        self.ui.profOpenBtn.clicked.connect(self.prof_open)
        self.ui.saveBtn.clicked.connect(self.save)
        self.ui.calcelBtn.clicked.connect(self.close)

        self.type_populate()
        self.type_selected()

    def rename(self, event):
        self.ui.nameLBL.setVisible(False)
        self.ui.nameLE.setVisible(True)
        self.ui.nameLE.setText(self.ui.nameLBL.text())
        self.ui.nameLE.selectAll()
        self.ui.nameLE.setFocus()

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj is self.ui.nameLE:
            if event.key() == QtCore.Qt.Key_Return and self.ui.nameLE.hasFocus():
                if self.ui.nameLE.text() in list(v.keys()):
                    QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Attenzione',
                                                  'Nome elemento già presente')
                    self.rename(None)
                else:

                    self.ui.nameLBL.setVisible(True)
                    self.ui.nameLE.setVisible(False)
                    self.ui.nameLBL.setText(self.ui.nameLE.text())
        return super().eventFilter(obj, event)

    def type_populate(self):
        typelist = list(el_format.keys() - ['ExternalGrid'])
        typelist.sort()
        self.ui.typeCB.addItems(typelist)
        self.ui.typeCB.currentIndexChanged.connect(self.type_selected)

    def type_selected(self):
        self.cat = self.ui.typeCB.currentText()

        for item in range(self.ui.parGL.count()):
            try:
                self.ui.parGL.itemAt(item).widget().deleteLater()
            except AttributeError:
                pass

        line = 0

        # -- Preparazione delle caselle dei paramerti -----------------------------------------------------------------
        for par in el_format[self.cat]:
            self.ui.__setattr__(par + 'ParLbl', QtWidgets.QLabel(par))
            self.ui.__setattr__(par + 'ParDsb', QtWidgets.QDoubleSpinBox(None))
            self.ui.__setattr__(par + 'ParUnitLbl', QtWidgets.QLabel(el_format[self.cat][par]['unit']))

            self.ui.parGL.addWidget(self.ui.__getattribute__(par + 'ParLbl'), line, 1)
            self.ui.parGL.addWidget(self.ui.__getattribute__(par + 'ParDsb'), line, 2)
            self.ui.parGL.addWidget(self.ui.__getattribute__(par + 'ParUnitLbl'), line, 3)

            # formattazione e popolazione dei campi
            self.dsb_format(self.ui.__getattribute__(par + 'ParDsb'), minimum=el_format[self.cat][par]['min'],
                            maximum=el_format[self.cat][par]['max'], decimals=el_format[self.cat][par]['decimal'])
            self.ui.__getattribute__(par + 'ParLbl').setAlignment(QtCore.Qt.AlignRight |
                                                               QtCore.Qt.AlignTrailing |
                                                               QtCore.Qt.AlignVCenter)
            self.ui.__getattribute__(par + 'ParDsb').setValue(el_format[self.cat][par]['default'])

            line += 1
        # -------------------------------------------------------------------------------------------------------------

        self.ui.parWgt.setVisible(True)
        self.ui.nodeWgt.setVisible(self.cat not in ['AC-Node', 'DC-Node'])
        for elem in ['node2CB', 'node2Lbl', 'vnode2Lbl', 'vnode2Dsb']:
            self.ui.__getattribute__(elem).setVisible(self.cat not in ['AC-Load', 'DC-Load', 'AC-Wind', 'DC-Wind',
                                                                       'PV', 'Bess'])
        self.ui.servWgt.setVisible(True)
        self.ui.scaleProfWgt.setVisible(self.cat in ['AC-Load', 'DC-Load', 'AC-Wind', 'DC-Wind', 'PV', 'Bess'])

        self.bb_changed(j=1)
        self.bb_changed(j=2)

    def bb_changed(self, sel=0, j=0):
        nodes = [None, None]

        # in nodes rimane None il nodo non modificato, mentre viene popolato il nodo appenna selezionato
        if j > 0:
            # i è il nodo non selezionato
            il = [1, 2]
            il.remove(j)
            i = il[0]

            nodes[j-1] = self.ui.__getattribute__('node' + str(j) + 'CB').currentText()

        # n[1] e n[2] contengono le liste dei nodi 1 e 2
        n = dict()
        n[1], n[2] = self.bb_read(self.cat, nodes[0], nodes[1])

        # -- aggiornamento dell'elenco diverso dal nodo appena cambiato -------------------------
        self.ui.__getattribute__('node' + str(i) + 'CB').currentIndexChanged.disconnect()
        old = self.ui.__getattribute__('node' + str(i) + 'CB').currentText()    # selezione precedente
        self.ui.__getattribute__('node' + str(i) + 'CB').clear()
        self.ui.__getattribute__('node' + str(i) + 'CB').addItems(n[i])

        # Se la selezione precedente è ancora presente nella lista, deve essere selezionata
        if old in n[i]:
            self.ui.__getattribute__('node' + str(i) + 'CB').setCurrentText(old)
        self.ui.__getattribute__('node' + str(i) + 'CB').currentIndexChanged.connect(partial(self.bb_changed, j=i))
        # ---------------------------------------------------------------------------------------

        # Scrittura del valore della tensione del nodo
        for k in [1, 2]:
            if self.ui.__getattribute__('node' + str(k) + 'CB').currentText() != '':
                self.ui.__getattribute__('vnode' + str(k) + 'Dsb').setValue(
                    v[self.ui.__getattribute__('node' + str(k) + 'CB').currentText()]['par']['Vn'][0])
            else:
                self.ui.__getattribute__('vnode' + str(k) + 'Dsb').setValue(0)

    def bb_read(self, cat, node1=None, node2=None):
        print(node1, node2)

        v_ac = dict()
        v_dc = dict()
        n_ac = []
        n_dc = []
        for elem in v:
            if v[elem]['category'] == 'AC-Node':
                n_ac.append(elem)
                if v[elem]['par']['Vn'][0] not in list(v_ac.keys()):
                    v_ac[v[elem]['par']['Vn'][0]] = []
                v_ac[v[elem]['par']['Vn'][0]].append(elem)
            elif v[elem]['category'] == 'DC-Node':
                n_dc.append(elem)
                if v[elem]['par']['Vn'][0] not in list(v_dc.keys()):
                    v_dc[v[elem]['par']['Vn'][0]] = []
                v_dc[v[elem]['par']['Vn'][0]].append(elem)

        n1, n2 = [], []

        if cat == '2W-Transformer':
            n1 = copy.deepcopy(n_ac)
            n2 = copy.deepcopy(n_ac)

            for n in n_ac:
                if ((node2 and v[n]['par']['Vn'][0] <= v[node2]['par']['Vn'][0]) or
                        v[n]['par']['Vn'][0] == min(list(v_ac.keys()))):
                    n1.remove(n)
                if ((node1 and v[n]['par']['Vn'][0] >= v[node1]['par']['Vn'][0]) or
                        v[n]['par']['Vn'][0] == max(list(v_ac.keys()))):
                    n2.remove(n)

        elif cat == 'AC-Line':
            n1 = copy.deepcopy(n_ac)
            n2 = copy.deepcopy(n_ac)

            for n in n_ac:
                # if node2 and v[n]['par']['Vn'][0] != v[node2]['par']['Vn'][0]:
                #     n1.remove(n)
                if node1 and v[n]['par']['Vn'][0] != v[node1]['par']['Vn'][0]:
                    n2.remove(n)

            if node1:
                n2.remove(node1)
            elif node2:
                n1.remove(node2)

        elif cat == 'DC-Line':
            n1 = copy.deepcopy(n_dc)
            n2 = copy.deepcopy(n_dc)

            for n in n_dc:
                if node2 and v[n]['par']['Vn'][0] != v[node2]['par']['Vn'][0]:
                    n1.remove(n)
                if node1 and v[n]['par']['Vn'][0] != v[node1]['par']['Vn'][0]:
                    n2.remove(n)

        elif cat == 'DC-DC-Converter':
            n1 = copy.deepcopy(n_dc)
            n2 = copy.deepcopy(n_dc)

            for n in n_dc:
                if ((node2 and v[n]['par']['Vn'][0] <= v[node2]['par']['Vn'][0]) or
                        v[n]['par']['Vn'][0] == min(list(v_dc.keys()))):
                    n1.remove(n)
                if ((node1 and v[n]['par']['Vn'][0] >= v[node1]['par']['Vn'][0]) or
                        v[n]['par']['Vn'][0] == max(list(v_dc.keys()))):
                    n2.remove(n)

        elif cat == 'PWM':
            n1 = copy.deepcopy(n_ac)
            n2 = copy.deepcopy(n_dc)

        elif cat in ['AC-Load', 'AC-Wind']:
            n1 = copy.deepcopy(n_ac)
        elif cat in ['DC-Load', 'DC-Wind']:
            n1 = copy.deepcopy(n_dc)

        try:
            n1.sort(), n2.sort()
        except AttributeError:
            pass

        # print(n1)
        # print(n2)

        return n1, n2

    def prof_selected(self):
        self.ui.pictureProfWgt.setVisible(self.ui.profScaleProfRB.isChecked())
        self.ui.scaleProfDsb.setEnabled(not self.ui.profScaleProfRB.isChecked())
        # print('Profilo')

    def prof_open(self):
        if '_temp' not in list(v.keys()):
            v['_temp'] = {'par': {'profile': {'curve': 1, 'name': None, }}}

        prof_popup = ElementsProfile('_temp')

        if prof_popup.exec_():
            # print('popup')
            pass
        # print(v['_temp']['par']['profile']['curve'])
        if v['_temp']['par']['profile']['name']:
            self.profilePlotWgtCreate()

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
        self.ax.plot([a/4 for a in range(0, 96)], v['_temp']['par']['profile']['curve'])  # TODO: da correggere: inserire i dati reali

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
        # self.profileWidget = QtWidgets.QWidget()
        # self.profileWidget.setStyleSheet(u"background-color: rgb(0, 0, 48); border-radius: 10px;")
        # self.profileWidget.setMaximumHeight(180)
        # self.profileWidget.setMaximumWidth(180)
        # self.profWgtVBL = QtWidgets.QVBoxLayout(self.profileWidget)
        self.profileLbl = QtWidgets.QLabel()

        self.profileLbl.setPixmap(QtGui.QPixmap("a.jpg"))
        # self.profWgtVBL.addWidget(self.profileLbl)
        # self.profWgtVBL.addWidget(self.canvas1)

        # self.profileBtn = QtWidgets.QPushButton('Apri profilo')
        # self.pb_format(self.profileBtn, min_h=20)
        #
        # self.profWgtVBL.addWidget(self.profileBtn)
        self.ui.pictureProfVL.itemAt(0).widget().deleteLater()
        self.ui.pictureProfVL.insertWidget(0, self.profileLbl)
        # self.ui.pictureProfVL.add

    def save(self):
        self.el = self.ui.nameLBL.text()
        dict_initialize(self.el, self.cat)
        if self.cat in mc['Line']:
            v[self.el]['top']['conn'] = [self.ui.node1CB.currentText(), self.ui.node2CB.currentText()]
            # TODO: categoria linea
        elif self.cat in mc['Transformer']:
            v[self.el]['top']['conn'] = [self.ui.node1CB.currentText(), self.ui.node2CB.currentText()]
        elif self.cat in mc['Node']:
            pass

        else:
            v[self.el]['top']['conn'] = [self.ui.node1CB.currentText()]

        for par in el_format[self.cat]:
            v[self.el]['par'][par] = self.ui.__getattribute__(par + 'ParDsb').value()

        v[self.el]['par']['out-of-service'] = self.ui.servCkB.isChecked()

        if  self.cat not in mc['Node']:
            v[self.el]['par']['Vn'] = []
            for b in v[self.el]['top']['conn']:
                v[self.el]['par']['Vn'].append(v[b]['par']['Vn'])

        if '_temp' in list(v.keys()):
            v[self.el]['par']['profile'] = copy.deepcopy(v['_temp']['par']['profile'])
            if self.ui.constScaleProfRB.isChecked():
                v[self.el]['par']['profile']['curve'] = self.ui.scaleProfDsb.value()
            del v['_temp']

        print(v[self.el])
        self.created = True
        self.close()

    # def close(self):
    #     self.close()

    # formattazione dei DoubleSPinBox
    def dsb_format(self, item, minimum=0, maximum=9999.99, decimals=2, step=0.1):
        item.setMinimum(minimum)
        item.setMaximum(maximum)
        item.setDecimals(decimals)
        item.setSingleStep(step)

        item.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        item.setStyleSheet(u"background-color: rgb(255, 255, 255);"
                           u"color: rgb(0, 0, 0);"
                           u"border: solid;"
                           u"border-width: 1px;"
                           u"border-color: rgb(223, 223, 223);")
        item.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
