# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'yearprofileUIIxOGNI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(601, 501)
        Form.setStyleSheet(u"background-color: rgb(0, 0, 7);\n"
"color: rgb(255, 255, 255);")
        self.profile_cap_LBL = QLabel(Form)
        self.profile_cap_LBL.setObjectName(u"profile_cap_LBL")
        self.profile_cap_LBL.setGeometry(QRect(10, 5, 41, 21))
        font = QFont()
        font.setPointSize(9)
        self.profile_cap_LBL.setFont(font)
        self.profile_TW = QTableWidget(Form)
        if (self.profile_TW.columnCount() < 2):
            self.profile_TW.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.profile_TW.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.profile_TW.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.profile_TW.rowCount() < 12):
            self.profile_TW.setRowCount(12)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(8, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(9, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(10, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.profile_TW.setVerticalHeaderItem(11, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.profile_TW.setItem(0, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.profile_TW.setItem(0, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.profile_TW.setItem(1, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.profile_TW.setItem(2, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.profile_TW.setItem(3, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.profile_TW.setItem(4, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.profile_TW.setItem(5, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.profile_TW.setItem(6, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.profile_TW.setItem(7, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.profile_TW.setItem(8, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.profile_TW.setItem(9, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.profile_TW.setItem(10, 0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.profile_TW.setItem(11, 0, __qtablewidgetitem26)
        self.profile_TW.setObjectName(u"profile_TW")
        self.profile_TW.setGeometry(QRect(10, 40, 171, 381))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(8)
        self.profile_TW.setFont(font1)
        self.profile_TW.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.profile_TW.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.profile_TW.horizontalHeader().setVisible(True)
        self.profile_TW.horizontalHeader().setDefaultSectionSize(75)
        self.profile_TW.verticalHeader().setVisible(False)
        self.profile_TW.verticalHeader().setDefaultSectionSize(27)
        self.profile_TW.verticalHeader().setHighlightSections(False)
        self.import_BTN = QPushButton(Form)
        self.import_BTN.setObjectName(u"import_BTN")
        self.import_BTN.setGeometry(QRect(290, 470, 91, 23))
        font2 = QFont()
        font2.setPointSize(7)
        self.import_BTN.setFont(font2)
        self.import_BTN.setStyleSheet(u"background-color: rgb(85, 85, 127);")
        self.load_BTN = QPushButton(Form)
        self.load_BTN.setObjectName(u"load_BTN")
        self.load_BTN.setGeometry(QRect(290, 440, 91, 23))
        self.load_BTN.setFont(font2)
        self.load_BTN.setStyleSheet(u"background-color: rgb(85, 85, 127);")
        self.new_BTN = QPushButton(Form)
        self.new_BTN.setObjectName(u"new_BTN")
        self.new_BTN.setGeometry(QRect(190, 440, 91, 23))
        self.new_BTN.setFont(font2)
        self.new_BTN.setStyleSheet(u"background-color: rgb(85, 85, 127);")
        self.elem_name_LN = QFrame(Form)
        self.elem_name_LN.setObjectName(u"elem_name_LN")
        self.elem_name_LN.setGeometry(QRect(0, 30, 580, 1))
        self.elem_name_LN.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.elem_name_LN.setLineWidth(1)
        self.elem_name_LN.setFrameShape(QFrame.HLine)
        self.elem_name_LN.setFrameShadow(QFrame.Sunken)
        self.confirm_BTN = QPushButton(Form)
        self.confirm_BTN.setObjectName(u"confirm_BTN")
        self.confirm_BTN.setGeometry(QRect(490, 440, 91, 23))
        self.confirm_BTN.setFont(font2)
        self.confirm_BTN.setStyleSheet(u"background-color: rgb(85, 85, 127);")
        self.save_BTN = QPushButton(Form)
        self.save_BTN.setObjectName(u"save_BTN")
        self.save_BTN.setGeometry(QRect(390, 440, 91, 23))
        self.save_BTN.setFont(font2)
        self.save_BTN.setStyleSheet(u"background-color: rgb(85, 85, 127);")
        self.exit_BTN = QPushButton(Form)
        self.exit_BTN.setObjectName(u"exit_BTN")
        self.exit_BTN.setGeometry(QRect(490, 470, 91, 23))
        self.exit_BTN.setFont(font2)
        self.exit_BTN.setStyleSheet(u"background-color: rgb(85, 85, 127);")
        self.profile_LBL = QLabel(Form)
        self.profile_LBL.setObjectName(u"profile_LBL")
        self.profile_LBL.setGeometry(QRect(60, 5, 521, 21))
        self.profile_LBL.setFont(font)
        self.month_BTN = QPushButton(Form)
        self.month_BTN.setObjectName(u"month_BTN")
        self.month_BTN.setGeometry(QRect(430, 40, 75, 23))
        self.month_BTN.setStyleSheet(u"")
        self.reset_BTN = QPushButton(Form)
        self.reset_BTN.setObjectName(u"reset_BTN")
        self.reset_BTN.setGeometry(QRect(390, 470, 91, 23))
        self.reset_BTN.setFont(font2)
        self.reset_BTN.setStyleSheet(u"background-color: rgb(85, 85, 127);")
        self.bottom_LN = QFrame(Form)
        self.bottom_LN.setObjectName(u"bottom_LN")
        self.bottom_LN.setGeometry(QRect(-10, 500, 600, 1))
        self.bottom_LN.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.bottom_LN.setLineWidth(1)
        self.bottom_LN.setFrameShape(QFrame.HLine)
        self.bottom_LN.setFrameShadow(QFrame.Sunken)
        self.year_BTN = QPushButton(Form)
        self.year_BTN.setObjectName(u"year_BTN")
        self.year_BTN.setGeometry(QRect(350, 40, 75, 23))
        self.year_BTN.setStyleSheet(u"")
        self.day_BTN = QPushButton(Form)
        self.day_BTN.setObjectName(u"day_BTN")
        self.day_BTN.setGeometry(QRect(510, 40, 75, 23))
        self.day_BTN.setStyleSheet(u"")
        self.elem_name_LN_2 = QFrame(Form)
        self.elem_name_LN_2.setObjectName(u"elem_name_LN_2")
        self.elem_name_LN_2.setGeometry(QRect(0, 430, 580, 1))
        self.elem_name_LN_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.elem_name_LN_2.setLineWidth(1)
        self.elem_name_LN_2.setFrameShape(QFrame.HLine)
        self.elem_name_LN_2.setFrameShadow(QFrame.Sunken)
        self.top_LN = QFrame(Form)
        self.top_LN.setObjectName(u"top_LN")
        self.top_LN.setGeometry(QRect(-10, 0, 600, 1))
        self.top_LN.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.top_LN.setLineWidth(1)
        self.top_LN.setFrameShape(QFrame.HLine)
        self.top_LN.setFrameShadow(QFrame.Sunken)
        self.plt_WGT = QWidget(Form)
        self.plt_WGT.setObjectName(u"plt_WGT")
        self.plt_WGT.setGeometry(QRect(180, 70, 411, 361))
        self.step_BTN = QPushButton(Form)
        self.step_BTN.setObjectName(u"step_BTN")
        self.step_BTN.setGeometry(QRect(10, 440, 171, 51))
        self.step_BTN.setFont(font2)
        self.step_BTN.setStyleSheet(u"background-color: rgb(85, 85, 127);")
        self.clear_BTN = QPushButton(Form)
        self.clear_BTN.setObjectName(u"clear_BTN")
        self.clear_BTN.setGeometry(QRect(190, 470, 91, 23))
        self.clear_BTN.setFont(font2)
        self.clear_BTN.setStyleSheet(u"background-color: rgb(85, 85, 127);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.profile_cap_LBL.setText(QCoreApplication.translate("Form", u"Profile:", None))
        ___qtablewidgetitem = self.profile_TW.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Time", None));
        ___qtablewidgetitem1 = self.profile_TW.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"T [\u00b0C]", None));
        ___qtablewidgetitem2 = self.profile_TW.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem3 = self.profile_TW.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem4 = self.profile_TW.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem5 = self.profile_TW.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem6 = self.profile_TW.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem7 = self.profile_TW.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem8 = self.profile_TW.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem9 = self.profile_TW.verticalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem10 = self.profile_TW.verticalHeaderItem(8)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem11 = self.profile_TW.verticalHeaderItem(9)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem12 = self.profile_TW.verticalHeaderItem(10)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem13 = self.profile_TW.verticalHeaderItem(11)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"New Row", None));

        __sortingEnabled = self.profile_TW.isSortingEnabled()
        self.profile_TW.setSortingEnabled(False)
        ___qtablewidgetitem14 = self.profile_TW.item(0, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"Gennaio", None));
        ___qtablewidgetitem15 = self.profile_TW.item(0, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"20", None));
        ___qtablewidgetitem16 = self.profile_TW.item(1, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form", u"Febbraio", None));
        ___qtablewidgetitem17 = self.profile_TW.item(2, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form", u"Marzo", None));
        ___qtablewidgetitem18 = self.profile_TW.item(3, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form", u"Aprile", None));
        ___qtablewidgetitem19 = self.profile_TW.item(4, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form", u"Maggio", None));
        ___qtablewidgetitem20 = self.profile_TW.item(5, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Form", u"Giugno", None));
        ___qtablewidgetitem21 = self.profile_TW.item(6, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Form", u"Luglio", None));
        ___qtablewidgetitem22 = self.profile_TW.item(7, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Form", u"Agosto", None));
        ___qtablewidgetitem23 = self.profile_TW.item(8, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Form", u"Settembre", None));
        ___qtablewidgetitem24 = self.profile_TW.item(9, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Form", u"Ottobre", None));
        ___qtablewidgetitem25 = self.profile_TW.item(10, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Form", u"Novembre", None));
        ___qtablewidgetitem26 = self.profile_TW.item(11, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Form", u"Dicembre", None));
        self.profile_TW.setSortingEnabled(__sortingEnabled)

        self.import_BTN.setText(QCoreApplication.translate("Form", u"Importa Dati", None))
        self.load_BTN.setText(QCoreApplication.translate("Form", u"Carica", None))
        self.new_BTN.setText(QCoreApplication.translate("Form", u"Nuovo", None))
        self.confirm_BTN.setText(QCoreApplication.translate("Form", u"Conferma e ESCI", None))
        self.save_BTN.setText(QCoreApplication.translate("Form", u"Salva", None))
        self.exit_BTN.setText(QCoreApplication.translate("Form", u"ESCI", None))
        self.profile_LBL.setText(QCoreApplication.translate("Form", u"Profile Name", None))
        self.month_BTN.setText(QCoreApplication.translate("Form", u"Settembre", None))
        self.reset_BTN.setText(QCoreApplication.translate("Form", u"Reset valori", None))
        self.year_BTN.setText(QCoreApplication.translate("Form", u"Anno  <<", None))
        self.day_BTN.setText(QCoreApplication.translate("Form", u"Giorno: 30", None))
        self.step_BTN.setText(QCoreApplication.translate("Form", u"Uniform for all days", None))
        self.clear_BTN.setText(QCoreApplication.translate("Form", u"Creazione guidata", None))
    # retranslateUi

