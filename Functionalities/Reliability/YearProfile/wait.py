from .waitUI import Ui_MainWindow
from PyQt5 import QtWidgets


class Wait(QtWidgets.QMainWindow):
    def __init__(self):
        super(Wait, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
