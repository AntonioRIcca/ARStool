from UI.ui_relParWgt import Ui_Form
from UI.ui_newGridDlg import Ui_newGridDlg


from PySide2 import QtGui, QtCore, QtWidgets
# from PyQt5 import QtWidgets, QtGui, QtCore

from variables import grid


class RelParWgt(QtWidgets.QWidget):
    def __init__(self):
        super(RelParWgt, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.profile_exixts = False

        self.ui.tempProfPb.clicked.connect(self.temperature_profile)

    def temperature_profile(self):
        print('profilo di temperatura')
        # from UI.newGridDlg import NewGrid
        #
        from Functionalities.Reliability.YearProfile.yearprofile import YearProfile
        popup = YearProfile(grid['rel']['prof_T']['name'], grid['rel']['prof_T']['profile'])
        # popup = NewGrid()

        if popup.exec():
            pass

        if popup.confirmed:
            if grid['rel']['prof_T']['name']:
                self.ui.tempProfPb.setText(grid['rel']['prof_T']['name'])

        # self.profile_exixts = popup.confirmed
        # self.profile_name = popup.name
        #
        # print(grid['rel']['prof_T'])
