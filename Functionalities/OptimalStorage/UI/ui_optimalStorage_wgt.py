# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'optimalStorage_wgtjmMJix.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1771, 1158)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.optStorWgt = QWidget(self.centralwidget)
        self.optStorWgt.setObjectName(u"optStorWgt")
        self.optStorWgt.setGeometry(QRect(40, 0, 1421, 1116))
        self.optStorWgt.setStyleSheet(u"")
        self.optStorHL = QHBoxLayout(self.optStorWgt)
        self.optStorHL.setObjectName(u"optStorHL")
        self.leftWgt = QWidget(self.optStorWgt)
        self.leftWgt.setObjectName(u"leftWgt")
        self.leftWgt.setMaximumSize(QSize(450, 16777215))
        self.leftWgt.setStyleSheet(u"*{}\n"
"\n"
"QWidget{\n"
"	border-radius: 10px\n"
"}\n"
"\n"
"QPushButton{\n"
"	font: 12px;\n"
"	text-align: center;\n"
"	padding: 5px 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(31, 31, 31); border: solid;\n"
"	border-width: 2px; border-radius: 15px; border-color: rgb(127, 127, 127)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(64, 64, 64); border-style: inset\n"
"}\n"
"")
        self.leftVL = QVBoxLayout(self.leftWgt)
        self.leftVL.setObjectName(u"leftVL")
        self.inputLbl = QLabel(self.leftWgt)
        self.inputLbl.setObjectName(u"inputLbl")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.inputLbl.setFont(font)
        self.inputLbl.setAlignment(Qt.AlignCenter)

        self.leftVL.addWidget(self.inputLbl)

        self.inputWgt = QWidget(self.leftWgt)
        self.inputWgt.setObjectName(u"inputWgt")
        self.inputWgt.setStyleSheet(u"*{\n"
"	background-color: rgb(31, 0, 0);\n"
"}\n"
"\n"
"QDoubleSpinBox{\n"
"	color: rgb(0, 0, 0);\n"
"	border: solid;\n"
"	border-radius: 0px;\n"
"	border-width: 1px;\n"
"	boder-color: rgb(127, 127, 127);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.inputGL = QGridLayout(self.inputWgt)
        self.inputGL.setObjectName(u"inputGL")
        self.inputGL.setHorizontalSpacing(20)
        self.inputGL.setVerticalSpacing(10)
        self.solarFerInputDsb = QDoubleSpinBox(self.inputWgt)
        self.solarFerInputDsb.setObjectName(u"solarFerInputDsb")
        self.solarFerInputDsb.setMinimumSize(QSize(70, 0))
        self.solarFerInputDsb.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        self.solarFerInputDsb.setFont(font1)
        self.solarFerInputDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.solarFerInputDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.solarFerInputDsb.setMaximum(100.000000000000000)
        self.solarFerInputDsb.setSingleStep(0.100000000000000)
        self.solarFerInputDsb.setValue(70.000000000000000)

        self.inputGL.addWidget(self.solarFerInputDsb, 4, 1, 1, 1)

        self.h2ConsInputDsb = QDoubleSpinBox(self.inputWgt)
        self.h2ConsInputDsb.setObjectName(u"h2ConsInputDsb")
        self.h2ConsInputDsb.setMinimumSize(QSize(70, 0))
        self.h2ConsInputDsb.setMaximumSize(QSize(16777215, 16777215))
        self.h2ConsInputDsb.setFont(font1)
        self.h2ConsInputDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.h2ConsInputDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.h2ConsInputDsb.setMaximum(100.000000000000000)
        self.h2ConsInputDsb.setSingleStep(0.100000000000000)
        self.h2ConsInputDsb.setValue(1.200000000000000)

        self.inputGL.addWidget(self.h2ConsInputDsb, 5, 1, 1, 1)

        self.ferGenInputDsb = QDoubleSpinBox(self.inputWgt)
        self.ferGenInputDsb.setObjectName(u"ferGenInputDsb")
        self.ferGenInputDsb.setMinimumSize(QSize(70, 0))
        self.ferGenInputDsb.setMaximumSize(QSize(16777215, 16777215))
        self.ferGenInputDsb.setFont(font1)
        self.ferGenInputDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ferGenInputDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ferGenInputDsb.setMaximum(100.000000000000000)
        self.ferGenInputDsb.setSingleStep(0.100000000000000)
        self.ferGenInputDsb.setValue(65.000000000000000)

        self.inputGL.addWidget(self.ferGenInputDsb, 3, 1, 1, 1)

        self.solarFerLbl = QLabel(self.inputWgt)
        self.solarFerLbl.setObjectName(u"solarFerLbl")
        font2 = QFont()
        font2.setPointSize(9)
        self.solarFerLbl.setFont(font2)
        self.solarFerLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.inputGL.addWidget(self.solarFerLbl, 4, 0, 1, 1)

        self.ferGenInputLbl = QLabel(self.inputWgt)
        self.ferGenInputLbl.setObjectName(u"ferGenInputLbl")
        self.ferGenInputLbl.setFont(font2)
        self.ferGenInputLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.inputGL.addWidget(self.ferGenInputLbl, 3, 0, 1, 1)

        self.enConsGrowInputDsb = QDoubleSpinBox(self.inputWgt)
        self.enConsGrowInputDsb.setObjectName(u"enConsGrowInputDsb")
        self.enConsGrowInputDsb.setMinimumSize(QSize(70, 0))
        self.enConsGrowInputDsb.setMaximumSize(QSize(16777215, 16777215))
        self.enConsGrowInputDsb.setFont(font1)
        self.enConsGrowInputDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.enConsGrowInputDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.enConsGrowInputDsb.setMaximum(100.000000000000000)
        self.enConsGrowInputDsb.setSingleStep(0.100000000000000)
        self.enConsGrowInputDsb.setValue(2.000000000000000)

        self.inputGL.addWidget(self.enConsGrowInputDsb, 2, 1, 1, 1)

        self.electrLevInputDsb = QDoubleSpinBox(self.inputWgt)
        self.electrLevInputDsb.setObjectName(u"electrLevInputDsb")
        self.electrLevInputDsb.setMinimumSize(QSize(70, 0))
        self.electrLevInputDsb.setMaximumSize(QSize(16777215, 16777215))
        self.electrLevInputDsb.setFont(font1)
        self.electrLevInputDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.electrLevInputDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.electrLevInputDsb.setMaximum(100.000000000000000)
        self.electrLevInputDsb.setSingleStep(0.100000000000000)
        self.electrLevInputDsb.setValue(28.000000000000000)

        self.inputGL.addWidget(self.electrLevInputDsb, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.inputGL.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.electrLevInputLbl = QLabel(self.inputWgt)
        self.electrLevInputLbl.setObjectName(u"electrLevInputLbl")
        self.electrLevInputLbl.setFont(font2)
        self.electrLevInputLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.inputGL.addWidget(self.electrLevInputLbl, 0, 0, 1, 1)

        self.enConsGrowInputLbl = QLabel(self.inputWgt)
        self.enConsGrowInputLbl.setObjectName(u"enConsGrowInputLbl")
        self.enConsGrowInputLbl.setFont(font2)
        self.enConsGrowInputLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.inputGL.addWidget(self.enConsGrowInputLbl, 2, 0, 1, 1)

        self.h2ConsInputLbl = QLabel(self.inputWgt)
        self.h2ConsInputLbl.setObjectName(u"h2ConsInputLbl")
        self.h2ConsInputLbl.setFont(font2)
        self.h2ConsInputLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.inputGL.addWidget(self.h2ConsInputLbl, 5, 0, 1, 1)


        self.leftVL.addWidget(self.inputWgt)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.leftVL.addItem(self.verticalSpacer_2)

        self.scenTitleLbl = QLabel(self.leftWgt)
        self.scenTitleLbl.setObjectName(u"scenTitleLbl")
        self.scenTitleLbl.setFont(font)
        self.scenTitleLbl.setAlignment(Qt.AlignCenter)

        self.leftVL.addWidget(self.scenTitleLbl)

        self.scenWgt = QFrame(self.leftWgt)
        self.scenWgt.setObjectName(u"scenWgt")
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.scenWgt.setFont(font3)
        self.scenWgt.setLayoutDirection(Qt.LeftToRight)
        self.scenWgt.setStyleSheet(u"*{\n"
"	background-color: rgb(47, 0, 0);\n"
"}\n"
"\n"
"QComboBox{\n"
"	text-align: right;\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLabel{\n"
"	text-align: left;\n"
"}")
        self.scenWgt.setFrameShape(QFrame.StyledPanel)
        self.scenWgt.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.scenWgt)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(10)
        self.co2EmisScenDsb = QDoubleSpinBox(self.scenWgt)
        self.co2EmisScenDsb.setObjectName(u"co2EmisScenDsb")
        self.co2EmisScenDsb.setMinimumSize(QSize(70, 0))
        self.co2EmisScenDsb.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.co2EmisScenDsb.setFont(font4)
        self.co2EmisScenDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.co2EmisScenDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.co2EmisScenDsb.setMaximum(999999999.990000009536743)
        self.co2EmisScenDsb.setSingleStep(0.100000000000000)
        self.co2EmisScenDsb.setValue(999999.989999999990687)

        self.gridLayout.addWidget(self.co2EmisScenDsb, 22, 1, 1, 1)

        self.scenLbl = QLabel(self.scenWgt)
        self.scenLbl.setObjectName(u"scenLbl")
        self.scenLbl.setFont(font2)
        self.scenLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.scenLbl, 1, 0, 1, 1)

        self.windGenScenDsb = QDoubleSpinBox(self.scenWgt)
        self.windGenScenDsb.setObjectName(u"windGenScenDsb")
        self.windGenScenDsb.setMinimumSize(QSize(70, 0))
        self.windGenScenDsb.setMaximumSize(QSize(16777215, 16777215))
        self.windGenScenDsb.setFont(font1)
        self.windGenScenDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.windGenScenDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.windGenScenDsb.setMaximum(999999.989999999990687)
        self.windGenScenDsb.setSingleStep(0.100000000000000)
        self.windGenScenDsb.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.windGenScenDsb, 14, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_9, 21, 0, 1, 1)

        self.solarCapScenPercDsb = QDoubleSpinBox(self.scenWgt)
        self.solarCapScenPercDsb.setObjectName(u"solarCapScenPercDsb")
        self.solarCapScenPercDsb.setMinimumSize(QSize(70, 0))
        self.solarCapScenPercDsb.setMaximumSize(QSize(16777215, 16777215))
        self.solarCapScenPercDsb.setFont(font1)
        self.solarCapScenPercDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.solarCapScenPercDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.solarCapScenPercDsb.setMaximum(100.000000000000000)
        self.solarCapScenPercDsb.setSingleStep(0.100000000000000)
        self.solarCapScenPercDsb.setValue(12.000000000000000)

        self.gridLayout.addWidget(self.solarCapScenPercDsb, 18, 2, 1, 1)

        self.enImportScenLbl = QLabel(self.scenWgt)
        self.enImportScenLbl.setObjectName(u"enImportScenLbl")
        self.enImportScenLbl.setFont(font2)
        self.enImportScenLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.enImportScenLbl, 9, 0, 1, 1)

        self.enImportScenDsb = QDoubleSpinBox(self.scenWgt)
        self.enImportScenDsb.setObjectName(u"enImportScenDsb")
        self.enImportScenDsb.setMinimumSize(QSize(70, 0))
        self.enImportScenDsb.setMaximumSize(QSize(16777215, 16777215))
        self.enImportScenDsb.setFont(font1)
        self.enImportScenDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.enImportScenDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.enImportScenDsb.setMaximum(999999.989999999990687)
        self.enImportScenDsb.setSingleStep(0.100000000000000)
        self.enImportScenDsb.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.enImportScenDsb, 9, 1, 1, 1)

        self.totEnConsScenLbl = QLabel(self.scenWgt)
        self.totEnConsScenLbl.setObjectName(u"totEnConsScenLbl")
        self.totEnConsScenLbl.setFont(font2)
        self.totEnConsScenLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.totEnConsScenLbl, 4, 0, 1, 1)

        self.scenCb = QComboBox(self.scenWgt)
        self.scenCb.addItem("")
        self.scenCb.setObjectName(u"scenCb")
        self.scenCb.setMinimumSize(QSize(100, 0))
        self.scenCb.setFont(font4)
        self.scenCb.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.scenCb, 1, 1, 1, 1)

        self.otherGenScenPercDsb = QDoubleSpinBox(self.scenWgt)
        self.otherGenScenPercDsb.setObjectName(u"otherGenScenPercDsb")
        self.otherGenScenPercDsb.setMinimumSize(QSize(70, 0))
        self.otherGenScenPercDsb.setMaximumSize(QSize(16777215, 16777215))
        self.otherGenScenPercDsb.setFont(font1)
        self.otherGenScenPercDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.otherGenScenPercDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.otherGenScenPercDsb.setMaximum(100.000000000000000)
        self.otherGenScenPercDsb.setSingleStep(0.100000000000000)
        self.otherGenScenPercDsb.setValue(12.000000000000000)

        self.gridLayout.addWidget(self.otherGenScenPercDsb, 15, 2, 1, 1)

        self.otherCapScenLbl = QLabel(self.scenWgt)
        self.otherCapScenLbl.setObjectName(u"otherCapScenLbl")
        self.otherCapScenLbl.setFont(font2)
        self.otherCapScenLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.otherCapScenLbl, 20, 0, 1, 1)

        self.solarCapScenDsb = QDoubleSpinBox(self.scenWgt)
        self.solarCapScenDsb.setObjectName(u"solarCapScenDsb")
        self.solarCapScenDsb.setMinimumSize(QSize(70, 0))
        self.solarCapScenDsb.setMaximumSize(QSize(16777215, 16777215))
        self.solarCapScenDsb.setFont(font1)
        self.solarCapScenDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.solarCapScenDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.solarCapScenDsb.setMaximum(999999.989999999990687)
        self.solarCapScenDsb.setSingleStep(0.100000000000000)
        self.solarCapScenDsb.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.solarCapScenDsb, 18, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 12, 3, 1, 1)

        self.solarGenScenDsb = QDoubleSpinBox(self.scenWgt)
        self.solarGenScenDsb.setObjectName(u"solarGenScenDsb")
        self.solarGenScenDsb.setMinimumSize(QSize(70, 0))
        self.solarGenScenDsb.setMaximumSize(QSize(16777215, 16777215))
        self.solarGenScenDsb.setFont(font1)
        self.solarGenScenDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.solarGenScenDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.solarGenScenDsb.setMaximum(999999.989999999990687)
        self.solarGenScenDsb.setSingleStep(0.100000000000000)
        self.solarGenScenDsb.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.solarGenScenDsb, 13, 1, 1, 1)

        self.ferGenScenPercDsb = QDoubleSpinBox(self.scenWgt)
        self.ferGenScenPercDsb.setObjectName(u"ferGenScenPercDsb")
        self.ferGenScenPercDsb.setMinimumSize(QSize(70, 0))
        self.ferGenScenPercDsb.setMaximumSize(QSize(16777215, 16777215))
        self.ferGenScenPercDsb.setFont(font4)
        self.ferGenScenPercDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ferGenScenPercDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ferGenScenPercDsb.setMaximum(100.000000000000000)
        self.ferGenScenPercDsb.setSingleStep(0.100000000000000)
        self.ferGenScenPercDsb.setValue(12.000000000000000)

        self.gridLayout.addWidget(self.ferGenScenPercDsb, 12, 2, 1, 1)

        self.totEnConsMtepScenDsb = QDoubleSpinBox(self.scenWgt)
        self.totEnConsMtepScenDsb.setObjectName(u"totEnConsMtepScenDsb")
        self.totEnConsMtepScenDsb.setMinimumSize(QSize(70, 0))
        self.totEnConsMtepScenDsb.setMaximumSize(QSize(16777215, 16777215))
        self.totEnConsMtepScenDsb.setFont(font1)
        self.totEnConsMtepScenDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.totEnConsMtepScenDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.totEnConsMtepScenDsb.setMaximum(999999.989999999990687)
        self.totEnConsMtepScenDsb.setSingleStep(0.100000000000000)
        self.totEnConsMtepScenDsb.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.totEnConsMtepScenDsb, 4, 1, 1, 1)

        self.windCapScenLbl = QLabel(self.scenWgt)
        self.windCapScenLbl.setObjectName(u"windCapScenLbl")
        self.windCapScenLbl.setFont(font2)
        self.windCapScenLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.windCapScenLbl, 19, 0, 1, 1)

        self.enProdScenDsb = QDoubleSpinBox(self.scenWgt)
        self.enProdScenDsb.setObjectName(u"enProdScenDsb")
        self.enProdScenDsb.setMinimumSize(QSize(70, 0))
        self.enProdScenDsb.setMaximumSize(QSize(16777215, 16777215))
        self.enProdScenDsb.setFont(font1)
        self.enProdScenDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.enProdScenDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.enProdScenDsb.setMaximum(999999.989999999990687)
        self.enProdScenDsb.setSingleStep(0.100000000000000)
        self.enProdScenDsb.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.enProdScenDsb, 10, 1, 1, 1)

        self.enDutyScenLbl = QLabel(self.scenWgt)
        self.enDutyScenLbl.setObjectName(u"enDutyScenLbl")
        self.enDutyScenLbl.setFont(font2)
        self.enDutyScenLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.enDutyScenLbl, 8, 0, 1, 1)

        self.enDutyScenDsb = QDoubleSpinBox(self.scenWgt)
        self.enDutyScenDsb.setObjectName(u"enDutyScenDsb")
        self.enDutyScenDsb.setMinimumSize(QSize(70, 0))
        self.enDutyScenDsb.setMaximumSize(QSize(16777215, 16777215))
        self.enDutyScenDsb.setFont(font1)
        self.enDutyScenDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.enDutyScenDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.enDutyScenDsb.setMaximum(999999.989999999990687)
        self.enDutyScenDsb.setSingleStep(0.100000000000000)
        self.enDutyScenDsb.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.enDutyScenDsb, 8, 1, 1, 1)

        self.solarCapScenLbl = QLabel(self.scenWgt)
        self.solarCapScenLbl.setObjectName(u"solarCapScenLbl")
        self.solarCapScenLbl.setFont(font2)
        self.solarCapScenLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.solarCapScenLbl, 18, 0, 1, 1)

        self.windCapScenPercDsb = QDoubleSpinBox(self.scenWgt)
        self.windCapScenPercDsb.setObjectName(u"windCapScenPercDsb")
        self.windCapScenPercDsb.setMinimumSize(QSize(70, 0))
        self.windCapScenPercDsb.setMaximumSize(QSize(16777215, 16777215))
        self.windCapScenPercDsb.setFont(font1)
        self.windCapScenPercDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.windCapScenPercDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.windCapScenPercDsb.setMaximum(100.000000000000000)
        self.windCapScenPercDsb.setSingleStep(0.100000000000000)
        self.windCapScenPercDsb.setValue(12.000000000000000)

        self.gridLayout.addWidget(self.windCapScenPercDsb, 19, 2, 1, 1)

        self.windGenScenPercDsb = QDoubleSpinBox(self.scenWgt)
        self.windGenScenPercDsb.setObjectName(u"windGenScenPercDsb")
        self.windGenScenPercDsb.setMinimumSize(QSize(70, 0))
        self.windGenScenPercDsb.setMaximumSize(QSize(16777215, 16777215))
        self.windGenScenPercDsb.setFont(font1)
        self.windGenScenPercDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.windGenScenPercDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.windGenScenPercDsb.setMaximum(100.000000000000000)
        self.windGenScenPercDsb.setSingleStep(0.100000000000000)
        self.windGenScenPercDsb.setValue(12.000000000000000)

        self.gridLayout.addWidget(self.windGenScenPercDsb, 14, 2, 1, 1)

        self.h2ConsScenDsb = QDoubleSpinBox(self.scenWgt)
        self.h2ConsScenDsb.setObjectName(u"h2ConsScenDsb")
        self.h2ConsScenDsb.setMinimumSize(QSize(70, 0))
        self.h2ConsScenDsb.setMaximumSize(QSize(16777215, 16777215))
        self.h2ConsScenDsb.setFont(font1)
        self.h2ConsScenDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.h2ConsScenDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.h2ConsScenDsb.setMaximum(999999.989999999990687)
        self.h2ConsScenDsb.setSingleStep(0.100000000000000)
        self.h2ConsScenDsb.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.h2ConsScenDsb, 6, 1, 1, 1)

        self.otherGenScenDsb = QDoubleSpinBox(self.scenWgt)
        self.otherGenScenDsb.setObjectName(u"otherGenScenDsb")
        self.otherGenScenDsb.setMinimumSize(QSize(70, 0))
        self.otherGenScenDsb.setMaximumSize(QSize(16777215, 16777215))
        self.otherGenScenDsb.setFont(font1)
        self.otherGenScenDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.otherGenScenDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.otherGenScenDsb.setMaximum(999999.989999999990687)
        self.otherGenScenDsb.setSingleStep(0.100000000000000)
        self.otherGenScenDsb.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.otherGenScenDsb, 15, 1, 1, 1)

        self.enProdScenLbl = QLabel(self.scenWgt)
        self.enProdScenLbl.setObjectName(u"enProdScenLbl")
        self.enProdScenLbl.setFont(font2)
        self.enProdScenLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.enProdScenLbl, 10, 0, 1, 1)

        self.ferGenScenDsb = QDoubleSpinBox(self.scenWgt)
        self.ferGenScenDsb.setObjectName(u"ferGenScenDsb")
        self.ferGenScenDsb.setMinimumSize(QSize(70, 0))
        self.ferGenScenDsb.setMaximumSize(QSize(16777215, 16777215))
        self.ferGenScenDsb.setFont(font4)
        self.ferGenScenDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ferGenScenDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ferGenScenDsb.setMaximum(999999.989999999990687)
        self.ferGenScenDsb.setSingleStep(0.100000000000000)
        self.ferGenScenDsb.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.ferGenScenDsb, 12, 1, 1, 1)

        self.windGenScenLbl = QLabel(self.scenWgt)
        self.windGenScenLbl.setObjectName(u"windGenScenLbl")
        self.windGenScenLbl.setFont(font2)
        self.windGenScenLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.windGenScenLbl, 14, 0, 1, 1)

        self.yearScenLbl = QLabel(self.scenWgt)
        self.yearScenLbl.setObjectName(u"yearScenLbl")
        self.yearScenLbl.setFont(font2)
        self.yearScenLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.yearScenLbl, 0, 0, 1, 1)

        self.ferCapScenLbl = QLabel(self.scenWgt)
        self.ferCapScenLbl.setObjectName(u"ferCapScenLbl")
        font5 = QFont()
        font5.setPointSize(9)
        font5.setBold(True)
        font5.setWeight(75)
        self.ferCapScenLbl.setFont(font5)
        self.ferCapScenLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.ferCapScenLbl, 17, 0, 1, 1)

        self.h2ConsScenLbl = QLabel(self.scenWgt)
        self.h2ConsScenLbl.setObjectName(u"h2ConsScenLbl")
        font6 = QFont()
        font6.setPointSize(9)
        font6.setItalic(True)
        self.h2ConsScenLbl.setFont(font6)
        self.h2ConsScenLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.h2ConsScenLbl, 6, 0, 1, 1)

        self.windCapScenDsb = QDoubleSpinBox(self.scenWgt)
        self.windCapScenDsb.setObjectName(u"windCapScenDsb")
        self.windCapScenDsb.setMinimumSize(QSize(70, 0))
        self.windCapScenDsb.setMaximumSize(QSize(16777215, 16777215))
        self.windCapScenDsb.setFont(font1)
        self.windCapScenDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.windCapScenDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.windCapScenDsb.setMaximum(999999.989999999990687)
        self.windCapScenDsb.setSingleStep(0.100000000000000)
        self.windCapScenDsb.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.windCapScenDsb, 19, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 3, 1, 1, 1)

        self.otherCapScenPercDsb = QDoubleSpinBox(self.scenWgt)
        self.otherCapScenPercDsb.setObjectName(u"otherCapScenPercDsb")
        self.otherCapScenPercDsb.setMinimumSize(QSize(70, 0))
        self.otherCapScenPercDsb.setMaximumSize(QSize(16777215, 16777215))
        self.otherCapScenPercDsb.setFont(font1)
        self.otherCapScenPercDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.otherCapScenPercDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.otherCapScenPercDsb.setMaximum(100.000000000000000)
        self.otherCapScenPercDsb.setSingleStep(0.100000000000000)
        self.otherCapScenPercDsb.setValue(12.000000000000000)

        self.gridLayout.addWidget(self.otherCapScenPercDsb, 20, 2, 1, 1)

        self.otherCapScenDsb = QDoubleSpinBox(self.scenWgt)
        self.otherCapScenDsb.setObjectName(u"otherCapScenDsb")
        self.otherCapScenDsb.setMinimumSize(QSize(70, 0))
        self.otherCapScenDsb.setMaximumSize(QSize(16777215, 16777215))
        self.otherCapScenDsb.setFont(font1)
        self.otherCapScenDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.otherCapScenDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.otherCapScenDsb.setMaximum(999999.989999999990687)
        self.otherCapScenDsb.setSingleStep(0.100000000000000)
        self.otherCapScenDsb.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.otherCapScenDsb, 20, 1, 1, 1)

        self.totEnConsScenDsb = QDoubleSpinBox(self.scenWgt)
        self.totEnConsScenDsb.setObjectName(u"totEnConsScenDsb")
        self.totEnConsScenDsb.setMinimumSize(QSize(70, 0))
        self.totEnConsScenDsb.setMaximumSize(QSize(16777215, 16777215))
        self.totEnConsScenDsb.setFont(font1)
        self.totEnConsScenDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.totEnConsScenDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.totEnConsScenDsb.setMaximum(999999.989999999990687)
        self.totEnConsScenDsb.setSingleStep(0.100000000000000)
        self.totEnConsScenDsb.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.totEnConsScenDsb, 5, 1, 1, 1)

        self.solarGenScenLbl = QLabel(self.scenWgt)
        self.solarGenScenLbl.setObjectName(u"solarGenScenLbl")
        self.solarGenScenLbl.setFont(font2)
        self.solarGenScenLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.solarGenScenLbl, 13, 0, 1, 1)

        self.yearScenCb = QComboBox(self.scenWgt)
        self.yearScenCb.addItem("")
        self.yearScenCb.addItem("")
        self.yearScenCb.addItem("")
        self.yearScenCb.setObjectName(u"yearScenCb")
        self.yearScenCb.setMinimumSize(QSize(100, 0))
        self.yearScenCb.setFont(font4)
        self.yearScenCb.setLayoutDirection(Qt.LeftToRight)
        self.yearScenCb.setStyleSheet(u"")

        self.gridLayout.addWidget(self.yearScenCb, 0, 1, 1, 1)

        self.ferCapScenDsb = QDoubleSpinBox(self.scenWgt)
        self.ferCapScenDsb.setObjectName(u"ferCapScenDsb")
        self.ferCapScenDsb.setMinimumSize(QSize(70, 0))
        self.ferCapScenDsb.setMaximumSize(QSize(16777215, 16777215))
        self.ferCapScenDsb.setFont(font4)
        self.ferCapScenDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ferCapScenDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ferCapScenDsb.setMaximum(999999.989999999990687)
        self.ferCapScenDsb.setSingleStep(0.100000000000000)
        self.ferCapScenDsb.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.ferCapScenDsb, 17, 1, 1, 1)

        self.ferGenScenLbl = QLabel(self.scenWgt)
        self.ferGenScenLbl.setObjectName(u"ferGenScenLbl")
        self.ferGenScenLbl.setFont(font5)
        self.ferGenScenLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.ferGenScenLbl, 12, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 11, 0, 1, 1)

        self.otherGenScenLbl = QLabel(self.scenWgt)
        self.otherGenScenLbl.setObjectName(u"otherGenScenLbl")
        self.otherGenScenLbl.setFont(font2)
        self.otherGenScenLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.otherGenScenLbl, 15, 0, 1, 1)

        self.solarGenScenPercLbl = QDoubleSpinBox(self.scenWgt)
        self.solarGenScenPercLbl.setObjectName(u"solarGenScenPercLbl")
        self.solarGenScenPercLbl.setMinimumSize(QSize(70, 0))
        self.solarGenScenPercLbl.setMaximumSize(QSize(16777215, 16777215))
        self.solarGenScenPercLbl.setFont(font1)
        self.solarGenScenPercLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.solarGenScenPercLbl.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.solarGenScenPercLbl.setMaximum(100.000000000000000)
        self.solarGenScenPercLbl.setSingleStep(0.100000000000000)
        self.solarGenScenPercLbl.setValue(12.000000000000000)

        self.gridLayout.addWidget(self.solarGenScenPercLbl, 13, 2, 1, 1)

        self.co2EmisScenLbl = QLabel(self.scenWgt)
        self.co2EmisScenLbl.setObjectName(u"co2EmisScenLbl")
        self.co2EmisScenLbl.setFont(font5)
        self.co2EmisScenLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.co2EmisScenLbl, 22, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 16, 0, 1, 1)

        self.ferCapScenPercDsb = QDoubleSpinBox(self.scenWgt)
        self.ferCapScenPercDsb.setObjectName(u"ferCapScenPercDsb")
        self.ferCapScenPercDsb.setMinimumSize(QSize(70, 0))
        self.ferCapScenPercDsb.setMaximumSize(QSize(16777215, 16777215))
        self.ferCapScenPercDsb.setFont(font4)
        self.ferCapScenPercDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ferCapScenPercDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ferCapScenPercDsb.setMaximum(100.000000000000000)
        self.ferCapScenPercDsb.setSingleStep(0.100000000000000)
        self.ferCapScenPercDsb.setValue(12.000000000000000)

        self.gridLayout.addWidget(self.ferCapScenPercDsb, 17, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_8, 7, 1, 1, 1)


        self.leftVL.addWidget(self.scenWgt)

        self.verticalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.leftVL.addItem(self.verticalSpacer_10)

        self.calcPb = QPushButton(self.leftWgt)
        self.calcPb.setObjectName(u"calcPb")
        self.calcPb.setMinimumSize(QSize(0, 30))
        self.calcPb.setMaximumSize(QSize(16777215, 30))

        self.leftVL.addWidget(self.calcPb)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.leftVL.addItem(self.verticalSpacer_11)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.leftVL.addItem(self.verticalSpacer)


        self.optStorHL.addWidget(self.leftWgt)

        self.resultsWgt = QWidget(self.optStorWgt)
        self.resultsWgt.setObjectName(u"resultsWgt")
        self.resultsWgt.setMaximumSize(QSize(16777215, 16777215))
        self.resultsHL = QHBoxLayout(self.resultsWgt)
        self.resultsHL.setSpacing(0)
        self.resultsHL.setObjectName(u"resultsHL")
        self.resultsHL.setContentsMargins(10, 0, 10, 0)
        self.centerWgt = QWidget(self.resultsWgt)
        self.centerWgt.setObjectName(u"centerWgt")
        self.centerWgt.setMaximumSize(QSize(450, 16777215))
        self.centerWgt.setStyleSheet(u"*{}\n"
"\n"
"QWidget{\n"
"	border-radius: 10px\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centerWgt)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.duttResLbl = QLabel(self.centerWgt)
        self.duttResLbl.setObjectName(u"duttResLbl")
        self.duttResLbl.setMinimumSize(QSize(0, 30))
        self.duttResLbl.setFont(font)
        self.duttResLbl.setStyleSheet(u"border: solid;\n"
"border-radius: 10px;\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.duttResLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.duttResLbl)

        self.energyResWgt = QWidget(self.centerWgt)
        self.energyResWgt.setObjectName(u"energyResWgt")
        self.energyResWgt.setMaximumSize(QSize(16777215, 16777215))
        self.energyResWgt.setStyleSheet(u"background-color: rgb(23, 23, 0);")
        self.gridLayout_3 = QGridLayout(self.energyResWgt)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.enImportResPerspDsb = QDoubleSpinBox(self.energyResWgt)
        self.enImportResPerspDsb.setObjectName(u"enImportResPerspDsb")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enImportResPerspDsb.sizePolicy().hasHeightForWidth())
        self.enImportResPerspDsb.setSizePolicy(sizePolicy)
        self.enImportResPerspDsb.setMinimumSize(QSize(110, 0))
        self.enImportResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.enImportResPerspDsb.setFont(font1)
        self.enImportResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.enImportResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.enImportResPerspDsb.setMaximum(999999.989999999990687)
        self.enImportResPerspDsb.setSingleStep(0.100000000000000)
        self.enImportResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_3.addWidget(self.enImportResPerspDsb, 7, 2, 1, 1)

        self.enImportResLbl = QLabel(self.energyResWgt)
        self.enImportResLbl.setObjectName(u"enImportResLbl")
        self.enImportResLbl.setFont(font2)
        self.enImportResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.enImportResLbl, 7, 0, 1, 1)

        self.totEnConsResActDsb = QDoubleSpinBox(self.energyResWgt)
        self.totEnConsResActDsb.setObjectName(u"totEnConsResActDsb")
        sizePolicy.setHeightForWidth(self.totEnConsResActDsb.sizePolicy().hasHeightForWidth())
        self.totEnConsResActDsb.setSizePolicy(sizePolicy)
        self.totEnConsResActDsb.setMinimumSize(QSize(110, 0))
        self.totEnConsResActDsb.setMaximumSize(QSize(110, 16777215))
        self.totEnConsResActDsb.setFont(font1)
        self.totEnConsResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.totEnConsResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.totEnConsResActDsb.setMaximum(999999.989999999990687)
        self.totEnConsResActDsb.setSingleStep(0.100000000000000)
        self.totEnConsResActDsb.setValue(0.000000000000000)

        self.gridLayout_3.addWidget(self.totEnConsResActDsb, 4, 1, 1, 1)

        self.perspDutyLbl = QLabel(self.energyResWgt)
        self.perspDutyLbl.setObjectName(u"perspDutyLbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.perspDutyLbl.sizePolicy().hasHeightForWidth())
        self.perspDutyLbl.setSizePolicy(sizePolicy1)
        self.perspDutyLbl.setMinimumSize(QSize(110, 0))
        self.perspDutyLbl.setMaximumSize(QSize(110, 16777215))
        font7 = QFont()
        font7.setBold(False)
        font7.setItalic(True)
        font7.setWeight(50)
        self.perspDutyLbl.setFont(font7)
        self.perspDutyLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.perspDutyLbl, 1, 2, 1, 1)

        self.actDutyLbl = QLabel(self.energyResWgt)
        self.actDutyLbl.setObjectName(u"actDutyLbl")
        sizePolicy1.setHeightForWidth(self.actDutyLbl.sizePolicy().hasHeightForWidth())
        self.actDutyLbl.setSizePolicy(sizePolicy1)
        self.actDutyLbl.setMinimumSize(QSize(110, 0))
        self.actDutyLbl.setMaximumSize(QSize(110, 16777215))
        self.actDutyLbl.setFont(font7)
        self.actDutyLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.actDutyLbl, 1, 1, 1, 1)

        self.h2ConsResLbl = QLabel(self.energyResWgt)
        self.h2ConsResLbl.setObjectName(u"h2ConsResLbl")
        self.h2ConsResLbl.setFont(font2)
        self.h2ConsResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.h2ConsResLbl, 5, 0, 1, 1)

        self.h2ConsResPerspDsb = QDoubleSpinBox(self.energyResWgt)
        self.h2ConsResPerspDsb.setObjectName(u"h2ConsResPerspDsb")
        sizePolicy.setHeightForWidth(self.h2ConsResPerspDsb.sizePolicy().hasHeightForWidth())
        self.h2ConsResPerspDsb.setSizePolicy(sizePolicy)
        self.h2ConsResPerspDsb.setMinimumSize(QSize(110, 0))
        self.h2ConsResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.h2ConsResPerspDsb.setFont(font1)
        self.h2ConsResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.h2ConsResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.h2ConsResPerspDsb.setMaximum(999999.989999999990687)
        self.h2ConsResPerspDsb.setSingleStep(0.100000000000000)
        self.h2ConsResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_3.addWidget(self.h2ConsResPerspDsb, 5, 2, 1, 1)

        self.totEnConsMtepResActDsb = QDoubleSpinBox(self.energyResWgt)
        self.totEnConsMtepResActDsb.setObjectName(u"totEnConsMtepResActDsb")
        sizePolicy.setHeightForWidth(self.totEnConsMtepResActDsb.sizePolicy().hasHeightForWidth())
        self.totEnConsMtepResActDsb.setSizePolicy(sizePolicy)
        self.totEnConsMtepResActDsb.setMinimumSize(QSize(110, 0))
        self.totEnConsMtepResActDsb.setMaximumSize(QSize(110, 16777215))
        self.totEnConsMtepResActDsb.setFont(font1)
        self.totEnConsMtepResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.totEnConsMtepResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.totEnConsMtepResActDsb.setMaximum(999999.989999999990687)
        self.totEnConsMtepResActDsb.setSingleStep(0.100000000000000)
        self.totEnConsMtepResActDsb.setValue(0.000000000000000)

        self.gridLayout_3.addWidget(self.totEnConsMtepResActDsb, 3, 1, 1, 1)

        self.enDutyResPerspDsb = QDoubleSpinBox(self.energyResWgt)
        self.enDutyResPerspDsb.setObjectName(u"enDutyResPerspDsb")
        sizePolicy.setHeightForWidth(self.enDutyResPerspDsb.sizePolicy().hasHeightForWidth())
        self.enDutyResPerspDsb.setSizePolicy(sizePolicy)
        self.enDutyResPerspDsb.setMinimumSize(QSize(110, 0))
        self.enDutyResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.enDutyResPerspDsb.setFont(font1)
        self.enDutyResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.enDutyResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.enDutyResPerspDsb.setMaximum(999999.989999999990687)
        self.enDutyResPerspDsb.setSingleStep(0.100000000000000)
        self.enDutyResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_3.addWidget(self.enDutyResPerspDsb, 6, 2, 1, 1)

        self.enProdResActDsb = QDoubleSpinBox(self.energyResWgt)
        self.enProdResActDsb.setObjectName(u"enProdResActDsb")
        sizePolicy.setHeightForWidth(self.enProdResActDsb.sizePolicy().hasHeightForWidth())
        self.enProdResActDsb.setSizePolicy(sizePolicy)
        self.enProdResActDsb.setMinimumSize(QSize(110, 0))
        self.enProdResActDsb.setMaximumSize(QSize(110, 16777215))
        self.enProdResActDsb.setFont(font1)
        self.enProdResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.enProdResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.enProdResActDsb.setMaximum(999999.989999999990687)
        self.enProdResActDsb.setSingleStep(0.100000000000000)
        self.enProdResActDsb.setValue(0.000000000000000)

        self.gridLayout_3.addWidget(self.enProdResActDsb, 8, 1, 1, 1)

        self.totEnConsResPerspDsb = QDoubleSpinBox(self.energyResWgt)
        self.totEnConsResPerspDsb.setObjectName(u"totEnConsResPerspDsb")
        sizePolicy.setHeightForWidth(self.totEnConsResPerspDsb.sizePolicy().hasHeightForWidth())
        self.totEnConsResPerspDsb.setSizePolicy(sizePolicy)
        self.totEnConsResPerspDsb.setMinimumSize(QSize(110, 0))
        self.totEnConsResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.totEnConsResPerspDsb.setFont(font1)
        self.totEnConsResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.totEnConsResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.totEnConsResPerspDsb.setMaximum(999999.989999999990687)
        self.totEnConsResPerspDsb.setSingleStep(0.100000000000000)
        self.totEnConsResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_3.addWidget(self.totEnConsResPerspDsb, 4, 2, 1, 1)

        self.enDutyResActDsb = QDoubleSpinBox(self.energyResWgt)
        self.enDutyResActDsb.setObjectName(u"enDutyResActDsb")
        sizePolicy.setHeightForWidth(self.enDutyResActDsb.sizePolicy().hasHeightForWidth())
        self.enDutyResActDsb.setSizePolicy(sizePolicy)
        self.enDutyResActDsb.setMinimumSize(QSize(110, 0))
        self.enDutyResActDsb.setMaximumSize(QSize(110, 16777215))
        self.enDutyResActDsb.setFont(font1)
        self.enDutyResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.enDutyResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.enDutyResActDsb.setMaximum(999999.989999999990687)
        self.enDutyResActDsb.setSingleStep(0.100000000000000)
        self.enDutyResActDsb.setValue(0.000000000000000)

        self.gridLayout_3.addWidget(self.enDutyResActDsb, 6, 1, 1, 1)

        self.enDutyResLbl = QLabel(self.energyResWgt)
        self.enDutyResLbl.setObjectName(u"enDutyResLbl")
        self.enDutyResLbl.setFont(font2)
        self.enDutyResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.enDutyResLbl, 6, 0, 1, 1)

        self.enProdResLbl = QLabel(self.energyResWgt)
        self.enProdResLbl.setObjectName(u"enProdResLbl")
        self.enProdResLbl.setFont(font2)
        self.enProdResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.enProdResLbl, 8, 0, 1, 1)

        self.enProdResPerspDsb = QDoubleSpinBox(self.energyResWgt)
        self.enProdResPerspDsb.setObjectName(u"enProdResPerspDsb")
        sizePolicy.setHeightForWidth(self.enProdResPerspDsb.sizePolicy().hasHeightForWidth())
        self.enProdResPerspDsb.setSizePolicy(sizePolicy)
        self.enProdResPerspDsb.setMinimumSize(QSize(110, 0))
        self.enProdResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.enProdResPerspDsb.setFont(font1)
        self.enProdResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.enProdResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.enProdResPerspDsb.setMaximum(999999.989999999990687)
        self.enProdResPerspDsb.setSingleStep(0.100000000000000)
        self.enProdResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_3.addWidget(self.enProdResPerspDsb, 8, 2, 1, 1)

        self.h2ConsResActDsb = QDoubleSpinBox(self.energyResWgt)
        self.h2ConsResActDsb.setObjectName(u"h2ConsResActDsb")
        sizePolicy.setHeightForWidth(self.h2ConsResActDsb.sizePolicy().hasHeightForWidth())
        self.h2ConsResActDsb.setSizePolicy(sizePolicy)
        self.h2ConsResActDsb.setMinimumSize(QSize(110, 0))
        self.h2ConsResActDsb.setMaximumSize(QSize(110, 16777215))
        self.h2ConsResActDsb.setFont(font1)
        self.h2ConsResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.h2ConsResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.h2ConsResActDsb.setMaximum(999999.989999999990687)
        self.h2ConsResActDsb.setSingleStep(0.100000000000000)
        self.h2ConsResActDsb.setValue(0.000000000000000)

        self.gridLayout_3.addWidget(self.h2ConsResActDsb, 5, 1, 1, 1)

        self.verticalSpacer_35 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_35, 2, 0, 1, 1)

        self.totEnConsMtepResPerspDsb = QDoubleSpinBox(self.energyResWgt)
        self.totEnConsMtepResPerspDsb.setObjectName(u"totEnConsMtepResPerspDsb")
        sizePolicy.setHeightForWidth(self.totEnConsMtepResPerspDsb.sizePolicy().hasHeightForWidth())
        self.totEnConsMtepResPerspDsb.setSizePolicy(sizePolicy)
        self.totEnConsMtepResPerspDsb.setMinimumSize(QSize(110, 0))
        self.totEnConsMtepResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.totEnConsMtepResPerspDsb.setFont(font1)
        self.totEnConsMtepResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.totEnConsMtepResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.totEnConsMtepResPerspDsb.setMaximum(999999.989999999990687)
        self.totEnConsMtepResPerspDsb.setSingleStep(0.100000000000000)
        self.totEnConsMtepResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_3.addWidget(self.totEnConsMtepResPerspDsb, 3, 2, 1, 1)

        self.enImportResActDsb = QDoubleSpinBox(self.energyResWgt)
        self.enImportResActDsb.setObjectName(u"enImportResActDsb")
        sizePolicy.setHeightForWidth(self.enImportResActDsb.sizePolicy().hasHeightForWidth())
        self.enImportResActDsb.setSizePolicy(sizePolicy)
        self.enImportResActDsb.setMinimumSize(QSize(110, 0))
        self.enImportResActDsb.setMaximumSize(QSize(110, 16777215))
        self.enImportResActDsb.setFont(font1)
        self.enImportResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.enImportResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.enImportResActDsb.setMaximum(999999.989999999990687)
        self.enImportResActDsb.setSingleStep(0.100000000000000)
        self.enImportResActDsb.setValue(0.000000000000000)

        self.gridLayout_3.addWidget(self.enImportResActDsb, 7, 1, 1, 1)

        self.totEnConsResLbl = QLabel(self.energyResWgt)
        self.totEnConsResLbl.setObjectName(u"totEnConsResLbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.totEnConsResLbl.sizePolicy().hasHeightForWidth())
        self.totEnConsResLbl.setSizePolicy(sizePolicy2)
        self.totEnConsResLbl.setFont(font2)
        self.totEnConsResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.totEnConsResLbl, 3, 0, 1, 1)


        self.verticalLayout.addWidget(self.energyResWgt)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.renResLBL = QLabel(self.centerWgt)
        self.renResLBL.setObjectName(u"renResLBL")
        self.renResLBL.setMinimumSize(QSize(0, 30))
        self.renResLBL.setFont(font)
        self.renResLBL.setStyleSheet(u"border: solid;\n"
"border-radius: 10px;\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.renResLBL.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.renResLBL)

        self.genResWgt = QWidget(self.centerWgt)
        self.genResWgt.setObjectName(u"genResWgt")
        self.genResWgt.setMaximumSize(QSize(16777215, 16777215))
        self.genResWgt.setStyleSheet(u"background-color: rgb(31, 31, 0);")
        self.gridLayout_4 = QGridLayout(self.genResWgt)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.solarGenResActDsb = QDoubleSpinBox(self.genResWgt)
        self.solarGenResActDsb.setObjectName(u"solarGenResActDsb")
        sizePolicy.setHeightForWidth(self.solarGenResActDsb.sizePolicy().hasHeightForWidth())
        self.solarGenResActDsb.setSizePolicy(sizePolicy)
        self.solarGenResActDsb.setMinimumSize(QSize(110, 0))
        self.solarGenResActDsb.setMaximumSize(QSize(110, 16777215))
        self.solarGenResActDsb.setFont(font1)
        self.solarGenResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.solarGenResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.solarGenResActDsb.setMaximum(999999.989999999990687)
        self.solarGenResActDsb.setSingleStep(0.100000000000000)
        self.solarGenResActDsb.setValue(0.000000000000000)

        self.gridLayout_4.addWidget(self.solarGenResActDsb, 5, 1, 1, 1)

        self.verticalSpacer_27 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_27, 7, 0, 1, 1)

        self.windGenPercResPerspDsb = QDoubleSpinBox(self.genResWgt)
        self.windGenPercResPerspDsb.setObjectName(u"windGenPercResPerspDsb")
        sizePolicy.setHeightForWidth(self.windGenPercResPerspDsb.sizePolicy().hasHeightForWidth())
        self.windGenPercResPerspDsb.setSizePolicy(sizePolicy)
        self.windGenPercResPerspDsb.setMinimumSize(QSize(110, 0))
        self.windGenPercResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.windGenPercResPerspDsb.setFont(font1)
        self.windGenPercResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.windGenPercResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.windGenPercResPerspDsb.setMaximum(100.000000000000000)
        self.windGenPercResPerspDsb.setSingleStep(0.100000000000000)
        self.windGenPercResPerspDsb.setValue(12.000000000000000)

        self.gridLayout_4.addWidget(self.windGenPercResPerspDsb, 9, 2, 1, 1)

        self.solarGenResPerspDsb = QDoubleSpinBox(self.genResWgt)
        self.solarGenResPerspDsb.setObjectName(u"solarGenResPerspDsb")
        sizePolicy.setHeightForWidth(self.solarGenResPerspDsb.sizePolicy().hasHeightForWidth())
        self.solarGenResPerspDsb.setSizePolicy(sizePolicy)
        self.solarGenResPerspDsb.setMinimumSize(QSize(110, 0))
        self.solarGenResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.solarGenResPerspDsb.setFont(font1)
        self.solarGenResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.solarGenResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.solarGenResPerspDsb.setMaximum(999999.989999999990687)
        self.solarGenResPerspDsb.setSingleStep(0.100000000000000)
        self.solarGenResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_4.addWidget(self.solarGenResPerspDsb, 5, 2, 1, 1)

        self.verticalSpacer_28 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_28, 4, 0, 1, 1)

        self.otherGenPercResActDsb = QDoubleSpinBox(self.genResWgt)
        self.otherGenPercResActDsb.setObjectName(u"otherGenPercResActDsb")
        sizePolicy.setHeightForWidth(self.otherGenPercResActDsb.sizePolicy().hasHeightForWidth())
        self.otherGenPercResActDsb.setSizePolicy(sizePolicy)
        self.otherGenPercResActDsb.setMinimumSize(QSize(110, 0))
        self.otherGenPercResActDsb.setMaximumSize(QSize(110, 16777215))
        self.otherGenPercResActDsb.setFont(font1)
        self.otherGenPercResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.otherGenPercResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.otherGenPercResActDsb.setMaximum(100.000000000000000)
        self.otherGenPercResActDsb.setSingleStep(0.100000000000000)
        self.otherGenPercResActDsb.setValue(12.000000000000000)

        self.gridLayout_4.addWidget(self.otherGenPercResActDsb, 12, 1, 1, 1)

        self.ferGenPercResPerspDsb = QDoubleSpinBox(self.genResWgt)
        self.ferGenPercResPerspDsb.setObjectName(u"ferGenPercResPerspDsb")
        sizePolicy.setHeightForWidth(self.ferGenPercResPerspDsb.sizePolicy().hasHeightForWidth())
        self.ferGenPercResPerspDsb.setSizePolicy(sizePolicy)
        self.ferGenPercResPerspDsb.setMinimumSize(QSize(110, 0))
        self.ferGenPercResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.ferGenPercResPerspDsb.setFont(font4)
        self.ferGenPercResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ferGenPercResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ferGenPercResPerspDsb.setMaximum(100.000000000000000)
        self.ferGenPercResPerspDsb.setSingleStep(0.100000000000000)
        self.ferGenPercResPerspDsb.setValue(12.000000000000000)

        self.gridLayout_4.addWidget(self.ferGenPercResPerspDsb, 3, 2, 1, 1)

        self.ferGenResPerspDsb = QDoubleSpinBox(self.genResWgt)
        self.ferGenResPerspDsb.setObjectName(u"ferGenResPerspDsb")
        sizePolicy.setHeightForWidth(self.ferGenResPerspDsb.sizePolicy().hasHeightForWidth())
        self.ferGenResPerspDsb.setSizePolicy(sizePolicy)
        self.ferGenResPerspDsb.setMinimumSize(QSize(110, 0))
        self.ferGenResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.ferGenResPerspDsb.setFont(font4)
        self.ferGenResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ferGenResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ferGenResPerspDsb.setMaximum(999999.989999999990687)
        self.ferGenResPerspDsb.setSingleStep(0.100000000000000)
        self.ferGenResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_4.addWidget(self.ferGenResPerspDsb, 2, 2, 1, 1)

        self.windGenResLbl = QLabel(self.genResWgt)
        self.windGenResLbl.setObjectName(u"windGenResLbl")
        self.windGenResLbl.setFont(font2)
        self.windGenResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.windGenResLbl, 8, 0, 1, 1)

        self.windGenResActDsb = QDoubleSpinBox(self.genResWgt)
        self.windGenResActDsb.setObjectName(u"windGenResActDsb")
        sizePolicy.setHeightForWidth(self.windGenResActDsb.sizePolicy().hasHeightForWidth())
        self.windGenResActDsb.setSizePolicy(sizePolicy)
        self.windGenResActDsb.setMinimumSize(QSize(110, 0))
        self.windGenResActDsb.setMaximumSize(QSize(110, 16777215))
        self.windGenResActDsb.setFont(font1)
        self.windGenResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.windGenResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.windGenResActDsb.setMaximum(999999.989999999990687)
        self.windGenResActDsb.setSingleStep(0.100000000000000)
        self.windGenResActDsb.setValue(0.000000000000000)

        self.gridLayout_4.addWidget(self.windGenResActDsb, 8, 1, 1, 1)

        self.solarGenPercResActDsb = QDoubleSpinBox(self.genResWgt)
        self.solarGenPercResActDsb.setObjectName(u"solarGenPercResActDsb")
        sizePolicy.setHeightForWidth(self.solarGenPercResActDsb.sizePolicy().hasHeightForWidth())
        self.solarGenPercResActDsb.setSizePolicy(sizePolicy)
        self.solarGenPercResActDsb.setMinimumSize(QSize(110, 0))
        self.solarGenPercResActDsb.setMaximumSize(QSize(110, 16777215))
        self.solarGenPercResActDsb.setFont(font1)
        self.solarGenPercResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.solarGenPercResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.solarGenPercResActDsb.setMaximum(100.000000000000000)
        self.solarGenPercResActDsb.setSingleStep(0.100000000000000)
        self.solarGenPercResActDsb.setValue(12.000000000000000)

        self.gridLayout_4.addWidget(self.solarGenPercResActDsb, 6, 1, 1, 1)

        self.ferGenResLbl = QLabel(self.genResWgt)
        self.ferGenResLbl.setObjectName(u"ferGenResLbl")
        self.ferGenResLbl.setFont(font5)
        self.ferGenResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.ferGenResLbl, 2, 0, 1, 1)

        self.windGenPercResActDsb = QDoubleSpinBox(self.genResWgt)
        self.windGenPercResActDsb.setObjectName(u"windGenPercResActDsb")
        sizePolicy.setHeightForWidth(self.windGenPercResActDsb.sizePolicy().hasHeightForWidth())
        self.windGenPercResActDsb.setSizePolicy(sizePolicy)
        self.windGenPercResActDsb.setMinimumSize(QSize(110, 0))
        self.windGenPercResActDsb.setMaximumSize(QSize(110, 16777215))
        self.windGenPercResActDsb.setFont(font1)
        self.windGenPercResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.windGenPercResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.windGenPercResActDsb.setMaximum(100.000000000000000)
        self.windGenPercResActDsb.setSingleStep(0.100000000000000)
        self.windGenPercResActDsb.setValue(12.000000000000000)

        self.gridLayout_4.addWidget(self.windGenPercResActDsb, 9, 1, 1, 1)

        self.otherGenPercResPerspDsb = QDoubleSpinBox(self.genResWgt)
        self.otherGenPercResPerspDsb.setObjectName(u"otherGenPercResPerspDsb")
        sizePolicy.setHeightForWidth(self.otherGenPercResPerspDsb.sizePolicy().hasHeightForWidth())
        self.otherGenPercResPerspDsb.setSizePolicy(sizePolicy)
        self.otherGenPercResPerspDsb.setMinimumSize(QSize(110, 0))
        self.otherGenPercResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.otherGenPercResPerspDsb.setFont(font1)
        self.otherGenPercResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.otherGenPercResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.otherGenPercResPerspDsb.setMaximum(100.000000000000000)
        self.otherGenPercResPerspDsb.setSingleStep(0.100000000000000)
        self.otherGenPercResPerspDsb.setValue(12.000000000000000)

        self.gridLayout_4.addWidget(self.otherGenPercResPerspDsb, 12, 2, 1, 1)

        self.ferGenPercResActDsb = QDoubleSpinBox(self.genResWgt)
        self.ferGenPercResActDsb.setObjectName(u"ferGenPercResActDsb")
        sizePolicy.setHeightForWidth(self.ferGenPercResActDsb.sizePolicy().hasHeightForWidth())
        self.ferGenPercResActDsb.setSizePolicy(sizePolicy)
        self.ferGenPercResActDsb.setMinimumSize(QSize(110, 0))
        self.ferGenPercResActDsb.setMaximumSize(QSize(110, 16777215))
        self.ferGenPercResActDsb.setFont(font4)
        self.ferGenPercResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ferGenPercResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ferGenPercResActDsb.setMaximum(100.000000000000000)
        self.ferGenPercResActDsb.setSingleStep(0.100000000000000)
        self.ferGenPercResActDsb.setValue(12.000000000000000)

        self.gridLayout_4.addWidget(self.ferGenPercResActDsb, 3, 1, 1, 1)

        self.ferGenResActDsb = QDoubleSpinBox(self.genResWgt)
        self.ferGenResActDsb.setObjectName(u"ferGenResActDsb")
        sizePolicy.setHeightForWidth(self.ferGenResActDsb.sizePolicy().hasHeightForWidth())
        self.ferGenResActDsb.setSizePolicy(sizePolicy)
        self.ferGenResActDsb.setMinimumSize(QSize(110, 0))
        self.ferGenResActDsb.setMaximumSize(QSize(110, 16777215))
        self.ferGenResActDsb.setFont(font4)
        self.ferGenResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ferGenResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ferGenResActDsb.setMaximum(999999.989999999990687)
        self.ferGenResActDsb.setSingleStep(0.100000000000000)
        self.ferGenResActDsb.setValue(0.000000000000000)

        self.gridLayout_4.addWidget(self.ferGenResActDsb, 2, 1, 1, 1)

        self.verticalSpacer_32 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_32, 1, 0, 1, 1)

        self.solarGenPercResPerspDsb = QDoubleSpinBox(self.genResWgt)
        self.solarGenPercResPerspDsb.setObjectName(u"solarGenPercResPerspDsb")
        sizePolicy.setHeightForWidth(self.solarGenPercResPerspDsb.sizePolicy().hasHeightForWidth())
        self.solarGenPercResPerspDsb.setSizePolicy(sizePolicy)
        self.solarGenPercResPerspDsb.setMinimumSize(QSize(110, 0))
        self.solarGenPercResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.solarGenPercResPerspDsb.setFont(font1)
        self.solarGenPercResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.solarGenPercResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.solarGenPercResPerspDsb.setMaximum(100.000000000000000)
        self.solarGenPercResPerspDsb.setSingleStep(0.100000000000000)
        self.solarGenPercResPerspDsb.setValue(1.200000000000000)

        self.gridLayout_4.addWidget(self.solarGenPercResPerspDsb, 6, 2, 1, 1)

        self.windGenResPerspDsb = QDoubleSpinBox(self.genResWgt)
        self.windGenResPerspDsb.setObjectName(u"windGenResPerspDsb")
        sizePolicy.setHeightForWidth(self.windGenResPerspDsb.sizePolicy().hasHeightForWidth())
        self.windGenResPerspDsb.setSizePolicy(sizePolicy)
        self.windGenResPerspDsb.setMinimumSize(QSize(110, 0))
        self.windGenResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.windGenResPerspDsb.setFont(font1)
        self.windGenResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.windGenResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.windGenResPerspDsb.setMaximum(999999.989999999990687)
        self.windGenResPerspDsb.setSingleStep(0.100000000000000)
        self.windGenResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_4.addWidget(self.windGenResPerspDsb, 8, 2, 1, 1)

        self.perspGenLbl = QLabel(self.genResWgt)
        self.perspGenLbl.setObjectName(u"perspGenLbl")
        sizePolicy1.setHeightForWidth(self.perspGenLbl.sizePolicy().hasHeightForWidth())
        self.perspGenLbl.setSizePolicy(sizePolicy1)
        self.perspGenLbl.setMinimumSize(QSize(110, 0))
        self.perspGenLbl.setMaximumSize(QSize(110, 16777215))
        self.perspGenLbl.setFont(font7)
        self.perspGenLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.perspGenLbl, 0, 2, 1, 1)

        self.otherGenResLbl = QLabel(self.genResWgt)
        self.otherGenResLbl.setObjectName(u"otherGenResLbl")
        self.otherGenResLbl.setFont(font2)
        self.otherGenResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.otherGenResLbl, 11, 0, 1, 1)

        self.otherGenResActDsb = QDoubleSpinBox(self.genResWgt)
        self.otherGenResActDsb.setObjectName(u"otherGenResActDsb")
        sizePolicy.setHeightForWidth(self.otherGenResActDsb.sizePolicy().hasHeightForWidth())
        self.otherGenResActDsb.setSizePolicy(sizePolicy)
        self.otherGenResActDsb.setMinimumSize(QSize(110, 0))
        self.otherGenResActDsb.setMaximumSize(QSize(110, 16777215))
        self.otherGenResActDsb.setFont(font1)
        self.otherGenResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.otherGenResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.otherGenResActDsb.setMaximum(999999.989999999990687)
        self.otherGenResActDsb.setSingleStep(0.100000000000000)
        self.otherGenResActDsb.setValue(0.000000000000000)

        self.gridLayout_4.addWidget(self.otherGenResActDsb, 11, 1, 1, 1)

        self.solarGenResLbl = QLabel(self.genResWgt)
        self.solarGenResLbl.setObjectName(u"solarGenResLbl")
        self.solarGenResLbl.setFont(font2)
        self.solarGenResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.solarGenResLbl, 5, 0, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_19, 10, 0, 1, 1)

        self.actGenLbl = QLabel(self.genResWgt)
        self.actGenLbl.setObjectName(u"actGenLbl")
        sizePolicy1.setHeightForWidth(self.actGenLbl.sizePolicy().hasHeightForWidth())
        self.actGenLbl.setSizePolicy(sizePolicy1)
        self.actGenLbl.setMinimumSize(QSize(110, 0))
        self.actGenLbl.setMaximumSize(QSize(110, 16777215))
        self.actGenLbl.setFont(font7)
        self.actGenLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.actGenLbl, 0, 1, 1, 1)

        self.otherGenResPerspDsb = QDoubleSpinBox(self.genResWgt)
        self.otherGenResPerspDsb.setObjectName(u"otherGenResPerspDsb")
        sizePolicy.setHeightForWidth(self.otherGenResPerspDsb.sizePolicy().hasHeightForWidth())
        self.otherGenResPerspDsb.setSizePolicy(sizePolicy)
        self.otherGenResPerspDsb.setMinimumSize(QSize(110, 0))
        self.otherGenResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.otherGenResPerspDsb.setFont(font1)
        self.otherGenResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.otherGenResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.otherGenResPerspDsb.setMaximum(999999.989999999990687)
        self.otherGenResPerspDsb.setSingleStep(0.100000000000000)
        self.otherGenResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_4.addWidget(self.otherGenResPerspDsb, 11, 2, 1, 1)


        self.verticalLayout.addWidget(self.genResWgt)

        self.overgenResWgt = QWidget(self.centerWgt)
        self.overgenResWgt.setObjectName(u"overgenResWgt")
        self.overgenResWgt.setMaximumSize(QSize(16777215, 16777215))
        self.overgenResWgt.setStyleSheet(u"background-color: rgb(39, 39, 0);")
        self.gridLayout_7 = QGridLayout(self.overgenResWgt)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.perspOvergenLbl = QLabel(self.overgenResWgt)
        self.perspOvergenLbl.setObjectName(u"perspOvergenLbl")
        sizePolicy1.setHeightForWidth(self.perspOvergenLbl.sizePolicy().hasHeightForWidth())
        self.perspOvergenLbl.setSizePolicy(sizePolicy1)
        self.perspOvergenLbl.setMinimumSize(QSize(110, 0))
        self.perspOvergenLbl.setMaximumSize(QSize(110, 16777215))
        self.perspOvergenLbl.setFont(font7)
        self.perspOvergenLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.perspOvergenLbl, 0, 2, 1, 1)

        self.hiOvergenResActDsb = QDoubleSpinBox(self.overgenResWgt)
        self.hiOvergenResActDsb.setObjectName(u"hiOvergenResActDsb")
        sizePolicy.setHeightForWidth(self.hiOvergenResActDsb.sizePolicy().hasHeightForWidth())
        self.hiOvergenResActDsb.setSizePolicy(sizePolicy)
        self.hiOvergenResActDsb.setMinimumSize(QSize(110, 0))
        self.hiOvergenResActDsb.setMaximumSize(QSize(110, 16777215))
        self.hiOvergenResActDsb.setFont(font4)
        self.hiOvergenResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.hiOvergenResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.hiOvergenResActDsb.setMaximum(999999.989999999990687)
        self.hiOvergenResActDsb.setSingleStep(0.100000000000000)
        self.hiOvergenResActDsb.setValue(0.000000000000000)

        self.gridLayout_7.addWidget(self.hiOvergenResActDsb, 2, 1, 1, 1)

        self.hiOvergenResLbl = QLabel(self.overgenResWgt)
        self.hiOvergenResLbl.setObjectName(u"hiOvergenResLbl")
        self.hiOvergenResLbl.setFont(font5)
        self.hiOvergenResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.hiOvergenResLbl, 2, 0, 1, 1)

        self.verticalSpacer_38 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_38, 1, 0, 1, 1)

        self.actOvergenResLbl = QLabel(self.overgenResWgt)
        self.actOvergenResLbl.setObjectName(u"actOvergenResLbl")
        sizePolicy1.setHeightForWidth(self.actOvergenResLbl.sizePolicy().hasHeightForWidth())
        self.actOvergenResLbl.setSizePolicy(sizePolicy1)
        self.actOvergenResLbl.setMinimumSize(QSize(110, 0))
        self.actOvergenResLbl.setMaximumSize(QSize(110, 16777215))
        self.actOvergenResLbl.setFont(font7)
        self.actOvergenResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.actOvergenResLbl, 0, 1, 1, 1)

        self.lowOvergenResLbl = QLabel(self.overgenResWgt)
        self.lowOvergenResLbl.setObjectName(u"lowOvergenResLbl")
        self.lowOvergenResLbl.setFont(font5)
        self.lowOvergenResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.lowOvergenResLbl, 3, 0, 1, 1)

        self.lowOvergenResActDsb = QDoubleSpinBox(self.overgenResWgt)
        self.lowOvergenResActDsb.setObjectName(u"lowOvergenResActDsb")
        sizePolicy.setHeightForWidth(self.lowOvergenResActDsb.sizePolicy().hasHeightForWidth())
        self.lowOvergenResActDsb.setSizePolicy(sizePolicy)
        self.lowOvergenResActDsb.setMinimumSize(QSize(110, 0))
        self.lowOvergenResActDsb.setMaximumSize(QSize(110, 16777215))
        self.lowOvergenResActDsb.setFont(font1)
        self.lowOvergenResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lowOvergenResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.lowOvergenResActDsb.setMaximum(999999.989999999990687)
        self.lowOvergenResActDsb.setSingleStep(0.100000000000000)
        self.lowOvergenResActDsb.setValue(0.000000000000000)

        self.gridLayout_7.addWidget(self.lowOvergenResActDsb, 3, 1, 1, 1)

        self.lowOvergenResPerspDsb = QDoubleSpinBox(self.overgenResWgt)
        self.lowOvergenResPerspDsb.setObjectName(u"lowOvergenResPerspDsb")
        sizePolicy.setHeightForWidth(self.lowOvergenResPerspDsb.sizePolicy().hasHeightForWidth())
        self.lowOvergenResPerspDsb.setSizePolicy(sizePolicy)
        self.lowOvergenResPerspDsb.setMinimumSize(QSize(110, 0))
        self.lowOvergenResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.lowOvergenResPerspDsb.setFont(font1)
        self.lowOvergenResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lowOvergenResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.lowOvergenResPerspDsb.setMaximum(999999.989999999990687)
        self.lowOvergenResPerspDsb.setSingleStep(0.100000000000000)
        self.lowOvergenResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_7.addWidget(self.lowOvergenResPerspDsb, 3, 2, 1, 1)

        self.hiOvergenResPerspDsb = QDoubleSpinBox(self.overgenResWgt)
        self.hiOvergenResPerspDsb.setObjectName(u"hiOvergenResPerspDsb")
        sizePolicy.setHeightForWidth(self.hiOvergenResPerspDsb.sizePolicy().hasHeightForWidth())
        self.hiOvergenResPerspDsb.setSizePolicy(sizePolicy)
        self.hiOvergenResPerspDsb.setMinimumSize(QSize(110, 0))
        self.hiOvergenResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.hiOvergenResPerspDsb.setFont(font4)
        self.hiOvergenResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.hiOvergenResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.hiOvergenResPerspDsb.setMaximum(999999.989999999990687)
        self.hiOvergenResPerspDsb.setSingleStep(0.100000000000000)
        self.hiOvergenResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_7.addWidget(self.hiOvergenResPerspDsb, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.overgenResWgt)

        self.capResWgt = QWidget(self.centerWgt)
        self.capResWgt.setObjectName(u"capResWgt")
        self.capResWgt.setMaximumSize(QSize(16777215, 16777215))
        self.capResWgt.setStyleSheet(u"background-color: rgb(47, 47, 0);")
        self.gridLayout_5 = QGridLayout(self.capResWgt)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.otherCapPercResPerspDsb = QDoubleSpinBox(self.capResWgt)
        self.otherCapPercResPerspDsb.setObjectName(u"otherCapPercResPerspDsb")
        sizePolicy.setHeightForWidth(self.otherCapPercResPerspDsb.sizePolicy().hasHeightForWidth())
        self.otherCapPercResPerspDsb.setSizePolicy(sizePolicy)
        self.otherCapPercResPerspDsb.setMinimumSize(QSize(110, 0))
        self.otherCapPercResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.otherCapPercResPerspDsb.setFont(font1)
        self.otherCapPercResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.otherCapPercResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.otherCapPercResPerspDsb.setMaximum(100.000000000000000)
        self.otherCapPercResPerspDsb.setSingleStep(0.100000000000000)
        self.otherCapPercResPerspDsb.setValue(12.000000000000000)

        self.gridLayout_5.addWidget(self.otherCapPercResPerspDsb, 12, 2, 1, 1)

        self.windCapResPerspDsb = QDoubleSpinBox(self.capResWgt)
        self.windCapResPerspDsb.setObjectName(u"windCapResPerspDsb")
        sizePolicy.setHeightForWidth(self.windCapResPerspDsb.sizePolicy().hasHeightForWidth())
        self.windCapResPerspDsb.setSizePolicy(sizePolicy)
        self.windCapResPerspDsb.setMinimumSize(QSize(110, 0))
        self.windCapResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.windCapResPerspDsb.setFont(font1)
        self.windCapResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.windCapResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.windCapResPerspDsb.setMaximum(999999.989999999990687)
        self.windCapResPerspDsb.setSingleStep(0.100000000000000)
        self.windCapResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_5.addWidget(self.windCapResPerspDsb, 8, 2, 1, 1)

        self.windCapPercResPerspDsb = QDoubleSpinBox(self.capResWgt)
        self.windCapPercResPerspDsb.setObjectName(u"windCapPercResPerspDsb")
        sizePolicy.setHeightForWidth(self.windCapPercResPerspDsb.sizePolicy().hasHeightForWidth())
        self.windCapPercResPerspDsb.setSizePolicy(sizePolicy)
        self.windCapPercResPerspDsb.setMinimumSize(QSize(110, 0))
        self.windCapPercResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.windCapPercResPerspDsb.setFont(font1)
        self.windCapPercResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.windCapPercResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.windCapPercResPerspDsb.setMaximum(100.000000000000000)
        self.windCapPercResPerspDsb.setSingleStep(0.100000000000000)
        self.windCapPercResPerspDsb.setValue(12.000000000000000)

        self.gridLayout_5.addWidget(self.windCapPercResPerspDsb, 9, 2, 1, 1)

        self.solarCapPercResPerspDsb = QDoubleSpinBox(self.capResWgt)
        self.solarCapPercResPerspDsb.setObjectName(u"solarCapPercResPerspDsb")
        sizePolicy.setHeightForWidth(self.solarCapPercResPerspDsb.sizePolicy().hasHeightForWidth())
        self.solarCapPercResPerspDsb.setSizePolicy(sizePolicy)
        self.solarCapPercResPerspDsb.setMinimumSize(QSize(110, 0))
        self.solarCapPercResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.solarCapPercResPerspDsb.setFont(font1)
        self.solarCapPercResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.solarCapPercResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.solarCapPercResPerspDsb.setMaximum(100.000000000000000)
        self.solarCapPercResPerspDsb.setSingleStep(0.100000000000000)
        self.solarCapPercResPerspDsb.setValue(12.000000000000000)

        self.gridLayout_5.addWidget(self.solarCapPercResPerspDsb, 6, 2, 1, 1)

        self.actualLbl_3 = QLabel(self.capResWgt)
        self.actualLbl_3.setObjectName(u"actualLbl_3")
        sizePolicy1.setHeightForWidth(self.actualLbl_3.sizePolicy().hasHeightForWidth())
        self.actualLbl_3.setSizePolicy(sizePolicy1)
        self.actualLbl_3.setMinimumSize(QSize(110, 0))
        self.actualLbl_3.setMaximumSize(QSize(110, 16777215))
        self.actualLbl_3.setFont(font7)
        self.actualLbl_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.actualLbl_3, 1, 1, 1, 1)

        self.otherCapResLbl = QLabel(self.capResWgt)
        self.otherCapResLbl.setObjectName(u"otherCapResLbl")
        self.otherCapResLbl.setFont(font2)
        self.otherCapResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.otherCapResLbl, 11, 0, 1, 1)

        self.solarCapResLbl = QLabel(self.capResWgt)
        self.solarCapResLbl.setObjectName(u"solarCapResLbl")
        self.solarCapResLbl.setFont(font2)
        self.solarCapResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.solarCapResLbl, 5, 0, 1, 1)

        self.otherCapResActDsb = QDoubleSpinBox(self.capResWgt)
        self.otherCapResActDsb.setObjectName(u"otherCapResActDsb")
        sizePolicy.setHeightForWidth(self.otherCapResActDsb.sizePolicy().hasHeightForWidth())
        self.otherCapResActDsb.setSizePolicy(sizePolicy)
        self.otherCapResActDsb.setMinimumSize(QSize(110, 0))
        self.otherCapResActDsb.setMaximumSize(QSize(110, 16777215))
        self.otherCapResActDsb.setFont(font1)
        self.otherCapResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.otherCapResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.otherCapResActDsb.setMaximum(999999.989999999990687)
        self.otherCapResActDsb.setSingleStep(0.100000000000000)
        self.otherCapResActDsb.setValue(0.000000000000000)

        self.gridLayout_5.addWidget(self.otherCapResActDsb, 11, 1, 1, 1)

        self.solarCapResPerspDsb = QDoubleSpinBox(self.capResWgt)
        self.solarCapResPerspDsb.setObjectName(u"solarCapResPerspDsb")
        sizePolicy.setHeightForWidth(self.solarCapResPerspDsb.sizePolicy().hasHeightForWidth())
        self.solarCapResPerspDsb.setSizePolicy(sizePolicy)
        self.solarCapResPerspDsb.setMinimumSize(QSize(110, 0))
        self.solarCapResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.solarCapResPerspDsb.setFont(font1)
        self.solarCapResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.solarCapResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.solarCapResPerspDsb.setMaximum(999999.989999999990687)
        self.solarCapResPerspDsb.setSingleStep(0.100000000000000)
        self.solarCapResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_5.addWidget(self.solarCapResPerspDsb, 5, 2, 1, 1)

        self.otherCapPercResActDsb = QDoubleSpinBox(self.capResWgt)
        self.otherCapPercResActDsb.setObjectName(u"otherCapPercResActDsb")
        sizePolicy.setHeightForWidth(self.otherCapPercResActDsb.sizePolicy().hasHeightForWidth())
        self.otherCapPercResActDsb.setSizePolicy(sizePolicy)
        self.otherCapPercResActDsb.setMinimumSize(QSize(110, 0))
        self.otherCapPercResActDsb.setMaximumSize(QSize(110, 16777215))
        self.otherCapPercResActDsb.setFont(font1)
        self.otherCapPercResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.otherCapPercResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.otherCapPercResActDsb.setMaximum(100.000000000000000)
        self.otherCapPercResActDsb.setSingleStep(0.100000000000000)
        self.otherCapPercResActDsb.setValue(12.000000000000000)

        self.gridLayout_5.addWidget(self.otherCapPercResActDsb, 12, 1, 1, 1)

        self.ferCapResLbl = QLabel(self.capResWgt)
        self.ferCapResLbl.setObjectName(u"ferCapResLbl")
        self.ferCapResLbl.setFont(font5)
        self.ferCapResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.ferCapResLbl, 3, 0, 1, 1)

        self.ferCapResActDsb = QDoubleSpinBox(self.capResWgt)
        self.ferCapResActDsb.setObjectName(u"ferCapResActDsb")
        sizePolicy.setHeightForWidth(self.ferCapResActDsb.sizePolicy().hasHeightForWidth())
        self.ferCapResActDsb.setSizePolicy(sizePolicy)
        self.ferCapResActDsb.setMinimumSize(QSize(110, 0))
        self.ferCapResActDsb.setMaximumSize(QSize(110, 16777215))
        self.ferCapResActDsb.setFont(font4)
        self.ferCapResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ferCapResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ferCapResActDsb.setMaximum(999999.989999999990687)
        self.ferCapResActDsb.setSingleStep(0.100000000000000)
        self.ferCapResActDsb.setValue(0.000000000000000)

        self.gridLayout_5.addWidget(self.ferCapResActDsb, 3, 1, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_20, 10, 0, 1, 1)

        self.ferCapResPerspDsb = QDoubleSpinBox(self.capResWgt)
        self.ferCapResPerspDsb.setObjectName(u"ferCapResPerspDsb")
        sizePolicy.setHeightForWidth(self.ferCapResPerspDsb.sizePolicy().hasHeightForWidth())
        self.ferCapResPerspDsb.setSizePolicy(sizePolicy)
        self.ferCapResPerspDsb.setMinimumSize(QSize(110, 0))
        self.ferCapResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.ferCapResPerspDsb.setFont(font4)
        self.ferCapResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ferCapResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ferCapResPerspDsb.setMaximum(999999.989999999990687)
        self.ferCapResPerspDsb.setSingleStep(0.100000000000000)
        self.ferCapResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_5.addWidget(self.ferCapResPerspDsb, 3, 2, 1, 1)

        self.solarCapPercResActDsb = QDoubleSpinBox(self.capResWgt)
        self.solarCapPercResActDsb.setObjectName(u"solarCapPercResActDsb")
        sizePolicy.setHeightForWidth(self.solarCapPercResActDsb.sizePolicy().hasHeightForWidth())
        self.solarCapPercResActDsb.setSizePolicy(sizePolicy)
        self.solarCapPercResActDsb.setMinimumSize(QSize(110, 0))
        self.solarCapPercResActDsb.setMaximumSize(QSize(110, 16777215))
        self.solarCapPercResActDsb.setFont(font1)
        self.solarCapPercResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.solarCapPercResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.solarCapPercResActDsb.setMaximum(100.000000000000000)
        self.solarCapPercResActDsb.setSingleStep(0.100000000000000)
        self.solarCapPercResActDsb.setValue(12.000000000000000)

        self.gridLayout_5.addWidget(self.solarCapPercResActDsb, 6, 1, 1, 1)

        self.windCapResLbl = QLabel(self.capResWgt)
        self.windCapResLbl.setObjectName(u"windCapResLbl")
        self.windCapResLbl.setFont(font2)
        self.windCapResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.windCapResLbl, 8, 0, 1, 1)

        self.verticalSpacer_30 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_30, 7, 0, 1, 1)

        self.windCapPercResActDsb = QDoubleSpinBox(self.capResWgt)
        self.windCapPercResActDsb.setObjectName(u"windCapPercResActDsb")
        sizePolicy.setHeightForWidth(self.windCapPercResActDsb.sizePolicy().hasHeightForWidth())
        self.windCapPercResActDsb.setSizePolicy(sizePolicy)
        self.windCapPercResActDsb.setMinimumSize(QSize(110, 0))
        self.windCapPercResActDsb.setMaximumSize(QSize(110, 16777215))
        self.windCapPercResActDsb.setFont(font1)
        self.windCapPercResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.windCapPercResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.windCapPercResActDsb.setMaximum(100.000000000000000)
        self.windCapPercResActDsb.setSingleStep(0.100000000000000)
        self.windCapPercResActDsb.setValue(12.000000000000000)

        self.gridLayout_5.addWidget(self.windCapPercResActDsb, 9, 1, 1, 1)

        self.verticalSpacer_31 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_31, 4, 0, 1, 1)

        self.solarCapResActDsb = QDoubleSpinBox(self.capResWgt)
        self.solarCapResActDsb.setObjectName(u"solarCapResActDsb")
        sizePolicy.setHeightForWidth(self.solarCapResActDsb.sizePolicy().hasHeightForWidth())
        self.solarCapResActDsb.setSizePolicy(sizePolicy)
        self.solarCapResActDsb.setMinimumSize(QSize(110, 0))
        self.solarCapResActDsb.setMaximumSize(QSize(110, 16777215))
        self.solarCapResActDsb.setFont(font1)
        self.solarCapResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.solarCapResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.solarCapResActDsb.setMaximum(999999.989999999990687)
        self.solarCapResActDsb.setSingleStep(0.100000000000000)
        self.solarCapResActDsb.setValue(0.000000000000000)

        self.gridLayout_5.addWidget(self.solarCapResActDsb, 5, 1, 1, 1)

        self.windCapResActDsb = QDoubleSpinBox(self.capResWgt)
        self.windCapResActDsb.setObjectName(u"windCapResActDsb")
        sizePolicy.setHeightForWidth(self.windCapResActDsb.sizePolicy().hasHeightForWidth())
        self.windCapResActDsb.setSizePolicy(sizePolicy)
        self.windCapResActDsb.setMinimumSize(QSize(110, 0))
        self.windCapResActDsb.setMaximumSize(QSize(110, 16777215))
        self.windCapResActDsb.setFont(font1)
        self.windCapResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.windCapResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.windCapResActDsb.setMaximum(999999.989999999990687)
        self.windCapResActDsb.setSingleStep(0.100000000000000)
        self.windCapResActDsb.setValue(0.000000000000000)

        self.gridLayout_5.addWidget(self.windCapResActDsb, 8, 1, 1, 1)

        self.otherCapResPerspDsb = QDoubleSpinBox(self.capResWgt)
        self.otherCapResPerspDsb.setObjectName(u"otherCapResPerspDsb")
        sizePolicy.setHeightForWidth(self.otherCapResPerspDsb.sizePolicy().hasHeightForWidth())
        self.otherCapResPerspDsb.setSizePolicy(sizePolicy)
        self.otherCapResPerspDsb.setMinimumSize(QSize(110, 0))
        self.otherCapResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.otherCapResPerspDsb.setFont(font1)
        self.otherCapResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.otherCapResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.otherCapResPerspDsb.setMaximum(999999.989999999990687)
        self.otherCapResPerspDsb.setSingleStep(0.100000000000000)
        self.otherCapResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_5.addWidget(self.otherCapResPerspDsb, 11, 2, 1, 1)

        self.perspectLbl_3 = QLabel(self.capResWgt)
        self.perspectLbl_3.setObjectName(u"perspectLbl_3")
        sizePolicy1.setHeightForWidth(self.perspectLbl_3.sizePolicy().hasHeightForWidth())
        self.perspectLbl_3.setSizePolicy(sizePolicy1)
        self.perspectLbl_3.setMinimumSize(QSize(110, 0))
        self.perspectLbl_3.setMaximumSize(QSize(110, 16777215))
        self.perspectLbl_3.setFont(font7)
        self.perspectLbl_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.perspectLbl_3, 1, 2, 1, 1)

        self.verticalSpacer_34 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_34, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.capResWgt)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_12)

        self.verticalSpacer_29 = QSpacerItem(10, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_29)


        self.resultsHL.addWidget(self.centerWgt)

        self.centerWgt_2 = QWidget(self.resultsWgt)
        self.centerWgt_2.setObjectName(u"centerWgt_2")
        self.centerWgt_2.setMaximumSize(QSize(450, 16777215))
        self.centerWgt_2.setStyleSheet(u"*{}\n"
"\n"
"QWidget{\n"
"	border-radius: 10px\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.centerWgt_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.storResLbl = QLabel(self.centerWgt_2)
        self.storResLbl.setObjectName(u"storResLbl")
        self.storResLbl.setMinimumSize(QSize(0, 30))
        self.storResLbl.setFont(font)
        self.storResLbl.setStyleSheet(u"border: solid;\n"
"border-radius: 10px;\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.storResLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.storResLbl)

        self.storResWgt = QWidget(self.centerWgt_2)
        self.storResWgt.setObjectName(u"storResWgt")
        self.storResWgt.setMaximumSize(QSize(16777215, 16777215))
        self.storResWgt.setStyleSheet(u"background-color: rgb(23, 23, 0);")
        self.gridLayout_8 = QGridLayout(self.storResWgt)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.perspStorLbl = QLabel(self.storResWgt)
        self.perspStorLbl.setObjectName(u"perspStorLbl")
        sizePolicy1.setHeightForWidth(self.perspStorLbl.sizePolicy().hasHeightForWidth())
        self.perspStorLbl.setSizePolicy(sizePolicy1)
        self.perspStorLbl.setMinimumSize(QSize(110, 0))
        self.perspStorLbl.setMaximumSize(QSize(110, 16777215))
        self.perspStorLbl.setFont(font7)
        self.perspStorLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.perspStorLbl, 1, 1, 1, 1)

        self.verticalSpacer_36 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_36, 2, 0, 1, 1)

        self.sysStorResLbl = QLabel(self.storResWgt)
        self.sysStorResLbl.setObjectName(u"sysStorResLbl")
        sizePolicy2.setHeightForWidth(self.sysStorResLbl.sizePolicy().hasHeightForWidth())
        self.sysStorResLbl.setSizePolicy(sizePolicy2)
        self.sysStorResLbl.setFont(font2)
        self.sysStorResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.sysStorResLbl, 3, 0, 1, 1)

        self.sysStorResPerspDsb = QDoubleSpinBox(self.storResWgt)
        self.sysStorResPerspDsb.setObjectName(u"sysStorResPerspDsb")
        sizePolicy.setHeightForWidth(self.sysStorResPerspDsb.sizePolicy().hasHeightForWidth())
        self.sysStorResPerspDsb.setSizePolicy(sizePolicy)
        self.sysStorResPerspDsb.setMinimumSize(QSize(110, 0))
        self.sysStorResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.sysStorResPerspDsb.setFont(font1)
        self.sysStorResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sysStorResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sysStorResPerspDsb.setMaximum(999999.989999999990687)
        self.sysStorResPerspDsb.setSingleStep(0.100000000000000)
        self.sysStorResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_8.addWidget(self.sysStorResPerspDsb, 3, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.storResWgt)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_13)

        self.h2ResLbl = QLabel(self.centerWgt_2)
        self.h2ResLbl.setObjectName(u"h2ResLbl")
        self.h2ResLbl.setMinimumSize(QSize(0, 30))
        self.h2ResLbl.setFont(font)
        self.h2ResLbl.setStyleSheet(u"border: solid;\n"
"border-radius: 10px;\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.h2ResLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.h2ResLbl)

        self.h2ResWgt = QWidget(self.centerWgt_2)
        self.h2ResWgt.setObjectName(u"h2ResWgt")
        self.h2ResWgt.setMaximumSize(QSize(16777215, 16777215))
        self.h2ResWgt.setStyleSheet(u"background-color: rgb(31, 31, 0);")
        self.gridLayout_9 = QGridLayout(self.h2ResWgt)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.overgenH2Lbl = QLabel(self.h2ResWgt)
        self.overgenH2Lbl.setObjectName(u"overgenH2Lbl")
        font8 = QFont()
        font8.setPointSize(9)
        font8.setBold(False)
        font8.setItalic(True)
        font8.setWeight(50)
        self.overgenH2Lbl.setFont(font8)
        self.overgenH2Lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.overgenH2Lbl, 1, 0, 1, 1)

        self.toprodHiH2ResPerspDsb = QDoubleSpinBox(self.h2ResWgt)
        self.toprodHiH2ResPerspDsb.setObjectName(u"toprodHiH2ResPerspDsb")
        sizePolicy.setHeightForWidth(self.toprodHiH2ResPerspDsb.sizePolicy().hasHeightForWidth())
        self.toprodHiH2ResPerspDsb.setSizePolicy(sizePolicy)
        self.toprodHiH2ResPerspDsb.setMinimumSize(QSize(110, 0))
        self.toprodHiH2ResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.toprodHiH2ResPerspDsb.setFont(font1)
        self.toprodHiH2ResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.toprodHiH2ResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.toprodHiH2ResPerspDsb.setMaximum(999999.989999999990687)
        self.toprodHiH2ResPerspDsb.setSingleStep(0.100000000000000)
        self.toprodHiH2ResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_9.addWidget(self.toprodHiH2ResPerspDsb, 4, 2, 1, 1)

        self.maxLowH2ResPerspDsb = QDoubleSpinBox(self.h2ResWgt)
        self.maxLowH2ResPerspDsb.setObjectName(u"maxLowH2ResPerspDsb")
        sizePolicy.setHeightForWidth(self.maxLowH2ResPerspDsb.sizePolicy().hasHeightForWidth())
        self.maxLowH2ResPerspDsb.setSizePolicy(sizePolicy)
        self.maxLowH2ResPerspDsb.setMinimumSize(QSize(110, 0))
        self.maxLowH2ResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.maxLowH2ResPerspDsb.setFont(font1)
        self.maxLowH2ResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.maxLowH2ResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.maxLowH2ResPerspDsb.setMaximum(999999.989999999990687)
        self.maxLowH2ResPerspDsb.setSingleStep(0.100000000000000)
        self.maxLowH2ResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_9.addWidget(self.maxLowH2ResPerspDsb, 3, 3, 1, 1)

        self.maxHiH2ResPerspDsb = QDoubleSpinBox(self.h2ResWgt)
        self.maxHiH2ResPerspDsb.setObjectName(u"maxHiH2ResPerspDsb")
        sizePolicy.setHeightForWidth(self.maxHiH2ResPerspDsb.sizePolicy().hasHeightForWidth())
        self.maxHiH2ResPerspDsb.setSizePolicy(sizePolicy)
        self.maxHiH2ResPerspDsb.setMinimumSize(QSize(110, 0))
        self.maxHiH2ResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.maxHiH2ResPerspDsb.setFont(font1)
        self.maxHiH2ResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.maxHiH2ResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.maxHiH2ResPerspDsb.setMaximum(999999.989999999990687)
        self.maxHiH2ResPerspDsb.setSingleStep(0.100000000000000)
        self.maxHiH2ResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_9.addWidget(self.maxHiH2ResPerspDsb, 3, 2, 1, 1)

        self.overgenLowH2Lbl = QLabel(self.h2ResWgt)
        self.overgenLowH2Lbl.setObjectName(u"overgenLowH2Lbl")
        self.overgenLowH2Lbl.setMinimumSize(QSize(110, 0))
        self.overgenLowH2Lbl.setMaximumSize(QSize(110, 16777215))
        self.overgenLowH2Lbl.setFont(font8)
        self.overgenLowH2Lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.overgenLowH2Lbl, 1, 3, 1, 1)

        self.toprodHiH2ResLbl = QLabel(self.h2ResWgt)
        self.toprodHiH2ResLbl.setObjectName(u"toprodHiH2ResLbl")
        self.toprodHiH2ResLbl.setFont(font6)
        self.toprodHiH2ResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.toprodHiH2ResLbl, 4, 0, 1, 1)

        self.maxHiH2ResLbl = QLabel(self.h2ResWgt)
        self.maxHiH2ResLbl.setObjectName(u"maxHiH2ResLbl")
        self.maxHiH2ResLbl.setFont(font6)
        self.maxHiH2ResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.maxHiH2ResLbl, 3, 0, 1, 1)

        self.toprodLowH2ResPerspDsb = QDoubleSpinBox(self.h2ResWgt)
        self.toprodLowH2ResPerspDsb.setObjectName(u"toprodLowH2ResPerspDsb")
        sizePolicy.setHeightForWidth(self.toprodLowH2ResPerspDsb.sizePolicy().hasHeightForWidth())
        self.toprodLowH2ResPerspDsb.setSizePolicy(sizePolicy)
        self.toprodLowH2ResPerspDsb.setMinimumSize(QSize(110, 0))
        self.toprodLowH2ResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.toprodLowH2ResPerspDsb.setFont(font1)
        self.toprodLowH2ResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.toprodLowH2ResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.toprodLowH2ResPerspDsb.setMaximum(999999.989999999990687)
        self.toprodLowH2ResPerspDsb.setSingleStep(0.100000000000000)
        self.toprodLowH2ResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_9.addWidget(self.toprodLowH2ResPerspDsb, 4, 3, 1, 1)

        self.overgenHiH2Lbl = QLabel(self.h2ResWgt)
        self.overgenHiH2Lbl.setObjectName(u"overgenHiH2Lbl")
        self.overgenHiH2Lbl.setMinimumSize(QSize(110, 0))
        self.overgenHiH2Lbl.setMaximumSize(QSize(110, 16777215))
        self.overgenHiH2Lbl.setFont(font8)
        self.overgenHiH2Lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.overgenHiH2Lbl, 1, 2, 1, 1)

        self.verticalSpacer_40 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_40, 2, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.h2ResWgt)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_15)

        self.costsResLbl = QLabel(self.centerWgt_2)
        self.costsResLbl.setObjectName(u"costsResLbl")
        self.costsResLbl.setMinimumSize(QSize(0, 30))
        self.costsResLbl.setFont(font)
        self.costsResLbl.setStyleSheet(u"border: solid;\n"
"border-radius: 10px;\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.costsResLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.costsResLbl)

        self.costsResWgt = QWidget(self.centerWgt_2)
        self.costsResWgt.setObjectName(u"costsResWgt")
        self.costsResWgt.setMaximumSize(QSize(16777215, 16777215))
        self.costsResWgt.setStyleSheet(u"background-color: rgb(31, 31, 0);")
        self.gridLayout_10 = QGridLayout(self.costsResWgt)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frnpCostsResLbl = QLabel(self.costsResWgt)
        self.frnpCostsResLbl.setObjectName(u"frnpCostsResLbl")
        self.frnpCostsResLbl.setFont(font5)
        self.frnpCostsResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.frnpCostsResLbl, 2, 0, 1, 1)

        self.h2CostsResPerspDsb = QDoubleSpinBox(self.costsResWgt)
        self.h2CostsResPerspDsb.setObjectName(u"h2CostsResPerspDsb")
        sizePolicy.setHeightForWidth(self.h2CostsResPerspDsb.sizePolicy().hasHeightForWidth())
        self.h2CostsResPerspDsb.setSizePolicy(sizePolicy)
        self.h2CostsResPerspDsb.setMinimumSize(QSize(110, 0))
        self.h2CostsResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.h2CostsResPerspDsb.setFont(font1)
        self.h2CostsResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.h2CostsResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.h2CostsResPerspDsb.setDecimals(0)
        self.h2CostsResPerspDsb.setMaximum(999999999999999.000000000000000)
        self.h2CostsResPerspDsb.setSingleStep(0.100000000000000)
        self.h2CostsResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_10.addWidget(self.h2CostsResPerspDsb, 4, 1, 1, 1)

        self.capexCostsResPerspDsb = QDoubleSpinBox(self.costsResWgt)
        self.capexCostsResPerspDsb.setObjectName(u"capexCostsResPerspDsb")
        sizePolicy.setHeightForWidth(self.capexCostsResPerspDsb.sizePolicy().hasHeightForWidth())
        self.capexCostsResPerspDsb.setSizePolicy(sizePolicy)
        self.capexCostsResPerspDsb.setMinimumSize(QSize(110, 0))
        self.capexCostsResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.capexCostsResPerspDsb.setFont(font1)
        self.capexCostsResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.capexCostsResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.capexCostsResPerspDsb.setDecimals(0)
        self.capexCostsResPerspDsb.setMaximum(999999999999999.000000000000000)
        self.capexCostsResPerspDsb.setSingleStep(0.100000000000000)
        self.capexCostsResPerspDsb.setValue(0.000000000000000)

        self.gridLayout_10.addWidget(self.capexCostsResPerspDsb, 3, 1, 1, 1)

        self.h2CostsResLbl = QLabel(self.costsResWgt)
        self.h2CostsResLbl.setObjectName(u"h2CostsResLbl")
        self.h2CostsResLbl.setFont(font5)
        self.h2CostsResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.h2CostsResLbl, 4, 0, 1, 1)

        self.capexCostsResLbl = QLabel(self.costsResWgt)
        self.capexCostsResLbl.setObjectName(u"capexCostsResLbl")
        self.capexCostsResLbl.setFont(font5)
        self.capexCostsResLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.capexCostsResLbl, 3, 0, 1, 1)

        self.frnpCostsResPerspDsb = QDoubleSpinBox(self.costsResWgt)
        self.frnpCostsResPerspDsb.setObjectName(u"frnpCostsResPerspDsb")
        sizePolicy.setHeightForWidth(self.frnpCostsResPerspDsb.sizePolicy().hasHeightForWidth())
        self.frnpCostsResPerspDsb.setSizePolicy(sizePolicy)
        self.frnpCostsResPerspDsb.setMinimumSize(QSize(110, 0))
        self.frnpCostsResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.frnpCostsResPerspDsb.setFont(font4)
        self.frnpCostsResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frnpCostsResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.frnpCostsResPerspDsb.setDecimals(0)
        self.frnpCostsResPerspDsb.setMaximum(999999999999999.000000000000000)
        self.frnpCostsResPerspDsb.setSingleStep(0.100000000000000)
        self.frnpCostsResPerspDsb.setValue(1000000.000000000000000)

        self.gridLayout_10.addWidget(self.frnpCostsResPerspDsb, 2, 1, 1, 1)

        self.verticalSpacer_41 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_10.addItem(self.verticalSpacer_41, 1, 0, 1, 1)

        self.perspCostsLbl = QLabel(self.costsResWgt)
        self.perspCostsLbl.setObjectName(u"perspCostsLbl")
        sizePolicy1.setHeightForWidth(self.perspCostsLbl.sizePolicy().hasHeightForWidth())
        self.perspCostsLbl.setSizePolicy(sizePolicy1)
        self.perspCostsLbl.setMinimumSize(QSize(110, 0))
        self.perspCostsLbl.setMaximumSize(QSize(110, 16777215))
        self.perspCostsLbl.setFont(font7)
        self.perspCostsLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.perspCostsLbl, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.costsResWgt)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_14)

        self.inputLbl_7 = QLabel(self.centerWgt_2)
        self.inputLbl_7.setObjectName(u"inputLbl_7")
        self.inputLbl_7.setMinimumSize(QSize(0, 30))
        self.inputLbl_7.setFont(font)
        self.inputLbl_7.setStyleSheet(u"border: solid;\n"
"border-radius: 10px;\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.inputLbl_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.inputLbl_7)

        self.emisResWgt = QWidget(self.centerWgt_2)
        self.emisResWgt.setObjectName(u"emisResWgt")
        self.emisResWgt.setMaximumSize(QSize(16777215, 16777215))
        self.emisResWgt.setStyleSheet(u"background-color: rgb(63, 63, 0);")
        self.gridLayout_6 = QGridLayout(self.emisResWgt)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.actualLbl_4 = QLabel(self.emisResWgt)
        self.actualLbl_4.setObjectName(u"actualLbl_4")
        sizePolicy1.setHeightForWidth(self.actualLbl_4.sizePolicy().hasHeightForWidth())
        self.actualLbl_4.setSizePolicy(sizePolicy1)
        self.actualLbl_4.setMinimumSize(QSize(110, 0))
        self.actualLbl_4.setMaximumSize(QSize(110, 16777215))
        self.actualLbl_4.setFont(font7)
        self.actualLbl_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.actualLbl_4, 0, 1, 1, 1)

        self.perspectLbl_4 = QLabel(self.emisResWgt)
        self.perspectLbl_4.setObjectName(u"perspectLbl_4")
        sizePolicy1.setHeightForWidth(self.perspectLbl_4.sizePolicy().hasHeightForWidth())
        self.perspectLbl_4.setSizePolicy(sizePolicy1)
        self.perspectLbl_4.setMinimumSize(QSize(110, 0))
        self.perspectLbl_4.setMaximumSize(QSize(110, 16777215))
        self.perspectLbl_4.setFont(font7)
        self.perspectLbl_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.perspectLbl_4, 0, 2, 1, 1)

        self.co2EmisResActLbl = QLabel(self.emisResWgt)
        self.co2EmisResActLbl.setObjectName(u"co2EmisResActLbl")
        self.co2EmisResActLbl.setFont(font5)
        self.co2EmisResActLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.co2EmisResActLbl, 2, 0, 1, 1)

        self.co2EmisResActDsb = QDoubleSpinBox(self.emisResWgt)
        self.co2EmisResActDsb.setObjectName(u"co2EmisResActDsb")
        sizePolicy.setHeightForWidth(self.co2EmisResActDsb.sizePolicy().hasHeightForWidth())
        self.co2EmisResActDsb.setSizePolicy(sizePolicy)
        self.co2EmisResActDsb.setMinimumSize(QSize(110, 0))
        self.co2EmisResActDsb.setMaximumSize(QSize(110, 16777215))
        self.co2EmisResActDsb.setFont(font4)
        self.co2EmisResActDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.co2EmisResActDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.co2EmisResActDsb.setMaximum(999999999.990000009536743)
        self.co2EmisResActDsb.setSingleStep(0.100000000000000)
        self.co2EmisResActDsb.setValue(9.990000000000000)

        self.gridLayout_6.addWidget(self.co2EmisResActDsb, 2, 1, 1, 1)

        self.co2EmisResPerspDsb = QDoubleSpinBox(self.emisResWgt)
        self.co2EmisResPerspDsb.setObjectName(u"co2EmisResPerspDsb")
        sizePolicy.setHeightForWidth(self.co2EmisResPerspDsb.sizePolicy().hasHeightForWidth())
        self.co2EmisResPerspDsb.setSizePolicy(sizePolicy)
        self.co2EmisResPerspDsb.setMinimumSize(QSize(110, 0))
        self.co2EmisResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.co2EmisResPerspDsb.setFont(font4)
        self.co2EmisResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.co2EmisResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.co2EmisResPerspDsb.setMaximum(999999999.990000009536743)
        self.co2EmisResPerspDsb.setSingleStep(0.100000000000000)
        self.co2EmisResPerspDsb.setValue(9.990000000000000)

        self.gridLayout_6.addWidget(self.co2EmisResPerspDsb, 2, 2, 1, 1)

        self.verticalSpacer_33 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_33, 1, 0, 1, 1)

        self.co2EmisRedResPerspLbl = QLabel(self.emisResWgt)
        self.co2EmisRedResPerspLbl.setObjectName(u"co2EmisRedResPerspLbl")
        self.co2EmisRedResPerspLbl.setFont(font5)
        self.co2EmisRedResPerspLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.co2EmisRedResPerspLbl, 3, 0, 1, 1)

        self.co2EmisRedResPerspDsb = QDoubleSpinBox(self.emisResWgt)
        self.co2EmisRedResPerspDsb.setObjectName(u"co2EmisRedResPerspDsb")
        sizePolicy.setHeightForWidth(self.co2EmisRedResPerspDsb.sizePolicy().hasHeightForWidth())
        self.co2EmisRedResPerspDsb.setSizePolicy(sizePolicy)
        self.co2EmisRedResPerspDsb.setMinimumSize(QSize(110, 0))
        self.co2EmisRedResPerspDsb.setMaximumSize(QSize(110, 16777215))
        self.co2EmisRedResPerspDsb.setFont(font4)
        self.co2EmisRedResPerspDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.co2EmisRedResPerspDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.co2EmisRedResPerspDsb.setMaximum(999999999.990000009536743)
        self.co2EmisRedResPerspDsb.setSingleStep(0.100000000000000)
        self.co2EmisRedResPerspDsb.setValue(9.990000000000000)

        self.gridLayout_6.addWidget(self.co2EmisRedResPerspDsb, 3, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.emisResWgt)

        self.verticalSpacer_46 = QSpacerItem(10, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_46)


        self.resultsHL.addWidget(self.centerWgt_2)


        self.optStorHL.addWidget(self.resultsWgt)

        self.horizontalSpacer_4 = QSpacerItem(10, 40, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.optStorHL.addItem(self.horizontalSpacer_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1771, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.inputLbl.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.solarFerInputDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.h2ConsInputDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.ferGenInputDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.solarFerLbl.setText(QCoreApplication.translate("MainWindow", u"Produzione solare su Res", None))
        self.ferGenInputLbl.setText(QCoreApplication.translate("MainWindow", u"Generazione da FER", None))
        self.enConsGrowInputDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.electrLevInputDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.electrLevInputLbl.setText(QCoreApplication.translate("MainWindow", u"Livello di elettrificazione", None))
        self.enConsGrowInputLbl.setText(QCoreApplication.translate("MainWindow", u"Crescita annua dei consumi di energia finale t.m.a.", None))
        self.h2ConsInputLbl.setText(QCoreApplication.translate("MainWindow", u"Consumi per produzione H2", None))
        self.scenTitleLbl.setText(QCoreApplication.translate("MainWindow", u"Scenario", None))
        self.co2EmisScenDsb.setSuffix(QCoreApplication.translate("MainWindow", u" kg", None))
        self.scenLbl.setText(QCoreApplication.translate("MainWindow", u"Scenario", None))
        self.windGenScenDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.solarCapScenPercDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.enImportScenLbl.setText(QCoreApplication.translate("MainWindow", u"Energia importata", None))
        self.enImportScenDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.totEnConsScenLbl.setText(QCoreApplication.translate("MainWindow", u"Consumi finali di energia", None))
        self.scenCb.setItemText(0, QCoreApplication.translate("MainWindow", u"Consuntivo", None))

        self.otherGenScenPercDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.otherCapScenLbl.setText(QCoreApplication.translate("MainWindow", u"di cui Altre fonti", None))
        self.solarCapScenDsb.setSuffix(QCoreApplication.translate("MainWindow", u" GW", None))
        self.solarGenScenDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.ferGenScenPercDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.totEnConsMtepScenDsb.setSuffix(QCoreApplication.translate("MainWindow", u" Mtep", None))
        self.windCapScenLbl.setText(QCoreApplication.translate("MainWindow", u"di cui Eolico", None))
        self.enProdScenDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.enDutyScenLbl.setText(QCoreApplication.translate("MainWindow", u"Fabbisogno di energia elettrica", None))
        self.enDutyScenDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.solarCapScenLbl.setText(QCoreApplication.translate("MainWindow", u"di cui Solalre", None))
        self.windCapScenPercDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.windGenScenPercDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.h2ConsScenDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.otherGenScenDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.enProdScenLbl.setText(QCoreApplication.translate("MainWindow", u"Energia prodotta", None))
        self.ferGenScenDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.windGenScenLbl.setText(QCoreApplication.translate("MainWindow", u"di cui Eolico", None))
        self.yearScenLbl.setText(QCoreApplication.translate("MainWindow", u"Anno Scenario", None))
        self.ferCapScenLbl.setText(QCoreApplication.translate("MainWindow", u"Capacit\u00e0 installata FER", None))
        self.h2ConsScenLbl.setText(QCoreApplication.translate("MainWindow", u"di cui consumi per produrre H2", None))
        self.windCapScenDsb.setSuffix(QCoreApplication.translate("MainWindow", u" GW", None))
        self.otherCapScenPercDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.otherCapScenDsb.setSuffix(QCoreApplication.translate("MainWindow", u" GW", None))
        self.totEnConsScenDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.solarGenScenLbl.setText(QCoreApplication.translate("MainWindow", u"di cui Solare", None))
        self.yearScenCb.setItemText(0, QCoreApplication.translate("MainWindow", u"2019", None))
        self.yearScenCb.setItemText(1, QCoreApplication.translate("MainWindow", u"2040", None))
        self.yearScenCb.setItemText(2, QCoreApplication.translate("MainWindow", u"2040", None))

        self.ferCapScenDsb.setSuffix(QCoreApplication.translate("MainWindow", u" GW", None))
        self.ferGenScenLbl.setText(QCoreApplication.translate("MainWindow", u"Generazione da FER", None))
        self.otherGenScenLbl.setText(QCoreApplication.translate("MainWindow", u"di cui Altre fonti", None))
        self.solarGenScenPercLbl.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.co2EmisScenLbl.setText(QCoreApplication.translate("MainWindow", u"Emissioni di CO2", None))
        self.ferCapScenPercDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.calcPb.setText(QCoreApplication.translate("MainWindow", u"Calcola", None))
        self.duttResLbl.setText(QCoreApplication.translate("MainWindow", u"Fabbisogno", None))
        self.enImportResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.enImportResLbl.setText(QCoreApplication.translate("MainWindow", u"Energia importata", None))
        self.totEnConsResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.perspDutyLbl.setText(QCoreApplication.translate("MainWindow", u"Valori prospettici", None))
        self.actDutyLbl.setText(QCoreApplication.translate("MainWindow", u"Valori attuali", None))
        self.h2ConsResLbl.setText(QCoreApplication.translate("MainWindow", u"di cui consumi per produrre H2", None))
        self.h2ConsResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.totEnConsMtepResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u" Mtep", None))
        self.enDutyResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.enProdResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.totEnConsResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.enDutyResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.enDutyResLbl.setText(QCoreApplication.translate("MainWindow", u"Fabbisogno di energia elettrica", None))
        self.enProdResLbl.setText(QCoreApplication.translate("MainWindow", u"Energia prodotta", None))
        self.enProdResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.h2ConsResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.totEnConsMtepResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" Mtep", None))
        self.enImportResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.totEnConsResLbl.setText(QCoreApplication.translate("MainWindow", u"Consumi finali di energia", None))
        self.renResLBL.setText(QCoreApplication.translate("MainWindow", u"Rinnovabili", None))
        self.solarGenResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.windGenPercResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.solarGenResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.otherGenPercResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.ferGenPercResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.ferGenResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.windGenResLbl.setText(QCoreApplication.translate("MainWindow", u"di cui Eolico", None))
        self.windGenResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.solarGenPercResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.ferGenResLbl.setText(QCoreApplication.translate("MainWindow", u"Generazione da FER", None))
        self.windGenPercResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.otherGenPercResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.ferGenPercResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.ferGenResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.solarGenPercResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.windGenResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.perspGenLbl.setText(QCoreApplication.translate("MainWindow", u"Valori prospettici", None))
        self.otherGenResLbl.setText(QCoreApplication.translate("MainWindow", u"di cui Altre fonti", None))
        self.otherGenResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.solarGenResLbl.setText(QCoreApplication.translate("MainWindow", u"di cui Solare", None))
        self.actGenLbl.setText(QCoreApplication.translate("MainWindow", u"Valori attuali", None))
        self.otherGenResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.perspOvergenLbl.setText(QCoreApplication.translate("MainWindow", u"Valori prospettici", None))
        self.hiOvergenResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.hiOvergenResLbl.setText(QCoreApplication.translate("MainWindow", u"Overgeneration ALTA", None))
        self.actOvergenResLbl.setText(QCoreApplication.translate("MainWindow", u"Valori attuali", None))
        self.lowOvergenResLbl.setText(QCoreApplication.translate("MainWindow", u"Overgeneration Bassa", None))
        self.lowOvergenResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.lowOvergenResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.hiOvergenResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.otherCapPercResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.windCapResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" GW", None))
        self.windCapPercResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.solarCapPercResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.actualLbl_3.setText(QCoreApplication.translate("MainWindow", u"Valori attuali", None))
        self.otherCapResLbl.setText(QCoreApplication.translate("MainWindow", u"di cui Altre fonti", None))
        self.solarCapResLbl.setText(QCoreApplication.translate("MainWindow", u"di cui Solalre", None))
        self.otherCapResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u" GW", None))
        self.solarCapResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" GW", None))
        self.otherCapPercResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.ferCapResLbl.setText(QCoreApplication.translate("MainWindow", u"Capacit\u00e0 installata FER", None))
        self.ferCapResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u" GW", None))
        self.ferCapResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" GW", None))
        self.solarCapPercResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.windCapResLbl.setText(QCoreApplication.translate("MainWindow", u"di cui Eolico", None))
        self.windCapPercResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.solarCapResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u" GW", None))
        self.windCapResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u" GW", None))
        self.otherCapResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" GW", None))
        self.perspectLbl_3.setText(QCoreApplication.translate("MainWindow", u"Valori prospettici", None))
        self.storResLbl.setText(QCoreApplication.translate("MainWindow", u"Accumuli", None))
        self.perspStorLbl.setText(QCoreApplication.translate("MainWindow", u"Valori prospettici", None))
        self.sysStorResLbl.setText(QCoreApplication.translate("MainWindow", u"Sistemi di stoccaggio (Ipotesi TERNA)", None))
        self.sysStorResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" Gwh", None))
        self.h2ResLbl.setText(QCoreApplication.translate("MainWindow", u"Idrogeno", None))
        self.overgenH2Lbl.setText(QCoreApplication.translate("MainWindow", u"Ipotesi Overgenreation", None))
        self.toprodHiH2ResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.maxLowH2ResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.maxHiH2ResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.overgenLowH2Lbl.setText(QCoreApplication.translate("MainWindow", u"BASSA", None))
        self.toprodHiH2ResLbl.setText(QCoreApplication.translate("MainWindow", u"H2 da prod. oltre l'overgeneration", None))
        self.maxHiH2ResLbl.setText(QCoreApplication.translate("MainWindow", u"max prod. H2 da overgenration", None))
        self.toprodLowH2ResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" TWh", None))
        self.overgenHiH2Lbl.setText(QCoreApplication.translate("MainWindow", u"ALTA", None))
        self.costsResLbl.setText(QCoreApplication.translate("MainWindow", u"Costi", None))
        self.frnpCostsResLbl.setText(QCoreApplication.translate("MainWindow", u"Costo FRNP (ak kW installato)", None))
        self.h2CostsResPerspDsb.setPrefix(QCoreApplication.translate("MainWindow", u"\u20ac ", None))
        self.h2CostsResPerspDsb.setSuffix("")
        self.capexCostsResPerspDsb.setPrefix(QCoreApplication.translate("MainWindow", u"\u20ac ", None))
        self.capexCostsResPerspDsb.setSuffix("")
        self.h2CostsResLbl.setText(QCoreApplication.translate("MainWindow", u"Costo H2", None))
        self.capexCostsResLbl.setText(QCoreApplication.translate("MainWindow", u"Capex totale SdA", None))
        self.frnpCostsResPerspDsb.setPrefix(QCoreApplication.translate("MainWindow", u"M\u20ac ", None))
        self.frnpCostsResPerspDsb.setSuffix("")
        self.perspCostsLbl.setText(QCoreApplication.translate("MainWindow", u"Valori prospettici", None))
        self.inputLbl_7.setText(QCoreApplication.translate("MainWindow", u"Emissioni", None))
        self.actualLbl_4.setText(QCoreApplication.translate("MainWindow", u"Valori attuali", None))
        self.perspectLbl_4.setText(QCoreApplication.translate("MainWindow", u"Valori prospettici", None))
        self.co2EmisResActLbl.setText(QCoreApplication.translate("MainWindow", u"Emissioni di CO2", None))
        self.co2EmisResActDsb.setSuffix(QCoreApplication.translate("MainWindow", u" Mt", None))
        self.co2EmisResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" Mt", None))
        self.co2EmisRedResPerspLbl.setText(QCoreApplication.translate("MainWindow", u"Riduzione delle emissioni", None))
        self.co2EmisRedResPerspDsb.setSuffix(QCoreApplication.translate("MainWindow", u" Mt", None))
    # retranslateUi

