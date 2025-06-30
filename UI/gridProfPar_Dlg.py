from UI.ui_gridProfPar_Dlg import Ui_Dialog

from PySide2 import QtGui, QtCore, QtWidgets
# from PyQt5 import QtWidgets, QtGui, QtCore

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from variables import *
from dictInitialize import *

from variables import *
import datetime
import copy
from functools import partial

from datetime import datetime as dt


class GridProfParDlg(QtWidgets.QDialog):
    def __init__(self):
        super(GridProfParDlg, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.steps = [1, 5, 10, 15, 30, 60, 180, 360, 1440]

        self.len = 2
        self.confirmed = False
        self.default = False

        self.date_init()

        self.ui.startDte.dateChanged.connect(self.datefix)
        self.ui.startDte.timeChanged.connect(self.datefix)
        self.ui.endDte.dateChanged.connect(self.lenfix)
        self.ui.endDte.timeChanged.connect(self.lenfix)
        self.ui.stepCB.currentTextChanged.connect(self.datefix)
        self.ui.confirmBtn.clicked.connect(self.store)
        self.ui.cancelBtn.clicked.connect(self.closeBtn)
        self.ui.defaultRB.clicked.connect(self.default_click)

        self.def_years = []
        f = open(mainpath + '/_benchmark/_data/_profiles/Gen_year.txt')
        for line in f:
            try:
                self.def_years.append(int(line.split()[0]))
            except ValueError:
                pass


        today = [datetime.date.today().year, datetime.date.today().month, datetime.date.today().day]

        self.ui.startDte.setDateTime(QtCore.QDateTime(today[0], today[1], today[2], 0, 0, 0))
        self.ui.endDte.setDateTime(QtCore.QDateTime(today[0], today[1], today[2], 23, 0, 0))

        self.datefix()

        # self.ui.datetimeWgt.setVisible(False)
        # self.ui.calendarCWgt.setVisible(False)
        #
        # self.ui.punctLfRB.toggled.connect(self.punct_selected)
        # self.ui.datetimeWgt.mouseDoubleClickEvent = self.date_selected
        # self.ui.calendarCWgt.selectionChanged.connect(self.date_modified)
        # # self.ui.calendarCWgt.mouseDoubleClickEvent = self.date_modified
        #
        # self.ui.dateLE.setText(str(dt.now().day) + '/' + str(dt.now().month) + '/' + str(dt.now().year))

    def date_init(self):
        if grid['profile']['exist']:
            self.ui.startDte.setDateTime(QtCore.QDateTime(grid['profile']['start'][0],
                                                          grid['profile']['start'][1],
                                                          grid['profile']['start'][2],
                                                          grid['profile']['start'][3],
                                                          grid['profile']['start'][4],
                                                          0))
            self.ui.endDte.setDateTime(QtCore.QDateTime(grid['profile']['end'][0],
                                                        grid['profile']['end'][1],
                                                        grid['profile']['end'][2],
                                                        grid['profile']['end'][3],
                                                        grid['profile']['end'][4],
                                                        0))
            self.ui.stepCB.setCurrentIndex(self.steps.index(grid['profile']['step']))
            self.lenfix()
        else:
            self.ui.startDte.setDateTime(QtCore.QDateTime(2024, 1, 1, 0, 0, 0))

    def datefix(self):
        i = self.ui.stepCB.currentIndex()
        self.ui.endDte.setDateTime(self.ui.startDte.dateTime().addSecs(self.steps[i] * 60 * (self.len - 1)))

        t = (self.ui.startDte.dateTime().toPython()
             + datetime.timedelta(minutes=self.steps[self.ui.stepCB.currentIndex()]))

        self.ui.endDte.setMinimumDateTime(QtCore.QDateTime(t))

        self.lenfix()

    def lenfix(self):
        d0 = self.ui.startDte.dateTime().toPython()
        d1 = self.ui.endDte.dateTime().toPython()

        # print(d0, d1)
        dtime = d1 - d0
        # print(dtime.total_seconds() / 3600)

        gap = (d1 - d0).total_seconds() / 60

        self.len = int(gap/self.steps[self.ui.stepCB.currentIndex()]) + 1

        self.ui.pointsLbl.setText(str(self.len) + ' punti')
        self.default_check()

    def default_check(self):
        # È possibile importare i dati di default solo se l'intervallo temporale rientra nel range di dati disponibili
        range_ok = (self.ui.startDte.dateTime().date().year() in self.def_years and
                    self.ui.endDte.dateTime().date().year() in self.def_years)
        self.ui.defaultRB.setVisible(range_ok)

        # Lo stato di default è vero se la casella è spuntata e se è visibile (se il timerange è appropriato)
        self.default = self.ui.defaultRB.isChecked() and range_ok

        # Nel caso di verifica, la casella deve essere attivata se lo era precedentemente e se il timestep è 1 ora
        self.ui.defaultRB.setChecked(self.ui.stepCB.currentIndex() > 2 and self.default)

    # Azioni da compiere quando cambia lo stato della casella Default
    def default_click(self):
        if self.ui.defaultRB.isChecked():
            # Se bisogna usare i dati di default, il timestep deve essere di 1 ora
            self.ui.stepCB.setCurrentIndex(5)

    def store(self):
        self.default_check()
        grid['profile']['start'] = [self.ui.startDte.dateTime().date().year(),
                                    self.ui.startDte.dateTime().date().month(),
                                    self.ui.startDte.dateTime().date().day(),
                                    self.ui.startDte.dateTime().time().hour(),
                                    self.ui.startDte.dateTime().time().minute()]
        grid['profile']['end'] = [self.ui.endDte.dateTime().date().year(),
                                  self.ui.endDte.dateTime().date().month(),
                                  self.ui.endDte.dateTime().date().day(),
                                  self.ui.endDte.dateTime().time().hour(),
                                  self.ui.endDte.dateTime().time().minute()]
        grid['profile']['step'] = self.steps[self.ui.stepCB.currentIndex()]
        grid['profile']['points'] = self.len
        grid['profile']['exist'] = True
        self.confirmed = True
        self.close()

    def closeBtn(self):
        self.default = False
        grid['profile'] = {'step': None, 'start': None, 'end': None, 'points': None, 'exist': False}
        self.close()
