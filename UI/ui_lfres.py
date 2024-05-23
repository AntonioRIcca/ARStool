# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lfresfIBoOU.ui'
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


class Ui_lfres_mainWGT(object):
    def setupUi(self, lfres_mainWGT):
        if lfres_mainWGT.objectName():
            lfres_mainWGT.setObjectName(u"lfres_mainWGT")
        lfres_mainWGT.resize(1123, 1237)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        lfres_mainWGT.setFont(font)
        lfres_mainWGT.setStyleSheet(u"")
        self.lfres_WGT = QWidget(lfres_mainWGT)
        self.lfres_WGT.setObjectName(u"lfres_WGT")
        self.lfres_WGT.setGeometry(QRect(30, 30, 480, 811))
        self.lfres_WGT.setMinimumSize(QSize(480, 700))
        self.lfres_WGT.setMaximumSize(QSize(600, 16777215))
        self.lfres_WGT.setStyleSheet(u"#lfres_WGT{\n"
"	background-color: #2c313c;\n"
"}\n"
"\n"
"#title_LBL{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#overall_GB, #loads_GB{\n"
"	background-color: #1f232a;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#extgrid_GB, #loads_GB, #loss_GB, #gen_GB, #bess_GB{	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #1f232a;\n"
" 	border: 1px solid  rgb(255, 255, 255);\n"
"	padding-top: 15 px\n"
"}\n"
"#extgrid_GB:title, #loads_GB:title, #loss_GB:title,#gen_GB:title, #bess_GB:title{\n"
"	subcontrol-origin:  margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 2px 1000px;\n"
"	background-color: rgb(0,0,0); \n"
" 	border: 1px solid  rgb(255, 255, 255);\n"
"}\n"
"\n"
"#p_eg_lbl_LBL, #p_eg_value_LBL, #p_eg_unit_LBL, \n"
"#p_loads_lbl_LBL, #p_loads_value_LBL, #p_loads_unit_LBL, \n"
"#p_gen_lbl_LBL, #p_gen_value_LBL, #p_gen_unit_LBL, \n"
"#p_loss_lbl_LBL, #p_loss_value_LBL, #p_loss_unit_LBL,\n"
"#p_bess_lbl_LBL, #p_bess_value_LBL, #p_bess_unit_LBL{\n"
"	color: rgb(170, 255, 127);\n"
"}\n"
"\n"
""
                        "#q_eg_lbl_LBL, #q_eg_value_LBL, #q_eg_unit_LBL, \n"
"#q_loads_lbl_LBL, #q_loads_value_LBL, #q_loads_unit_LBL, \n"
"#q_gen_lbl_LBL, #q_gen_value_LBL, #q_gen_unit_LBL, \n"
"#q_loss_lbl_LBL, #q_loss_value_LBL, #q_loss_unit_LBL, \n"
"#q_bess_lbl_LBL, #q_bess_value_LBL, #q_bess_unit_LBL{\n"
"	\n"
"	color: rgb(255, 170, 127);\n"
"}\n"
"")
        self.lfres_VL = QVBoxLayout(self.lfres_WGT)
        self.lfres_VL.setObjectName(u"lfres_VL")
        self.title_LBL = QLabel(self.lfres_WGT)
        self.title_LBL.setObjectName(u"title_LBL")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_LBL.sizePolicy().hasHeightForWidth())
        self.title_LBL.setSizePolicy(sizePolicy)
        self.title_LBL.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.title_LBL.setFont(font1)
        self.title_LBL.setAlignment(Qt.AlignCenter)

        self.lfres_VL.addWidget(self.title_LBL)

        self.lfres_top_WGT = QWidget(self.lfres_WGT)
        self.lfres_top_WGT.setObjectName(u"lfres_top_WGT")
        self.horizontalLayout = QHBoxLayout(self.lfres_top_WGT)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sx_WGT = QWidget(self.lfres_top_WGT)
        self.sx_WGT.setObjectName(u"sx_WGT")
        self.verticalLayout_2 = QVBoxLayout(self.sx_WGT)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.extgrid_GB = QGroupBox(self.sx_WGT)
        self.extgrid_GB.setObjectName(u"extgrid_GB")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.extgrid_GB.setFont(font2)
        self.extgrid_GB.setFlat(False)
        self.gridLayout_6 = QGridLayout(self.extgrid_GB)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.q_eg_value_LBL = QLabel(self.extgrid_GB)
        self.q_eg_value_LBL.setObjectName(u"q_eg_value_LBL")
        self.q_eg_value_LBL.setMinimumSize(QSize(0, 25))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.q_eg_value_LBL.setFont(font3)
        self.q_eg_value_LBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.q_eg_value_LBL, 2, 2, 1, 1)

        self.q_eg_lbl_LBL = QLabel(self.extgrid_GB)
        self.q_eg_lbl_LBL.setObjectName(u"q_eg_lbl_LBL")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.q_eg_lbl_LBL.sizePolicy().hasHeightForWidth())
        self.q_eg_lbl_LBL.setSizePolicy(sizePolicy1)
        self.q_eg_lbl_LBL.setMinimumSize(QSize(0, 25))
        self.q_eg_lbl_LBL.setFont(font3)
        self.q_eg_lbl_LBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.q_eg_lbl_LBL, 2, 1, 1, 1)

        self.q_eg_unit_LBL = QLabel(self.extgrid_GB)
        self.q_eg_unit_LBL.setObjectName(u"q_eg_unit_LBL")
        self.q_eg_unit_LBL.setMinimumSize(QSize(0, 25))
        self.q_eg_unit_LBL.setFont(font3)
        self.q_eg_unit_LBL.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.q_eg_unit_LBL, 2, 3, 1, 1)

        self.p_eg_unit_LBL = QLabel(self.extgrid_GB)
        self.p_eg_unit_LBL.setObjectName(u"p_eg_unit_LBL")
        self.p_eg_unit_LBL.setMinimumSize(QSize(0, 25))
        self.p_eg_unit_LBL.setFont(font3)
        self.p_eg_unit_LBL.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.p_eg_unit_LBL, 1, 3, 1, 1)

        self.p_eg_value_LBL = QLabel(self.extgrid_GB)
        self.p_eg_value_LBL.setObjectName(u"p_eg_value_LBL")
        self.p_eg_value_LBL.setMinimumSize(QSize(0, 25))
        self.p_eg_value_LBL.setFont(font3)
        self.p_eg_value_LBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.p_eg_value_LBL, 1, 2, 1, 1)

        self.p_eg_lbl_LBL = QLabel(self.extgrid_GB)
        self.p_eg_lbl_LBL.setObjectName(u"p_eg_lbl_LBL")
        sizePolicy1.setHeightForWidth(self.p_eg_lbl_LBL.sizePolicy().hasHeightForWidth())
        self.p_eg_lbl_LBL.setSizePolicy(sizePolicy1)
        self.p_eg_lbl_LBL.setMinimumSize(QSize(0, 25))
        self.p_eg_lbl_LBL.setFont(font3)
        self.p_eg_lbl_LBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.p_eg_lbl_LBL, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.extgrid_GB)

        self.o1_VSp = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.o1_VSp)

        self.loads_GB = QGroupBox(self.sx_WGT)
        self.loads_GB.setObjectName(u"loads_GB")
        self.loads_GB.setFont(font2)
        self.gridLayout_5 = QGridLayout(self.loads_GB)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.p_loads_lbl_LBL = QLabel(self.loads_GB)
        self.p_loads_lbl_LBL.setObjectName(u"p_loads_lbl_LBL")
        sizePolicy1.setHeightForWidth(self.p_loads_lbl_LBL.sizePolicy().hasHeightForWidth())
        self.p_loads_lbl_LBL.setSizePolicy(sizePolicy1)
        self.p_loads_lbl_LBL.setMinimumSize(QSize(0, 25))
        self.p_loads_lbl_LBL.setFont(font3)
        self.p_loads_lbl_LBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.p_loads_lbl_LBL, 3, 0, 1, 1)

        self.p_loads_value_LBL = QLabel(self.loads_GB)
        self.p_loads_value_LBL.setObjectName(u"p_loads_value_LBL")
        self.p_loads_value_LBL.setMinimumSize(QSize(0, 25))
        self.p_loads_value_LBL.setFont(font3)
        self.p_loads_value_LBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.p_loads_value_LBL, 3, 1, 1, 1)

        self.q_loads_lbl_LBL = QLabel(self.loads_GB)
        self.q_loads_lbl_LBL.setObjectName(u"q_loads_lbl_LBL")
        sizePolicy1.setHeightForWidth(self.q_loads_lbl_LBL.sizePolicy().hasHeightForWidth())
        self.q_loads_lbl_LBL.setSizePolicy(sizePolicy1)
        self.q_loads_lbl_LBL.setMinimumSize(QSize(0, 25))
        self.q_loads_lbl_LBL.setFont(font3)
        self.q_loads_lbl_LBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.q_loads_lbl_LBL, 4, 0, 1, 1)

        self.p_loads_unit_LBL = QLabel(self.loads_GB)
        self.p_loads_unit_LBL.setObjectName(u"p_loads_unit_LBL")
        self.p_loads_unit_LBL.setMinimumSize(QSize(0, 25))
        self.p_loads_unit_LBL.setFont(font3)
        self.p_loads_unit_LBL.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.p_loads_unit_LBL, 3, 2, 1, 1)

        self.q_loads_unit_LBL = QLabel(self.loads_GB)
        self.q_loads_unit_LBL.setObjectName(u"q_loads_unit_LBL")
        self.q_loads_unit_LBL.setMinimumSize(QSize(0, 25))
        self.q_loads_unit_LBL.setFont(font3)
        self.q_loads_unit_LBL.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.q_loads_unit_LBL, 4, 2, 1, 1)

        self.q_loads_value_LBL = QLabel(self.loads_GB)
        self.q_loads_value_LBL.setObjectName(u"q_loads_value_LBL")
        self.q_loads_value_LBL.setMinimumSize(QSize(0, 25))
        self.q_loads_value_LBL.setFont(font3)
        self.q_loads_value_LBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.q_loads_value_LBL, 4, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.loads_GB)

        self.o3_VSp = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.o3_VSp)

        self.bess_GB = QGroupBox(self.sx_WGT)
        self.bess_GB.setObjectName(u"bess_GB")
        self.bess_GB.setFont(font2)
        self.gridLayout_7 = QGridLayout(self.bess_GB)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.p_bess_lbl_LBL = QLabel(self.bess_GB)
        self.p_bess_lbl_LBL.setObjectName(u"p_bess_lbl_LBL")
        sizePolicy1.setHeightForWidth(self.p_bess_lbl_LBL.sizePolicy().hasHeightForWidth())
        self.p_bess_lbl_LBL.setSizePolicy(sizePolicy1)
        self.p_bess_lbl_LBL.setMinimumSize(QSize(0, 25))
        self.p_bess_lbl_LBL.setFont(font3)
        self.p_bess_lbl_LBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.p_bess_lbl_LBL, 3, 0, 1, 1)

        self.p_bess_value_LBL = QLabel(self.bess_GB)
        self.p_bess_value_LBL.setObjectName(u"p_bess_value_LBL")
        self.p_bess_value_LBL.setMinimumSize(QSize(0, 25))
        self.p_bess_value_LBL.setFont(font3)
        self.p_bess_value_LBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.p_bess_value_LBL, 3, 1, 1, 1)

        self.q_bess_lbl_LBL = QLabel(self.bess_GB)
        self.q_bess_lbl_LBL.setObjectName(u"q_bess_lbl_LBL")
        sizePolicy1.setHeightForWidth(self.q_bess_lbl_LBL.sizePolicy().hasHeightForWidth())
        self.q_bess_lbl_LBL.setSizePolicy(sizePolicy1)
        self.q_bess_lbl_LBL.setMinimumSize(QSize(0, 25))
        self.q_bess_lbl_LBL.setFont(font3)
        self.q_bess_lbl_LBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.q_bess_lbl_LBL, 4, 0, 1, 1)

        self.p_bess_unit_LBL = QLabel(self.bess_GB)
        self.p_bess_unit_LBL.setObjectName(u"p_bess_unit_LBL")
        self.p_bess_unit_LBL.setMinimumSize(QSize(0, 25))
        self.p_bess_unit_LBL.setFont(font3)
        self.p_bess_unit_LBL.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.p_bess_unit_LBL, 3, 2, 1, 1)

        self.q_bess_unit_LBL = QLabel(self.bess_GB)
        self.q_bess_unit_LBL.setObjectName(u"q_bess_unit_LBL")
        self.q_bess_unit_LBL.setMinimumSize(QSize(0, 25))
        self.q_bess_unit_LBL.setFont(font3)
        self.q_bess_unit_LBL.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.q_bess_unit_LBL, 4, 2, 1, 1)

        self.q_bess_value_LBL = QLabel(self.bess_GB)
        self.q_bess_value_LBL.setObjectName(u"q_bess_value_LBL")
        self.q_bess_value_LBL.setMinimumSize(QSize(0, 25))
        self.q_bess_value_LBL.setFont(font3)
        self.q_bess_value_LBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.q_bess_value_LBL, 4, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.bess_GB)


        self.horizontalLayout.addWidget(self.sx_WGT)

        self.dx_WGT = QWidget(self.lfres_top_WGT)
        self.dx_WGT.setObjectName(u"dx_WGT")
        self.verticalLayout_4 = QVBoxLayout(self.dx_WGT)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gen_GB = QGroupBox(self.dx_WGT)
        self.gen_GB.setObjectName(u"gen_GB")
        self.gen_GB.setFont(font2)
        self.gen_GB.setFlat(False)
        self.gridLayout_4 = QGridLayout(self.gen_GB)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.p_gen_lbl_LBL = QLabel(self.gen_GB)
        self.p_gen_lbl_LBL.setObjectName(u"p_gen_lbl_LBL")
        sizePolicy1.setHeightForWidth(self.p_gen_lbl_LBL.sizePolicy().hasHeightForWidth())
        self.p_gen_lbl_LBL.setSizePolicy(sizePolicy1)
        self.p_gen_lbl_LBL.setMinimumSize(QSize(0, 25))
        self.p_gen_lbl_LBL.setFont(font3)
        self.p_gen_lbl_LBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.p_gen_lbl_LBL, 2, 0, 1, 1)

        self.q_gen_unit_LBL = QLabel(self.gen_GB)
        self.q_gen_unit_LBL.setObjectName(u"q_gen_unit_LBL")
        self.q_gen_unit_LBL.setMinimumSize(QSize(0, 25))
        self.q_gen_unit_LBL.setFont(font3)
        self.q_gen_unit_LBL.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.q_gen_unit_LBL, 3, 2, 1, 1)

        self.q_gen_lbl_LBL = QLabel(self.gen_GB)
        self.q_gen_lbl_LBL.setObjectName(u"q_gen_lbl_LBL")
        sizePolicy1.setHeightForWidth(self.q_gen_lbl_LBL.sizePolicy().hasHeightForWidth())
        self.q_gen_lbl_LBL.setSizePolicy(sizePolicy1)
        self.q_gen_lbl_LBL.setMinimumSize(QSize(0, 25))
        self.q_gen_lbl_LBL.setFont(font3)
        self.q_gen_lbl_LBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.q_gen_lbl_LBL, 3, 0, 1, 1)

        self.q_gen_value_LBL = QLabel(self.gen_GB)
        self.q_gen_value_LBL.setObjectName(u"q_gen_value_LBL")
        self.q_gen_value_LBL.setMinimumSize(QSize(0, 25))
        self.q_gen_value_LBL.setFont(font3)
        self.q_gen_value_LBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.q_gen_value_LBL, 3, 1, 1, 1)

        self.p_gen_value_LBL = QLabel(self.gen_GB)
        self.p_gen_value_LBL.setObjectName(u"p_gen_value_LBL")
        self.p_gen_value_LBL.setMinimumSize(QSize(0, 25))
        self.p_gen_value_LBL.setFont(font3)
        self.p_gen_value_LBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.p_gen_value_LBL, 2, 1, 1, 1)

        self.p_gen_unit_LBL = QLabel(self.gen_GB)
        self.p_gen_unit_LBL.setObjectName(u"p_gen_unit_LBL")
        self.p_gen_unit_LBL.setMinimumSize(QSize(0, 25))
        self.p_gen_unit_LBL.setFont(font3)
        self.p_gen_unit_LBL.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.p_gen_unit_LBL, 2, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.gen_GB)

        self.o2_VSp = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.o2_VSp)

        self.loss_GB = QGroupBox(self.dx_WGT)
        self.loss_GB.setObjectName(u"loss_GB")
        self.loss_GB.setFont(font2)
        self.gridLayout = QGridLayout(self.loss_GB)
        self.gridLayout.setObjectName(u"gridLayout")
        self.p_loss_lbl_LBL = QLabel(self.loss_GB)
        self.p_loss_lbl_LBL.setObjectName(u"p_loss_lbl_LBL")
        sizePolicy1.setHeightForWidth(self.p_loss_lbl_LBL.sizePolicy().hasHeightForWidth())
        self.p_loss_lbl_LBL.setSizePolicy(sizePolicy1)
        self.p_loss_lbl_LBL.setMinimumSize(QSize(0, 25))
        self.p_loss_lbl_LBL.setFont(font3)
        self.p_loss_lbl_LBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.p_loss_lbl_LBL, 0, 0, 1, 1)

        self.p_loss_value_LBL = QLabel(self.loss_GB)
        self.p_loss_value_LBL.setObjectName(u"p_loss_value_LBL")
        self.p_loss_value_LBL.setMinimumSize(QSize(0, 25))
        self.p_loss_value_LBL.setFont(font3)
        self.p_loss_value_LBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.p_loss_value_LBL, 0, 1, 1, 1)

        self.p_loss_unit_LBL = QLabel(self.loss_GB)
        self.p_loss_unit_LBL.setObjectName(u"p_loss_unit_LBL")
        self.p_loss_unit_LBL.setMinimumSize(QSize(0, 25))
        self.p_loss_unit_LBL.setFont(font3)
        self.p_loss_unit_LBL.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.p_loss_unit_LBL, 0, 2, 1, 1)

        self.q_loss_lbl_LBL = QLabel(self.loss_GB)
        self.q_loss_lbl_LBL.setObjectName(u"q_loss_lbl_LBL")
        sizePolicy1.setHeightForWidth(self.q_loss_lbl_LBL.sizePolicy().hasHeightForWidth())
        self.q_loss_lbl_LBL.setSizePolicy(sizePolicy1)
        self.q_loss_lbl_LBL.setMinimumSize(QSize(0, 25))
        self.q_loss_lbl_LBL.setFont(font3)
        self.q_loss_lbl_LBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.q_loss_lbl_LBL, 1, 0, 1, 1)

        self.q_loss_value_LBL = QLabel(self.loss_GB)
        self.q_loss_value_LBL.setObjectName(u"q_loss_value_LBL")
        self.q_loss_value_LBL.setMinimumSize(QSize(0, 25))
        self.q_loss_value_LBL.setFont(font3)
        self.q_loss_value_LBL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.q_loss_value_LBL, 1, 1, 1, 1)

        self.q_loss_unit_LBL = QLabel(self.loss_GB)
        self.q_loss_unit_LBL.setObjectName(u"q_loss_unit_LBL")
        self.q_loss_unit_LBL.setMinimumSize(QSize(0, 25))
        self.q_loss_unit_LBL.setFont(font3)
        self.q_loss_unit_LBL.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.q_loss_unit_LBL, 1, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.loss_GB)


        self.horizontalLayout.addWidget(self.dx_WGT, 0, Qt.AlignTop)


        self.lfres_VL.addWidget(self.lfres_top_WGT)

        self.lfres_center_WGT = QWidget(self.lfres_WGT)
        self.lfres_center_WGT.setObjectName(u"lfres_center_WGT")
        self.lfres_center_WGT.setMinimumSize(QSize(0, 20))
        self.lfres_center_WGT.setMaximumSize(QSize(16777215, 300))
        self.lfres_center_WGT.setStyleSheet(u"background-color: rgb(255, 255, 127);")

        self.lfres_VL.addWidget(self.lfres_center_WGT)

        self.lfres_bottom_WGT = QWidget(self.lfres_WGT)
        self.lfres_bottom_WGT.setObjectName(u"lfres_bottom_WGT")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lfres_bottom_WGT.sizePolicy().hasHeightForWidth())
        self.lfres_bottom_WGT.setSizePolicy(sizePolicy2)
        self.lfres_bottom_WGT.setMinimumSize(QSize(300, 200))
        self.lfres_bottom_WGT.setMaximumSize(QSize(600, 600))
        self.lfres_bottom_WGT.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.image_VL = QVBoxLayout(self.lfres_bottom_WGT)
        self.image_VL.setObjectName(u"image_VL")

        self.lfres_VL.addWidget(self.lfres_bottom_WGT)


        self.retranslateUi(lfres_mainWGT)

        QMetaObject.connectSlotsByName(lfres_mainWGT)
    # setupUi

    def retranslateUi(self, lfres_mainWGT):
        lfres_mainWGT.setWindowTitle(QCoreApplication.translate("lfres_mainWGT", u"Form", None))
        self.title_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"LoadFLow", None))
        self.extgrid_GB.setTitle(QCoreApplication.translate("lfres_mainWGT", u"External Grid ", None))
        self.q_eg_value_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"2000.00", None))
        self.q_eg_lbl_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"Reactive Power:", None))
        self.q_eg_unit_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"kVar", None))
        self.p_eg_unit_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"kW", None))
        self.p_eg_value_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"1258.25", None))
        self.p_eg_lbl_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"Active Power:", None))
        self.loads_GB.setTitle(QCoreApplication.translate("lfres_mainWGT", u"Loads", None))
        self.p_loads_lbl_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"Active Power:", None))
        self.p_loads_value_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"1258.25", None))
        self.q_loads_lbl_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"Reactive Power:", None))
        self.p_loads_unit_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"kW", None))
        self.q_loads_unit_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"kVar", None))
        self.q_loads_value_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"2000.00", None))
        self.bess_GB.setTitle(QCoreApplication.translate("lfres_mainWGT", u"BESS", None))
        self.p_bess_lbl_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"Active Power:", None))
        self.p_bess_value_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"1258.25", None))
        self.q_bess_lbl_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"Reactive Power:", None))
        self.p_bess_unit_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"kW", None))
        self.q_bess_unit_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"kVar", None))
        self.q_bess_value_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"2000.00", None))
        self.gen_GB.setTitle(QCoreApplication.translate("lfres_mainWGT", u"Generators", None))
        self.p_gen_lbl_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"Active Power:", None))
        self.q_gen_unit_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"kVar", None))
        self.q_gen_lbl_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"Reactive Power:", None))
        self.q_gen_value_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"2000.00", None))
        self.p_gen_value_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"1258.25", None))
        self.p_gen_unit_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"kW", None))
        self.loss_GB.setTitle(QCoreApplication.translate("lfres_mainWGT", u"Losses", None))
        self.p_loss_lbl_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"Active Power:", None))
        self.p_loss_value_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"1258.25", None))
        self.p_loss_unit_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"kW", None))
        self.q_loss_lbl_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"Reactive Power:", None))
        self.q_loss_value_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"2000.00", None))
        self.q_loss_unit_LBL.setText(QCoreApplication.translate("lfres_mainWGT", u"kVar", None))
    # retranslateUi

