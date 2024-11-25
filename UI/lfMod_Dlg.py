from UI.ui_lfMod_Dlg import Ui_Dialog

from PySide2 import QtGui, QtCore, QtWidgets
# from PyQt5 import QtWidgets, QtGui, QtCore

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from variables import *
from dictInitialize import *
import copy
from functools import partial

from datetime import datetime as dt

# print(datestart, dateend)


class LfModDlg(QtWidgets.QDialog):
    def __init__(self):
        super(LfModDlg, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.confirm = False
        self.profile = False

        self.datestart = dt(grid['profile']['start'][0], grid['profile']['start'][1], grid['profile']['start'][2],
                       grid['profile']['start'][3], grid['profile']['start'][4])
        self.dateend = dt(grid['profile']['end'][0], grid['profile']['end'][1], grid['profile']['end'][2],
                     grid['profile']['end'][3], grid['profile']['end'][4])

        self.ui.endWgt.setVisible(False)

        self.limits_reset()

        self.ui.punctLfRB.setChecked(True)

        self.ui.punctLfRB.toggled.connect(self.punct_selected)
        self.ui.startDte.dateTimeChanged.connect(self.date_modified)
        self.ui.endDte.dateTimeChanged.connect(self.date_modified)

        self.ui.calcPls.clicked.connect(self.calculate)

    def punct_selected(self):
        self.ui.endWgt.setVisible(self.ui.profLfRB.isChecked())
        pass

    def date_selected(self, event):
        # print('doppio click sulla data')
        # self.ui.calendarCWgt.setVisible(True)
        pass

    def date_modified(self):
        self.ui.startDte.setMaximumDateTime(QtCore.QDateTime(self.ui.endDte.dateTime().toPython()))

    def limits_reset(self):
        self.ui.startDte.setMinimumDateTime(QtCore.QDateTime(self.datestart))
        self.ui.startDte.setMaximumDateTime(QtCore.QDateTime(self.dateend))
        self.ui.endDte.setMinimumDateTime(QtCore.QDateTime(self.datestart))
        self.ui.endDte.setMaximumDateTime(QtCore.QDateTime(self.dateend))

        self.ui.startDte.setDateTime(QtCore.QDateTime(self.datestart))
        self.ui.endDte.setDateTime(QtCore.QDateTime(self.dateend))
        pass

    def calculate(self):
        self.i_start = int(QtCore.QDateTime(self.datestart).msecsTo(self.ui.startDte.dateTime()) / (60000) /
                           grid['profile']['step'])

        d0 = self.ui.startDte.dateTime().toPython()
        d1 = self.ui.endDte.dateTime().toPython()
        gap = (d1 - d0).total_seconds() / 60
        self.i_steps = int(gap / grid['profile']['step']) + 1

        self.confirm = True
        self.profile = self.ui.profLfRB.isChecked()

        grid['lf']['start'] = [self.ui.startDte.dateTime().date().year(),
                               self.ui.startDte.dateTime().date().month(),
                               self.ui.startDte.dateTime().date().day(),
                               self.ui.startDte.dateTime().time().hour(),
                               self.ui.startDte.dateTime().time().minute()]
        if self.profile:
            grid['lf']['end'] = [self.ui.endDte.dateTime().date().year(),
                                 self.ui.endDte.dateTime().date().month(),
                                 self.ui.endDte.dateTime().date().day(),
                                 self.ui.endDte.dateTime().time().hour(),
                                 self.ui.endDte.dateTime().time().minute()]
            grid['lf']['points'] = self.i_steps
        else:
            grid['lf']['end'] = copy.deepcopy(grid['lf']['start'])
            grid['lf']['points'] = 1

        self.close()
