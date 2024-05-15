# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_wgtxvxmFW.ui'
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
        Form.resize(491, 685)
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
"	border-radius: 20px;\n"
"	border-color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(63, 63, 63);\n"
"}\n"
"")
        self.startWgt = QWidget(Form)
        self.startWgt.setObjectName(u"startWgt")
        self.startWgt.setGeometry(QRect(10, 0, 421, 635))
        self.verticalLayout = QVBoxLayout(self.startWgt)
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 9, -1, -1)
        self.importDssBtn = QPushButton(self.startWgt)
        self.importDssBtn.setObjectName(u"importDssBtn")
        self.importDssBtn.setMinimumSize(QSize(0, 80))
        self.importDssBtn.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.importDssBtn.setFont(font)
        self.importDssBtn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/importfile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.importDssBtn.setIcon(icon)
        self.importDssBtn.setIconSize(QSize(50, 50))
        self.importDssBtn.setFlat(False)

        self.verticalLayout.addWidget(self.importDssBtn)

        self.openFileBtn = QPushButton(self.startWgt)
        self.openFileBtn.setObjectName(u"openFileBtn")
        self.openFileBtn.setMinimumSize(QSize(0, 80))
        self.openFileBtn.setMaximumSize(QSize(16777215, 16777215))
        self.openFileBtn.setFont(font)
        self.openFileBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/openfile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openFileBtn.setIcon(icon1)
        self.openFileBtn.setIconSize(QSize(50, 50))
        self.openFileBtn.setFlat(False)

        self.verticalLayout.addWidget(self.openFileBtn)

        self.benchOpenBtn = QPushButton(self.startWgt)
        self.benchOpenBtn.setObjectName(u"benchOpenBtn")
        self.benchOpenBtn.setMinimumSize(QSize(0, 80))
        self.benchOpenBtn.setMaximumSize(QSize(16777215, 16777215))
        self.benchOpenBtn.setFont(font)
        self.benchOpenBtn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/benchmark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.benchOpenBtn.setIcon(icon2)
        self.benchOpenBtn.setIconSize(QSize(50, 50))
        self.benchOpenBtn.setFlat(False)

        self.verticalLayout.addWidget(self.benchOpenBtn)

        self.startSpacer = QSpacerItem(20, 146, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.startSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.importDssBtn.setText(QCoreApplication.translate("Form", u"  Importa file DSS", None))
        self.openFileBtn.setText(QCoreApplication.translate("Form", u"  Apri rete", None))
        self.benchOpenBtn.setText(QCoreApplication.translate("Form", u"  Benchmark", None))
    # retranslateUi

