# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'elementsProfile_DlgCDVYcG.ui'
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


class Ui_mainDlg(object):
    def setupUi(self, mainDlg):
        if mainDlg.objectName():
            mainDlg.setObjectName(u"mainDlg")
        mainDlg.resize(800, 600)
        mainDlg.setStyleSheet(u"*{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(31, 31, 31); \n"
"	border: solid; \n"
"	border-width: 2px; \n"
"	border-radius: 10px;\n"
"	border-color: rgb(223, 223, 223);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(63, 63, 63);\n"
"}\n"
"")
        self.nameLbl = QLabel(mainDlg)
        self.nameLbl.setObjectName(u"nameLbl")
        self.nameLbl.setGeometry(QRect(10, 10, 780, 30))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nameLbl.setFont(font)
        self.upLn = QFrame(mainDlg)
        self.upLn.setObjectName(u"upLn")
        self.upLn.setGeometry(QRect(10, 40, 780, 3))
        self.upLn.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: solid;\n"
"")
        self.upLn.setFrameShape(QFrame.HLine)
        self.upLn.setFrameShadow(QFrame.Sunken)
        self.profileTW = QTableWidget(mainDlg)
        if (self.profileTW.columnCount() < 2):
            self.profileTW.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.profileTW.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.profileTW.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.profileTW.setObjectName(u"profileTW")
        self.profileTW.setGeometry(QRect(10, 50, 200, 490))
        self.profileTW.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.profileTW.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.profileTW.setAutoScroll(True)
        self.downLn = QFrame(mainDlg)
        self.downLn.setObjectName(u"downLn")
        self.downLn.setGeometry(QRect(10, 550, 780, 3))
        self.downLn.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: solid;\n"
"")
        self.downLn.setFrameShape(QFrame.HLine)
        self.downLn.setFrameShadow(QFrame.Sunken)
        self.saveBtn = QPushButton(mainDlg)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setGeometry(QRect(10, 560, 100, 30))
        self.cancelBtn = QPushButton(mainDlg)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setGeometry(QRect(690, 560, 100, 30))
        self.importBtn = QPushButton(mainDlg)
        self.importBtn.setObjectName(u"importBtn")
        self.importBtn.setGeometry(QRect(250, 560, 100, 30))
        self.exportBtn = QPushButton(mainDlg)
        self.exportBtn.setObjectName(u"exportBtn")
        self.exportBtn.setGeometry(QRect(130, 560, 100, 30))
        self.plotWgt = QWidget(mainDlg)
        self.plotWgt.setObjectName(u"plotWgt")
        self.plotWgt.setGeometry(QRect(220, 50, 570, 490))
        QWidget.setTabOrder(self.profileTW, self.cancelBtn)
        QWidget.setTabOrder(self.cancelBtn, self.saveBtn)
        QWidget.setTabOrder(self.saveBtn, self.exportBtn)
        QWidget.setTabOrder(self.exportBtn, self.importBtn)

        self.retranslateUi(mainDlg)

        QMetaObject.connectSlotsByName(mainDlg)
    # setupUi

    def retranslateUi(self, mainDlg):
        mainDlg.setWindowTitle(QCoreApplication.translate("mainDlg", u"Dialog", None))
        self.nameLbl.setText(QCoreApplication.translate("mainDlg", u"Nome Profilo", None))
        ___qtablewidgetitem = self.profileTW.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mainDlg", u"Ora", None));
        ___qtablewidgetitem1 = self.profileTW.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mainDlg", u"Scala [p.u.]", None));
        self.saveBtn.setText(QCoreApplication.translate("mainDlg", u"Salva", None))
        self.cancelBtn.setText(QCoreApplication.translate("mainDlg", u"Annulla", None))
        self.importBtn.setText(QCoreApplication.translate("mainDlg", u"Importa", None))
        self.exportBtn.setText(QCoreApplication.translate("mainDlg", u"Esporta", None))
    # retranslateUi

