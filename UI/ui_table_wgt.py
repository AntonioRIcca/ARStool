# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table_wgttWsKzU.ui'
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
        Form.resize(796, 667)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 501, 561))
        self.widget.setStyleSheet(u"*{}\n"
"QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(31, 31, 31); border: solid;\n"
"border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(64, 64, 64); border-style: inset\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tableWidget)

        self.buttons_WGT = QWidget(self.widget)
        self.buttons_WGT.setObjectName(u"buttons_WGT")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.buttons_WGT.sizePolicy().hasHeightForWidth())
        self.buttons_WGT.setSizePolicy(sizePolicy2)
        self.buttons_WGT.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.horizontalLayout_2 = QHBoxLayout(self.buttons_WGT)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.add_Btn = QPushButton(self.buttons_WGT)
        self.add_Btn.setObjectName(u"add_Btn")
        self.add_Btn.setMinimumSize(QSize(80, 25))
        self.add_Btn.setStyleSheet(u"border-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.add_Btn)

        self.del_Btn = QPushButton(self.buttons_WGT)
        self.del_Btn.setObjectName(u"del_Btn")
        self.del_Btn.setMinimumSize(QSize(80, 25))
        self.del_Btn.setStyleSheet(u"border-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.del_Btn)

        self.ren_Btn = QPushButton(self.buttons_WGT)
        self.ren_Btn.setObjectName(u"ren_Btn")
        self.ren_Btn.setMinimumSize(QSize(80, 25))
        self.ren_Btn.setStyleSheet(u"border-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.ren_Btn)

        self.buttons_Spc = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.buttons_Spc)

        self.save_Btn = QPushButton(self.buttons_WGT)
        self.save_Btn.setObjectName(u"save_Btn")
        self.save_Btn.setMinimumSize(QSize(80, 25))
        self.save_Btn.setStyleSheet(u"border-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.save_Btn)


        self.verticalLayout.addWidget(self.buttons_WGT)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Elemento", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"New Column", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"3", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"ufg", None));
        ___qtablewidgetitem6 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"uytfuvh", None));
        ___qtablewidgetitem7 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"tyfv", None));
        ___qtablewidgetitem8 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"7rfkyi", None));
        ___qtablewidgetitem9 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"uyk", None));
        ___qtablewidgetitem10 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"76ruyt", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.add_Btn.setText(QCoreApplication.translate("Form", u"Aggiungi", None))
        self.del_Btn.setText(QCoreApplication.translate("Form", u"Elimina", None))
        self.ren_Btn.setText(QCoreApplication.translate("Form", u"Rinomina", None))
        self.save_Btn.setText(QCoreApplication.translate("Form", u"Salva", None))
    # retranslateUi

