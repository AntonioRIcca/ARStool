# import py_dss_interface
# from PySide2.QtCharts import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis
import os.path
from functools import partial
import xlsxwriter

from PySide2 import QtGui, QtCore, QtWidgets

from PySide2.QtCharts import *

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

from UI.test_elementProperties import ElementProperties
from UI.elementProperties import Window
from UI.elementsProfile import ElementsProfile
from UI.newItem import NewItem

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
        # self.app = QApplication(sys.argv)
        self.interface_open()       # TODO: da elimianre da questa posizione: va dopo la scelta della rete

        # f_main = Thread(target=self.interface_open)
        # print('start')
        # f_main.start()

    def interface_open(self):
        os.chdir(mainpath)
        self.mainwindow = MainWindow()
        self.ui = self.mainwindow.ui
        self.ui.mainBodyContent.setStyleSheet(u'#mainBodyContent{background-image: url(ARStool500_shadow.png);'
                                              u'background-repeat: no-repeat;'
                                              u'background-position: center;}')
        self.mainwindow.show()

        self.func_check()

        # self.ui.label_10.setText('APERTO!!!')
        #
        # from UI.table_wgt import Table
        # self.myform = Table()
        # mywidget = self.myform.ui.widget
        #
        # self.ui.homeSW.removeWidget(self.ui.homeSW.currentWidget())
        # self.ui.homeSW.addWidget(mywidget)

        self.startWgtCreate()
        # self.elementsTableWgtCreate()                                               # TODO: da riattivare

        # self.homeWGT_create()                                                     # TODO: da NON riattivare
        self.ui.mainPages.setCurrentIndex(0)

        # self.elementsTableFill()                                                  # TODO: da NON riattivare

        # self.myform.ui.tableWidget.currentCellChanged.connect(self.test_action)   # TODO: da NON riattivare

        self.ui.profileMenuBtn.clicked.connect(self.test_action2)
        self.ui.moreMenuBtn.clicked.connect(self.test_action2)
        self.ui.lf_Btn.clicked.connect(self.loadflow)
        self.ui.restartBtn.clicked.connect(self.startWgtCreate)

        # Window(list(v.keys())[0])                                                 # TODO: da NON riattivare
        # self.ui.rightMenuContainer.expandMenu()

        self.app.exec_()
        # exit(self.app.exec_())
        # print(3)

    def func_disabled(self):
        self.ui.lf_Btn.setEnabled(False)

    # TODO: deve verificare la disponibilità delle funzioni della rete ed abilitare le funzioni selettivamente
    def func_enabled(self):
        self.ui.loadflow_Btn.setEnabled(True)

    def func_check(self):
        for btn in fn_en:
            self.ui.__getattribute__(btn + '_Btn').setVisible(fn_en[btn])

        # self.ui.lf_Btn.setVisible(True)

    def startWgtCreate(self):
        for f in fn:
            fn[f] = False
            
        self.savepath = os.path.join(os.environ['USERPROFILE'], 'Desktop')

        try:
            self.ui.home_WGT.deleteLater()
        except:
            self.home_WGT.deleteLater()
        self.home_WGT = QWidget()


        # self.homeHBL = QHBoxLayout(self.home_WGT)
        self.homeHBL = QHBoxLayout()
        self.home_WGT.setLayout(self.homeHBL)
        self.homeHBL.setContentsMargins(0, 0, 0, 0)

        from UI.start_wgt import StartWGT
        self.startWGT = StartWGT()
        # self.startWGT = self.myform.ui.startWgt
        self.startWGT.ui.startWgt.setMinimumSize(QtCore.QSize(300, 0))

        self.homeHBL.addWidget(self.startWGT.ui.startWgt, 0, QtCore.Qt.AlignLeft)

        self.ui.home_VL.addWidget(self.home_WGT)

        # Si ripete in self.elementsTableWgtCreate() --> self.homeWGT_create()
        # TODO: Capire se tutto questo può essere messo estermanemte
        self.home2_WGT = QWidget()
        self.home3_WGT = QWidget()
        # self.home3_WGT.setStyleSheet("background-color: rgb(0,0,255);")
        self.home3_WGT.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)

        self.home3_VL = QVBoxLayout(self.home3_WGT)
        self.home3_VL.setContentsMargins(0, 0, 0, 0)
        self.home3_top_WGT = QWidget()
        self.home3_center_WGT = QWidget()
        self.home3_bottom_WGT = QWidget()
        self.home3_bottom_WGT.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        # self.home3_bottom_WGT.setStyleSheet("background-color: rgb(255,0,255);")
        # self.home3_bottom_WGT.setStyleSheet(u'background-image: url(ARStool500.png);'
        #                                     u'background-repeat: no-repeat;'
        #                                     u'background-position: center;')

        self.home3_VL.addWidget(self.home3_top_WGT)
        self.home3_VL.addWidget(self.home3_center_WGT)
        self.home3_VL.addWidget(self.home3_bottom_WGT)

        # self.homeHBL.deleteLater()
        self.homeHBL.addWidget(self.home2_WGT)
        self.homeHBL.addWidget(self.home3_WGT)

        self.startWGT.ui.importDssBtn.clicked.connect(self.dss_open)
        self.startWGT.ui.openFileBtn.clicked.connect(self.yml_open)
        self.startWGT.ui.benchOpenBtn.clicked.connect(self.benchmarkWGT_create)
        self.startWGT.ui.optStorBtn.clicked.connect(self.optstor_create)


    # Creazione dell'elenco delle reti benchmark
    def benchmarkWGT_create(self):
        self.startWGT.ui.benchOpenBtn.setStyleSheet(u"background-color: rgb(63, 63, 63);")

        self.home2_WGT.deleteLater()

        self.home2_WGT = QWidget()
        self.home2_WGT.setMinimumWidth(250)
        self.bmWgtVBL = QVBoxLayout()
        self.bmWgtVBL.setSpacing(20)
        self.home2_WGT.setLayout(self.bmWgtVBL)

        bm = yaml.safe_load(open(mainpath + '/_benchmark/grid_models/grid_bench.yml'))

        for b in bm.keys():

            self.gridPls = QPushButton()
            self.gridPls.setText('  ' + bm[b]['name'])
            self.gridPls.setMinimumHeight(50)
            self.testIco = QtGui.QIcon()
            self.testIco.addFile(u":/icons/icons/importfile.png",
                                 QtCore.QSize(100, 100), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.gridPls.setIcon(self.testIco)
            self.gridPls.setIconSize(QtCore.QSize(30, 30))

            self.gridPls.setStyleSheet(u"QPushButton {"
                                       u"font: 24px;"
                                       u"text-align: left;"
                                       u"padding: 10px 20px;"
                                       u"color: rgb(255, 255, 255);"
                                       u"background-color: rgb(31, 31, 31); border: solid;"  # border-style: outset;"
                                       u"border-width: 2px; border-radius: 20px; border-color: rgb(127, 127, 127)"
                                       u"}"
                                       u"QPushButton:pressed {"
                                       u"background-color: rgb(64, 64, 64); border-style: inset"
                                       u"}")
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

        self.filepath = mainpath + '/_benchmark/grid_models/' + grid['file']
        self.dsspath = mainpath + '/_benchmark/grid_models/'
        self.gridname = gridname

        self.gridDetailsWgt.ui.open.clicked.connect(partial(self.dss_open, self.filepath))
        self.yml_bench_save()

        # self.main.ui.EV303_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/arrowSX_20x20.png")

        # self.home3_WGT.setSizePolicy(QSizePolicy.Policy.Minimum)

    # Apertura del file DSS
    def dss_open(self, filename=None):
        v_initialize()
        if not filename:
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog

            filename, ext = QtWidgets.QFileDialog.getOpenFileName(caption="Apri file DSS",
                                                                  dir=self.savepath,
                                                                  filter='*.dss')

            self.gridname = 'externalDSS'

        if filename:
            # self.dss = opendss.OpenDSS()

            # TODO: Da ripristinare
            # try:
            #     self.dss.open(filename)
            #     self.elementsTableWgtCreate()
            #     print('tabella')
            #     # self.func_enabled()
            #     self.func_check()
            # except:
            #     QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Attenzione', 'Modello DSS non compatibile')

            # TODO: da eliminare
            self.dss.open(filename)
            self.elementsTableWgtCreate()
            # self.func_enabled()
            self.func_check()

    def yml_open(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog

        filename, ext = QtWidgets.QFileDialog.getOpenFileName(caption="Apri file di rete",
                                                              dir=self.savepath,
                                                              filter='*.yml')

        if filename:
            name = filename.split('/')
            self.savepath = filename.removesuffix(name[len(name)-1])
            self.gridname = name[len(name)-1].split('.')[0]
            v0 = yaml.safe_load(open(filename))
            for elem in v0:
                v[elem] = v0[elem]
            self.elementsTableWgtCreate()
            # self.func_enabled()
            self.func_check()

            # a = 'as'
            # a.re

    def yml_bench_save(self):
        filename = self.dsspath + '/' + self.gridname + '.yml'
        with open(filename, 'w') as file:
            yaml.dump(v, file)
            file.close()

    # Salvataggio del file YML della rete
    def yml_save(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog

        filename, ext = QtWidgets.QFileDialog.getSaveFileName(caption="Salva configurazione di rete",
                                                              dir=self.savepath + '/' + self.gridname,
                                                              filter='*.yml')

        if filename:
            with open(filename, 'w') as file:
                yaml.dump(v, file)
                file.close()

    # Inserimento della tabella degli elementi nel widget principale
    def elementsTableWgtCreate(self):
        self.homeWGT_create()
        self.elementsTableFill()
        self.myform.ui.tableWidget.currentCellChanged.connect(self.test_action)
        self.myform.ui.save_Btn.clicked.connect(self.yml_save)
        self.myform.ui.add_Btn.clicked.connect(self.new_element)
        self.myform.ui.del_Btn.clicked.connect(self.del_element)
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

    def readsize(self):
        self.par_wgt = Window('rs_line')
        self.ui.rightMenuPages.addWidget(self.par_wgt.mywidget)
        self.ui.rightMenuPages.setCurrentIndex(2)
        pass

    def elementsTableFill(self):
        self.myform.ui.tableWidget.clear()
        self.myform.ui.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Nome Elemento'))
        self.myform.ui.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Categoria'))

        self.myform.ui.tableWidget.setRowCount(len(v))

        i = 0
        for elem in v:
            self.myform.ui.tableWidget.setItem(i, 0, QTableWidgetItem(elem))
            self.myform.ui.tableWidget.setItem(i, 1, QTableWidgetItem(v[elem]['category']))
            i += 1
        self.elementsTableFormat()

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
        line = self .myform.ui.tableWidget.currentRow()
        self.elem = self.myform.ui.tableWidget.item(line, 0).text()
        self.myform.ui.del_Btn.setVisible(True)
        # dss.writeline(elem)   TODO: ???????

        try:
            self.ui.rightMenuPages.removeWidget(self.ui.rightMenuPages.widget(2))
        except:
            pass

        self.ui.rightMenu_LBL.setText(self.elem)
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
        # # print(self.ui.rightMenuPages.count())
        # --------------------------------------------------------------------------------------

        # self.ui.lfWgtPls.clicked.connect(self.myaction1)
        # self.ui.relWgtPls.clicked.connect(self.myaction2)
        # self.ui.lfWgtPls.clicked.connect(self.ui.lfWgt.expandMenu)
        # self.ui.relWgtPls.clicked.connect(self.ui.lfWgt.collapseMenu)

        # -- Nuovo richiamo alla form ---------------------------------------------------------- TODO: da riattivare
        self.elemPropWgt = ElementProperties(self.elem)
        self.ui.rightMenuPages.addWidget(self.elemPropWgt.ui.propertiesWgt)
        # self.par_wgt.mainWidget.setMinimumHeight(1200)

        self.ui.rightMenuPages.setCurrentIndex(self.ui.rightMenuPages.count() - 1)
        self.elemPropWgt.ui.lfPls.clicked.connect(self.myaction1)
        self.elemPropWgt.ui.relPls.clicked.connect(self.myaction2)

        self.elemPropWgt.ui.cancelPLS.clicked.connect(self.ui.rightMenuContainer.collapseMenu)

        try:
            self.elemPropWgt.profile_RB.toggled.connect(self.profile_switch)
            self.elemPropWgt.profileBtn.clicked.connect(self.profile_open)
        except AttributeError:
            pass
        # --------------------------------------------------------------------------------------
        pass

    def myaction1(self):
        # self.ui.relWgt.collapseMenu()
        # self.ui.lfWgt.expandMenu()
        self.elemPropWgt.ui.lfWgt.setMaximumHeight(1500)
        self.elemPropWgt.ui.relWgt.setMaximumHeight(20)

    def myaction2(self):

        self.elemPropWgt.ui.relWgt.setMaximumHeight(1500)
        self.elemPropWgt.ui.lfWgt.setMaximumHeight(20)

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
        popup = ElementsProfile(self.elem)

        if popup.exec_():
            pass

        if popup.refresh:
            self.elemPropWgt.profileWgtRefresh()
            self.elemPropWgt.profileBtn.clicked.connect(self.profile_open)

    def profile_switch(self):
        # self.elemPropWgt.profileCheck()
        if self.elemPropWgt.profile_RB.isChecked():
            if not v[self.elem]['par']['profile']['name']:
                popup = ElementsProfile(self.elem)

                if popup.exec_():
                    pass

                if popup.refresh:
                    self.elemPropWgt.profilePlotWgtCreate()
                    self.elemPropWgt.ui.lfVL.insertWidget(3, self.elemPropWgt.profileWidget)
                    self.elemPropWgt.profileBtn.clicked.connect(self.profile_open)

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


    def test_action2(self, mcat, event=None):
        # print(self.ui.rightMenuPages.currentIndex())
        # -- Creazione del diagramma delle generazioni ---------------------------
        # Todo: da definire come gestire i dati  del diagramma
        from UI.donutbreakdown2 import DonutBreakdownChart
        db_graph = DonutBreakdownChart(mcat=mcat, data=self.lf_cat[mcat])

        self.home3_top_WGT.deleteLater()
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
        # self.homeHBL.addWidget(self.homeDxWGT)

        # self.ui.homeSW.removeWidget(self.ui.homeSW.currentWidget())
        self.ui.home_VL.addWidget(self.home_WGT)
        # self.ui.home_SW.insertWidget(0, self.ui.home_WGT)
        # self.ui.mainPages.setCurrentIndex(1)
        # print(self.ui.mainPages.currentIndex())
        # self.ui.mainPages.setCurrentWidget(self.ui.home_WGT)

        # super(lfWGT, self).__init__()
        # wgt = LFrWGT()
        # self.lfWGT = wgt.ui.lfres_WGT
        #
        # self.homeHBL.addWidget(self.lfWGT)

        # self.widget2 = QWidget()
        # # self.lbl = QLabel(self.widget2)
        # # self.lbl.setText('ooooooooooooo')
        # self.widget2.setStyleSheet("background-color:rgb(255,0,0);")
        # self.widget2.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        # self.homeHBL.addWidget(self.widget2)
        # self.homeDxWGT.setStyleSheet("background-color: rgb(0,255,0);")

        # self.homeHBL.removeWidget(self.homeDxWGT)
        # self.homeDxWGT = QWidget()
        self.home2_WGT = QWidget()
        self.home3_WGT = QWidget()
        # self.home3_WGT.setStyleSheet("background-color: rgb(0,0,255);")
        self.home3_WGT.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)

        self.home3_VL = QVBoxLayout(self.home3_WGT)
        self.home3_VL.setContentsMargins(0, 0, 0, 0)
        self.home3_top_WGT = QWidget()
        self.home3_center_WGT = QWidget()
        self.home3_bottom_WGT = QWidget()
        self.home3_bottom_WGT.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        # self.home3_bottom_WGT.setStyleSheet("background-color: rgb(255,0,255);")

        self.home3_VL.addWidget(self.home3_top_WGT)
        self.home3_VL.addWidget(self.home3_center_WGT)
        self.home3_VL.addWidget(self.home3_bottom_WGT)

        # self.homeHBL.deleteLater()
        self.homeHBL.addWidget(self.home2_WGT)
        self.homeHBL.addWidget(self.home3_WGT)

        # self.homeDxWGT.deleteLater()

        # self.barchart()

        # -- Creazione del diagramma a torta ---------------------------
        # Todo: da definire come gestire i dati  deò diagramma
        # from UI.piechart import PieChart
        # chart = PieChart()
        # chart_view = QtCharts.QChartView(chart)
        #
        # self.lf_WGT.ui.image_VL.addWidget(chart_view)
        # --------------------------------------------------------------

    def barchart(self):
        # set0 = QtCharts.QBarSet('Parwix')
        # set1 = QtCharts.QBarSet('Bob')
        # set2 = QtCharts.QBarSet('Tom')
        # set3 = QtCharts.QBarSet('Logan')
        # set4 = QtCharts.QBarSet('Karim')
        #
        # set0 << 1 << 2 << 3 << 4 << 5 << 6
        # set1 << 5 << 0 << 0 << 4 << 0 << 7
        # set2 << 3 << 5 << 8 << 13 << 8 << 5
        # set3 << 5 << 6 << 7 << 3 << 4 << 5
        # set4 << 9 << 7 << 5 << 3 << 1 << 1
        #
        # series = QtCharts.QPercentBarSeries()
        # series.append(set0)
        # series.append(set1)
        # series.append(set2)
        # series.append(set3)
        # series.append(set4)
        #
        # chart = QtCharts.QChart()
        # chart.addSeries(series)
        # chart.setTitle('Percent BarChart Example')
        # chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        #
        # categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', ]

        cat = ['External Grid', 'Generation', 'Loads', 'BESS', 'Losses']
        p = ['eg', 'gen', 'loads', 'bess', 'loss']
        series = QtCharts.QPercentBarSeries()

        for i in range(5):
            self.__setattr__('set' + str(i), QtCharts.QBarSet(cat[i]))
            if cat[i] in ['Generation', 'External Grid']:
                if self.__getattribute__('p_' + p[i]) >= 0:
                    self.__getattribute__('set' + str(i)).append([self.__getattribute__('p_' + p[i]), 0])
                else:
                    self.__getattribute__('set' + str(i)).append([0, self.__getattribute__('p_' + p[i])])
            else:
                if self.__getattribute__('p_' + p[i]) >= 0:
                    self.__getattribute__('set' + str(i)).append([0, self.__getattribute__('p_' + p[i])])
                else:
                    self.__getattribute__('set' + str(i)).append([self.__getattribute__('p_' + p[i]), 0])

            series.append(self.__getattribute__('set' + str(i)))

        # series = QtCharts.QPercentBarSeries()
        # set0 = QtCharts.QBarSet('External Grid')
        # set1 = QtCharts.QBarSet('Generation')
        # set2 = QtCharts.QBarSet('Loads')
        # set3 = QtCharts.QBarSet('BESS')
        # set4 = QtCharts.QBarSet('Losses')
        #
        # set0.append([1800, 1000])
        # set1.append([1500, 0])
        # set2.append([0, 3200])
        # set3.append([0, 100])
        # set4.append([0, 500])
        # # set4 << 9 << 7 << 5 << 3 << 1 << 1
        #
        # series.append(set0)
        # series.append(set1)
        # series.append(set2)
        # series.append(set3)
        # series.append(set4)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        # chart.setTitle('Percent BarChart Example')
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        categories = ['In', 'Cons']

        axis = QtCharts.QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
        chart.setBackgroundBrush(QtGui.QBrush(QtGui.QColor('transparent')))
        # chart.legend().setLabelColor('white')
        chart.legend().setLabelColor(QtGui.QColor('white'))
        chart.setTitleBrush(QtGui.QColor(255, 255, 255))
        chart.setTitleFont(QtGui.QFont("Arial", 12))
        chart.axisX().setLabelsColor(QtGui.QColor(255, 255, 255))
        chart.axisY().setLabelsColor(QtGui.QColor(255, 255, 255))
        # chart.axisY().__format__("%.0f")
        chart.axisY().setLabelFormat("%.0f%%")
        chart.legend().setFont(QtGui.QFont("Arial", 10))

        # self.home3_top_WGT.deleteLater()

        self.lf_WGT.ui.lfres_bottom_WGT.deleteLater()

        lfres_bottom_wgt = QtCharts.QChartView(chart)
        self.lf_WGT.ui.lfres_VL.insertWidget(3, lfres_bottom_wgt)

    def loadflow(self):
        self.ui.rightMenuContainer.collapseMenu()
        try:
            self.home2_WGT.deleteLater()
        except RuntimeError:
            pass

        # from UI.lfMod_Dlg import LfModDlg
        # lf_popup = LfModDlg()
        #
        # if lf_popup.exec_():
        #     print('popup')
        #     pass
        # print('popup closed')



        self.dss.full_parse_to_dss()
        # self.yml_bench_save()
        # dss.write_all()
        # dss.solve()

        # write_excel()

        # self.dss.test()  # TODO: da eliminare, è una prova

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
                self.p_loads += v[elem]['lf']['p']
                self.q_loads += v[elem]['lf']['q']
                mcat = 'Loads'

            elif v[elem]['category'] in mc['BESS']:
                self.p_bess += v[elem]['lf']['p']
                self.q_bess += v[elem]['lf']['q']
                mcat = 'BESS'

            elif v[elem]['category'] in mc['Generator']:
                self.p_gen -= v[elem]['lf']['p']
                self.q_gen -= v[elem]['lf']['q']
                mcat = 'Generators'

            if cat in prof_elem:
                if cat not in list(self.lf_cat[mcat].keys()):
                    self.lf_cat[mcat][cat] = dict()
                self.lf_cat[mcat][cat][elem] = {
                    'p': abs(v[elem]['lf']['p']),
                    'q': abs(v[elem]['lf']['q']),
                }

        self.p_eg, self.q_eg = -v['source']['lf']['p'], -v['source']['lf']['q']
        self.p_loss = self.p_eg + self.p_gen - self.p_loads - self.p_bess
        self.q_loss = self.q_eg + self.q_gen - self.q_loads - self.q_bess

        self.lf_WGT = LFrWGT()
        self.home2_WGT = self.lf_WGT.ui.lfres_WGT

        self.homeHBL.insertWidget(1, self.home2_WGT)

        self.lf_WGT.ui.gen_GB.mouseDoubleClickEvent = partial(self.test_action2, 'Generators')
        self.lf_WGT.ui.loads_GB.mouseDoubleClickEvent = partial(self.test_action2, 'Loads')
        self.lf_WGT.ui.bess_GB.mouseDoubleClickEvent = partial(self.test_action2, 'BESS')

        for cat in ['eg', 'loss', 'loads', 'bess', 'gen']:
            self.lf_WGT.ui.__getattribute__('p_' + cat + '_value_LBL').setText(
                str(round(self.__getattribute__('p_' + cat), 2)))
            self.lf_WGT.ui.__getattribute__('q_' + cat + '_value_LBL').setText(
                str(round(self.__getattribute__('q_' + cat), 2)))

        self.barchart()

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

        # print('LF done')

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
    #             # print(el)
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
        # print(str(a))

        self.home3_center_WGT.deleteLater()

        self.home3_center_WGT = QWidget()
        # self.home3_center_WGT.setStyleSheet("font: 10pt")
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.home3_center_WGT.setFont(font)
        # self.home3_center_WGT.setFont(QtGui.QFont().setPointSize(20))
        self.home3_center_VL = QVBoxLayout(self.home3_center_WGT)
        self.home3_center_VL.setSpacing(0)
        # self.home3_center_VL.setContentsMargins()
        for cat in self.lf_cat[mcat]:
            self.__setattr__('home3_' + cat + '_top_LN', QFrame())
            self.__getattribute__('home3_' + cat + '_top_LN').setStyleSheet('border: 1px solid rgb(255, 255, 255);')
            self.__getattribute__('home3_' + cat + '_top_LN').setFrameShape(QFrame.HLine)

            self.__setattr__('home3_' + cat + '_WGT', QWidget())

            # self.__getattribute__('home3_' + cat + '_WGT').setStyleSheet(
            #     '#home3_' + cat + '_WGT{'
            #     'border-top: 1px solid rgb(255,255,255);'
            #     'border-bottom: 1px solid rgb(255,255,255);'
            #     '}'
            # )

            # print(self.__getattribute__('home3_' + cat + '_WGT').styleSheet())

            self.__setattr__('home3_' + cat + '_HL', QHBoxLayout(self.__getattribute__('home3_' + cat + '_WGT')))
            self.__getattribute__('home3_' + cat + '_HL').setContentsMargins(0, 0, 0, 0)
            self.__setattr__('home3_' + cat + '_sx_LBL', QLabel(cat))
            self.__setattr__('home3_' + cat + '_ctr_WGT', QWidget())
            self.__setattr__('home3_' + cat + '_dx_WGT', QWidget())
            sizepolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
            # sizepolicy1.setHorizontalStretch(2)
            sizepolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            # sizepolicy2.setHorizontalStretch(1)
            sizepolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
            # sizepolicy3.setHorizontalStretch(2)

            self.__getattribute__('home3_' + cat + '_sx_LBL').setSizePolicy(sizepolicy1)
            self.__getattribute__('home3_' + cat + '_sx_LBL').setMinimumSize(80, 0)

            self.__getattribute__('home3_' + cat + '_sx_LBL').setAlignment(QtGui.Qt.AlignRight | QtGui.Qt.AlignVCenter)
            self.__getattribute__('home3_' + cat + '_sx_LBL').setStyleSheet(u'font: bold 12pt "MS Shell Dlg 2"')
            self.__getattribute__('home3_' + cat + '_ctr_WGT').setSizePolicy(sizepolicy2)
            self.__getattribute__('home3_' + cat + '_dx_WGT').setSizePolicy(sizepolicy3)
            # self.__getattribute__('home3_' + cat + '_dx_WGT').setSizePolicy(QSizePolicy.MinimumExpanding,
            #                                                                    QSizePolicy.Preferred)
            self.__getattribute__('home3_' + cat + '_HL').addWidget(self.__getattribute__('home3_' + cat + '_sx_LBL'))
            self.__getattribute__('home3_' + cat + '_HL').addWidget(self.__getattribute__('home3_' + cat + '_ctr_WGT'))
            self.__getattribute__('home3_' + cat + '_HL').addWidget(self.__getattribute__('home3_' + cat + '_dx_WGT'))

            self.__setattr__('home3_' + cat + '_VL', QVBoxLayout(self.__getattribute__('home3_' + cat + '_ctr_WGT')))
            self.__getattribute__('home3_' + cat + '_VL').setSpacing(0)
            # self.__getattribute__('home3_' + cat + '_VL').setContentsMargins(0, 0, 0, 0)

            # self.__setattr__('home3_' + cat + '_VL', QVBoxLayout(self.__getattribute__('home3_' + cat + '_WGT')))

            self.home3_center_VL.addWidget(self.__getattribute__('home3_' + cat + '_top_LN'))
            self.home3_center_VL.addWidget(self.__getattribute__('home3_' + cat + '_WGT'))
            for elem in self.lf_cat[mcat][cat]:
                self.__setattr__('home3_' + elem + '_WGT', QWidget())
                # print('home3_' + elem + '_WGT')
                self.__setattr__('home3_' + elem + '_HL', QHBoxLayout(self.__getattribute__('home3_' + elem + '_WGT')))
                self.__getattribute__('home3_' + elem + '_HL').setContentsMargins(0, 5, 0, 5)

                self.__setattr__('home3_' + elem + '_name_LBL', QLabel(elem + ':'))
                self.__setattr__('home3_' + elem + '_color_WGT', QWidget())
                # self.__setattr__('home3_' + elem + '_p_LBL', QLabel((f"{self.lf_cat[mcat][cat][elem]['p']:.1f}")))
                self.__setattr__('home3_' + elem + '_p_LBL', QLabel())
                self.__getattribute__('home3_' + elem + '_p_LBL',).setText(f"{self.lf_cat[mcat][cat][elem]['p']:.1f}")

                # QLabel(QtCore.QObject())

                # self.__setattr__('home3_' + elem + '_unit_LBL', QLabel('kW'))
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
                # self.__getattribute__('home3_' + elem + '_name_LBL').setMinimumSize(150, 0)
                self.__getattribute__('home3_' + elem + '_p_LBL').setSizePolicy(QSizePolicy.Fixed,
                                                                                QSizePolicy.Preferred)
                self.__getattribute__('home3_' + elem + '_p_LBL').setMinimumSize(50, 0)
                # self.__getattribute__('home3_' + elem + '_unit_LBL').setSizePolicy(QSizePolicy.MinimumExpanding,
                #                                                                    QSizePolicy.Preferred)
                self.__getattribute__('home3_' + elem + '_p_LBL').setAlignment(QtGui.Qt.AlignRight)

                # mycolor = QtGui.QColor(50, 50, 50)
                self.__getattribute__('home3_' + elem + '_name_LBL').setStyleSheet('color: ' + mycolor)

                self.__getattribute__('home3_' + cat + '_VL').addWidget(self.__getattribute__('home3_' + elem + '_WGT'))
            i += 1

        self.home3_table_bottom_LN = QFrame()
        self.home3_table_bottom_LN.setStyleSheet('border: 1px solid rgb(255, 255, 255);')
        self.home3_table_bottom_LN.setFrameShape(QFrame.HLine)
        self.home3_center_VL.addWidget(self.home3_table_bottom_LN)

        self.home3_VL.insertWidget(1, self.home3_center_WGT)
        self.home3_VL.insertWidget(0, self.home3_top_WGT)
        #
        # self.home3_PV_WGT.setObjectName(u"#home3_PV_WGT")
        # self.home3_PV_WGT.setStyleSheet(u"#home3_PV_WGT{\n"
        #                                 "	border-top: 1px solid rgb(85, 255, 127);\n"
        #                                 "	border-bottom: 1px solid rgb(255, 255, 0);\n"
        #                                 "   background-color: rgb(0,255,0);\n"
        #                                 "}"
        #                                 )
        # print(self.home3_PV_WGT.styleSheet())
        # self.home3_PV_WGT.setStyleSheet(u'border-top: 1px solid rgb(255,255,255);'
        #                                 u'border-bottom: 1px solid rgb(255,255,255);')

    def optstor_create(self):
        from Functionalities.OptimalStorage.optimalStorage import OptStorWGT

        try:
            self.ui.home_WGT.deleteLater()
        except:
            self.home_WGT.deleteLater()

        self.optStorWgt = OptStorWGT()

        self.home_WGT = self.optStorWgt.ui.optStorWgt

        # # self.homeHBL = QHBoxLayout(self.home_WGT)
        # self.homeHBL = QHBoxLayout()
        # self.home_WGT.setLayout(self.homeHBL)
        # self.homeHBL.setContentsMargins(0, 0, 0, 0)
        #
        self.ui.home_VL.addWidget(self.home_WGT)
        #
        # self.startWGT.ui.optStorBtn.setStyleSheet(u"background-color: rgb(63, 63, 63);")
        #
        # self.home2_WGT.deleteLater()
        #
        # self.home2_WGT = QWidget()
        # self.home2_WGT.setMinimumWidth(250)
        # self.optStorWgtVBL = QVBoxLayout()
        # self.optStorWgtVBL.setSpacing(20)
        # self.home2_WGT.setLayout(self.optStorWgtVBL)
        #
        # self.optStorWgt = OptStorWGT()
        # self.optStorWgt.ui.resultsWgt.setVisible(False)
        # # self.home2_WGT = self.optStorWgt.ui.optStorWgt
        # self.OptStorInputWgt = self.optStorWgt.ui.leftWgt
        # # self.home2_WGT.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        # self.home2_WGT.setStyleSheet(u'background-color: rgb(0, 200, 0);')
        #
        # self.homeHBL.insertWidget(0, self.OptStorInputWgt)
        #
        # spacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)
        # spacerWgt = QtWidgets.QWidget()
        # spacerWgt.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        # # spacerWgt.setGeometry(1000, 1000, 1000, 1000)
        # spacerWgt.setStyleSheet(u'background-color: rgb(0, 0, 200);')
        # # self.homeHBL.insertItem(1, spacer)
        # self.homeHBL.insertWidget(2, spacerWgt)
        # self.optStorWgt.ui.calcPb.clicked.connect(self.optStorWgt.ui.resultsWgt.setVisible(True))

class LFrWGT(QMainWindow):
    def __init__(self):
        from UI.ui_lfres import Ui_lfres_mainWGT

        super(LFrWGT, self).__init__(None)
        self.ui = Ui_lfres_mainWGT()
        self.ui.setupUi(self)


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
        # worksheet.write(2, 10, 'pepe')

        for el in v:
            # print(el)
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


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     # mw = QMainWindow()
#     window = LFrWGT()
#     # window.ui.setupUi(mw)
#     window.show()
#
#     sys.exit(app.exec_())

# TODO: Sosopesi ----------------
# dss = opendss.OpenDSS()
#
# filename = 'C:/Users/anton/PycharmProjects/ARStool/CityArea.dss'
#
# dss.open(filename)
#  -------------------------------


# print(list(v.keys())[0])

# dss.write_all()

# dss.solve_profile()
# dss.solve()

# dss.losses_calc()
#
# print(dss.dss.circuit.total_power)
#
# el = 'pros_pv'
# v[el]['par']['P'] = 200
# dss.write('pros_pv')
# dss.solve()
#
# print(dss.dss.circuit.total_power)

Main()
print(300)

# with open('CityArea.yml', 'w') as file:
#     yaml.dump(v, file)
#     file.close()
# print('end')


# print('end2')

# Apri file

#
#
# # -- VECCHIO CODICE -------------------------------------------------------------------------------------------------
#
# dss = py_dss_interface.DSS(r"C:\Program Files\OpenDSS")
# dss_file = r"C:\Users\anton\PycharmProjects\OpenDSS\CityArea.dss"
#
# dss.text(f"compile [{dss_file}")
#
# dss.solution.solve()
#
# converged = dss.solution.converged
#
# # dss.text('Show voltage LN node')
#
# bus = dict()
#
# buses = dss.circuit.buses_names
#
# bus_V = dss.circuit.buses_vmag
#
# # dss.circuit_set_active_element('Load.UG_SERV_AC-LOAD1')
# # print(dss.cktelement_currents())
# # print(dss.cktelement_currents_mag_ang())
#
# print('\n\n')
# # print('Load.UG_SERV_AC-LOAD1')
#
# params = ['currents_mag_ang', 'currents', 'variables_values', 'name', 'property_names', 'variables_names',
#           'cplx_seq_currents', 'cplx_seq_voltages', 'energymeter', 'has_switch_control', 'has_volt_control',
#           'is_terminal_open', 'losses', 'node_order', 'num_conductors', 'num_controls', 'num_phases',
#           'num_properties', 'num_terminals', 'ocp_dev_index', 'ocp_dev_type', 'phase_losses', 'powers', 'bus_names',
#           'display', 'emerg_amps', 'is_enabled', 'norm_amps', 'residuals_currents', 'seq_currents', 'seq_powers',
#           'seq_voltages', 'voltages', 'voltages_mag_ang', 'y_prim']
# print('\n\n')
#
# for e in dss.circuit.elements_names:
#     print(e)
#     vdss[e] = dict()
#     dss.circuit.set_active_element(e)
#     for p in params:
#         # print(p + ' = ' + str(dss.cktelement_currents_mag_ang()))
#         # dss.cktelement_currents_mag_ang()
#         print(p)
#         print(p + ' = ' + str(dss.cktelement.__getattribute__('_' + p)()))
#         # dss.cktelement._is
#         vdss[e][p] = dss.cktelement.__getattribute__('_' + p)()
#
#     print('\n')
#
# # print('kW = ' + str(dss.dssproperties_read_value('kW')))
# # print('kW = ' + str(dss.dssproperties_read_value('Load.UG_SERV_AC-LOAD1')))
#
#
# print(dss.circuit.elements_names)
#
# i = 0
# for i in range(0, len(buses)):
#     bus[buses[i]] = dict()
#     for j in range(0, 3):
#         bus[buses[i]][j + 1] = dict()
#         bus[buses[i]][j + 1]['V'] = bus_V[3 * i + j]
#
# elem = dict()
# elem_names = dss.circuit.elements_names
#
# bus_names = dss.circuit.nodes_names
#
# # for el in elem_names:
# #     elem[el] = dict()
# #     dss.circuit.set_active_element(el)
# #     curr = dss.cktelement._currents_mag_ang()
# #     elem[el]['i'] = dict()
# #     for i in range(0, 3):
# #         elem[el]['i'][i] = curr[i * 2]
# #     elem[el]['i']['n'] = curr[6]
#
# for el in elem_names:
#     [macro_cat, name] = el.split('.')
#     # c = name.split('_')[len(name.split('_'))-1]
#     # print(c, mc[macro_cat])
#     try:
#         cat = c[name.split('_')[len(name.split('_'))-1]]
#     except KeyError:
#         cat = 'undefined'
#
#     print(name + ': ' + cat)
#
#     # print(el, dss.cktelement._property_names())
#
# # for el in elem_names:
# #     if
#
# with open('grid.yml', 'w') as file:
#     yaml.dump(vdss, file)
#     file.close()
# # print('here')
#
# dss.circuit.set_active_element('Load.rs_2_ac-load')
# print('\n\n\n\n')
# print(dss.loads.name)
# print(dss.loads.kw)
# print(dss.loads.names)
#
# dss.circuit.set_active_element('Vsource.source')
# # nodes = dss.cktelement.bus_names
# for node in dss.cktelement.bus_names:
#     if node not in elem.keys():
#         elem[node] = dict()
#         elem[node]['category'] = 'AC-Node'
#         elem[node]['par'] = dict()
#         elem[node]['par']['Vn'] = dss.vsources.base_kv
#         elem[node]['top'] = dict()
#         elem[node]['top']['conn'] = ['source']
#
# unr_conv = []
# unr_line = []
#
# for el in elem_names:
#     dss.circuit.set_active_element(el)
#
#     mcat = str(el).split('.')[0]
#     name = str(el).removeprefix(mcat + '.')
#     cat = name.split('_')[len(name.split('_')) - 1]
#     # if str(el).split('.')[0] == 'Generator':
#     # print(el, mcat, name, cat)
#     if mcat == 'Load':
#         print('break')
#
#     elem[name] = dict()
#     elem[name]['top'] = dict()
#     elem[name]['par'] = dict()
#     elem[name]['top']['conn'] = dss.cktelement.bus_names
#
#     # -- verifica e inizializzazione della busbar ------------
#     for i in [0, len(elem[name]['top']['conn']) - 1]:
#         bus = elem[name]['top']['conn'][i]
#         if bus not in elem.keys():
#             elem[bus] = dict()
#             elem[bus]['category'] = bus
#             elem[bus]['par'] = dict()
#             elem[bus]['par']['Vn'] = None
#             # elem[elem[name]['top']['conn'][1]]['par']['Vn'] = elem[name]['par']['Vn1']
#             elem[bus]['top'] = dict()
#             elem[bus]['top']['conn'] = [name]
#         elif name not in elem[bus]['top']['conn']:
#             elem[bus]['top']['conn'].append(name)
#     # --------------------------------------------------------
#
#     if mcat == 'Generator':
#         dss.generators.name = name
#
#         if cat == 'pv':
#             # print(el, name, dss.generators.name)
#             elem[name]['category'] = 'PV'
#             elem[name]['par']['P'] = dss.generators.kw
#             elem[name]['par']['Vn'] = dss.generators.kv
#             elem[name]['par']['profile'] = dict()
#             elem[name]['par']['profile']['name'] = None
#             elem[name]['par']['profile']['curve'] = 1
#
#         elif cat == 'bess':
#             elem[name]['category'] = 'BESS'
#             elem[name]['par']['Vn'] = dss.generators.kv
#             elem[name]['par']['P'] = dss.generators.kw
#             elem[name]['par']['cap'] = 100
#             elem[name]['par']['eff'] = 1
#
#         elif cat == 'wind':
#             elem[name]['category'] = 'Wind'
#             elem[name]['par']['Vn'] = dss.generators.kv
#             elem[name]['par']['P'] = dss.generators.kw
#             elem[name]['par']['Q'] = dss.generators.kvar
#             elem[name]['par']['f'] = dss.generators.pf
#             elem[name]['par']['eff'] = 1
#             elem[name]['par']['profile'] = dict()
#             elem[name]['par']['profile']['name'] = None
#             elem[name]['par']['profile']['curve'] = 1
#
#         elif cat == 'dc-micro-wind':
#             elem[name]['category'] = 'DC-micro-Wind'
#             elem[name]['par']['Vn'] = dss.generators.kv
#             elem[name]['par']['P'] = dss.generators.kw
#             elem[name]['par']['eff'] = 1
#             elem[name]['par']['profile'] = dict()
#             elem[name]['par']['profile']['name'] = None
#             elem[name]['par']['profile']['curve'] = 1
#
#     elif mcat == 'Transformer':
#         dss.transformers.name = name
#         unr_conv.append(name)
#
#         if cat == 'tr':       # no
#             elem[name]['category'] = '2W-Transformer'
#             bus = 'AC-Node'
#         elif cat == 'pwm':       # no
#             elem[name]['category'] = 'PWM'
#             bus = 'DC-Node'
#         elif cat == 'dc-dc-conv':       # no
#             elem[name]['category'] = '2W-Transformer'
#             bus = 'DC-Node'
#
#         elem[name]['par']['Vn1'] = dss.transformers.kv
#         elem[name]['par']['Sr'] = dss.transformers.kva
#         # elem[name]['par']['Rs'] = dss.transformers.r
#         # elem[name]['par']['Rn'] = dss.transformers.r_neut
#         elem[name]['par']['XHL'] = dss.transformers.xhl
#         # elem[name]['par']['XHT'] = dss.transformers.xht
#         # elem[name]['par']['XLT'] = dss.transformers.xlt
#         elem[elem[name]['top']['conn'][1]]['par']['Vn'] = elem[name]['par']['Vn1']
#
#         # if elem[name]['top']['conn'][1] not in elem.keys():
#         #     elem[elem[name]['top']['conn'][1]] = dict()
#         #     elem[elem[name]['top']['conn'][1]]['category'] = bus
#         #     elem[elem[name]['top']['conn'][1]]['par'] = dict()
#         #     elem[elem[name]['top']['conn'][1]]['top'] = dict()
#         #     elem[elem[name]['top']['conn'][1]]['par']['conn'] = [name]
#         # else:
#         #     elem[elem[name]['top']['conn'][1]]['par']['conn'].append(name)
#
#     elif mcat == 'Load':
#         if cat == 'ac-load':  # ok
#             elem[name]['category'] = 'AC-Load'
#             elem[name]['par']['Q'] = dss.loads.kvar
#             elem[name]['par']['f'] = dss.loads.pf
#
#         elif cat == 'dc-load':
#             elem[name]['category'] = 'DC-Load'
#
#         elem[name]['par']['P'] = dss.loads.kw
#         elem[name]['par']['Vn'] = dss.loads.kv
#         elem[name]['par']['profile'] = dict()
#         elem[name]['par']['profile']['name'] = None
#         elem[name]['par']['profile']['curve'] = 1
#
#     elif mcat == 'Line':     # ok
#         unr_line.append(name)
#
#         if cat == 'line':
#             elem[name]['category'] = 'AC-Load'
#             elem[name]['par']['R0'] = dss.lines.r0
#             elem[name]['par']['X0'] = dss.lines.x0
#             elem[name]['par']['c0'] = dss.lines.c0
#             elem[name]['par']['c1'] = dss.lines.c1
#
#         elif cat == 'dc-line':
#             elem[name]['category'] = 'DC-Load'
#
#         elem[name]['par']['length'] = dss.lines.length
#         elem[name]['par']['R1'] = dss.lines.r1
#         elem[name]['par']['X1'] = dss.lines.x1
#         elem[name]['par']['In'] = dss.lines.norm_amps
#
#         # for i in [0, 1]:
#         #     bus = elem[name]['top']['conn'][i]
#         #     if bus not in elem.keys():
#         #         elem[bus] = dict()
#         #         elem[bus]['category'] = bus
#         #         elem[bus]['par'] = dict()
#         #         # elem[elem[name]['top']['conn'][1]]['par']['Vn'] = elem[name]['par']['Vn1']
#         #         elem[bus]['top'] = dict()
#         #         elem[bus]['par']['conn'] = [name]
#         #     else:
#         #         elem[bus]['par']['conn'].append(name)
#
# while unr_conv + unr_line != []:
#     print(unr_conv, unr_line)
#
#     for name in unr_conv:
#         if elem[name]['top']['conn'][0] in elem.keys():
#             bus = elem[name]['top']['conn'][0]
#             if elem[bus]['par']['Vn']:
#                 elem[name]['par']['Vn0'] = elem[bus]['par']['Vn']
#                 unr_conv.remove(name)
#
#     for name in unr_line:
#         v = None
#         bus2 = None
#         if elem[name]['top']['conn'][0] in elem.keys():
#             bus = elem[name]['top']['conn'][0]
#             if elem[bus]['par']['Vn']:
#                 v = elem[bus]['par']['Vn']
#                 bus2 = elem[name]['top']['conn'][1]
#
#         elif elem[name]['top']['conn'][1] in elem.keys():
#             bus = elem[name]['top']['conn'][1]
#             if elem[bus]['par']['Vn']:
#                 v = elem[bus]['par']['Vn']
#                 bus2 = elem[name]['top']['conn'][0]
#
#         if v:
#             elem[name]['par']['Vn'] = v
#             elem[bus2]['par']['Vn'] = v
#             unr_line.remove(name)
#
# print('done')
#
# with open('CityArea.yml', 'w') as file:
#     yaml.dump(elem, file)
#     file.close()
#
# dss.circuit.set_active_element('Load.ug_dc-load')
# print(dss.cktelement.name)
# dss.cktelement.enabled(False)
# print(dss.cktelement.has_switch_control)
#
#
# dss.circuit.set_active_element('Transformer.ugs_pwm')
# print(dss.cktelement.name)
# dss.cktelement.enabled(True)
# print(dss.cktelement.has_switch_control)
#
# print(dss.cktelement.is_enabled)
#
# dss.circuit.set_active_element('Line.ug_line')
#
# print(dss.cktelement.name, dss.cktelement.has_switch_control, dss.lines.geometry)
#
# dss.solution.solve()
#
# dss.circuit.set_active_element('Vsource.source')
# print(dss.cktelement.powers)
#
# # -------------------------------------------------------------------------------------------------------------------
#
#
