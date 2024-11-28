# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'relParWgtkmynJU.ui'
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
        self.relParWgt = QWidget(Form)
        self.relParWgt.setObjectName(u"relParWgt")
        self.relParWgt.setGeometry(QRect(110, 60, 271, 91))
        self.relParWgt.setStyleSheet(u"*{\n"
"	color: rgb(255, 255, 255);\n"
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
        self.gridLayout = QGridLayout(self.relParWgt)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.missionTimeLbl = QLabel(self.relParWgt)
        self.missionTimeLbl.setObjectName(u"missionTimeLbl")
        self.missionTimeLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.missionTimeLbl, 0, 0, 1, 1)

        self.tempProfLbl = QLabel(self.relParWgt)
        self.tempProfLbl.setObjectName(u"tempProfLbl")
        self.tempProfLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.tempProfLbl, 1, 0, 1, 1)

        self.tempProfPb = QPushButton(self.relParWgt)
        self.tempProfPb.setObjectName(u"tempProfPb")
        self.tempProfPb.setMinimumSize(QSize(0, 20))
        self.tempProfPb.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.tempProfPb, 1, 1, 1, 1)

        self.missionTimeDsb = QDoubleSpinBox(self.relParWgt)
        self.missionTimeDsb.setObjectName(u"missionTimeDsb")
        self.missionTimeDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.missionTimeDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout.addWidget(self.missionTimeDsb, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.missionTimeLbl.setText(QCoreApplication.translate("Form", u"Mission Time", None))
        self.tempProfLbl.setText(QCoreApplication.translate("Form", u"Temperature Prodile", None))
        self.tempProfPb.setText(QCoreApplication.translate("Form", u"View", None))
        self.missionTimeDsb.setSuffix(QCoreApplication.translate("Form", u" h", None))
    # retranslateUi

