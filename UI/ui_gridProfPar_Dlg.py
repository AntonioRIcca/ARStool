# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gridProfPar_DlgJWoeun.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QDateTime, QDate, QTime)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(340, 280)
        Dialog.setStyleSheet(u"*{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(191, 191, 191);\n"
"}\n"
"\n"
"\n"
"\n"
"QLineEdit{\n"
"	border: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(255,255,255);\n"
"}\n"
"\n"
"QComboBox{\n"
"	border: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(255,255,255);\n"
"}\n"
"\n"
"QDoubleSpinBox{\n"
"	border: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	text-align: center;\n"
"	padding: 0px 00px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(31, 31, 31); \n"
"	border: solid;\n"
"	border-width: 2px; \n"
"	border-radius: 10px; \n"
"	border-color: rgb(127, 127, 127)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(64, 64, 64); \n"
"	border-style: inset\n"
"}")
        self.startLbl = QLabel(Dialog)
        self.startLbl.setObjectName(u"startLbl")
        self.startLbl.setGeometry(QRect(10, 50, 50, 25))
        font = QFont()
        font.setPointSize(10)
        self.startLbl.setFont(font)
        self.startLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.endLbl = QLabel(Dialog)
        self.endLbl.setObjectName(u"endLbl")
        self.endLbl.setGeometry(QRect(10, 90, 50, 25))
        self.endLbl.setFont(font)
        self.endLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.stepLbl = QLabel(Dialog)
        self.stepLbl.setObjectName(u"stepLbl")
        self.stepLbl.setGeometry(QRect(10, 130, 50, 25))
        self.stepLbl.setFont(font)
        self.stepLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.stepCB = QComboBox(Dialog)
        self.stepCB.addItem("")
        self.stepCB.addItem("")
        self.stepCB.addItem("")
        self.stepCB.addItem("")
        self.stepCB.addItem("")
        self.stepCB.addItem("")
        self.stepCB.addItem("")
        self.stepCB.addItem("")
        self.stepCB.addItem("")
        self.stepCB.setObjectName(u"stepCB")
        self.stepCB.setGeometry(QRect(70, 130, 90, 25))
        self.titleLbl = QLabel(Dialog)
        self.titleLbl.setObjectName(u"titleLbl")
        self.titleLbl.setGeometry(QRect(10, 10, 321, 25))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.titleLbl.setFont(font1)
        self.titleLbl.setAlignment(Qt.AlignCenter)
        self.startDte = QDateTimeEdit(Dialog)
        self.startDte.setObjectName(u"startDte")
        self.startDte.setGeometry(QRect(70, 50, 194, 25))
        self.startDte.setFont(font)
        self.startDte.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))
        self.startDte.setCalendarPopup(True)
        self.endDte = QDateTimeEdit(Dialog)
        self.endDte.setObjectName(u"endDte")
        self.endDte.setGeometry(QRect(70, 90, 194, 25))
        self.endDte.setFont(font)
        self.endDte.setProperty("showGroupSeparator", False)
        self.endDte.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))
        self.endDte.setCalendarPopup(True)
        self.pointsLbl = QLabel(Dialog)
        self.pointsLbl.setObjectName(u"pointsLbl")
        self.pointsLbl.setGeometry(QRect(170, 130, 161, 25))
        self.pointsLbl.setFont(font)
        self.pointsLbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.confirmBtn = QPushButton(Dialog)
        self.confirmBtn.setObjectName(u"confirmBtn")
        self.confirmBtn.setGeometry(QRect(20, 240, 75, 23))
        self.cancelBtn = QPushButton(Dialog)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setGeometry(QRect(250, 240, 75, 23))
        self.defaultRB = QCheckBox(Dialog)
        self.defaultRB.setObjectName(u"defaultRB")
        self.defaultRB.setGeometry(QRect(70, 170, 91, 20))
        self.defaultRB.setFont(font)
        self.defaultRB.setLayoutDirection(Qt.RightToLeft)
        self.defaultRB.setChecked(True)
        QWidget.setTabOrder(self.startDte, self.endDte)
        QWidget.setTabOrder(self.endDte, self.stepCB)
        QWidget.setTabOrder(self.stepCB, self.confirmBtn)
        QWidget.setTabOrder(self.confirmBtn, self.cancelBtn)

        self.retranslateUi(Dialog)

        self.stepCB.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Parametri Profilo", None))
        self.startLbl.setText(QCoreApplication.translate("Dialog", u"Inizio", None))
        self.endLbl.setText(QCoreApplication.translate("Dialog", u"Fine", None))
        self.stepLbl.setText(QCoreApplication.translate("Dialog", u"Passo", None))
        self.stepCB.setItemText(0, QCoreApplication.translate("Dialog", u"1 min", None))
        self.stepCB.setItemText(1, QCoreApplication.translate("Dialog", u"5 min", None))
        self.stepCB.setItemText(2, QCoreApplication.translate("Dialog", u"10 min", None))
        self.stepCB.setItemText(3, QCoreApplication.translate("Dialog", u"15 min", None))
        self.stepCB.setItemText(4, QCoreApplication.translate("Dialog", u"30 min", None))
        self.stepCB.setItemText(5, QCoreApplication.translate("Dialog", u"1 h", None))
        self.stepCB.setItemText(6, QCoreApplication.translate("Dialog", u"3 h", None))
        self.stepCB.setItemText(7, QCoreApplication.translate("Dialog", u"6 h", None))
        self.stepCB.setItemText(8, QCoreApplication.translate("Dialog", u"1 giorno", None))

        self.stepCB.setCurrentText(QCoreApplication.translate("Dialog", u"1 h", None))
        self.titleLbl.setText(QCoreApplication.translate("Dialog", u"Inserire i parametri dei profili temporali della rete", None))
        self.pointsLbl.setText(QCoreApplication.translate("Dialog", u"NN punti", None))
        self.confirmBtn.setText(QCoreApplication.translate("Dialog", u"Conferma", None))
        self.cancelBtn.setText(QCoreApplication.translate("Dialog", u"Cancella", None))
        self.defaultRB.setText(QCoreApplication.translate("Dialog", u"Default data", None))
    # retranslateUi

