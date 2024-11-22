# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_uiqxSSoe.ui'
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

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1350, 900)
        MainWindow.setBaseSize(QSize(1200, 800))
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: #1f232a;\n"
"}\n"
"\n"
"#leftMenuSubContainer{\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"#leftMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#centerMenuSubContainer, #rightMenuSubContainer{\n"
"	background-color: #2c313c;\n"
"	\n"
"}\n"
"\n"
"#frame_4, #frame_8, #popupNotificationSubContainer{\n"
"	background-color: #16191d;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#headerContainer, #footerContainer{\n"
"	background-color: #2c313c;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMinimumSize(QSize(150, 0))
        self.leftMenuContainer.setMaximumSize(QSize(53, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.leftMenuSubContainer.setMinimumSize(QSize(0, 0))
        self.leftMenuSubContainer.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setMinimumSize(QSize(0, 40))
        self.menuBtn.setMaximumSize(QSize(16777215, 40))
        self.menuBtn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))
        self.menuBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setMinimumSize(QSize(0, 40))
        self.homeBtn.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.homeBtn.setFont(font)
        self.homeBtn.setStyleSheet(u"background-color: #1f232a;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))
        self.homeBtn.setFlat(False)

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.dataBtn = QPushButton(self.frame_2)
        self.dataBtn.setObjectName(u"dataBtn")
        self.dataBtn.setMinimumSize(QSize(0, 40))
        self.dataBtn.setMaximumSize(QSize(150, 40))
        self.dataBtn.setFont(font)
        self.dataBtn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/analysis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dataBtn.setIcon(icon2)
        self.dataBtn.setIconSize(QSize(24, 24))
        self.dataBtn.setFlat(False)

        self.verticalLayout_3.addWidget(self.dataBtn)

        self.reportBtn = QPushButton(self.frame_2)
        self.reportBtn.setObjectName(u"reportBtn")
        self.reportBtn.setMinimumSize(QSize(0, 40))
        self.reportBtn.setMaximumSize(QSize(16777215, 40))
        self.reportBtn.setFont(font)
        self.reportBtn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/print.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reportBtn.setIcon(icon3)
        self.reportBtn.setIconSize(QSize(24, 24))
        self.reportBtn.setFlat(False)

        self.verticalLayout_3.addWidget(self.reportBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.gridFrm = QFrame(self.leftMenuSubContainer)
        self.gridFrm.setObjectName(u"gridFrm")
        self.gridFrm.setFrameShape(QFrame.StyledPanel)
        self.gridFrm.setFrameShadow(QFrame.Raised)
        self.gridFrmVL = QVBoxLayout(self.gridFrm)
        self.gridFrmVL.setSpacing(0)
        self.gridFrmVL.setObjectName(u"gridFrmVL")
        self.gridFrmVL.setContentsMargins(0, 10, 0, 10)
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridFrmVL.addItem(self.verticalSpacer_6)

        self.loadProfilesBtn = QPushButton(self.gridFrm)
        self.loadProfilesBtn.setObjectName(u"loadProfilesBtn")
        self.loadProfilesBtn.setMinimumSize(QSize(0, 40))
        self.loadProfilesBtn.setMaximumSize(QSize(16777215, 40))
        self.loadProfilesBtn.setFont(font)
        self.loadProfilesBtn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/trend.png", QSize(), QIcon.Normal, QIcon.Off)
        self.loadProfilesBtn.setIcon(icon4)
        self.loadProfilesBtn.setIconSize(QSize(24, 24))
        self.loadProfilesBtn.setFlat(False)

        self.gridFrmVL.addWidget(self.loadProfilesBtn)

        self.restartBtn = QPushButton(self.gridFrm)
        self.restartBtn.setObjectName(u"restartBtn")
        self.restartBtn.setMinimumSize(QSize(0, 40))
        self.restartBtn.setMaximumSize(QSize(16777215, 40))
        self.restartBtn.setFont(font)
        self.restartBtn.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/restart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restartBtn.setIcon(icon5)
        self.restartBtn.setIconSize(QSize(24, 24))
        self.restartBtn.setFlat(False)

        self.gridFrmVL.addWidget(self.restartBtn)


        self.verticalLayout_2.addWidget(self.gridFrm)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_11 = QFrame(self.leftMenuSubContainer)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_11)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.loadflow_Btn = QPushButton(self.frame_11)
        self.loadflow_Btn.setObjectName(u"loadflow_Btn")
        self.loadflow_Btn.setMinimumSize(QSize(0, 40))
        self.loadflow_Btn.setMaximumSize(QSize(16777215, 40))
        self.loadflow_Btn.setFont(font)
        self.loadflow_Btn.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/loadflow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.loadflow_Btn.setIcon(icon6)
        self.loadflow_Btn.setIconSize(QSize(24, 24))
        self.loadflow_Btn.setFlat(False)

        self.verticalLayout_16.addWidget(self.loadflow_Btn)

        self.anom_Btn = QPushButton(self.frame_11)
        self.anom_Btn.setObjectName(u"anom_Btn")
        self.anom_Btn.setMinimumSize(QSize(0, 40))
        self.anom_Btn.setMaximumSize(QSize(16777215, 40))
        self.anom_Btn.setFont(font)
        self.anom_Btn.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/anomaly.png", QSize(), QIcon.Normal, QIcon.Off)
        self.anom_Btn.setIcon(icon7)
        self.anom_Btn.setIconSize(QSize(24, 24))
        self.anom_Btn.setFlat(False)

        self.verticalLayout_16.addWidget(self.anom_Btn)

        self.opf_Btn = QPushButton(self.frame_11)
        self.opf_Btn.setObjectName(u"opf_Btn")
        self.opf_Btn.setMinimumSize(QSize(0, 40))
        self.opf_Btn.setMaximumSize(QSize(16777215, 40))
        self.opf_Btn.setFont(font)
        self.opf_Btn.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/opf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.opf_Btn.setIcon(icon8)
        self.opf_Btn.setIconSize(QSize(24, 24))
        self.opf_Btn.setFlat(False)

        self.verticalLayout_16.addWidget(self.opf_Btn)

        self.reliabilithy_Btn = QPushButton(self.frame_11)
        self.reliabilithy_Btn.setObjectName(u"reliabilithy_Btn")
        self.reliabilithy_Btn.setMinimumSize(QSize(0, 40))
        self.reliabilithy_Btn.setMaximumSize(QSize(16777215, 40))
        self.reliabilithy_Btn.setFont(font)
        self.reliabilithy_Btn.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/reliability.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reliabilithy_Btn.setIcon(icon9)
        self.reliabilithy_Btn.setIconSize(QSize(24, 24))
        self.reliabilithy_Btn.setFlat(False)

        self.verticalLayout_16.addWidget(self.reliabilithy_Btn)

        self.reliabilithy_Btn_2 = QPushButton(self.frame_11)
        self.reliabilithy_Btn_2.setObjectName(u"reliabilithy_Btn_2")
        self.reliabilithy_Btn_2.setMinimumSize(QSize(0, 40))
        self.reliabilithy_Btn_2.setMaximumSize(QSize(16777215, 40))
        self.reliabilithy_Btn_2.setFont(font)
        self.reliabilithy_Btn_2.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/adequacy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reliabilithy_Btn_2.setIcon(icon10)
        self.reliabilithy_Btn_2.setIconSize(QSize(24, 24))
        self.reliabilithy_Btn_2.setFlat(False)

        self.verticalLayout_16.addWidget(self.reliabilithy_Btn_2)

        self.gidman_Btn = QPushButton(self.frame_11)
        self.gidman_Btn.setObjectName(u"gidman_Btn")
        self.gidman_Btn.setMinimumSize(QSize(0, 40))
        self.gidman_Btn.setMaximumSize(QSize(16777215, 40))
        self.gidman_Btn.setFont(font)
        self.gidman_Btn.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/gridmanagement.png", QSize(), QIcon.Normal, QIcon.Off)
        self.gidman_Btn.setIcon(icon11)
        self.gidman_Btn.setIconSize(QSize(24, 24))
        self.gidman_Btn.setFlat(False)

        self.verticalLayout_16.addWidget(self.gidman_Btn)

        self.onr_Btn = QPushButton(self.frame_11)
        self.onr_Btn.setObjectName(u"onr_Btn")
        self.onr_Btn.setMinimumSize(QSize(0, 40))
        self.onr_Btn.setMaximumSize(QSize(16777215, 40))
        self.onr_Btn.setFont(font)
        self.onr_Btn.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/onr.png", QSize(), QIcon.Normal, QIcon.Off)
        self.onr_Btn.setIcon(icon12)
        self.onr_Btn.setIconSize(QSize(24, 24))
        self.onr_Btn.setFlat(False)

        self.verticalLayout_16.addWidget(self.onr_Btn)


        self.verticalLayout_2.addWidget(self.frame_11)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setMinimumSize(QSize(0, 40))
        self.settingsBtn.setMaximumSize(QSize(16777215, 40))
        self.settingsBtn.setFont(font)
        self.settingsBtn.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon13)
        self.settingsBtn.setIconSize(QSize(24, 24))
        self.settingsBtn.setFlat(False)

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.frame_3)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setMinimumSize(QSize(0, 40))
        self.infoBtn.setMaximumSize(QSize(16777215, 40))
        self.infoBtn.setFont(font)
        self.infoBtn.setStyleSheet(u"")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon14)
        self.infoBtn.setIconSize(QSize(24, 24))
        self.infoBtn.setFlat(False)

        self.verticalLayout_4.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setMinimumSize(QSize(0, 40))
        self.helpBtn.setMaximumSize(QSize(16777215, 40))
        self.helpBtn.setFont(font)
        self.helpBtn.setStyleSheet(u"")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon15)
        self.helpBtn.setIconSize(QSize(24, 24))
        self.helpBtn.setFlat(False)

        self.verticalLayout_4.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.closeCenterMenuBtn = QPushButton(self.frame_4)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon16)
        self.closeCenterMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.centerMenuPages = QCustomStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.centerMenuPages.setMinimumSize(QSize(0, 0))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.centerMenuPages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.centerMenuPages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.centerMenuPages.addWidget(self.page_3)

        self.verticalLayout_6.addWidget(self.centerMenuPages)


        self.verticalLayout_5.addWidget(self.centerMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(64, 30))
        self.label_5.setPixmap(QPixmap(u":/images/LogoENEA_eng_200x80.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_6.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.notificationBtn = QPushButton(self.frame_6)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/notifications.png", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon17)
        self.notificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.notificationBtn)

        self.moreMenuBtn = QPushButton(self.frame_6)
        self.moreMenuBtn.setObjectName(u"moreMenuBtn")
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/dots.png", QSize(), QIcon.Normal, QIcon.Off)
        self.moreMenuBtn.setIcon(icon18)
        self.moreMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.moreMenuBtn)

        self.profileMenuBtn = QPushButton(self.frame_6)
        self.profileMenuBtn.setObjectName(u"profileMenuBtn")
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profileMenuBtn.setIcon(icon19)
        self.profileMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.profileMenuBtn)


        self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon20 = QIcon()
        icon20.addFile(u":/icons/icons/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon20)

        self.horizontalLayout_4.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon21 = QIcon()
        icon21.addFile(u":/icons/icons/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon21)

        self.horizontalLayout_4.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        icon22 = QIcon()
        icon22.addFile(u":/icons/icons/close2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon22)

        self.horizontalLayout_4.addWidget(self.closeBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy2)
        self.mainBodyContent.setMinimumSize(QSize(600, 400))
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.verticalLayout_15 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.home_PG = QWidget()
        self.home_PG.setObjectName(u"home_PG")
        self.home_VL = QVBoxLayout(self.home_PG)
        self.home_VL.setObjectName(u"home_VL")
        self.home_WGT = QWidget(self.home_PG)
        self.home_WGT.setObjectName(u"home_WGT")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.home_WGT.sizePolicy().hasHeightForWidth())
        self.home_WGT.setSizePolicy(sizePolicy3)
        self.horizontalLayout_13 = QHBoxLayout(self.home_WGT)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_10 = QLabel(self.home_WGT)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_10)


        self.home_VL.addWidget(self.home_WGT)

        self.mainPages.addWidget(self.home_PG)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_17 = QVBoxLayout(self.page_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_11 = QLabel(self.page_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_11)

        self.mainPages.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_18 = QVBoxLayout(self.page_8)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_12 = QLabel(self.page_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_12)

        self.mainPages.addWidget(self.page_8)

        self.verticalLayout_15.addWidget(self.mainPages)


        self.horizontalLayout_8.addWidget(self.mainContentsContainer)

        self.rightMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(0, 0))
        self.rightMenuContainer.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_12 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.frame_8 = QFrame(self.rightMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.rightMenu_LBL = QLabel(self.frame_8)
        self.rightMenu_LBL.setObjectName(u"rightMenu_LBL")
        self.rightMenu_LBL.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.rightMenu_LBL)

        self.elemNameLE = QLineEdit(self.frame_8)
        self.elemNameLE.setObjectName(u"elemNameLE")

        self.horizontalLayout_10.addWidget(self.elemNameLE)

        self.closeRightMenuBtn = QPushButton(self.frame_8)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setIcon(icon16)
        self.closeRightMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.rightMenuPages = QCustomStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.rightMenuPages.setStyleSheet(u"*{}\n"
"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0); border: solid;\n"
"	border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(64, 64, 64); border-style: inset\n"
"}")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_13 = QVBoxLayout(self.page_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(10, 10, 10, 10)
        self.lfWgt = QWidget(self.page_4)
        self.lfWgt.setObjectName(u"lfWgt")
        self.lfWgt.setMaximumSize(QSize(16777215, 35))
        self.verticalLayout_21 = QVBoxLayout(self.lfWgt)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, -1, 0, -1)
        self.lfWgtPls = QPushButton(self.lfWgt)
        self.lfWgtPls.setObjectName(u"lfWgtPls")
        self.lfWgtPls.setMinimumSize(QSize(0, 25))

        self.verticalLayout_21.addWidget(self.lfWgtPls)

        self.lfParLbl = QLabel(self.lfWgt)
        self.lfParLbl.setObjectName(u"lfParLbl")
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.lfParLbl.setFont(font3)
        self.lfParLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.lfParLbl)

        self.lfParWgt = QWidget(self.lfWgt)
        self.lfParWgt.setObjectName(u"lfParWgt")
        self.lfParWgt.setStyleSheet(u"*{}\n"
"\n"
"QDoubleSpinBox{\n"
"	border: solid;\n"
"	border-width: 0.5px;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")
        self.gridLayout = QGridLayout(self.lfParWgt)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(5, 0, 5, 0)
        self.label_7 = QLabel(self.lfParWgt)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.lfParWgt)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimumSize(QSize(60, 0))
        self.doubleSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout.addWidget(self.doubleSpinBox, 0, 1, 1, 1)

        self.label_8 = QLabel(self.lfParWgt)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)


        self.verticalLayout_21.addWidget(self.lfParWgt)

        self.lfResLbl = QLabel(self.lfWgt)
        self.lfResLbl.setObjectName(u"lfResLbl")
        self.lfResLbl.setFont(font3)
        self.lfResLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.lfResLbl)

        self.lfResWgt = QWidget(self.lfWgt)
        self.lfResWgt.setObjectName(u"lfResWgt")
        self.lfResWgt.setStyleSheet(u"*{}\n"
"\n"
"QDoubleSpinBox{\n"
"	border: solid;\n"
"	border-width: 0.5px;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")
        self.gridLayout_5 = QGridLayout(self.lfResWgt)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(6)
        self.gridLayout_5.setContentsMargins(5, 0, 5, 0)
        self.doubleSpinBox_5 = QDoubleSpinBox(self.lfResWgt)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setMinimumSize(QSize(60, 0))
        self.doubleSpinBox_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_5.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout_5.addWidget(self.doubleSpinBox_5, 0, 1, 1, 1)

        self.label_23 = QLabel(self.lfResWgt)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_5.addWidget(self.label_23, 0, 2, 1, 1)

        self.label_24 = QLabel(self.lfResWgt)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_5.addWidget(self.label_24, 0, 0, 1, 1)


        self.verticalLayout_21.addWidget(self.lfResWgt)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_21.addItem(self.verticalSpacer_3)


        self.verticalLayout_13.addWidget(self.lfWgt)

        self.relWgt = QWidget(self.page_4)
        self.relWgt.setObjectName(u"relWgt")
        self.relWgt.setMaximumSize(QSize(16777215, 35))
        self.verticalLayout_22 = QVBoxLayout(self.relWgt)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, -1, 0, -1)
        self.relWgtPls = QPushButton(self.relWgt)
        self.relWgtPls.setObjectName(u"relWgtPls")
        self.relWgtPls.setMinimumSize(QSize(0, 25))

        self.verticalLayout_22.addWidget(self.relWgtPls)

        self.relParLbl = QLabel(self.relWgt)
        self.relParLbl.setObjectName(u"relParLbl")
        self.relParLbl.setFont(font3)
        self.relParLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.relParLbl)

        self.relParWgt = QWidget(self.relWgt)
        self.relParWgt.setObjectName(u"relParWgt")
        self.relParWgt.setStyleSheet(u"*{}\n"
"\n"
"QDoubleSpinBox{\n"
"	border: solid;\n"
"	border-width: 0.5px;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")
        self.gridLayout_2 = QGridLayout(self.relParWgt)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setContentsMargins(5, 0, 5, 0)
        self.label_17 = QLabel(self.relParWgt)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 0, 0, 1, 1)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.relParWgt)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setMinimumSize(QSize(60, 0))
        self.doubleSpinBox_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_2.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout_2.addWidget(self.doubleSpinBox_2, 0, 1, 1, 1)

        self.label_18 = QLabel(self.relParWgt)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 0, 2, 1, 1)


        self.verticalLayout_22.addWidget(self.relParWgt)

        self.relResLbl = QLabel(self.relWgt)
        self.relResLbl.setObjectName(u"relResLbl")
        self.relResLbl.setFont(font3)
        self.relResLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.relResLbl)

        self.relResWgt = QWidget(self.relWgt)
        self.relResWgt.setObjectName(u"relResWgt")
        self.relResWgt.setStyleSheet(u"*{}\n"
"\n"
"QDoubleSpinBox{\n"
"	border: solid;\n"
"	border-width: 0.5px;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")
        self.gridLayout_3 = QGridLayout(self.relResWgt)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setContentsMargins(5, 0, 5, 0)
        self.doubleSpinBox_3 = QDoubleSpinBox(self.relResWgt)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setMinimumSize(QSize(60, 0))
        self.doubleSpinBox_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_3.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout_3.addWidget(self.doubleSpinBox_3, 0, 1, 1, 1)

        self.label_20 = QLabel(self.relResWgt)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_3.addWidget(self.label_20, 0, 2, 1, 1)

        self.label_19 = QLabel(self.relResWgt)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 0, 0, 1, 1)


        self.verticalLayout_22.addWidget(self.relResWgt)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_22.addItem(self.verticalSpacer_4)


        self.verticalLayout_13.addWidget(self.relWgt)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_5)

        self.parPlsWgt = QWidget(self.page_4)
        self.parPlsWgt.setObjectName(u"parPlsWgt")
        self.horizontalLayout_14 = QHBoxLayout(self.parPlsWgt)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, -1, 0, -1)
        self.pushButton = QPushButton(self.parPlsWgt)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(60, 20))

        self.horizontalLayout_14.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(1, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.parPlsWgt)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(60, 20))

        self.horizontalLayout_14.addWidget(self.pushButton_2)


        self.verticalLayout_13.addWidget(self.parPlsWgt)

        self.rightMenuPages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_14 = QVBoxLayout(self.page_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.page_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)

        self.rightMenuPages.addWidget(self.page_5)

        self.verticalLayout_12.addWidget(self.rightMenuPages)


        self.verticalLayout_11.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_8.addWidget(self.rightMenuContainer, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.mainBodyContent)

        self.popupNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
        self.verticalLayout_19 = QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
        self.verticalLayout_20 = QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_14 = QLabel(self.popupNotificationSubContainer)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)

        self.verticalLayout_20.addWidget(self.label_14)

        self.frame_9 = QFrame(self.popupNotificationSubContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setPointSize(10)
        self.label_13.setFont(font4)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_13)

        self.closeNotificationBtn = QPushButton(self.frame_9)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        self.closeNotificationBtn.setIcon(icon16)
        self.closeNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.closeNotificationBtn)


        self.verticalLayout_20.addWidget(self.frame_9)


        self.verticalLayout_19.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_10.addWidget(self.popupNotificationContainer)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.horizontalLayout_11 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 5, 0)
        self.frame_10 = QFrame(self.footerContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_12.addWidget(self.label_15)


        self.horizontalLayout_11.addWidget(self.frame_10)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(15, 15))
        self.sizeGrip.setMaximumSize(QSize(15, 15))
        self.sizeGrip.setStyleSheet(u"")
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.sizeGrip)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(0, 0, 15, 15))
        self.label_16.setPixmap(QPixmap(u":/icons/icons/resize.png"))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.sizeGrip)


        self.verticalLayout_10.addWidget(self.footerContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.frame_2.setToolTip(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.dataBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Grid details", None))
#endif // QT_CONFIG(tooltip)
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u"Grid Details", None))
#if QT_CONFIG(tooltip)
        self.reportBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Report", None))
#endif // QT_CONFIG(tooltip)
        self.reportBtn.setText(QCoreApplication.translate("MainWindow", u"Report", None))
#if QT_CONFIG(tooltip)
        self.loadProfilesBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Load Profiles", None))
#endif // QT_CONFIG(tooltip)
        self.loadProfilesBtn.setText(QCoreApplication.translate("MainWindow", u"Load Profiles", None))
#if QT_CONFIG(tooltip)
        self.restartBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.restartBtn.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
#if QT_CONFIG(tooltip)
        self.loadflow_Btn.setToolTip(QCoreApplication.translate("MainWindow", u"LoadFlow", None))
#endif // QT_CONFIG(tooltip)
        self.loadflow_Btn.setText(QCoreApplication.translate("MainWindow", u"LoadFlow", None))
#if QT_CONFIG(tooltip)
        self.anom_Btn.setToolTip(QCoreApplication.translate("MainWindow", u"Anomalies Generation", None))
#endif // QT_CONFIG(tooltip)
        self.anom_Btn.setText(QCoreApplication.translate("MainWindow", u"Anomalies Gen.", None))
#if QT_CONFIG(tooltip)
        self.opf_Btn.setToolTip(QCoreApplication.translate("MainWindow", u"Optimal Power Flow", None))
#endif // QT_CONFIG(tooltip)
        self.opf_Btn.setText(QCoreApplication.translate("MainWindow", u"OPF", None))
#if QT_CONFIG(tooltip)
        self.reliabilithy_Btn.setToolTip(QCoreApplication.translate("MainWindow", u"Reliability", None))
#endif // QT_CONFIG(tooltip)
        self.reliabilithy_Btn.setText(QCoreApplication.translate("MainWindow", u"Reliability", None))
#if QT_CONFIG(tooltip)
        self.reliabilithy_Btn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Adequacy", None))
#endif // QT_CONFIG(tooltip)
        self.reliabilithy_Btn_2.setText(QCoreApplication.translate("MainWindow", u"Adequacy", None))
#if QT_CONFIG(tooltip)
        self.gidman_Btn.setToolTip(QCoreApplication.translate("MainWindow", u"Grid Management", None))
#endif // QT_CONFIG(tooltip)
        self.gidman_Btn.setText(QCoreApplication.translate("MainWindow", u"Grid Management", None))
#if QT_CONFIG(tooltip)
        self.onr_Btn.setToolTip(QCoreApplication.translate("MainWindow", u"Optimal Network Reconfiguration", None))
#endif // QT_CONFIG(tooltip)
        self.onr_Btn.setText(QCoreApplication.translate("MainWindow", u"ONR", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Information", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ARS tool", None))
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.moreMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.moreMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.profileMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.profileMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.rightMenu_LBL.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
#if QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setText("")
        self.lfWgtPls.setText(QCoreApplication.translate("MainWindow", u"LoadFlow", None))
        self.lfParLbl.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"param", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"unit", None))
        self.lfResLbl.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"unit", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"param", None))
        self.relWgtPls.setText(QCoreApplication.translate("MainWindow", u"Reliability", None))
        self.relParLbl.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"param", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"unit", None))
        self.relResLbl.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"unit", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"param", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Salva", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Annulla", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"More...", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Notification Message", None))
#if QT_CONFIG(tooltip)
        self.closeNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotificationBtn.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Copyright ENEA", None))
        self.label_16.setText("")
    # retranslateUi

