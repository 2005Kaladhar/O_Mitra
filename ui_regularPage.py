# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'regularPagedRdpXH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(798, 547)
        MainWindow.setMinimumSize(QSize(200, 0))
        icon = QIcon()
        icon.addFile(u"../O-Mitra Original Working With Background IMages/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"border-image: url(:/newPrefix/5c1d033b0b95a-wallpaper-preview.jpg);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-image:None;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.TitleBar_2 = QFrame(self.centralwidget)
        self.TitleBar_2.setObjectName(u"TitleBar_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleBar_2.sizePolicy().hasHeightForWidth())
        self.TitleBar_2.setSizePolicy(sizePolicy)
        self.TitleBar_2.setMinimumSize(QSize(0, 0))
        self.TitleBar_2.setMaximumSize(QSize(16777215, 30))
        self.TitleBar_2.setStyleSheet(u"QFrame{\n"
"\n"
"	\n"
"\n"
"	background-color: rgb(42, 8, 70);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.38, x2:1, y2:0.670636, stop:0 rgba(0, 0, 0, 59), stop:1 rgba(13, 13, 13, 11));\n"
"\n"
"\n"
"}")
        self.TitleBar_2.setFrameShape(QFrame.StyledPanel)
        self.TitleBar_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.TitleBar_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.TitleBar_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.TitleBar = QLabel(self.frame_2)
        self.TitleBar.setObjectName(u"TitleBar")
        self.TitleBar.setMinimumSize(QSize(60, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.TitleBar.setFont(font)
        self.TitleBar.setCursor(QCursor(Qt.SizeAllCursor))
        self.TitleBar.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 0, 255);\n"
"border-radius:3px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.38, x2:1, y2:0.670636, stop:0 rgba(0, 0, 0, 59), stop:1 rgba(13, 13, 13, 11));\n"
"}")
        self.TitleBar.setTextFormat(Qt.RichText)
        self.TitleBar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.TitleBar)


        self.horizontalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.TitleBar_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(0, 25))
        self.frame_3.setMaximumSize(QSize(100, 16777215))
        self.frame_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 0, 0, 0)
        self.Minimizebtn = QPushButton(self.frame_3)
        self.Minimizebtn.setObjectName(u"Minimizebtn")
        sizePolicy1.setHeightForWidth(self.Minimizebtn.sizePolicy().hasHeightForWidth())
        self.Minimizebtn.setSizePolicy(sizePolicy1)
        self.Minimizebtn.setMaximumSize(QSize(15, 15))
        self.Minimizebtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 0);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.Minimizebtn)

        self.Maximizebtn = QPushButton(self.frame_3)
        self.Maximizebtn.setObjectName(u"Maximizebtn")
        sizePolicy1.setHeightForWidth(self.Maximizebtn.sizePolicy().hasHeightForWidth())
        self.Maximizebtn.setSizePolicy(sizePolicy1)
        self.Maximizebtn.setMaximumSize(QSize(15, 15))
        self.Maximizebtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 0);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(85, 170, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.Maximizebtn)

        self.CloseButton = QPushButton(self.frame_3)
        self.CloseButton.setObjectName(u"CloseButton")
        sizePolicy1.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy1)
        self.CloseButton.setMaximumSize(QSize(15, 15))
        self.CloseButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(235, 0, 16);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.CloseButton)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.TitleBar_2)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.MainContent1Stacked = QWidget()
        self.MainContent1Stacked.setObjectName(u"MainContent1Stacked")
        self.horizontalLayout_10 = QHBoxLayout(self.MainContent1Stacked)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.MainContent1Stacked)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QSize(0, 20))
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(47, 0, 70,100);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"	color: rgba(255, 255, 0, 190);\n"
"\n"
"\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.gridLayout_4.addWidget(self.frame_5, 2, 0, 1, 1)

        self.contentPage = QFrame(self.frame)
        self.contentPage.setObjectName(u"contentPage")
        self.contentPage.setStyleSheet(u"QFrame{\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0 rgba(0, 0, 51, 255), stop:1 rgba(0, 0, 127, 255));\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}")
        self.contentPage.setFrameShape(QFrame.StyledPanel)
        self.contentPage.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.contentPage)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.contentPage)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy2)
        self.frame_11.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.StartButtonMain = QPushButton(self.frame_11)
        self.StartButtonMain.setObjectName(u"StartButtonMain")
        self.StartButtonMain.setMaximumSize(QSize(287, 200))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(26)
        font1.setBold(False)
        font1.setWeight(50)
        self.StartButtonMain.setFont(font1)
        self.StartButtonMain.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.494591, y1:0.972, x2:0.487955, y2:0.267, stop:0 rgba(74, 156, 198, 224), stop:1 rgba(239, 239, 37, 255));\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494591, y1:0.972, x2:0.487955, y2:0.267, stop:0 rgba(74, 156, 198, 224), stop:1 rgba(37, 239, 68, 255));\n"
"\n"
"}")

        self.horizontalLayout_8.addWidget(self.StartButtonMain)


        self.gridLayout_3.addWidget(self.frame_11, 2, 1, 3, 1)

        self.frame_10 = QFrame(self.contentPage)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setMinimumSize(QSize(7, 119))
        self.frame_10.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_10)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.AddUrgentMeeting = QPushButton(self.frame_10)
        self.AddUrgentMeeting.setObjectName(u"AddUrgentMeeting")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.AddUrgentMeeting.sizePolicy().hasHeightForWidth())
        self.AddUrgentMeeting.setSizePolicy(sizePolicy3)
        self.AddUrgentMeeting.setMinimumSize(QSize(131, 30))
        self.AddUrgentMeeting.setMaximumSize(QSize(200, 20))
        font2 = QFont()
        font2.setPointSize(11)
        self.AddUrgentMeeting.setFont(font2)
        self.AddUrgentMeeting.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(255, 255, 0);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.AddUrgentMeeting, 0, 0, 1, 1)

        self.UrgentMeeting = QLineEdit(self.frame_10)
        self.UrgentMeeting.setObjectName(u"UrgentMeeting")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(21)
        sizePolicy4.setHeightForWidth(self.UrgentMeeting.sizePolicy().hasHeightForWidth())
        self.UrgentMeeting.setSizePolicy(sizePolicy4)
        self.UrgentMeeting.setMinimumSize(QSize(191, 27))
        self.UrgentMeeting.setMaximumSize(QSize(16777215, 20))
        font3 = QFont()
        font3.setPointSize(9)
        self.UrgentMeeting.setFont(font3)
        self.UrgentMeeting.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"text-align:centre;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.UrgentMeeting.setEchoMode(QLineEdit.Normal)
        self.UrgentMeeting.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.UrgentMeeting, 1, 0, 1, 1)

        self.UrgentMeetingStartBtn = QPushButton(self.frame_10)
        self.UrgentMeetingStartBtn.setObjectName(u"UrgentMeetingStartBtn")
        sizePolicy3.setHeightForWidth(self.UrgentMeetingStartBtn.sizePolicy().hasHeightForWidth())
        self.UrgentMeetingStartBtn.setSizePolicy(sizePolicy3)
        self.UrgentMeetingStartBtn.setMinimumSize(QSize(0, 29))
        self.UrgentMeetingStartBtn.setMaximumSize(QSize(16777215, 20))
        font4 = QFont()
        font4.setPointSize(10)
        self.UrgentMeetingStartBtn.setFont(font4)
        self.UrgentMeetingStartBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 141, 26);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	\n"
"	background-color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 151, 46);\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.UrgentMeetingStartBtn, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_10, 2, 2, 1, 1)

        self.frame_6 = QFrame(self.contentPage)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 0, -1, 0)
        self.Heading = QLabel(self.frame_6)
        self.Heading.setObjectName(u"Heading")
        self.Heading.setMinimumSize(QSize(50, 0))
        font5 = QFont()
        font5.setPointSize(24)
        self.Heading.setFont(font5)
        self.Heading.setStyleSheet(u"QLabel{\n"
"\n"
"border-radius:30px;\n"
"	\n"
"	color: rgba(170, 255, 127, 230);\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(180, 0, 164, 255), stop:1 rgba(241, 71, 93, 250));\n"
"\n"
"\n"
"}")
        self.Heading.setMidLineWidth(4)
        self.Heading.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.Heading)


        self.gridLayout_3.addWidget(self.frame_6, 0, 0, 1, 3)

        self.frame_13 = QFrame(self.contentPage)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy5)
        self.frame_13.setMinimumSize(QSize(194, 0))
        self.frame_13.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(70, 0, 11, 0)
        self.StartButtonsecond = QPushButton(self.frame_13)
        self.StartButtonsecond.setObjectName(u"StartButtonsecond")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.StartButtonsecond.sizePolicy().hasHeightForWidth())
        self.StartButtonsecond.setSizePolicy(sizePolicy6)
        self.StartButtonsecond.setMinimumSize(QSize(0, 15))
        self.StartButtonsecond.setMaximumSize(QSize(16777215, 42))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setWeight(50)
        self.StartButtonsecond.setFont(font6)
        self.StartButtonsecond.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.653, x2:1, y2:0.631, stop:0 rgba(255, 0, 255, 255), stop:1 rgba(166, 43, 200, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(75, 200, 100);\n"
"\n"
"}")

        self.horizontalLayout_9.addWidget(self.StartButtonsecond)


        self.gridLayout_3.addWidget(self.frame_13, 4, 2, 1, 1)

        self.frame_12 = QFrame(self.contentPage)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(225, 0))
        self.frame_12.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.UseDefaultBrowser = QRadioButton(self.frame_12)
        self.UseDefaultBrowser.setObjectName(u"UseDefaultBrowser")
        sizePolicy1.setHeightForWidth(self.UseDefaultBrowser.sizePolicy().hasHeightForWidth())
        self.UseDefaultBrowser.setSizePolicy(sizePolicy1)
        self.UseDefaultBrowser.setMinimumSize(QSize(147, 29))
        self.UseDefaultBrowser.setStyleSheet(u"QRadioButton{\n"
"border-radius:5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(232, 154, 0, 255), stop:1 rgba(255, 102, 25, 255));\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QRadioButton::hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(212, 70, 0, 255), stop:1 rgba(255, 255, 0, 255));\n"
"\n"
"	background-color: rgba(242, 132, 11, 200);\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/Browsers_009.png", QSize(), QIcon.Normal, QIcon.Off)
        self.UseDefaultBrowser.setIcon(icon1)

        self.horizontalLayout_16.addWidget(self.UseDefaultBrowser)


        self.gridLayout_3.addWidget(self.frame_12, 3, 2, 1, 1)

        self.frame_8 = QFrame(self.contentPage)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_8)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 1, 0, 0)
        self.TimerStackedView = QStackedWidget(self.frame_8)
        self.TimerStackedView.setObjectName(u"TimerStackedView")
        sizePolicy.setHeightForWidth(self.TimerStackedView.sizePolicy().hasHeightForWidth())
        self.TimerStackedView.setSizePolicy(sizePolicy)
        self.O_MitraTitle = QWidget()
        self.O_MitraTitle.setObjectName(u"O_MitraTitle")
        self.horizontalLayout_19 = QHBoxLayout(self.O_MitraTitle)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_7 = QFrame(self.O_MitraTitle)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 52))
        self.frame_7.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.frame_7)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 0))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(20)
        font7.setBold(False)
        font7.setWeight(50)
        self.title.setFont(font7)
        self.title.setLayoutDirection(Qt.LeftToRight)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet(u"QLabel{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgba(255, 255, 127,255);\n"
"border-radius:10px;\n"
"\n"
"}")
        self.title.setTextFormat(Qt.RichText)
        self.title.setScaledContents(False)
        self.title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.title)


        self.horizontalLayout_19.addWidget(self.frame_7)

        self.TimerStackedView.addWidget(self.O_MitraTitle)
        self.TimerPage = QWidget()
        self.TimerPage.setObjectName(u"TimerPage")
        self.horizontalLayout_20 = QHBoxLayout(self.TimerPage)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.TimerPage)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(243, 0, 187, 0)
        self.TimerText = QPushButton(self.frame_4)
        self.TimerText.setObjectName(u"TimerText")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.TimerText.sizePolicy().hasHeightForWidth())
        self.TimerText.setSizePolicy(sizePolicy7)
        self.TimerText.setMinimumSize(QSize(236, 30))
        self.TimerText.setMaximumSize(QSize(200, 20))
        self.TimerText.setFont(font2)
        self.TimerText.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(255, 255, 0);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"\n"
"}")

        self.horizontalLayout_21.addWidget(self.TimerText)

        self.TimerClose = QPushButton(self.frame_4)
        self.TimerClose.setObjectName(u"TimerClose")
        sizePolicy1.setHeightForWidth(self.TimerClose.sizePolicy().hasHeightForWidth())
        self.TimerClose.setSizePolicy(sizePolicy1)
        self.TimerClose.setMaximumSize(QSize(23, 23))
        self.TimerClose.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(235, 0, 16);\n"
"border-radius:11px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.horizontalLayout_21.addWidget(self.TimerClose)


        self.horizontalLayout_20.addWidget(self.frame_4)

        self.TimerStackedView.addWidget(self.TimerPage)

        self.verticalLayout.addWidget(self.TimerStackedView)

        self.Description_2 = QLabel(self.frame_8)
        self.Description_2.setObjectName(u"Description_2")
        self.Description_2.setMinimumSize(QSize(0, 34))
        font8 = QFont()
        font8.setFamily(u"Segoe UI Semibold")
        font8.setPointSize(14)
        font8.setBold(True)
        font8.setWeight(75)
        self.Description_2.setFont(font8)
        self.Description_2.setLayoutDirection(Qt.LeftToRight)
        self.Description_2.setAutoFillBackground(False)
        self.Description_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"\n"
"border-radius:15px;\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(180, 0, 164, 197), stop:1 rgba(241, 71, 93, 195));\n"
"\n"
"color: rgba(227, 227, 227, 255);")
        self.Description_2.setTextFormat(Qt.RichText)
        self.Description_2.setScaledContents(False)
        self.Description_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Description_2)

        self.stackedWidget_2 = QStackedWidget(self.frame_8)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy)
        self.stackedWidget_2.setMinimumSize(QSize(0, 44))
        self.stackedWidget_2.setStyleSheet(u"background-color: rgb(56, 56, 56);")
        self.NormalMsg = QWidget()
        self.NormalMsg.setObjectName(u"NormalMsg")
        self.horizontalLayout = QHBoxLayout(self.NormalMsg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Description = QLabel(self.NormalMsg)
        self.Description.setObjectName(u"Description")
        self.Description.setMinimumSize(QSize(0, 0))
        font9 = QFont()
        font9.setFamily(u"Segoe UI Semibold")
        font9.setPointSize(16)
        font9.setBold(True)
        font9.setWeight(75)
        self.Description.setFont(font9)
        self.Description.setLayoutDirection(Qt.LeftToRight)
        self.Description.setAutoFillBackground(False)
        self.Description.setStyleSheet(u"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00568182 rgba(116, 255, 54, 180), stop:1 rgba(255, 170, 0, 150));")
        self.Description.setTextFormat(Qt.RichText)
        self.Description.setScaledContents(False)
        self.Description.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Description)

        self.stackedWidget_2.addWidget(self.NormalMsg)
        self.InvalidPageLink = QWidget()
        self.InvalidPageLink.setObjectName(u"InvalidPageLink")
        self.horizontalLayout_4 = QHBoxLayout(self.InvalidPageLink)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(62, 0, 46, 0)
        self.Description_3 = QLabel(self.InvalidPageLink)
        self.Description_3.setObjectName(u"Description_3")
        self.Description_3.setMinimumSize(QSize(0, 0))
        self.Description_3.setFont(font9)
        self.Description_3.setLayoutDirection(Qt.LeftToRight)
        self.Description_3.setAutoFillBackground(False)
        self.Description_3.setStyleSheet(u"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00568182 rgba(116, 255, 54, 180), stop:1 rgba(255, 170, 0, 150));\n"
"background-color: rgb(56, 56, 56);\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.Description_3.setTextFormat(Qt.RichText)
        self.Description_3.setScaledContents(False)
        self.Description_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.Description_3)

        self.urgentLinkClose = QPushButton(self.InvalidPageLink)
        self.urgentLinkClose.setObjectName(u"urgentLinkClose")
        sizePolicy1.setHeightForWidth(self.urgentLinkClose.sizePolicy().hasHeightForWidth())
        self.urgentLinkClose.setSizePolicy(sizePolicy1)
        self.urgentLinkClose.setMinimumSize(QSize(34, 34))
        self.urgentLinkClose.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"\n"
"	\n"
"	border-image: url(:/newPrefix/closebutton.png);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	border-image: url(:/newPrefix/closebutton2.png);\n"
"	\n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.urgentLinkClose)

        self.stackedWidget_2.addWidget(self.InvalidPageLink)

        self.verticalLayout.addWidget(self.stackedWidget_2)


        self.gridLayout_3.addWidget(self.frame_8, 1, 0, 1, 3)

        self.frame_9 = QFrame(self.contentPage)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy2.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy2)
        self.frame_9.setMinimumSize(QSize(233, 0))
        self.frame_9.setMaximumSize(QSize(198, 16777215))
        self.frame_9.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_9)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ChangeEmailPass = QPushButton(self.frame_9)
        self.ChangeEmailPass.setObjectName(u"ChangeEmailPass")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.ChangeEmailPass.sizePolicy().hasHeightForWidth())
        self.ChangeEmailPass.setSizePolicy(sizePolicy8)
        self.ChangeEmailPass.setMinimumSize(QSize(200, 50))
        self.ChangeEmailPass.setMaximumSize(QSize(500, 16777215))
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(10)
        font10.setBold(False)
        font10.setWeight(50)
        self.ChangeEmailPass.setFont(font10)
        self.ChangeEmailPass.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.653, x2:1, y2:0.631, stop:0 rgba(255, 0, 255, 255), stop:1 rgba(166, 43, 200, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(75, 200, 100);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.ChangeEmailPass, 0, 0, 1, 1)

        self.ClearSavedData = QPushButton(self.frame_9)
        self.ClearSavedData.setObjectName(u"ClearSavedData")
        self.ClearSavedData.setMinimumSize(QSize(0, 50))
        self.ClearSavedData.setFont(font10)
        self.ClearSavedData.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.653, x2:1, y2:0.631, stop:0 rgba(255, 0, 255, 255), stop:1 rgba(166, 43, 200, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(75, 200, 100);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.ClearSavedData, 1, 0, 1, 1)

        self.ContactDeveloper = QPushButton(self.frame_9)
        self.ContactDeveloper.setObjectName(u"ContactDeveloper")
        self.ContactDeveloper.setMinimumSize(QSize(0, 50))
        self.ContactDeveloper.setFont(font10)
        self.ContactDeveloper.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.653, x2:1, y2:0.631, stop:0 rgba(255, 0, 255, 255), stop:1 rgba(166, 43, 200, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(75, 200, 100);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.ContactDeveloper, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_9, 2, 0, 3, 1)


        self.gridLayout_4.addWidget(self.contentPage, 1, 0, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame)

        self.stackedWidget.addWidget(self.MainContent1Stacked)
        self.DeleteMessagePage = QWidget()
        self.DeleteMessagePage.setObjectName(u"DeleteMessagePage")
        self.horizontalLayout_11 = QHBoxLayout(self.DeleteMessagePage)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.DeleteMessagePage)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(7)
        self.gridLayout_5.setVerticalSpacing(23)
        self.gridLayout_5.setContentsMargins(10, -1, 10, -1)
        self.NoDelete = QPushButton(self.frame_14)
        self.NoDelete.setObjectName(u"NoDelete")
        self.NoDelete.setMinimumSize(QSize(0, 90))
        self.NoDelete.setFont(font2)
        self.NoDelete.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 141, 26);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"		background-color: rgb(255, 151, 46);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"background-color: rgb(31, 236, 35);\n"
"\n"
"}")

        self.gridLayout_5.addWidget(self.NoDelete, 1, 1, 1, 1)

        self.YesDelete = QPushButton(self.frame_14)
        self.YesDelete.setObjectName(u"YesDelete")
        self.YesDelete.setMinimumSize(QSize(0, 90))
        self.YesDelete.setFont(font2)
        self.YesDelete.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 141, 26);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"		background-color: rgb(255, 151, 46);\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"background-color: rgb(31, 236, 35);\n"
"\n"
"}")

        self.gridLayout_5.addWidget(self.YesDelete, 1, 0, 1, 1)

        self.DeleteMessage = QLabel(self.frame_14)
        self.DeleteMessage.setObjectName(u"DeleteMessage")
        font11 = QFont()
        font11.setPointSize(12)
        self.DeleteMessage.setFont(font11)
        self.DeleteMessage.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.71, x2:1, y2:0.670636, stop:0 rgba(0, 0, 0, 190), stop:1 rgba(13, 13, 13, 187));\n"
"\n"
"}")
        self.DeleteMessage.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.DeleteMessage, 0, 0, 1, 2)


        self.horizontalLayout_12.addLayout(self.gridLayout_5)


        self.horizontalLayout_11.addWidget(self.frame_14)

        self.stackedWidget.addWidget(self.DeleteMessagePage)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_14 = QHBoxLayout(self.page)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.UrgentLinkAlert = QFrame(self.page)
        self.UrgentLinkAlert.setObjectName(u"UrgentLinkAlert")
        self.UrgentLinkAlert.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 215), stop:1 rgba(11, 15, 50, 194));")
        self.UrgentLinkAlert.setFrameShape(QFrame.StyledPanel)
        self.UrgentLinkAlert.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.UrgentLinkAlert)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 2, -1, -1)
        self.label_2 = QLabel(self.UrgentLinkAlert)
        self.label_2.setObjectName(u"label_2")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy9)
        self.label_2.setMinimumSize(QSize(5, 0))
        self.label_2.setFont(font11)
        self.label_2.setStyleSheet(u"QLabel{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 1)

        self.frame_15 = QFrame(self.UrgentLinkAlert)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(180, 0))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.UrgentLinkClose = QPushButton(self.frame_15)
        self.UrgentLinkClose.setObjectName(u"UrgentLinkClose")
        sizePolicy.setHeightForWidth(self.UrgentLinkClose.sizePolicy().hasHeightForWidth())
        self.UrgentLinkClose.setSizePolicy(sizePolicy)
        self.UrgentLinkClose.setMinimumSize(QSize(14, 50))
        font12 = QFont()
        font12.setBold(True)
        font12.setWeight(75)
        self.UrgentLinkClose.setFont(font12)
        self.UrgentLinkClose.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-radius:5px;\n"
"	color: rgb(121, 121, 121);\n"
"	background-color: rgb(43, 43, 43);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"		background-color: rgb(81, 81, 81);\n"
"	color: rgb(240, 240, 240);\n"
"\n"
"}")

        self.horizontalLayout_15.addWidget(self.UrgentLinkClose)


        self.gridLayout_6.addWidget(self.frame_15, 0, 1, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_6)


        self.horizontalLayout_14.addWidget(self.UrgentLinkAlert)

        self.stackedWidget.addWidget(self.page)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.AddUrgentMeeting, self.UrgentMeeting)
        QWidget.setTabOrder(self.UrgentMeeting, self.UrgentMeetingStartBtn)
        QWidget.setTabOrder(self.UrgentMeetingStartBtn, self.ChangeEmailPass)
        QWidget.setTabOrder(self.ChangeEmailPass, self.ClearSavedData)
        QWidget.setTabOrder(self.ClearSavedData, self.ContactDeveloper)
        QWidget.setTabOrder(self.ContactDeveloper, self.StartButtonMain)
        QWidget.setTabOrder(self.StartButtonMain, self.StartButtonsecond)
        QWidget.setTabOrder(self.StartButtonsecond, self.YesDelete)
        QWidget.setTabOrder(self.YesDelete, self.NoDelete)
        QWidget.setTabOrder(self.NoDelete, self.UrgentLinkClose)
        QWidget.setTabOrder(self.UrgentLinkClose, self.Minimizebtn)
        QWidget.setTabOrder(self.Minimizebtn, self.Maximizebtn)
        QWidget.setTabOrder(self.Maximizebtn, self.CloseButton)
        QWidget.setTabOrder(self.CloseButton, self.Minimizebtn)
        QWidget.setTabOrder(self.Minimizebtn, self.Maximizebtn)
        QWidget.setTabOrder(self.Maximizebtn, self.CloseButton)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.TimerStackedView.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.TitleBar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt; font-weight:400;\">O-Mitra</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.Minimizebtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Minimize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Minimizebtn.setText("")
#if QT_CONFIG(tooltip)
        self.Maximizebtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Maximize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Maximizebtn.setText("")
#if QT_CONFIG(tooltip)
        self.CloseButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Close</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.CloseButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Created : Kaladhar Gopal", None))
        self.StartButtonMain.setText(QCoreApplication.translate("MainWindow", u"Start", None))
#if QT_CONFIG(shortcut)
        self.StartButtonMain.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.AddUrgentMeeting.setText(QCoreApplication.translate("MainWindow", u"Urgent Meeting", None))
#if QT_CONFIG(tooltip)
        self.UrgentMeeting.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter the meeting link which is not in your schedule, link should be of GoogleMeet.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.UrgentMeeting.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Add a Meeting Link", None))
        self.UrgentMeetingStartBtn.setText(QCoreApplication.translate("MainWindow", u"Start Urgent Meeting", None))
        self.Heading.setText(QCoreApplication.translate("MainWindow", u"Ready For Your Service...", None))
        self.StartButtonsecond.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.UseDefaultBrowser.setText(QCoreApplication.translate("MainWindow", u"Use Default WebBrowser  ", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"O-Mitra", None))
        self.TimerText.setText(QCoreApplication.translate("MainWindow", u"Urgent Meeting", None))
#if QT_CONFIG(tooltip)
        self.TimerClose.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Close</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.TimerClose.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.Description_2.setText(QCoreApplication.translate("MainWindow", u"Online Meetings Manager In Tiny Robust Application", None))
        self.Description.setText(QCoreApplication.translate("MainWindow", u"You can Trust me, I'm here to Manage all your Meetings.", None))
        self.Description_3.setText(QCoreApplication.translate("MainWindow", u"Please Provide A Valid Meeting Link", None))
        self.urgentLinkClose.setText("")
        self.ChangeEmailPass.setText(QCoreApplication.translate("MainWindow", u"Change Email and Password", None))
#if QT_CONFIG(shortcut)
        self.ChangeEmailPass.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.ClearSavedData.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">.</span>It will clear all the save data like Email, Password, Name, Meeting details etc.</p><p><span style=\" font-weight:600;\">.</span>It neither harm your computer nor the app, just restart the app and it will ask you for the details again. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ClearSavedData.setText(QCoreApplication.translate("MainWindow", u"Clear Saved Data", None))
#if QT_CONFIG(shortcut)
        self.ClearSavedData.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.ContactDeveloper.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>You will be redirected to developer's website.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ContactDeveloper.setText(QCoreApplication.translate("MainWindow", u"Contact Developer", None))
#if QT_CONFIG(shortcut)
        self.ContactDeveloper.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.NoDelete.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.YesDelete.setText(QCoreApplication.translate("MainWindow", u"Yes ", None))
        self.DeleteMessage.setText(QCoreApplication.translate("MainWindow", u"Do You Really Want to Delete All Your Saved Data ? ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Please Provide A Valid Link For THe Meeting...", None))
        self.UrgentLinkClose.setText(QCoreApplication.translate("MainWindow", u"Okay", None))
    # retranslateUi

