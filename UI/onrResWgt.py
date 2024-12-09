from UI.ui_onrResWgt import Ui_Form

from PySide2 import QtGui, QtCore, QtWidgets
# from PyQt5 import QtWidgets, QtGui, QtCore


class OnrResWgt(QtWidgets.QWidget):
    def __init__(self):
        super(OnrResWgt, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # self.ui.onrTabWgt.setStyleSheet('QTabBar::tab{'
        #                                         'font: 75 10pt "MS Shell Dlg 2";'
        #                                         'background-color: rgb(0, 0, 0);'
        #                                         'border: 1px solid rgb(255, 255, 255);'
        #                                         'height: 120px;'
        #                                         'width: 30 px;'
        #                                         '} '
        #                                         'QTabBar::tab::selected{'
        #                                         'background-color: rgb(63, 63, 63);'
        #                                         '}'
        #                                         'QTabWidget::pane{'
        #                                         'background-color: rgb(255, 0, 0);'
        #                                         '}')
        #
        # self.ui.onr1Wgt.setStyleSheet('background-color: rgb(255, 0, 0);')
