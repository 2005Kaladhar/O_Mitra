# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowragiGB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainPage(object):
    def setupUi(self, MainPage):
        if not MainPage.objectName():
            MainPage.setObjectName(u"MainPage")
        MainPage.resize(849, 611)
        MainPage.setMinimumSize(QSize(0, 530))
        icon = QIcon()
        icon.addFile(u"../O-Mitra Original Working With Background IMages/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainPage.setWindowIcon(icon)
        MainPage.setStyleSheet(u"border-image: url(:/newPrefix/Untitled.png);\n"
"\n"
"")
        self.centralwidget = QWidget(MainPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(0, 0, 0);\n"
"\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Credit = QFrame(self.frame)
        self.Credit.setObjectName(u"Credit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Credit.sizePolicy().hasHeightForWidth())
        self.Credit.setSizePolicy(sizePolicy)
        self.Credit.setMinimumSize(QSize(0, 15))
        self.Credit.setMaximumSize(QSize(16777215, 100))
        self.Credit.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color: rgba(189, 27, 184, 150);\n"
"border-image:None;\n"
"}")
        self.Credit.setFrameShape(QFrame.StyledPanel)
        self.Credit.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Credit)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(9, 0, 0, 0)
        self.label = QLabel(self.Credit)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(16777215, 200))
        self.label.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(185, 185, 185);\n"
"\n"
"}")
        self.label.setTextFormat(Qt.RichText)

        self.horizontalLayout_6.addWidget(self.label)


        self.gridLayout.addWidget(self.Credit, 3, 0, 1, 1)

        self.Content = QFrame(self.frame)
        self.Content.setObjectName(u"Content")
        self.Content.setMinimumSize(QSize(0, 50))
        self.Content.setStyleSheet(u"QFrame{\n"
"	\n"
"border-image:None;\n"
"\n"
"}")
        self.Content.setFrameShape(QFrame.StyledPanel)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.Content)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.SubContent = QFrame(self.Content)
        self.SubContent.setObjectName(u"SubContent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.SubContent.sizePolicy().hasHeightForWidth())
        self.SubContent.setSizePolicy(sizePolicy2)
        self.SubContent.setStyleSheet(u"QFrame{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-radius:15px;\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-image:None;\n"
"}")
        self.SubContent.setFrameShape(QFrame.StyledPanel)
        self.SubContent.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.SubContent)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.SubContent)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy3)
        self.frame_8.setMaximumSize(QSize(16777215, 150))
        self.frame_8.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_8)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 3, -1, 9)
        self.Description = QLabel(self.frame_8)
        self.Description.setObjectName(u"Description")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Description.sizePolicy().hasHeightForWidth())
        self.Description.setSizePolicy(sizePolicy4)
        self.Description.setMinimumSize(QSize(0, 43))
        self.Description.setMaximumSize(QSize(1677215, 16777215))
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Description.setFont(font)
        self.Description.setLayoutDirection(Qt.LeftToRight)
        self.Description.setAutoFillBackground(False)
        self.Description.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.0113636, y1:0.637, x2:1, y2:0.664773, stop:0 rgba(242, 255, 29, 190), stop:1 rgba(67, 201, 0, 240));\n"
"border-radius:18px;")
        self.Description.setTextFormat(Qt.RichText)
        self.Description.setScaledContents(False)
        self.Description.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Description)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(194, 0, 194, 0)
        self.Description_2 = QLabel(self.frame_9)
        self.Description_2.setObjectName(u"Description_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Description_2.sizePolicy().hasHeightForWidth())
        self.Description_2.setSizePolicy(sizePolicy5)
        self.Description_2.setMinimumSize(QSize(0, 36))
        self.Description_2.setMaximumSize(QSize(1677215, 16777215))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.Description_2.setFont(font1)
        self.Description_2.setLayoutDirection(Qt.LeftToRight)
        self.Description_2.setAutoFillBackground(False)
        self.Description_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.0113636, y1:0.637, x2:1, y2:0.664773, stop:0 rgba(242, 255, 29, 150), stop:1 rgba(67, 201, 0, 200));\n"
"border-radius:17px;")
        self.Description_2.setTextFormat(Qt.RichText)
        self.Description_2.setScaledContents(False)
        self.Description_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.Description_2)


        self.verticalLayout.addWidget(self.frame_9)


        self.gridLayout_5.addWidget(self.frame_8, 0, 0, 1, 4)

        self.frame_7 = QFrame(self.SubContent)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(700, 16777215))
        self.frame_7.setStyleSheet(u"border-image:None;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(3)
        self.gridLayout_4.setVerticalSpacing(35)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 4)
        self.Subject_1From = QTimeEdit(self.frame_7)
        self.Subject_1From.setObjectName(u"Subject_1From")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Subject_1From.sizePolicy().hasHeightForWidth())
        self.Subject_1From.setSizePolicy(sizePolicy6)
        self.Subject_1From.setMouseTracking(True)
        self.Subject_1From.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:7px;\n"
"\n"
"\n"
"}\n"
"QTimeEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_1From.setAlignment(Qt.AlignCenter)
        self.Subject_1From.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Subject_1From.setAccelerated(False)
        self.Subject_1From.setProperty("showGroupSeparator", False)

        self.gridLayout_4.addWidget(self.Subject_1From, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(15, 16777215))
        self.label_2.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_2, 0, 1, 1, 1)

        self.Subject_1To = QTimeEdit(self.frame_7)
        self.Subject_1To.setObjectName(u"Subject_1To")
        sizePolicy6.setHeightForWidth(self.Subject_1To.sizePolicy().hasHeightForWidth())
        self.Subject_1To.setSizePolicy(sizePolicy6)
        self.Subject_1To.setMouseTracking(True)
        self.Subject_1To.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QTimeEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_1To.setAlignment(Qt.AlignCenter)
        self.Subject_1To.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Subject_1To.setProperty("showGroupSeparator", False)

        self.gridLayout_4.addWidget(self.Subject_1To, 0, 2, 1, 1)

        self.SubjectsDaysBtn = QPushButton(self.frame_7)
        self.SubjectsDaysBtn.setObjectName(u"SubjectsDaysBtn")
        sizePolicy6.setHeightForWidth(self.SubjectsDaysBtn.sizePolicy().hasHeightForWidth())
        self.SubjectsDaysBtn.setSizePolicy(sizePolicy6)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setWeight(50)
        self.SubjectsDaysBtn.setFont(font2)
        self.SubjectsDaysBtn.setStyleSheet(u"QPushButton{\n"
"border-radius:7px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(232, 154, 0, 255), stop:1 rgba(255, 102, 25, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 170, 0, 255));\n"
"}")

        self.gridLayout_4.addWidget(self.SubjectsDaysBtn, 0, 3, 1, 1)

        self.Subject_2From = QTimeEdit(self.frame_7)
        self.Subject_2From.setObjectName(u"Subject_2From")
        sizePolicy6.setHeightForWidth(self.Subject_2From.sizePolicy().hasHeightForWidth())
        self.Subject_2From.setSizePolicy(sizePolicy6)
        self.Subject_2From.setMouseTracking(True)
        self.Subject_2From.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QTimeEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_2From.setAlignment(Qt.AlignCenter)
        self.Subject_2From.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Subject_2From.setProperty("showGroupSeparator", False)

        self.gridLayout_4.addWidget(self.Subject_2From, 1, 0, 1, 1)

        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(15, 16777215))
        self.label_3.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_3, 1, 1, 1, 1)

        self.Subject_2To = QTimeEdit(self.frame_7)
        self.Subject_2To.setObjectName(u"Subject_2To")
        sizePolicy6.setHeightForWidth(self.Subject_2To.sizePolicy().hasHeightForWidth())
        self.Subject_2To.setSizePolicy(sizePolicy6)
        self.Subject_2To.setMouseTracking(True)
        self.Subject_2To.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QTimeEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_2To.setAlignment(Qt.AlignCenter)
        self.Subject_2To.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Subject_2To.setProperty("showGroupSeparator", False)

        self.gridLayout_4.addWidget(self.Subject_2To, 1, 2, 1, 1)

        self.SubjectsDaysBtn_2 = QPushButton(self.frame_7)
        self.SubjectsDaysBtn_2.setObjectName(u"SubjectsDaysBtn_2")
        sizePolicy6.setHeightForWidth(self.SubjectsDaysBtn_2.sizePolicy().hasHeightForWidth())
        self.SubjectsDaysBtn_2.setSizePolicy(sizePolicy6)
        self.SubjectsDaysBtn_2.setFont(font2)
        self.SubjectsDaysBtn_2.setStyleSheet(u"QPushButton{\n"
"border-radius:7px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(232, 154, 0, 255), stop:1 rgba(255, 102, 25, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 170, 0, 255));\n"
"}")

        self.gridLayout_4.addWidget(self.SubjectsDaysBtn_2, 1, 3, 1, 1)

        self.Subject_3From = QTimeEdit(self.frame_7)
        self.Subject_3From.setObjectName(u"Subject_3From")
        sizePolicy6.setHeightForWidth(self.Subject_3From.sizePolicy().hasHeightForWidth())
        self.Subject_3From.setSizePolicy(sizePolicy6)
        self.Subject_3From.setMouseTracking(True)
        self.Subject_3From.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QTimeEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_3From.setAlignment(Qt.AlignCenter)
        self.Subject_3From.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Subject_3From.setProperty("showGroupSeparator", False)

        self.gridLayout_4.addWidget(self.Subject_3From, 2, 0, 1, 1)

        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(15, 16777215))
        self.label_4.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_4, 2, 1, 1, 1)

        self.Subject_3To = QTimeEdit(self.frame_7)
        self.Subject_3To.setObjectName(u"Subject_3To")
        sizePolicy6.setHeightForWidth(self.Subject_3To.sizePolicy().hasHeightForWidth())
        self.Subject_3To.setSizePolicy(sizePolicy6)
        self.Subject_3To.setMouseTracking(True)
        self.Subject_3To.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QTimeEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_3To.setAlignment(Qt.AlignCenter)
        self.Subject_3To.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Subject_3To.setProperty("showGroupSeparator", False)

        self.gridLayout_4.addWidget(self.Subject_3To, 2, 2, 1, 1)

        self.SubjectsDaysBtn_3 = QPushButton(self.frame_7)
        self.SubjectsDaysBtn_3.setObjectName(u"SubjectsDaysBtn_3")
        sizePolicy6.setHeightForWidth(self.SubjectsDaysBtn_3.sizePolicy().hasHeightForWidth())
        self.SubjectsDaysBtn_3.setSizePolicy(sizePolicy6)
        self.SubjectsDaysBtn_3.setFont(font2)
        self.SubjectsDaysBtn_3.setStyleSheet(u"QPushButton{\n"
"border-radius:7px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(232, 154, 0, 255), stop:1 rgba(255, 102, 25, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 170, 0, 255));\n"
"}")

        self.gridLayout_4.addWidget(self.SubjectsDaysBtn_3, 2, 3, 1, 1)

        self.Subject_4From = QTimeEdit(self.frame_7)
        self.Subject_4From.setObjectName(u"Subject_4From")
        sizePolicy6.setHeightForWidth(self.Subject_4From.sizePolicy().hasHeightForWidth())
        self.Subject_4From.setSizePolicy(sizePolicy6)
        self.Subject_4From.setMouseTracking(True)
        self.Subject_4From.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QTimeEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_4From.setAlignment(Qt.AlignCenter)
        self.Subject_4From.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Subject_4From.setProperty("showGroupSeparator", False)

        self.gridLayout_4.addWidget(self.Subject_4From, 3, 0, 1, 1)

        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(15, 16777215))
        self.label_5.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_5, 3, 1, 1, 1)

        self.Subject_4To = QTimeEdit(self.frame_7)
        self.Subject_4To.setObjectName(u"Subject_4To")
        sizePolicy6.setHeightForWidth(self.Subject_4To.sizePolicy().hasHeightForWidth())
        self.Subject_4To.setSizePolicy(sizePolicy6)
        self.Subject_4To.setMouseTracking(True)
        self.Subject_4To.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QTimeEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_4To.setAlignment(Qt.AlignCenter)
        self.Subject_4To.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Subject_4To.setProperty("showGroupSeparator", False)

        self.gridLayout_4.addWidget(self.Subject_4To, 3, 2, 1, 1)

        self.SubjectsDaysBtn_4 = QPushButton(self.frame_7)
        self.SubjectsDaysBtn_4.setObjectName(u"SubjectsDaysBtn_4")
        sizePolicy6.setHeightForWidth(self.SubjectsDaysBtn_4.sizePolicy().hasHeightForWidth())
        self.SubjectsDaysBtn_4.setSizePolicy(sizePolicy6)
        self.SubjectsDaysBtn_4.setFont(font2)
        self.SubjectsDaysBtn_4.setStyleSheet(u"QPushButton{\n"
"border-radius:7px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(232, 154, 0, 255), stop:1 rgba(255, 102, 25, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 170, 0, 255));\n"
"}")

        self.gridLayout_4.addWidget(self.SubjectsDaysBtn_4, 3, 3, 1, 1)

        self.Subject_5From = QTimeEdit(self.frame_7)
        self.Subject_5From.setObjectName(u"Subject_5From")
        sizePolicy6.setHeightForWidth(self.Subject_5From.sizePolicy().hasHeightForWidth())
        self.Subject_5From.setSizePolicy(sizePolicy6)
        self.Subject_5From.setMouseTracking(True)
        self.Subject_5From.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QTimeEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_5From.setAlignment(Qt.AlignCenter)
        self.Subject_5From.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Subject_5From.setProperty("showGroupSeparator", False)

        self.gridLayout_4.addWidget(self.Subject_5From, 4, 0, 1, 1)

        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(15, 16777215))
        self.label_6.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_6, 4, 1, 1, 1)

        self.Subject_5To = QTimeEdit(self.frame_7)
        self.Subject_5To.setObjectName(u"Subject_5To")
        sizePolicy6.setHeightForWidth(self.Subject_5To.sizePolicy().hasHeightForWidth())
        self.Subject_5To.setSizePolicy(sizePolicy6)
        self.Subject_5To.setMouseTracking(True)
        self.Subject_5To.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QTimeEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_5To.setAlignment(Qt.AlignCenter)
        self.Subject_5To.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Subject_5To.setProperty("showGroupSeparator", False)

        self.gridLayout_4.addWidget(self.Subject_5To, 4, 2, 1, 1)

        self.SubjectsDaysBtn_5 = QPushButton(self.frame_7)
        self.SubjectsDaysBtn_5.setObjectName(u"SubjectsDaysBtn_5")
        sizePolicy6.setHeightForWidth(self.SubjectsDaysBtn_5.sizePolicy().hasHeightForWidth())
        self.SubjectsDaysBtn_5.setSizePolicy(sizePolicy6)
        self.SubjectsDaysBtn_5.setFont(font2)
        self.SubjectsDaysBtn_5.setStyleSheet(u"QPushButton{\n"
"border-radius:7px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(232, 154, 0, 255), stop:1 rgba(255, 102, 25, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 170, 0, 255));\n"
"}")

        self.gridLayout_4.addWidget(self.SubjectsDaysBtn_5, 4, 3, 1, 1)

        self.Subject_6From = QTimeEdit(self.frame_7)
        self.Subject_6From.setObjectName(u"Subject_6From")
        sizePolicy6.setHeightForWidth(self.Subject_6From.sizePolicy().hasHeightForWidth())
        self.Subject_6From.setSizePolicy(sizePolicy6)
        self.Subject_6From.setMouseTracking(True)
        self.Subject_6From.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QTimeEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_6From.setAlignment(Qt.AlignCenter)
        self.Subject_6From.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Subject_6From.setProperty("showGroupSeparator", False)

        self.gridLayout_4.addWidget(self.Subject_6From, 5, 0, 1, 1)

        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(15, 16777215))
        self.label_7.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_7, 5, 1, 1, 1)

        self.Subject_6To = QTimeEdit(self.frame_7)
        self.Subject_6To.setObjectName(u"Subject_6To")
        sizePolicy6.setHeightForWidth(self.Subject_6To.sizePolicy().hasHeightForWidth())
        self.Subject_6To.setSizePolicy(sizePolicy6)
        self.Subject_6To.setMouseTracking(True)
        self.Subject_6To.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QTimeEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_6To.setAlignment(Qt.AlignCenter)
        self.Subject_6To.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Subject_6To.setProperty("showGroupSeparator", False)

        self.gridLayout_4.addWidget(self.Subject_6To, 5, 2, 1, 1)

        self.SubjectsDaysBtn_6 = QPushButton(self.frame_7)
        self.SubjectsDaysBtn_6.setObjectName(u"SubjectsDaysBtn_6")
        sizePolicy6.setHeightForWidth(self.SubjectsDaysBtn_6.sizePolicy().hasHeightForWidth())
        self.SubjectsDaysBtn_6.setSizePolicy(sizePolicy6)
        self.SubjectsDaysBtn_6.setFont(font2)
        self.SubjectsDaysBtn_6.setStyleSheet(u"QPushButton{\n"
"border-radius:7px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(232, 154, 0, 255), stop:1 rgba(255, 102, 25, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 170, 0, 255));\n"
"}")

        self.gridLayout_4.addWidget(self.SubjectsDaysBtn_6, 5, 3, 1, 1)

        self.Subject_7From = QTimeEdit(self.frame_7)
        self.Subject_7From.setObjectName(u"Subject_7From")
        sizePolicy6.setHeightForWidth(self.Subject_7From.sizePolicy().hasHeightForWidth())
        self.Subject_7From.setSizePolicy(sizePolicy6)
        self.Subject_7From.setMouseTracking(True)
        self.Subject_7From.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QTimeEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_7From.setAlignment(Qt.AlignCenter)
        self.Subject_7From.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Subject_7From.setProperty("showGroupSeparator", False)

        self.gridLayout_4.addWidget(self.Subject_7From, 6, 0, 1, 1)

        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(15, 16777215))
        self.label_8.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_8, 6, 1, 1, 1)

        self.Subject_7To = QTimeEdit(self.frame_7)
        self.Subject_7To.setObjectName(u"Subject_7To")
        sizePolicy6.setHeightForWidth(self.Subject_7To.sizePolicy().hasHeightForWidth())
        self.Subject_7To.setSizePolicy(sizePolicy6)
        self.Subject_7To.setMouseTracking(True)
        self.Subject_7To.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QTimeEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_7To.setAlignment(Qt.AlignCenter)
        self.Subject_7To.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Subject_7To.setProperty("showGroupSeparator", False)

        self.gridLayout_4.addWidget(self.Subject_7To, 6, 2, 1, 1)

        self.SubjectsDaysBtn_7 = QPushButton(self.frame_7)
        self.SubjectsDaysBtn_7.setObjectName(u"SubjectsDaysBtn_7")
        sizePolicy6.setHeightForWidth(self.SubjectsDaysBtn_7.sizePolicy().hasHeightForWidth())
        self.SubjectsDaysBtn_7.setSizePolicy(sizePolicy6)
        self.SubjectsDaysBtn_7.setFont(font2)
        self.SubjectsDaysBtn_7.setStyleSheet(u"QPushButton{\n"
"border-radius:7px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(232, 154, 0, 255), stop:1 rgba(255, 102, 25, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 170, 0, 255));\n"
"}")

        self.gridLayout_4.addWidget(self.SubjectsDaysBtn_7, 6, 3, 1, 1)

        self.Subject_8From = QTimeEdit(self.frame_7)
        self.Subject_8From.setObjectName(u"Subject_8From")
        sizePolicy6.setHeightForWidth(self.Subject_8From.sizePolicy().hasHeightForWidth())
        self.Subject_8From.setSizePolicy(sizePolicy6)
        self.Subject_8From.setMouseTracking(True)
        self.Subject_8From.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QTimeEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_8From.setAlignment(Qt.AlignCenter)
        self.Subject_8From.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Subject_8From.setProperty("showGroupSeparator", False)

        self.gridLayout_4.addWidget(self.Subject_8From, 7, 0, 1, 1)

        self.Subject_8To_2 = QTimeEdit(self.frame_7)
        self.Subject_8To_2.setObjectName(u"Subject_8To_2")
        sizePolicy6.setHeightForWidth(self.Subject_8To_2.sizePolicy().hasHeightForWidth())
        self.Subject_8To_2.setSizePolicy(sizePolicy6)
        self.Subject_8To_2.setMouseTracking(True)
        self.Subject_8To_2.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QTimeEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_8To_2.setAlignment(Qt.AlignCenter)
        self.Subject_8To_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Subject_8To_2.setProperty("showGroupSeparator", False)

        self.gridLayout_4.addWidget(self.Subject_8To_2, 7, 2, 1, 1)

        self.SubjectsDaysBtn_8 = QPushButton(self.frame_7)
        self.SubjectsDaysBtn_8.setObjectName(u"SubjectsDaysBtn_8")
        sizePolicy6.setHeightForWidth(self.SubjectsDaysBtn_8.sizePolicy().hasHeightForWidth())
        self.SubjectsDaysBtn_8.setSizePolicy(sizePolicy6)
        self.SubjectsDaysBtn_8.setFont(font2)
        self.SubjectsDaysBtn_8.setStyleSheet(u"QPushButton{\n"
"border-radius:7px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(232, 154, 0, 255), stop:1 rgba(255, 102, 25, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 170, 0, 255));\n"
"}")

        self.gridLayout_4.addWidget(self.SubjectsDaysBtn_8, 7, 3, 1, 1)

        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(15, 16777215))
        self.label_9.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_9, 7, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame_7, 1, 2, 1, 1)

        self.frame_6 = QFrame(self.SubContent)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy7)
        self.frame_6.setMaximumSize(QSize(600, 16777215))
        self.frame_6.setStyleSheet(u"border-image:None;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(22)
        self.gridLayout_3.setContentsMargins(-1, 0, -1, 4)
        self.Subject_Link_1 = QLineEdit(self.frame_6)
        self.Subject_Link_1.setObjectName(u"Subject_Link_1")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.Subject_Link_1.sizePolicy().hasHeightForWidth())
        self.Subject_Link_1.setSizePolicy(sizePolicy8)
        font3 = QFont()
        font3.setPointSize(9)
        self.Subject_Link_1.setFont(font3)
        self.Subject_Link_1.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"text-align:centre;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_Link_1.setEchoMode(QLineEdit.Normal)
        self.Subject_Link_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Subject_Link_1, 0, 0, 1, 1)

        self.Subject_Link_2 = QLineEdit(self.frame_6)
        self.Subject_Link_2.setObjectName(u"Subject_Link_2")
        sizePolicy8.setHeightForWidth(self.Subject_Link_2.sizePolicy().hasHeightForWidth())
        self.Subject_Link_2.setSizePolicy(sizePolicy8)
        self.Subject_Link_2.setFont(font3)
        self.Subject_Link_2.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"text-align:centre;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_Link_2.setEchoMode(QLineEdit.Normal)
        self.Subject_Link_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Subject_Link_2, 1, 0, 1, 1)

        self.Subject_Link_3 = QLineEdit(self.frame_6)
        self.Subject_Link_3.setObjectName(u"Subject_Link_3")
        sizePolicy8.setHeightForWidth(self.Subject_Link_3.sizePolicy().hasHeightForWidth())
        self.Subject_Link_3.setSizePolicy(sizePolicy8)
        self.Subject_Link_3.setFont(font3)
        self.Subject_Link_3.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"text-align:centre;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_Link_3.setEchoMode(QLineEdit.Normal)
        self.Subject_Link_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Subject_Link_3, 2, 0, 1, 1)

        self.Subject_Link_4 = QLineEdit(self.frame_6)
        self.Subject_Link_4.setObjectName(u"Subject_Link_4")
        sizePolicy8.setHeightForWidth(self.Subject_Link_4.sizePolicy().hasHeightForWidth())
        self.Subject_Link_4.setSizePolicy(sizePolicy8)
        self.Subject_Link_4.setFont(font3)
        self.Subject_Link_4.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"text-align:centre;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_Link_4.setEchoMode(QLineEdit.Normal)
        self.Subject_Link_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Subject_Link_4, 3, 0, 1, 1)

        self.Subject_Link_5 = QLineEdit(self.frame_6)
        self.Subject_Link_5.setObjectName(u"Subject_Link_5")
        sizePolicy8.setHeightForWidth(self.Subject_Link_5.sizePolicy().hasHeightForWidth())
        self.Subject_Link_5.setSizePolicy(sizePolicy8)
        self.Subject_Link_5.setFont(font3)
        self.Subject_Link_5.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"text-align:centre;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_Link_5.setEchoMode(QLineEdit.Normal)
        self.Subject_Link_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Subject_Link_5, 4, 0, 1, 1)

        self.Subject_Link_6 = QLineEdit(self.frame_6)
        self.Subject_Link_6.setObjectName(u"Subject_Link_6")
        sizePolicy8.setHeightForWidth(self.Subject_Link_6.sizePolicy().hasHeightForWidth())
        self.Subject_Link_6.setSizePolicy(sizePolicy8)
        self.Subject_Link_6.setFont(font3)
        self.Subject_Link_6.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"text-align:centre;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_Link_6.setEchoMode(QLineEdit.Normal)
        self.Subject_Link_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Subject_Link_6, 5, 0, 1, 1)

        self.Subject_Link_7 = QLineEdit(self.frame_6)
        self.Subject_Link_7.setObjectName(u"Subject_Link_7")
        sizePolicy8.setHeightForWidth(self.Subject_Link_7.sizePolicy().hasHeightForWidth())
        self.Subject_Link_7.setSizePolicy(sizePolicy8)
        self.Subject_Link_7.setFont(font3)
        self.Subject_Link_7.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"text-align:centre;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_Link_7.setEchoMode(QLineEdit.Normal)
        self.Subject_Link_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Subject_Link_7, 6, 0, 1, 1)

        self.Subject_Link_8 = QLineEdit(self.frame_6)
        self.Subject_Link_8.setObjectName(u"Subject_Link_8")
        sizePolicy8.setHeightForWidth(self.Subject_Link_8.sizePolicy().hasHeightForWidth())
        self.Subject_Link_8.setSizePolicy(sizePolicy8)
        self.Subject_Link_8.setFont(font3)
        self.Subject_Link_8.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"text-align:centre;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	background-color: rgb(255, 216, 76);\n"
"\n"
"}\n"
"")
        self.Subject_Link_8.setEchoMode(QLineEdit.Normal)
        self.Subject_Link_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Subject_Link_8, 7, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_6, 1, 1, 1, 1)

        self.stackedWidget = QStackedWidget(self.SubContent)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy7.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy7)
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(300, 16777215))
        self.stackedWidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.38, x2:1, y2:0.670636, stop:0 rgba(0, 0, 0, 59), stop:1 rgba(13, 13, 13, 11));\n"
"\n"
"border-image:None;")
        self.Day8 = QWidget()
        self.Day8.setObjectName(u"Day8")
        self.Day8.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.horizontalLayout_9 = QHBoxLayout(self.Day8)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.SubjectDays_8 = QFrame(self.Day8)
        self.SubjectDays_8.setObjectName(u"SubjectDays_8")
        self.SubjectDays_8.setFrameShape(QFrame.StyledPanel)
        self.SubjectDays_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.SubjectDays_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.Subject8DaysHeading = QLabel(self.SubjectDays_8)
        self.Subject8DaysHeading.setObjectName(u"Subject8DaysHeading")
        self.Subject8DaysHeading.setMinimumSize(QSize(0, 36))
        self.Subject8DaysHeading.setMaximumSize(QSize(16777215, 100))
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setWeight(75)
        self.Subject8DaysHeading.setFont(font4)
        self.Subject8DaysHeading.setStyleSheet(u"QLabel{\n"
"	\n"
"color: rgb(241, 44, 172);\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(150, 255, 69,200);\n"
"border-radius:50px;\n"
"\n"
"}")
        self.Subject8DaysHeading.setMidLineWidth(4)
        self.Subject8DaysHeading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.Subject8DaysHeading)

        self.Subject8Sunday = QCheckBox(self.SubjectDays_8)
        self.Subject8Sunday.setObjectName(u"Subject8Sunday")
        font5 = QFont()
        font5.setPointSize(11)
        self.Subject8Sunday.setFont(font5)
        self.Subject8Sunday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject8Sunday.setTristate(False)

        self.verticalLayout_11.addWidget(self.Subject8Sunday)

        self.Subject8Monday = QCheckBox(self.SubjectDays_8)
        self.Subject8Monday.setObjectName(u"Subject8Monday")
        self.Subject8Monday.setFont(font5)
        self.Subject8Monday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject8Monday.setTristate(False)

        self.verticalLayout_11.addWidget(self.Subject8Monday)

        self.Subject8Tuesday = QCheckBox(self.SubjectDays_8)
        self.Subject8Tuesday.setObjectName(u"Subject8Tuesday")
        self.Subject8Tuesday.setFont(font5)
        self.Subject8Tuesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject8Tuesday.setTristate(False)

        self.verticalLayout_11.addWidget(self.Subject8Tuesday)

        self.Subject8Wednesday = QCheckBox(self.SubjectDays_8)
        self.Subject8Wednesday.setObjectName(u"Subject8Wednesday")
        self.Subject8Wednesday.setFont(font5)
        self.Subject8Wednesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject8Wednesday.setTristate(False)

        self.verticalLayout_11.addWidget(self.Subject8Wednesday)

        self.Subject8Thursday = QCheckBox(self.SubjectDays_8)
        self.Subject8Thursday.setObjectName(u"Subject8Thursday")
        self.Subject8Thursday.setFont(font5)
        self.Subject8Thursday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject8Thursday.setTristate(False)

        self.verticalLayout_11.addWidget(self.Subject8Thursday)

        self.Subject8Friday = QCheckBox(self.SubjectDays_8)
        self.Subject8Friday.setObjectName(u"Subject8Friday")
        self.Subject8Friday.setFont(font5)
        self.Subject8Friday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject8Friday.setTristate(False)

        self.verticalLayout_11.addWidget(self.Subject8Friday)

        self.Subject8Saturday = QCheckBox(self.SubjectDays_8)
        self.Subject8Saturday.setObjectName(u"Subject8Saturday")
        self.Subject8Saturday.setFont(font5)
        self.Subject8Saturday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject8Saturday.setTristate(False)

        self.verticalLayout_11.addWidget(self.Subject8Saturday)


        self.horizontalLayout_9.addWidget(self.SubjectDays_8)

        self.stackedWidget.addWidget(self.Day8)
        self.Day7 = QWidget()
        self.Day7.setObjectName(u"Day7")
        self.Day7.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.horizontalLayout_10 = QHBoxLayout(self.Day7)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.SubjectDays_7 = QFrame(self.Day7)
        self.SubjectDays_7.setObjectName(u"SubjectDays_7")
        self.SubjectDays_7.setStyleSheet(u"QLabel{\n"
"\n"
"background-color: rgba(150, 255, 69,200);\n"
"\n"
"border-radius:90px;\n"
"\n"
"\n"
"\n"
"\n"
"}")
        self.SubjectDays_7.setFrameShape(QFrame.StyledPanel)
        self.SubjectDays_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.SubjectDays_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.Subject7DaysHeading = QLabel(self.SubjectDays_7)
        self.Subject7DaysHeading.setObjectName(u"Subject7DaysHeading")
        self.Subject7DaysHeading.setMaximumSize(QSize(16777215, 100))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.Subject7DaysHeading.setFont(font6)
        self.Subject7DaysHeading.setStyleSheet(u"QLabel{\n"
"	\n"
"color: rgb(241, 44, 172);\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(150, 255, 69,200);\n"
"border-radius:50px;\n"
"\n"
"}")
        self.Subject7DaysHeading.setMidLineWidth(4)
        self.Subject7DaysHeading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.Subject7DaysHeading)

        self.Subject7Sunday = QCheckBox(self.SubjectDays_7)
        self.Subject7Sunday.setObjectName(u"Subject7Sunday")
        self.Subject7Sunday.setFont(font5)
        self.Subject7Sunday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject7Sunday.setTristate(False)

        self.verticalLayout_10.addWidget(self.Subject7Sunday)

        self.Subject7Monday = QCheckBox(self.SubjectDays_7)
        self.Subject7Monday.setObjectName(u"Subject7Monday")
        self.Subject7Monday.setFont(font5)
        self.Subject7Monday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject7Monday.setTristate(False)

        self.verticalLayout_10.addWidget(self.Subject7Monday)

        self.Subject7Tuesday = QCheckBox(self.SubjectDays_7)
        self.Subject7Tuesday.setObjectName(u"Subject7Tuesday")
        self.Subject7Tuesday.setFont(font5)
        self.Subject7Tuesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject7Tuesday.setTristate(False)

        self.verticalLayout_10.addWidget(self.Subject7Tuesday)

        self.Subject7Wednesday = QCheckBox(self.SubjectDays_7)
        self.Subject7Wednesday.setObjectName(u"Subject7Wednesday")
        self.Subject7Wednesday.setFont(font5)
        self.Subject7Wednesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject7Wednesday.setTristate(False)

        self.verticalLayout_10.addWidget(self.Subject7Wednesday)

        self.Subject7Thursday = QCheckBox(self.SubjectDays_7)
        self.Subject7Thursday.setObjectName(u"Subject7Thursday")
        self.Subject7Thursday.setFont(font5)
        self.Subject7Thursday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject7Thursday.setTristate(False)

        self.verticalLayout_10.addWidget(self.Subject7Thursday)

        self.Subject7Friday = QCheckBox(self.SubjectDays_7)
        self.Subject7Friday.setObjectName(u"Subject7Friday")
        self.Subject7Friday.setFont(font5)
        self.Subject7Friday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject7Friday.setTristate(False)

        self.verticalLayout_10.addWidget(self.Subject7Friday)

        self.Subject7Saturday = QCheckBox(self.SubjectDays_7)
        self.Subject7Saturday.setObjectName(u"Subject7Saturday")
        self.Subject7Saturday.setFont(font5)
        self.Subject7Saturday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject7Saturday.setTristate(False)

        self.verticalLayout_10.addWidget(self.Subject7Saturday)


        self.horizontalLayout_10.addWidget(self.SubjectDays_7)

        self.stackedWidget.addWidget(self.Day7)
        self.Day6 = QWidget()
        self.Day6.setObjectName(u"Day6")
        self.Day6.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.horizontalLayout_11 = QHBoxLayout(self.Day6)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.SubjectDays_6 = QFrame(self.Day6)
        self.SubjectDays_6.setObjectName(u"SubjectDays_6")
        self.SubjectDays_6.setFrameShape(QFrame.StyledPanel)
        self.SubjectDays_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.SubjectDays_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.Subject6DaysHeading = QLabel(self.SubjectDays_6)
        self.Subject6DaysHeading.setObjectName(u"Subject6DaysHeading")
        self.Subject6DaysHeading.setMaximumSize(QSize(16777215, 100))
        self.Subject6DaysHeading.setFont(font6)
        self.Subject6DaysHeading.setStyleSheet(u"QLabel{\n"
"	\n"
"color: rgb(241, 44, 172);\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(150, 255, 69,200);\n"
"border-radius:50px;\n"
"\n"
"}")
        self.Subject6DaysHeading.setMidLineWidth(4)
        self.Subject6DaysHeading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.Subject6DaysHeading)

        self.Subject6Sunday = QCheckBox(self.SubjectDays_6)
        self.Subject6Sunday.setObjectName(u"Subject6Sunday")
        self.Subject6Sunday.setFont(font5)
        self.Subject6Sunday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject6Sunday.setTristate(False)

        self.verticalLayout_9.addWidget(self.Subject6Sunday)

        self.Subject6Monday = QCheckBox(self.SubjectDays_6)
        self.Subject6Monday.setObjectName(u"Subject6Monday")
        self.Subject6Monday.setFont(font5)
        self.Subject6Monday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject6Monday.setTristate(False)

        self.verticalLayout_9.addWidget(self.Subject6Monday)

        self.Subject6Tuesday = QCheckBox(self.SubjectDays_6)
        self.Subject6Tuesday.setObjectName(u"Subject6Tuesday")
        self.Subject6Tuesday.setFont(font5)
        self.Subject6Tuesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject6Tuesday.setTristate(False)

        self.verticalLayout_9.addWidget(self.Subject6Tuesday)

        self.Subject6Wednesday = QCheckBox(self.SubjectDays_6)
        self.Subject6Wednesday.setObjectName(u"Subject6Wednesday")
        self.Subject6Wednesday.setFont(font5)
        self.Subject6Wednesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject6Wednesday.setTristate(False)

        self.verticalLayout_9.addWidget(self.Subject6Wednesday)

        self.Subject6Thursday = QCheckBox(self.SubjectDays_6)
        self.Subject6Thursday.setObjectName(u"Subject6Thursday")
        self.Subject6Thursday.setFont(font5)
        self.Subject6Thursday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject6Thursday.setTristate(False)

        self.verticalLayout_9.addWidget(self.Subject6Thursday)

        self.Subject6Friday = QCheckBox(self.SubjectDays_6)
        self.Subject6Friday.setObjectName(u"Subject6Friday")
        self.Subject6Friday.setFont(font5)
        self.Subject6Friday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject6Friday.setTristate(False)

        self.verticalLayout_9.addWidget(self.Subject6Friday)

        self.Subject6Saturday = QCheckBox(self.SubjectDays_6)
        self.Subject6Saturday.setObjectName(u"Subject6Saturday")
        self.Subject6Saturday.setFont(font5)
        self.Subject6Saturday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject6Saturday.setTristate(False)

        self.verticalLayout_9.addWidget(self.Subject6Saturday)


        self.horizontalLayout_11.addWidget(self.SubjectDays_6)

        self.stackedWidget.addWidget(self.Day6)
        self.Day5 = QWidget()
        self.Day5.setObjectName(u"Day5")
        self.Day5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.horizontalLayout_12 = QHBoxLayout(self.Day5)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.SubjectDays_5 = QFrame(self.Day5)
        self.SubjectDays_5.setObjectName(u"SubjectDays_5")
        self.SubjectDays_5.setFrameShape(QFrame.StyledPanel)
        self.SubjectDays_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.SubjectDays_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Subject5DaysHeading = QLabel(self.SubjectDays_5)
        self.Subject5DaysHeading.setObjectName(u"Subject5DaysHeading")
        self.Subject5DaysHeading.setMaximumSize(QSize(16777215, 100))
        self.Subject5DaysHeading.setFont(font6)
        self.Subject5DaysHeading.setStyleSheet(u"QLabel{\n"
"	\n"
"color: rgb(241, 44, 172);\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(150, 255, 69,200);\n"
"border-radius:50px;\n"
"\n"
"}")
        self.Subject5DaysHeading.setMidLineWidth(4)
        self.Subject5DaysHeading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.Subject5DaysHeading)

        self.Subject5Sunday = QCheckBox(self.SubjectDays_5)
        self.Subject5Sunday.setObjectName(u"Subject5Sunday")
        self.Subject5Sunday.setFont(font5)
        self.Subject5Sunday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject5Sunday.setTristate(False)

        self.verticalLayout_8.addWidget(self.Subject5Sunday)

        self.Subject5Monday = QCheckBox(self.SubjectDays_5)
        self.Subject5Monday.setObjectName(u"Subject5Monday")
        self.Subject5Monday.setFont(font5)
        self.Subject5Monday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject5Monday.setTristate(False)

        self.verticalLayout_8.addWidget(self.Subject5Monday)

        self.Subjcet5Tuesday = QCheckBox(self.SubjectDays_5)
        self.Subjcet5Tuesday.setObjectName(u"Subjcet5Tuesday")
        self.Subjcet5Tuesday.setFont(font5)
        self.Subjcet5Tuesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subjcet5Tuesday.setTristate(False)

        self.verticalLayout_8.addWidget(self.Subjcet5Tuesday)

        self.Subject5Wednesday = QCheckBox(self.SubjectDays_5)
        self.Subject5Wednesday.setObjectName(u"Subject5Wednesday")
        self.Subject5Wednesday.setFont(font5)
        self.Subject5Wednesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject5Wednesday.setTristate(False)

        self.verticalLayout_8.addWidget(self.Subject5Wednesday)

        self.Subject5Thursday = QCheckBox(self.SubjectDays_5)
        self.Subject5Thursday.setObjectName(u"Subject5Thursday")
        self.Subject5Thursday.setFont(font5)
        self.Subject5Thursday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject5Thursday.setTristate(False)

        self.verticalLayout_8.addWidget(self.Subject5Thursday)

        self.Subject5Friday = QCheckBox(self.SubjectDays_5)
        self.Subject5Friday.setObjectName(u"Subject5Friday")
        self.Subject5Friday.setFont(font5)
        self.Subject5Friday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject5Friday.setTristate(False)

        self.verticalLayout_8.addWidget(self.Subject5Friday)

        self.Subject5Saturday = QCheckBox(self.SubjectDays_5)
        self.Subject5Saturday.setObjectName(u"Subject5Saturday")
        self.Subject5Saturday.setFont(font5)
        self.Subject5Saturday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject5Saturday.setTristate(False)

        self.verticalLayout_8.addWidget(self.Subject5Saturday)


        self.horizontalLayout_12.addWidget(self.SubjectDays_5)

        self.stackedWidget.addWidget(self.Day5)
        self.Day4 = QWidget()
        self.Day4.setObjectName(u"Day4")
        self.Day4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.horizontalLayout_13 = QHBoxLayout(self.Day4)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.SubjectDays_4 = QFrame(self.Day4)
        self.SubjectDays_4.setObjectName(u"SubjectDays_4")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.SubjectDays_4.sizePolicy().hasHeightForWidth())
        self.SubjectDays_4.setSizePolicy(sizePolicy9)
        self.SubjectDays_4.setFrameShape(QFrame.StyledPanel)
        self.SubjectDays_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.SubjectDays_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Subject4DaysHeading = QLabel(self.SubjectDays_4)
        self.Subject4DaysHeading.setObjectName(u"Subject4DaysHeading")
        self.Subject4DaysHeading.setMaximumSize(QSize(16777215, 100))
        self.Subject4DaysHeading.setFont(font6)
        self.Subject4DaysHeading.setStyleSheet(u"QLabel{\n"
"	\n"
"color: rgb(241, 44, 172);\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(150, 255, 69,200);\n"
"border-radius:50px;\n"
"\n"
"}")
        self.Subject4DaysHeading.setMidLineWidth(4)
        self.Subject4DaysHeading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.Subject4DaysHeading)

        self.Subject4Sunday = QCheckBox(self.SubjectDays_4)
        self.Subject4Sunday.setObjectName(u"Subject4Sunday")
        self.Subject4Sunday.setFont(font5)
        self.Subject4Sunday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject4Sunday.setTristate(False)

        self.verticalLayout_7.addWidget(self.Subject4Sunday)

        self.Subject4Monday = QCheckBox(self.SubjectDays_4)
        self.Subject4Monday.setObjectName(u"Subject4Monday")
        self.Subject4Monday.setFont(font5)
        self.Subject4Monday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject4Monday.setTristate(False)

        self.verticalLayout_7.addWidget(self.Subject4Monday)

        self.Subject4Tuesday = QCheckBox(self.SubjectDays_4)
        self.Subject4Tuesday.setObjectName(u"Subject4Tuesday")
        self.Subject4Tuesday.setFont(font5)
        self.Subject4Tuesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject4Tuesday.setTristate(False)

        self.verticalLayout_7.addWidget(self.Subject4Tuesday)

        self.Subject4Wednesday = QCheckBox(self.SubjectDays_4)
        self.Subject4Wednesday.setObjectName(u"Subject4Wednesday")
        self.Subject4Wednesday.setFont(font5)
        self.Subject4Wednesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject4Wednesday.setTristate(False)

        self.verticalLayout_7.addWidget(self.Subject4Wednesday)

        self.Subject4Thursday = QCheckBox(self.SubjectDays_4)
        self.Subject4Thursday.setObjectName(u"Subject4Thursday")
        self.Subject4Thursday.setFont(font5)
        self.Subject4Thursday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject4Thursday.setTristate(False)

        self.verticalLayout_7.addWidget(self.Subject4Thursday)

        self.Subject4Friday = QCheckBox(self.SubjectDays_4)
        self.Subject4Friday.setObjectName(u"Subject4Friday")
        self.Subject4Friday.setFont(font5)
        self.Subject4Friday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject4Friday.setTristate(False)

        self.verticalLayout_7.addWidget(self.Subject4Friday)

        self.Subject4Saturday = QCheckBox(self.SubjectDays_4)
        self.Subject4Saturday.setObjectName(u"Subject4Saturday")
        self.Subject4Saturday.setFont(font5)
        self.Subject4Saturday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject4Saturday.setTristate(False)

        self.verticalLayout_7.addWidget(self.Subject4Saturday)


        self.horizontalLayout_13.addWidget(self.SubjectDays_4)

        self.stackedWidget.addWidget(self.Day4)
        self.Day3 = QWidget()
        self.Day3.setObjectName(u"Day3")
        self.Day3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.horizontalLayout_14 = QHBoxLayout(self.Day3)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.SubjectDays_3 = QFrame(self.Day3)
        self.SubjectDays_3.setObjectName(u"SubjectDays_3")
        self.SubjectDays_3.setFrameShape(QFrame.StyledPanel)
        self.SubjectDays_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.SubjectDays_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Subject3DaysHeading = QLabel(self.SubjectDays_3)
        self.Subject3DaysHeading.setObjectName(u"Subject3DaysHeading")
        self.Subject3DaysHeading.setMaximumSize(QSize(16777215, 100))
        self.Subject3DaysHeading.setFont(font6)
        self.Subject3DaysHeading.setStyleSheet(u"QLabel{\n"
"	\n"
"color: rgb(241, 44, 172);\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(150, 255, 69,200);\n"
"border-radius:50px;\n"
"\n"
"}")
        self.Subject3DaysHeading.setMidLineWidth(4)
        self.Subject3DaysHeading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.Subject3DaysHeading)

        self.Subject3Sunday = QCheckBox(self.SubjectDays_3)
        self.Subject3Sunday.setObjectName(u"Subject3Sunday")
        self.Subject3Sunday.setFont(font5)
        self.Subject3Sunday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject3Sunday.setTristate(False)

        self.verticalLayout_6.addWidget(self.Subject3Sunday)

        self.Subject3Monday = QCheckBox(self.SubjectDays_3)
        self.Subject3Monday.setObjectName(u"Subject3Monday")
        self.Subject3Monday.setFont(font5)
        self.Subject3Monday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject3Monday.setTristate(False)

        self.verticalLayout_6.addWidget(self.Subject3Monday)

        self.Subject3Tuesday = QCheckBox(self.SubjectDays_3)
        self.Subject3Tuesday.setObjectName(u"Subject3Tuesday")
        self.Subject3Tuesday.setFont(font5)
        self.Subject3Tuesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject3Tuesday.setTristate(False)

        self.verticalLayout_6.addWidget(self.Subject3Tuesday)

        self.Subject3Wednesday = QCheckBox(self.SubjectDays_3)
        self.Subject3Wednesday.setObjectName(u"Subject3Wednesday")
        self.Subject3Wednesday.setFont(font5)
        self.Subject3Wednesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject3Wednesday.setTristate(False)

        self.verticalLayout_6.addWidget(self.Subject3Wednesday)

        self.Subject3Thursday = QCheckBox(self.SubjectDays_3)
        self.Subject3Thursday.setObjectName(u"Subject3Thursday")
        self.Subject3Thursday.setFont(font5)
        self.Subject3Thursday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject3Thursday.setTristate(False)

        self.verticalLayout_6.addWidget(self.Subject3Thursday)

        self.Subject3Friday = QCheckBox(self.SubjectDays_3)
        self.Subject3Friday.setObjectName(u"Subject3Friday")
        self.Subject3Friday.setFont(font5)
        self.Subject3Friday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject3Friday.setTristate(False)

        self.verticalLayout_6.addWidget(self.Subject3Friday)

        self.Subject3Saturday = QCheckBox(self.SubjectDays_3)
        self.Subject3Saturday.setObjectName(u"Subject3Saturday")
        self.Subject3Saturday.setFont(font5)
        self.Subject3Saturday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject3Saturday.setTristate(False)

        self.verticalLayout_6.addWidget(self.Subject3Saturday)


        self.horizontalLayout_14.addWidget(self.SubjectDays_3)

        self.stackedWidget.addWidget(self.Day3)
        self.Day2 = QWidget()
        self.Day2.setObjectName(u"Day2")
        self.Day2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.horizontalLayout_15 = QHBoxLayout(self.Day2)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.SubjectDays_2 = QFrame(self.Day2)
        self.SubjectDays_2.setObjectName(u"SubjectDays_2")
        self.SubjectDays_2.setFrameShape(QFrame.StyledPanel)
        self.SubjectDays_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.SubjectDays_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Subject2DaysHeading = QLabel(self.SubjectDays_2)
        self.Subject2DaysHeading.setObjectName(u"Subject2DaysHeading")
        self.Subject2DaysHeading.setMaximumSize(QSize(16777215, 100))
        self.Subject2DaysHeading.setFont(font6)
        self.Subject2DaysHeading.setStyleSheet(u"QLabel{\n"
"	\n"
"color: rgb(241, 44, 172);\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(150, 255, 69,200);\n"
"border-radius:50px;\n"
"\n"
"}")
        self.Subject2DaysHeading.setMidLineWidth(4)
        self.Subject2DaysHeading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.Subject2DaysHeading)

        self.Subject2Sunday = QCheckBox(self.SubjectDays_2)
        self.Subject2Sunday.setObjectName(u"Subject2Sunday")
        self.Subject2Sunday.setFont(font5)
        self.Subject2Sunday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject2Sunday.setTristate(False)

        self.verticalLayout_5.addWidget(self.Subject2Sunday)

        self.Subject2Monday = QCheckBox(self.SubjectDays_2)
        self.Subject2Monday.setObjectName(u"Subject2Monday")
        self.Subject2Monday.setFont(font5)
        self.Subject2Monday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject2Monday.setTristate(False)

        self.verticalLayout_5.addWidget(self.Subject2Monday)

        self.Subject2Tuesday = QCheckBox(self.SubjectDays_2)
        self.Subject2Tuesday.setObjectName(u"Subject2Tuesday")
        self.Subject2Tuesday.setFont(font5)
        self.Subject2Tuesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject2Tuesday.setTristate(False)

        self.verticalLayout_5.addWidget(self.Subject2Tuesday)

        self.Subject2Wednesday = QCheckBox(self.SubjectDays_2)
        self.Subject2Wednesday.setObjectName(u"Subject2Wednesday")
        self.Subject2Wednesday.setFont(font5)
        self.Subject2Wednesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject2Wednesday.setTristate(False)

        self.verticalLayout_5.addWidget(self.Subject2Wednesday)

        self.Subject2Thursday = QCheckBox(self.SubjectDays_2)
        self.Subject2Thursday.setObjectName(u"Subject2Thursday")
        self.Subject2Thursday.setFont(font5)
        self.Subject2Thursday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject2Thursday.setTristate(False)

        self.verticalLayout_5.addWidget(self.Subject2Thursday)

        self.Subject2Friday = QCheckBox(self.SubjectDays_2)
        self.Subject2Friday.setObjectName(u"Subject2Friday")
        self.Subject2Friday.setFont(font5)
        self.Subject2Friday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject2Friday.setTristate(False)

        self.verticalLayout_5.addWidget(self.Subject2Friday)

        self.Subject2Saturday = QCheckBox(self.SubjectDays_2)
        self.Subject2Saturday.setObjectName(u"Subject2Saturday")
        self.Subject2Saturday.setFont(font5)
        self.Subject2Saturday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject2Saturday.setTristate(False)

        self.verticalLayout_5.addWidget(self.Subject2Saturday)


        self.horizontalLayout_15.addWidget(self.SubjectDays_2)

        self.stackedWidget.addWidget(self.Day2)
        self.Day1 = QWidget()
        self.Day1.setObjectName(u"Day1")
        self.Day1.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.horizontalLayout_16 = QHBoxLayout(self.Day1)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.SubjectDays = QFrame(self.Day1)
        self.SubjectDays.setObjectName(u"SubjectDays")
        self.SubjectDays.setFrameShape(QFrame.StyledPanel)
        self.SubjectDays.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.SubjectDays)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Subject1DaysHeading = QLabel(self.SubjectDays)
        self.Subject1DaysHeading.setObjectName(u"Subject1DaysHeading")
        self.Subject1DaysHeading.setMaximumSize(QSize(16777215, 100))
        self.Subject1DaysHeading.setFont(font6)
        self.Subject1DaysHeading.setStyleSheet(u"QLabel{\n"
"	\n"
"color: rgb(241, 44, 172);\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(150, 255, 69,200);\n"
"border-radius:50px;\n"
"\n"
"}")
        self.Subject1DaysHeading.setMidLineWidth(4)
        self.Subject1DaysHeading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Subject1DaysHeading)

        self.Subject1Sunday = QCheckBox(self.SubjectDays)
        self.Subject1Sunday.setObjectName(u"Subject1Sunday")
        self.Subject1Sunday.setFont(font5)
        self.Subject1Sunday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject1Sunday.setTristate(False)

        self.verticalLayout_2.addWidget(self.Subject1Sunday)

        self.Subject1Monday = QCheckBox(self.SubjectDays)
        self.Subject1Monday.setObjectName(u"Subject1Monday")
        self.Subject1Monday.setFont(font5)
        self.Subject1Monday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject1Monday.setTristate(False)

        self.verticalLayout_2.addWidget(self.Subject1Monday)

        self.Subject1Tuesday = QCheckBox(self.SubjectDays)
        self.Subject1Tuesday.setObjectName(u"Subject1Tuesday")
        self.Subject1Tuesday.setFont(font5)
        self.Subject1Tuesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject1Tuesday.setTristate(False)

        self.verticalLayout_2.addWidget(self.Subject1Tuesday)

        self.Subject1Wednesday = QCheckBox(self.SubjectDays)
        self.Subject1Wednesday.setObjectName(u"Subject1Wednesday")
        self.Subject1Wednesday.setFont(font5)
        self.Subject1Wednesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject1Wednesday.setTristate(False)

        self.verticalLayout_2.addWidget(self.Subject1Wednesday)

        self.Subject1Thursday = QCheckBox(self.SubjectDays)
        self.Subject1Thursday.setObjectName(u"Subject1Thursday")
        self.Subject1Thursday.setFont(font5)
        self.Subject1Thursday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject1Thursday.setTristate(False)

        self.verticalLayout_2.addWidget(self.Subject1Thursday)

        self.Subject1Friday = QCheckBox(self.SubjectDays)
        self.Subject1Friday.setObjectName(u"Subject1Friday")
        self.Subject1Friday.setFont(font5)
        self.Subject1Friday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject1Friday.setTristate(False)

        self.verticalLayout_2.addWidget(self.Subject1Friday)

        self.Subject1Saturday = QCheckBox(self.SubjectDays)
        self.Subject1Saturday.setObjectName(u"Subject1Saturday")
        self.Subject1Saturday.setFont(font5)
        self.Subject1Saturday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject1Saturday.setTristate(False)

        self.verticalLayout_2.addWidget(self.Subject1Saturday)


        self.horizontalLayout_16.addWidget(self.SubjectDays)

        self.stackedWidget.addWidget(self.Day1)

        self.gridLayout_5.addWidget(self.stackedWidget, 1, 3, 1, 1)

        self.frame_5 = QFrame(self.SubContent)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(171, 0))
        self.frame_5.setMaximumSize(QSize(122, 16777215))
        self.frame_5.setStyleSheet(u"border-image:None;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, 4)
        self.Subject_1 = QLineEdit(self.frame_5)
        self.Subject_1.setObjectName(u"Subject_1")
        sizePolicy8.setHeightForWidth(self.Subject_1.sizePolicy().hasHeightForWidth())
        self.Subject_1.setSizePolicy(sizePolicy8)
        self.Subject_1.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setFamily(u"Segoe UI Semibold")
        font7.setPointSize(11)
        self.Subject_1.setFont(font7)
        self.Subject_1.setStyleSheet(u"QLineEdit{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 129, 23, 255), stop:1 rgba(239, 239, 37, 255));\n"
"}")
        self.Subject_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Subject_1, 0, 0, 1, 1)

        self.Subject_2 = QLineEdit(self.frame_5)
        self.Subject_2.setObjectName(u"Subject_2")
        sizePolicy8.setHeightForWidth(self.Subject_2.sizePolicy().hasHeightForWidth())
        self.Subject_2.setSizePolicy(sizePolicy8)
        self.Subject_2.setFont(font7)
        self.Subject_2.setStyleSheet(u"QLineEdit{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 129, 23, 255), stop:1 rgba(239, 239, 37, 255));\n"
"}")
        self.Subject_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Subject_2, 1, 0, 1, 1)

        self.Subject_3 = QLineEdit(self.frame_5)
        self.Subject_3.setObjectName(u"Subject_3")
        sizePolicy8.setHeightForWidth(self.Subject_3.sizePolicy().hasHeightForWidth())
        self.Subject_3.setSizePolicy(sizePolicy8)
        self.Subject_3.setFont(font7)
        self.Subject_3.setStyleSheet(u"QLineEdit{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 129, 23, 255), stop:1 rgba(239, 239, 37, 255));\n"
"}")
        self.Subject_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Subject_3, 2, 0, 1, 1)

        self.Subject_4 = QLineEdit(self.frame_5)
        self.Subject_4.setObjectName(u"Subject_4")
        sizePolicy8.setHeightForWidth(self.Subject_4.sizePolicy().hasHeightForWidth())
        self.Subject_4.setSizePolicy(sizePolicy8)
        self.Subject_4.setFont(font7)
        self.Subject_4.setStyleSheet(u"QLineEdit{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 129, 23, 255), stop:1 rgba(239, 239, 37, 255));\n"
"}")
        self.Subject_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Subject_4, 3, 0, 1, 1)

        self.Subject_5 = QLineEdit(self.frame_5)
        self.Subject_5.setObjectName(u"Subject_5")
        sizePolicy8.setHeightForWidth(self.Subject_5.sizePolicy().hasHeightForWidth())
        self.Subject_5.setSizePolicy(sizePolicy8)
        self.Subject_5.setFont(font7)
        self.Subject_5.setStyleSheet(u"QLineEdit{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 129, 23, 255), stop:1 rgba(239, 239, 37, 255));\n"
"}")
        self.Subject_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Subject_5, 4, 0, 1, 1)

        self.Subject_6 = QLineEdit(self.frame_5)
        self.Subject_6.setObjectName(u"Subject_6")
        sizePolicy8.setHeightForWidth(self.Subject_6.sizePolicy().hasHeightForWidth())
        self.Subject_6.setSizePolicy(sizePolicy8)
        self.Subject_6.setFont(font7)
        self.Subject_6.setStyleSheet(u"QLineEdit{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 129, 23, 255), stop:1 rgba(239, 239, 37, 255));\n"
"}")
        self.Subject_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Subject_6, 5, 0, 1, 1)

        self.Subject_7 = QLineEdit(self.frame_5)
        self.Subject_7.setObjectName(u"Subject_7")
        sizePolicy8.setHeightForWidth(self.Subject_7.sizePolicy().hasHeightForWidth())
        self.Subject_7.setSizePolicy(sizePolicy8)
        self.Subject_7.setFont(font7)
        self.Subject_7.setStyleSheet(u"QLineEdit{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 129, 23, 255), stop:1 rgba(239, 239, 37, 255));\n"
"}")
        self.Subject_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Subject_7, 6, 0, 1, 1)

        self.Subject_8 = QLineEdit(self.frame_5)
        self.Subject_8.setObjectName(u"Subject_8")
        sizePolicy8.setHeightForWidth(self.Subject_8.sizePolicy().hasHeightForWidth())
        self.Subject_8.setSizePolicy(sizePolicy8)
        self.Subject_8.setFont(font7)
        self.Subject_8.setStyleSheet(u"QLineEdit{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 129, 23, 255), stop:1 rgba(239, 239, 37, 255));\n"
"}")
        self.Subject_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Subject_8, 7, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_5, 1, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.SubContent)


        self.gridLayout.addWidget(self.Content, 2, 0, 1, 1)

        self.TitleBar_2 = QFrame(self.frame)
        self.TitleBar_2.setObjectName(u"TitleBar_2")
        sizePolicy5.setHeightForWidth(self.TitleBar_2.sizePolicy().hasHeightForWidth())
        self.TitleBar_2.setSizePolicy(sizePolicy5)
        self.TitleBar_2.setMinimumSize(QSize(0, 0))
        self.TitleBar_2.setMaximumSize(QSize(16777215, 30))
        self.TitleBar_2.setStyleSheet(u"QFrame{\n"
"	background-color: qlineargradient(spread:pad, x1:0.383085, y1:0.352, x2:0.587065, y2:0.534, stop:0 rgba(0, 0, 0, 82), stop:0.970149 rgba(0, 0, 0, 76), stop:1 rgba(0, 0, 0, 76));\n"
"border-image:None;\n"
"}")
        self.TitleBar_2.setFrameShape(QFrame.StyledPanel)
        self.TitleBar_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.TitleBar_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.TitleBar_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border-image:None;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.TitleBar = QFrame(self.frame_2)
        self.TitleBar.setObjectName(u"TitleBar")
        self.TitleBar.setCursor(QCursor(Qt.SizeAllCursor))
        self.TitleBar.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.TitleBar.setFrameShape(QFrame.StyledPanel)
        self.TitleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.TitleBar)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 500, 0)
        self.AppTitle = QLabel(self.TitleBar)
        self.AppTitle.setObjectName(u"AppTitle")
        self.AppTitle.setMinimumSize(QSize(60, 0))
        font8 = QFont()
        font8.setPointSize(11)
        font8.setBold(True)
        font8.setWeight(75)
        self.AppTitle.setFont(font8)
        self.AppTitle.setStyleSheet(u"QLabel{\n"
"	color: rgba(255, 229, 84, 180);\n"
"border-radius:3px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.38, x2:1, y2:0.670636, stop:0 rgba(0, 0, 0, 59), stop:1 rgba(13, 13, 13, 11));\n"
"}")
        self.AppTitle.setTextFormat(Qt.RichText)
        self.AppTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.AppTitle)

        self.GoBackButton = QPushButton(self.TitleBar)
        self.GoBackButton.setObjectName(u"GoBackButton")
        sizePolicy10 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.GoBackButton.sizePolicy().hasHeightForWidth())
        self.GoBackButton.setSizePolicy(sizePolicy10)
        self.GoBackButton.setMinimumSize(QSize(101, 24))
        self.GoBackButton.setMaximumSize(QSize(80, 16777215))
        font9 = QFont()
        font9.setPointSize(10)
        font9.setBold(False)
        font9.setWeight(50)
        self.GoBackButton.setFont(font9)
        self.GoBackButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.GoBackButton.setStyleSheet(u"QPushButton{\n"
"border-radius:7px;\n"
"	background-color: rgba(255, 170, 0, 190);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 0);\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.GoBackButton)


        self.horizontalLayout_17.addWidget(self.TitleBar)

        self.NextButton = QPushButton(self.frame_2)
        self.NextButton.setObjectName(u"NextButton")
        sizePolicy10.setHeightForWidth(self.NextButton.sizePolicy().hasHeightForWidth())
        self.NextButton.setSizePolicy(sizePolicy10)
        self.NextButton.setMinimumSize(QSize(80, 24))
        self.NextButton.setMaximumSize(QSize(80, 16777215))
        self.NextButton.setFont(font5)
        self.NextButton.setStyleSheet(u"QPushButton{\n"
"border-radius:7px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.653, x2:1, y2:0.631, stop:0 rgba(255, 0, 255, 255), stop:1 rgba(166, 43, 200, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 0);\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout_17.addWidget(self.NextButton)


        self.horizontalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.TitleBar_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy10.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy10)
        self.frame_3.setMinimumSize(QSize(0, 25))
        self.frame_3.setMaximumSize(QSize(100, 16777215))
        self.frame_3.setStyleSheet(u"border-image:None;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 0, 0, 0)
        self.Minimizebtn = QPushButton(self.frame_3)
        self.Minimizebtn.setObjectName(u"Minimizebtn")
        sizePolicy10.setHeightForWidth(self.Minimizebtn.sizePolicy().hasHeightForWidth())
        self.Minimizebtn.setSizePolicy(sizePolicy10)
        self.Minimizebtn.setMaximumSize(QSize(15, 15))
        self.Minimizebtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 0);\n"
"border-radius:7px;\n"
"	border-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.Minimizebtn)

        self.Maximizebtn = QPushButton(self.frame_3)
        self.Maximizebtn.setObjectName(u"Maximizebtn")
        sizePolicy10.setHeightForWidth(self.Maximizebtn.sizePolicy().hasHeightForWidth())
        self.Maximizebtn.setSizePolicy(sizePolicy10)
        self.Maximizebtn.setMaximumSize(QSize(15, 15))
        self.Maximizebtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 150, 0);\n"
"border-radius:7px;\n"
"	background-color: rgb(124, 218, 0);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(85, 170, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.Maximizebtn)

        self.CloseButton = QPushButton(self.frame_3)
        self.CloseButton.setObjectName(u"CloseButton")
        sizePolicy10.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy10)
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


        self.gridLayout.addWidget(self.TitleBar_2, 0, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)


        self.horizontalLayout.addWidget(self.frame)

        MainPage.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.Subject_1, self.Subject_Link_1)
        QWidget.setTabOrder(self.Subject_Link_1, self.Subject_1From)
        QWidget.setTabOrder(self.Subject_1From, self.Subject_1To)
        QWidget.setTabOrder(self.Subject_1To, self.SubjectsDaysBtn)
        QWidget.setTabOrder(self.SubjectsDaysBtn, self.Subject_2)
        QWidget.setTabOrder(self.Subject_2, self.Subject_Link_2)
        QWidget.setTabOrder(self.Subject_Link_2, self.Subject_2From)
        QWidget.setTabOrder(self.Subject_2From, self.Subject_2To)
        QWidget.setTabOrder(self.Subject_2To, self.SubjectsDaysBtn_2)
        QWidget.setTabOrder(self.SubjectsDaysBtn_2, self.Subject_3)
        QWidget.setTabOrder(self.Subject_3, self.Subject_Link_3)
        QWidget.setTabOrder(self.Subject_Link_3, self.Subject_3From)
        QWidget.setTabOrder(self.Subject_3From, self.Subject_3To)
        QWidget.setTabOrder(self.Subject_3To, self.SubjectsDaysBtn_3)
        QWidget.setTabOrder(self.SubjectsDaysBtn_3, self.Subject_4)
        QWidget.setTabOrder(self.Subject_4, self.Subject_Link_4)
        QWidget.setTabOrder(self.Subject_Link_4, self.Subject_4From)
        QWidget.setTabOrder(self.Subject_4From, self.Subject_4To)
        QWidget.setTabOrder(self.Subject_4To, self.SubjectsDaysBtn_4)
        QWidget.setTabOrder(self.SubjectsDaysBtn_4, self.Subject_5)
        QWidget.setTabOrder(self.Subject_5, self.Subject_Link_5)
        QWidget.setTabOrder(self.Subject_Link_5, self.Subject_5From)
        QWidget.setTabOrder(self.Subject_5From, self.Subject_5To)
        QWidget.setTabOrder(self.Subject_5To, self.SubjectsDaysBtn_5)
        QWidget.setTabOrder(self.SubjectsDaysBtn_5, self.Subject_6)
        QWidget.setTabOrder(self.Subject_6, self.Subject_Link_6)
        QWidget.setTabOrder(self.Subject_Link_6, self.Subject_6From)
        QWidget.setTabOrder(self.Subject_6From, self.Subject_6To)
        QWidget.setTabOrder(self.Subject_6To, self.SubjectsDaysBtn_6)
        QWidget.setTabOrder(self.SubjectsDaysBtn_6, self.Subject_7)
        QWidget.setTabOrder(self.Subject_7, self.Subject_Link_7)
        QWidget.setTabOrder(self.Subject_Link_7, self.Subject_7From)
        QWidget.setTabOrder(self.Subject_7From, self.Subject_7To)
        QWidget.setTabOrder(self.Subject_7To, self.SubjectsDaysBtn_7)
        QWidget.setTabOrder(self.SubjectsDaysBtn_7, self.Subject_8)
        QWidget.setTabOrder(self.Subject_8, self.Subject_Link_8)
        QWidget.setTabOrder(self.Subject_Link_8, self.Subject_8From)
        QWidget.setTabOrder(self.Subject_8From, self.Subject_8To_2)
        QWidget.setTabOrder(self.Subject_8To_2, self.SubjectsDaysBtn_8)
        QWidget.setTabOrder(self.SubjectsDaysBtn_8, self.Minimizebtn)
        QWidget.setTabOrder(self.Minimizebtn, self.CloseButton)
        QWidget.setTabOrder(self.CloseButton, self.Maximizebtn)
        QWidget.setTabOrder(self.Maximizebtn, self.Subject8Sunday)
        QWidget.setTabOrder(self.Subject8Sunday, self.Subject8Monday)
        QWidget.setTabOrder(self.Subject8Monday, self.Subject8Tuesday)
        QWidget.setTabOrder(self.Subject8Tuesday, self.Subject8Wednesday)
        QWidget.setTabOrder(self.Subject8Wednesday, self.Subject8Thursday)
        QWidget.setTabOrder(self.Subject8Thursday, self.Subject8Friday)
        QWidget.setTabOrder(self.Subject8Friday, self.Subject8Saturday)
        QWidget.setTabOrder(self.Subject8Saturday, self.Subject7Sunday)
        QWidget.setTabOrder(self.Subject7Sunday, self.Subject7Monday)
        QWidget.setTabOrder(self.Subject7Monday, self.Subject7Tuesday)
        QWidget.setTabOrder(self.Subject7Tuesday, self.Subject7Wednesday)
        QWidget.setTabOrder(self.Subject7Wednesday, self.Subject7Thursday)
        QWidget.setTabOrder(self.Subject7Thursday, self.Subject7Friday)
        QWidget.setTabOrder(self.Subject7Friday, self.Subject7Saturday)
        QWidget.setTabOrder(self.Subject7Saturday, self.Subject6Sunday)
        QWidget.setTabOrder(self.Subject6Sunday, self.Subject6Monday)
        QWidget.setTabOrder(self.Subject6Monday, self.Subject6Tuesday)
        QWidget.setTabOrder(self.Subject6Tuesday, self.Subject6Wednesday)
        QWidget.setTabOrder(self.Subject6Wednesday, self.Subject6Thursday)
        QWidget.setTabOrder(self.Subject6Thursday, self.Subject6Friday)
        QWidget.setTabOrder(self.Subject6Friday, self.Subject6Saturday)
        QWidget.setTabOrder(self.Subject6Saturday, self.Subject5Sunday)
        QWidget.setTabOrder(self.Subject5Sunday, self.Subject5Monday)
        QWidget.setTabOrder(self.Subject5Monday, self.Subjcet5Tuesday)
        QWidget.setTabOrder(self.Subjcet5Tuesday, self.Subject5Wednesday)
        QWidget.setTabOrder(self.Subject5Wednesday, self.Subject5Thursday)
        QWidget.setTabOrder(self.Subject5Thursday, self.Subject5Friday)
        QWidget.setTabOrder(self.Subject5Friday, self.Subject5Saturday)
        QWidget.setTabOrder(self.Subject5Saturday, self.Subject4Sunday)
        QWidget.setTabOrder(self.Subject4Sunday, self.Subject4Monday)
        QWidget.setTabOrder(self.Subject4Monday, self.Subject4Tuesday)
        QWidget.setTabOrder(self.Subject4Tuesday, self.Subject4Wednesday)
        QWidget.setTabOrder(self.Subject4Wednesday, self.Subject4Thursday)
        QWidget.setTabOrder(self.Subject4Thursday, self.Subject4Friday)
        QWidget.setTabOrder(self.Subject4Friday, self.Subject4Saturday)
        QWidget.setTabOrder(self.Subject4Saturday, self.Subject3Sunday)
        QWidget.setTabOrder(self.Subject3Sunday, self.Subject3Monday)
        QWidget.setTabOrder(self.Subject3Monday, self.Subject3Tuesday)
        QWidget.setTabOrder(self.Subject3Tuesday, self.Subject3Wednesday)
        QWidget.setTabOrder(self.Subject3Wednesday, self.Subject3Thursday)
        QWidget.setTabOrder(self.Subject3Thursday, self.Subject3Friday)
        QWidget.setTabOrder(self.Subject3Friday, self.Subject3Saturday)
        QWidget.setTabOrder(self.Subject3Saturday, self.Subject2Sunday)
        QWidget.setTabOrder(self.Subject2Sunday, self.Subject2Monday)
        QWidget.setTabOrder(self.Subject2Monday, self.Subject2Tuesday)
        QWidget.setTabOrder(self.Subject2Tuesday, self.Subject2Wednesday)
        QWidget.setTabOrder(self.Subject2Wednesday, self.Subject2Thursday)
        QWidget.setTabOrder(self.Subject2Thursday, self.Subject2Friday)
        QWidget.setTabOrder(self.Subject2Friday, self.Subject2Saturday)
        QWidget.setTabOrder(self.Subject2Saturday, self.Subject1Sunday)
        QWidget.setTabOrder(self.Subject1Sunday, self.Subject1Monday)
        QWidget.setTabOrder(self.Subject1Monday, self.Subject1Tuesday)
        QWidget.setTabOrder(self.Subject1Tuesday, self.Subject1Wednesday)
        QWidget.setTabOrder(self.Subject1Wednesday, self.Subject1Thursday)
        QWidget.setTabOrder(self.Subject1Thursday, self.Subject1Friday)
        QWidget.setTabOrder(self.Subject1Friday, self.Subject1Saturday)

        self.retranslateUi(MainPage)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPage)
    # setupUi

    def retranslateUi(self, MainPage):
        MainPage.setWindowTitle(QCoreApplication.translate("MainPage", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainPage", u"<html><head/><body><p><span style=\" font-weight:600;\">Created</span>:<span style=\" text-decoration: underline;\"/><span style=\" font-weight:600;\">Kaladhar Gopal</span></p></body></html>", None))
        self.Description.setText(QCoreApplication.translate("MainPage", u"  Fill Your Meeting Links And Their Time Here ", None))
        self.Description_2.setText(QCoreApplication.translate("MainPage", u"Leave It Empty If You Do Not Need Them", None))
        self.label_2.setText(QCoreApplication.translate("MainPage", u"TO", None))
        self.SubjectsDaysBtn.setText(QCoreApplication.translate("MainPage", u"Days", None))
#if QT_CONFIG(shortcut)
        self.SubjectsDaysBtn.setShortcut(QCoreApplication.translate("MainPage", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_3.setText(QCoreApplication.translate("MainPage", u"TO", None))
        self.SubjectsDaysBtn_2.setText(QCoreApplication.translate("MainPage", u"Days", None))
#if QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_2.setShortcut(QCoreApplication.translate("MainPage", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_4.setText(QCoreApplication.translate("MainPage", u"TO", None))
        self.SubjectsDaysBtn_3.setText(QCoreApplication.translate("MainPage", u"Days", None))
#if QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_3.setShortcut(QCoreApplication.translate("MainPage", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_5.setText(QCoreApplication.translate("MainPage", u"TO", None))
        self.SubjectsDaysBtn_4.setText(QCoreApplication.translate("MainPage", u"Days", None))
#if QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_4.setShortcut(QCoreApplication.translate("MainPage", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_6.setText(QCoreApplication.translate("MainPage", u"TO", None))
        self.SubjectsDaysBtn_5.setText(QCoreApplication.translate("MainPage", u"Days", None))
#if QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_5.setShortcut(QCoreApplication.translate("MainPage", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_7.setText(QCoreApplication.translate("MainPage", u"TO", None))
        self.SubjectsDaysBtn_6.setText(QCoreApplication.translate("MainPage", u"Days", None))
#if QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_6.setShortcut(QCoreApplication.translate("MainPage", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_8.setText(QCoreApplication.translate("MainPage", u"TO", None))
        self.SubjectsDaysBtn_7.setText(QCoreApplication.translate("MainPage", u"Days", None))
#if QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_7.setShortcut(QCoreApplication.translate("MainPage", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_8.setText(QCoreApplication.translate("MainPage", u"Days", None))
#if QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_8.setShortcut(QCoreApplication.translate("MainPage", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_9.setText(QCoreApplication.translate("MainPage", u"TO", None))
        self.Subject_Link_1.setPlaceholderText(QCoreApplication.translate("MainPage", u"Enter the Meeting Link", None))
        self.Subject_Link_2.setPlaceholderText(QCoreApplication.translate("MainPage", u"Enter the Meeting Link", None))
        self.Subject_Link_3.setPlaceholderText(QCoreApplication.translate("MainPage", u"Enter the Meeting Link", None))
        self.Subject_Link_4.setPlaceholderText(QCoreApplication.translate("MainPage", u"Enter the Meeting Link", None))
        self.Subject_Link_5.setPlaceholderText(QCoreApplication.translate("MainPage", u"Enter the Meeting Link", None))
        self.Subject_Link_6.setPlaceholderText(QCoreApplication.translate("MainPage", u"Enter the Meeting Link", None))
        self.Subject_Link_7.setPlaceholderText(QCoreApplication.translate("MainPage", u"Enter the Meeting Link", None))
        self.Subject_Link_8.setPlaceholderText(QCoreApplication.translate("MainPage", u"Enter the Meeting Link", None))
        self.Subject8DaysHeading.setText(QCoreApplication.translate("MainPage", u"Days 8", None))
        self.Subject8Sunday.setText(QCoreApplication.translate("MainPage", u"Sun", None))
        self.Subject8Monday.setText(QCoreApplication.translate("MainPage", u"Mon", None))
        self.Subject8Tuesday.setText(QCoreApplication.translate("MainPage", u"Tue", None))
        self.Subject8Wednesday.setText(QCoreApplication.translate("MainPage", u"Wed", None))
        self.Subject8Thursday.setText(QCoreApplication.translate("MainPage", u"Thu", None))
        self.Subject8Friday.setText(QCoreApplication.translate("MainPage", u"Fri", None))
        self.Subject8Saturday.setText(QCoreApplication.translate("MainPage", u"Sat", None))
        self.Subject7DaysHeading.setText(QCoreApplication.translate("MainPage", u"Days 7", None))
        self.Subject7Sunday.setText(QCoreApplication.translate("MainPage", u"Sun", None))
        self.Subject7Monday.setText(QCoreApplication.translate("MainPage", u"Mon", None))
        self.Subject7Tuesday.setText(QCoreApplication.translate("MainPage", u"Tue", None))
        self.Subject7Wednesday.setText(QCoreApplication.translate("MainPage", u"Wed", None))
        self.Subject7Thursday.setText(QCoreApplication.translate("MainPage", u"Thu", None))
        self.Subject7Friday.setText(QCoreApplication.translate("MainPage", u"Fri", None))
        self.Subject7Saturday.setText(QCoreApplication.translate("MainPage", u"Sat", None))
        self.Subject6DaysHeading.setText(QCoreApplication.translate("MainPage", u"Days 6", None))
        self.Subject6Sunday.setText(QCoreApplication.translate("MainPage", u"Sun", None))
        self.Subject6Monday.setText(QCoreApplication.translate("MainPage", u"Mon", None))
        self.Subject6Tuesday.setText(QCoreApplication.translate("MainPage", u"Tue", None))
        self.Subject6Wednesday.setText(QCoreApplication.translate("MainPage", u"Wed", None))
        self.Subject6Thursday.setText(QCoreApplication.translate("MainPage", u"Thu", None))
        self.Subject6Friday.setText(QCoreApplication.translate("MainPage", u"Fri", None))
        self.Subject6Saturday.setText(QCoreApplication.translate("MainPage", u"Sat", None))
        self.Subject5DaysHeading.setText(QCoreApplication.translate("MainPage", u"Days 5", None))
        self.Subject5Sunday.setText(QCoreApplication.translate("MainPage", u"Sun", None))
        self.Subject5Monday.setText(QCoreApplication.translate("MainPage", u"Mon", None))
        self.Subjcet5Tuesday.setText(QCoreApplication.translate("MainPage", u"Tue", None))
        self.Subject5Wednesday.setText(QCoreApplication.translate("MainPage", u"Wed", None))
        self.Subject5Thursday.setText(QCoreApplication.translate("MainPage", u"Thu", None))
        self.Subject5Friday.setText(QCoreApplication.translate("MainPage", u"Fri", None))
        self.Subject5Saturday.setText(QCoreApplication.translate("MainPage", u"Sat", None))
        self.Subject4DaysHeading.setText(QCoreApplication.translate("MainPage", u"Days 4", None))
        self.Subject4Sunday.setText(QCoreApplication.translate("MainPage", u"Sun", None))
        self.Subject4Monday.setText(QCoreApplication.translate("MainPage", u"Mon", None))
        self.Subject4Tuesday.setText(QCoreApplication.translate("MainPage", u"Tue", None))
        self.Subject4Wednesday.setText(QCoreApplication.translate("MainPage", u"Wed", None))
        self.Subject4Thursday.setText(QCoreApplication.translate("MainPage", u"Thu", None))
        self.Subject4Friday.setText(QCoreApplication.translate("MainPage", u"Fri", None))
        self.Subject4Saturday.setText(QCoreApplication.translate("MainPage", u"Sat", None))
        self.Subject3DaysHeading.setText(QCoreApplication.translate("MainPage", u"Days 3", None))
        self.Subject3Sunday.setText(QCoreApplication.translate("MainPage", u"Sun", None))
        self.Subject3Monday.setText(QCoreApplication.translate("MainPage", u"Mon", None))
        self.Subject3Tuesday.setText(QCoreApplication.translate("MainPage", u"Tue", None))
        self.Subject3Wednesday.setText(QCoreApplication.translate("MainPage", u"Wed", None))
        self.Subject3Thursday.setText(QCoreApplication.translate("MainPage", u"Thu", None))
        self.Subject3Friday.setText(QCoreApplication.translate("MainPage", u"Fri", None))
        self.Subject3Saturday.setText(QCoreApplication.translate("MainPage", u"Sat", None))
        self.Subject2DaysHeading.setText(QCoreApplication.translate("MainPage", u"Days 2", None))
        self.Subject2Sunday.setText(QCoreApplication.translate("MainPage", u"Sun", None))
        self.Subject2Monday.setText(QCoreApplication.translate("MainPage", u"Mon", None))
        self.Subject2Tuesday.setText(QCoreApplication.translate("MainPage", u"Tue", None))
        self.Subject2Wednesday.setText(QCoreApplication.translate("MainPage", u"Wed", None))
        self.Subject2Thursday.setText(QCoreApplication.translate("MainPage", u"Thu", None))
        self.Subject2Friday.setText(QCoreApplication.translate("MainPage", u"Fri", None))
        self.Subject2Saturday.setText(QCoreApplication.translate("MainPage", u"Sat", None))
        self.Subject1DaysHeading.setText(QCoreApplication.translate("MainPage", u"Days 1", None))
        self.Subject1Sunday.setText(QCoreApplication.translate("MainPage", u"Sun", None))
        self.Subject1Monday.setText(QCoreApplication.translate("MainPage", u"Mon", None))
        self.Subject1Tuesday.setText(QCoreApplication.translate("MainPage", u"Tue", None))
        self.Subject1Wednesday.setText(QCoreApplication.translate("MainPage", u"Wed", None))
        self.Subject1Thursday.setText(QCoreApplication.translate("MainPage", u"Thu", None))
        self.Subject1Friday.setText(QCoreApplication.translate("MainPage", u"Fri", None))
        self.Subject1Saturday.setText(QCoreApplication.translate("MainPage", u"Sat", None))
        self.Subject_1.setText("")
        self.Subject_1.setPlaceholderText(QCoreApplication.translate("MainPage", u"Enter Subject", None))
        self.Subject_2.setText("")
        self.Subject_2.setPlaceholderText(QCoreApplication.translate("MainPage", u"Enter Subject", None))
        self.Subject_3.setText("")
        self.Subject_3.setPlaceholderText(QCoreApplication.translate("MainPage", u"Enter Subject", None))
        self.Subject_4.setText("")
        self.Subject_4.setPlaceholderText(QCoreApplication.translate("MainPage", u"Enter Subject", None))
        self.Subject_5.setText("")
        self.Subject_5.setPlaceholderText(QCoreApplication.translate("MainPage", u"Enter Subject", None))
        self.Subject_6.setText("")
        self.Subject_6.setPlaceholderText(QCoreApplication.translate("MainPage", u"Enter Subject", None))
        self.Subject_7.setText("")
        self.Subject_7.setPlaceholderText(QCoreApplication.translate("MainPage", u"Enter Subject", None))
        self.Subject_8.setText("")
        self.Subject_8.setPlaceholderText(QCoreApplication.translate("MainPage", u"Enter Subject", None))
        self.AppTitle.setText(QCoreApplication.translate("MainPage", u"<html><head/><body><p align=\"justify\">Information Page</p></body></html>", None))
        self.GoBackButton.setText(QCoreApplication.translate("MainPage", u"<- Go Back ", None))
        self.NextButton.setText(QCoreApplication.translate("MainPage", u"Next", None))
#if QT_CONFIG(tooltip)
        self.Minimizebtn.setToolTip(QCoreApplication.translate("MainPage", u"<html><head/><body><p>Minimize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Minimizebtn.setText("")
#if QT_CONFIG(tooltip)
        self.Maximizebtn.setToolTip(QCoreApplication.translate("MainPage", u"<html><head/><body><p>Maximize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Maximizebtn.setText("")
#if QT_CONFIG(tooltip)
        self.CloseButton.setToolTip(QCoreApplication.translate("MainPage", u"<html><head/><body><p>Close</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.CloseButton.setText("")
    # retranslateUi

