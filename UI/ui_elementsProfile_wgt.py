# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'elementsProfile_wgtpZFhAo.ui'
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
        self.mainWgt.setGeometry(QRect(30, 20, 531, 641))
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
"QLabel{\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
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
        self.mainSaWgt.setGeometry(QRect(0, 0, 511, 621))
        self.mainSaWgtGL = QGridLayout(self.mainSaWgt)
        self.mainSaWgtGL.setObjectName(u"mainSaWgtGL")
        self.MainSaWgtGB = QGroupBox(self.mainSaWgt)
        self.MainSaWgtGB.setObjectName(u"MainSaWgtGB")
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.MainSaWgtGB.setFont(font)
        self.gridLayout_2 = QGridLayout(self.MainSaWgtGB)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 30, 9, -1)
        self.catLbl_7 = QLabel(self.MainSaWgtGB)
        self.catLbl_7.setObjectName(u"catLbl_7")

        self.gridLayout_2.addWidget(self.catLbl_7, 6, 1, 1, 1)

        self.elemLbl_3 = QLabel(self.MainSaWgtGB)
        self.elemLbl_3.setObjectName(u"elemLbl_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elemLbl_3.sizePolicy().hasHeightForWidth())
        self.elemLbl_3.setSizePolicy(sizePolicy)
        self.elemLbl_3.setMinimumSize(QSize(0, 30))
        self.elemLbl_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.elemLbl_3, 2, 0, 1, 1)

        self.catLbl_4 = QLabel(self.MainSaWgtGB)
        self.catLbl_4.setObjectName(u"catLbl_4")

        self.gridLayout_2.addWidget(self.catLbl_4, 3, 1, 1, 1)

        self.catLbl = QLabel(self.MainSaWgtGB)
        self.catLbl.setObjectName(u"catLbl")

        self.gridLayout_2.addWidget(self.catLbl, 0, 1, 1, 1)

        self.catLbl_2 = QLabel(self.MainSaWgtGB)
        self.catLbl_2.setObjectName(u"catLbl_2")

        self.gridLayout_2.addWidget(self.catLbl_2, 1, 1, 1, 1)

        self.typeCB_3 = QComboBox(self.MainSaWgtGB)
        self.typeCB_3.setObjectName(u"typeCB_3")

        self.gridLayout_2.addWidget(self.typeCB_3, 3, 2, 1, 1)

        self.catLbl_3 = QLabel(self.MainSaWgtGB)
        self.catLbl_3.setObjectName(u"catLbl_3")

        self.gridLayout_2.addWidget(self.catLbl_3, 2, 1, 1, 1)

        self.typeCB_7 = QComboBox(self.MainSaWgtGB)
        self.typeCB_7.setObjectName(u"typeCB_7")

        self.gridLayout_2.addWidget(self.typeCB_7, 4, 2, 1, 1)

        self.elemLbl_8 = QLabel(self.MainSaWgtGB)
        self.elemLbl_8.setObjectName(u"elemLbl_8")
        sizePolicy.setHeightForWidth(self.elemLbl_8.sizePolicy().hasHeightForWidth())
        self.elemLbl_8.setSizePolicy(sizePolicy)
        self.elemLbl_8.setMinimumSize(QSize(0, 30))
        self.elemLbl_8.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.elemLbl_8, 6, 0, 1, 1)

        self.elemLbl_4 = QLabel(self.MainSaWgtGB)
        self.elemLbl_4.setObjectName(u"elemLbl_4")
        sizePolicy.setHeightForWidth(self.elemLbl_4.sizePolicy().hasHeightForWidth())
        self.elemLbl_4.setSizePolicy(sizePolicy)
        self.elemLbl_4.setMinimumSize(QSize(0, 30))
        self.elemLbl_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.elemLbl_4, 3, 0, 1, 1)

        self.catLbl_8 = QLabel(self.MainSaWgtGB)
        self.catLbl_8.setObjectName(u"catLbl_8")

        self.gridLayout_2.addWidget(self.catLbl_8, 4, 1, 1, 1)

        self.typeCB_4 = QComboBox(self.MainSaWgtGB)
        self.typeCB_4.setObjectName(u"typeCB_4")

        self.gridLayout_2.addWidget(self.typeCB_4, 2, 2, 1, 1)

        self.typeCB_2 = QComboBox(self.MainSaWgtGB)
        self.typeCB_2.setObjectName(u"typeCB_2")

        self.gridLayout_2.addWidget(self.typeCB_2, 1, 2, 1, 1)

        self.elemLbl_6 = QLabel(self.MainSaWgtGB)
        self.elemLbl_6.setObjectName(u"elemLbl_6")
        sizePolicy.setHeightForWidth(self.elemLbl_6.sizePolicy().hasHeightForWidth())
        self.elemLbl_6.setSizePolicy(sizePolicy)
        self.elemLbl_6.setMinimumSize(QSize(0, 30))
        self.elemLbl_6.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.elemLbl_6, 7, 0, 1, 1)

        self.elemLbl_5 = QLabel(self.MainSaWgtGB)
        self.elemLbl_5.setObjectName(u"elemLbl_5")
        sizePolicy.setHeightForWidth(self.elemLbl_5.sizePolicy().hasHeightForWidth())
        self.elemLbl_5.setSizePolicy(sizePolicy)
        self.elemLbl_5.setMinimumSize(QSize(0, 30))
        self.elemLbl_5.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.elemLbl_5, 5, 0, 1, 1)

        self.typeCB_6 = QComboBox(self.MainSaWgtGB)
        self.typeCB_6.setObjectName(u"typeCB_6")

        self.gridLayout_2.addWidget(self.typeCB_6, 6, 2, 1, 1)

        self.elemLbl_7 = QLabel(self.MainSaWgtGB)
        self.elemLbl_7.setObjectName(u"elemLbl_7")
        sizePolicy.setHeightForWidth(self.elemLbl_7.sizePolicy().hasHeightForWidth())
        self.elemLbl_7.setSizePolicy(sizePolicy)
        self.elemLbl_7.setMinimumSize(QSize(0, 30))
        self.elemLbl_7.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.elemLbl_7, 4, 0, 1, 1)

        self.typeCB_5 = QComboBox(self.MainSaWgtGB)
        self.typeCB_5.setObjectName(u"typeCB_5")

        self.gridLayout_2.addWidget(self.typeCB_5, 5, 2, 1, 1)

        self.elemLbl = QLabel(self.MainSaWgtGB)
        self.elemLbl.setObjectName(u"elemLbl")
        sizePolicy.setHeightForWidth(self.elemLbl.sizePolicy().hasHeightForWidth())
        self.elemLbl.setSizePolicy(sizePolicy)
        self.elemLbl.setMinimumSize(QSize(0, 30))
        self.elemLbl.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.elemLbl, 0, 0, 1, 1)

        self.elemLbl_2 = QLabel(self.MainSaWgtGB)
        self.elemLbl_2.setObjectName(u"elemLbl_2")
        sizePolicy.setHeightForWidth(self.elemLbl_2.sizePolicy().hasHeightForWidth())
        self.elemLbl_2.setSizePolicy(sizePolicy)
        self.elemLbl_2.setMinimumSize(QSize(0, 30))
        self.elemLbl_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.elemLbl_2, 1, 0, 1, 1)

        self.catLbl_5 = QLabel(self.MainSaWgtGB)
        self.catLbl_5.setObjectName(u"catLbl_5")

        self.gridLayout_2.addWidget(self.catLbl_5, 5, 1, 1, 1)

        self.catLbl_6 = QLabel(self.MainSaWgtGB)
        self.catLbl_6.setObjectName(u"catLbl_6")

        self.gridLayout_2.addWidget(self.catLbl_6, 7, 1, 1, 1)

        self.typeCB_8 = QComboBox(self.MainSaWgtGB)
        self.typeCB_8.setObjectName(u"typeCB_8")

        self.gridLayout_2.addWidget(self.typeCB_8, 7, 2, 1, 1)

        self.typeCB = QComboBox(self.MainSaWgtGB)
        self.typeCB.setObjectName(u"typeCB")

        self.gridLayout_2.addWidget(self.typeCB, 0, 2, 1, 1)


        self.mainSaWgtGL.addWidget(self.MainSaWgtGB, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.mainSaWgtGL.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.mainSA.setWidget(self.mainSaWgt)

        self.verticalLayout.addWidget(self.mainSA)


        self.retranslateUi(elemProfWgt)

        QMetaObject.connectSlotsByName(elemProfWgt)
    # setupUi

    def retranslateUi(self, elemProfWgt):
        elemProfWgt.setWindowTitle(QCoreApplication.translate("elemProfWgt", u"Form", None))
        self.MainSaWgtGB.setTitle(QCoreApplication.translate("elemProfWgt", u"AC Load", None))
        self.catLbl_7.setText(QCoreApplication.translate("elemProfWgt", u"Categoria", None))
        self.elemLbl_3.setText(QCoreApplication.translate("elemProfWgt", u"Nome elemento", None))
        self.catLbl_4.setText(QCoreApplication.translate("elemProfWgt", u"Categoria", None))
        self.catLbl.setText(QCoreApplication.translate("elemProfWgt", u"Categoria", None))
        self.catLbl_2.setText(QCoreApplication.translate("elemProfWgt", u"Categoria", None))
        self.catLbl_3.setText(QCoreApplication.translate("elemProfWgt", u"Categoria", None))
        self.elemLbl_8.setText(QCoreApplication.translate("elemProfWgt", u"Nome elemento", None))
        self.elemLbl_4.setText(QCoreApplication.translate("elemProfWgt", u"Nome elemento", None))
        self.catLbl_8.setText(QCoreApplication.translate("elemProfWgt", u"Categoria", None))
        self.elemLbl_6.setText(QCoreApplication.translate("elemProfWgt", u"Nome elemento", None))
        self.elemLbl_5.setText(QCoreApplication.translate("elemProfWgt", u"Nome elemento", None))
        self.elemLbl_7.setText(QCoreApplication.translate("elemProfWgt", u"Nome elemento", None))
        self.elemLbl.setText(QCoreApplication.translate("elemProfWgt", u"Nome elemento", None))
        self.elemLbl_2.setText(QCoreApplication.translate("elemProfWgt", u"Nome elemento", None))
        self.catLbl_5.setText(QCoreApplication.translate("elemProfWgt", u"Categoria", None))
        self.catLbl_6.setText(QCoreApplication.translate("elemProfWgt", u"Categoria", None))
    # retranslateUi

