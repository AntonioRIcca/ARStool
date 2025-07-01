# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'elementPropertiesMFanRD.ui'
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
        Form.resize(785, 1196)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.propertiesWgt = QWidget(Form)
        self.propertiesWgt.setObjectName(u"propertiesWgt")
        self.propertiesWgt.setGeometry(QRect(140, 40, 185, 931))
        self.propertiesWgt.setStyleSheet(u"*{\n"
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
"}")
        self.propertiesVL = QVBoxLayout(self.propertiesWgt)
        self.propertiesVL.setSpacing(20)
        self.propertiesVL.setObjectName(u"propertiesVL")
        self.propertiesVL.setContentsMargins(5, 5, 5, 5)
        self.lfWgt = QWidget(self.propertiesWgt)
        self.lfWgt.setObjectName(u"lfWgt")
        self.lfWgt.setMinimumSize(QSize(0, 0))
        self.lfWgt.setMaximumSize(QSize(16777215, 500))
        self.lfWgt.setStyleSheet(u"")
        self.lfVL = QVBoxLayout(self.lfWgt)
        self.lfVL.setSpacing(6)
        self.lfVL.setObjectName(u"lfVL")
        self.lfVL.setContentsMargins(2, 0, 2, 0)
        self.lfPls = QPushButton(self.lfWgt)
        self.lfPls.setObjectName(u"lfPls")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lfPls.sizePolicy().hasHeightForWidth())
        self.lfPls.setSizePolicy(sizePolicy1)
        self.lfPls.setMinimumSize(QSize(0, 20))

        self.lfVL.addWidget(self.lfPls)

        self.lfNodeWgt = QWidget(self.lfWgt)
        self.lfNodeWgt.setObjectName(u"lfNodeWgt")
        self.lfNodeWgt.setStyleSheet(u"*{\n"
"	background-color: rgb(0, 0, 23);\n"
"	border-radius: 10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0); border: solid;\n"
"	border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(64, 64, 64); border-style: inset\n"
"}\n"
"")
        self.lfNodeGL = QGridLayout(self.lfNodeWgt)
        self.lfNodeGL.setObjectName(u"lfNodeGL")
        self.label_19 = QLabel(self.lfNodeWgt)
        self.label_19.setObjectName(u"label_19")

        self.lfNodeGL.addWidget(self.label_19, 0, 0, 1, 1)


        self.lfVL.addWidget(self.lfNodeWgt)

        self.lfParMainWgt = QWidget(self.lfWgt)
        self.lfParMainWgt.setObjectName(u"lfParMainWgt")
        self.lfParMainWgt.setStyleSheet(u"*{\n"
"	background-color: rgb(0, 0, 31);\n"
"	border-radius: 10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton, QDoubleSpinBox {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0); border: solid;\n"
"	border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(64, 64, 64); border-style: inset\n"
"}")
        self.lfParMainVL = QVBoxLayout(self.lfParMainWgt)
        self.lfParMainVL.setObjectName(u"lfParMainVL")
        self.lfParMainVL.setContentsMargins(0, -1, 0, -1)
        self.lfParLbl = QLabel(self.lfParMainWgt)
        self.lfParLbl.setObjectName(u"lfParLbl")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lfParLbl.setFont(font)
        self.lfParLbl.setAlignment(Qt.AlignCenter)

        self.lfParMainVL.addWidget(self.lfParLbl)

        self.lfParWgt = QWidget(self.lfParMainWgt)
        self.lfParWgt.setObjectName(u"lfParWgt")
        self.lfParGL = QGridLayout(self.lfParWgt)
        self.lfParGL.setObjectName(u"lfParGL")
        self.label = QLabel(self.lfParWgt)
        self.label.setObjectName(u"label")

        self.lfParGL.addWidget(self.label, 0, 0, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.lfParWgt)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.lfParGL.addWidget(self.doubleSpinBox, 0, 1, 1, 1)

        self.label_6 = QLabel(self.lfParWgt)
        self.label_6.setObjectName(u"label_6")

        self.lfParGL.addWidget(self.label_6, 3, 2, 1, 1)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.lfParWgt)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_3.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.lfParGL.addWidget(self.doubleSpinBox_3, 3, 1, 1, 1)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.lfParWgt)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_2.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.lfParGL.addWidget(self.doubleSpinBox_2, 1, 1, 1, 1)

        self.label_5 = QLabel(self.lfParWgt)
        self.label_5.setObjectName(u"label_5")

        self.lfParGL.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_4 = QLabel(self.lfParWgt)
        self.label_4.setObjectName(u"label_4")

        self.lfParGL.addWidget(self.label_4, 1, 2, 1, 1)

        self.label_3 = QLabel(self.lfParWgt)
        self.label_3.setObjectName(u"label_3")

        self.lfParGL.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_2 = QLabel(self.lfParWgt)
        self.label_2.setObjectName(u"label_2")

        self.lfParGL.addWidget(self.label_2, 0, 2, 1, 1)


        self.lfParMainVL.addWidget(self.lfParWgt)


        self.lfVL.addWidget(self.lfParMainWgt)

        self.lfResMainWgt = QWidget(self.lfWgt)
        self.lfResMainWgt.setObjectName(u"lfResMainWgt")
        self.lfResMainWgt.setStyleSheet(u"*{\n"
"	background-color: rgb(0, 0, 63);\n"
"	border-radius: 10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton, QDoubleSpinBox {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0); border: solid;\n"
"	border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(64, 64, 64); border-style: inset\n"
"}")
        self.verticalLayout = QVBoxLayout(self.lfResMainWgt)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lfResLbl = QLabel(self.lfResMainWgt)
        self.lfResLbl.setObjectName(u"lfResLbl")
        self.lfResLbl.setFont(font)
        self.lfResLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lfResLbl)

        self.lfResWgt = QWidget(self.lfResMainWgt)
        self.lfResWgt.setObjectName(u"lfResWgt")
        self.lfResGL = QGridLayout(self.lfResWgt)
        self.lfResGL.setObjectName(u"lfResGL")

        self.verticalLayout.addWidget(self.lfResWgt)


        self.lfVL.addWidget(self.lfResMainWgt)

        self.lfNodeWgt.raise_()
        self.lfResMainWgt.raise_()
        self.lfParMainWgt.raise_()
        self.lfPls.raise_()

        self.propertiesVL.addWidget(self.lfWgt)

        self.relWgt = QWidget(self.propertiesWgt)
        self.relWgt.setObjectName(u"relWgt")
        self.relWgt.setMaximumSize(QSize(16777215, 800))
        self.relWgt.setStyleSheet(u"/**\n"
"*{\n"
"	background-color: rgb(0, 31, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton, QDoubleSpinBox {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0); border: solid;\n"
"	border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(64, 64, 64); border-style: inset\n"
"}\n"
"**/")
        self.relVL = QVBoxLayout(self.relWgt)
        self.relVL.setSpacing(6)
        self.relVL.setObjectName(u"relVL")
        self.relVL.setContentsMargins(2, 0, 2, 0)
        self.relPls = QPushButton(self.relWgt)
        self.relPls.setObjectName(u"relPls")
        sizePolicy1.setHeightForWidth(self.relPls.sizePolicy().hasHeightForWidth())
        self.relPls.setSizePolicy(sizePolicy1)
        self.relPls.setMinimumSize(QSize(0, 20))

        self.relVL.addWidget(self.relPls)

        self.relParMainWgt = QWidget(self.relWgt)
        self.relParMainWgt.setObjectName(u"relParMainWgt")
        self.relParMainWgt.setStyleSheet(u"*{\n"
"	background-color: rgb(0, 23, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton, QDoubleSpinBox {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0); border: solid;\n"
"	border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(64, 64, 64); border-style: inset\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.relParMainWgt)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.relParLbl = QLabel(self.relParMainWgt)
        self.relParLbl.setObjectName(u"relParLbl")
        self.relParLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.relParLbl)

        self.relParWgt = QWidget(self.relParMainWgt)
        self.relParWgt.setObjectName(u"relParWgt")
        self.relParWgt.setStyleSheet(u"")
        self.relParGL = QGridLayout(self.relParWgt)
        self.relParGL.setObjectName(u"relParGL")
        self.Pi_EDsb = QDoubleSpinBox(self.relParWgt)
        self.Pi_EDsb.setObjectName(u"Pi_EDsb")
        self.Pi_EDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Pi_EDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Pi_EDsb.setDecimals(3)
        self.Pi_EDsb.setMaximum(50.000000000000000)
        self.Pi_EDsb.setSingleStep(0.100000000000000)

        self.relParGL.addWidget(self.Pi_EDsb, 4, 1, 1, 1)

        self.betaUnitLbl = QLabel(self.relParWgt)
        self.betaUnitLbl.setObjectName(u"betaUnitLbl")

        self.relParGL.addWidget(self.betaUnitLbl, 2, 2, 1, 1)

        self.betaLbl = QLabel(self.relParWgt)
        self.betaLbl.setObjectName(u"betaLbl")
        self.betaLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.relParGL.addWidget(self.betaLbl, 2, 0, 1, 1)

        self.Pi_ELBL = QLabel(self.relParWgt)
        self.Pi_ELBL.setObjectName(u"Pi_ELBL")
        self.Pi_ELBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.relParGL.addWidget(self.Pi_ELBL, 4, 0, 1, 1)

        self.Pi_QDsb = QDoubleSpinBox(self.relParWgt)
        self.Pi_QDsb.setObjectName(u"Pi_QDsb")
        self.Pi_QDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Pi_QDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Pi_QDsb.setDecimals(3)
        self.Pi_QDsb.setMaximum(20.000000000000000)
        self.Pi_QDsb.setSingleStep(0.100000000000000)

        self.relParGL.addWidget(self.Pi_QDsb, 5, 1, 1, 1)

        self.Pi_QUnitLbl = QLabel(self.relParWgt)
        self.Pi_QUnitLbl.setObjectName(u"Pi_QUnitLbl")

        self.relParGL.addWidget(self.Pi_QUnitLbl, 5, 2, 1, 1)

        self.alfaUnitLbl = QLabel(self.relParWgt)
        self.alfaUnitLbl.setObjectName(u"alfaUnitLbl")

        self.relParGL.addWidget(self.alfaUnitLbl, 1, 2, 1, 1)

        self.Pi_QLbl = QLabel(self.relParWgt)
        self.Pi_QLbl.setObjectName(u"Pi_QLbl")
        self.Pi_QLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.relParGL.addWidget(self.Pi_QLbl, 5, 0, 1, 1)

        self.betaDsb = QDoubleSpinBox(self.relParWgt)
        self.betaDsb.setObjectName(u"betaDsb")
        self.betaDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.betaDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.betaDsb.setDecimals(3)
        self.betaDsb.setMinimum(1.000000000000000)
        self.betaDsb.setMaximum(10.000000000000000)
        self.betaDsb.setSingleStep(0.100000000000000)

        self.relParGL.addWidget(self.betaDsb, 2, 1, 1, 1)

        self.alfaLbl = QLabel(self.relParWgt)
        self.alfaLbl.setObjectName(u"alfaLbl")
        self.alfaLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.relParGL.addWidget(self.alfaLbl, 1, 0, 1, 1)

        self.alfaDsb = QDoubleSpinBox(self.relParWgt)
        self.alfaDsb.setObjectName(u"alfaDsb")
        self.alfaDsb.setMinimumSize(QSize(60, 0))
        self.alfaDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.alfaDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.alfaDsb.setDecimals(1)
        self.alfaDsb.setMaximum(999999.900000000023283)
        self.alfaDsb.setValue(438000.000000000000000)

        self.relParGL.addWidget(self.alfaDsb, 1, 1, 1, 1)

        self.Pi_EUnitLbl = QLabel(self.relParWgt)
        self.Pi_EUnitLbl.setObjectName(u"Pi_EUnitLbl")

        self.relParGL.addWidget(self.Pi_EUnitLbl, 4, 2, 1, 1)

        self.t_pregLbl = QLabel(self.relParWgt)
        self.t_pregLbl.setObjectName(u"t_pregLbl")
        self.t_pregLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.relParGL.addWidget(self.t_pregLbl, 0, 0, 1, 1)

        self.t_pregDsb = QDoubleSpinBox(self.relParWgt)
        self.t_pregDsb.setObjectName(u"t_pregDsb")
        self.t_pregDsb.setMinimumSize(QSize(60, 0))
        self.t_pregDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.t_pregDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.t_pregDsb.setDecimals(1)
        self.t_pregDsb.setMaximum(999999.900000000023283)
        self.t_pregDsb.setValue(438000.000000000000000)

        self.relParGL.addWidget(self.t_pregDsb, 0, 1, 1, 1)

        self.t_pregUnitLbl = QLabel(self.relParWgt)
        self.t_pregUnitLbl.setObjectName(u"t_pregUnitLbl")

        self.relParGL.addWidget(self.t_pregUnitLbl, 0, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.relParWgt)


        self.relVL.addWidget(self.relParMainWgt)

        self.relResMainWgt = QWidget(self.relWgt)
        self.relResMainWgt.setObjectName(u"relResMainWgt")
        self.relResMainWgt.setStyleSheet(u"*{\n"
"	background-color: rgb(0, 47, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton, QDoubleSpinBox {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0); border: solid;\n"
"	border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(64, 64, 64); border-style: inset\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.relResMainWgt)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.relResLbl = QLabel(self.relResMainWgt)
        self.relResLbl.setObjectName(u"relResLbl")
        self.relResLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.relResLbl)

        self.relResWgt = QWidget(self.relResMainWgt)
        self.relResWgt.setObjectName(u"relResWgt")
        self.relResGL = QGridLayout(self.relResWgt)
        self.relResGL.setObjectName(u"relResGL")
        self.relResGL.setContentsMargins(0, -1, 0, -1)
        self.mtbfHrsLbl = QLabel(self.relResWgt)
        self.mtbfHrsLbl.setObjectName(u"mtbfHrsLbl")
        self.mtbfHrsLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.relResGL.addWidget(self.mtbfHrsLbl, 4, 0, 1, 1)

        self.mtbfHrsUnitLbl = QLabel(self.relResWgt)
        self.mtbfHrsUnitLbl.setObjectName(u"mtbfHrsUnitLbl")

        self.relResGL.addWidget(self.mtbfHrsUnitLbl, 4, 2, 1, 1)

        self.lbdRelLbl = QLabel(self.relResWgt)
        self.lbdRelLbl.setObjectName(u"lbdRelLbl")
        self.lbdRelLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.relResGL.addWidget(self.lbdRelLbl, 0, 0, 1, 1)

        self.lbdRelUniLbl = QLabel(self.relResWgt)
        self.lbdRelUniLbl.setObjectName(u"lbdRelUniLbl")

        self.relResGL.addWidget(self.lbdRelUniLbl, 0, 2, 1, 1)

        self.mtbfYrDsb = QDoubleSpinBox(self.relResWgt)
        self.mtbfYrDsb.setObjectName(u"mtbfYrDsb")
        self.mtbfYrDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.mtbfYrDsb.setReadOnly(True)
        self.mtbfYrDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.mtbfYrDsb.setDecimals(5)
        self.mtbfYrDsb.setMaximum(99.000000000000000)

        self.relResGL.addWidget(self.mtbfYrDsb, 5, 1, 1, 1)

        self.lbdRelDsb = QDoubleSpinBox(self.relResWgt)
        self.lbdRelDsb.setObjectName(u"lbdRelDsb")
        self.lbdRelDsb.setMinimumSize(QSize(60, 0))
        self.lbdRelDsb.setAcceptDrops(True)
        self.lbdRelDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbdRelDsb.setReadOnly(True)
        self.lbdRelDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.lbdRelDsb.setDecimals(6)
        self.lbdRelDsb.setMaximum(1.000000000000000)
        self.lbdRelDsb.setValue(0.000000000000000)

        self.relResGL.addWidget(self.lbdRelDsb, 0, 1, 1, 1)

        self.mtbfHrsDsb = QDoubleSpinBox(self.relResWgt)
        self.mtbfHrsDsb.setObjectName(u"mtbfHrsDsb")
        self.mtbfHrsDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.mtbfHrsDsb.setReadOnly(True)
        self.mtbfHrsDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.mtbfHrsDsb.setDecimals(1)
        self.mtbfHrsDsb.setMaximum(999999.900000000023283)

        self.relResGL.addWidget(self.mtbfHrsDsb, 4, 1, 1, 1)

        self.piSiRelDsb = QDoubleSpinBox(self.relResWgt)
        self.piSiRelDsb.setObjectName(u"piSiRelDsb")
        self.piSiRelDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.piSiRelDsb.setReadOnly(True)
        self.piSiRelDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.piSiRelDsb.setDecimals(3)
        self.piSiRelDsb.setMinimum(0.000000000000000)
        self.piSiRelDsb.setMaximum(999.000000000000000)
        self.piSiRelDsb.setSingleStep(0.100000000000000)

        self.relResGL.addWidget(self.piSiRelDsb, 2, 1, 1, 1)

        self.pSiRelUnitLbl = QLabel(self.relResWgt)
        self.pSiRelUnitLbl.setObjectName(u"pSiRelUnitLbl")

        self.relResGL.addWidget(self.pSiRelUnitLbl, 2, 2, 1, 1)

        self.piSiRelLbl = QLabel(self.relResWgt)
        self.piSiRelLbl.setObjectName(u"piSiRelLbl")
        self.piSiRelLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.relResGL.addWidget(self.piSiRelLbl, 2, 0, 1, 1)

        self.mtbfYrsUnitLbl = QLabel(self.relResWgt)
        self.mtbfYrsUnitLbl.setObjectName(u"mtbfYrsUnitLbl")

        self.relResGL.addWidget(self.mtbfYrsUnitLbl, 5, 2, 1, 1)

        self.rRelLbl = QLabel(self.relResWgt)
        self.rRelLbl.setObjectName(u"rRelLbl")
        self.rRelLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.relResGL.addWidget(self.rRelLbl, 1, 0, 1, 1)

        self.rRelDsb = QDoubleSpinBox(self.relResWgt)
        self.rRelDsb.setObjectName(u"rRelDsb")
        self.rRelDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.rRelDsb.setReadOnly(True)
        self.rRelDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.rRelDsb.setDecimals(6)
        self.rRelDsb.setMinimum(0.000000000000000)
        self.rRelDsb.setMaximum(999.000000000000000)
        self.rRelDsb.setSingleStep(0.100000000000000)

        self.relResGL.addWidget(self.rRelDsb, 1, 1, 1, 1)

        self.rUnitLbl = QLabel(self.relResWgt)
        self.rUnitLbl.setObjectName(u"rUnitLbl")

        self.relResGL.addWidget(self.rUnitLbl, 1, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.relResWgt)

        self.relFurnWgt = QWidget(self.relResMainWgt)
        self.relFurnWgt.setObjectName(u"relFurnWgt")
        self.relResGL_2 = QGridLayout(self.relFurnWgt)
        self.relResGL_2.setObjectName(u"relResGL_2")
        self.relResGL_2.setContentsMargins(0, -1, 0, -1)
        self.rNightRelLbl = QLabel(self.relFurnWgt)
        self.rNightRelLbl.setObjectName(u"rNightRelLbl")
        self.rNightRelLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.relResGL_2.addWidget(self.rNightRelLbl, 1, 0, 1, 1)

        self.rNightRelDsb = QDoubleSpinBox(self.relFurnWgt)
        self.rNightRelDsb.setObjectName(u"rNightRelDsb")
        self.rNightRelDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.rNightRelDsb.setReadOnly(True)
        self.rNightRelDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.rNightRelDsb.setDecimals(5)
        self.rNightRelDsb.setMinimum(0.000000000000000)
        self.rNightRelDsb.setMaximum(1.000000000000000)
        self.rNightRelDsb.setSingleStep(0.100000000000000)

        self.relResGL_2.addWidget(self.rNightRelDsb, 1, 1, 1, 1)

        self.rDayRelLbl = QLabel(self.relFurnWgt)
        self.rDayRelLbl.setObjectName(u"rDayRelLbl")
        self.rDayRelLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.relResGL_2.addWidget(self.rDayRelLbl, 0, 0, 1, 1)

        self.rNightRelUnitLbl = QLabel(self.relFurnWgt)
        self.rNightRelUnitLbl.setObjectName(u"rNightRelUnitLbl")

        self.relResGL_2.addWidget(self.rNightRelUnitLbl, 1, 2, 1, 1)

        self.rDayRelUniLbl = QLabel(self.relFurnWgt)
        self.rDayRelUniLbl.setObjectName(u"rDayRelUniLbl")

        self.relResGL_2.addWidget(self.rDayRelUniLbl, 0, 2, 1, 1)

        self.rDayRelDsb = QDoubleSpinBox(self.relFurnWgt)
        self.rDayRelDsb.setObjectName(u"rDayRelDsb")
        self.rDayRelDsb.setMinimumSize(QSize(60, 0))
        self.rDayRelDsb.setAcceptDrops(True)
        self.rDayRelDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.rDayRelDsb.setReadOnly(True)
        self.rDayRelDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.rDayRelDsb.setDecimals(4)
        self.rDayRelDsb.setMinimum(0.000000000000000)
        self.rDayRelDsb.setMaximum(1.000000000000000)
        self.rDayRelDsb.setValue(0.000000000000000)

        self.relResGL_2.addWidget(self.rDayRelDsb, 0, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.relFurnWgt)


        self.relVL.addWidget(self.relResMainWgt)

        self.relParMainWgt.raise_()
        self.relResMainWgt.raise_()
        self.relPls.raise_()

        self.propertiesVL.addWidget(self.relWgt)

        self.anomWgt = QWidget(self.propertiesWgt)
        self.anomWgt.setObjectName(u"anomWgt")
        self.anomWgt.setMaximumSize(QSize(16777215, 500))
        self.anomWgt.setStyleSheet(u"*{\n"
"   /**background-color: rgb(128, 0, 0);**/\n"
"	/**border-radius: 10px;**/\n"
"}\n"
"\n"
"#anomAddPls, QDoubleSpinBox {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0); border: solid;\n"
"	border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)\n"
"}\n"
"\n"
"#anomAddPls:pressed {\n"
"	background-color: rgb(64, 64, 64); border-style: inset\n"
"}")
        self.anomVL = QVBoxLayout(self.anomWgt)
        self.anomVL.setSpacing(6)
        self.anomVL.setObjectName(u"anomVL")
        self.anomVL.setContentsMargins(2, 0, 2, 0)
        self.anomPls = QPushButton(self.anomWgt)
        self.anomPls.setObjectName(u"anomPls")
        sizePolicy1.setHeightForWidth(self.anomPls.sizePolicy().hasHeightForWidth())
        self.anomPls.setSizePolicy(sizePolicy1)
        self.anomPls.setMinimumSize(QSize(0, 20))

        self.anomVL.addWidget(self.anomPls)

        self.agingWgt = QWidget(self.anomWgt)
        self.agingWgt.setObjectName(u"agingWgt")
        self.agingWgt.setStyleSheet(u"*{\n"
"	background-color: rgb(24, 0, 0);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"	border: none;\n"
"}\n"
"\n"
"#AgingTopWgt, #agingParWgt, #agingCkB{\n"
"	border: none;\n"
"	background-color: rgb(24, 0, 0);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"#agingWgt{\n"
"	border: none;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	border-color: rgb(128, 128, 128);\n"
"}\n"
"\n"
"#agingRateDsb{\n"
"		border-radius: 0px\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.agingWgt)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 5)
        self.AgingTopWgt = QWidget(self.agingWgt)
        self.AgingTopWgt.setObjectName(u"AgingTopWgt")
        self.horizontalLayout_2 = QHBoxLayout(self.AgingTopWgt)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.agingLbl = QLabel(self.AgingTopWgt)
        self.agingLbl.setObjectName(u"agingLbl")
        self.agingLbl.setFont(font)
        self.agingLbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.agingLbl)

        self.agingCkB = QCheckBox(self.AgingTopWgt)
        self.agingCkB.setObjectName(u"agingCkB")
        self.agingCkB.setMaximumSize(QSize(15, 16777215))

        self.horizontalLayout_2.addWidget(self.agingCkB)


        self.verticalLayout_2.addWidget(self.AgingTopWgt)

        self.agingParWgt = QWidget(self.agingWgt)
        self.agingParWgt.setObjectName(u"agingParWgt")
        self.horizontalLayout = QHBoxLayout(self.agingParWgt)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.agingRateLbl = QLabel(self.agingParWgt)
        self.agingRateLbl.setObjectName(u"agingRateLbl")
        self.agingRateLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.agingRateLbl)

        self.agingRateDsb = QDoubleSpinBox(self.agingParWgt)
        self.agingRateDsb.setObjectName(u"agingRateDsb")
        self.agingRateDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.agingRateDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.agingRateDsb.setDecimals(4)
        self.agingRateDsb.setMaximum(999999.900000000023283)

        self.horizontalLayout.addWidget(self.agingRateDsb)

        self.rateUnitLbl = QLabel(self.agingParWgt)
        self.rateUnitLbl.setObjectName(u"rateUnitLbl")

        self.horizontalLayout.addWidget(self.rateUnitLbl)


        self.verticalLayout_2.addWidget(self.agingParWgt)


        self.anomVL.addWidget(self.agingWgt)

        self.anomListWgt = QWidget(self.anomWgt)
        self.anomListWgt.setObjectName(u"anomListWgt")
        self.anomListVL = QVBoxLayout(self.anomListWgt)
        self.anomListVL.setSpacing(10)
        self.anomListVL.setObjectName(u"anomListVL")
        self.anomListVL.setContentsMargins(0, 0, 0, 0)

        self.anomVL.addWidget(self.anomListWgt)

        self.anomParWgt = QWidget(self.anomWgt)
        self.anomParWgt.setObjectName(u"anomParWgt")
        self.anomParWgt.setMinimumSize(QSize(0, 20))
        self.anomParWgt.setStyleSheet(u"")
        self.relParGL_3 = QGridLayout(self.anomParWgt)
        self.relParGL_3.setSpacing(0)
        self.relParGL_3.setObjectName(u"relParGL_3")
        self.relParGL_3.setContentsMargins(0, 0, 0, 0)
        self.anomAddPls = QPushButton(self.anomParWgt)
        self.anomAddPls.setObjectName(u"anomAddPls")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.anomAddPls.sizePolicy().hasHeightForWidth())
        self.anomAddPls.setSizePolicy(sizePolicy2)
        self.anomAddPls.setMinimumSize(QSize(120, 20))
        self.anomAddPls.setMaximumSize(QSize(120, 16777215))

        self.relParGL_3.addWidget(self.anomAddPls, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.relParGL_3.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.relParGL_3.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)


        self.anomVL.addWidget(self.anomParWgt)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.anomVL.addItem(self.verticalSpacer)

        self.agingWgt.raise_()
        self.anomListWgt.raise_()
        self.anomParWgt.raise_()
        self.anomPls.raise_()

        self.propertiesVL.addWidget(self.anomWgt)

        self.propertiesSpc = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.propertiesVL.addItem(self.propertiesSpc)

        self.buttonsWgt = QWidget(self.propertiesWgt)
        self.buttonsWgt.setObjectName(u"buttonsWgt")
        self.buttonsHL = QHBoxLayout(self.buttonsWgt)
        self.buttonsHL.setSpacing(30)
        self.buttonsHL.setObjectName(u"buttonsHL")
        self.buttonsHL.setContentsMargins(0, 0, 0, 0)
        self.savePLS = QPushButton(self.buttonsWgt)
        self.savePLS.setObjectName(u"savePLS")
        self.savePLS.setMinimumSize(QSize(0, 20))

        self.buttonsHL.addWidget(self.savePLS)

        self.cancelPLS = QPushButton(self.buttonsWgt)
        self.cancelPLS.setObjectName(u"cancelPLS")
        self.cancelPLS.setMinimumSize(QSize(0, 20))

        self.buttonsHL.addWidget(self.cancelPLS)


        self.propertiesVL.addWidget(self.buttonsWgt)

        QWidget.setTabOrder(self.doubleSpinBox, self.doubleSpinBox_2)
        QWidget.setTabOrder(self.doubleSpinBox_2, self.doubleSpinBox_3)
        QWidget.setTabOrder(self.doubleSpinBox_3, self.t_pregDsb)
        QWidget.setTabOrder(self.t_pregDsb, self.alfaDsb)
        QWidget.setTabOrder(self.alfaDsb, self.betaDsb)
        QWidget.setTabOrder(self.betaDsb, self.Pi_EDsb)
        QWidget.setTabOrder(self.Pi_EDsb, self.Pi_QDsb)
        QWidget.setTabOrder(self.Pi_QDsb, self.agingRateDsb)
        QWidget.setTabOrder(self.agingRateDsb, self.savePLS)
        QWidget.setTabOrder(self.savePLS, self.cancelPLS)
        QWidget.setTabOrder(self.cancelPLS, self.lfPls)
        QWidget.setTabOrder(self.lfPls, self.relPls)
        QWidget.setTabOrder(self.relPls, self.mtbfYrDsb)
        QWidget.setTabOrder(self.mtbfYrDsb, self.lbdRelDsb)
        QWidget.setTabOrder(self.lbdRelDsb, self.mtbfHrsDsb)
        QWidget.setTabOrder(self.mtbfHrsDsb, self.piSiRelDsb)
        QWidget.setTabOrder(self.piSiRelDsb, self.rRelDsb)
        QWidget.setTabOrder(self.rRelDsb, self.rNightRelDsb)
        QWidget.setTabOrder(self.rNightRelDsb, self.rDayRelDsb)
        QWidget.setTabOrder(self.rDayRelDsb, self.agingCkB)
        QWidget.setTabOrder(self.agingCkB, self.anomPls)
        QWidget.setTabOrder(self.anomPls, self.anomAddPls)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lfPls.setText(QCoreApplication.translate("Form", u"LoadFlow", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"HV Node", None))
        self.lfParLbl.setText(QCoreApplication.translate("Form", u"Parametri", None))
        self.label.setText(QCoreApplication.translate("Form", u"Power", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"unit", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Power", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"unit", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Power", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"unit", None))
        self.lfResLbl.setText(QCoreApplication.translate("Form", u"Risultati", None))
        self.relPls.setText(QCoreApplication.translate("Form", u"Affidabilit\u00e0", None))
        self.relParLbl.setText(QCoreApplication.translate("Form", u"Parametri", None))
#if QT_CONFIG(tooltip)
        self.Pi_EDsb.setToolTip(QCoreApplication.translate("Form", u"Fattore di Stress Ambientale ", None))
#endif // QT_CONFIG(tooltip)
        self.betaUnitLbl.setText(QCoreApplication.translate("Form", u"-", None))
        self.betaLbl.setText(QCoreApplication.translate("Form", u"beta", None))
        self.Pi_ELBL.setText(QCoreApplication.translate("Form", u"Pi_E", None))
#if QT_CONFIG(tooltip)
        self.Pi_QDsb.setToolTip(QCoreApplication.translate("Form", u"Fattore di Qualit\u00e0", None))
#endif // QT_CONFIG(tooltip)
        self.Pi_QUnitLbl.setText(QCoreApplication.translate("Form", u"-", None))
        self.alfaUnitLbl.setText(QCoreApplication.translate("Form", u"h", None))
        self.Pi_QLbl.setText(QCoreApplication.translate("Form", u"Pi_Q", None))
        self.alfaLbl.setText(QCoreApplication.translate("Form", u"alfa", None))
        self.Pi_EUnitLbl.setText(QCoreApplication.translate("Form", u"-", None))
        self.t_pregLbl.setText(QCoreApplication.translate("Form", u"vita preg.", None))
#if QT_CONFIG(tooltip)
        self.t_pregDsb.setToolTip(QCoreApplication.translate("Form", u"Vita pregressa di componente", None))
#endif // QT_CONFIG(tooltip)
        self.t_pregUnitLbl.setText(QCoreApplication.translate("Form", u"h", None))
        self.relResLbl.setText(QCoreApplication.translate("Form", u"Risultati", None))
        self.mtbfHrsLbl.setText(QCoreApplication.translate("Form", u"MTBF", None))
        self.mtbfHrsUnitLbl.setText(QCoreApplication.translate("Form", u"h", None))
        self.lbdRelLbl.setText(QCoreApplication.translate("Form", u"lambda", None))
        self.lbdRelUniLbl.setText(QCoreApplication.translate("Form", u"f/h", None))
#if QT_CONFIG(tooltip)
        self.mtbfYrDsb.setToolTip(QCoreApplication.translate("Form", u"Tempo medio tra i guasti", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lbdRelDsb.setToolTip(QCoreApplication.translate("Form", u"Tasso di guasto", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.mtbfHrsDsb.setToolTip(QCoreApplication.translate("Form", u"Tempo medio tra i guasti", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.piSiRelDsb.setToolTip(QCoreApplication.translate("Form", u"Fattore di Stress Termico", None))
#endif // QT_CONFIG(tooltip)
        self.pSiRelUnitLbl.setText(QCoreApplication.translate("Form", u"-", None))
        self.piSiRelLbl.setText(QCoreApplication.translate("Form", u"Pi_Si", None))
        self.mtbfYrsUnitLbl.setText(QCoreApplication.translate("Form", u"yr", None))
        self.rRelLbl.setText(QCoreApplication.translate("Form", u"R", None))
#if QT_CONFIG(tooltip)
        self.rRelDsb.setToolTip(QCoreApplication.translate("Form", u"Affidabilit\u00e0", None))
#endif // QT_CONFIG(tooltip)
        self.rUnitLbl.setText(QCoreApplication.translate("Form", u"-", None))
        self.rNightRelLbl.setText(QCoreApplication.translate("Form", u"R (night)", None))
#if QT_CONFIG(tooltip)
        self.rNightRelDsb.setToolTip(QCoreApplication.translate("Form", u"Affidabilit\u00e0 notturna", None))
#endif // QT_CONFIG(tooltip)
        self.rDayRelLbl.setText(QCoreApplication.translate("Form", u"R (day)", None))
        self.rNightRelUnitLbl.setText(QCoreApplication.translate("Form", u"-", None))
        self.rDayRelUniLbl.setText(QCoreApplication.translate("Form", u"-", None))
#if QT_CONFIG(tooltip)
        self.rDayRelDsb.setToolTip(QCoreApplication.translate("Form", u"Affidabilit\u00e0 diurna", None))
#endif // QT_CONFIG(tooltip)
        self.anomPls.setText(QCoreApplication.translate("Form", u"Anomalie", None))
        self.agingLbl.setText(QCoreApplication.translate("Form", u"Deterioramento", None))
        self.agingCkB.setText("")
        self.agingRateLbl.setText(QCoreApplication.translate("Form", u"rate", None))
        self.rateUnitLbl.setText(QCoreApplication.translate("Form", u"1/y", None))
        self.anomAddPls.setText(QCoreApplication.translate("Form", u"Nuova anomalia", None))
        self.savePLS.setText(QCoreApplication.translate("Form", u"Salva", None))
        self.cancelPLS.setText(QCoreApplication.translate("Form", u"Annulla", None))
    # retranslateUi

