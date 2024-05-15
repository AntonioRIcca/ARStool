# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'grid_detailsAZCtyQ.ui'
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


class Ui_mainWgt(object):
    def setupUi(self, mainWgt):
        if mainWgt.objectName():
            mainWgt.setObjectName(u"mainWgt")
        mainWgt.resize(548, 815)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWgt.sizePolicy().hasHeightForWidth())
        mainWgt.setSizePolicy(sizePolicy)
        mainWgt.setMinimumSize(QSize(0, 0))
        mainWgt.setStyleSheet(u"* {\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.gridDetailsMainWgt = QWidget(mainWgt)
        self.gridDetailsMainWgt.setObjectName(u"gridDetailsMainWgt")
        self.gridDetailsMainWgt.setGeometry(QRect(10, 10, 491, 791))
        sizePolicy.setHeightForWidth(self.gridDetailsMainWgt.sizePolicy().hasHeightForWidth())
        self.gridDetailsMainWgt.setSizePolicy(sizePolicy)
        self.gridDetailsMainWgt.setStyleSheet(u"* {\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	padding: 5px 4px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(31, 31, 31);\n"
"	border: solid;\n"
"	border-width: 2px; \n"
"	border-radius: 10px; \n"
"	border-color: rgb(127, 127, 127);\n"
"}\n"
"  \n"
"QPushButton:pressed {\n"
"	background-color: rgb(64, 64, 64); \n"
"	border-style: inset\n"
"}")
        self.verticalLayout = QVBoxLayout(self.gridDetailsMainWgt)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.imageLbl = QLabel(self.gridDetailsMainWgt)
        self.imageLbl.setObjectName(u"imageLbl")
        self.imageLbl.setMinimumSize(QSize(400, 300))
        self.imageLbl.setMaximumSize(QSize(600, 450))
        font = QFont()
        font.setPointSize(10)
        self.imageLbl.setFont(font)
        self.imageLbl.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.imageLbl.setTextFormat(Qt.AutoText)
        self.imageLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.imageLbl, 0, Qt.AlignHCenter)

        self.centralWgt = QWidget(self.gridDetailsMainWgt)
        self.centralWgt.setObjectName(u"centralWgt")
        self.gridLayout = QGridLayout(self.centralWgt)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.nameCapLbl = QLabel(self.centralWgt)
        self.nameCapLbl.setObjectName(u"nameCapLbl")
        sizePolicy.setHeightForWidth(self.nameCapLbl.sizePolicy().hasHeightForWidth())
        self.nameCapLbl.setSizePolicy(sizePolicy)
        self.nameCapLbl.setMinimumSize(QSize(50, 0))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setItalic(True)
        self.nameCapLbl.setFont(font1)
        self.nameCapLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.nameCapLbl, 0, 0, 1, 1)

        self.nameLbl = QLabel(self.centralWgt)
        self.nameLbl.setObjectName(u"nameLbl")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.nameLbl.setFont(font2)

        self.gridLayout.addWidget(self.nameLbl, 0, 1, 1, 1)

        self.descCapLbl = QLabel(self.centralWgt)
        self.descCapLbl.setObjectName(u"descCapLbl")
        self.descCapLbl.setFont(font1)
        self.descCapLbl.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.descCapLbl, 1, 0, 1, 1)

        self.descLbl = QLabel(self.centralWgt)
        self.descLbl.setObjectName(u"descLbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.descLbl.sizePolicy().hasHeightForWidth())
        self.descLbl.setSizePolicy(sizePolicy1)
        self.descLbl.setFont(font2)
        self.descLbl.setLineWidth(1)
        self.descLbl.setMidLineWidth(0)
        self.descLbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.descLbl.setWordWrap(True)

        self.gridLayout.addWidget(self.descLbl, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.centralWgt)

        self.widget_2 = QWidget(self.gridDetailsMainWgt)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.open = QPushButton(self.widget_2)
        self.open.setObjectName(u"open")
        self.open.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.open)


        self.verticalLayout.addWidget(self.widget_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(mainWgt)

        QMetaObject.connectSlotsByName(mainWgt)
    # setupUi

    def retranslateUi(self, mainWgt):
        mainWgt.setWindowTitle(QCoreApplication.translate("mainWgt", u"Form", None))
        self.imageLbl.setText(QCoreApplication.translate("mainWgt", u"Immagine non disponibile", None))
        self.nameCapLbl.setText(QCoreApplication.translate("mainWgt", u"Nome rete:", None))
        self.nameLbl.setText(QCoreApplication.translate("mainWgt", u"City Area", None))
        self.descCapLbl.setText(QCoreApplication.translate("mainWgt", u"Descrizione:", None))
        self.descLbl.setText(QCoreApplication.translate("mainWgt", u"Rete urbana ibrida Rete urbana ibrida Rete urbana ibrida Rete urbana ibrida Rete urbana ibrida Rete urbana ibrida Rete urbana ibrida Rete urbana ibrida Rete urbana ibrida ", None))
        self.open.setText(QCoreApplication.translate("mainWgt", u"Apri Rete", None))
    # retranslateUi

