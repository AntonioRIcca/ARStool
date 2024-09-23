# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'elemProfCat_DlgNFdMju.ui'
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
        Dialog.resize(240, 140)
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
        self.titleLbl = QLabel(Dialog)
        self.titleLbl.setObjectName(u"titleLbl")
        self.titleLbl.setGeometry(QRect(0, 10, 240, 25))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.titleLbl.setFont(font)
        self.titleLbl.setAlignment(Qt.AlignCenter)
        self.confirmBtn = QPushButton(Dialog)
        self.confirmBtn.setObjectName(u"confirmBtn")
        self.confirmBtn.setGeometry(QRect(20, 100, 75, 23))
        self.cancelBtn = QPushButton(Dialog)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setGeometry(QRect(140, 100, 75, 23))
        self.profCatCB = QComboBox(Dialog)
        self.profCatCB.setObjectName(u"profCatCB")
        self.profCatCB.setGeometry(QRect(30, 50, 180, 25))
        QWidget.setTabOrder(self.profCatCB, self.confirmBtn)
        QWidget.setTabOrder(self.confirmBtn, self.cancelBtn)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Categoria profilo", None))
        self.titleLbl.setText(QCoreApplication.translate("Dialog", u"Seleziona la tipologia del profilo", None))
        self.confirmBtn.setText(QCoreApplication.translate("Dialog", u"Conferma", None))
        self.cancelBtn.setText(QCoreApplication.translate("Dialog", u"Cancella", None))
    # retranslateUi

