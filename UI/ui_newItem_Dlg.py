# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newItem_DlgwlYUcY.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(349, 840)
        Dialog.setStyleSheet(u"*{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QWidget{\n"
"border:solid;\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QLabel{\n"
"	border-width: 0px\n"
"}")
        self.mainVL = QVBoxLayout(Dialog)
        self.mainVL.setSpacing(20)
        self.mainVL.setObjectName(u"mainVL")
        self.mainVL.setContentsMargins(10, 10, 10, 10)
        self.nameLBL = QLabel(Dialog)
        self.nameLBL.setObjectName(u"nameLBL")
        self.nameLBL.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nameLBL.setFont(font)
        self.nameLBL.setStyleSheet(u"border: solid;\n"
"border-width: 1 px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")

        self.mainVL.addWidget(self.nameLBL)

        self.nameLE = QLineEdit(Dialog)
        self.nameLE.setObjectName(u"nameLE")
        self.nameLE.setMinimumSize(QSize(0, 30))
        self.nameLE.setStyleSheet(u"border-radius: 0px;")

        self.mainVL.addWidget(self.nameLE)

        self.typeWgt = QWidget(Dialog)
        self.typeWgt.setObjectName(u"typeWgt")
        self.typeWgt.setMinimumSize(QSize(0, 0))
        self.typeVL = QHBoxLayout(self.typeWgt)
        self.typeVL.setSpacing(5)
        self.typeVL.setObjectName(u"typeVL")
        self.typeLeftSpc = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.typeVL.addItem(self.typeLeftSpc)

        self.typeLbl = QLabel(self.typeWgt)
        self.typeLbl.setObjectName(u"typeLbl")
        self.typeLbl.setMinimumSize(QSize(50, 0))
        self.typeLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.typeVL.addWidget(self.typeLbl)

        self.typeCB = QComboBox(self.typeWgt)
        self.typeCB.setObjectName(u"typeCB")
        self.typeCB.setMinimumSize(QSize(150, 0))

        self.typeVL.addWidget(self.typeCB)

        self.typeRightSpc = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.typeVL.addItem(self.typeRightSpc)


        self.mainVL.addWidget(self.typeWgt)

        self.nodeWgt = QWidget(Dialog)
        self.nodeWgt.setObjectName(u"nodeWgt")
        self.nodeWgt.setMinimumSize(QSize(0, 0))
        self.nodeGL = QGridLayout(self.nodeWgt)
        self.nodeGL.setSpacing(5)
        self.nodeGL.setObjectName(u"nodeGL")
        self.nodeGL.setContentsMargins(10, 10, 10, 10)
        self.node1Lbl = QLabel(self.nodeWgt)
        self.node1Lbl.setObjectName(u"node1Lbl")
        self.node1Lbl.setMinimumSize(QSize(50, 0))
        self.node1Lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.nodeGL.addWidget(self.node1Lbl, 0, 1, 1, 1)

        self.vnode2Lbl = QLabel(self.nodeWgt)
        self.vnode2Lbl.setObjectName(u"vnode2Lbl")
        self.vnode2Lbl.setMinimumSize(QSize(50, 0))
        self.vnode2Lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.nodeGL.addWidget(self.vnode2Lbl, 4, 1, 1, 1)

        self.node2CB = QComboBox(self.nodeWgt)
        self.node2CB.setObjectName(u"node2CB")
        self.node2CB.setMinimumSize(QSize(150, 0))

        self.nodeGL.addWidget(self.node2CB, 3, 2, 1, 1)

        self.vnode1Dsb = QDoubleSpinBox(self.nodeWgt)
        self.vnode1Dsb.setObjectName(u"vnode1Dsb")
        self.vnode1Dsb.setMinimumSize(QSize(100, 0))
        self.vnode1Dsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.vnode1Dsb.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.nodeGL.addWidget(self.vnode1Dsb, 1, 2, 1, 1)

        self.node2Lbl = QLabel(self.nodeWgt)
        self.node2Lbl.setObjectName(u"node2Lbl")
        self.node2Lbl.setMinimumSize(QSize(50, 0))
        self.node2Lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.nodeGL.addWidget(self.node2Lbl, 3, 1, 1, 1)

        self.nodeLeftSpc = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.nodeGL.addItem(self.nodeLeftSpc, 0, 0, 1, 1)

        self.vnode1Lbl = QLabel(self.nodeWgt)
        self.vnode1Lbl.setObjectName(u"vnode1Lbl")
        self.vnode1Lbl.setMinimumSize(QSize(50, 0))
        self.vnode1Lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.nodeGL.addWidget(self.vnode1Lbl, 1, 1, 1, 1)

        self.node1CB = QComboBox(self.nodeWgt)
        self.node1CB.setObjectName(u"node1CB")
        self.node1CB.setMinimumSize(QSize(150, 0))

        self.nodeGL.addWidget(self.node1CB, 0, 2, 1, 1)

        self.nodeRightSpc = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.nodeGL.addItem(self.nodeRightSpc, 0, 3, 1, 1)

        self.vnode2Dsb = QDoubleSpinBox(self.nodeWgt)
        self.vnode2Dsb.setObjectName(u"vnode2Dsb")
        self.vnode2Dsb.setMinimumSize(QSize(100, 0))
        self.vnode2Dsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.vnode2Dsb.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.nodeGL.addWidget(self.vnode2Dsb, 4, 2, 1, 1)

        self.nodeVertSpc = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.nodeGL.addItem(self.nodeVertSpc, 2, 2, 1, 1)


        self.mainVL.addWidget(self.nodeWgt)

        self.parWgt = QWidget(Dialog)
        self.parWgt.setObjectName(u"parWgt")
        self.parWgt.setMinimumSize(QSize(0, 0))
        self.parGL = QGridLayout(self.parWgt)
        self.parGL.setSpacing(5)
        self.parGL.setObjectName(u"parGL")
        self.parGL.setContentsMargins(10, 10, 10, 10)
        self.unitParWgt = QLabel(self.parWgt)
        self.unitParWgt.setObjectName(u"unitParWgt")
        self.unitParWgt.setMinimumSize(QSize(45, 0))
        self.unitParWgt.setSizeIncrement(QSize(0, 0))

        self.parGL.addWidget(self.unitParWgt, 0, 3, 1, 1)

        self.parLbl = QLabel(self.parWgt)
        self.parLbl.setObjectName(u"parLbl")
        self.parLbl.setMinimumSize(QSize(50, 0))
        self.parLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.parGL.addWidget(self.parLbl, 0, 1, 1, 1)

        self.parLeftSpc = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.parGL.addItem(self.parLeftSpc, 0, 0, 1, 1)

        self.parDsb = QDoubleSpinBox(self.parWgt)
        self.parDsb.setObjectName(u"parDsb")
        self.parDsb.setMinimumSize(QSize(100, 0))
        self.parDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.parDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.parGL.addWidget(self.parDsb, 0, 2, 1, 1)

        self.parRightSpc = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.parGL.addItem(self.parRightSpc, 0, 4, 1, 1)


        self.mainVL.addWidget(self.parWgt)

        self.scaleProfWgt = QWidget(Dialog)
        self.scaleProfWgt.setObjectName(u"scaleProfWgt")
        self.scaleProfWgt.setStyleSheet(u"QRadioButton{\n"
"border: none;\n"
"\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.scaleProfWgt)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.scaleProfDsb = QDoubleSpinBox(self.scaleProfWgt)
        self.scaleProfDsb.setObjectName(u"scaleProfDsb")
        self.scaleProfDsb.setMinimumSize(QSize(100, 0))
        self.scaleProfDsb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.scaleProfDsb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.scaleProfDsb.setDecimals(4)
        self.scaleProfDsb.setMaximum(100.000000000000000)
        self.scaleProfDsb.setSingleStep(0.100000000000000)
        self.scaleProfDsb.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.scaleProfDsb, 0, 2, 1, 1)

        self.unitScaleProfWgt = QLabel(self.scaleProfWgt)
        self.unitScaleProfWgt.setObjectName(u"unitScaleProfWgt")
        self.unitScaleProfWgt.setMinimumSize(QSize(45, 0))
        self.unitScaleProfWgt.setSizeIncrement(QSize(0, 0))

        self.gridLayout_2.addWidget(self.unitScaleProfWgt, 0, 3, 1, 1)

        self.constScaleProfRB = QRadioButton(self.scaleProfWgt)
        self.constScaleProfRB.setObjectName(u"constScaleProfRB")
        self.constScaleProfRB.setChecked(True)

        self.gridLayout_2.addWidget(self.constScaleProfRB, 1, 2, 1, 1)

        self.sceleProfRightSpc = QSpacerItem(48, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.sceleProfRightSpc, 0, 4, 1, 1)

        self.scaleProfLbl = QLabel(self.scaleProfWgt)
        self.scaleProfLbl.setObjectName(u"scaleProfLbl")
        self.scaleProfLbl.setMinimumSize(QSize(50, 0))
        self.scaleProfLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.scaleProfLbl, 0, 1, 1, 1)

        self.scaleParLeftSpc = QSpacerItem(40, 17, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.scaleParLeftSpc, 0, 0, 1, 1)

        self.profScaleProfRB = QRadioButton(self.scaleProfWgt)
        self.profScaleProfRB.setObjectName(u"profScaleProfRB")

        self.gridLayout_2.addWidget(self.profScaleProfRB, 2, 2, 1, 1)


        self.mainVL.addWidget(self.scaleProfWgt)

        self.pictureProfWgt = QWidget(Dialog)
        self.pictureProfWgt.setObjectName(u"pictureProfWgt")
        self.pictureProfWgt.setMinimumSize(QSize(0, 0))
        self.pictureProfHL = QHBoxLayout(self.pictureProfWgt)
        self.pictureProfHL.setSpacing(10)
        self.pictureProfHL.setObjectName(u"pictureProfHL")
        self.pictureProfHL.setContentsMargins(0, 10, 0, 10)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.pictureProfHL.addItem(self.horizontalSpacer)

        self.pictureProfCenterWgt = QWidget(self.pictureProfWgt)
        self.pictureProfCenterWgt.setObjectName(u"pictureProfCenterWgt")
        self.pictureProfCenterWgt.setMinimumSize(QSize(170, 0))
        self.pictureProfCenterWgt.setStyleSheet(u"QWidget{\n"
"	border: None;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(255, 255, 255)	\n"
"}")
        self.pictureProfVL = QVBoxLayout(self.pictureProfCenterWgt)
        self.pictureProfVL.setSpacing(5)
        self.pictureProfVL.setObjectName(u"pictureProfVL")
        self.pictureProfVL.setContentsMargins(0, 0, 0, 0)
        self.profImgLbl = QLabel(self.pictureProfCenterWgt)
        self.profImgLbl.setObjectName(u"profImgLbl")
        font1 = QFont()
        font1.setPointSize(1)
        self.profImgLbl.setFont(font1)

        self.pictureProfVL.addWidget(self.profImgLbl)

        self.profOpenBtn = QPushButton(self.pictureProfCenterWgt)
        self.profOpenBtn.setObjectName(u"profOpenBtn")
        self.profOpenBtn.setMinimumSize(QSize(0, 20))

        self.pictureProfVL.addWidget(self.profOpenBtn)


        self.pictureProfHL.addWidget(self.pictureProfCenterWgt)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.pictureProfHL.addItem(self.horizontalSpacer_2)


        self.mainVL.addWidget(self.pictureProfWgt)

        self.servWgt = QWidget(Dialog)
        self.servWgt.setObjectName(u"servWgt")
        self.servWgt.setMinimumSize(QSize(0, 0))
        self.servWgt.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.servWgt)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.parRightSpc_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.parRightSpc_2, 0, 2, 1, 1)

        self.checkBox = QCheckBox(self.servWgt)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"border: none;")

        self.gridLayout_3.addWidget(self.checkBox, 0, 1, 1, 1)

        self.parLbl_2 = QLabel(self.servWgt)
        self.parLbl_2.setObjectName(u"parLbl_2")
        self.parLbl_2.setMinimumSize(QSize(100, 0))
        self.parLbl_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.parLbl_2, 0, 0, 1, 1)


        self.mainVL.addWidget(self.servWgt)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.mainVL.addItem(self.verticalSpacer)

        self.buttonsWgt = QWidget(Dialog)
        self.buttonsWgt.setObjectName(u"buttonsWgt")
        self.buttonsWgt.setMinimumSize(QSize(0, 30))
        self.buttonsWgt.setStyleSheet(u"*{\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton{\n"
"border:solid;\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(31, 31, 31); border: solid;\n"
"border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(64, 64, 64); border-style: inset\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.buttonsWgt)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.calcelBtn = QPushButton(self.buttonsWgt)
        self.calcelBtn.setObjectName(u"calcelBtn")
        self.calcelBtn.setMinimumSize(QSize(80, 20))

        self.horizontalLayout.addWidget(self.calcelBtn)

        self.buttonsSpc = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.buttonsSpc)

        self.saveBtn = QPushButton(self.buttonsWgt)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setMinimumSize(QSize(80, 20))

        self.horizontalLayout.addWidget(self.saveBtn)


        self.mainVL.addWidget(self.buttonsWgt)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Nuovo Elemento", None))
        self.nameLBL.setText(QCoreApplication.translate("Dialog", u"Nome Elemento", None))
        self.typeLbl.setText(QCoreApplication.translate("Dialog", u"Tipologia", None))
        self.node1Lbl.setText(QCoreApplication.translate("Dialog", u"Nodo 1", None))
        self.vnode2Lbl.setText(QCoreApplication.translate("Dialog", u"Vn2", None))
        self.vnode1Dsb.setSuffix(QCoreApplication.translate("Dialog", u" kV", None))
        self.node2Lbl.setText(QCoreApplication.translate("Dialog", u"Nodo 2", None))
        self.vnode1Lbl.setText(QCoreApplication.translate("Dialog", u"Vn1", None))
        self.vnode2Dsb.setSuffix(QCoreApplication.translate("Dialog", u" kV", None))
        self.unitParWgt.setText(QCoreApplication.translate("Dialog", u"unit", None))
        self.parLbl.setText(QCoreApplication.translate("Dialog", u"Par", None))
        self.unitScaleProfWgt.setText("")
        self.constScaleProfRB.setText(QCoreApplication.translate("Dialog", u"Costante", None))
        self.scaleProfLbl.setText(QCoreApplication.translate("Dialog", u"Scala", None))
        self.profScaleProfRB.setText(QCoreApplication.translate("Dialog", u"Profilo", None))
        self.profImgLbl.setText("")
        self.profOpenBtn.setText(QCoreApplication.translate("Dialog", u"Apri profilo", None))
        self.checkBox.setText("")
        self.parLbl_2.setText(QCoreApplication.translate("Dialog", u"Out of service", None))
        self.calcelBtn.setText(QCoreApplication.translate("Dialog", u"Annulla", None))
        self.saveBtn.setText(QCoreApplication.translate("Dialog", u"Salva", None))
    # retranslateUi

