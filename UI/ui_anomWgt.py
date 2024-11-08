# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'anomWgtZbmGnK.ui'
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


class Ui_mainAnomWgt(object):
    def setupUi(self, mainAnomWgt):
        if mainAnomWgt.objectName():
            mainAnomWgt.setObjectName(u"mainAnomWgt")
        mainAnomWgt.resize(239, 829)
        mainAnomWgt.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.anomWgt = QWidget(mainAnomWgt)
        self.anomWgt.setObjectName(u"anomWgt")
        self.anomWgt.setGeometry(QRect(20, 20, 145, 260))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.anomWgt.sizePolicy().hasHeightForWidth())
        self.anomWgt.setSizePolicy(sizePolicy)
        self.anomWgt.setMaximumSize(QSize(16777215, 500))
        self.anomWgt.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
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
"*{\n"
"	background-color: rgb(0, 31, 31);\n"
"	border-radius: 5px;\n"
"   \n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QDoubleSpinBox {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0); border: solid;\n"
"	border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(64, 64, 64); border-style: inset\n"
"}")
        self.relVL = QVBoxLayout(self.anomWgt)
        self.relVL.setSpacing(0)
        self.relVL.setObjectName(u"relVL")
        self.relVL.setContentsMargins(2, 0, 2, 0)
        self.anomLbl = QLabel(self.anomWgt)
        self.anomLbl.setObjectName(u"anomLbl")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.anomLbl.setFont(font)
        self.anomLbl.setAlignment(Qt.AlignCenter)

        self.relVL.addWidget(self.anomLbl)

        self.detailsWgt = QWidget(self.anomWgt)
        self.detailsWgt.setObjectName(u"detailsWgt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.detailsWgt.sizePolicy().hasHeightForWidth())
        self.detailsWgt.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.detailsWgt)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.catWgt = QWidget(self.detailsWgt)
        self.catWgt.setObjectName(u"catWgt")
        self.horizontalLayout_2 = QHBoxLayout(self.catWgt)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 10, -1, 0)
        self.catLbl = QLabel(self.catWgt)
        self.catLbl.setObjectName(u"catLbl")
        self.catLbl.setMinimumSize(QSize(0, 0))
        self.catLbl.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_2.addWidget(self.catLbl)

        self.catCB = QComboBox(self.catWgt)
        self.catCB.setObjectName(u"catCB")

        self.horizontalLayout_2.addWidget(self.catCB)


        self.verticalLayout.addWidget(self.catWgt)

        self.typeWgt = QWidget(self.detailsWgt)
        self.typeWgt.setObjectName(u"typeWgt")
        self.horizontalLayout_3 = QHBoxLayout(self.typeWgt)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.typeLbl = QLabel(self.typeWgt)
        self.typeLbl.setObjectName(u"typeLbl")
        self.typeLbl.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.typeLbl)

        self.typeCB = QComboBox(self.typeWgt)
        self.typeCB.setObjectName(u"typeCB")

        self.horizontalLayout_3.addWidget(self.typeCB)


        self.verticalLayout.addWidget(self.typeWgt)

        self.anomRateWgt = QWidget(self.detailsWgt)
        self.anomRateWgt.setObjectName(u"anomRateWgt")
        self.anomRateWgt.setStyleSheet(u"")
        self.relParGL_2 = QGridLayout(self.anomRateWgt)
        self.relParGL_2.setObjectName(u"relParGL_2")
        self.rateDsb = QDoubleSpinBox(self.anomRateWgt)
        self.rateDsb.setObjectName(u"rateDsb")
        self.rateDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.rateDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.rateDsb.setDecimals(4)
        self.rateDsb.setMaximum(999999.900000000023283)

        self.relParGL_2.addWidget(self.rateDsb, 0, 1, 1, 1)

        self.rateUnitLbl = QLabel(self.anomRateWgt)
        self.rateUnitLbl.setObjectName(u"rateUnitLbl")

        self.relParGL_2.addWidget(self.rateUnitLbl, 0, 2, 1, 1)

        self.rateLbl = QLabel(self.anomRateWgt)
        self.rateLbl.setObjectName(u"rateLbl")

        self.relParGL_2.addWidget(self.rateLbl, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.anomRateWgt)

        self.anomParWgt = QWidget(self.detailsWgt)
        self.anomParWgt.setObjectName(u"anomParWgt")
        self.anomParWgt.setStyleSheet(u"")
        self.relParGL = QGridLayout(self.anomParWgt)
        self.relParGL.setObjectName(u"relParGL")
        self.parLbl = QLabel(self.anomParWgt)
        self.parLbl.setObjectName(u"parLbl")

        self.relParGL.addWidget(self.parLbl, 4, 0, 1, 1)

        self.lbddurUnitLbl = QLabel(self.anomParWgt)
        self.lbddurUnitLbl.setObjectName(u"lbddurUnitLbl")

        self.relParGL.addWidget(self.lbddurUnitLbl, 1, 2, 1, 1)

        self.lbddurDsb = QDoubleSpinBox(self.anomParWgt)
        self.lbddurDsb.setObjectName(u"lbddurDsb")
        self.lbddurDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbddurDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.lbddurDsb.setDecimals(3)
        self.lbddurDsb.setMinimum(-1.000000000000000)
        self.lbddurDsb.setMaximum(99999.000000000000000)
        self.lbddurDsb.setSingleStep(0.100000000000000)
        self.lbddurDsb.setValue(1.000000000000000)

        self.relParGL.addWidget(self.lbddurDsb, 1, 1, 1, 1)

        self.fixLbl = QLabel(self.anomParWgt)
        self.fixLbl.setObjectName(u"fixLbl")

        self.relParGL.addWidget(self.fixLbl, 3, 0, 1, 1)

        self.lbdaLbl = QLabel(self.anomParWgt)
        self.lbdaLbl.setObjectName(u"lbdaLbl")

        self.relParGL.addWidget(self.lbdaLbl, 0, 0, 1, 1)

        self.parUnitLbl = QLabel(self.anomParWgt)
        self.parUnitLbl.setObjectName(u"parUnitLbl")

        self.relParGL.addWidget(self.parUnitLbl, 4, 2, 1, 1)

        self.lbddurLbl = QLabel(self.anomParWgt)
        self.lbddurLbl.setObjectName(u"lbddurLbl")

        self.relParGL.addWidget(self.lbddurLbl, 1, 0, 1, 1)

        self.lbdaUnitLbl = QLabel(self.anomParWgt)
        self.lbdaUnitLbl.setObjectName(u"lbdaUnitLbl")

        self.relParGL.addWidget(self.lbdaUnitLbl, 0, 2, 1, 1)

        self.lbdaDsb = QDoubleSpinBox(self.anomParWgt)
        self.lbdaDsb.setObjectName(u"lbdaDsb")
        self.lbdaDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbdaDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.lbdaDsb.setDecimals(3)
        self.lbdaDsb.setMaximum(99999.000000000000000)

        self.relParGL.addWidget(self.lbdaDsb, 0, 1, 1, 1)

        self.parDsb = QDoubleSpinBox(self.anomParWgt)
        self.parDsb.setObjectName(u"parDsb")
        self.parDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.parDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.parDsb.setDecimals(3)
        self.parDsb.setMaximum(99999.000000000000000)
        self.parDsb.setSingleStep(0.100000000000000)

        self.relParGL.addWidget(self.parDsb, 4, 1, 1, 1)

        self.fixCkb = QCheckBox(self.anomParWgt)
        self.fixCkb.setObjectName(u"fixCkb")

        self.relParGL.addWidget(self.fixCkb, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.anomParWgt)

        self.plsWgt = QWidget(self.detailsWgt)
        self.plsWgt.setObjectName(u"plsWgt")
        self.plsWgt.setStyleSheet(u"font: 7pt \"MS Shell Dlg 2\";")
        self.horizontalLayout = QHBoxLayout(self.plsWgt)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 5, 10)
        self.upPb = QPushButton(self.plsWgt)
        self.upPb.setObjectName(u"upPb")
        self.upPb.setMinimumSize(QSize(0, 18))

        self.horizontalLayout.addWidget(self.upPb)

        self.downPb = QPushButton(self.plsWgt)
        self.downPb.setObjectName(u"downPb")
        self.downPb.setMinimumSize(QSize(0, 18))

        self.horizontalLayout.addWidget(self.downPb)

        self.cancPb = QPushButton(self.plsWgt)
        self.cancPb.setObjectName(u"cancPb")
        self.cancPb.setMinimumSize(QSize(0, 18))

        self.horizontalLayout.addWidget(self.cancPb)


        self.verticalLayout.addWidget(self.plsWgt)


        self.relVL.addWidget(self.detailsWgt)

        self.detailsPbWgt = QWidget(self.anomWgt)
        self.detailsPbWgt.setObjectName(u"detailsPbWgt")
        self.detailsPbWgt.setMinimumSize(QSize(0, 0))
        self.detailsPbWgt.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_4 = QHBoxLayout(self.detailsPbWgt)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 10)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.detailsPb = QPushButton(self.detailsPbWgt)
        self.detailsPb.setObjectName(u"detailsPb")
        self.detailsPb.setMinimumSize(QSize(100, 18))

        self.horizontalLayout_4.addWidget(self.detailsPb)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.relVL.addWidget(self.detailsPbWgt)

        self.line = QFrame(self.anomWgt)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.relVL.addWidget(self.line)


        self.retranslateUi(mainAnomWgt)

        QMetaObject.connectSlotsByName(mainAnomWgt)
    # setupUi

    def retranslateUi(self, mainAnomWgt):
        mainAnomWgt.setWindowTitle(QCoreApplication.translate("mainAnomWgt", u"Form", None))
        self.anomLbl.setText(QCoreApplication.translate("mainAnomWgt", u"Anomalia 1", None))
        self.catLbl.setText(QCoreApplication.translate("mainAnomWgt", u"Cat.:", None))
        self.typeLbl.setText(QCoreApplication.translate("mainAnomWgt", u"Tipol.:", None))
        self.rateUnitLbl.setText(QCoreApplication.translate("mainAnomWgt", u"1/y", None))
        self.rateLbl.setText(QCoreApplication.translate("mainAnomWgt", u"rate", None))
        self.parLbl.setText(QCoreApplication.translate("mainAnomWgt", u"valore", None))
        self.lbddurUnitLbl.setText(QCoreApplication.translate("mainAnomWgt", u"h", None))
        self.fixLbl.setText(QCoreApplication.translate("mainAnomWgt", u"is fixed", None))
        self.lbdaLbl.setText(QCoreApplication.translate("mainAnomWgt", u"lbd_a", None))
        self.parUnitLbl.setText(QCoreApplication.translate("mainAnomWgt", u"-", None))
        self.lbddurLbl.setText(QCoreApplication.translate("mainAnomWgt", u"lbd_dur", None))
        self.lbdaUnitLbl.setText(QCoreApplication.translate("mainAnomWgt", u"h/y", None))
#if QT_CONFIG(tooltip)
        self.parDsb.setToolTip(QCoreApplication.translate("mainAnomWgt", u"Fattore di Qialit\u00e0", None))
#endif // QT_CONFIG(tooltip)
        self.fixCkb.setText("")
        self.upPb.setText(QCoreApplication.translate("mainAnomWgt", u"Up", None))
        self.downPb.setText(QCoreApplication.translate("mainAnomWgt", u"Down", None))
        self.cancPb.setText(QCoreApplication.translate("mainAnomWgt", u"Canc", None))
        self.detailsPb.setText(QCoreApplication.translate("mainAnomWgt", u"Vedi dettagli", None))
    # retranslateUi

