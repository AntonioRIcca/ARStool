# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'onrParWgtJtFbvE.ui'
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
        Form.resize(640, 480)
        Form.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.onrParWgt = QWidget(Form)
        self.onrParWgt.setObjectName(u"onrParWgt")
        self.onrParWgt.setGeometry(QRect(110, 60, 271, 51))
        self.onrParWgt.setStyleSheet(u"*{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton{\n"
"	border: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(223, 223, 223);\n"
"	border-radius: 8px;\n"
"	background-color: rgb(31, 31, 31);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(64, 64, 64); \n"
"	border-style: inset\n"
"}\n"
"\n"
"#relParWgt{\n"
"	border: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(223, 223, 223);\n"
"	border-radius: 15px;\n"
"}")
        self.gridLayout = QGridLayout(self.onrParWgt)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.onrLogicLbl = QLabel(self.onrParWgt)
        self.onrLogicLbl.setObjectName(u"onrLogicLbl")
        self.onrLogicLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.onrLogicLbl, 0, 0, 1, 1)

        self.onrLogicCB = QComboBox(self.onrParWgt)
        self.onrLogicCB.addItem("")
        self.onrLogicCB.addItem("")
        self.onrLogicCB.addItem("")
        self.onrLogicCB.setObjectName(u"onrLogicCB")
        self.onrLogicCB.setMaximumSize(QSize(50, 16777215))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.onrLogicCB.setFont(font)

        self.gridLayout.addWidget(self.onrLogicCB, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.onrLogicLbl.setText(QCoreApplication.translate("Form", u"Scegli logica di automazione:", None))
        self.onrLogicCB.setItemText(0, QCoreApplication.translate("Form", u"FRG", None))
        self.onrLogicCB.setItemText(1, QCoreApplication.translate("Form", u"FNG", None))
        self.onrLogicCB.setItemText(2, QCoreApplication.translate("Form", u"SFS", None))

    # retranslateUi

