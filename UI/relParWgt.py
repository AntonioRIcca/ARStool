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

        self.ui.tempProfPb.clicked.connect(self.tempreature_profile)

    def tempreature_profile(self):
        print('profilo di temperatura')
        # from UI.newGridDlg import NewGrid
        #
        from Functionalities.Reliability.YearProfile.yearprofile import YearProfile
        popup = YearProfile('Nuovo profilo', None)
        # popup = NewGrid()

        if popup.exec():
            pass

        print(grid['rel']['prof_T'])
