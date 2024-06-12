# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_elementePropertiesllUrpZ.ui'
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
        Form.resize(785, 829)
        Form.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.propertiesWgt = QWidget(Form)
        self.propertiesWgt.setObjectName(u"propertiesWgt")
        self.propertiesWgt.setGeometry(QRect(140, 40, 148, 651))
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
"}")
        self.propertiesVL = QVBoxLayout(self.propertiesWgt)
        self.propertiesVL.setSpacing(20)
        self.propertiesVL.setObjectName(u"propertiesVL")
        self.propertiesVL.setContentsMargins(5, 5, 5, 5)
        self.lfWgt = QWidget(self.propertiesWgt)
        self.lfWgt.setObjectName(u"lfWgt")
        self.lfWgt.setMinimumSize(QSize(0, 0))
        self.lfWgt.setMaximumSize(QSize(16777215, 1000))
        self.lfWgt.setStyleSheet(u"")
        self.lfVL = QVBoxLayout(self.lfWgt)
        self.lfVL.setSpacing(6)
        self.lfVL.setObjectName(u"lfVL")
        self.lfVL.setContentsMargins(2, 0, 2, 0)
        self.lfPls = QPushButton(self.lfWgt)
        self.lfPls.setObjectName(u"lfPls")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfPls.sizePolicy().hasHeightForWidth())
        self.lfPls.setSizePolicy(sizePolicy)
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

        self.lineEdit = QLineEdit(self.lfNodeWgt)
        self.lineEdit.setObjectName(u"lineEdit")

        self.lfNodeGL.addWidget(self.lineEdit, 0, 1, 1, 1)


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
        self.lfPls.raise_()
        self.lfResMainWgt.raise_()
        self.lfParMainWgt.raise_()

        self.propertiesVL.addWidget(self.lfWgt)

        self.relWgt = QWidget(self.propertiesWgt)
        self.relWgt.setObjectName(u"relWgt")
        self.relWgt.setMaximumSize(QSize(16777215, 500))
        self.relWgt.setStyleSheet(u"*{\n"
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
"}")
        self.relVL = QVBoxLayout(self.relWgt)
        self.relVL.setObjectName(u"relVL")
        self.relVL.setContentsMargins(2, 0, 2, 0)
        self.relPls = QPushButton(self.relWgt)
        self.relPls.setObjectName(u"relPls")
        sizePolicy.setHeightForWidth(self.relPls.sizePolicy().hasHeightForWidth())
        self.relPls.setSizePolicy(sizePolicy)
        self.relPls.setMinimumSize(QSize(0, 20))

        self.relVL.addWidget(self.relPls)

        self.relParLbl = QLabel(self.relWgt)
        self.relParLbl.setObjectName(u"relParLbl")
        self.relParLbl.setAlignment(Qt.AlignCenter)

        self.relVL.addWidget(self.relParLbl)

        self.reParWgt = QWidget(self.relWgt)
        self.reParWgt.setObjectName(u"reParWgt")
        self.reParWgt.setStyleSheet(u"")
        self.relParGL = QGridLayout(self.reParWgt)
        self.relParGL.setObjectName(u"relParGL")
        self.label_7 = QLabel(self.reParWgt)
        self.label_7.setObjectName(u"label_7")

        self.relParGL.addWidget(self.label_7, 0, 0, 1, 1)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.reParWgt)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_4.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.relParGL.addWidget(self.doubleSpinBox_4, 0, 1, 1, 1)

        self.label_8 = QLabel(self.reParWgt)
        self.label_8.setObjectName(u"label_8")

        self.relParGL.addWidget(self.label_8, 3, 2, 1, 1)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.reParWgt)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_5.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.relParGL.addWidget(self.doubleSpinBox_5, 3, 1, 1, 1)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.reParWgt)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        self.doubleSpinBox_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_6.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.relParGL.addWidget(self.doubleSpinBox_6, 1, 1, 1, 1)

        self.label_9 = QLabel(self.reParWgt)
        self.label_9.setObjectName(u"label_9")

        self.relParGL.addWidget(self.label_9, 3, 0, 1, 1)

        self.label_10 = QLabel(self.reParWgt)
        self.label_10.setObjectName(u"label_10")

        self.relParGL.addWidget(self.label_10, 1, 2, 1, 1)

        self.label_11 = QLabel(self.reParWgt)
        self.label_11.setObjectName(u"label_11")

        self.relParGL.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_12 = QLabel(self.reParWgt)
        self.label_12.setObjectName(u"label_12")

        self.relParGL.addWidget(self.label_12, 0, 2, 1, 1)


        self.relVL.addWidget(self.reParWgt)

        self.relLine = QFrame(self.relWgt)
        self.relLine.setObjectName(u"relLine")
        self.relLine.setMaximumSize(QSize(16777215, 1))
        self.relLine.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.relLine.setFrameShape(QFrame.HLine)
        self.relLine.setFrameShadow(QFrame.Sunken)

        self.relVL.addWidget(self.relLine)

        self.relResLbl = QLabel(self.relWgt)
        self.relResLbl.setObjectName(u"relResLbl")
        self.relResLbl.setAlignment(Qt.AlignCenter)

        self.relVL.addWidget(self.relResLbl)

        self.relResWgt = QWidget(self.relWgt)
        self.relResWgt.setObjectName(u"relResWgt")
        self.relResGL = QGridLayout(self.relResWgt)
        self.relResGL.setObjectName(u"relResGL")
        self.label_25 = QLabel(self.relResWgt)
        self.label_25.setObjectName(u"label_25")

        self.relResGL.addWidget(self.label_25, 3, 0, 1, 1)

        self.label_27 = QLabel(self.relResWgt)
        self.label_27.setObjectName(u"label_27")

        self.relResGL.addWidget(self.label_27, 1, 0, 1, 1)

        self.label_26 = QLabel(self.relResWgt)
        self.label_26.setObjectName(u"label_26")

        self.relResGL.addWidget(self.label_26, 1, 2, 1, 1)

        self.label_28 = QLabel(self.relResWgt)
        self.label_28.setObjectName(u"label_28")

        self.relResGL.addWidget(self.label_28, 0, 2, 1, 1)

        self.label_23 = QLabel(self.relResWgt)
        self.label_23.setObjectName(u"label_23")

        self.relResGL.addWidget(self.label_23, 0, 0, 1, 1)

        self.label_24 = QLabel(self.relResWgt)
        self.label_24.setObjectName(u"label_24")

        self.relResGL.addWidget(self.label_24, 3, 2, 1, 1)

        self.doubleSpinBox_11 = QDoubleSpinBox(self.relResWgt)
        self.doubleSpinBox_11.setObjectName(u"doubleSpinBox_11")
        self.doubleSpinBox_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_11.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.relResGL.addWidget(self.doubleSpinBox_11, 3, 1, 1, 1)

        self.doubleSpinBox_10 = QDoubleSpinBox(self.relResWgt)
        self.doubleSpinBox_10.setObjectName(u"doubleSpinBox_10")
        self.doubleSpinBox_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_10.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.relResGL.addWidget(self.doubleSpinBox_10, 0, 1, 1, 1)

        self.doubleSpinBox_12 = QDoubleSpinBox(self.relResWgt)
        self.doubleSpinBox_12.setObjectName(u"doubleSpinBox_12")
        self.doubleSpinBox_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_12.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.relResGL.addWidget(self.doubleSpinBox_12, 1, 1, 1, 1)


        self.relVL.addWidget(self.relResWgt)

        self.relParLbl.raise_()
        self.reParWgt.raise_()
        self.relResLbl.raise_()
        self.relResWgt.raise_()
        self.relLine.raise_()
        self.relPls.raise_()

        self.propertiesVL.addWidget(self.relWgt)

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


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lfPls.setText(QCoreApplication.translate("Form", u"LoadFlow", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"HV Node", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"Busbar", None))
        self.lfParLbl.setText(QCoreApplication.translate("Form", u"Parameters", None))
        self.label.setText(QCoreApplication.translate("Form", u"Power", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"unit", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Power", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"unit", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Power", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"unit", None))
        self.lfResLbl.setText(QCoreApplication.translate("Form", u"Results", None))
        self.relPls.setText(QCoreApplication.translate("Form", u"Reliability", None))
        self.relParLbl.setText(QCoreApplication.translate("Form", u"Parameters", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Power", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"unit", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Power", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"unit", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Power", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"unit", None))
        self.relResLbl.setText(QCoreApplication.translate("Form", u"Results", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Power", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"Power", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"unit", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"unit", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Power", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"unit", None))
        self.savePLS.setText(QCoreApplication.translate("Form", u"Salva", None))
        self.cancelPLS.setText(QCoreApplication.translate("Form", u"Annulla", None))
    # retranslateUi

