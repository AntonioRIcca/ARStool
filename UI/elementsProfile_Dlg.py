# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'elementsProfile_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainDlg(object):
    def setupUi(self, mainDlg):
        mainDlg.setObjectName("mainDlg")
        mainDlg.resize(800, 600)
        mainDlg.setStyleSheet("*{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(31, 31, 31); \n"
"    border: solid; \n"
"    border-width: 2px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(223, 223, 223);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(63, 63, 63);\n"
"}\n"
"")
        self.nameLbl = QtWidgets.QLabel(mainDlg)
        self.nameLbl.setGeometry(QtCore.QRect(10, 10, 780, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nameLbl.setFont(font)
        self.nameLbl.setObjectName("nameLbl")
        self.upLn = QtWidgets.QFrame(mainDlg)
        self.upLn.setGeometry(QtCore.QRect(10, 40, 780, 3))
        self.upLn.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: solid;\n"
"")
        self.upLn.setFrameShape(QtWidgets.QFrame.HLine)
        self.upLn.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.upLn.setObjectName("upLn")
        self.profileTW = QtWidgets.QTableWidget(mainDlg)
        self.profileTW.setGeometry(QtCore.QRect(10, 50, 200, 490))
        self.profileTW.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.profileTW.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.profileTW.setAutoScroll(True)
        self.profileTW.setObjectName("profileTW")
        self.profileTW.setColumnCount(2)
        self.profileTW.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.profileTW.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.profileTW.setHorizontalHeaderItem(1, item)
        self.downLn = QtWidgets.QFrame(mainDlg)
        self.downLn.setGeometry(QtCore.QRect(10, 550, 780, 3))
        self.downLn.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: solid;\n"
"")
        self.downLn.setFrameShape(QtWidgets.QFrame.HLine)
        self.downLn.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.downLn.setObjectName("downLn")
        self.saveBtn = QtWidgets.QPushButton(mainDlg)
        self.saveBtn.setGeometry(QtCore.QRect(10, 560, 100, 30))
        self.saveBtn.setObjectName("saveBtn")
        self.cancelBtn = QtWidgets.QPushButton(mainDlg)
        self.cancelBtn.setGeometry(QtCore.QRect(690, 560, 100, 30))
        self.cancelBtn.setObjectName("cancelBtn")
        self.importBtn = QtWidgets.QPushButton(mainDlg)
        self.importBtn.setGeometry(QtCore.QRect(250, 560, 100, 30))
        self.importBtn.setObjectName("importBtn")
        self.exportBtn = QtWidgets.QPushButton(mainDlg)
        self.exportBtn.setGeometry(QtCore.QRect(130, 560, 100, 30))
        self.exportBtn.setObjectName("exportBtn")
        self.plotWgt = QtWidgets.QWidget(mainDlg)
        self.plotWgt.setGeometry(QtCore.QRect(220, 50, 570, 490))
        self.plotWgt.setObjectName("plotWgt")
        self.defaultBtn = QtWidgets.QPushButton(mainDlg)
        self.defaultBtn.setGeometry(QtCore.QRect(370, 560, 100, 30))
        self.defaultBtn.setObjectName("defaultBtn")

        self.retranslateUi(mainDlg)
        QtCore.QMetaObject.connectSlotsByName(mainDlg)
        mainDlg.setTabOrder(self.profileTW, self.cancelBtn)
        mainDlg.setTabOrder(self.cancelBtn, self.saveBtn)
        mainDlg.setTabOrder(self.saveBtn, self.exportBtn)
        mainDlg.setTabOrder(self.exportBtn, self.importBtn)

    def retranslateUi(self, mainDlg):
        _translate = QtCore.QCoreApplication.translate
        mainDlg.setWindowTitle(_translate("mainDlg", "Dialog"))
        self.nameLbl.setText(_translate("mainDlg", "Nome Profilo"))
        item = self.profileTW.horizontalHeaderItem(0)
        item.setText(_translate("mainDlg", "Ora"))
        item = self.profileTW.horizontalHeaderItem(1)
        item.setText(_translate("mainDlg", "Scala [p.u.]"))
        self.saveBtn.setText(_translate("mainDlg", "Salva"))
        self.cancelBtn.setText(_translate("mainDlg", "Annulla"))
        self.importBtn.setText(_translate("mainDlg", "Importa"))
        self.exportBtn.setText(_translate("mainDlg", "Esporta"))
        self.defaultBtn.setText(_translate("mainDlg", "Predefinito"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainDlg = QtWidgets.QDialog()
    ui = Ui_mainDlg()
    ui.setupUi(mainDlg)
    mainDlg.show()
    sys.exit(app.exec_())
