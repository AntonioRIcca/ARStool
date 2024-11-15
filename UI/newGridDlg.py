from UI.ui_newGridDlg import Ui_newGridDlg

from PySide2 import QtGui, QtCore, QtWidgets

from pathvalidate import sanitize_filename


class NewGrid(QtWidgets.QDialog):
    def __init__(self):
        super(NewGrid, self).__init__()
        self.ui = Ui_newGridDlg()
        self.ui.setupUi(self)

        self.newGridStart = False

        self.check()

        self.ui.createPb.clicked.connect(self.grid_create)
        self.ui.cancelPb.clicked.connect(self.close)

        self.ui.nameLe.textChanged.connect(self.check)
        self.ui.sourceVDsb.valueChanged.connect(self.check)

    def check(self):
        self.ui.createPb.setVisible(self.ui.nameLe.text() == sanitize_filename(self.ui.nameLe.text()) and
                                    self.ui.nameLbl != "" and self.ui.sourceVDsb.value() > 0)

    def grid_create(self):
        self.newGridStart = True
        self.close()
        pass
    #
    # def cancel(self):
    #     self.close()
    #
