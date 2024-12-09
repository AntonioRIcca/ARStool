# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'onrResWgtyOIQhm.ui'
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
        Form.resize(1701, 1164)
        Form.setStyleSheet(u"\n"
"\n"
"/**\n"
"QTabWidget::pane {10px solid #C2C7CB;}\n"
"**/")
        self.onrMainWgt = QWidget(Form)
        self.onrMainWgt.setObjectName(u"onrMainWgt")
        self.onrMainWgt.setGeometry(QRect(10, 10, 900, 758))
        self.onrMainWgt.setMinimumSize(QSize(0, 0))
        self.onrMainWgt.setStyleSheet(u"background-color: #1f232a;\n"
"color: rgb(255, 170, 0);\n"
"")
        self.onrMainVBL = QVBoxLayout(self.onrMainWgt)
        self.onrMainVBL.setSpacing(10)
        self.onrMainVBL.setObjectName(u"onrMainVBL")
        self.onrMainVBL.setContentsMargins(0, 0, 0, 0)
        self.onrTitleLbl = QLabel(self.onrMainWgt)
        self.onrTitleLbl.setObjectName(u"onrTitleLbl")
        self.onrTitleLbl.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.onrMainVBL.addWidget(self.onrTitleLbl)

        self.onrTabWgt = QTabWidget(self.onrMainWgt)
        self.onrTabWgt.setObjectName(u"onrTabWgt")
        self.onrTabWgt.setStyleSheet(u"QTabBar::tab{\n"
"	\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	height: 120px;\n"
"	width: 30\n"
"px;\n"
"}\n"
"\n"
"QTabBar::tab::selected{\n"
"	background-color: rgb(63, 63, 63);\n"
"}\n"
"\n"
"QTabWidget::pane{\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.onrTabWgt.setTabPosition(QTabWidget.East)
        self.onr1TabWgt = QWidget()
        self.onr1TabWgt.setObjectName(u"onr1TabWgt")
        self.onr1TabWgt.setStyleSheet(u"")
        self.onr1TabVBL = QVBoxLayout(self.onr1TabWgt)
        self.onr1TabVBL.setSpacing(0)
        self.onr1TabVBL.setObjectName(u"onr1TabVBL")
        self.onr1TabVBL.setContentsMargins(0, 0, 0, 0)
        self.onr1Wgt = QWidget(self.onr1TabWgt)
        self.onr1Wgt.setObjectName(u"onr1Wgt")
        self.onr1HBL = QHBoxLayout(self.onr1Wgt)
        self.onr1HBL.setObjectName(u"onr1HBL")
        self.onr1sxWgt = QWidget(self.onr1Wgt)
        self.onr1sxWgt.setObjectName(u"onr1sxWgt")
        self.onr1sxVBL = QVBoxLayout(self.onr1sxWgt)
        self.onr1sxVBL.setSpacing(20)
        self.onr1sxVBL.setObjectName(u"onr1sxVBL")
        self.onr1sxVBL.setContentsMargins(5, 5, 5, 5)
        self.onr1sxTitleLbl = QLabel(self.onr1sxWgt)
        self.onr1sxTitleLbl.setObjectName(u"onr1sxTitleLbl")
        self.onr1sxTitleLbl.setMinimumSize(QSize(0, 30))
        self.onr1sxTitleLbl.setMaximumSize(QSize(16777215, 30))
        self.onr1sxTitleLbl.setSizeIncrement(QSize(0, 30))
        self.onr1sxTitleLbl.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-top: 1px solid rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(255, 255, 255);")
        self.onr1sxTitleLbl.setAlignment(Qt.AlignCenter)

        self.onr1sxVBL.addWidget(self.onr1sxTitleLbl)

        self.onr1sxFigLbl = QLabel(self.onr1sxWgt)
        self.onr1sxFigLbl.setObjectName(u"onr1sxFigLbl")

        self.onr1sxVBL.addWidget(self.onr1sxFigLbl)

        self.onr1logLbl = QLabel(self.onr1sxWgt)
        self.onr1logLbl.setObjectName(u"onr1logLbl")
        self.onr1logLbl.setMinimumSize(QSize(0, 200))
        self.onr1logLbl.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-top: 1px solid  rgb(255, 255, 255);\n"
"border-bottom: 1px solid  rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.onr1logLbl.setMargin(10)

        self.onr1sxVBL.addWidget(self.onr1logLbl)

        self.onr1SxSpc = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.onr1sxVBL.addItem(self.onr1SxSpc)


        self.onr1HBL.addWidget(self.onr1sxWgt)

        self.onr1dxWgt = QWidget(self.onr1Wgt)
        self.onr1dxWgt.setObjectName(u"onr1dxWgt")
        self.onr1dxVBL = QVBoxLayout(self.onr1dxWgt)
        self.onr1dxVBL.setSpacing(20)
        self.onr1dxVBL.setObjectName(u"onr1dxVBL")
        self.onr1dxVBL.setContentsMargins(5, 5, 5, 5)
        self.onr1dxTitleLbl = QLabel(self.onr1dxWgt)
        self.onr1dxTitleLbl.setObjectName(u"onr1dxTitleLbl")
        self.onr1dxTitleLbl.setMinimumSize(QSize(0, 30))
        self.onr1dxTitleLbl.setMaximumSize(QSize(16777215, 30))
        self.onr1dxTitleLbl.setSizeIncrement(QSize(0, 30))
        self.onr1dxTitleLbl.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-top: 1px solid rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(255, 255, 255);")
        self.onr1dxTitleLbl.setAlignment(Qt.AlignCenter)

        self.onr1dxVBL.addWidget(self.onr1dxTitleLbl)

        self.onr1dxFigLbl = QLabel(self.onr1dxWgt)
        self.onr1dxFigLbl.setObjectName(u"onr1dxFigLbl")

        self.onr1dxVBL.addWidget(self.onr1dxFigLbl)

        self.onr1dxSpc = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.onr1dxVBL.addItem(self.onr1dxSpc)


        self.onr1HBL.addWidget(self.onr1dxWgt)


        self.onr1TabVBL.addWidget(self.onr1Wgt)

        self.indexCalcPb = QPushButton(self.onr1TabWgt)
        self.indexCalcPb.setObjectName(u"indexCalcPb")
        self.indexCalcPb.setMinimumSize(QSize(0, 40))
        self.indexCalcPb.setMaximumSize(QSize(16777215, 40))
        self.indexCalcPb.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(127, 127, 127);\n"
"	border-radius: 10px\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(63, 63, 63);\n"
"	border-style: inset;\n"
"}\n"
"")

        self.onr1TabVBL.addWidget(self.indexCalcPb)

        self.onrTabWgt.addTab(self.onr1TabWgt, "")
        self.onr2TabWgt = QWidget()
        self.onr2TabWgt.setObjectName(u"onr2TabWgt")
        self.onr2TabHBL = QHBoxLayout(self.onr2TabWgt)
        self.onr2TabHBL.setSpacing(0)
        self.onr2TabHBL.setObjectName(u"onr2TabHBL")
        self.onr2TabHBL.setContentsMargins(0, 0, 0, 0)
        self.onr2sxWgt = QWidget(self.onr2TabWgt)
        self.onr2sxWgt.setObjectName(u"onr2sxWgt")
        self.onr2sxVBL = QVBoxLayout(self.onr2sxWgt)
        self.onr2sxVBL.setSpacing(20)
        self.onr2sxVBL.setObjectName(u"onr2sxVBL")
        self.onr2sxVBL.setContentsMargins(10, 10, 10, 10)
        self.onr2sxTitleLbl = QLabel(self.onr2sxWgt)
        self.onr2sxTitleLbl.setObjectName(u"onr2sxTitleLbl")
        self.onr2sxTitleLbl.setMinimumSize(QSize(0, 30))
        self.onr2sxTitleLbl.setMaximumSize(QSize(16777215, 30))
        self.onr2sxTitleLbl.setSizeIncrement(QSize(0, 30))
        self.onr2sxTitleLbl.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-top: 1px solid rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(255, 255, 255);")
        self.onr2sxTitleLbl.setAlignment(Qt.AlignCenter)

        self.onr2sxVBL.addWidget(self.onr2sxTitleLbl)

        self.onr2sxFigWgt = QWidget(self.onr2sxWgt)
        self.onr2sxFigWgt.setObjectName(u"onr2sxFigWgt")
        self.onr2sxFigGL = QGridLayout(self.onr2sxFigWgt)
        self.onr2sxFigGL.setSpacing(10)
        self.onr2sxFigGL.setObjectName(u"onr2sxFigGL")
        self.onr2sxFigGL.setContentsMargins(0, 0, 0, 0)
        self.onr2Fig1Lbl = QLabel(self.onr2sxFigWgt)
        self.onr2Fig1Lbl.setObjectName(u"onr2Fig1Lbl")

        self.onr2sxFigGL.addWidget(self.onr2Fig1Lbl, 0, 0, 1, 1)

        self.onr2Fig2Lbl = QLabel(self.onr2sxFigWgt)
        self.onr2Fig2Lbl.setObjectName(u"onr2Fig2Lbl")

        self.onr2sxFigGL.addWidget(self.onr2Fig2Lbl, 0, 1, 1, 1)

        self.onr2Fig3Lbl = QLabel(self.onr2sxFigWgt)
        self.onr2Fig3Lbl.setObjectName(u"onr2Fig3Lbl")

        self.onr2sxFigGL.addWidget(self.onr2Fig3Lbl, 1, 0, 1, 1)

        self.onr2Fig4Lbl = QLabel(self.onr2sxFigWgt)
        self.onr2Fig4Lbl.setObjectName(u"onr2Fig4Lbl")

        self.onr2sxFigGL.addWidget(self.onr2Fig4Lbl, 1, 1, 1, 1)


        self.onr2sxVBL.addWidget(self.onr2sxFigWgt)

        self.onr2sxSpc = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.onr2sxVBL.addItem(self.onr2sxSpc)

        self.onr2calcWgt = QWidget(self.onr2sxWgt)
        self.onr2calcWgt.setObjectName(u"onr2calcWgt")
        self.onr2calcWgt.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.onr2calcHBL = QHBoxLayout(self.onr2calcWgt)
        self.onr2calcHBL.setObjectName(u"onr2calcHBL")
        self.onr2calcLbl = QLabel(self.onr2calcWgt)
        self.onr2calcLbl.setObjectName(u"onr2calcLbl")
        self.onr2calcLbl.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")
        self.onr2calcLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2calcHBL.addWidget(self.onr2calcLbl)

        self.onr2calcCB = QComboBox(self.onr2calcWgt)
        self.onr2calcCB.addItem("")
        self.onr2calcCB.addItem("")
        self.onr2calcCB.addItem("")
        self.onr2calcCB.setObjectName(u"onr2calcCB")
        self.onr2calcCB.setMinimumSize(QSize(0, 40))
        self.onr2calcCB.setMaximumSize(QSize(70, 16777215))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.onr2calcCB.setFont(font)
        self.onr2calcCB.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")

        self.onr2calcHBL.addWidget(self.onr2calcCB)

        self.onr2calcBtn = QPushButton(self.onr2calcWgt)
        self.onr2calcBtn.setObjectName(u"onr2calcBtn")
        self.onr2calcBtn.setMinimumSize(QSize(0, 40))
        self.onr2calcBtn.setMaximumSize(QSize(16777215, 40))
        self.onr2calcBtn.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(127, 127, 127);\n"
"	border-radius: 10px\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(63, 63, 63);\n"
"	border-style: inset;\n"
"}\n"
"")

        self.onr2calcHBL.addWidget(self.onr2calcBtn)


        self.onr2sxVBL.addWidget(self.onr2calcWgt)


        self.onr2TabHBL.addWidget(self.onr2sxWgt)

        self.onr2dxWgt = QWidget(self.onr2TabWgt)
        self.onr2dxWgt.setObjectName(u"onr2dxWgt")
        self.onr2dxWgt.setMinimumSize(QSize(300, 0))
        self.onr2dxWgt.setMaximumSize(QSize(300, 16777215))
        self.onr2dxWgt.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.onr2dxVBL = QVBoxLayout(self.onr2dxWgt)
        self.onr2dxVBL.setSpacing(20)
        self.onr2dxVBL.setObjectName(u"onr2dxVBL")
        self.onr2dxVBL.setContentsMargins(10, 10, 10, 10)
        self.onr2dxTopSpc = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.onr2dxVBL.addItem(self.onr2dxTopSpc)

        self.onr2indTitleLbl = QLabel(self.onr2dxWgt)
        self.onr2indTitleLbl.setObjectName(u"onr2indTitleLbl")
        self.onr2indTitleLbl.setMinimumSize(QSize(0, 30))
        self.onr2indTitleLbl.setMaximumSize(QSize(16777215, 30))
        self.onr2indTitleLbl.setSizeIncrement(QSize(0, 30))
        self.onr2indTitleLbl.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(255, 255, 255);")
        self.onr2indTitleLbl.setAlignment(Qt.AlignCenter)

        self.onr2dxVBL.addWidget(self.onr2indTitleLbl)

        self.onr2indWgt = QWidget(self.onr2dxWgt)
        self.onr2indWgt.setObjectName(u"onr2indWgt")
        self.onr2indGL = QGridLayout(self.onr2indWgt)
        self.onr2indGL.setSpacing(0)
        self.onr2indGL.setObjectName(u"onr2indGL")
        self.onr2indFRGSAIFILbl = QLabel(self.onr2indWgt)
        self.onr2indFRGSAIFILbl.setObjectName(u"onr2indFRGSAIFILbl")
        self.onr2indFRGSAIFILbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2indGL.addWidget(self.onr2indFRGSAIFILbl, 2, 3, 1, 1)

        self.onr2indTitleEENSLbl = QLabel(self.onr2indWgt)
        self.onr2indTitleEENSLbl.setObjectName(u"onr2indTitleEENSLbl")
        self.onr2indTitleEENSLbl.setMinimumSize(QSize(70, 0))
        font1 = QFont()
        font1.setItalic(True)
        self.onr2indTitleEENSLbl.setFont(font1)
        self.onr2indTitleEENSLbl.setStyleSheet(u"border-bottom: 1px solid rgb(255, 170, 0);")
        self.onr2indTitleEENSLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr2indTitleEENSLbl.setMargin(2)

        self.onr2indGL.addWidget(self.onr2indTitleEENSLbl, 1, 1, 1, 1)

        self.onr2indNullLbl = QLabel(self.onr2indWgt)
        self.onr2indNullLbl.setObjectName(u"onr2indNullLbl")
        self.onr2indNullLbl.setMinimumSize(QSize(40, 20))
        self.onr2indNullLbl.setMaximumSize(QSize(40, 20))
        self.onr2indNullLbl.setFont(font1)
        self.onr2indNullLbl.setStyleSheet(u"border-bottom: 1px solid rgb(255, 170, 0);\n"
"border-right: 1px solid rgb(255, 170, 0);")
        self.onr2indNullLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr2indNullLbl.setMargin(5)

        self.onr2indGL.addWidget(self.onr2indNullLbl, 1, 0, 1, 1)

        self.onr2indFRGSAIDILbl = QLabel(self.onr2indWgt)
        self.onr2indFRGSAIDILbl.setObjectName(u"onr2indFRGSAIDILbl")
        self.onr2indFRGSAIDILbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2indGL.addWidget(self.onr2indFRGSAIDILbl, 2, 2, 1, 1)

        self.onr2indTitleSAIFILbl = QLabel(self.onr2indWgt)
        self.onr2indTitleSAIFILbl.setObjectName(u"onr2indTitleSAIFILbl")
        self.onr2indTitleSAIFILbl.setMinimumSize(QSize(70, 0))
        self.onr2indTitleSAIFILbl.setFont(font1)
        self.onr2indTitleSAIFILbl.setStyleSheet(u"border-bottom: 1px solid rgb(255, 170, 0);")
        self.onr2indTitleSAIFILbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr2indTitleSAIFILbl.setMargin(2)

        self.onr2indGL.addWidget(self.onr2indTitleSAIFILbl, 1, 3, 1, 1)

        self.onr2indTitleSAIDILbl = QLabel(self.onr2indWgt)
        self.onr2indTitleSAIDILbl.setObjectName(u"onr2indTitleSAIDILbl")
        self.onr2indTitleSAIDILbl.setMinimumSize(QSize(70, 0))
        self.onr2indTitleSAIDILbl.setFont(font1)
        self.onr2indTitleSAIDILbl.setStyleSheet(u"border-bottom: 1px solid rgb(255, 170, 0);")
        self.onr2indTitleSAIDILbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr2indTitleSAIDILbl.setMargin(2)

        self.onr2indGL.addWidget(self.onr2indTitleSAIDILbl, 1, 2, 1, 1)

        self.onr2indFNCEENSLbl = QLabel(self.onr2indWgt)
        self.onr2indFNCEENSLbl.setObjectName(u"onr2indFNCEENSLbl")
        self.onr2indFNCEENSLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2indGL.addWidget(self.onr2indFNCEENSLbl, 4, 1, 1, 1)

        self.onr2indSFSEENSLbl = QLabel(self.onr2indWgt)
        self.onr2indSFSEENSLbl.setObjectName(u"onr2indSFSEENSLbl")
        self.onr2indSFSEENSLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2indGL.addWidget(self.onr2indSFSEENSLbl, 5, 1, 1, 1)

        self.onr2indFNCSAIDILbl = QLabel(self.onr2indWgt)
        self.onr2indFNCSAIDILbl.setObjectName(u"onr2indFNCSAIDILbl")
        self.onr2indFNCSAIDILbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2indGL.addWidget(self.onr2indFNCSAIDILbl, 4, 2, 1, 1)

        self.onr2indSFSSAIFILbl = QLabel(self.onr2indWgt)
        self.onr2indSFSSAIFILbl.setObjectName(u"onr2indSFSSAIFILbl")
        self.onr2indSFSSAIFILbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2indGL.addWidget(self.onr2indSFSSAIFILbl, 5, 3, 1, 1)

        self.onr2indSFSSAIDILbl = QLabel(self.onr2indWgt)
        self.onr2indSFSSAIDILbl.setObjectName(u"onr2indSFSSAIDILbl")
        self.onr2indSFSSAIDILbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2indGL.addWidget(self.onr2indSFSSAIDILbl, 5, 2, 1, 1)

        self.onr2indFRGTitleLbl = QLabel(self.onr2indWgt)
        self.onr2indFRGTitleLbl.setObjectName(u"onr2indFRGTitleLbl")
        self.onr2indFRGTitleLbl.setMinimumSize(QSize(0, 25))
        self.onr2indFRGTitleLbl.setMaximumSize(QSize(16777215, 20))
        self.onr2indFRGTitleLbl.setFont(font1)
        self.onr2indFRGTitleLbl.setStyleSheet(u"border-right: 1px solid rgb(255, 170, 0);")
        self.onr2indFRGTitleLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr2indFRGTitleLbl.setMargin(2)

        self.onr2indGL.addWidget(self.onr2indFRGTitleLbl, 2, 0, 1, 1)

        self.onr2indSFSTitleLbl = QLabel(self.onr2indWgt)
        self.onr2indSFSTitleLbl.setObjectName(u"onr2indSFSTitleLbl")
        self.onr2indSFSTitleLbl.setMinimumSize(QSize(0, 25))
        self.onr2indSFSTitleLbl.setMaximumSize(QSize(16777215, 20))
        self.onr2indSFSTitleLbl.setFont(font1)
        self.onr2indSFSTitleLbl.setStyleSheet(u"border-right: 1px solid rgb(255, 170, 0);")
        self.onr2indSFSTitleLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr2indSFSTitleLbl.setMargin(2)

        self.onr2indGL.addWidget(self.onr2indSFSTitleLbl, 5, 0, 1, 1)

        self.onr2indFNCTitleLbl = QLabel(self.onr2indWgt)
        self.onr2indFNCTitleLbl.setObjectName(u"onr2indFNCTitleLbl")
        self.onr2indFNCTitleLbl.setMinimumSize(QSize(0, 25))
        self.onr2indFNCTitleLbl.setMaximumSize(QSize(16777215, 20))
        self.onr2indFNCTitleLbl.setFont(font1)
        self.onr2indFNCTitleLbl.setStyleSheet(u"border-right: 1px solid rgb(255, 170, 0);")
        self.onr2indFNCTitleLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr2indFNCTitleLbl.setMargin(2)

        self.onr2indGL.addWidget(self.onr2indFNCTitleLbl, 4, 0, 1, 1)

        self.onr2indFNCSAIFILbl = QLabel(self.onr2indWgt)
        self.onr2indFNCSAIFILbl.setObjectName(u"onr2indFNCSAIFILbl")
        self.onr2indFNCSAIFILbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2indGL.addWidget(self.onr2indFNCSAIFILbl, 4, 3, 1, 1)

        self.onr2indFRGEENSLbl = QLabel(self.onr2indWgt)
        self.onr2indFRGEENSLbl.setObjectName(u"onr2indFRGEENSLbl")
        self.onr2indFRGEENSLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2indGL.addWidget(self.onr2indFRGEENSLbl, 2, 1, 1, 1)

        self.onr2indSpc = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.onr2indGL.addItem(self.onr2indSpc, 1, 4, 1, 1)


        self.onr2dxVBL.addWidget(self.onr2indWgt)

        self.onr2dx1Spc = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.onr2dxVBL.addItem(self.onr2dx1Spc)

        self.onr2indNormTitleLbl = QLabel(self.onr2dxWgt)
        self.onr2indNormTitleLbl.setObjectName(u"onr2indNormTitleLbl")
        self.onr2indNormTitleLbl.setMinimumSize(QSize(0, 30))
        self.onr2indNormTitleLbl.setMaximumSize(QSize(16777215, 30))
        self.onr2indNormTitleLbl.setSizeIncrement(QSize(0, 30))
        self.onr2indNormTitleLbl.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(255, 255, 255);")
        self.onr2indNormTitleLbl.setAlignment(Qt.AlignCenter)

        self.onr2dxVBL.addWidget(self.onr2indNormTitleLbl)

        self.onr2indNormWgt = QWidget(self.onr2dxWgt)
        self.onr2indNormWgt.setObjectName(u"onr2indNormWgt")
        self.onr2indNormGL = QGridLayout(self.onr2indNormWgt)
        self.onr2indNormGL.setSpacing(0)
        self.onr2indNormGL.setObjectName(u"onr2indNormGL")
        self.onr2indNormFRGSAIFILbl = QLabel(self.onr2indNormWgt)
        self.onr2indNormFRGSAIFILbl.setObjectName(u"onr2indNormFRGSAIFILbl")
        self.onr2indNormFRGSAIFILbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2indNormGL.addWidget(self.onr2indNormFRGSAIFILbl, 2, 3, 1, 1)

        self.onr2indNormTitleEENSLbl = QLabel(self.onr2indNormWgt)
        self.onr2indNormTitleEENSLbl.setObjectName(u"onr2indNormTitleEENSLbl")
        self.onr2indNormTitleEENSLbl.setMinimumSize(QSize(70, 0))
        self.onr2indNormTitleEENSLbl.setFont(font1)
        self.onr2indNormTitleEENSLbl.setStyleSheet(u"border-bottom: 1px solid rgb(255, 170, 0);")
        self.onr2indNormTitleEENSLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr2indNormTitleEENSLbl.setMargin(2)

        self.onr2indNormGL.addWidget(self.onr2indNormTitleEENSLbl, 1, 1, 1, 1)

        self.onr2indNormFRGSAIDILbl = QLabel(self.onr2indNormWgt)
        self.onr2indNormFRGSAIDILbl.setObjectName(u"onr2indNormFRGSAIDILbl")
        self.onr2indNormFRGSAIDILbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2indNormGL.addWidget(self.onr2indNormFRGSAIDILbl, 2, 2, 1, 1)

        self.onr2indNormTitleSAIFILbl = QLabel(self.onr2indNormWgt)
        self.onr2indNormTitleSAIFILbl.setObjectName(u"onr2indNormTitleSAIFILbl")
        self.onr2indNormTitleSAIFILbl.setMinimumSize(QSize(70, 0))
        self.onr2indNormTitleSAIFILbl.setFont(font1)
        self.onr2indNormTitleSAIFILbl.setStyleSheet(u"border-bottom: 1px solid rgb(255, 170, 0);")
        self.onr2indNormTitleSAIFILbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr2indNormTitleSAIFILbl.setMargin(2)

        self.onr2indNormGL.addWidget(self.onr2indNormTitleSAIFILbl, 1, 3, 1, 1)

        self.onr2indNormTitleSAIDILbl = QLabel(self.onr2indNormWgt)
        self.onr2indNormTitleSAIDILbl.setObjectName(u"onr2indNormTitleSAIDILbl")
        self.onr2indNormTitleSAIDILbl.setMinimumSize(QSize(70, 0))
        self.onr2indNormTitleSAIDILbl.setFont(font1)
        self.onr2indNormTitleSAIDILbl.setStyleSheet(u"border-bottom: 1px solid rgb(255, 170, 0);")
        self.onr2indNormTitleSAIDILbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr2indNormTitleSAIDILbl.setMargin(2)

        self.onr2indNormGL.addWidget(self.onr2indNormTitleSAIDILbl, 1, 2, 1, 1)

        self.onr2indNormFNCEENSLbl = QLabel(self.onr2indNormWgt)
        self.onr2indNormFNCEENSLbl.setObjectName(u"onr2indNormFNCEENSLbl")
        self.onr2indNormFNCEENSLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2indNormGL.addWidget(self.onr2indNormFNCEENSLbl, 4, 1, 1, 1)

        self.onr2indNormSFSEENSLbl = QLabel(self.onr2indNormWgt)
        self.onr2indNormSFSEENSLbl.setObjectName(u"onr2indNormSFSEENSLbl")
        self.onr2indNormSFSEENSLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2indNormGL.addWidget(self.onr2indNormSFSEENSLbl, 5, 1, 1, 1)

        self.onr2indNormFNCSAIDILbl = QLabel(self.onr2indNormWgt)
        self.onr2indNormFNCSAIDILbl.setObjectName(u"onr2indNormFNCSAIDILbl")
        self.onr2indNormFNCSAIDILbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2indNormGL.addWidget(self.onr2indNormFNCSAIDILbl, 4, 2, 1, 1)

        self.onr2indNormSFSSAIFILbl = QLabel(self.onr2indNormWgt)
        self.onr2indNormSFSSAIFILbl.setObjectName(u"onr2indNormSFSSAIFILbl")
        self.onr2indNormSFSSAIFILbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2indNormGL.addWidget(self.onr2indNormSFSSAIFILbl, 5, 3, 1, 1)

        self.onr2indNormSFSSAIDILbl = QLabel(self.onr2indNormWgt)
        self.onr2indNormSFSSAIDILbl.setObjectName(u"onr2indNormSFSSAIDILbl")
        self.onr2indNormSFSSAIDILbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2indNormGL.addWidget(self.onr2indNormSFSSAIDILbl, 5, 2, 1, 1)

        self.onr2indNormSFSTitleLbl = QLabel(self.onr2indNormWgt)
        self.onr2indNormSFSTitleLbl.setObjectName(u"onr2indNormSFSTitleLbl")
        self.onr2indNormSFSTitleLbl.setMinimumSize(QSize(0, 25))
        self.onr2indNormSFSTitleLbl.setMaximumSize(QSize(16777215, 20))
        self.onr2indNormSFSTitleLbl.setFont(font1)
        self.onr2indNormSFSTitleLbl.setStyleSheet(u"border-right: 1px solid rgb(255, 170, 0);")
        self.onr2indNormSFSTitleLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr2indNormSFSTitleLbl.setMargin(2)

        self.onr2indNormGL.addWidget(self.onr2indNormSFSTitleLbl, 5, 0, 1, 1)

        self.onr2indNormFNCTitleLbl = QLabel(self.onr2indNormWgt)
        self.onr2indNormFNCTitleLbl.setObjectName(u"onr2indNormFNCTitleLbl")
        self.onr2indNormFNCTitleLbl.setMinimumSize(QSize(0, 25))
        self.onr2indNormFNCTitleLbl.setMaximumSize(QSize(16777215, 20))
        self.onr2indNormFNCTitleLbl.setFont(font1)
        self.onr2indNormFNCTitleLbl.setStyleSheet(u"border-right: 1px solid rgb(255, 170, 0);")
        self.onr2indNormFNCTitleLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr2indNormFNCTitleLbl.setMargin(2)

        self.onr2indNormGL.addWidget(self.onr2indNormFNCTitleLbl, 4, 0, 1, 1)

        self.onr2indNormFNCSAIFILbl = QLabel(self.onr2indNormWgt)
        self.onr2indNormFNCSAIFILbl.setObjectName(u"onr2indNormFNCSAIFILbl")
        self.onr2indNormFNCSAIFILbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2indNormGL.addWidget(self.onr2indNormFNCSAIFILbl, 4, 3, 1, 1)

        self.onr2indNormFRGEENSLbl = QLabel(self.onr2indNormWgt)
        self.onr2indNormFRGEENSLbl.setObjectName(u"onr2indNormFRGEENSLbl")
        self.onr2indNormFRGEENSLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2indNormGL.addWidget(self.onr2indNormFRGEENSLbl, 2, 1, 1, 1)

        self.onr2indNormSpc = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.onr2indNormGL.addItem(self.onr2indNormSpc, 1, 4, 1, 1)

        self.onr2indNormFRGTitleLbl = QLabel(self.onr2indNormWgt)
        self.onr2indNormFRGTitleLbl.setObjectName(u"onr2indNormFRGTitleLbl")
        self.onr2indNormFRGTitleLbl.setMinimumSize(QSize(0, 25))
        self.onr2indNormFRGTitleLbl.setMaximumSize(QSize(16777215, 20))
        self.onr2indNormFRGTitleLbl.setFont(font1)
        self.onr2indNormFRGTitleLbl.setStyleSheet(u"border-right: 1px solid rgb(255, 170, 0);")
        self.onr2indNormFRGTitleLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr2indNormFRGTitleLbl.setMargin(2)

        self.onr2indNormGL.addWidget(self.onr2indNormFRGTitleLbl, 2, 0, 1, 1)

        self.onr2indNormNullLbl = QLabel(self.onr2indNormWgt)
        self.onr2indNormNullLbl.setObjectName(u"onr2indNormNullLbl")
        self.onr2indNormNullLbl.setMinimumSize(QSize(40, 20))
        self.onr2indNormNullLbl.setMaximumSize(QSize(40, 20))
        self.onr2indNormNullLbl.setFont(font1)
        self.onr2indNormNullLbl.setStyleSheet(u"border-bottom: 1px solid rgb(255, 170, 0);\n"
"border-right: 1px solid rgb(255, 170, 0);")
        self.onr2indNormNullLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr2indNormNullLbl.setMargin(5)

        self.onr2indNormGL.addWidget(self.onr2indNormNullLbl, 1, 0, 1, 1)


        self.onr2dxVBL.addWidget(self.onr2indNormWgt)

        self.onr2dx2Spc = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.onr2dxVBL.addItem(self.onr2dx2Spc)

        self.onr2fobLbl = QLabel(self.onr2dxWgt)
        self.onr2fobLbl.setObjectName(u"onr2fobLbl")
        self.onr2fobLbl.setMinimumSize(QSize(0, 30))
        self.onr2fobLbl.setMaximumSize(QSize(16777215, 30))
        self.onr2fobLbl.setSizeIncrement(QSize(0, 30))
        self.onr2fobLbl.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(255, 255, 255);")
        self.onr2fobLbl.setAlignment(Qt.AlignCenter)

        self.onr2dxVBL.addWidget(self.onr2fobLbl)

        self.onr2fobWgt = QWidget(self.onr2dxWgt)
        self.onr2fobWgt.setObjectName(u"onr2fobWgt")
        self.onr2fobGL = QGridLayout(self.onr2fobWgt)
        self.onr2fobGL.setSpacing(0)
        self.onr2fobGL.setObjectName(u"onr2fobGL")
        self.onr2fobFNCTitleLbl = QLabel(self.onr2fobWgt)
        self.onr2fobFNCTitleLbl.setObjectName(u"onr2fobFNCTitleLbl")
        self.onr2fobFNCTitleLbl.setMinimumSize(QSize(0, 25))
        self.onr2fobFNCTitleLbl.setMaximumSize(QSize(16777215, 20))
        self.onr2fobFNCTitleLbl.setFont(font1)
        self.onr2fobFNCTitleLbl.setStyleSheet(u"border-right: 1px solid rgb(255, 170, 0);")
        self.onr2fobFNCTitleLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr2fobFNCTitleLbl.setMargin(2)

        self.onr2fobGL.addWidget(self.onr2fobFNCTitleLbl, 3, 0, 1, 1)

        self.onr2fobFRGTitleLbl = QLabel(self.onr2fobWgt)
        self.onr2fobFRGTitleLbl.setObjectName(u"onr2fobFRGTitleLbl")
        self.onr2fobFRGTitleLbl.setMinimumSize(QSize(0, 25))
        self.onr2fobFRGTitleLbl.setMaximumSize(QSize(16777215, 20))
        self.onr2fobFRGTitleLbl.setFont(font1)
        self.onr2fobFRGTitleLbl.setStyleSheet(u"border-right: 1px solid rgb(255, 170, 0);")
        self.onr2fobFRGTitleLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr2fobFRGTitleLbl.setMargin(2)

        self.onr2fobGL.addWidget(self.onr2fobFRGTitleLbl, 2, 0, 1, 1)

        self.onr2fobFNCEENSLbl = QLabel(self.onr2fobWgt)
        self.onr2fobFNCEENSLbl.setObjectName(u"onr2fobFNCEENSLbl")
        self.onr2fobFNCEENSLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2fobGL.addWidget(self.onr2fobFNCEENSLbl, 3, 1, 1, 1)

        self.onr2fobSFSEENSLbl = QLabel(self.onr2fobWgt)
        self.onr2fobSFSEENSLbl.setObjectName(u"onr2fobSFSEENSLbl")
        self.onr2fobSFSEENSLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2fobGL.addWidget(self.onr2fobSFSEENSLbl, 4, 1, 1, 1)

        self.onr2fobNullLbl = QLabel(self.onr2fobWgt)
        self.onr2fobNullLbl.setObjectName(u"onr2fobNullLbl")
        self.onr2fobNullLbl.setMinimumSize(QSize(40, 20))
        self.onr2fobNullLbl.setMaximumSize(QSize(40, 20))
        self.onr2fobNullLbl.setFont(font1)
        self.onr2fobNullLbl.setStyleSheet(u"border-bottom: 1px solid rgb(255, 170, 0);\n"
"border-right: 1px solid rgb(255, 170, 0);")
        self.onr2fobNullLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr2fobNullLbl.setMargin(5)

        self.onr2fobGL.addWidget(self.onr2fobNullLbl, 1, 0, 1, 1)

        self.onr2fobSFSTitleLbl = QLabel(self.onr2fobWgt)
        self.onr2fobSFSTitleLbl.setObjectName(u"onr2fobSFSTitleLbl")
        self.onr2fobSFSTitleLbl.setMinimumSize(QSize(0, 25))
        self.onr2fobSFSTitleLbl.setMaximumSize(QSize(16777215, 20))
        self.onr2fobSFSTitleLbl.setFont(font1)
        self.onr2fobSFSTitleLbl.setStyleSheet(u"border-right: 1px solid rgb(255, 170, 0);")
        self.onr2fobSFSTitleLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr2fobSFSTitleLbl.setMargin(2)

        self.onr2fobGL.addWidget(self.onr2fobSFSTitleLbl, 4, 0, 1, 1)

        self.onr2fobTitleEENSLbl = QLabel(self.onr2fobWgt)
        self.onr2fobTitleEENSLbl.setObjectName(u"onr2fobTitleEENSLbl")
        self.onr2fobTitleEENSLbl.setMinimumSize(QSize(70, 0))
        self.onr2fobTitleEENSLbl.setFont(font1)
        self.onr2fobTitleEENSLbl.setStyleSheet(u"border-bottom: 1px solid rgb(255, 170, 0);")
        self.onr2fobTitleEENSLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr2fobTitleEENSLbl.setMargin(2)

        self.onr2fobGL.addWidget(self.onr2fobTitleEENSLbl, 1, 1, 1, 1)

        self.onr2fobSpc = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.onr2fobGL.addItem(self.onr2fobSpc, 1, 2, 1, 1)

        self.onr2fobFRGEENSLbl = QLabel(self.onr2fobWgt)
        self.onr2fobFRGEENSLbl.setObjectName(u"onr2fobFRGEENSLbl")
        self.onr2fobFRGEENSLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr2fobGL.addWidget(self.onr2fobFRGEENSLbl, 2, 1, 1, 1)


        self.onr2dxVBL.addWidget(self.onr2fobWgt)

        self.onr2dxBottomSpc = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.onr2dxVBL.addItem(self.onr2dxBottomSpc)


        self.onr2TabHBL.addWidget(self.onr2dxWgt)

        self.onrTabWgt.addTab(self.onr2TabWgt, "")
        self.onr3TabWgt = QWidget()
        self.onr3TabWgt.setObjectName(u"onr3TabWgt")
        self.onr3TabHBL = QHBoxLayout(self.onr3TabWgt)
        self.onr3TabHBL.setSpacing(0)
        self.onr3TabHBL.setObjectName(u"onr3TabHBL")
        self.onr3TabHBL.setContentsMargins(0, 0, 0, 0)
        self.onr3sxWgt = QWidget(self.onr3TabWgt)
        self.onr3sxWgt.setObjectName(u"onr3sxWgt")
        self.onr3sxVBL = QVBoxLayout(self.onr3sxWgt)
        self.onr3sxVBL.setSpacing(20)
        self.onr3sxVBL.setObjectName(u"onr3sxVBL")
        self.onr3sxVBL.setContentsMargins(10, 10, 10, 10)
        self.onr3sxTitleLbl = QLabel(self.onr3sxWgt)
        self.onr3sxTitleLbl.setObjectName(u"onr3sxTitleLbl")
        self.onr3sxTitleLbl.setMinimumSize(QSize(0, 30))
        self.onr3sxTitleLbl.setMaximumSize(QSize(16777215, 30))
        self.onr3sxTitleLbl.setSizeIncrement(QSize(0, 30))
        self.onr3sxTitleLbl.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-top: 1px solid rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(255, 255, 255);")
        self.onr3sxTitleLbl.setAlignment(Qt.AlignCenter)

        self.onr3sxVBL.addWidget(self.onr3sxTitleLbl)

        self.onr3Fig1Lbl = QLabel(self.onr3sxWgt)
        self.onr3Fig1Lbl.setObjectName(u"onr3Fig1Lbl")

        self.onr3sxVBL.addWidget(self.onr3Fig1Lbl)

        self.onr3Fig2Lbl = QLabel(self.onr3sxWgt)
        self.onr3Fig2Lbl.setObjectName(u"onr3Fig2Lbl")

        self.onr3sxVBL.addWidget(self.onr3Fig2Lbl)

        self.onr3sxSpc = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.onr3sxVBL.addItem(self.onr3sxSpc)


        self.onr3TabHBL.addWidget(self.onr3sxWgt)

        self.onr3dxWgt = QWidget(self.onr3TabWgt)
        self.onr3dxWgt.setObjectName(u"onr3dxWgt")
        self.onr3dxWgt.setMinimumSize(QSize(300, 0))
        self.onr3dxWgt.setMaximumSize(QSize(300, 16777215))
        self.onr3dxVBL = QVBoxLayout(self.onr3dxWgt)
        self.onr3dxVBL.setSpacing(20)
        self.onr3dxVBL.setObjectName(u"onr3dxVBL")
        self.onr3dxVBL.setContentsMargins(10, 10, 10, 10)
        self.onr3dxTopSpc = QSpacerItem(277, 27, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.onr3dxVBL.addItem(self.onr3dxTopSpc)

        self.onr3log1TB = QTextBrowser(self.onr3dxWgt)
        self.onr3log1TB.setObjectName(u"onr3log1TB")
        self.onr3log1TB.setMaximumSize(QSize(16777215, 200))

        self.onr3dxVBL.addWidget(self.onr3log1TB)

        self.onr3log2YB = QTextBrowser(self.onr3dxWgt)
        self.onr3log2YB.setObjectName(u"onr3log2YB")

        self.onr3dxVBL.addWidget(self.onr3log2YB)


        self.onr3TabHBL.addWidget(self.onr3dxWgt)

        self.onrTabWgt.addTab(self.onr3TabWgt, "")
        self.onr4TabWgt = QWidget()
        self.onr4TabWgt.setObjectName(u"onr4TabWgt")
        self.onr4TabHBL = QHBoxLayout(self.onr4TabWgt)
        self.onr4TabHBL.setObjectName(u"onr4TabHBL")
        self.onr4TabHBL.setContentsMargins(0, 0, 0, 0)
        self.onr4sxWgt = QWidget(self.onr4TabWgt)
        self.onr4sxWgt.setObjectName(u"onr4sxWgt")
        self.onr4sxVBL = QVBoxLayout(self.onr4sxWgt)
        self.onr4sxVBL.setSpacing(20)
        self.onr4sxVBL.setObjectName(u"onr4sxVBL")
        self.onr4sxVBL.setContentsMargins(10, 10, 10, 10)
        self.onr4sxTitleLbl = QLabel(self.onr4sxWgt)
        self.onr4sxTitleLbl.setObjectName(u"onr4sxTitleLbl")
        self.onr4sxTitleLbl.setMinimumSize(QSize(0, 30))
        self.onr4sxTitleLbl.setMaximumSize(QSize(16777215, 30))
        self.onr4sxTitleLbl.setSizeIncrement(QSize(0, 30))
        self.onr4sxTitleLbl.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-top: 1px solid rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(255, 255, 255);")
        self.onr4sxTitleLbl.setAlignment(Qt.AlignCenter)

        self.onr4sxVBL.addWidget(self.onr4sxTitleLbl)

        self.onr4Fig1Lbl = QLabel(self.onr4sxWgt)
        self.onr4Fig1Lbl.setObjectName(u"onr4Fig1Lbl")

        self.onr4sxVBL.addWidget(self.onr4Fig1Lbl)

        self.onr4Fig2Lbl = QLabel(self.onr4sxWgt)
        self.onr4Fig2Lbl.setObjectName(u"onr4Fig2Lbl")

        self.onr4sxVBL.addWidget(self.onr4Fig2Lbl)

        self.onr4logWgt = QWidget(self.onr4sxWgt)
        self.onr4logWgt.setObjectName(u"onr4logWgt")
        self.onr4logWgt.setMinimumSize(QSize(0, 100))
        self.onr4logGL = QGridLayout(self.onr4logWgt)
        self.onr4logGL.setObjectName(u"onr4logGL")
        self.onr4log1TB = QTextBrowser(self.onr4logWgt)
        self.onr4log1TB.setObjectName(u"onr4log1TB")
        self.onr4log1TB.setMaximumSize(QSize(16777215, 200))

        self.onr4logGL.addWidget(self.onr4log1TB, 1, 0, 1, 1)

        self.onr4log2TB = QTextBrowser(self.onr4logWgt)
        self.onr4log2TB.setObjectName(u"onr4log2TB")
        self.onr4log2TB.setMaximumSize(QSize(16777215, 200))

        self.onr4logGL.addWidget(self.onr4log2TB, 1, 1, 1, 1)

        self.onr4log1TitleLbl = QLabel(self.onr4logWgt)
        self.onr4log1TitleLbl.setObjectName(u"onr4log1TitleLbl")
        self.onr4log1TitleLbl.setMinimumSize(QSize(0, 30))
        self.onr4log1TitleLbl.setMaximumSize(QSize(16777215, 30))
        self.onr4log1TitleLbl.setSizeIncrement(QSize(0, 30))
        self.onr4log1TitleLbl.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(255, 255, 255);")
        self.onr4log1TitleLbl.setAlignment(Qt.AlignCenter)

        self.onr4logGL.addWidget(self.onr4log1TitleLbl, 0, 0, 1, 1)

        self.onr4log2TitleLbl = QLabel(self.onr4logWgt)
        self.onr4log2TitleLbl.setObjectName(u"onr4log2TitleLbl")
        self.onr4log2TitleLbl.setMinimumSize(QSize(0, 30))
        self.onr4log2TitleLbl.setMaximumSize(QSize(16777215, 30))
        self.onr4log2TitleLbl.setSizeIncrement(QSize(0, 30))
        self.onr4log2TitleLbl.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(255, 255, 255);")
        self.onr4log2TitleLbl.setAlignment(Qt.AlignCenter)

        self.onr4logGL.addWidget(self.onr4log2TitleLbl, 0, 1, 1, 1)


        self.onr4sxVBL.addWidget(self.onr4logWgt)

        self.onr4sxSpc = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.onr4sxVBL.addItem(self.onr4sxSpc)


        self.onr4TabHBL.addWidget(self.onr4sxWgt)

        self.onr4dxWgt = QWidget(self.onr4TabWgt)
        self.onr4dxWgt.setObjectName(u"onr4dxWgt")
        self.onr4dxWgt.setMinimumSize(QSize(300, 0))
        self.onr4dxWgt.setMaximumSize(QSize(300, 16777215))
        self.onr4dxWgt.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.onr4dxVBL = QVBoxLayout(self.onr4dxWgt)
        self.onr4dxVBL.setSpacing(20)
        self.onr4dxVBL.setObjectName(u"onr4dxVBL")
        self.onr4dxVBL.setContentsMargins(10, 10, 10, 10)
        self.onr4dxTopSpc = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.onr4dxVBL.addItem(self.onr4dxTopSpc)

        self.onr4indTitleLbl = QLabel(self.onr4dxWgt)
        self.onr4indTitleLbl.setObjectName(u"onr4indTitleLbl")
        self.onr4indTitleLbl.setMinimumSize(QSize(0, 30))
        self.onr4indTitleLbl.setMaximumSize(QSize(16777215, 30))
        self.onr4indTitleLbl.setSizeIncrement(QSize(0, 30))
        self.onr4indTitleLbl.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(255, 255, 255);")
        self.onr4indTitleLbl.setAlignment(Qt.AlignCenter)

        self.onr4dxVBL.addWidget(self.onr4indTitleLbl)

        self.onr4indFigLbl = QLabel(self.onr4dxWgt)
        self.onr4indFigLbl.setObjectName(u"onr4indFigLbl")

        self.onr4dxVBL.addWidget(self.onr4indFigLbl)

        self.onrdxSpc = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.onr4dxVBL.addItem(self.onrdxSpc)

        self.onr4indWgt = QWidget(self.onr4dxWgt)
        self.onr4indWgt.setObjectName(u"onr4indWgt")
        self.onr4indGL = QGridLayout(self.onr4indWgt)
        self.onr4indGL.setSpacing(0)
        self.onr4indGL.setObjectName(u"onr4indGL")
        self.onr4indSAIDItitleLbl = QLabel(self.onr4indWgt)
        self.onr4indSAIDItitleLbl.setObjectName(u"onr4indSAIDItitleLbl")
        self.onr4indSAIDItitleLbl.setMinimumSize(QSize(0, 25))
        self.onr4indSAIDItitleLbl.setMaximumSize(QSize(16777215, 20))
        self.onr4indSAIDItitleLbl.setFont(font1)
        self.onr4indSAIDItitleLbl.setStyleSheet(u"border-right: 1px solid rgb(255, 170, 0);")
        self.onr4indSAIDItitleLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr4indSAIDItitleLbl.setMargin(2)

        self.onr4indGL.addWidget(self.onr4indSAIDItitleLbl, 4, 0, 1, 1)

        self.onr4indSAIFIpreLbl = QLabel(self.onr4indWgt)
        self.onr4indSAIFIpreLbl.setObjectName(u"onr4indSAIFIpreLbl")
        self.onr4indSAIFIpreLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr4indGL.addWidget(self.onr4indSAIFIpreLbl, 5, 1, 1, 1)

        self.onr4indFOBpreLbl = QLabel(self.onr4indWgt)
        self.onr4indFOBpreLbl.setObjectName(u"onr4indFOBpreLbl")
        self.onr4indFOBpreLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr4indGL.addWidget(self.onr4indFOBpreLbl, 6, 1, 1, 1)

        self.onr4indSAIFIpostLBL = QLabel(self.onr4indWgt)
        self.onr4indSAIFIpostLBL.setObjectName(u"onr4indSAIFIpostLBL")
        self.onr4indSAIFIpostLBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr4indGL.addWidget(self.onr4indSAIFIpostLBL, 5, 2, 1, 1)

        self.onr4indSAIDIpreLbl = QLabel(self.onr4indWgt)
        self.onr4indSAIDIpreLbl.setObjectName(u"onr4indSAIDIpreLbl")
        self.onr4indSAIDIpreLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr4indGL.addWidget(self.onr4indSAIDIpreLbl, 4, 1, 1, 1)

        self.onr4indFOBpostLbl = QLabel(self.onr4indWgt)
        self.onr4indFOBpostLbl.setObjectName(u"onr4indFOBpostLbl")
        self.onr4indFOBpostLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr4indGL.addWidget(self.onr4indFOBpostLbl, 6, 2, 1, 1)

        self.onr4indSpc = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.onr4indGL.addItem(self.onr4indSpc, 1, 3, 1, 1)

        self.onr4indEENSpostLbl = QLabel(self.onr4indWgt)
        self.onr4indEENSpostLbl.setObjectName(u"onr4indEENSpostLbl")
        self.onr4indEENSpostLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr4indGL.addWidget(self.onr4indEENSpostLbl, 2, 2, 1, 1)

        self.onr4indSAIDIpostLbl = QLabel(self.onr4indWgt)
        self.onr4indSAIDIpostLbl.setObjectName(u"onr4indSAIDIpostLbl")
        self.onr4indSAIDIpostLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr4indGL.addWidget(self.onr4indSAIDIpostLbl, 4, 2, 1, 1)

        self.onr4indNullLbl = QLabel(self.onr4indWgt)
        self.onr4indNullLbl.setObjectName(u"onr4indNullLbl")
        self.onr4indNullLbl.setMinimumSize(QSize(40, 20))
        self.onr4indNullLbl.setMaximumSize(QSize(40, 20))
        self.onr4indNullLbl.setFont(font1)
        self.onr4indNullLbl.setStyleSheet(u"border-bottom: 1px solid rgb(255, 170, 0);\n"
"border-right: 1px solid rgb(255, 170, 0);")
        self.onr4indNullLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr4indNullLbl.setMargin(5)

        self.onr4indGL.addWidget(self.onr4indNullLbl, 1, 0, 1, 1)

        self.onr4indTitlePreLbl = QLabel(self.onr4indWgt)
        self.onr4indTitlePreLbl.setObjectName(u"onr4indTitlePreLbl")
        self.onr4indTitlePreLbl.setMinimumSize(QSize(100, 0))
        self.onr4indTitlePreLbl.setFont(font1)
        self.onr4indTitlePreLbl.setStyleSheet(u"border-bottom: 1px solid rgb(255, 170, 0);")
        self.onr4indTitlePreLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr4indTitlePreLbl.setMargin(2)

        self.onr4indGL.addWidget(self.onr4indTitlePreLbl, 1, 1, 1, 1)

        self.onr4indFOBtitleLBL = QLabel(self.onr4indWgt)
        self.onr4indFOBtitleLBL.setObjectName(u"onr4indFOBtitleLBL")
        self.onr4indFOBtitleLBL.setMinimumSize(QSize(0, 25))
        self.onr4indFOBtitleLBL.setMaximumSize(QSize(16777215, 20))
        self.onr4indFOBtitleLBL.setFont(font1)
        self.onr4indFOBtitleLBL.setStyleSheet(u"border-right: 1px solid rgb(255, 170, 0);")
        self.onr4indFOBtitleLBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr4indFOBtitleLBL.setMargin(2)

        self.onr4indGL.addWidget(self.onr4indFOBtitleLBL, 6, 0, 1, 1)

        self.onr4indEENStitleLbl = QLabel(self.onr4indWgt)
        self.onr4indEENStitleLbl.setObjectName(u"onr4indEENStitleLbl")
        self.onr4indEENStitleLbl.setMinimumSize(QSize(0, 25))
        self.onr4indEENStitleLbl.setMaximumSize(QSize(16777215, 20))
        self.onr4indEENStitleLbl.setFont(font1)
        self.onr4indEENStitleLbl.setStyleSheet(u"border-right: 1px solid rgb(255, 170, 0);")
        self.onr4indEENStitleLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr4indEENStitleLbl.setMargin(2)

        self.onr4indGL.addWidget(self.onr4indEENStitleLbl, 2, 0, 1, 1)

        self.onr4indEENSpreLbl = QLabel(self.onr4indWgt)
        self.onr4indEENSpreLbl.setObjectName(u"onr4indEENSpreLbl")
        self.onr4indEENSpreLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.onr4indGL.addWidget(self.onr4indEENSpreLbl, 2, 1, 1, 1)

        self.onr4indSAIFItitleLbl = QLabel(self.onr4indWgt)
        self.onr4indSAIFItitleLbl.setObjectName(u"onr4indSAIFItitleLbl")
        self.onr4indSAIFItitleLbl.setMinimumSize(QSize(0, 25))
        self.onr4indSAIFItitleLbl.setMaximumSize(QSize(16777215, 20))
        self.onr4indSAIFItitleLbl.setFont(font1)
        self.onr4indSAIFItitleLbl.setStyleSheet(u"border-right: 1px solid rgb(255, 170, 0);")
        self.onr4indSAIFItitleLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr4indSAIFItitleLbl.setMargin(2)

        self.onr4indGL.addWidget(self.onr4indSAIFItitleLbl, 5, 0, 1, 1)

        self.onr4indTitlePostLbl = QLabel(self.onr4indWgt)
        self.onr4indTitlePostLbl.setObjectName(u"onr4indTitlePostLbl")
        self.onr4indTitlePostLbl.setMinimumSize(QSize(100, 0))
        self.onr4indTitlePostLbl.setFont(font1)
        self.onr4indTitlePostLbl.setStyleSheet(u"border-bottom: 1px solid rgb(255, 170, 0);")
        self.onr4indTitlePostLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.onr4indTitlePostLbl.setMargin(2)

        self.onr4indGL.addWidget(self.onr4indTitlePostLbl, 1, 2, 1, 1)


        self.onr4dxVBL.addWidget(self.onr4indWgt)

        self.onr4dxBottomSpc = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.onr4dxVBL.addItem(self.onr4dxBottomSpc)


        self.onr4TabHBL.addWidget(self.onr4dxWgt)

        self.onrTabWgt.addTab(self.onr4TabWgt, "")
        self.onr5TabWgt = QWidget()
        self.onr5TabWgt.setObjectName(u"onr5TabWgt")
        self.onr5TabHBL = QHBoxLayout(self.onr5TabWgt)
        self.onr5TabHBL.setSpacing(0)
        self.onr5TabHBL.setObjectName(u"onr5TabHBL")
        self.onr5TabHBL.setContentsMargins(0, 0, 0, 0)
        self.onr5sxWgt = QWidget(self.onr5TabWgt)
        self.onr5sxWgt.setObjectName(u"onr5sxWgt")
        self.onr4sxVBL_2 = QVBoxLayout(self.onr5sxWgt)
        self.onr4sxVBL_2.setSpacing(20)
        self.onr4sxVBL_2.setObjectName(u"onr4sxVBL_2")
        self.onr4sxVBL_2.setContentsMargins(10, 10, 10, 10)
        self.onr4sxTitleLbl_2 = QLabel(self.onr5sxWgt)
        self.onr4sxTitleLbl_2.setObjectName(u"onr4sxTitleLbl_2")
        self.onr4sxTitleLbl_2.setMinimumSize(QSize(0, 30))
        self.onr4sxTitleLbl_2.setMaximumSize(QSize(16777215, 30))
        self.onr4sxTitleLbl_2.setSizeIncrement(QSize(0, 30))
        self.onr4sxTitleLbl_2.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-top: 1px solid rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(255, 255, 255);")
        self.onr4sxTitleLbl_2.setAlignment(Qt.AlignCenter)

        self.onr4sxVBL_2.addWidget(self.onr4sxTitleLbl_2)

        self.onr5Fig1Lbl = QLabel(self.onr5sxWgt)
        self.onr5Fig1Lbl.setObjectName(u"onr5Fig1Lbl")

        self.onr4sxVBL_2.addWidget(self.onr5Fig1Lbl)

        self.onr5FigWgt = QWidget(self.onr5sxWgt)
        self.onr5FigWgt.setObjectName(u"onr5FigWgt")
        self.onr5FigWgt.setMinimumSize(QSize(0, 100))
        self.onr5FigGL = QGridLayout(self.onr5FigWgt)
        self.onr5FigGL.setObjectName(u"onr5FigGL")
        self.onr4log1TitleLbl_2 = QLabel(self.onr5FigWgt)
        self.onr4log1TitleLbl_2.setObjectName(u"onr4log1TitleLbl_2")
        self.onr4log1TitleLbl_2.setMinimumSize(QSize(0, 30))
        self.onr4log1TitleLbl_2.setMaximumSize(QSize(16777215, 30))
        self.onr4log1TitleLbl_2.setSizeIncrement(QSize(0, 30))
        self.onr4log1TitleLbl_2.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(255, 255, 255);")
        self.onr4log1TitleLbl_2.setAlignment(Qt.AlignCenter)

        self.onr5FigGL.addWidget(self.onr4log1TitleLbl_2, 0, 0, 1, 1)

        self.onr4log2TitleLbl_2 = QLabel(self.onr5FigWgt)
        self.onr4log2TitleLbl_2.setObjectName(u"onr4log2TitleLbl_2")
        self.onr4log2TitleLbl_2.setMinimumSize(QSize(0, 30))
        self.onr4log2TitleLbl_2.setMaximumSize(QSize(16777215, 30))
        self.onr4log2TitleLbl_2.setSizeIncrement(QSize(0, 30))
        self.onr4log2TitleLbl_2.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(255, 255, 255);")
        self.onr4log2TitleLbl_2.setAlignment(Qt.AlignCenter)

        self.onr5FigGL.addWidget(self.onr4log2TitleLbl_2, 0, 1, 1, 1)

        self.onr5Fig2Lbl = QLabel(self.onr5FigWgt)
        self.onr5Fig2Lbl.setObjectName(u"onr5Fig2Lbl")

        self.onr5FigGL.addWidget(self.onr5Fig2Lbl, 1, 0, 1, 1)

        self.onr5Fig3Lbl = QLabel(self.onr5FigWgt)
        self.onr5Fig3Lbl.setObjectName(u"onr5Fig3Lbl")

        self.onr5FigGL.addWidget(self.onr5Fig3Lbl, 1, 1, 1, 1)


        self.onr4sxVBL_2.addWidget(self.onr5FigWgt)

        self.onr4sxSpc_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.onr4sxVBL_2.addItem(self.onr4sxSpc_2)


        self.onr5TabHBL.addWidget(self.onr5sxWgt)

        self.onr5dxWgt = QWidget(self.onr5TabWgt)
        self.onr5dxWgt.setObjectName(u"onr5dxWgt")
        self.onr5dxWgt.setMinimumSize(QSize(300, 0))
        self.onr5dxWgt.setMaximumSize(QSize(300, 16777215))
        self.onr5dxWgt.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.onr4dxVBL_2 = QVBoxLayout(self.onr5dxWgt)
        self.onr4dxVBL_2.setSpacing(20)
        self.onr4dxVBL_2.setObjectName(u"onr4dxVBL_2")
        self.onr4dxVBL_2.setContentsMargins(10, 10, 10, 10)
        self.onr5dxTopSpc = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.onr4dxVBL_2.addItem(self.onr5dxTopSpc)

        self.onr5logTitleLbl = QLabel(self.onr5dxWgt)
        self.onr5logTitleLbl.setObjectName(u"onr5logTitleLbl")
        self.onr5logTitleLbl.setMinimumSize(QSize(0, 30))
        self.onr5logTitleLbl.setMaximumSize(QSize(16777215, 30))
        self.onr5logTitleLbl.setSizeIncrement(QSize(0, 30))
        self.onr5logTitleLbl.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(255, 255, 255);")
        self.onr5logTitleLbl.setAlignment(Qt.AlignCenter)

        self.onr4dxVBL_2.addWidget(self.onr5logTitleLbl)

        self.onr5log2TB = QTextBrowser(self.onr5dxWgt)
        self.onr5log2TB.setObjectName(u"onr5log2TB")
        self.onr5log2TB.setMaximumSize(QSize(16777215, 16777215))

        self.onr4dxVBL_2.addWidget(self.onr5log2TB)


        self.onr5TabHBL.addWidget(self.onr5dxWgt)

        self.onrTabWgt.addTab(self.onr5TabWgt, "")

        self.onrMainVBL.addWidget(self.onrTabWgt)


        self.retranslateUi(Form)

        self.onrTabWgt.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.onrTitleLbl.setText(QCoreApplication.translate("Form", u"Optimal Network Reconfiguration", None))
        self.onr1sxTitleLbl.setText(QCoreApplication.translate("Form", u"Grafo Nodale Zonale", None))
        self.onr1sxFigLbl.setText(QCoreApplication.translate("Form", u"img1", None))
        self.onr1logLbl.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.onr1dxTitleLbl.setText(QCoreApplication.translate("Form", u"Grafo Nodale Radiale", None))
        self.onr1dxFigLbl.setText(QCoreApplication.translate("Form", u"img1", None))
        self.indexCalcPb.setText(QCoreApplication.translate("Form", u"Calcolo Indici di Qualit\u00e0", None))
        self.onrTabWgt.setTabText(self.onrTabWgt.indexOf(self.onr1TabWgt), QCoreApplication.translate("Form", u"Grafi pre-ONR", None))
        self.onr2sxTitleLbl.setText(QCoreApplication.translate("Form", u"Indici affidabilistici topologia iniziale radiale", None))
        self.onr2Fig1Lbl.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.onr2Fig2Lbl.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.onr2Fig3Lbl.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.onr2Fig4Lbl.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.onr2calcLbl.setText(QCoreApplication.translate("Form", u"Scegli llogica di automazione", None))
        self.onr2calcCB.setItemText(0, QCoreApplication.translate("Form", u"FRG", None))
        self.onr2calcCB.setItemText(1, QCoreApplication.translate("Form", u"FNC", None))
        self.onr2calcCB.setItemText(2, QCoreApplication.translate("Form", u"SFS", None))

        self.onr2calcBtn.setText(QCoreApplication.translate("Form", u"Calcolo Indici di Qualit\u00e0", None))
        self.onr2indTitleLbl.setText(QCoreApplication.translate("Form", u"Indici di Affidabilit\u00e0 allo stato iniziale", None))
        self.onr2indFRGSAIFILbl.setText(QCoreApplication.translate("Form", u"3.5784", None))
        self.onr2indTitleEENSLbl.setText(QCoreApplication.translate("Form", u"EENS", None))
        self.onr2indNullLbl.setText("")
        self.onr2indFRGSAIDILbl.setText(QCoreApplication.translate("Form", u"6.4346", None))
        self.onr2indTitleSAIFILbl.setText(QCoreApplication.translate("Form", u"SAIFI", None))
        self.onr2indTitleSAIDILbl.setText(QCoreApplication.translate("Form", u"SAIDI", None))
        self.onr2indFNCEENSLbl.setText(QCoreApplication.translate("Form", u"70361.6025", None))
        self.onr2indSFSEENSLbl.setText(QCoreApplication.translate("Form", u"70361.6025", None))
        self.onr2indFNCSAIDILbl.setText(QCoreApplication.translate("Form", u"6.4346", None))
        self.onr2indSFSSAIFILbl.setText(QCoreApplication.translate("Form", u"70361.6025", None))
        self.onr2indSFSSAIDILbl.setText(QCoreApplication.translate("Form", u"6.4346", None))
        self.onr2indFRGTitleLbl.setText(QCoreApplication.translate("Form", u"FRG ", None))
        self.onr2indSFSTitleLbl.setText(QCoreApplication.translate("Form", u"SFS ", None))
        self.onr2indFNCTitleLbl.setText(QCoreApplication.translate("Form", u"FNC ", None))
        self.onr2indFNCSAIFILbl.setText(QCoreApplication.translate("Form", u"70361.6025", None))
        self.onr2indFRGEENSLbl.setText(QCoreApplication.translate("Form", u"70361.6025", None))
        self.onr2indNormTitleLbl.setText(QCoreApplication.translate("Form", u"Indici di Affidabilit\u00e0 normalizzati allo stato iniziale", None))
        self.onr2indNormFRGSAIFILbl.setText(QCoreApplication.translate("Form", u"3.5784", None))
        self.onr2indNormTitleEENSLbl.setText(QCoreApplication.translate("Form", u"EENS", None))
        self.onr2indNormFRGSAIDILbl.setText(QCoreApplication.translate("Form", u"6.4346", None))
        self.onr2indNormTitleSAIFILbl.setText(QCoreApplication.translate("Form", u"SAIFI", None))
        self.onr2indNormTitleSAIDILbl.setText(QCoreApplication.translate("Form", u"SAIDI", None))
        self.onr2indNormFNCEENSLbl.setText(QCoreApplication.translate("Form", u"70361.6025", None))
        self.onr2indNormSFSEENSLbl.setText(QCoreApplication.translate("Form", u"70361.6025", None))
        self.onr2indNormFNCSAIDILbl.setText(QCoreApplication.translate("Form", u"6.4346", None))
        self.onr2indNormSFSSAIFILbl.setText(QCoreApplication.translate("Form", u"70361.6025", None))
        self.onr2indNormSFSSAIDILbl.setText(QCoreApplication.translate("Form", u"6.4346", None))
        self.onr2indNormSFSTitleLbl.setText(QCoreApplication.translate("Form", u"SFS ", None))
        self.onr2indNormFNCTitleLbl.setText(QCoreApplication.translate("Form", u"FNC ", None))
        self.onr2indNormFNCSAIFILbl.setText(QCoreApplication.translate("Form", u"70361.6025", None))
        self.onr2indNormFRGEENSLbl.setText(QCoreApplication.translate("Form", u"70361.6025", None))
        self.onr2indNormFRGTitleLbl.setText(QCoreApplication.translate("Form", u"FRG ", None))
        self.onr2indNormNullLbl.setText("")
        self.onr2fobLbl.setText(QCoreApplication.translate("Form", u"Funzione obiettivo allo stato iniziale", None))
        self.onr2fobFNCTitleLbl.setText(QCoreApplication.translate("Form", u"FNC ", None))
        self.onr2fobFRGTitleLbl.setText(QCoreApplication.translate("Form", u"FRG ", None))
        self.onr2fobFNCEENSLbl.setText(QCoreApplication.translate("Form", u"70361.6025", None))
        self.onr2fobSFSEENSLbl.setText(QCoreApplication.translate("Form", u"70361.6025", None))
        self.onr2fobNullLbl.setText("")
        self.onr2fobSFSTitleLbl.setText(QCoreApplication.translate("Form", u"SFS ", None))
        self.onr2fobTitleEENSLbl.setText(QCoreApplication.translate("Form", u"f. Obiettivo", None))
        self.onr2fobFRGEENSLbl.setText(QCoreApplication.translate("Form", u"70361.6025", None))
        self.onrTabWgt.setTabText(self.onrTabWgt.indexOf(self.onr2TabWgt), QCoreApplication.translate("Form", u"Indici pre-ONR", None))
        self.onr3sxTitleLbl.setText(QCoreApplication.translate("Form", u"Violazioni su nodi e linee", None))
        self.onr3Fig1Lbl.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.onr3Fig2Lbl.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.onr3log1TB.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze ("
                        "ACLF) con la topologia iniziale:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right"
                        ":0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bot"
                        "tom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.onr3log2YB.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Violazione di tensione sul nodo n0123456789122335 - Vi = 1.1445 p.u.</p></body></html>", None))
        self.onrTabWgt.setTabText(self.onrTabWgt.indexOf(self.onr3TabWgt), QCoreApplication.translate("Form", u"Violazioni pre-ONR", None))
        self.onr4sxTitleLbl.setText(QCoreApplication.translate("Form", u"Risultati ONR", None))
        self.onr4Fig1Lbl.setText(QCoreApplication.translate("Form", u"Grafo zonale pre", None))
        self.onr4Fig2Lbl.setText(QCoreApplication.translate("Form", u"Grafo zonale post", None))
        self.onr4log1TB.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze ("
                        "ACLF) con la topologia iniziale:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right"
                        ":0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bot"
                        "tom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.onr4log2TB.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze ("
                        "ACLF) con la topologia iniziale:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right"
                        ":0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bot"
                        "tom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.onr4log1TitleLbl.setText(QCoreApplication.translate("Form", u"LOG Solver", None))
        self.onr4log2TitleLbl.setText(QCoreApplication.translate("Form", u"LOG Switch", None))
        self.onr4indTitleLbl.setText(QCoreApplication.translate("Form", u"Indici di Affidabilit\u00e0 ", None))
        self.onr4indFigLbl.setText(QCoreApplication.translate("Form", u"Figura Indici", None))
        self.onr4indSAIDItitleLbl.setText(QCoreApplication.translate("Form", u"SAIDI ", None))
        self.onr4indSAIFIpreLbl.setText(QCoreApplication.translate("Form", u"70361.6025", None))
        self.onr4indFOBpreLbl.setText(QCoreApplication.translate("Form", u"70361.6025", None))
        self.onr4indSAIFIpostLBL.setText(QCoreApplication.translate("Form", u"70361.6025", None))
        self.onr4indSAIDIpreLbl.setText(QCoreApplication.translate("Form", u"70361.6025", None))
        self.onr4indFOBpostLbl.setText(QCoreApplication.translate("Form", u"70361.6025", None))
        self.onr4indEENSpostLbl.setText(QCoreApplication.translate("Form", u"6.4346", None))
        self.onr4indSAIDIpostLbl.setText(QCoreApplication.translate("Form", u"6.4346", None))
        self.onr4indNullLbl.setText("")
        self.onr4indTitlePreLbl.setText(QCoreApplication.translate("Form", u"Pre-ONR", None))
        self.onr4indFOBtitleLBL.setText(QCoreApplication.translate("Form", u"f. Ob. ", None))
        self.onr4indEENStitleLbl.setText(QCoreApplication.translate("Form", u"EENS ", None))
        self.onr4indEENSpreLbl.setText(QCoreApplication.translate("Form", u"70361.6025", None))
        self.onr4indSAIFItitleLbl.setText(QCoreApplication.translate("Form", u"SAIFI ", None))
        self.onr4indTitlePostLbl.setText(QCoreApplication.translate("Form", u"Post-ONR", None))
        self.onrTabWgt.setTabText(self.onrTabWgt.indexOf(self.onr4TabWgt), QCoreApplication.translate("Form", u"Risultati ONR (1)", None))
        self.onr4sxTitleLbl_2.setText(QCoreApplication.translate("Form", u"Risultati ONR", None))
        self.onr5Fig1Lbl.setText(QCoreApplication.translate("Form", u"Output grafici tensioni", None))
        self.onr4log1TitleLbl_2.setText(QCoreApplication.translate("Form", u"Sovraccarico linee pre-ONR", None))
        self.onr4log2TitleLbl_2.setText(QCoreApplication.translate("Form", u"Sovraccarico linee post-ONR", None))
        self.onr5Fig2Lbl.setText(QCoreApplication.translate("Form", u"Output grafici tensioni", None))
        self.onr5Fig3Lbl.setText(QCoreApplication.translate("Form", u"Output grafici tensioni", None))
        self.onr5logTitleLbl.setText(QCoreApplication.translate("Form", u"Log", None))
        self.onr5log2TB.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze ("
                        "ACLF) con la topologia iniziale:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right"
                        ":0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid Power: P = 10314.0 kW  |  Q = -234.8 KVar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analisi delle potenze (ACLF) con la topologia iniziale:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bot"
                        "tom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.onrTabWgt.setTabText(self.onrTabWgt.indexOf(self.onr5TabWgt), QCoreApplication.translate("Form", u"Risultati ONR (2)", None))
    # retranslateUi

