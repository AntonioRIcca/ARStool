# import py_dss_interface
# from PySide2.QtCharts import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis
import copy
import datetime
import datetime as dt
import os.path
from functools import partial
import xlsxwriter

from PySide2 import QtGui, QtCore, QtWidgets

from PySide2.QtCharts import *

import variables
# import matplotlib
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# import matplotlib.pyplot as plt

# import variables
# from variables import v
# from variables import mainpath

from variables import *

import yaml
# from PySide2 import *
from PySide2.QtWidgets import *
# import sys

import opendss
# from threading import Thread

from mainUI import MainWindow

from UI.elementProperties import ElementProperties

from UI.elementsProfile import ElementsProfile
from UI.newItem import NewItem
from UI.gridProfPar_Dlg import GridProfParDlg
import dictInitialize

# import time

from collections import namedtuple
Data = namedtuple('Data', ['name', 'value', 'primary_color', 'secondary_color'])


# noinspection PyBroadException,PyArgumentList,PyUnusedLocal
class Main:
    def __init__(self):
        # variabili globali
        self.mainwindow = None
        self.ui = None

        self.dsspath = os.getcwd()
        self.savepath = os.path.join(os.environ['USERPROFILE'], 'Desktop')

        self.elem = None

        self.lf_cat = None
        self.p_eg = None
        self.q_eg = None
        self.p_loss = None
        self.q_loss = None

        self.lg_wgt = None
        self.lf_WGT = None
        self.par_wgt = None
        self.home_WGT = None
        self.home2_WGT = None
        self.home3_WGT = None
        self.home3_VL = None
        self.home3_top_WGT = None
        self.home3_center_WGT = None
        self.home3_center_VL = None
        self.home3_bottom_WGT = None
        self.homeHBL = None
        self.p_loads, self.q_loads = None, None
        self.p_gen, self.q_gen = None, None
        self.p_bess, self.q_bess = None, None
        self.home3_table_bottom_LN = None
        self.myform = None
        self.elemementTableWGT = None

        self.dss = opendss.OpenDSS()

        self.app = QApplication()
        self.interface_open()       # TODO: da elimianre da questa posizione: va dopo la scelta della rete


    def interface_open(self):
        os.chdir(mainpath)
        self.mainwindow = MainWindow()
        self.ui = self.mainwindow.ui
        self.ui.mainBodyContent.setStyleSheet(u'#mainBodyContent{background-image: url(ARStool500_shadow.png);'
                                              u'background-repeat: no-repeat;'
                                              u'background-position: center;}')
        self.mainwindow.show()

        # self.func_check()

        # self.ui.label_10.setText('APERTO!!!')
        #
        # from UI.table_wgt import Table
        # self.myform = Table()
        # mywidget = self.myform.ui.widget
        #
        # self.ui.homeSW.removeWidget(self.ui.homeSW.currentWidget())
        # self.ui.homeSW.addWidget(mywidget)

        v_initialize()
        self.startWgtCreate()
        # self.elementsTableWgtCreate()                                               # TODO: da riattivare

        # self.homeWGT_create()                                                     # TODO: da NON riattivare
        self.ui.mainPages.setCurrentIndex(0)

        # self.elementsTableFill()                                                  # TODO: da NON riattivare

        # self.myform.ui.tableWidget.currentCellChanged.connect(self.test_action)   # TODO: da NON riattivare

        self.ui.profileMenuBtn.clicked.connect(self.test_action2)
        self.ui.moreMenuBtn.clicked.connect(self.test_action2)
        self.ui.loadflow_Btn.clicked.connect(self.loadflow)
        self.ui.restartBtn.clicked.connect(self.startWgtCreate)
        self.ui.loadProfilesBtn.clicked.connect(self.elemProfList)
        self.ui.anom_Btn.clicked.connect(self.anomStart)
        self.ui.reliabilithy_Btn.clicked.connect(self.relStart)

        self.app.exec_()

    def func_disabled(self):
        self.ui.lf_Btn.setEnabled(False)

    # TODO: deve verificare la disponibilità delle funzioni della rete ed abilitare le funzioni selettivamente
    def func_enabled(self):
        self.ui.loadflow_Btn.setEnabled(True)

    def func_check(self):
        # for btn in fn_en:
        #     self.ui.__getattribute__(btn + 'WgtPls').setVisible(fn_en[btn])
        #     self.ui.__getattribute__(btn + 'WgtPls').setEnabled(fn_en[btn])
        # self.ui.lf_Btn.setVisible(True)
        pass

    def startWgtCreate(self):
        for f in grid['studies']:
            grid['studies'][f] = False
            
        self.savepath = os.path.join(os.environ['USERPROFILE'], 'Desktop')

        try:
            self.ui.home_WGT.deleteLater()
        except:
            self.home_WGT.deleteLater()
        self.home_WGT = QWidget()

        self.homeHBL = QHBoxLayout()
        self.home_WGT.setLayout(self.homeHBL)
        self.homeHBL.setContentsMargins(0, 0, 0, 0)

        from UI.start_wgt import StartWGT
        self.startWGT = StartWGT()
        self.startWGT.ui.startWgt.setMinimumSize(QtCore.QSize(300, 0))

        self.homeHBL.addWidget(self.startWGT.ui.startWgt, 0, QtCore.Qt.AlignLeft)

        self.ui.home_VL.addWidget(self.home_WGT)

        # Si ripete in self.elementsTableWgtCreate() --> self.homeWGT_create()
        # TODO: Capire se tutto questo può essere messo estermanemte
        self.home2_WGT = QWidget()
        self.home3_WGT = QWidget()
        self.home3_WGT.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)

        self.home3_VL = QVBoxLayout(self.home3_WGT)
        self.home3_VL.setContentsMargins(0, 0, 0, 0)
        self.home3_top_WGT = QWidget()
        self.home3_center_WGT = QWidget()
        self.home3_bottom_WGT = QWidget()
        self.home3_bottom_WGT.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)

        self.home3_VL.addWidget(self.home3_top_WGT)
        self.home3_VL.addWidget(self.home3_center_WGT)
        self.home3_VL.addWidget(self.home3_bottom_WGT)

        self.homeHBL.addWidget(self.home2_WGT)
        self.homeHBL.addWidget(self.home3_WGT)

        self.ui.rightMenuContainer.collapseMenu()

        self.startWGT.ui.importDssBtn.clicked.connect(self.dss_open)
        self.startWGT.ui.openFileBtn.clicked.connect(self.yml_open)
        self.startWGT.ui.benchOpenBtn.clicked.connect(self.benchmarkWGT_create)
        self.startWGT.ui.optStorBtn.clicked.connect(self.optstor_create)
        self.startWGT.ui.newGridBtn.clicked.connect(self.new_grid)

        v_initialize()
        # v['_grid_'] = copy.deepcopy()


    # Creazione dell'elenco delle reti benchmark
    def benchmarkWGT_create(self):
        grid['benchmark'] = True
        self.startWGT.ui.benchOpenBtn.setStyleSheet(u"background-color: rgb(63, 63, 63);")

        self.home2_WGT.deleteLater()

        self.home2_WGT = QWidget()
        self.home2_WGT.setMinimumWidth(250)
        self.bmWgtVBL = QVBoxLayout()
        self.bmWgtVBL.setSpacing(20)
        self.home2_WGT.setLayout(self.bmWgtVBL)

        bm = yaml.safe_load(open(mainpath + '/_benchmark/grid_models/grid_bench.yml'))

        for b in bm.keys():
            self.gridPls = pb_create(text='  ' + bm[b]['name'], height=30, font=24, border=2, radius=10,
                                     icon='importfile.png')
            # self.gridPls = QPushButton()
            # self.gridPls.setText('  ' + bm[b]['name'])
            # self.gridPls.setMinimumHeight(50)
            # self.testIco = QtGui.QIcon()
            # self.testIco.addFile(u":/icons/icons/importfile.png",
            #                      QtCore.QSize(100, 100), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            # self.gridPls.setIcon(self.testIco)
            # self.gridPls.setIconSize(QtCore.QSize(30, 30))
            #
            # self.gridPls.setStyleSheet(u"QPushButton {"
            #                            u"font: 24px;"
            #                            u"text-align: left;"
            #                            u"padding: 10px 20px;"
            #                            u"color: rgb(255, 255, 255);"
            #                            u"background-color: rgb(31, 31, 31); border: solid;"  # border-style: outset;"
            #                            u"border-width: 2px; border-radius: 20px; border-color: rgb(127, 127, 127)"
            #                            u"}"
            #                            u"QPushButton:pressed {"
            #                            u"background-color: rgb(64, 64, 64); border-style: inset"
            #                            u"}")
            self.bmWgtVBL.addWidget(self.gridPls)
            self.gridPls.clicked.connect(partial(self.gridDetailsWgtCreate, bm[b], b))

            # self.test.clicked.connect(self.gridDetailsWgtCreate)

        bm_spacer = QSpacerItem(20, 146, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.bmWgtVBL.addItem(bm_spacer)

        self.homeHBL.insertWidget(1, self.home2_WGT)
        pass

    def gridDetailsWgtCreate(self, grid, gridname):
        self.home3_WGT.deleteLater()

        from UI.grid_details_ui import GridDetailsWGT

        self.gridDetailsWgt = GridDetailsWGT()
        self.home3_WGT = self.gridDetailsWgt.ui.gridDetailsMainWgt

        self.homeHBL.insertWidget(2, self.home3_WGT)

        self.gridDetailsWgt.ui.nameLbl.setText(grid['name'])
        self.gridDetailsWgt.ui.descLbl.setText(grid['description'])
        img = mainpath + '/_benchmark/grid_models/images/' + gridname + '.png'
        self.gridDetailsWgt.ui.imageLbl.setPixmap(QtGui.QPixmap(img))

        self.filepath = mainpath + '/_benchmark/grid_models/' + gridname
        self.dsspath = mainpath + '/_benchmark/grid_models/'
        # self.gridname = gridname

        self.gridDetailsWgt.ui.open.clicked.connect(partial(self.dss_open, self.filepath))
        # self.yml_bench_save()

        # self.main.ui.EV303_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/arrowSX_20x20.png")

        # self.home3_WGT.setSizePolicy(QSizePolicy.Policy.Minimum)

    def new_grid(self):
        from UI.newGridDlg import NewGrid
        popup = NewGrid()

        if popup.exec_():
            pass

        if popup.newGridStart:
            v_initialize()
            grid['name'] = popup.ui.nameLe.text()

            dictInitialize.dict_initialize('source', 'ExternalGrid')
            v['source']['par']['Vn'] = [popup.ui.sourceVDsb.value()]
            v['source']['par']['out-of-service'] = False
            v['source']['top']['conn'] = ['sourcebus']

            dictInitialize.dict_initialize('sourcebus', 'AC-Node')
            v['sourcebus']['par']['Vn'] = [popup.ui.sourceVDsb.value()]
            v['sourcebus']['par']['out-of-service'] = False
            v['sourcebus']['top']['conn'] = ['source']

            self.elementsTableWgtCreate()
            self.func_check()


    # Apertura del file DSS
    def dss_open(self, filename=None):
        v_initialize()
        if not filename:
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog

            filename, ext = QtWidgets.QFileDialog.getOpenFileName(caption="Apri file DSS",
                                                                  dir=self.savepath,
                                                                  filter='*.dss')

            # self.gridname = 'externalDSS'

            # TODO: da riattivare
            grid['profile'] = {'step': None, 'start': None, 'end': None, 'points': None, 'exist': False}

        if filename:
            grid['benchmark'] = '_benchmark' in filename.split('/')
            # self.dss = opendss.OpenDSS()

            # TODO: Da ripristinare
            # try:
            #     self.dss.open(filename)
            #     self.elementsTableWgtCreate()
            #     # self.func_enabled()
            #     self.func_check()
            # except:
            #     QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Attenzione', 'Modello DSS non compatibile')

            # TODO: da eliminare
            self.dss.open(filename)
            self.elementsTableWgtCreate()
            # self.func_enabled()
            self.func_check()
            grid['name'] = filename.split('/')[len(filename.split('/')) - 1].removesuffix('.dss')

    def yml_open(self):
        grid['benchmark'] = False       # TODO: perché? non viene automaticamente sovrascritta?
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog

        filename, ext = QtWidgets.QFileDialog.getOpenFileName(caption="Apri file di rete",
                                                              dir=self.savepath,
                                                              filter='*.yml')

        if filename:
            name = filename.split('/')
            self.savepath = filename.removesuffix(name[len(name)-1])
            # self.gridname = name[len(name)-1].split('.')[0]
            v0 = yaml.safe_load(open(filename))

            for par in v0['_grid_']:
                grid[par] = v0['_grid_'][par]
            del v0['_grid_']

            for elem in v0:
                v[elem] = v0[elem]
            self.elementsTableWgtCreate()
            # self.func_enabled()
            self.func_check()

        for el in v:
            dictInitialize.lf_initialize(el)

    def yml_bench_save(self):   # TODO: non ricordo a che serve salvare la rete
        filename = self.dsspath + '/' + grid['name'] + '.yml'
        with open(filename, 'w') as file:
            yaml.dump(v, file)
            file.close()

    # Salvataggio del file YML della rete
    def yml_save(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog

        filename, ext = QtWidgets.QFileDialog.getSaveFileName(caption="Salva configurazione di rete",
                                                              dir=self.savepath + '/' + grid['name'],
                                                              filter='*.yml')

        if filename:
            a = {'_grid_': grid}
            ts = dt.datetime.now()

            with open(filename, 'w') as file:
                yaml.dump({**a, **v}, file)
                file.close()
            nts = dt.datetime.now() - ts

            print('Save time:', nts.total_seconds())

    # Inserimento della tabella degli elementi nel widget principale
    def elementsTableWgtCreate(self):
        self.homeWGT_create()
        self.elementsTableFill()
        self.myform.ui.tableWidget.currentCellChanged.connect(self.test_action)
        # self.myform.ui.tableWidget.mouseDoubleClickEvent = self.elementRename
        self.myform.ui.save_Btn.clicked.connect(self.yml_save)
        self.myform.ui.add_Btn.clicked.connect(self.new_element)
        self.myform.ui.del_Btn.clicked.connect(self.del_element)
        self.myform.ui.ren_Btn.clicked.connect(self.elementRename)
        # Window(list(v.keys())[0])

    def new_element(self):
        popup = NewItem()

        if popup.exec_():
            pass

        if popup.created:
            self.myform.ui.tableWidget.insertRow(0)
            self.myform.ui.tableWidget.setItem(0, 0, QTableWidgetItem(popup.el))
            self.myform.ui.tableWidget.setItem(0, 1, QTableWidgetItem(popup.cat))

    def del_element(self):
        line = self.myform.ui.tableWidget.currentRow()
        del v[self.elem]
        self.myform.ui.tableWidget.removeRow(line)
        self.ui.rightMenuContainer.collapseMenu()
        self.myform.ui.del_Btn.setVisible(False)

    def elementsTableFill(self):
        self.myform.ui.tableWidget.clear()
        self.myform.ui.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Nome Elemento'))
        self.myform.ui.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Categoria'))

        self.myform.ui.tableWidget.setRowCount(len(v))

        i = 0
        for elem in dict(sorted(v.items())):    # dict(sorted() necessario per ordinare alfabeticamente gli elementi
            self.myform.ui.tableWidget.setItem(i, 0, QTableWidgetItem(elem))
            self.myform.ui.tableWidget.setItem(i, 1, QTableWidgetItem(v[elem]['category']))
            i += 1
        self.elementsTableFormat()

        self.myform.ui.tableWidget.sortByColumn(1, QtCore.Qt.AscendingOrder)

    def elementsTableFormat(self):
        self.myform.ui.tableWidget.setSortingEnabled(True)
        self.myform.ui.tableWidget.setShowGrid(False)
        self.myform.ui.tableWidget.setStyleSheet('QTableView::item {border-top: 1px solid #333333;}')
        self.myform.ui.tableWidget.verticalHeader().setVisible(False)

        stylesheet = \
            "QHeaderView::section{color:rgb(251,251,251); Background-color:rgb(1,1,1); border - radius: 14 px;}"
        self.myform.ui.tableWidget.horizontalHeader().setStyleSheet(stylesheet)
        for i in range(0, self.myform.ui.tableWidget.rowCount()):
            for j in range(0, self.myform.ui.tableWidget.columnCount()):
                self.myform.ui.tableWidget.item(i, j).setForeground(QtGui.QColor(255, 255, 255))

        self.myform.ui.tableWidget.setColumnWidth(0, 160)
        self.myform.ui.tableWidget.setColumnWidth(1, 150)

    def test_action(self):
        line = self.myform.ui.tableWidget.currentRow()
        self.elem = self.myform.ui.tableWidget.item(line, 0).text()
        self.myform.ui.del_Btn.setVisible(self.elem not in ['source', 'sourcebus'])
        self.myform.ui.ren_Btn.setVisible(self.elem not in ['source', 'sourcebus'])
        # dss.writeline(elem)   TODO: ???????

        try:
            self.ui.rightMenuPages.removeWidget(self.ui.rightMenuPages.widget(2))
        except:
            pass

        # self.ui.elemNameLE.setVisible(False)
        # self.ui.rightMenu_LBL.setVisible(True)
        self.ui.rightMenu_LBL.setText(self.elem)
        # self.ui.rightMenu_LBL.mouseDoubleClickEvent = self.mainwindow.elementRename

        self.ui.rightMenuContainer.expandMenu()

        # -- Sospeso per prova nuovo layout ----------------------------------------------------
        # self.par_wgt = Window(self.elem)
        #
        # # self.profile_draw()
        # self.ui.rightMenuPages.addWidget(self.par_wgt.mainWidget)
        # self.par_wgt.mainWidget.setMinimumHeight(1200)
        #
        # self.ui.rightMenuPages.setCurrentIndex(self.ui.rightMenuPages.count() - 1)
        #
        # self.par_wgt.cancel_BTN.clicked.connect(self.ui.rightMenuContainer.collapseMenu)
        # try:
        #     self.par_wgt.profileBtn.clicked.connect(self.profile_open)
        # except AttributeError:
        #     pass
        #
        # # dss.readline(elem, v[elem]['category'])
        #
        # --------------------------------------------------------------------------------------

        # self.ui.lfWgtPls.clicked.connect(self.myaction1)
        # self.ui.relWgtPls.clicked.connect(self.myaction2)
        # self.ui.lfWgtPls.clicked.connect(self.ui.lfWgt.expandMenu)
        # self.ui.relWgtPls.clicked.connect(self.ui.lfWgt.collapseMenu)

        # -- Nuovo richiamo alla form ---------------------------------------------------------- TODO: da riattivare
        self.elemPropWgt = ElementProperties(self.elem)
        self.ui.rightMenuPages.addWidget(self.elemPropWgt.ui.propertiesWgt)

        self.ui.rightMenuPages.setCurrentIndex(self.ui.rightMenuPages.count() - 1)
        # self.elemPropWgt.ui.lfPls.clicked.connect(self.myaction1)
        # self.elemPropWgt.ui.relPls.clicked.connect(self.myaction2)

        self.elemPropWgt.ui.cancelPLS.clicked.connect(self.ui.rightMenuContainer.collapseMenu)

        try:
            self.elemPropWgt.profile_RB.toggled.connect(self.profile_switch)
            self.elemPropWgt.profileBtn.clicked.connect(self.profile_open)
        except AttributeError:
            pass
        # --------------------------------------------------------------------------------------
        pass

    def elementRename(self):
        spec_char = '!@#$%^&*()?=,<>/" '     # elenco dei caratteri che non possono essere insereiti nel nome del file

        closed = False  # Variabile necessaria per capire se si può chiudere la finestrsa di dialogo
        while not closed:
            text, ok = QInputDialog.getText(None, 'Nuovo nome', 'Inserisci il nuovo nome', QLineEdit.Normal, self.elem)

            if ok:  # Le azioni sottostanti devono essere eseguite se si è premuto OK o il tasto Invio

                # se il nome è nuovo, si sovrascrive
                if text != '' and text not in v and not any(c in spec_char for c in text):
                    v[text] = copy.deepcopy(v[self.elem])
                    del v[self.elem]
                    for el in v:
                        for i in range(len(v[el]['top']['conn'])):
                            if v[el]['top']['conn'][i] == self.elem:
                                v[el]['top']['conn'][i] = text

                    self.ui.rightMenu_LBL.setText(text)
                    self.elementsTableWgtCreate()
                    closed = True

                # se si lascia il vecchio nome si chiude la dialogo senza azioni
                elif text == self.elem:
                    closed = True

                # se il nome non è inedito la schermata non si chiude
            else:
                closed = True


    # def myaction1(self):
    #     # self.ui.relWgt.collapseMenu()
    #     # self.ui.lfWgt.expandMenu()
    #     self.elemPropWgt.ui.lfWgt.setMaximumHeight(1500)
    #     self.elemPropWgt.ui.relWgt.setMaximumHeight(20)
    #
    # def myaction2(self):
    #
    #     self.elemPropWgt.ui.relWgt.setMaximumHeight(1500)
    #     self.elemPropWgt.ui.lfWgt.setMaximumHeight(20)

    def profile_draw(self, l=180, h=120):
        font = {
            'weight': 'normal',
            'size': 4
        }

        matplotlib.rc('font', **font)
        self.canvas = FigureCanvas(plt.Figure(figsize=(2, 1.5)))
        # self.ax = self.canvas.figure.subplots()
        self.ax = self.canvas.figure.add_subplot(111)
        self.ax.plot([0, 12, 24], [0.3, 0.9, 0.6])

        self.ax.set_title('Profilo')
        self.ax.set_ylim([0, 1.05])
        self.ax.set_xlim([0, 24])
        self.ax.set_xlabel('Tempo [h]', fontsize=4)
        self.ax.set_ylabel('Profilo [p.u.]', fontsize=2)

        # self.line, = self.ax.plot([0,12,24], [0.3, 0.9, 0.6])
        self.canvas.draw()
        self.canvas.flush_events()
        self.canvas.flush_events()

        self.par_wgt.mainVBL.insertWidget(2, self.canvas)

    def profile_open(self):
        # if not grid['profile']['exist']:
        #     popup1 = GridProfParDlg()
        #     if popup1.exec_():
        #         pass

        popup = ElementsProfile(self.elem)
        if popup.exec_():
            pass

        if popup.refresh:
            self.elemPropWgt.profileWgtRefresh()
            self.elemPropWgt.profileBtn.clicked.connect(self.profile_open)

    def profile_switch(self):
        default, cat = False, None
        gp = copy.deepcopy(grid['profile'])

        if not grid['profile']['exist'] and self.elemPropWgt.profile_RB.isChecked():
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
                    for pcat in bench['profiles']['load']:
                        dlg.ui.profCatCB.addItem(bench['profiles']['load'][pcat])
                    dlg.exec_()
                    if dlg.ok:
                        cat = dlg.ui.profCatCB.currentText()
                    else:
                        default, cat = True, None

        if self.elemPropWgt.profile_RB.isChecked() and grid['profile']['exist']:
            # gp = copy.deepcopy(grid['profile'])

            if not v[self.elem]['par']['profile']['name']:
                popup = ElementsProfile(self.elem, default, cat)
                if popup.exec_():
                    pass

                if popup.refresh:
                    self.elemPropWgt.profilePlotWgtCreate()
                    self.elemPropWgt.ui.lfVL.insertWidget(3, self.elemPropWgt.profileWidget)
                    self.elemPropWgt.profileBtn.clicked.connect(self.profile_open)
                else:
                    grid['profile'] = gp

            else:
                self.elemPropWgt.profilePlotWgtCreate()
                # self.ui.lfVL.addWidget(self.profileWidget)
                self.elemPropWgt.ui.lfVL.insertWidget(3, self.elemPropWgt.profileWidget)
                self.elemPropWgt.profileBtn.clicked.connect(self.profile_open)
        else:
            try:
                self.elemPropWgt.profileWidget.deleteLater()
            except AttributeError:
                pass
        self.elemPropWgt.profileCheck()
        self.elemPropWgt.scale_RB.setChecked(v[self.elem]['par']['profile']['name'] is None)


    def test_action2(self, mcat, event=None):
        # -- Creazione del diagramma delle generazioni ---------------------------
        # Todo: da definire come gestire i dati  del diagramma
        from UI.donutbreakdown2 import DonutBreakdownChart
        db_graph = DonutBreakdownChart(mcat=mcat, data=self.lf_cat[mcat])

        try:
            self.home3_top_WGT.deleteLater()
        except: pass
        self.home3_top_WGT = QtCharts.QChartView(db_graph)
        self.home3_VL.insertWidget(0, self.home3_top_WGT)
        # --------------------------------------------------------------

        self.lf_cat_widget(mcat)

        pass

    def homeWGT_create(self):
        try:
            self.ui.home_WGT.deleteLater()
        except:
            self.home_WGT.deleteLater()
        self.home_WGT = QWidget()

        # self.homeHBL = QHBoxLayout(self.home_WGT)
        self.homeHBL = QHBoxLayout()
        self.home_WGT.setLayout(self.homeHBL)
        self.homeHBL.setContentsMargins(0, 0, 0, 0)

        from UI.table_wgt import Table
        self.myform = Table()
        self.elemementTableWGT = self.myform.ui.widget

        self.elemementTableWGT.setMinimumSize(QtCore.QSize(350, 0))

        self.homeHBL.addWidget(self.elemementTableWGT, 0, QtCore.Qt.AlignLeft)

        self.ui.home_VL.addWidget(self.home_WGT)

        self.home2_WGT = QWidget()
        self.home3_WGT = QWidget()
        self.home3_WGT.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)

        self.home3_VL = QVBoxLayout(self.home3_WGT)
        self.home3_VL.setContentsMargins(0, 0, 0, 0)
        self.home3_top_WGT = QWidget()
        self.home3_center_WGT = QWidget()
        self.home3_bottom_WGT = QWidget()
        self.home3_bottom_WGT.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)

        self.home3_VL.addWidget(self.home3_top_WGT)
        self.home3_VL.addWidget(self.home3_center_WGT)
        self.home3_VL.addWidget(self.home3_bottom_WGT)

        self.homeHBL.addWidget(self.home2_WGT)
        self.homeHBL.addWidget(self.home3_WGT)

        # -- Creazione del diagramma a torta ---------------------------
        # Todo: da definire come gestire i dati  del diagramma
        # from UI.piechart import PieChart
        # chart = PieChart()
        # chart_view = QtCharts.QChartView(chart)
        #
        # self.lf_WGT.ui.image_VL.addWidget(chart_view)
        # --------------------------------------------------------------

    def barchart(self):
        cat = ['External Grid', 'Generation', 'Loads', 'BESS', 'Losses']
        p = ['eg', 'gen', 'loads', 'bess', 'loss']
        series = QtCharts.QPercentBarSeries()

        for i in range(5):
            self.__setattr__('set' + str(i), QtCharts.QBarSet(cat[i]))
            if cat[i] in ['Generation', 'External Grid']:
                if self.__getattribute__('p_' + p[i]) >= 0:
                    self.__getattribute__('set' + str(i)).append([self.__getattribute__('p_' + p[i]), 0])
                else:
                    self.__getattribute__('set' + str(i)).append([0, - self.__getattribute__('p_' + p[i])])
            else:
                if self.__getattribute__('p_' + p[i]) >= 0:
                    self.__getattribute__('set' + str(i)).append([0, self.__getattribute__('p_' + p[i])])
                else:
                    self.__getattribute__('set' + str(i)).append([- self.__getattribute__('p_' + p[i]), 0])

            series.append(self.__getattribute__('set' + str(i)))

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        categories = ['In', 'Cons']

        axis = QtCharts.QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
        chart.setBackgroundBrush(QtGui.QBrush(QtGui.QColor('transparent')))
        chart.legend().setLabelColor(QtGui.QColor('white'))
        chart.setTitleBrush(QtGui.QColor(255, 255, 255))
        chart.setTitleFont(QtGui.QFont("Arial", 12))
        chart.axisX().setLabelsColor(QtGui.QColor(255, 255, 255))
        chart.axisY().setLabelsColor(QtGui.QColor(255, 255, 255))
        chart.axisY().setLabelFormat("%.0f%%")
        chart.legend().setFont(QtGui.QFont("Arial", 10))

        try:
            self.lf_WGT.ui.lfres_bottom_WGT.deleteLater()
        except: pass

        try:
            self.lfres_bottom_wgt.deleteLater()
        except: pass
        try:
            self.home3_center_WGT.deleteLater()
            self.home3_top_WGT.deleteLater()
        except: pass

        self.lfres_bottom_wgt = QtCharts.QChartView(chart)

        # try:
        #     self.lf_WGT.ui.lfres_VL.removeWidget(self.lfres_bottom_wgt)
        # except:
        #     print('non riesco')
        self.lf_WGT.ui.lfres_VL.insertWidget(3, self.lfres_bottom_wgt)

        a = QtWidgets.QVBoxLayout()

    def loadflow(self):
        self.ui.rightMenuContainer.collapseMenu()

        self.ui.rightMenuContainer.collapseMenu()
        try:
            self.home2_WGT.deleteLater()
        except RuntimeError:
            pass

        # is_profile = False
        time = None
        #
        # for el in v:
        #     if v[el]['category'] in mc['Load'] + mc['Generator']:
        #         if v[el]['par']['profile']['name']:
        #             is_profile = True
        #             break
        #
        # print(grid['profile']['start'])
        # print(grid['profile']['end'])

        s, t0 = None, None
        if grid['profile']['exist']:
            from UI.lfMod_Dlg import LfModDlg
            lf_popup = LfModDlg()

            if lf_popup.exec_():
                pass

            if lf_popup.confirm:
                # Reset dei risultati
                for el in v:
                    dictInitialize.lf_initialize(el)

                grid['studies']['lf'] = True

                self.datestart = dt.datetime(grid['lf']['start'][0], grid['lf']['start'][1], grid['lf']['start'][2],
                                             grid['lf']['start'][3], grid['lf']['start'][4])
                self.dateend = dt.datetime(grid['lf']['end'][0], grid['lf']['end'][1], grid['lf']['end'][2],
                                           grid['lf']['end'][3], grid['lf']['end'][4])
                self.loadflow_results_init()
                self.lf_WGT.ui.lfres_center_WGT.setVisible(lf_popup.profile)

                grid['current'] = copy.deepcopy(grid['lf']['start'])

                if lf_popup.profile:

                    ts = dt.datetime.now()
                    # self.dss.full_parse_profil_to_dss_csv(t0=lf_popup.i_start, steps=lf_popup.i_steps)      # csv
                    # self.dss.full_parse_profil_to_dss_polars(t0=lf_popup.i_start, steps=lf_popup.i_steps)   # Polars
                    # self.dss.full_parse_profil_to_dss_numpy(t0=lf_popup.i_start, steps=lf_popup.i_steps)    # Numpy
                    # self.dss.full_parse_profil_to_dss_numpy_chatGPT(t0=lf_popup.i_start, steps=lf_popup.i_steps)    # chatGPT
                    # self.dss.full_parse_profil_to_dss_numpy_chatGPT_nodata(t0=lf_popup.i_start, steps=lf_popup.i_steps)    # chatGPT No Data

                    # self.dss.full_parse_profil_to_dss_array(t0=lf_popup.i_start, steps=lf_popup.i_steps)    # Array
                    # self.dss.full_parse_profil_to_dss(t0=lf_popup.i_start, steps=lf_popup.i_steps)          # PandaFrame
                    for i in range(lf_popup.i_steps):                                                       # Dizionario
                        self.dss.full_parse_to_dss(time=lf_popup.i_start + i)
                        self.dss.solve()
                        self.dss.results_store_all()
                    nts = dt.datetime.now() - ts

                    print('Elaboration time:', nts.total_seconds())
                else:
                    print('single')
                    self.dss.full_parse_to_dss(time=lf_popup.i_start)
                    self.dss.solve()
                    self.dss.results_store_all()
                    self.loadflow_results_refresh()

                    # self.loadflow_results_init()
                    # self.lf_WGT.ui.lfres_center_WGT.setVisible(lf_popup.profile)
                # self.loadflow_results_refresh(t=0)

        else:
            print('no-profile')
            grid['current'] = None
            self.dss.full_parse_to_dss(time=None)
            self.dss.solve()
            self.dss.results_store_all()
            self.loadflow_results_init()
            self.lf_WGT.ui.lfres_center_WGT.setVisible(False)

        self.loadflow_results_refresh(t=0)

        # if s:
        # self.dss.full_parse_to_dss(is_profile=True, time=time)
        # self.yml_bench_save()
        # dss.write_all()
        # dss.solve()

        # write_excel()

        # self.dss.test()  # TODO: da eliminare, è una prova

    def loadflow_results_refresh(self, t=0):
        self.loadflow_results(t=t)
        self.loadflow_table_compile()
        self.barchart()
        pass

    def loadflow_results(self, t=0):
        self.p_loads, self.q_loads = 0, 0
        self.p_gen, self.q_gen = 0, 0
        self.p_bess, self.q_bess = 0, 0

        self.lf_cat = dict()
        for mcat in ['Generators', 'Loads', 'BESS']:
            self.lf_cat[mcat] = dict()
        # for cat in ['AC-Load', 'DC-Load', 'PV', 'AC-Wind', 'DC-Wind', 'BESS']:
        #     lf_cat[cat] = dict()

        for elem in v.keys():
            cat = v[elem]['category']
            if v[elem]['category'] in mc['Load']:
                self.p_loads += v[elem]['lf']['p'][t]
                self.q_loads += v[elem]['lf']['q'][t]
                mcat = 'Loads'

            elif v[elem]['category'] in mc['BESS']:
                self.p_bess += v[elem]['lf']['p'][t]
                self.q_bess += v[elem]['lf']['q'][t]
                mcat = 'BESS'

            elif v[elem]['category'] in mc['Generator']:
                self.p_gen -= v[elem]['lf']['p'][t]
                self.q_gen -= v[elem]['lf']['q'][t]
                mcat = 'Generators'

            if cat in prof_elem:
                if cat not in list(self.lf_cat[mcat].keys()):
                    self.lf_cat[mcat][cat] = dict()
                self.lf_cat[mcat][cat][elem] = {
                    'p': abs(v[elem]['lf']['p'][t]),
                    'q': abs(v[elem]['lf']['q'][t]),
                }

        self.p_eg, self.q_eg = -v['source']['lf']['p'][t], -v['source']['lf']['q'][t]
        self.p_loss = self.p_eg + self.p_gen - self.p_loads - self.p_bess
        self.q_loss = self.q_eg + self.q_gen - self.q_loads - self.q_bess

    def loadflow_results_init(self):
        # pasqu
        self.lf_WGT = LFrWGT()
        self.home2_WGT = self.lf_WGT.ui.lfres_WGT

        self.homeHBL.insertWidget(1, self.home2_WGT)

        self.lf_WGT.ui.gen_GB.mouseDoubleClickEvent = partial(self.test_action2, 'Generators')
        self.lf_WGT.ui.loads_GB.mouseDoubleClickEvent = partial(self.test_action2, 'Loads')
        self.lf_WGT.ui.bess_GB.mouseDoubleClickEvent = partial(self.test_action2, 'BESS')

        try:
            self.lf_WGT.ui.lfresDte.setMinimumDateTime(QtCore.QDateTime(self.datestart))
            self.lf_WGT.ui.lfresDte.setMaximumDateTime(QtCore.QDateTime(self.dateend))
        except: pass

        self.lf_WGT.ui.lfresDte.dateChanged.connect(self.loafdlow_date_change)
        self.lf_WGT.ui.lfresDte.timeChanged.connect(self.loafdlow_date_change)

    def loafdlow_date_change(self):
        sel_time = self.lf_WGT.ui.lfresDte.dateTime()
        step = int(QtCore.QDateTime(self.datestart).secsTo(sel_time) / 60 /
                   grid['profile']['step'])

        self.loadflow_results_refresh(t=step)

        sel_time = sel_time.toPython()

        grid['current'] = [sel_time.year, sel_time.month, sel_time.day, sel_time.hour, sel_time.minute]

        # -- Procedura di aggiornamento del valore di Scala nella finiestra degli elementi -------------------------
        timestart = dt.datetime(grid['profile']['start'][0], grid['profile']['start'][1],
                                grid['profile']['start'][2], grid['profile']['start'][3],
                                grid['profile']['start'][4])
        currenttime = dt.datetime(grid['current'][0], grid['current'][1], grid['current'][2],
                                  grid['current'][3], grid['current'][4])
        i = int((currenttime - timestart).total_seconds() / (60 * grid['profile']['step']))

        if self.elem:
            if v[self.elem]['category'] in (mc['Load'] + mc['Generator']) and v[self.elem]['par']['profile']['name']:
                print('forse profili')
                self.elemPropWgt.scale_DSB.setValue(v[self.elem]['par']['profile']['curve'][i])
                self.elemPropWgt.PeffDSB.setValue(v[self.elem]['par']['profile']['curve'][i] * v[self.elem]['par']['P'])

            self.elemPropWgt.fillLfRes(i)
        # ----------------------------------------------------------------------------------------------------------
        pass

    def loadflow_table_compile(self):
        for cat in ['eg', 'loss', 'loads', 'bess', 'gen']:
            self.lf_WGT.ui.__getattribute__('p_' + cat + '_value_LBL').setText(
                str(round(self.__getattribute__('p_' + cat), 2)))
            self.lf_WGT.ui.__getattribute__('q_' + cat + '_value_LBL').setText(
                str(round(self.__getattribute__('q_' + cat), 2)))


        # # -- Creazione del diagramma a torta ---------------------------
        # eg = Data('External Grid', self.p_eg, QtGui.QColor("#ffc000"), QtGui.QColor("#ffe699"))
        # gen = Data('Generation', self.p_gen, QtGui.QColor("#ed7d31"), QtGui.QColor("#f8cbad"))
        # loads = Data('Loads', self.p_loads, QtGui.QColor("#5b9bd5"), QtGui.QColor("#bdd7ee"))
        # bess = Data('BESS', self.p_bess, QtGui.QColor("#70ad47"), QtGui.QColor("#c5e0b4"))
        # loss = Data('Losses', self.p_loss, QtGui.QColor("#44546a"), QtGui.QColor("#adb9ca"))
        # data = [eg, gen, loads, bess, loss]
        #
        # from UI.piechart import PieChart
        # chart = PieChart(data=data)
        # chart_view = QtCharts.QChartView(chart)
        #
        # self.lf_WGT.ui.image_VL.addWidget(chart_view)
        # chart_view.setAlignment()
        # # --------------------------------------------------------------

    # def write_excel(self):
    #     file_excel = xlsxwriter.Workbook('risultato.xlsx')
    #     worksheet = file_excel.add_worksheet()
    #     worksheet.write(0, 0, 'Results')
    #
    #     lf_par = ['v', 'p', 'q', 'i']
    #     row, col = 1, 0
    #     for cat in ['AC-Load', 'DC-Load', 'BESS', 'PV', 'AC-Wind', 'DC-Wind', 'Diesel-Motor']:
    #         row += 1
    #         worksheet.write(row, col, cat)
    #         row += 1
    #
    #         col = 1
    #         for par in lf_par:
    #             worksheet.write(row, col, par)
    #             col += 1
    #         row += 1
    #         col = 0
    #
    #         for el in v:
    #             if v[el]['category'] == cat:
    #                 worksheet.write(row, col, el)
    #                 col = 1
    #                 for par in lf_par:
    #                     worksheet.write(row, col, v[el]['lf'][par])
    #                     col += 1
    #                 row += 1
    #                 col = 0
    #
    #     for cat in ['2W-Transformer', 'PWM', 'DC-DC-Converter', 'AC-Line', 'DC-Line']:
    #         row += 1
    #         worksheet.write(row, col, cat)
    #         row += 1
    #
    #         col = 1
    #         for par in lf_par:
    #             for i in [0, 1]:
    #                 worksheet.write(row, col, par + str(i))
    #                 col += 1
    #         row += 1
    #         col = 0
    #         # worksheet.write(2, 10, 'pepe')
    #
    #         for el in v:
    #             if v[el]['category'] == cat:
    #                 worksheet.write(row, col, el)
    #                 col = 1
    #                 for par in lf_par:
    #                     for i in [0, 1]:
    #                         worksheet.write(row, col, v[el]['lf'][par][i])
    #                         col += 1
    #                 row += 1
    #                 col = 0
    #
    #
    #     file_excel.close()
    #     pass
    #
    def lf_cat_widget(self, mcat):
        colors = [QtGui.Qt.red, QtGui.Qt.darkGreen, QtGui.Qt.darkBlue]
        i = 0
        mycol = QtGui.Qt.red

        mycolor = 'rgb(100,100,100)'
        try:
            self.home3_center_WGT.deleteLater()
        except: pass

        self.home3_center_WGT = QWidget()
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.home3_center_WGT.setFont(font)
        self.home3_center_VL = QVBoxLayout(self.home3_center_WGT)
        self.home3_center_VL.setSpacing(0)
        for cat in self.lf_cat[mcat]:
            self.__setattr__('home3_' + cat + '_top_LN', QFrame())
            self.__getattribute__('home3_' + cat + '_top_LN').setStyleSheet('border: 1px solid rgb(255, 255, 255);')
            self.__getattribute__('home3_' + cat + '_top_LN').setFrameShape(QFrame.HLine)

            self.__setattr__('home3_' + cat + '_WGT', QWidget())

            self.__setattr__('home3_' + cat + '_HL', QHBoxLayout(self.__getattribute__('home3_' + cat + '_WGT')))
            self.__getattribute__('home3_' + cat + '_HL').setContentsMargins(0, 0, 0, 0)
            self.__setattr__('home3_' + cat + '_sx_LBL', QLabel(cat))
            self.__setattr__('home3_' + cat + '_ctr_WGT', QWidget())
            self.__setattr__('home3_' + cat + '_dx_WGT', QWidget())
            sizepolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
            sizepolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            sizepolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)

            self.__getattribute__('home3_' + cat + '_sx_LBL').setSizePolicy(sizepolicy1)
            self.__getattribute__('home3_' + cat + '_sx_LBL').setMinimumSize(80, 0)

            self.__getattribute__('home3_' + cat + '_sx_LBL').setAlignment(QtGui.Qt.AlignRight | QtGui.Qt.AlignVCenter)
            self.__getattribute__('home3_' + cat + '_sx_LBL').setStyleSheet(u'font: bold 12pt "MS Shell Dlg 2"')
            self.__getattribute__('home3_' + cat + '_ctr_WGT').setSizePolicy(sizepolicy2)
            self.__getattribute__('home3_' + cat + '_dx_WGT').setSizePolicy(sizepolicy3)
            self.__getattribute__('home3_' + cat + '_HL').addWidget(self.__getattribute__('home3_' + cat + '_sx_LBL'))
            self.__getattribute__('home3_' + cat + '_HL').addWidget(self.__getattribute__('home3_' + cat + '_ctr_WGT'))
            self.__getattribute__('home3_' + cat + '_HL').addWidget(self.__getattribute__('home3_' + cat + '_dx_WGT'))

            self.__setattr__('home3_' + cat + '_VL', QVBoxLayout(self.__getattribute__('home3_' + cat + '_ctr_WGT')))
            self.__getattribute__('home3_' + cat + '_VL').setSpacing(0)

            self.home3_center_VL.addWidget(self.__getattribute__('home3_' + cat + '_top_LN'))
            self.home3_center_VL.addWidget(self.__getattribute__('home3_' + cat + '_WGT'))
            for elem in self.lf_cat[mcat][cat]:
                self.__setattr__('home3_' + elem + '_WGT', QWidget())
                self.__setattr__('home3_' + elem + '_HL', QHBoxLayout(self.__getattribute__('home3_' + elem + '_WGT')))
                self.__getattribute__('home3_' + elem + '_HL').setContentsMargins(0, 5, 0, 5)

                self.__setattr__('home3_' + elem + '_name_LBL', QLabel(elem + ':'))
                self.__setattr__('home3_' + elem + '_color_WGT', QWidget())
                self.__setattr__('home3_' + elem + '_p_LBL', QLabel())
                self.__getattribute__('home3_' + elem + '_p_LBL',).setText(f"{self.lf_cat[mcat][cat][elem]['p']:.1f}")

                self.__setattr__('home3_' + elem + '_unit_LBL', QLabel())
                self.__getattribute__('home3_' + elem + '_unit_LBL').setText('kW')
                self.__getattribute__('home3_' + elem + '_HL').addWidget(
                    self.__getattribute__('home3_' + elem + '_name_LBL'))
                self.__getattribute__('home3_' + elem + '_HL').addWidget(
                    self.__getattribute__('home3_' + elem + '_color_WGT'))
                self.__getattribute__('home3_' + elem + '_HL').addWidget(
                    self.__getattribute__('home3_' + elem + '_p_LBL'))
                self.__getattribute__('home3_' + elem + '_HL').addWidget(
                    self.__getattribute__('home3_' + elem + '_unit_LBL'))
                self.__getattribute__('home3_' + elem + '_name_LBL').setAlignment(QtGui.Qt.AlignRight)
                self.__getattribute__('home3_' + elem + '_name_LBL').setSizePolicy(QSizePolicy.Preferred,
                                                                                   QSizePolicy.Preferred)
                self.__getattribute__('home3_' + elem + '_name_LBL').setMinimumSize(150, 0)
                self.__getattribute__('home3_' + elem + '_p_LBL').setSizePolicy(QSizePolicy.Fixed,
                                                                                QSizePolicy.Preferred)
                self.__getattribute__('home3_' + elem + '_p_LBL').setMinimumSize(50, 0)
                self.__getattribute__('home3_' + elem + '_p_LBL').setAlignment(QtGui.Qt.AlignRight)

                self.__getattribute__('home3_' + elem + '_name_LBL').setStyleSheet('color: ' + mycolor)

                self.__getattribute__('home3_' + cat + '_VL').addWidget(self.__getattribute__('home3_' + elem + '_WGT'))
            i += 1

        self.home3_table_bottom_LN = QFrame()
        self.home3_table_bottom_LN.setStyleSheet('border: 1px solid rgb(255, 255, 255);')
        self.home3_table_bottom_LN.setFrameShape(QFrame.HLine)
        self.home3_center_VL.addWidget(self.home3_table_bottom_LN)

        self.home3_VL.insertWidget(1, self.home3_center_WGT)
        self.home3_VL.insertWidget(0, self.home3_top_WGT)

    def optstor_create(self):
        from Functionalities.OptimalStorage.optimalStorage import OptStorWGT

        try:
            self.ui.home_WGT.deleteLater()
        except:
            self.home_WGT.deleteLater()

        self.optStorWgt = OptStorWGT()

        self.home_WGT = self.optStorWgt.ui.optStorWgt

        self.ui.home_VL.addWidget(self.home_WGT)

    def elemProfList(self):
        print('lista')
        try:
            self.home2_WGT.deleteLater()
        except RuntimeError:
            pass

        self.home2_WGT = QWidget()
        self.home2_WGT.setMinimumWidth(450)

        self.home2_WGT.setStyleSheet(u"*{\n"
                                           u"background-color: rgb(0, 0, 0);\n"
                                           u"color: rgb(191, 191, 191);\n"
                                           u"}\n\n"
                                           u"QGroupBox{\n"
                                           u"font: 75 12pt \"MS Shell Dlg 2\";\n\n"
                                           u"QGroupBox::title  {\n"
                                           u"subcontrol-origin: margin;\nsubcontrol-position: top center;\n"
                                           u"padding: 5px 50 5px 50px;\n"
                                           u"background-color: rgb(0, 0, 21);\n"
                                           u"border-color: rgb(255, 255, 255);\n"
                                           u"color: rgb(255, 255, 255);\n"
                                           u"}\n")

        self.elemProfListWgtVL = QVBoxLayout(self.home2_WGT)
        self.elemProfListSA = QScrollArea(self.home2_WGT)
        self.elemProfListSA.setWidgetResizable(True)
        self.elemProfListSAWgt = QWidget()

        self.elemProfListSAWgtGL = QGridLayout(self.elemProfListSAWgt)
        self.elemProfListSAWgtGL.setVerticalSpacing(0)
        self.elemProfListSA.setWidget(self.elemProfListSAWgt)
        self.elemProfListWgtVL.addWidget(self.elemProfListSA)

        self.homeHBL.insertWidget(1, self.home2_WGT)

        lblfont = QtGui.QFont()
        lblfont.setFamily(u"MS Shell Dlg 2")
        lblfont.setPointSize(12)
        lblfont.setBold(True)
        lblfont.setItalic(False)
        lblfont.setWeight(75)

        pt = dict()
        for cat in list(bench['categories'].keys()):
            pt[cat] = {'elements': [],}
            for el in v:
                if v[el]['category'] == cat:
                    pt[cat]['elements'].append(el)
            if pt[cat]['elements']:
                self.__setattr__(cat + 'Lbl', QtWidgets.QLabel(cat))
                self.__getattribute__(cat + 'Lbl').setMinimumHeight(30)
                self.__getattribute__(cat + 'Lbl').setMaximumHeight(30)
                self.__getattribute__(cat + 'Lbl').setFont(lblfont)
                self.__getattribute__(cat + 'Lbl').setAlignment(QtGui.Qt.AlignCenter)
                self.__getattribute__(cat + 'Lbl').setStyleSheet(u"border-top-left-radius: 15px;\n"
                                                                 u"border-top-right-radius: 15px;\n"
                                                                 u"padding: 5px 150px;\n"
                                                                 u"background-color: rgb(127, 127, 127);\n"
                                                                 u"color: rgb(255, 255, 255);\n")

                self.__setattr__(cat + 'VSpc', QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed))

                self.__setattr__(cat + 'Frm', QtWidgets.QFrame())
                self.__getattribute__(cat + 'Frm').setStyleSheet(u"*{\n"
                                                                 u"background-color: rgb(0, 0, 0);\n"
                                                                 u"color: rgb(255, 255, 255)\n"
                                                                 u"}\n\n"
                                                                 u"QFrame {\n"
                                                                 u"border: solid;\n"
                                                                 u"border-width: 2px;\n"
                                                                 u"border-color: rgb(127, 127, 127);\n"
                                                                 u"border-bottom-left-radius: 15px;\n"
                                                                 u"border-bottom-right-radius: 15px;\n"
                                                                 u"}\n\n"
                                                                 u"QLabel {\n"
                                                                 u"border-width: 0px;\n"
                                                                 u"border-radius: 0px;\n"
                                                                 u"}")

                self.__setattr__(cat + 'GL', QtWidgets.QGridLayout())
                self.__getattribute__(cat + 'Frm').setLayout(self.__getattribute__(cat + 'GL'))
                self.__getattribute__(cat + 'GL').setContentsMargins(10, 10, 10, 10)

                line = 0
                for el in pt[cat]['elements']:
                    self.__setattr__(el + 'Lbl', QtWidgets.QLabel(el))
                    self.__getattribute__(el + 'Lbl').setMinimumHeight(30)
                    self.__getattribute__(el + 'Lbl').setMaximumHeight(30)
                    self.__setattr__(el + 'CB', QtWidgets.QComboBox())
                    self.__getattribute__(cat + 'GL').addWidget(self.__getattribute__(el + 'Lbl'), line, 0)
                    self.__getattribute__(cat + 'GL').addWidget(self.__getattribute__(el + 'CB'), line, 1)

                    proflist = []
                    if isinstance(bench['categories'][cat], list):
                        for t in bench['categories'][cat]:
                            for mt in bench['profiles']:
                                try:
                                    proflist.append(bench['profiles'][mt][t])
                                    break
                                except:
                                    pass
                    elif bench['categories'][cat] in bench['profiles']:
                        mt = bench['categories'][cat]
                        for t in bench['profiles'][bench['categories'][cat]]:
                            proflist.append(bench['profiles'][bench['categories'][cat]][t])
                        # proflist = list(bench['profiles'][bench['categories'][cat]].keys())

                    else:
                        for mt in bench['profiles']:
                            try:
                                proflist.append(bench['profiles'][mt][bench['categories'][cat]])
                                break
                            except:
                                pass

                    self.__getattribute__(el + 'CB').clear()
                    self.__getattribute__(el + 'CB').addItems(proflist)

                    if v[el]['par']['profile']['name']:
                        if '_(' in v[el]['par']['profile']['name']:
                            a = v[el]['par']['profile']['name'].split('_(')
                            prof_cat = a[len(a) - 1].removesuffix(')')
                            prof_name = bench['profiles'][mt][prof_cat]
                            self.__getattribute__(el + 'CB').setCurrentText(prof_name)

                    line += 1

                self.elemProfListSAWgtGL.addWidget(self.__getattribute__(cat + 'Lbl'))
                self.elemProfListSAWgtGL.addWidget(self.__getattribute__(cat + 'Frm'))
                self.elemProfListSAWgtGL.addItem(self.__getattribute__(cat + 'VSpc'))

            else:
                pt.pop(cat)

        self.elemProfListPlsWgt = QWidget()
        self.elemProfListPlsWgtHL = QtWidgets.QHBoxLayout(self.elemProfListPlsWgt)
        self.elemProfListPlsWgtHL.setContentsMargins(50, 10, 50, 10)
        self.elemProfListSaveBtn = QtWidgets.QPushButton()
        self.elemProfListSaveBtn.setText('Salva')
        self.elemProfListSaveBtn.setMinimumSize(100, 25)
        self.elemProfListCancelBtn = QtWidgets.QPushButton()
        self.elemProfListCancelBtn.setText('Annulla')
        self.elemProfListCancelBtn.setMinimumSize(100, 25)
        self.elemProfListBtnSpc = QtWidgets.QSpacerItem(20, 50, QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        self.elemProfListPlsWgtHL.addWidget(self.elemProfListSaveBtn)
        self.elemProfListPlsWgtHL.addItem(self.elemProfListBtnSpc)
        self.elemProfListPlsWgtHL.addWidget(self.elemProfListCancelBtn)
        self.elemProfListWgtVL.addWidget(self.elemProfListPlsWgt)
        self.elemProfListPlsWgt.setStyleSheet(u"*{\n"
                                              u"}\n\n"
                                              u"QPushButton {\n"
                                              u"border: solid;\n"
                                              u"border-width: 2px;\n"
                                              u"border-color: rgb(127, 127, 127);\n"
                                              u"border-radius: 10px;\n"
                                              u"}\n\n"
                                              u"QPushButton:pressed {"
                                              u"background-color: rgb(64, 64, 64); border-style: inset"
                                              u"}")

        self.elemProfListCancelBtn.clicked.connect(self.elemProfListCancel)
        self.elemProfListSaveBtn.clicked.connect(partial(self.elemProfListSave, pt))

        if grid['benchmark']:
            filepath = mainpath + '/_benchmark/grid_models/' + grid['name'] + '_ProfCat.yml'
            if os.path.exists(filepath):
                print(grid['name'])
                pl = yaml.safe_load(open(filepath))
                for el in pl:
                    # self.__getattribute__(el + 'CB').setCurrentText('Agricolo')
                    self.__getattribute__(el + 'CB').setCurrentText(pl[el])

        pass

    def elemProfListSave(self, pt):
        pl = self.elemProfListCopmile(pt)

        prof = False
        if not grid['profile']['exist']:
            popup1 = GridProfParDlg()
            if popup1.exec_():
                pass
            prof = popup1.confirmed

        print(grid['profile']['start'])
        print(grid['profile']['end'])

        if prof:
            import defProfImport as dpi
            for el in pl:
                v[el]['par']['profile']['name'], v[el]['par']['profile']['curve'] = (
                        dpi.defaultProfileImport(el, pl[el]))

                # print(el, )

            self.home2_WGT.deleteLater()

    def elemProfListCopmile(self, pt):
        pl = dict()
        for mcat in pt:
            for el in pt[mcat]['elements']:
                pl[el] = self.__getattribute__(el + 'CB').currentText()
        return pl

    def elemProfListCancel(self):
        self.home2_WGT.deleteLater()

    def anomStart(self):
        if self.myform.ui.verticalLayout.count() > 2:
            self.myform.ui.verticalLayout.itemAt(2).widget().deleteLater()

        variables.visualpar = 'anom'

        # self.homeHBL = QHBoxLayout()
        # self.homeHBL.setContentsMargins(0, 0, 0, 0)
        # self.home2_WGT.setLayout(self.homeHBL)

        anomRunPls = pb_create(text='   Avvia calcolo Anomalie', height=50, font=14, border=2, radius=15,
                                    icon='anomaly.png')

        self.myform.ui.verticalLayout.addWidget(anomRunPls)

        # print(self.myform.ui.verticalLayout.count())
        # print(self.myform.ui.verticalLayout.itemAt(2).widget().objectName())

        a = QVBoxLayout
        b = QWidget

        anomRunPls.clicked.connect(self.anomRun)

        # a.itemAt(1).
        # a.insertWidget()

        #  TODO: Mostrare i risultati, se disponibili

    def anomRun(self):
        print('run LCA')
        from Functionalities.Anomalies import launch_create_anomalies as lca
        anome_elem = lca.lauch_create_anomalies()
        grid['studies']['anom'] = True
        print(list(anome_elem.keys()))

    def relStart(self):
        if self.myform.ui.verticalLayout.count() > 2:
            self.myform.ui.verticalLayout.itemAt(2).widget().deleteLater()

        variables.visualpar = 'rel'

        # self.homeHBL = QHBoxLayout()
        # self.homeHBL.setContentsMargins(0, 0, 0, 0)
        # self.home2_WGT.setLayout(self.homeHBL)

        self.relRunPls = pb_create(text='   Avvia calcolo Affidabilità', height=50, font=14, border=2, radius=15,
                                   icon='reliability.png')

        self.myform.ui.verticalLayout.addWidget(self.relRunPls)
        #  TODO: Mostrare i risultati, se disponibili


class LFrWGT(QMainWindow):
    def __init__(self):
        from UI.ui_lfres import Ui_lfres_mainWGT

        super(LFrWGT, self).__init__(None)
        self.ui = Ui_lfres_mainWGT()
        self.ui.setupUi(self)

        self.ui.lfResDtePlusPb.clicked.connect(partial(self.datachange, +1))
        self.ui.lfResDteMinusPb.clicked.connect(partial(self.datachange, -1))

    def datachange(self, t):
        step = grid['profile']['step']
        time = self.ui.lfresDte.dateTime()
        # print(time)
        # a = time.toPython()
        # b = a + datetime.timedelta(minutes=step)
        # self.ui.lfresDte.setDateTime(b)
        self.ui.lfresDte.setDateTime(time.toPython() + datetime.timedelta(minutes=(step * t)))

        # print(b)


def write_excel():
    file_excel = xlsxwriter.Workbook('risultato.xlsx')
    worksheet = file_excel.add_worksheet()
    worksheet.write(0, 0, 'Results')

    lf_par = ['v', 'p', 'q', 'i']
    row, col = 1, 0
    for cat in prof_elem:
        row += 1
        worksheet.write(row, col, cat)
        row += 1

        col = 1
        for par in lf_par:
            worksheet.write(row, col, par)
            col += 1
        row += 1
        col = 0

        for el in v:
            if v[el]['category'] == cat:
                worksheet.write(row, col, el)
                col = 1
                for par in lf_par:
                    worksheet.write(row, col, v[el]['lf'][par])
                    col += 1
                row += 1
                col = 0

    for cat in ['2W-Transformer', 'PWM', 'DC-DC-Converter', 'AC-Line', 'DC-Line']:
        row += 1
        worksheet.write(row, col, cat)
        row += 1

        col = 1
        for par in lf_par:
            for i in [0, 1]:
                worksheet.write(row, col, par + str(i))
                col += 1
        row += 1
        col = 0

        for el in v:
            if v[el]['category'] == cat:
                worksheet.write(row, col, el)
                col = 1
                for par in lf_par:
                    for i in [0, 1]:
                        worksheet.write(row, col, v[el]['lf'][par][i])
                        col += 1
                row += 1
                col = 0

    file_excel.close()
    pass


def pb_create(text='Pulsante', font=16, radius=10, height=30, icon=None, padding=None, border=1):
    pls = QPushButton()
    pls.setText(text)
    pls.setMinimumHeight(height)
    if icon:
        ico = QtGui.QIcon()
        ico.addFile(u":/icons/icons/" + icon, QtCore.QSize(100, 100), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pls.setIcon(ico)
        pls.setIconSize(QtCore.QSize(30, 30))

    style = 'QPushButton {'
    style += 'font: ' + str(font) + 'px; '
    style += 'text-align: center; '
    if padding:
        style += 'padding: ' + padding[0] + 'px' + padding[1] + 'px; '
    style += 'image-position:right; '
    style += 'color: rgb(255, 255, 255); '
    style += 'background-color: rgb(31, 31, 31); '
    style += 'border: solid; '
    style += 'border-width: ' + str(border) + 'px; '
    style += 'border-radius: ' + str(radius) + 'px; '
    style += 'rgb(127, 127, 127);'
    style += '} '
    style += 'QPushButton:pressed {background-color: rgb(64, 64, 64); border-style: inset}'

    # pls.setStyleSheet(style)

    # style += ''
    # style += ''
    #
    #
    #
    pls.setStyleSheet(u"QPushButton {"
                      u"font: " + str(font) + "px;"
                      u"text-align: center;"
                      u"padding: 10px 20px;"
                      u"image-position:right;"
                      u"color: rgb(255, 255, 255);"
                      u"background-color: rgb(31, 31, 31); border: solid;"  # border-style: outset;"
                      u"border-width: 2px; border-radius: " + str(radius) + "px; border-color: rgb(127, 127, 127);"
                      u"}"
                      u"QPushButton:pressed {"
                      u"background-color: rgb(64, 64, 64); border-style: inset"
                      u"}")
    return pls


Main()

