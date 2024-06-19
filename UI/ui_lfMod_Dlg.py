# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lfMod_DlgirPVaS.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(340, 330)
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
        self.punctLfRB = QRadioButton(Dialog)
        self.punctLfRB.setObjectName(u"punctLfRB")
        self.punctLfRB.setGeometry(QRect(10, 50, 320, 17))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.punctLfRB.setFont(font)
        self.profLfRB = QRadioButton(Dialog)
        self.profLfRB.setObjectName(u"profLfRB")
        self.profLfRB.setGeometry(QRect(10, 20, 320, 17))
        self.profLfRB.setFont(font)
        self.calendarCWgt = QCalendarWidget(Dialog)
        self.calendarCWgt.setObjectName(u"calendarCWgt")
        self.calendarCWgt.setGeometry(QRect(10, 130, 320, 191))
        self.calendarCWgt.setStyleSheet(u"")
        self.calcPls = QPushButton(Dialog)
        self.calcPls.setObjectName(u"calcPls")
        self.calcPls.setGeometry(QRect(230, 80, 100, 25))
        self.datetimeWgt = QWidget(Dialog)
        self.datetimeWgt.setObjectName(u"datetimeWgt")
        self.datetimeWgt.setGeometry(QRect(10, 80, 181, 25))
        self.timeSepLbl = QLabel(self.datetimeWgt)
        self.timeSepLbl.setObjectName(u"timeSepLbl")
        self.timeSepLbl.setGeometry(QRect(140, 0, 10, 25))
        self.timeSepLbl.setFont(font)
        self.timeSepLbl.setAlignment(Qt.AlignCenter)
        self.dateLE = QLineEdit(self.datetimeWgt)
        self.dateLE.setObjectName(u"dateLE")
        self.dateLE.setEnabled(False)
        self.dateLE.setGeometry(QRect(0, 0, 90, 25))
        self.dateLE.setFont(font)
        self.dateLE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sepLbl = QLabel(self.datetimeWgt)
        self.sepLbl.setObjectName(u"sepLbl")
        self.sepLbl.setGeometry(QRect(90, 0, 20, 25))
        self.sepLbl.setFont(font)
        self.sepLbl.setAlignment(Qt.AlignCenter)
        self.minuteDsb = QDoubleSpinBox(self.datetimeWgt)
        self.minuteDsb.setObjectName(u"minuteDsb")
        self.minuteDsb.setGeometry(QRect(150, 0, 30, 25))
        self.minuteDsb.setFont(font)
        self.minuteDsb.setAlignment(Qt.AlignCenter)
        self.minuteDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.minuteDsb.setDecimals(0)
        self.minuteDsb.setSingleStep(15.000000000000000)
        self.minuteDsb.setValue(30.000000000000000)
        self.hourDsb = QDoubleSpinBox(self.datetimeWgt)
        self.hourDsb.setObjectName(u"hourDsb")
        self.hourDsb.setGeometry(QRect(110, 0, 30, 25))
        self.hourDsb.setFont(font)
        self.hourDsb.setAlignment(Qt.AlignCenter)
        self.hourDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.hourDsb.setDecimals(0)
        self.hourDsb.setMaximum(23.000000000000000)
        self.hourDsb.setValue(23.000000000000000)
        self.timeSepLbl.raise_()
        self.sepLbl.raise_()
        self.minuteDsb.raise_()
        self.hourDsb.raise_()
        self.dateLE.raise_()
        self.punctLfRB.raise_()
        self.profLfRB.raise_()
        self.calcPls.raise_()
        self.datetimeWgt.raise_()
        self.calendarCWgt.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.punctLfRB.setText(QCoreApplication.translate("Dialog", u"LoadFlow puntuale", None))
        self.profLfRB.setText(QCoreApplication.translate("Dialog", u"LoadFlow nell'intero intervallo di tempo", None))
        self.calcPls.setText(QCoreApplication.translate("Dialog", u"Calcola", None))
        self.timeSepLbl.setText(QCoreApplication.translate("Dialog", u":", None))
        self.dateLE.setText(QCoreApplication.translate("Dialog", u"21/12/2002", None))
        self.sepLbl.setText(QCoreApplication.translate("Dialog", u"-", None))
    # retranslateUi

