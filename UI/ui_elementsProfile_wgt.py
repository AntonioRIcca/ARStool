# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'elementsProfile_wgtMZkZtu.ui'
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


class Ui_elemProfWgt(object):
    def setupUi(self, elemProfWgt):
        if elemProfWgt.objectName():
            elemProfWgt.setObjectName(u"elemProfWgt")
        elemProfWgt.resize(721, 716)
        self.mainWgt = QWidget(elemProfWgt)
        self.mainWgt.setObjectName(u"mainWgt")
        self.mainWgt.setGeometry(QRect(30, 20, 581, 661))
        self.mainWgt.setStyleSheet(u"*{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(191, 191, 191);\n"
"}\n"
"\n"
"\n"
"QGroupBox{\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 5px 50 5px 50px;\n"
"    background-color: rgb(0, 0, 21);\n"
"	border-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.mainWgt)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainSA = QScrollArea(self.mainWgt)
        self.mainSA.setObjectName(u"mainSA")
        self.mainSA.setMinimumSize(QSize(0, 0))
        self.mainSA.setMaximumSize(QSize(16777215, 16777215))
        self.mainSA.setStyleSheet(u"")
        self.mainSA.setWidgetResizable(True)
        self.mainSaWgt = QWidget()
        self.mainSaWgt.setObjectName(u"mainSaWgt")
        self.mainSaWgt.setGeometry(QRect(0, 0, 561, 641))
        self.mainSaWgtGL = QGridLayout(self.mainSaWgt)
        self.mainSaWgtGL.setObjectName(u"mainSaWgtGL")
        self.mainSaWgtGL.setVerticalSpacing(0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.mainSaWgtGL.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.mainSaWgtGL.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.ACLoadLbl = QLabel(self.mainSaWgt)
        self.ACLoadLbl.setObjectName(u"ACLoadLbl")
        self.ACLoadLbl.setMinimumSize(QSize(0, 30))
        self.ACLoadLbl.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ACLoadLbl.setFont(font)
        self.ACLoadLbl.setStyleSheet(u"border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    padding: 5px 150px;\n"
"    background-color: rgb(127, 127, 127);\n"
"    color: rgb(255, 255, 255);\n"
"")
        self.ACLoadLbl.setAlignment(Qt.AlignCenter)

        self.mainSaWgtGL.addWidget(self.ACLoadLbl, 1, 0, 1, 1)

        self.frame = QFrame(self.mainSaWgt)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 100))
        self.frame.setStyleSheet(u"*{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QFrame {\n"
"	border: solid;\n"
"	border-width: 2px;\n"
"	border-color: rgb(127, 127, 127);\n"
"	border-bottom-left-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QLabel {\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.elemLbl = QLabel(self.frame)
        self.elemLbl.setObjectName(u"elemLbl")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elemLbl.sizePolicy().hasHeightForWidth())
        self.elemLbl.setSizePolicy(sizePolicy)
        self.elemLbl.setMinimumSize(QSize(0, 30))
        self.elemLbl.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.elemLbl, 0, 0, 1, 1)

        self.catLbl = QLabel(self.frame)
        self.catLbl.setObjectName(u"catLbl")

        self.gridLayout.addWidget(self.catLbl, 0, 1, 1, 1)

        self.typeCB = QComboBox(self.frame)
        self.typeCB.setObjectName(u"typeCB")

        self.gridLayout.addWidget(self.typeCB, 0, 2, 1, 1)

        self.elemLbl_2 = QLabel(self.frame)
        self.elemLbl_2.setObjectName(u"elemLbl_2")
        sizePolicy.setHeightForWidth(self.elemLbl_2.sizePolicy().hasHeightForWidth())
        self.elemLbl_2.setSizePolicy(sizePolicy)
        self.elemLbl_2.setMinimumSize(QSize(0, 30))
        self.elemLbl_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.elemLbl_2, 1, 0, 1, 1)

        self.catLbl_2 = QLabel(self.frame)
        self.catLbl_2.setObjectName(u"catLbl_2")

        self.gridLayout.addWidget(self.catLbl_2, 1, 1, 1, 1)

        self.typeCB_2 = QComboBox(self.frame)
        self.typeCB_2.setObjectName(u"typeCB_2")

        self.gridLayout.addWidget(self.typeCB_2, 1, 2, 1, 1)

        self.elemLbl_3 = QLabel(self.frame)
        self.elemLbl_3.setObjectName(u"elemLbl_3")
        sizePolicy.setHeightForWidth(self.elemLbl_3.sizePolicy().hasHeightForWidth())
        self.elemLbl_3.setSizePolicy(sizePolicy)
        self.elemLbl_3.setMinimumSize(QSize(0, 30))
        self.elemLbl_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.elemLbl_3, 2, 0, 1, 1)

        self.catLbl_3 = QLabel(self.frame)
        self.catLbl_3.setObjectName(u"catLbl_3")

        self.gridLayout.addWidget(self.catLbl_3, 2, 1, 1, 1)

        self.typeCB_4 = QComboBox(self.frame)
        self.typeCB_4.setObjectName(u"typeCB_4")

        self.gridLayout.addWidget(self.typeCB_4, 2, 2, 1, 1)

        self.elemLbl_4 = QLabel(self.frame)
        self.elemLbl_4.setObjectName(u"elemLbl_4")
        sizePolicy.setHeightForWidth(self.elemLbl_4.sizePolicy().hasHeightForWidth())
        self.elemLbl_4.setSizePolicy(sizePolicy)
        self.elemLbl_4.setMinimumSize(QSize(0, 30))
        self.elemLbl_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.elemLbl_4, 3, 0, 1, 1)

        self.catLbl_4 = QLabel(self.frame)
        self.catLbl_4.setObjectName(u"catLbl_4")

        self.gridLayout.addWidget(self.catLbl_4, 3, 1, 1, 1)

        self.typeCB_3 = QComboBox(self.frame)
        self.typeCB_3.setObjectName(u"typeCB_3")

        self.gridLayout.addWidget(self.typeCB_3, 3, 2, 1, 1)


        self.mainSaWgtGL.addWidget(self.frame, 2, 0, 1, 1)

        self.mainSA.setWidget(self.mainSaWgt)

        self.verticalLayout.addWidget(self.mainSA)


        self.retranslateUi(elemProfWgt)

        QMetaObject.connectSlotsByName(elemProfWgt)
    # setupUi

    def retranslateUi(self, elemProfWgt):
        elemProfWgt.setWindowTitle(QCoreApplication.translate("elemProfWgt", u"Form", None))
        self.ACLoadLbl.setText(QCoreApplication.translate("elemProfWgt", u"AC Load", None))
        self.elemLbl.setText(QCoreApplication.translate("elemProfWgt", u"Nome elemento", None))
        self.catLbl.setText(QCoreApplication.translate("elemProfWgt", u"Categoria", None))
        self.elemLbl_2.setText(QCoreApplication.translate("elemProfWgt", u"Nome elemento", None))
        self.catLbl_2.setText(QCoreApplication.translate("elemProfWgt", u"Categoria", None))
        self.elemLbl_3.setText(QCoreApplication.translate("elemProfWgt", u"Nome elemento", None))
        self.catLbl_3.setText(QCoreApplication.translate("elemProfWgt", u"Categoria", None))
        self.elemLbl_4.setText(QCoreApplication.translate("elemProfWgt", u"Nome elemento", None))
        self.catLbl_4.setText(QCoreApplication.translate("elemProfWgt", u"Categoria", None))
    # retranslateUi

