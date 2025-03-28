import sys
import os


from UI.ui_main_ui import *

# from PySide2 import *

from Custom_Widgets.Widgets import *

from functools import partial

from variables import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################

        # self.show()

        # EXPAND CENTER MENU WIDGET SIZE
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())

        # CLOSE CENTER MENU WIDGET
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())

        # EXPAND RIGHT MENU WIDGET SIZE
        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())

        # CLOSE RIGHT MENU WIDGET
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())

        # CLOSE NOTIFICATION WIDGET
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())
    #
    # def elementRename(self, event):     # TODO: forse da eliminare
    #     self.ui.elemNameLE.installEventFilter(self)
    #
    #     self.ui.elemNameLE.setText(self.ui.rightMenu_LBL.text())
    #     self.ui.rightMenu_LBL.setVisible(False)
    #     self.ui.elemNameLE.setVisible(True)
    #     # self.ui.elemNameTE = QLineEdit()
    #     # a = QLineEdit()
    #     # a.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
    #     # self.ui.horizontalLayout_10.insertWidget(0, self.ui.elemNameTE)
    #     # self.ui.elemNameLE.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
    #     self.ui.elemNameLE.selectAll()
    #     self.ui.elemNameLE.setFocus()
    #     # print(self.elem)
    #
    # def eventFilter(self, obj, event):
    #     # print('evento')
    #     if event.type() == QtCore.QEvent.KeyPress and obj is self.ui.elemNameLE:
    #         if event.key() == QtCore.Qt.Key_Return and self.ui.elemNameLE.hasFocus():
    #             if self.ui.elemNameLE.text() in list(v.keys()):
    #                 QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), 'Attenzione',
    #                                               'Nome elemento già presente')
    #                 # self.rename(None)
    #             else:
    #                 self.ui.rightMenu_LBL.setVisible(True)
    #                 self.ui.elemNameLE.setVisible(False)
    #                 self.ui.rightMenu_LBL.setText(self.ui.elemNameLE.text())
    #         if event.key() == QtCore.Qt.Key_Escape and self.ui.elemNameLE.hasFocus():
    #             self.ui.rightMenu_LBL.setVisible(True)
    #             self.ui.elemNameLE.setVisible(False)
    #     return super().eventFilter(obj, event)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # mw = QMainWindow()
    window = MainWindow()
    # window.ui.setupUi(mw)
    window.show()

    sys.exit(app.exec_())

#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
