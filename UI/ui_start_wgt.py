# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_wgtEtPfdR.ui'
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

import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(489, 635)
        Form.setStyleSheet(u"*{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align: left;\n"
"	padding: 10px 40px;\n"
"	color: rgb(224, 224, 224);\n"
"	background-color: rgb(31, 31, 31);\n"
"	border: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 30px;\n"
"	border-color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(63, 63, 63);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dataBtn = QPushButton(Form)
        self.dataBtn.setObjectName(u"dataBtn")
        self.dataBtn.setMinimumSize(QSize(0, 150))
        self.dataBtn.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dataBtn.setFont(font)
        self.dataBtn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/analysis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dataBtn.setIcon(icon)
        self.dataBtn.setIconSize(QSize(100, 100))
        self.dataBtn.setFlat(False)

        self.verticalLayout.addWidget(self.dataBtn)

        self.dataBtn_2 = QPushButton(Form)
        self.dataBtn_2.setObjectName(u"dataBtn_2")
        self.dataBtn_2.setMinimumSize(QSize(0, 150))
        self.dataBtn_2.setMaximumSize(QSize(16777215, 16777215))
        self.dataBtn_2.setFont(font)
        self.dataBtn_2.setStyleSheet(u"")
        self.dataBtn_2.setIcon(icon)
        self.dataBtn_2.setIconSize(QSize(100, 100))
        self.dataBtn_2.setFlat(False)

        self.verticalLayout.addWidget(self.dataBtn_2)

        self.dataBtn_3 = QPushButton(Form)
        self.dataBtn_3.setObjectName(u"dataBtn_3")
        self.dataBtn_3.setMinimumSize(QSize(0, 150))
        self.dataBtn_3.setMaximumSize(QSize(16777215, 16777215))
        self.dataBtn_3.setFont(font)
        self.dataBtn_3.setStyleSheet(u"")
        self.dataBtn_3.setIcon(icon)
        self.dataBtn_3.setIconSize(QSize(100, 100))
        self.dataBtn_3.setFlat(False)

        self.verticalLayout.addWidget(self.dataBtn_3)

        self.verticalSpacer = QSpacerItem(20, 146, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.dataBtn.setText(QCoreApplication.translate("Form", u"New grid", None))
        self.dataBtn_2.setText(QCoreApplication.translate("Form", u"Open grid", None))
        self.dataBtn_3.setText(QCoreApplication.translate("Form", u"Benchmark", None))
    # retranslateUi

