# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lfMod_DlgghKEhQ.ui'
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
        Dialog.resize(340, 160)
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
        self.calcPls = QPushButton(Dialog)
        self.calcPls.setObjectName(u"calcPls")
        self.calcPls.setGeometry(QRect(230, 80, 100, 25))
        self.startWgt = QWidget(Dialog)
        self.startWgt.setObjectName(u"startWgt")
        self.startWgt.setGeometry(QRect(10, 80, 200, 25))
        self.startDte = QDateTimeEdit(self.startWgt)
        self.startDte.setObjectName(u"startDte")
        self.startDte.setGeometry(QRect(70, 0, 130, 25))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.startDte.setFont(font1)
        self.startDte.setCalendarPopup(True)
        self.startLbl = QLabel(self.startWgt)
        self.startLbl.setObjectName(u"startLbl")
        self.startLbl.setGeometry(QRect(0, 0, 60, 25))
        self.startLbl.setFont(font)
        self.endWgt = QWidget(Dialog)
        self.endWgt.setObjectName(u"endWgt")
        self.endWgt.setGeometry(QRect(10, 120, 200, 25))
        self.endDte = QDateTimeEdit(self.endWgt)
        self.endDte.setObjectName(u"endDte")
        self.endDte.setGeometry(QRect(70, 0, 130, 25))
        self.endDte.setFont(font1)
        self.endDte.setCalendarPopup(True)
        self.endLbl = QLabel(self.endWgt)
        self.endLbl.setObjectName(u"endLbl")
        self.endLbl.setGeometry(QRect(0, 0, 60, 25))
        self.endLbl.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.punctLfRB.setText(QCoreApplication.translate("Dialog", u"LoadFlow puntuale", None))
        self.profLfRB.setText(QCoreApplication.translate("Dialog", u"LoadFlow nell'intero intervallo di tempo", None))
        self.calcPls.setText(QCoreApplication.translate("Dialog", u"Calcola", None))
        self.startLbl.setText(QCoreApplication.translate("Dialog", u"Inizio", None))
        self.endLbl.setText(QCoreApplication.translate("Dialog", u"Fine", None))
    # retranslateUi

