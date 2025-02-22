from UI.ui_onrParWgt import Ui_Form
from UI.ui_newGridDlg import Ui_newGridDlg


from PySide2 import QtGui, QtCore, QtWidgets
# from PyQt5 import QtWidgets, QtGui, QtCore

from variables import grid


class ONRParWgt(QtWidgets.QWidget):
    def __init__(self):
        super(ONRParWgt, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
