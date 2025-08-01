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

from UI.gridProfPar_Dlg import GridProfParDlg


class NewItem(QtWidgets.QDialog):
    def __init__(self):
        super(NewItem, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.created = False

        self.name_check()

        v['_temp'] = dict()

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

    def name_check(self):
        while self.ui.nameLBL.text() in v:
            # if self.ui.nameLBL.text() in v:
            self.ui.nameLBL.setText(self.ui.nameLBL.text() + ' (1)')
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

        v['_temp'] = {'par': {}, 'category': self.cat}
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

        self.ui.parWgt.setVisible(line > 0)
        # -------------------------------------------------------------------------------------------------------------

        # self.ui.parWgt.setVisible(True)
        self.ui.nodeWgt.setVisible(self.cat not in ['AC-Node', 'DC-Node'])
        for elem in ['node2CB', 'node2Lbl', 'vnode2Lbl', 'vnode2Dsb']:
            self.ui.__getattribute__(elem).setVisible(self.cat not in prof_elem)
        self.ui.servWgt.setVisible(True)
        self.ui.scaleProfWgt.setVisible(self.cat in prof_elem)
        if not(self.cat in prof_elem and 'profile' in v['_temp']['par'] and
               v['_temp']['par']['profile']['name'] is not None):
            self.ui.pictureProfWgt.setVisible(False)
            self.profilePlotWgtDelete()
            self.ui.constScaleProfRB.setChecked(True)

        if self.cat not in mc['Node']:
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

        # Verifica che le busbar a cui connettere l'elemento siano selezionate (che esistano...)
        self.ui.saveBtn.setVisible(False)
        if self.cat not in mc['Node']:
            if self.ui.node1CB.currentText():
                if self.cat in mc['Transformer'] + mc['Line']:
                    if self.ui.node2CB.currentText():
                        self.ui.saveBtn.setVisible(True)
                else:
                    self.ui.saveBtn.setVisible(True)
        else:
            self.ui.saveBtn.setVisible(True)

    def bb_read(self, cat, node1=None, node2=None):
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

        elif cat in ['AC-Line', 'Switch']:
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

        elif cat in ['AC-Load', 'AC-Wind', 'AC-PV', 'AC-BESS', ]:
            n1 = copy.deepcopy(n_ac)
        elif cat in ['DC-Load', 'DC-Wind', 'DC-PV', 'DC-BESS', ]:
            n1 = copy.deepcopy(n_dc)

        try:
            n1.sort(), n2.sort()
        except AttributeError:
            pass

        return n1, n2

    def prof_selected(self):
        self.ui.pictureProfWgt.setVisible(self.ui.profScaleProfRB.isChecked())
        self.ui.scaleProfDsb.setEnabled(not self.ui.profScaleProfRB.isChecked())
        self.profile_switch()

    def prof_open(self):
        if '_temp' not in list(v.keys()):
            v['_temp'] = {'par': {'profile': {'curve': 1, 'name': None, }}}

        prof_popup = ElementsProfile('_temp')

        if prof_popup.exec_():
            pass

        if v['_temp']['par']['profile']['name']:
            self.profilePlotWgtCreate()

    def profile_switch(self):
        default, cat = False, None
        gp = copy.deepcopy(grid['profile'])

        v['_temp'] = {'par': {'profile': {'curve': 1, 'name': None, }}, 'category': self.cat}

        if not grid['profile']['exist'] and self.ui.profScaleProfRB.isChecked():
            prof, default, cat = True, True, None
            popup1 = GridProfParDlg()

            while prof and default and cat is None:
                if popup1.exec_():
                    pass
                default = popup1.default
                prof = popup1.confirmed

                if default and grid['profile']['exist']:
                    from UI.elemProfCat_Dlg import ElemProfCatDlg
                    dlg = ElemProfCatDlg()
                    if self.cat in mc['Load']:
                        for pcat in bench['profiles']['load']:
                            dlg.ui.profCatCB.addItem(bench['profiles']['load'][pcat])
                    elif self.cat in ['AC-PV', 'DC-PV']:
                        dlg.ui.profCatCB.addItem('Fotovoltaico')
                    else:
                        dlg.ui.profCatCB.addItem('Cogeneratore')
                    dlg.exec_()
                    if dlg.ok:
                        cat = dlg.ui.profCatCB.currentText()
                    else:
                        default, cat = True, None
                else:
                    self.ui.constScaleProfRB.setChecked(True)

        if self.ui.profScaleProfRB.isChecked() and grid['profile']['exist']:
            # gp = copy.deepcopy(grid['profile'])

            if not v['_temp']['par']['profile']['name']:
                popup = ElementsProfile('_temp', default, cat)
                if popup.exec_():
                    pass

                if popup.refresh:
                    # self.elemPropWgt.profilePlotWgtCreate()
                    # self.elemPropWgt.ui.lfVL.insertWidget(3, self.elemPropWgt.profileWidget)
                    # self.elemPropWgt.profileBtn.clicked.connect(self.profile_open)
                    self.profilePlotWgtCreate()
                else:
                    grid['profile'] = gp
                    self.ui.constScaleProfRB.setChecked(True)

            # else:
            #     print('non dovrebbe arrivarci')
            #     self.elemPropWgt.profilePlotWgtCreate()
            #     # self.ui.lfVL.addWidget(self.profileWidget)
            #     self.elemPropWgt.ui.lfVL.insertWidget(3, self.elemPropWgt.profileWidget)
            #     self.elemPropWgt.profileBtn.clicked.connect(self.profile_open)
        else:
            try:
                self.elemPropWgt.profileWidget.deleteLater()
            except AttributeError:
                pass
        # self.elemPropWgt.profileCheck()
        # self.elemPropWgt.scale_RB.setChecked(v[self.elem]['par']['profile']['name'] is None)

    def profilePlotWgtCreate(self):
        font = {
            'weight': 'normal',
            'size': 4
        }

        matplotlib.rc('font', **font)
        self.canvas1 = FigureCanvas(plt.Figure(figsize=(1.7, 1.4)))
        self.ax = self.canvas1.figure.subplots()

        self.ax.plot([a for a in range(0, grid['profile']['points'])], v['_temp']['par']['profile']['curve'])  # TODO: da correggere: inserire i dati reali

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
        try:
            self.ui.pictureProfVL.itemAt(0).widget().deleteLater()
        except:
            pass
        self.ui.pictureProfVL.insertWidget(0, self.profileLbl)
        # self.ui.pictureProfVL.add

    def profilePlotWgtDelete(self):
        try:
            self.profileLbl.deleteLater()
        except:
            pass

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

        if self.cat not in mc['Node']:
            v[self.el]['par']['Vn'] = []
            for b in v[self.el]['top']['conn']:
                v[self.el]['par']['Vn'].append(v[b]['par']['Vn'][0])
        else:
            v[self.el]['par']['Vn'] = [v[self.el]['par']['Vn']]

        if '_temp' in list(v.keys()):
            if 'profile' in v['_temp']['par']:
                v[self.el]['par']['profile'] = copy.deepcopy(v['_temp']['par']['profile'])
                if self.ui.constScaleProfRB.isChecked():
                    v[self.el]['par']['profile']['curve'] = self.ui.scaleProfDsb.value()
            # del v['_temp']

        # for self.cat in mc['Generator'] + mc['BESS'] + mc['Load']:
        for n in v[self.el]['top']['conn']:
            v[n]['top']['conn'].append(self.el)

        self.created = True
        self.close()

    # def cancel(self):
    #     # self.closing_check()
    #     self.close()
    #
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Escape:
            self.close()

    def closeEvent(self, a0):
        del v['_temp']
        # try:
        #     print('cancellato')
        # except:
        #     pass
        # print('chiuso')

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
