# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newGridDlgmZVEwb.ui'
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


class Ui_newGridDlg(object):
    def setupUi(self, newGridDlg):
        if newGridDlg.objectName():
            newGridDlg.setObjectName(u"newGridDlg")
        newGridDlg.resize(220, 160)
        newGridDlg.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.newGridWgt = QWidget(newGridDlg)
        self.newGridWgt.setObjectName(u"newGridWgt")
        self.newGridWgt.setGeometry(QRect(10, 10, 200, 140))
        self.newGridWgt.setStyleSheet(u"*{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	font: 7pt \"MS Shell Dlg 2\";\n"
"	border-radius: 10px;\n"
"	border: solid;\n"
"	border-width: 2px;\n"
"	border-color: rgb(255, 255, 255);\n"
"	background-color: rgb(63, 63, 63);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(127, 127, 127);\n"
"}\n"
"\n"
"\n"
"#mainWgt{\n"
"	border-radius: 15px;\n"
"	border: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")
        self.newGridLbl = QLabel(self.newGridWgt)
        self.newGridLbl.setObjectName(u"newGridLbl")
        self.newGridLbl.setGeometry(QRect(10, 10, 180, 13))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.newGridLbl.setFont(font)
        self.newGridLbl.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font-weight: bold;")
        self.newGridLbl.setAlignment(Qt.AlignCenter)
        self.nameLbl = QLabel(self.newGridWgt)
        self.nameLbl.setObjectName(u"nameLbl")
        self.nameLbl.setGeometry(QRect(10, 40, 90, 20))
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.nameLbl.setFont(font1)
        self.nameLe = QLineEdit(self.newGridWgt)
        self.nameLe.setObjectName(u"nameLe")
        self.nameLe.setGeometry(QRect(100, 40, 90, 20))
        self.nameLe.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sourceVLbl = QLabel(self.newGridWgt)
        self.sourceVLbl.setObjectName(u"sourceVLbl")
        self.sourceVLbl.setGeometry(QRect(10, 70, 90, 20))
        self.sourceVLbl.setFont(font1)
        self.sourceVDsb = QDoubleSpinBox(self.newGridWgt)
        self.sourceVDsb.setObjectName(u"sourceVDsb")
        self.sourceVDsb.setGeometry(QRect(100, 70, 90, 20))
        self.sourceVDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sourceVDsb.setDecimals(3)
        self.sourceVDsb.setMaximum(999.990000000000009)
        self.createPb = QPushButton(self.newGridWgt)
        self.createPb.setObjectName(u"createPb")
        self.createPb.setGeometry(QRect(10, 110, 75, 20))
        self.cancelPb = QPushButton(self.newGridWgt)
        self.cancelPb.setObjectName(u"cancelPb")
        self.cancelPb.setGeometry(QRect(110, 110, 75, 20))

        self.retranslateUi(newGridDlg)

        QMetaObject.connectSlotsByName(newGridDlg)
    # setupUi

    def retranslateUi(self, newGridDlg):
        newGridDlg.setWindowTitle(QCoreApplication.translate("newGridDlg", u"Dialog", None))
        self.newGridLbl.setText(QCoreApplication.translate("newGridDlg", u"Crea Nouva Rete", None))
        self.nameLbl.setText(QCoreApplication.translate("newGridDlg", u"Nome rete:", None))
        self.sourceVLbl.setText(QCoreApplication.translate("newGridDlg", u"V rete esterna", None))
        self.sourceVDsb.setSuffix(QCoreApplication.translate("newGridDlg", u" kV", None))
        self.createPb.setText(QCoreApplication.translate("newGridDlg", u"Crea", None))
        self.cancelPb.setText(QCoreApplication.translate("newGridDlg", u"Annulla", None))
    # retranslateUi

