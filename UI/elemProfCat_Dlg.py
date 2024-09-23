from UI.ui_elemProfCat_Dlg import Ui_Dialog

from PySide2 import QtGui, QtCore, QtWidgets


class ElemProfCatDlg(QtWidgets.QDialog):
    def __init__(self):
        super(ElemProfCatDlg, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ok = False

        self.ui.confirmBtn.clicked.connect(self.confirm)
        self.ui.cancelBtn.clicked.connect(self.close)

    def confirm(self):
        self.ok = True
        self.close()

