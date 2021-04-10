# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginFormAziDpr.ui'
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
        MainWindow.resize(700, 441)
        icon = QIcon()
        icon.addFile(u"../../.designer/O-Mitra Original Working With Background IMages/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"border-image: url(:/newPrefix/73c08740bcfe5c7b6db3659f4f67874b.png);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setStyleSheet(u"\n"
"border-image:None;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 88), stop:1 rgba(0, 0, 0, 90));")
        self.Content.setFrameShape(QFrame.StyledPanel)
        self.Content.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.Content)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.Content)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_4, 4, 2, 1, 2)

        self.frame_5 = QFrame(self.Content)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(108, 0))
        self.frame_5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.NextButton = QPushButton(self.frame_5)
        self.NextButton.setObjectName(u"NextButton")
        self.NextButton.setMinimumSize(QSize(0, 39))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.NextButton.setFont(font)
        self.NextButton.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.653, x2:1, y2:0.631, stop:0 rgba(255, 0, 255, 255), stop:1 rgba(166, 43, 200, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(75, 200, 100);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.NextButton)


        self.gridLayout_4.addWidget(self.frame_5, 5, 3, 1, 1)

        self.frame_9 = QFrame(self.Content)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_9, 5, 2, 1, 1)

        self.frame_3 = QFrame(self.Content)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(130, 0))
        self.frame_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.MaleRadioBtn = QRadioButton(self.frame_3)
        self.MaleRadioBtn.setObjectName(u"MaleRadioBtn")
        self.MaleRadioBtn.setMinimumSize(QSize(116, 28))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setWeight(50)
        self.MaleRadioBtn.setFont(font1)
        self.MaleRadioBtn.setLayoutDirection(Qt.LeftToRight)
        self.MaleRadioBtn.setAutoFillBackground(False)
        self.MaleRadioBtn.setStyleSheet(u"QRadioButton{\n"
"border-radius:10px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.568, x2:1, y2:0.517, stop:0 rgba(0, 115, 255, 255), stop:1 rgba(219, 179, 234, 255));\n"
"\n"
"}\n"
"\n"
"QRadioButton::hover{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.568, x2:1, y2:0.517, stop:0 rgba(0, 115, 255, 150), stop:1 rgba(219, 179, 234, 200));\n"
"\n"
"}")
        self.MaleRadioBtn.setCheckable(True)
        self.MaleRadioBtn.setChecked(False)

        self.gridLayout_3.addWidget(self.MaleRadioBtn, 0, 0, 1, 1)

        self.FemaleRadioBtn = QRadioButton(self.frame_3)
        self.FemaleRadioBtn.setObjectName(u"FemaleRadioBtn")
        self.FemaleRadioBtn.setMinimumSize(QSize(116, 28))
        self.FemaleRadioBtn.setFont(font1)
        self.FemaleRadioBtn.setStyleSheet(u"QRadioButton{\n"
"border-radius:10px;\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.568, x2:1, y2:0.517, stop:0 rgba(255, 0, 237, 255), stop:1 rgba(219, 179, 234, 255));\n"
"}\n"
"\n"
"QRadioButton::hover{\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.568, x2:1, y2:0.517, stop:0 rgba(255, 0, 237, 150), stop:1 rgba(219, 179, 234, 200));\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.FemaleRadioBtn, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_3, 3, 2, 1, 2)

        self.label_2 = QLabel(self.Content)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 54))
        font2 = QFont()
        font2.setPointSize(24)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgba(255, 0, 255,240);\n"
"border-radius:20px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(120, 0, 86, 255), stop:1 rgba(241, 0, 31, 255));\n"
"\n"
"}")
        self.label_2.setMidLineWidth(4)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_2, 1, 1, 1, 1)

        self.frame = QFrame(self.Content)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(166, 0))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(34)
        self.gridLayout.setContentsMargins(-1, 54, -1, 54)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_3.setFont(font3)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"QLabel{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"border-radius:15px;\n"
"\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 129, 23, 255), stop:1 rgba(239, 239, 37, 255));\n"
"\n"
"}")
        self.label_3.setTextFormat(Qt.RichText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.Description_5 = QLabel(self.frame)
        self.Description_5.setObjectName(u"Description_5")
        sizePolicy2.setHeightForWidth(self.Description_5.sizePolicy().hasHeightForWidth())
        self.Description_5.setSizePolicy(sizePolicy2)
        self.Description_5.setFont(font3)
        self.Description_5.setLayoutDirection(Qt.LeftToRight)
        self.Description_5.setAutoFillBackground(False)
        self.Description_5.setStyleSheet(u"QLabel{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"border-radius:15px;\n"
"\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 129, 23, 255), stop:1 rgba(239, 239, 37, 255));\n"
"\n"
"}")
        self.Description_5.setTextFormat(Qt.RichText)
        self.Description_5.setScaledContents(False)
        self.Description_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Description_5, 1, 0, 1, 1)

        self.Description_4 = QLabel(self.frame)
        self.Description_4.setObjectName(u"Description_4")
        sizePolicy2.setHeightForWidth(self.Description_4.sizePolicy().hasHeightForWidth())
        self.Description_4.setSizePolicy(sizePolicy2)
        self.Description_4.setFont(font3)
        self.Description_4.setLayoutDirection(Qt.LeftToRight)
        self.Description_4.setAutoFillBackground(False)
        self.Description_4.setStyleSheet(u"QLabel{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"border-radius:15px;\n"
"\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 129, 23, 255), stop:1 rgba(239, 239, 37, 255));\n"
"\n"
"}")
        self.Description_4.setTextFormat(Qt.RichText)
        self.Description_4.setScaledContents(False)
        self.Description_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Description_4, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame, 3, 0, 3, 1)

        self.frame_2 = QFrame(self.Content)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(301, 0))
        self.frame_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(29)
        self.gridLayout_2.setContentsMargins(0, 54, 0, 54)
        self.Name = QLineEdit(self.frame_2)
        self.Name.setObjectName(u"Name")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Name.sizePolicy().hasHeightForWidth())
        self.Name.setSizePolicy(sizePolicy3)
        self.Name.setMinimumSize(QSize(301, 38))
        font4 = QFont()
        font4.setPointSize(10)
        self.Name.setFont(font4)
        self.Name.setStyleSheet(u"QLineEdit{\n"
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
        self.Name.setEchoMode(QLineEdit.Normal)
        self.Name.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Name, 0, 0, 1, 1)

        self.Email = QLineEdit(self.frame_2)
        self.Email.setObjectName(u"Email")
        sizePolicy3.setHeightForWidth(self.Email.sizePolicy().hasHeightForWidth())
        self.Email.setSizePolicy(sizePolicy3)
        self.Email.setMinimumSize(QSize(301, 38))
        self.Email.setFont(font4)
        self.Email.setStyleSheet(u"QLineEdit{\n"
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
        self.Email.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Email, 1, 0, 1, 1)

        self.Password = QLineEdit(self.frame_2)
        self.Password.setObjectName(u"Password")
        sizePolicy3.setHeightForWidth(self.Password.sizePolicy().hasHeightForWidth())
        self.Password.setSizePolicy(sizePolicy3)
        self.Password.setMinimumSize(QSize(301, 38))
        self.Password.setFont(font4)
        self.Password.setStyleSheet(u"QLineEdit{\n"
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
        self.Password.setEchoMode(QLineEdit.Password)
        self.Password.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Password, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 3, 1, 3, 1)

        self.TitleBar_2 = QFrame(self.Content)
        self.TitleBar_2.setObjectName(u"TitleBar_2")
        sizePolicy.setHeightForWidth(self.TitleBar_2.sizePolicy().hasHeightForWidth())
        self.TitleBar_2.setSizePolicy(sizePolicy)
        self.TitleBar_2.setMinimumSize(QSize(0, 0))
        self.TitleBar_2.setMaximumSize(QSize(16777215, 30))
        self.TitleBar_2.setStyleSheet(u"QFrame{\n"
"\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 215), stop:1 rgba(11, 15, 50, 194));\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"\n"
"}")
        self.TitleBar_2.setFrameShape(QFrame.StyledPanel)
        self.TitleBar_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.TitleBar_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.TitleBar = QFrame(self.TitleBar_2)
        self.TitleBar.setObjectName(u"TitleBar")
        self.TitleBar.setCursor(QCursor(Qt.SizeAllCursor))
        self.TitleBar.setFrameShape(QFrame.StyledPanel)
        self.TitleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.TitleBar)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.TitleBar)

        self.frame_8 = QFrame(self.TitleBar_2)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy4)
        self.frame_8.setMinimumSize(QSize(0, 25))
        self.frame_8.setMaximumSize(QSize(100, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, 0, 0, 0)
        self.Minimizebtn = QPushButton(self.frame_8)
        self.Minimizebtn.setObjectName(u"Minimizebtn")
        sizePolicy4.setHeightForWidth(self.Minimizebtn.sizePolicy().hasHeightForWidth())
        self.Minimizebtn.setSizePolicy(sizePolicy4)
        self.Minimizebtn.setMaximumSize(QSize(15, 15))
        self.Minimizebtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 0);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 0, 150);\n"
"\n"
"}")
        self.Minimizebtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_6.addWidget(self.Minimizebtn)

        self.Maximizebtn = QPushButton(self.frame_8)
        self.Maximizebtn.setObjectName(u"Maximizebtn")
        sizePolicy4.setHeightForWidth(self.Maximizebtn.sizePolicy().hasHeightForWidth())
        self.Maximizebtn.setSizePolicy(sizePolicy4)
        self.Maximizebtn.setMaximumSize(QSize(15, 15))
        self.Maximizebtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 0);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(85, 170, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.Maximizebtn)

        self.CloseButton = QPushButton(self.frame_8)
        self.CloseButton.setObjectName(u"CloseButton")
        sizePolicy4.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy4)
        self.CloseButton.setMaximumSize(QSize(15, 15))
        self.CloseButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(235, 0, 16);\n"
"\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.CloseButton)


        self.horizontalLayout_5.addWidget(self.frame_8)


        self.gridLayout_4.addWidget(self.TitleBar_2, 0, 0, 1, 4)

        self.stackedWidget = QStackedWidget(self.Content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy5)
        self.stackedWidget.setMaximumSize(QSize(16777215, 64))
        self.stackedWidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.UsusalTitle = QWidget()
        self.UsusalTitle.setObjectName(u"UsusalTitle")
        self.horizontalLayout_2 = QHBoxLayout(self.UsusalTitle)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Description = QLabel(self.UsusalTitle)
        self.Description.setObjectName(u"Description")
        self.Description.setFont(font3)
        self.Description.setLayoutDirection(Qt.LeftToRight)
        self.Description.setAutoFillBackground(False)
        self.Description.setStyleSheet(u"border-radius:15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 200), stop:0.892045 rgba(255, 255, 52, 200));\n"
"\n"
"")
        self.Description.setTextFormat(Qt.RichText)
        self.Description.setScaledContents(False)
        self.Description.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.Description)

        self.stackedWidget.addWidget(self.UsusalTitle)
        self.EmailError = QWidget()
        self.EmailError.setObjectName(u"EmailError")
        self.horizontalLayout_8 = QHBoxLayout(self.EmailError)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.NotFilledAlertFrame = QFrame(self.EmailError)
        self.NotFilledAlertFrame.setObjectName(u"NotFilledAlertFrame")
        sizePolicy.setHeightForWidth(self.NotFilledAlertFrame.sizePolicy().hasHeightForWidth())
        self.NotFilledAlertFrame.setSizePolicy(sizePolicy)
        self.NotFilledAlertFrame.setMinimumSize(QSize(0, 50))
        self.NotFilledAlertFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 215), stop:1 rgba(11, 15, 50, 194));\n"
"border-radius:10px;")
        self.NotFilledAlertFrame.setFrameShape(QFrame.StyledPanel)
        self.NotFilledAlertFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.NotFilledAlertFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.NotFilledAlertText = QLabel(self.NotFilledAlertFrame)
        self.NotFilledAlertText.setObjectName(u"NotFilledAlertText")
        font5 = QFont()
        font5.setPointSize(11)
        self.NotFilledAlertText.setFont(font5)
        self.NotFilledAlertText.setStyleSheet(u"QLabel{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.NotFilledAlertText.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.NotFilledAlertText)

        self.NotFilledClose = QPushButton(self.NotFilledAlertFrame)
        self.NotFilledClose.setObjectName(u"NotFilledClose")
        sizePolicy3.setHeightForWidth(self.NotFilledClose.sizePolicy().hasHeightForWidth())
        self.NotFilledClose.setSizePolicy(sizePolicy3)
        self.NotFilledClose.setMinimumSize(QSize(3, 0))
        self.NotFilledClose.setMaximumSize(QSize(35, 16777215))
        font6 = QFont()
        font6.setBold(True)
        font6.setWeight(75)
        self.NotFilledClose.setFont(font6)
        self.NotFilledClose.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_7.addWidget(self.NotFilledClose)


        self.horizontalLayout_8.addWidget(self.NotFilledAlertFrame)

        self.stackedWidget.addWidget(self.EmailError)

        self.gridLayout_4.addWidget(self.stackedWidget, 2, 0, 1, 4)


        self.horizontalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.NextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.MaleRadioBtn.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.FemaleRadioBtn.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.Description_5.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.Description_4.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.Name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Your Name", None))
        self.Email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Your Email", None))
        self.Password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Your Password", None))
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
        self.Description.setText(QCoreApplication.translate("MainWindow", u" Your Information is required by the Automation Software", None))
        self.NotFilledAlertText.setText(QCoreApplication.translate("MainWindow", u"Please Filll All The Required Fields Correctly", None))
        self.NotFilledClose.setText(QCoreApplication.translate("MainWindow", u"X", None))
    # retranslateUi

