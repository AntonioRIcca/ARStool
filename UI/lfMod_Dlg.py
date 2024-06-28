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


class LfModDlg(QtWidgets.QDialog):
    def __init__(self):
        super(LfModDlg, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.datetimeWgt.setVisible(False)
        self.ui.calendarCWgt.setVisible(False)

        self.ui.punctLfRB.toggled.connect(self.punct_selected)
        self.ui.datetimeWgt.mouseDoubleClickEvent = self.date_selected
        self.ui.calendarCWgt.selectionChanged.connect(self.date_modified)
        # self.ui.calendarCWgt.mouseDoubleClickEvent = self.date_modified

        self.ui.dateLE.setText(str(dt.now().day) + '/' + str(dt.now().month) + '/' + str(dt.now().year))

    def punct_selected(self):
        self.ui.datetimeWgt.setVisible(self.ui.punctLfRB.isChecked())

    def date_selected(self, event):
        # print('doppio click sulla data')
        self.ui.calendarCWgt.setVisible(True)

    def date_modified(self):
        # print('data selezionata')
        self.ui.calendarCWgt.setVisible(False)
        # print(self.ui.calendarCWgt.selectedDate())
        datesel = self.ui.calendarCWgt.selectedDate()
        # print(datesel.day(), datesel.month(), datesel.year())
        self.ui.dateLE.setText(str(datesel.day()) + '/' + str(datesel.month()) + '/' + str(datesel.year()))



