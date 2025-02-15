# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yearprofileUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(611, 501)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 7);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.profile_cap_LBL = QtWidgets.QLabel(self.centralwidget)
        self.profile_cap_LBL.setGeometry(QtCore.QRect(20, 5, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.profile_cap_LBL.setFont(font)
        self.profile_cap_LBL.setObjectName("profile_cap_LBL")
        self.plt_WGT = QtWidgets.QWidget(self.centralwidget)
        self.plt_WGT.setGeometry(QtCore.QRect(190, 70, 411, 361))
        self.plt_WGT.setObjectName("plt_WGT")
        self.profile_TW = QtWidgets.QTableWidget(self.centralwidget)
        self.profile_TW.setGeometry(QtCore.QRect(20, 40, 171, 381))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.profile_TW.setFont(font)
        self.profile_TW.setStyleSheet("color: rgb(255, 255, 255);")
        self.profile_TW.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.profile_TW.setObjectName("profile_TW")
        self.profile_TW.setColumnCount(2)
        self.profile_TW.setRowCount(12)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.profile_TW.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.profile_TW.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.profile_TW.setItem(11, 0, item)
        self.profile_TW.horizontalHeader().setVisible(True)
        self.profile_TW.horizontalHeader().setDefaultSectionSize(75)
        self.profile_TW.verticalHeader().setVisible(False)
        self.profile_TW.verticalHeader().setDefaultSectionSize(27)
        self.profile_TW.verticalHeader().setHighlightSections(False)
        self.step_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.step_BTN.setGeometry(QtCore.QRect(20, 440, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.step_BTN.setFont(font)
        self.step_BTN.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.step_BTN.setObjectName("step_BTN")
        self.load_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.load_BTN.setGeometry(QtCore.QRect(300, 440, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.load_BTN.setFont(font)
        self.load_BTN.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.load_BTN.setObjectName("load_BTN")
        self.new_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.new_BTN.setGeometry(QtCore.QRect(200, 440, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.new_BTN.setFont(font)
        self.new_BTN.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.new_BTN.setObjectName("new_BTN")
        self.reset_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.reset_BTN.setGeometry(QtCore.QRect(400, 470, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.reset_BTN.setFont(font)
        self.reset_BTN.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.reset_BTN.setObjectName("reset_BTN")
        self.save_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.save_BTN.setGeometry(QtCore.QRect(400, 440, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.save_BTN.setFont(font)
        self.save_BTN.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.save_BTN.setObjectName("save_BTN")
        self.profile_LBL = QtWidgets.QLabel(self.centralwidget)
        self.profile_LBL.setGeometry(QtCore.QRect(70, 5, 521, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.profile_LBL.setFont(font)
        self.profile_LBL.setObjectName("profile_LBL")
        self.elem_name_LN = QtWidgets.QFrame(self.centralwidget)
        self.elem_name_LN.setGeometry(QtCore.QRect(10, 30, 580, 1))
        self.elem_name_LN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.elem_name_LN.setLineWidth(1)
        self.elem_name_LN.setFrameShape(QtWidgets.QFrame.HLine)
        self.elem_name_LN.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.elem_name_LN.setObjectName("elem_name_LN")
        self.top_LN = QtWidgets.QFrame(self.centralwidget)
        self.top_LN.setGeometry(QtCore.QRect(0, 0, 600, 1))
        self.top_LN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.top_LN.setLineWidth(1)
        self.top_LN.setFrameShape(QtWidgets.QFrame.HLine)
        self.top_LN.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.top_LN.setObjectName("top_LN")
        self.bottom_LN = QtWidgets.QFrame(self.centralwidget)
        self.bottom_LN.setGeometry(QtCore.QRect(0, 500, 600, 1))
        self.bottom_LN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bottom_LN.setLineWidth(1)
        self.bottom_LN.setFrameShape(QtWidgets.QFrame.HLine)
        self.bottom_LN.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bottom_LN.setObjectName("bottom_LN")
        self.year_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.year_BTN.setGeometry(QtCore.QRect(360, 40, 75, 23))
        self.year_BTN.setStyleSheet("")
        self.year_BTN.setObjectName("year_BTN")
        self.month_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.month_BTN.setGeometry(QtCore.QRect(440, 40, 75, 23))
        self.month_BTN.setStyleSheet("")
        self.month_BTN.setObjectName("month_BTN")
        self.day_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.day_BTN.setGeometry(QtCore.QRect(520, 40, 75, 23))
        self.day_BTN.setStyleSheet("")
        self.day_BTN.setObjectName("day_BTN")
        self.import_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.import_BTN.setGeometry(QtCore.QRect(300, 470, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.import_BTN.setFont(font)
        self.import_BTN.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.import_BTN.setObjectName("import_BTN")
        self.confirm_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.confirm_BTN.setGeometry(QtCore.QRect(500, 440, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.confirm_BTN.setFont(font)
        self.confirm_BTN.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.confirm_BTN.setObjectName("confirm_BTN")
        self.exit_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.exit_BTN.setGeometry(QtCore.QRect(500, 470, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.exit_BTN.setFont(font)
        self.exit_BTN.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.exit_BTN.setObjectName("exit_BTN")
        self.elem_name_LN_2 = QtWidgets.QFrame(self.centralwidget)
        self.elem_name_LN_2.setGeometry(QtCore.QRect(10, 430, 580, 1))
        self.elem_name_LN_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.elem_name_LN_2.setLineWidth(1)
        self.elem_name_LN_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.elem_name_LN_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.elem_name_LN_2.setObjectName("elem_name_LN_2")
        self.clear_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.clear_BTN.setGeometry(QtCore.QRect(200, 470, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.clear_BTN.setFont(font)
        self.clear_BTN.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.clear_BTN.setObjectName("clear_BTN")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.profile_cap_LBL.setText(_translate("MainWindow", "Profile:"))
        item = self.profile_TW.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.profile_TW.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.profile_TW.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.profile_TW.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.profile_TW.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.profile_TW.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.profile_TW.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.profile_TW.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.profile_TW.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.profile_TW.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.profile_TW.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.profile_TW.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.profile_TW.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time"))
        item = self.profile_TW.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "T [°C]"))
        __sortingEnabled = self.profile_TW.isSortingEnabled()
        self.profile_TW.setSortingEnabled(False)
        item = self.profile_TW.item(0, 0)
        item.setText(_translate("MainWindow", "Gennaio"))
        item = self.profile_TW.item(0, 1)
        item.setText(_translate("MainWindow", "20"))
        item = self.profile_TW.item(1, 0)
        item.setText(_translate("MainWindow", "Febbraio"))
        item = self.profile_TW.item(2, 0)
        item.setText(_translate("MainWindow", "Marzo"))
        item = self.profile_TW.item(3, 0)
        item.setText(_translate("MainWindow", "Aprile"))
        item = self.profile_TW.item(4, 0)
        item.setText(_translate("MainWindow", "Maggio"))
        item = self.profile_TW.item(5, 0)
        item.setText(_translate("MainWindow", "Giugno"))
        item = self.profile_TW.item(6, 0)
        item.setText(_translate("MainWindow", "Luglio"))
        item = self.profile_TW.item(7, 0)
        item.setText(_translate("MainWindow", "Agosto"))
        item = self.profile_TW.item(8, 0)
        item.setText(_translate("MainWindow", "Settembre"))
        item = self.profile_TW.item(9, 0)
        item.setText(_translate("MainWindow", "Ottobre"))
        item = self.profile_TW.item(10, 0)
        item.setText(_translate("MainWindow", "Novembre"))
        item = self.profile_TW.item(11, 0)
        item.setText(_translate("MainWindow", "Dicembre"))
        self.profile_TW.setSortingEnabled(__sortingEnabled)
        self.step_BTN.setText(_translate("MainWindow", "Uniform for all days"))
        self.load_BTN.setText(_translate("MainWindow", "Carica"))
        self.new_BTN.setText(_translate("MainWindow", "Nuovo"))
        self.reset_BTN.setText(_translate("MainWindow", "Reset valori"))
        self.save_BTN.setText(_translate("MainWindow", "Salva"))
        self.profile_LBL.setText(_translate("MainWindow", "Profile Name"))
        self.year_BTN.setText(_translate("MainWindow", "Anno  <<"))
        self.month_BTN.setText(_translate("MainWindow", "Settembre"))
        self.day_BTN.setText(_translate("MainWindow", "Giorno: 30"))
        self.import_BTN.setText(_translate("MainWindow", "Importa Dati"))
        self.confirm_BTN.setText(_translate("MainWindow", "Conferma e ESCI"))
        self.exit_BTN.setText(_translate("MainWindow", "ESCI"))
        self.clear_BTN.setText(_translate("MainWindow", "Creazione guidata"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
