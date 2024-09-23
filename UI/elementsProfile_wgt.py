from UI.ui_elementsProfile_wgt import Ui_elemProfWgt

from PySide2 import QtGui, QtCore, QtWidgets
# from PyQt5 import QtWidgets, QtGui, QtCore


class ElemProfListWgt(QtWidgets.QWidget):
    def __init__(self):
        super(ElemProfListWgt, self).__init__()
        self.ui = Ui_elemProfWgt()
        self.ui.setupUi(self)
