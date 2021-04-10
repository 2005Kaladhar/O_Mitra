# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'afterloginMdcJSy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AfterLogin(object):
    def setupUi(self, AfterLogin):
        if not AfterLogin.objectName():
            AfterLogin.setObjectName(u"AfterLogin")
        AfterLogin.resize(814, 506)
        AfterLogin.setMinimumSize(QSize(814, 506))
        AfterLogin.setMaximumSize(QSize(814, 506))
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        AfterLogin.setWindowIcon(icon)
        self.centralwidget = QWidget(AfterLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setSizeIncrement(QSize(814, 506))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, 0, 841, 521))
        self.label.setPixmap(QPixmap(u"25864037242020b0c4a5baed125bad00-700.jpg"))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setGeometry(QRect(0, 0, 811, 501))
        self.frame.setStyleSheet(u"QFrame{\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.71, x2:1, y2:0.670636, stop:0 rgba(0, 0, 0, 153), stop:1 rgba(13, 13, 13, 142));\n"
"	border-radius:10px;\n"
"\n"
"}")
        self.frame.setInputMethodHints(Qt.ImhNone)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.NextButton = QPushButton(self.frame)
        self.NextButton.setObjectName(u"NextButton")
        self.NextButton.setGeometry(QRect(660, 460, 131, 31))
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
"	background-color: rgb(0, 170, 0);\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")
        self.CloseButton = QPushButton(self.frame)
        self.CloseButton.setObjectName(u"CloseButton")
        self.CloseButton.setGeometry(QRect(760, 0, 51, 21))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.CloseButton.setFont(font1)
        self.CloseButton.setStyleSheet(u"QPushButton{\n"
"border-radius:5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.773, x2:0.982955, y2:0.767, stop:0 rgba(178, 10, 10, 255), stop:0.903409 rgba(226, 14, 122, 244));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.773, x2:0.982955, y2:0.767, stop:0 rgba(133, 0, 0, 255), stop:0.903409 rgba(178, 0, 90, 244));\n"
"	color: rgb(240, 240, 240);\n"
"\n"
"}")
        self.Heading = QLabel(self.frame)
        self.Heading.setObjectName(u"Heading")
        self.Heading.setGeometry(QRect(170, 0, 471, 41))
        font2 = QFont()
        font2.setPointSize(24)
        self.Heading.setFont(font2)
        self.Heading.setStyleSheet(u"QLabel{\n"
"	\n"
"color: rgb(241, 44, 172);\n"
"border-radius:10px;\n"
"\n"
"}")
        self.Heading.setMidLineWidth(4)
        self.Heading.setAlignment(Qt.AlignCenter)
        self.Description = QLabel(self.frame)
        self.Description.setObjectName(u"Description")
        self.Description.setGeometry(QRect(60, 50, 681, 51))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.Description.setFont(font3)
        self.Description.setLayoutDirection(Qt.LeftToRight)
        self.Description.setAutoFillBackground(False)
        self.Description.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(242, 255, 29, 255), stop:1 rgba(67, 201, 0, 255));")
        self.Description.setTextFormat(Qt.RichText)
        self.Description.setScaledContents(False)
        self.Description.setAlignment(Qt.AlignCenter)
        self.Subject_Link_1 = QLineEdit(self.frame)
        self.Subject_Link_1.setObjectName(u"Subject_Link_1")
        self.Subject_Link_1.setGeometry(QRect(160, 150, 161, 21))
        font4 = QFont()
        font4.setPointSize(9)
        self.Subject_Link_1.setFont(font4)
        self.Subject_Link_1.setStyleSheet(u"QLineEdit{\n"
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
        self.Subject_Link_1.setEchoMode(QLineEdit.Normal)
        self.Subject_Link_1.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(460, 150, 21, 16))
        self.label_2.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(460, 190, 21, 16))
        self.label_3.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(460, 230, 21, 16))
        self.label_4.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(460, 270, 21, 16))
        self.label_5.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(460, 310, 21, 16))
        self.label_6.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(460, 350, 21, 16))
        self.label_7.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(460, 390, 21, 16))
        self.label_8.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.Subject_1From = QTimeEdit(self.frame)
        self.Subject_1From.setObjectName(u"Subject_1From")
        self.Subject_1From.setGeometry(QRect(340, 150, 118, 21))
        self.Subject_1From.setMouseTracking(True)
        self.Subject_1From.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:10px;\n"
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
        self.Subject_1To = QTimeEdit(self.frame)
        self.Subject_1To.setObjectName(u"Subject_1To")
        self.Subject_1To.setGeometry(QRect(480, 150, 118, 21))
        self.Subject_1To.setMouseTracking(True)
        self.Subject_1To.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:10px;\n"
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
        self.Subject_2From = QTimeEdit(self.frame)
        self.Subject_2From.setObjectName(u"Subject_2From")
        self.Subject_2From.setGeometry(QRect(340, 190, 118, 21))
        self.Subject_2From.setMouseTracking(True)
        self.Subject_2From.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:10px;\n"
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
        self.Subject_2To = QTimeEdit(self.frame)
        self.Subject_2To.setObjectName(u"Subject_2To")
        self.Subject_2To.setGeometry(QRect(480, 190, 118, 21))
        self.Subject_2To.setMouseTracking(True)
        self.Subject_2To.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:10px;\n"
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
        self.Subject_3From = QTimeEdit(self.frame)
        self.Subject_3From.setObjectName(u"Subject_3From")
        self.Subject_3From.setGeometry(QRect(340, 230, 118, 21))
        self.Subject_3From.setMouseTracking(True)
        self.Subject_3From.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:10px;\n"
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
        self.Subject_3To = QTimeEdit(self.frame)
        self.Subject_3To.setObjectName(u"Subject_3To")
        self.Subject_3To.setGeometry(QRect(480, 230, 118, 21))
        self.Subject_3To.setMouseTracking(True)
        self.Subject_3To.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:10px;\n"
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
        self.Subject_4From = QTimeEdit(self.frame)
        self.Subject_4From.setObjectName(u"Subject_4From")
        self.Subject_4From.setGeometry(QRect(340, 270, 118, 21))
        self.Subject_4From.setMouseTracking(True)
        self.Subject_4From.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:10px;\n"
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
        self.Subject_4To = QTimeEdit(self.frame)
        self.Subject_4To.setObjectName(u"Subject_4To")
        self.Subject_4To.setGeometry(QRect(480, 270, 118, 21))
        self.Subject_4To.setMouseTracking(True)
        self.Subject_4To.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:10px;\n"
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
        self.Subject_5From = QTimeEdit(self.frame)
        self.Subject_5From.setObjectName(u"Subject_5From")
        self.Subject_5From.setGeometry(QRect(340, 310, 118, 21))
        self.Subject_5From.setMouseTracking(True)
        self.Subject_5From.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:10px;\n"
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
        self.Subject_5To = QTimeEdit(self.frame)
        self.Subject_5To.setObjectName(u"Subject_5To")
        self.Subject_5To.setGeometry(QRect(480, 310, 118, 21))
        self.Subject_5To.setMouseTracking(True)
        self.Subject_5To.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:10px;\n"
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
        self.Subject_6From = QTimeEdit(self.frame)
        self.Subject_6From.setObjectName(u"Subject_6From")
        self.Subject_6From.setGeometry(QRect(340, 350, 118, 21))
        self.Subject_6From.setMouseTracking(True)
        self.Subject_6From.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:10px;\n"
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
        self.Subject_6To = QTimeEdit(self.frame)
        self.Subject_6To.setObjectName(u"Subject_6To")
        self.Subject_6To.setGeometry(QRect(480, 350, 118, 21))
        self.Subject_6To.setMouseTracking(True)
        self.Subject_6To.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:10px;\n"
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
        self.Subject_7From = QTimeEdit(self.frame)
        self.Subject_7From.setObjectName(u"Subject_7From")
        self.Subject_7From.setGeometry(QRect(340, 390, 118, 21))
        self.Subject_7From.setMouseTracking(True)
        self.Subject_7From.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:10px;\n"
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
        self.Subject_7To = QTimeEdit(self.frame)
        self.Subject_7To.setObjectName(u"Subject_7To")
        self.Subject_7To.setGeometry(QRect(480, 390, 118, 21))
        self.Subject_7To.setMouseTracking(True)
        self.Subject_7To.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:10px;\n"
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
        self.Subject_1 = QLineEdit(self.frame)
        self.Subject_1.setObjectName(u"Subject_1")
        self.Subject_1.setGeometry(QRect(20, 140, 121, 31))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Semibold")
        font5.setPointSize(11)
        self.Subject_1.setFont(font5)
        self.Subject_1.setStyleSheet(u"QLineEdit{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 129, 23, 255), stop:1 rgba(239, 239, 37, 255));\n"
"}")
        self.Subject_1.setAlignment(Qt.AlignCenter)
        self.Subject_2 = QLineEdit(self.frame)
        self.Subject_2.setObjectName(u"Subject_2")
        self.Subject_2.setGeometry(QRect(20, 180, 121, 31))
        self.Subject_2.setFont(font5)
        self.Subject_2.setStyleSheet(u"QLineEdit{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 129, 23, 255), stop:1 rgba(239, 239, 37, 255));\n"
"}")
        self.Subject_2.setAlignment(Qt.AlignCenter)
        self.Subject_3 = QLineEdit(self.frame)
        self.Subject_3.setObjectName(u"Subject_3")
        self.Subject_3.setGeometry(QRect(20, 220, 121, 31))
        self.Subject_3.setFont(font5)
        self.Subject_3.setStyleSheet(u"QLineEdit{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 129, 23, 255), stop:1 rgba(239, 239, 37, 255));\n"
"}")
        self.Subject_3.setAlignment(Qt.AlignCenter)
        self.Subject_4 = QLineEdit(self.frame)
        self.Subject_4.setObjectName(u"Subject_4")
        self.Subject_4.setGeometry(QRect(20, 260, 121, 31))
        self.Subject_4.setFont(font5)
        self.Subject_4.setStyleSheet(u"QLineEdit{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 129, 23, 255), stop:1 rgba(239, 239, 37, 255));\n"
"}")
        self.Subject_4.setAlignment(Qt.AlignCenter)
        self.Subject_5 = QLineEdit(self.frame)
        self.Subject_5.setObjectName(u"Subject_5")
        self.Subject_5.setGeometry(QRect(20, 300, 121, 31))
        self.Subject_5.setFont(font5)
        self.Subject_5.setStyleSheet(u"QLineEdit{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 129, 23, 255), stop:1 rgba(239, 239, 37, 255));\n"
"}")
        self.Subject_5.setAlignment(Qt.AlignCenter)
        self.Subject_6 = QLineEdit(self.frame)
        self.Subject_6.setObjectName(u"Subject_6")
        self.Subject_6.setGeometry(QRect(20, 340, 121, 31))
        self.Subject_6.setFont(font5)
        self.Subject_6.setStyleSheet(u"QLineEdit{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 129, 23, 255), stop:1 rgba(239, 239, 37, 255));\n"
"}")
        self.Subject_6.setAlignment(Qt.AlignCenter)
        self.Subject_7 = QLineEdit(self.frame)
        self.Subject_7.setObjectName(u"Subject_7")
        self.Subject_7.setGeometry(QRect(20, 380, 121, 31))
        self.Subject_7.setFont(font5)
        self.Subject_7.setStyleSheet(u"QLineEdit{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 129, 23, 255), stop:1 rgba(239, 239, 37, 255));\n"
"}")
        self.Subject_7.setAlignment(Qt.AlignCenter)
        self.Subject_Link_2 = QLineEdit(self.frame)
        self.Subject_Link_2.setObjectName(u"Subject_Link_2")
        self.Subject_Link_2.setGeometry(QRect(160, 190, 161, 21))
        self.Subject_Link_2.setFont(font4)
        self.Subject_Link_2.setStyleSheet(u"QLineEdit{\n"
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
        self.Subject_Link_2.setEchoMode(QLineEdit.Normal)
        self.Subject_Link_2.setAlignment(Qt.AlignCenter)
        self.Subject_Link_3 = QLineEdit(self.frame)
        self.Subject_Link_3.setObjectName(u"Subject_Link_3")
        self.Subject_Link_3.setGeometry(QRect(160, 230, 161, 21))
        self.Subject_Link_3.setFont(font4)
        self.Subject_Link_3.setStyleSheet(u"QLineEdit{\n"
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
        self.Subject_Link_3.setEchoMode(QLineEdit.Normal)
        self.Subject_Link_3.setAlignment(Qt.AlignCenter)
        self.Subject_Link_4 = QLineEdit(self.frame)
        self.Subject_Link_4.setObjectName(u"Subject_Link_4")
        self.Subject_Link_4.setGeometry(QRect(160, 270, 161, 21))
        self.Subject_Link_4.setFont(font4)
        self.Subject_Link_4.setStyleSheet(u"QLineEdit{\n"
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
        self.Subject_Link_4.setEchoMode(QLineEdit.Normal)
        self.Subject_Link_4.setAlignment(Qt.AlignCenter)
        self.Subject_Link_5 = QLineEdit(self.frame)
        self.Subject_Link_5.setObjectName(u"Subject_Link_5")
        self.Subject_Link_5.setGeometry(QRect(160, 310, 161, 21))
        self.Subject_Link_5.setFont(font4)
        self.Subject_Link_5.setStyleSheet(u"QLineEdit{\n"
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
        self.Subject_Link_5.setEchoMode(QLineEdit.Normal)
        self.Subject_Link_5.setAlignment(Qt.AlignCenter)
        self.Subject_Link_6 = QLineEdit(self.frame)
        self.Subject_Link_6.setObjectName(u"Subject_Link_6")
        self.Subject_Link_6.setGeometry(QRect(160, 350, 161, 21))
        self.Subject_Link_6.setFont(font4)
        self.Subject_Link_6.setStyleSheet(u"QLineEdit{\n"
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
        self.Subject_Link_6.setEchoMode(QLineEdit.Normal)
        self.Subject_Link_6.setAlignment(Qt.AlignCenter)
        self.Subject_Link_7 = QLineEdit(self.frame)
        self.Subject_Link_7.setObjectName(u"Subject_Link_7")
        self.Subject_Link_7.setGeometry(QRect(160, 390, 161, 21))
        self.Subject_Link_7.setFont(font4)
        self.Subject_Link_7.setStyleSheet(u"QLineEdit{\n"
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
        self.Subject_Link_7.setEchoMode(QLineEdit.Normal)
        self.Subject_Link_7.setAlignment(Qt.AlignCenter)
        self.Subject_8 = QLineEdit(self.frame)
        self.Subject_8.setObjectName(u"Subject_8")
        self.Subject_8.setGeometry(QRect(20, 420, 121, 31))
        self.Subject_8.setFont(font5)
        self.Subject_8.setStyleSheet(u"QLineEdit{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 129, 23, 255), stop:1 rgba(239, 239, 37, 255));\n"
"}")
        self.Subject_8.setAlignment(Qt.AlignCenter)
        self.Subject_Link_8 = QLineEdit(self.frame)
        self.Subject_Link_8.setObjectName(u"Subject_Link_8")
        self.Subject_Link_8.setGeometry(QRect(160, 430, 161, 21))
        self.Subject_Link_8.setFont(font4)
        self.Subject_Link_8.setStyleSheet(u"QLineEdit{\n"
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
        self.Subject_Link_8.setEchoMode(QLineEdit.Normal)
        self.Subject_Link_8.setAlignment(Qt.AlignCenter)
        self.Subject_8From = QTimeEdit(self.frame)
        self.Subject_8From.setObjectName(u"Subject_8From")
        self.Subject_8From.setGeometry(QRect(340, 430, 118, 21))
        self.Subject_8From.setMouseTracking(True)
        self.Subject_8From.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:10px;\n"
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
        self.Subject_8To_2 = QTimeEdit(self.frame)
        self.Subject_8To_2.setObjectName(u"Subject_8To_2")
        self.Subject_8To_2.setGeometry(QRect(480, 430, 118, 21))
        self.Subject_8To_2.setMouseTracking(True)
        self.Subject_8To_2.setStyleSheet(u"QTimeEdit{\n"
"\n"
"border-radius:10px;\n"
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
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(460, 430, 21, 16))
        self.label_9.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.SubjectDays = QFrame(self.frame)
        self.SubjectDays.setObjectName(u"SubjectDays")
        self.SubjectDays.setGeometry(QRect(670, 170, 118, 233))
        self.SubjectDays.setFrameShape(QFrame.StyledPanel)
        self.SubjectDays.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.SubjectDays)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Subject1DaysHeading = QLabel(self.SubjectDays)
        self.Subject1DaysHeading.setObjectName(u"Subject1DaysHeading")
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.Subject1DaysHeading.setFont(font6)
        self.Subject1DaysHeading.setStyleSheet(u"QLabel{\n"
"	\n"
"color: rgb(241, 44, 172);\n"
"border-radius:10px;\n"
"\n"
"}")
        self.Subject1DaysHeading.setMidLineWidth(4)
        self.Subject1DaysHeading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Subject1DaysHeading)

        self.Subject1Sunday = QCheckBox(self.SubjectDays)
        self.Subject1Sunday.setObjectName(u"Subject1Sunday")
        font7 = QFont()
        font7.setPointSize(11)
        self.Subject1Sunday.setFont(font7)
        self.Subject1Sunday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject1Sunday.setTristate(False)

        self.verticalLayout_2.addWidget(self.Subject1Sunday)

        self.Subject1Monday = QCheckBox(self.SubjectDays)
        self.Subject1Monday.setObjectName(u"Subject1Monday")
        self.Subject1Monday.setFont(font7)
        self.Subject1Monday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject1Monday.setTristate(False)

        self.verticalLayout_2.addWidget(self.Subject1Monday)

        self.Subject1Tuesday = QCheckBox(self.SubjectDays)
        self.Subject1Tuesday.setObjectName(u"Subject1Tuesday")
        self.Subject1Tuesday.setFont(font7)
        self.Subject1Tuesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject1Tuesday.setTristate(False)

        self.verticalLayout_2.addWidget(self.Subject1Tuesday)

        self.Subject1Wednesday = QCheckBox(self.SubjectDays)
        self.Subject1Wednesday.setObjectName(u"Subject1Wednesday")
        self.Subject1Wednesday.setFont(font7)
        self.Subject1Wednesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject1Wednesday.setTristate(False)

        self.verticalLayout_2.addWidget(self.Subject1Wednesday)

        self.Subject1Thursday = QCheckBox(self.SubjectDays)
        self.Subject1Thursday.setObjectName(u"Subject1Thursday")
        self.Subject1Thursday.setFont(font7)
        self.Subject1Thursday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject1Thursday.setTristate(False)

        self.verticalLayout_2.addWidget(self.Subject1Thursday)

        self.Subject1Friday = QCheckBox(self.SubjectDays)
        self.Subject1Friday.setObjectName(u"Subject1Friday")
        self.Subject1Friday.setFont(font7)
        self.Subject1Friday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject1Friday.setTristate(False)

        self.verticalLayout_2.addWidget(self.Subject1Friday)

        self.Subject1Saturday = QCheckBox(self.SubjectDays)
        self.Subject1Saturday.setObjectName(u"Subject1Saturday")
        self.Subject1Saturday.setFont(font7)
        self.Subject1Saturday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject1Saturday.setTristate(False)

        self.verticalLayout_2.addWidget(self.Subject1Saturday)

        self.SubjectsDaysBtn = QPushButton(self.frame)
        self.SubjectsDaysBtn.setObjectName(u"SubjectsDaysBtn")
        self.SubjectsDaysBtn.setGeometry(QRect(600, 150, 41, 21))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(9)
        font8.setBold(False)
        font8.setWeight(50)
        self.SubjectsDaysBtn.setFont(font8)
        self.SubjectsDaysBtn.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(232, 154, 0, 255), stop:1 rgba(255, 102, 25, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 170, 0, 255));\n"
"}")
        self.SubjectsDaysBtn_2 = QPushButton(self.frame)
        self.SubjectsDaysBtn_2.setObjectName(u"SubjectsDaysBtn_2")
        self.SubjectsDaysBtn_2.setGeometry(QRect(600, 190, 41, 21))
        self.SubjectsDaysBtn_2.setFont(font8)
        self.SubjectsDaysBtn_2.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(232, 154, 0, 255), stop:1 rgba(255, 102, 25, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 170, 0, 255));\n"
"}")
        self.SubjectsDaysBtn_3 = QPushButton(self.frame)
        self.SubjectsDaysBtn_3.setObjectName(u"SubjectsDaysBtn_3")
        self.SubjectsDaysBtn_3.setGeometry(QRect(600, 230, 41, 21))
        self.SubjectsDaysBtn_3.setFont(font8)
        self.SubjectsDaysBtn_3.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(232, 154, 0, 255), stop:1 rgba(255, 102, 25, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 170, 0, 255));\n"
"}")
        self.SubjectsDaysBtn_4 = QPushButton(self.frame)
        self.SubjectsDaysBtn_4.setObjectName(u"SubjectsDaysBtn_4")
        self.SubjectsDaysBtn_4.setGeometry(QRect(600, 270, 41, 21))
        self.SubjectsDaysBtn_4.setFont(font8)
        self.SubjectsDaysBtn_4.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(232, 154, 0, 255), stop:1 rgba(255, 102, 25, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 170, 0, 255));\n"
"}")
        self.SubjectsDaysBtn_5 = QPushButton(self.frame)
        self.SubjectsDaysBtn_5.setObjectName(u"SubjectsDaysBtn_5")
        self.SubjectsDaysBtn_5.setGeometry(QRect(600, 310, 41, 21))
        self.SubjectsDaysBtn_5.setFont(font8)
        self.SubjectsDaysBtn_5.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(232, 154, 0, 255), stop:1 rgba(255, 102, 25, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 170, 0, 255));\n"
"}")
        self.SubjectsDaysBtn_6 = QPushButton(self.frame)
        self.SubjectsDaysBtn_6.setObjectName(u"SubjectsDaysBtn_6")
        self.SubjectsDaysBtn_6.setGeometry(QRect(600, 350, 41, 21))
        self.SubjectsDaysBtn_6.setFont(font8)
        self.SubjectsDaysBtn_6.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(232, 154, 0, 255), stop:1 rgba(255, 102, 25, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 170, 0, 255));\n"
"}")
        self.SubjectsDaysBtn_7 = QPushButton(self.frame)
        self.SubjectsDaysBtn_7.setObjectName(u"SubjectsDaysBtn_7")
        self.SubjectsDaysBtn_7.setGeometry(QRect(600, 390, 41, 21))
        self.SubjectsDaysBtn_7.setFont(font8)
        self.SubjectsDaysBtn_7.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(232, 154, 0, 255), stop:1 rgba(255, 102, 25, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 170, 0, 255));\n"
"}")
        self.SubjectsDaysBtn_8 = QPushButton(self.frame)
        self.SubjectsDaysBtn_8.setObjectName(u"SubjectsDaysBtn_8")
        self.SubjectsDaysBtn_8.setGeometry(QRect(600, 430, 41, 21))
        self.SubjectsDaysBtn_8.setFont(font8)
        self.SubjectsDaysBtn_8.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(232, 154, 0, 255), stop:1 rgba(255, 102, 25, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 170, 0, 255));\n"
"}")
        self.SubjectDays_2 = QFrame(self.frame)
        self.SubjectDays_2.setObjectName(u"SubjectDays_2")
        self.SubjectDays_2.setGeometry(QRect(670, 170, 118, 233))
        self.SubjectDays_2.setFrameShape(QFrame.StyledPanel)
        self.SubjectDays_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.SubjectDays_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Subject2DaysHeading = QLabel(self.SubjectDays_2)
        self.Subject2DaysHeading.setObjectName(u"Subject2DaysHeading")
        self.Subject2DaysHeading.setFont(font6)
        self.Subject2DaysHeading.setStyleSheet(u"QLabel{\n"
"	\n"
"color: rgb(241, 44, 172);\n"
"border-radius:10px;\n"
"\n"
"}")
        self.Subject2DaysHeading.setMidLineWidth(4)
        self.Subject2DaysHeading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.Subject2DaysHeading)

        self.Subject2Sunday = QCheckBox(self.SubjectDays_2)
        self.Subject2Sunday.setObjectName(u"Subject2Sunday")
        self.Subject2Sunday.setFont(font7)
        self.Subject2Sunday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject2Sunday.setTristate(False)

        self.verticalLayout_5.addWidget(self.Subject2Sunday)

        self.Subject2Monday = QCheckBox(self.SubjectDays_2)
        self.Subject2Monday.setObjectName(u"Subject2Monday")
        self.Subject2Monday.setFont(font7)
        self.Subject2Monday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject2Monday.setTristate(False)

        self.verticalLayout_5.addWidget(self.Subject2Monday)

        self.Subject2Tuesday = QCheckBox(self.SubjectDays_2)
        self.Subject2Tuesday.setObjectName(u"Subject2Tuesday")
        self.Subject2Tuesday.setFont(font7)
        self.Subject2Tuesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject2Tuesday.setTristate(False)

        self.verticalLayout_5.addWidget(self.Subject2Tuesday)

        self.Subject2Wednesday = QCheckBox(self.SubjectDays_2)
        self.Subject2Wednesday.setObjectName(u"Subject2Wednesday")
        self.Subject2Wednesday.setFont(font7)
        self.Subject2Wednesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject2Wednesday.setTristate(False)

        self.verticalLayout_5.addWidget(self.Subject2Wednesday)

        self.Subject2Thursday = QCheckBox(self.SubjectDays_2)
        self.Subject2Thursday.setObjectName(u"Subject2Thursday")
        self.Subject2Thursday.setFont(font7)
        self.Subject2Thursday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject2Thursday.setTristate(False)

        self.verticalLayout_5.addWidget(self.Subject2Thursday)

        self.Subject2Friday = QCheckBox(self.SubjectDays_2)
        self.Subject2Friday.setObjectName(u"Subject2Friday")
        self.Subject2Friday.setFont(font7)
        self.Subject2Friday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject2Friday.setTristate(False)

        self.verticalLayout_5.addWidget(self.Subject2Friday)

        self.Subject2Saturday = QCheckBox(self.SubjectDays_2)
        self.Subject2Saturday.setObjectName(u"Subject2Saturday")
        self.Subject2Saturday.setFont(font7)
        self.Subject2Saturday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject2Saturday.setTristate(False)

        self.verticalLayout_5.addWidget(self.Subject2Saturday)

        self.SubjectDays_3 = QFrame(self.frame)
        self.SubjectDays_3.setObjectName(u"SubjectDays_3")
        self.SubjectDays_3.setGeometry(QRect(670, 170, 118, 233))
        self.SubjectDays_3.setFrameShape(QFrame.StyledPanel)
        self.SubjectDays_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.SubjectDays_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Subject3DaysHeading = QLabel(self.SubjectDays_3)
        self.Subject3DaysHeading.setObjectName(u"Subject3DaysHeading")
        self.Subject3DaysHeading.setFont(font6)
        self.Subject3DaysHeading.setStyleSheet(u"QLabel{\n"
"	\n"
"color: rgb(241, 44, 172);\n"
"border-radius:10px;\n"
"\n"
"}")
        self.Subject3DaysHeading.setMidLineWidth(4)
        self.Subject3DaysHeading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.Subject3DaysHeading)

        self.Subject3Sunday = QCheckBox(self.SubjectDays_3)
        self.Subject3Sunday.setObjectName(u"Subject3Sunday")
        self.Subject3Sunday.setFont(font7)
        self.Subject3Sunday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject3Sunday.setTristate(False)

        self.verticalLayout_6.addWidget(self.Subject3Sunday)

        self.Subject3Monday = QCheckBox(self.SubjectDays_3)
        self.Subject3Monday.setObjectName(u"Subject3Monday")
        self.Subject3Monday.setFont(font7)
        self.Subject3Monday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject3Monday.setTristate(False)

        self.verticalLayout_6.addWidget(self.Subject3Monday)

        self.Subject3Tuesday = QCheckBox(self.SubjectDays_3)
        self.Subject3Tuesday.setObjectName(u"Subject3Tuesday")
        self.Subject3Tuesday.setFont(font7)
        self.Subject3Tuesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject3Tuesday.setTristate(False)

        self.verticalLayout_6.addWidget(self.Subject3Tuesday)

        self.Subject3Wednesday = QCheckBox(self.SubjectDays_3)
        self.Subject3Wednesday.setObjectName(u"Subject3Wednesday")
        self.Subject3Wednesday.setFont(font7)
        self.Subject3Wednesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject3Wednesday.setTristate(False)

        self.verticalLayout_6.addWidget(self.Subject3Wednesday)

        self.Subject3Thursday = QCheckBox(self.SubjectDays_3)
        self.Subject3Thursday.setObjectName(u"Subject3Thursday")
        self.Subject3Thursday.setFont(font7)
        self.Subject3Thursday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject3Thursday.setTristate(False)

        self.verticalLayout_6.addWidget(self.Subject3Thursday)

        self.Subject3Friday = QCheckBox(self.SubjectDays_3)
        self.Subject3Friday.setObjectName(u"Subject3Friday")
        self.Subject3Friday.setFont(font7)
        self.Subject3Friday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject3Friday.setTristate(False)

        self.verticalLayout_6.addWidget(self.Subject3Friday)

        self.Subject3Saturday = QCheckBox(self.SubjectDays_3)
        self.Subject3Saturday.setObjectName(u"Subject3Saturday")
        self.Subject3Saturday.setFont(font7)
        self.Subject3Saturday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject3Saturday.setTristate(False)

        self.verticalLayout_6.addWidget(self.Subject3Saturday)

        self.SubjectDays_4 = QFrame(self.frame)
        self.SubjectDays_4.setObjectName(u"SubjectDays_4")
        self.SubjectDays_4.setGeometry(QRect(670, 170, 118, 233))
        self.SubjectDays_4.setFrameShape(QFrame.StyledPanel)
        self.SubjectDays_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.SubjectDays_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Subject4DaysHeading = QLabel(self.SubjectDays_4)
        self.Subject4DaysHeading.setObjectName(u"Subject4DaysHeading")
        self.Subject4DaysHeading.setFont(font6)
        self.Subject4DaysHeading.setStyleSheet(u"QLabel{\n"
"	\n"
"color: rgb(241, 44, 172);\n"
"border-radius:10px;\n"
"\n"
"}")
        self.Subject4DaysHeading.setMidLineWidth(4)
        self.Subject4DaysHeading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.Subject4DaysHeading)

        self.Subject4Sunday = QCheckBox(self.SubjectDays_4)
        self.Subject4Sunday.setObjectName(u"Subject4Sunday")
        self.Subject4Sunday.setFont(font7)
        self.Subject4Sunday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject4Sunday.setTristate(False)

        self.verticalLayout_7.addWidget(self.Subject4Sunday)

        self.Subject4Monday = QCheckBox(self.SubjectDays_4)
        self.Subject4Monday.setObjectName(u"Subject4Monday")
        self.Subject4Monday.setFont(font7)
        self.Subject4Monday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject4Monday.setTristate(False)

        self.verticalLayout_7.addWidget(self.Subject4Monday)

        self.Subject4Tuesday = QCheckBox(self.SubjectDays_4)
        self.Subject4Tuesday.setObjectName(u"Subject4Tuesday")
        self.Subject4Tuesday.setFont(font7)
        self.Subject4Tuesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject4Tuesday.setTristate(False)

        self.verticalLayout_7.addWidget(self.Subject4Tuesday)

        self.Subject4Wednesday = QCheckBox(self.SubjectDays_4)
        self.Subject4Wednesday.setObjectName(u"Subject4Wednesday")
        self.Subject4Wednesday.setFont(font7)
        self.Subject4Wednesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject4Wednesday.setTristate(False)

        self.verticalLayout_7.addWidget(self.Subject4Wednesday)

        self.Subject4Thursday = QCheckBox(self.SubjectDays_4)
        self.Subject4Thursday.setObjectName(u"Subject4Thursday")
        self.Subject4Thursday.setFont(font7)
        self.Subject4Thursday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject4Thursday.setTristate(False)

        self.verticalLayout_7.addWidget(self.Subject4Thursday)

        self.Subject4Friday = QCheckBox(self.SubjectDays_4)
        self.Subject4Friday.setObjectName(u"Subject4Friday")
        self.Subject4Friday.setFont(font7)
        self.Subject4Friday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject4Friday.setTristate(False)

        self.verticalLayout_7.addWidget(self.Subject4Friday)

        self.Subject4Saturday = QCheckBox(self.SubjectDays_4)
        self.Subject4Saturday.setObjectName(u"Subject4Saturday")
        self.Subject4Saturday.setFont(font7)
        self.Subject4Saturday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject4Saturday.setTristate(False)

        self.verticalLayout_7.addWidget(self.Subject4Saturday)

        self.SubjectDays_5 = QFrame(self.frame)
        self.SubjectDays_5.setObjectName(u"SubjectDays_5")
        self.SubjectDays_5.setGeometry(QRect(670, 170, 118, 233))
        self.SubjectDays_5.setFrameShape(QFrame.StyledPanel)
        self.SubjectDays_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.SubjectDays_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Subject5DaysHeading = QLabel(self.SubjectDays_5)
        self.Subject5DaysHeading.setObjectName(u"Subject5DaysHeading")
        self.Subject5DaysHeading.setFont(font6)
        self.Subject5DaysHeading.setStyleSheet(u"QLabel{\n"
"	\n"
"color: rgb(241, 44, 172);\n"
"border-radius:10px;\n"
"\n"
"}")
        self.Subject5DaysHeading.setMidLineWidth(4)
        self.Subject5DaysHeading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.Subject5DaysHeading)

        self.Subject5Sunday = QCheckBox(self.SubjectDays_5)
        self.Subject5Sunday.setObjectName(u"Subject5Sunday")
        self.Subject5Sunday.setFont(font7)
        self.Subject5Sunday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject5Sunday.setTristate(False)

        self.verticalLayout_8.addWidget(self.Subject5Sunday)

        self.Subject5Monday = QCheckBox(self.SubjectDays_5)
        self.Subject5Monday.setObjectName(u"Subject5Monday")
        self.Subject5Monday.setFont(font7)
        self.Subject5Monday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject5Monday.setTristate(False)

        self.verticalLayout_8.addWidget(self.Subject5Monday)

        self.Subjcet5Tuesday = QCheckBox(self.SubjectDays_5)
        self.Subjcet5Tuesday.setObjectName(u"Subjcet5Tuesday")
        self.Subjcet5Tuesday.setFont(font7)
        self.Subjcet5Tuesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subjcet5Tuesday.setTristate(False)

        self.verticalLayout_8.addWidget(self.Subjcet5Tuesday)

        self.Subject5Wednesday = QCheckBox(self.SubjectDays_5)
        self.Subject5Wednesday.setObjectName(u"Subject5Wednesday")
        self.Subject5Wednesday.setFont(font7)
        self.Subject5Wednesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject5Wednesday.setTristate(False)

        self.verticalLayout_8.addWidget(self.Subject5Wednesday)

        self.Subject5Thursday = QCheckBox(self.SubjectDays_5)
        self.Subject5Thursday.setObjectName(u"Subject5Thursday")
        self.Subject5Thursday.setFont(font7)
        self.Subject5Thursday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject5Thursday.setTristate(False)

        self.verticalLayout_8.addWidget(self.Subject5Thursday)

        self.Subject5Friday = QCheckBox(self.SubjectDays_5)
        self.Subject5Friday.setObjectName(u"Subject5Friday")
        self.Subject5Friday.setFont(font7)
        self.Subject5Friday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject5Friday.setTristate(False)

        self.verticalLayout_8.addWidget(self.Subject5Friday)

        self.Subject5Saturday = QCheckBox(self.SubjectDays_5)
        self.Subject5Saturday.setObjectName(u"Subject5Saturday")
        self.Subject5Saturday.setFont(font7)
        self.Subject5Saturday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject5Saturday.setTristate(False)

        self.verticalLayout_8.addWidget(self.Subject5Saturday)

        self.SubjectDays_6 = QFrame(self.frame)
        self.SubjectDays_6.setObjectName(u"SubjectDays_6")
        self.SubjectDays_6.setGeometry(QRect(670, 170, 118, 233))
        self.SubjectDays_6.setFrameShape(QFrame.StyledPanel)
        self.SubjectDays_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.SubjectDays_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.Subject6DaysHeading = QLabel(self.SubjectDays_6)
        self.Subject6DaysHeading.setObjectName(u"Subject6DaysHeading")
        self.Subject6DaysHeading.setFont(font6)
        self.Subject6DaysHeading.setStyleSheet(u"QLabel{\n"
"	\n"
"color: rgb(241, 44, 172);\n"
"border-radius:10px;\n"
"\n"
"}")
        self.Subject6DaysHeading.setMidLineWidth(4)
        self.Subject6DaysHeading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.Subject6DaysHeading)

        self.Subject6Sunday = QCheckBox(self.SubjectDays_6)
        self.Subject6Sunday.setObjectName(u"Subject6Sunday")
        self.Subject6Sunday.setFont(font7)
        self.Subject6Sunday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject6Sunday.setTristate(False)

        self.verticalLayout_9.addWidget(self.Subject6Sunday)

        self.Subject6Monday = QCheckBox(self.SubjectDays_6)
        self.Subject6Monday.setObjectName(u"Subject6Monday")
        self.Subject6Monday.setFont(font7)
        self.Subject6Monday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject6Monday.setTristate(False)

        self.verticalLayout_9.addWidget(self.Subject6Monday)

        self.Subject6Tuesday = QCheckBox(self.SubjectDays_6)
        self.Subject6Tuesday.setObjectName(u"Subject6Tuesday")
        self.Subject6Tuesday.setFont(font7)
        self.Subject6Tuesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject6Tuesday.setTristate(False)

        self.verticalLayout_9.addWidget(self.Subject6Tuesday)

        self.Subject6Wednesday = QCheckBox(self.SubjectDays_6)
        self.Subject6Wednesday.setObjectName(u"Subject6Wednesday")
        self.Subject6Wednesday.setFont(font7)
        self.Subject6Wednesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject6Wednesday.setTristate(False)

        self.verticalLayout_9.addWidget(self.Subject6Wednesday)

        self.Subject6Thursday = QCheckBox(self.SubjectDays_6)
        self.Subject6Thursday.setObjectName(u"Subject6Thursday")
        self.Subject6Thursday.setFont(font7)
        self.Subject6Thursday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject6Thursday.setTristate(False)

        self.verticalLayout_9.addWidget(self.Subject6Thursday)

        self.Subject6Friday = QCheckBox(self.SubjectDays_6)
        self.Subject6Friday.setObjectName(u"Subject6Friday")
        self.Subject6Friday.setFont(font7)
        self.Subject6Friday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject6Friday.setTristate(False)

        self.verticalLayout_9.addWidget(self.Subject6Friday)

        self.Subject6Saturday = QCheckBox(self.SubjectDays_6)
        self.Subject6Saturday.setObjectName(u"Subject6Saturday")
        self.Subject6Saturday.setFont(font7)
        self.Subject6Saturday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject6Saturday.setTristate(False)

        self.verticalLayout_9.addWidget(self.Subject6Saturday)

        self.SubjectDays_7 = QFrame(self.frame)
        self.SubjectDays_7.setObjectName(u"SubjectDays_7")
        self.SubjectDays_7.setGeometry(QRect(670, 170, 118, 233))
        self.SubjectDays_7.setFrameShape(QFrame.StyledPanel)
        self.SubjectDays_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.SubjectDays_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.Subject7DaysHeading = QLabel(self.SubjectDays_7)
        self.Subject7DaysHeading.setObjectName(u"Subject7DaysHeading")
        self.Subject7DaysHeading.setFont(font6)
        self.Subject7DaysHeading.setStyleSheet(u"QLabel{\n"
"	\n"
"color: rgb(241, 44, 172);\n"
"border-radius:10px;\n"
"\n"
"}")
        self.Subject7DaysHeading.setMidLineWidth(4)
        self.Subject7DaysHeading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.Subject7DaysHeading)

        self.Subject7Sunday = QCheckBox(self.SubjectDays_7)
        self.Subject7Sunday.setObjectName(u"Subject7Sunday")
        self.Subject7Sunday.setFont(font7)
        self.Subject7Sunday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject7Sunday.setTristate(False)

        self.verticalLayout_10.addWidget(self.Subject7Sunday)

        self.Subject7Monday = QCheckBox(self.SubjectDays_7)
        self.Subject7Monday.setObjectName(u"Subject7Monday")
        self.Subject7Monday.setFont(font7)
        self.Subject7Monday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject7Monday.setTristate(False)

        self.verticalLayout_10.addWidget(self.Subject7Monday)

        self.Subject7Tuesday = QCheckBox(self.SubjectDays_7)
        self.Subject7Tuesday.setObjectName(u"Subject7Tuesday")
        self.Subject7Tuesday.setFont(font7)
        self.Subject7Tuesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject7Tuesday.setTristate(False)

        self.verticalLayout_10.addWidget(self.Subject7Tuesday)

        self.Subject7Wednesday = QCheckBox(self.SubjectDays_7)
        self.Subject7Wednesday.setObjectName(u"Subject7Wednesday")
        self.Subject7Wednesday.setFont(font7)
        self.Subject7Wednesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject7Wednesday.setTristate(False)

        self.verticalLayout_10.addWidget(self.Subject7Wednesday)

        self.Subject7Thursday = QCheckBox(self.SubjectDays_7)
        self.Subject7Thursday.setObjectName(u"Subject7Thursday")
        self.Subject7Thursday.setFont(font7)
        self.Subject7Thursday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject7Thursday.setTristate(False)

        self.verticalLayout_10.addWidget(self.Subject7Thursday)

        self.Subject7Friday = QCheckBox(self.SubjectDays_7)
        self.Subject7Friday.setObjectName(u"Subject7Friday")
        self.Subject7Friday.setFont(font7)
        self.Subject7Friday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject7Friday.setTristate(False)

        self.verticalLayout_10.addWidget(self.Subject7Friday)

        self.Subject7Saturday = QCheckBox(self.SubjectDays_7)
        self.Subject7Saturday.setObjectName(u"Subject7Saturday")
        self.Subject7Saturday.setFont(font7)
        self.Subject7Saturday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject7Saturday.setTristate(False)

        self.verticalLayout_10.addWidget(self.Subject7Saturday)

        self.SubjectDays_8 = QFrame(self.frame)
        self.SubjectDays_8.setObjectName(u"SubjectDays_8")
        self.SubjectDays_8.setGeometry(QRect(670, 170, 118, 233))
        self.SubjectDays_8.setFrameShape(QFrame.StyledPanel)
        self.SubjectDays_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.SubjectDays_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.Subject8DaysHeading = QLabel(self.SubjectDays_8)
        self.Subject8DaysHeading.setObjectName(u"Subject8DaysHeading")
        self.Subject8DaysHeading.setFont(font6)
        self.Subject8DaysHeading.setStyleSheet(u"QLabel{\n"
"	\n"
"color: rgb(241, 44, 172);\n"
"border-radius:10px;\n"
"\n"
"}")
        self.Subject8DaysHeading.setMidLineWidth(4)
        self.Subject8DaysHeading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.Subject8DaysHeading)

        self.Subject8Sunday = QCheckBox(self.SubjectDays_8)
        self.Subject8Sunday.setObjectName(u"Subject8Sunday")
        self.Subject8Sunday.setFont(font7)
        self.Subject8Sunday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject8Sunday.setTristate(False)

        self.verticalLayout_11.addWidget(self.Subject8Sunday)

        self.Subject8Monday = QCheckBox(self.SubjectDays_8)
        self.Subject8Monday.setObjectName(u"Subject8Monday")
        self.Subject8Monday.setFont(font7)
        self.Subject8Monday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject8Monday.setTristate(False)

        self.verticalLayout_11.addWidget(self.Subject8Monday)

        self.Subject8Tuesday = QCheckBox(self.SubjectDays_8)
        self.Subject8Tuesday.setObjectName(u"Subject8Tuesday")
        self.Subject8Tuesday.setFont(font7)
        self.Subject8Tuesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject8Tuesday.setTristate(False)

        self.verticalLayout_11.addWidget(self.Subject8Tuesday)

        self.Subject8Wednesday = QCheckBox(self.SubjectDays_8)
        self.Subject8Wednesday.setObjectName(u"Subject8Wednesday")
        self.Subject8Wednesday.setFont(font7)
        self.Subject8Wednesday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject8Wednesday.setTristate(False)

        self.verticalLayout_11.addWidget(self.Subject8Wednesday)

        self.Subject8Thursday = QCheckBox(self.SubjectDays_8)
        self.Subject8Thursday.setObjectName(u"Subject8Thursday")
        self.Subject8Thursday.setFont(font7)
        self.Subject8Thursday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject8Thursday.setTristate(False)

        self.verticalLayout_11.addWidget(self.Subject8Thursday)

        self.Subject8Friday = QCheckBox(self.SubjectDays_8)
        self.Subject8Friday.setObjectName(u"Subject8Friday")
        self.Subject8Friday.setFont(font7)
        self.Subject8Friday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject8Friday.setTristate(False)

        self.verticalLayout_11.addWidget(self.Subject8Friday)

        self.Subject8Saturday = QCheckBox(self.SubjectDays_8)
        self.Subject8Saturday.setObjectName(u"Subject8Saturday")
        self.Subject8Saturday.setFont(font7)
        self.Subject8Saturday.setStyleSheet(u"QCheckBox{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Subject8Saturday.setTristate(False)

        self.verticalLayout_11.addWidget(self.Subject8Saturday)

        self.Description_2 = QLabel(self.frame)
        self.Description_2.setObjectName(u"Description_2")
        self.Description_2.setGeometry(QRect(260, 110, 291, 21))
        font9 = QFont()
        font9.setFamily(u"Segoe UI Semibold")
        font9.setPointSize(10)
        font9.setBold(True)
        font9.setWeight(75)
        self.Description_2.setFont(font9)
        self.Description_2.setLayoutDirection(Qt.LeftToRight)
        self.Description_2.setAutoFillBackground(False)
        self.Description_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(242, 255, 29, 255), stop:1 rgba(67, 201, 0, 255));")
        self.Description_2.setTextFormat(Qt.RichText)
        self.Description_2.setScaledContents(False)
        self.Description_2.setAlignment(Qt.AlignCenter)
        self.GoBackButton = QPushButton(self.frame)
        self.GoBackButton.setObjectName(u"GoBackButton")
        self.GoBackButton.setGeometry(QRect(10, 10, 71, 31))
        self.GoBackButton.setFont(font)
        self.GoBackButton.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(206, 103, 12, 255), stop:1 rgba(38, 165, 208, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(232, 154, 0, 255), stop:1 rgba(255, 102, 25, 255));\n"
"}")
        AfterLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(AfterLogin)

        QMetaObject.connectSlotsByName(AfterLogin)
    # setupUi

    def retranslateUi(self, AfterLogin):
        AfterLogin.setWindowTitle(QCoreApplication.translate("AfterLogin", u"DataCollection", None))
        self.label.setText("")
        self.NextButton.setText(QCoreApplication.translate("AfterLogin", u"Next", None))
#if QT_CONFIG(shortcut)
        self.NextButton.setShortcut(QCoreApplication.translate("AfterLogin", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.CloseButton.setText(QCoreApplication.translate("AfterLogin", u" X", None))
        self.Heading.setText(QCoreApplication.translate("AfterLogin", u"Getting Your Meeting Details...", None))
        self.Description.setText(QCoreApplication.translate("AfterLogin", u"  Fill Your Meeting Links And Their Time So That We Can Manage Them For You ", None))
        self.Subject_Link_1.setPlaceholderText(QCoreApplication.translate("AfterLogin", u"Enter the Meeting Link", None))
        self.label_2.setText(QCoreApplication.translate("AfterLogin", u"TO", None))
        self.label_3.setText(QCoreApplication.translate("AfterLogin", u"TO", None))
        self.label_4.setText(QCoreApplication.translate("AfterLogin", u"TO", None))
        self.label_5.setText(QCoreApplication.translate("AfterLogin", u"TO", None))
        self.label_6.setText(QCoreApplication.translate("AfterLogin", u"TO", None))
        self.label_7.setText(QCoreApplication.translate("AfterLogin", u"TO", None))
        self.label_8.setText(QCoreApplication.translate("AfterLogin", u"TO", None))
        self.Subject_1.setText("")
        self.Subject_1.setPlaceholderText(QCoreApplication.translate("AfterLogin", u"Enter Subject", None))
        self.Subject_2.setText("")
        self.Subject_2.setPlaceholderText(QCoreApplication.translate("AfterLogin", u"Enter Subject", None))
        self.Subject_3.setText("")
        self.Subject_3.setPlaceholderText(QCoreApplication.translate("AfterLogin", u"Enter Subject", None))
        self.Subject_4.setText("")
        self.Subject_4.setPlaceholderText(QCoreApplication.translate("AfterLogin", u"Enter Subject", None))
        self.Subject_5.setText("")
        self.Subject_5.setPlaceholderText(QCoreApplication.translate("AfterLogin", u"Enter Subject", None))
        self.Subject_6.setText("")
        self.Subject_6.setPlaceholderText(QCoreApplication.translate("AfterLogin", u"Enter Subject", None))
        self.Subject_7.setText("")
        self.Subject_7.setPlaceholderText(QCoreApplication.translate("AfterLogin", u"Enter Subject", None))
        self.Subject_Link_2.setPlaceholderText(QCoreApplication.translate("AfterLogin", u"Enter the Meeting Link", None))
        self.Subject_Link_3.setPlaceholderText(QCoreApplication.translate("AfterLogin", u"Enter the Meeting Link", None))
        self.Subject_Link_4.setPlaceholderText(QCoreApplication.translate("AfterLogin", u"Enter the Meeting Link", None))
        self.Subject_Link_5.setPlaceholderText(QCoreApplication.translate("AfterLogin", u"Enter the Meeting Link", None))
        self.Subject_Link_6.setPlaceholderText(QCoreApplication.translate("AfterLogin", u"Enter the Meeting Link", None))
        self.Subject_Link_7.setPlaceholderText(QCoreApplication.translate("AfterLogin", u"Enter the Meeting Link", None))
        self.Subject_8.setText("")
        self.Subject_8.setPlaceholderText(QCoreApplication.translate("AfterLogin", u"Enter Subject", None))
        self.Subject_Link_8.setPlaceholderText(QCoreApplication.translate("AfterLogin", u"Enter the Meeting Link", None))
        self.label_9.setText(QCoreApplication.translate("AfterLogin", u"TO", None))
        self.Subject1DaysHeading.setText(QCoreApplication.translate("AfterLogin", u"Days 1", None))
        self.Subject1Sunday.setText(QCoreApplication.translate("AfterLogin", u"Sun", None))
        self.Subject1Monday.setText(QCoreApplication.translate("AfterLogin", u"Mon", None))
        self.Subject1Tuesday.setText(QCoreApplication.translate("AfterLogin", u"Tue", None))
        self.Subject1Wednesday.setText(QCoreApplication.translate("AfterLogin", u"Wed", None))
        self.Subject1Thursday.setText(QCoreApplication.translate("AfterLogin", u"Thu", None))
        self.Subject1Friday.setText(QCoreApplication.translate("AfterLogin", u"Fri", None))
        self.Subject1Saturday.setText(QCoreApplication.translate("AfterLogin", u"Sat", None))
        self.SubjectsDaysBtn.setText(QCoreApplication.translate("AfterLogin", u"Days", None))
#if QT_CONFIG(shortcut)
        self.SubjectsDaysBtn.setShortcut(QCoreApplication.translate("AfterLogin", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_2.setText(QCoreApplication.translate("AfterLogin", u"Days", None))
#if QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_2.setShortcut(QCoreApplication.translate("AfterLogin", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_3.setText(QCoreApplication.translate("AfterLogin", u"Days", None))
#if QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_3.setShortcut(QCoreApplication.translate("AfterLogin", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_4.setText(QCoreApplication.translate("AfterLogin", u"Days", None))
#if QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_4.setShortcut(QCoreApplication.translate("AfterLogin", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_5.setText(QCoreApplication.translate("AfterLogin", u"Days", None))
#if QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_5.setShortcut(QCoreApplication.translate("AfterLogin", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_6.setText(QCoreApplication.translate("AfterLogin", u"Days", None))
#if QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_6.setShortcut(QCoreApplication.translate("AfterLogin", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_7.setText(QCoreApplication.translate("AfterLogin", u"Days", None))
#if QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_7.setShortcut(QCoreApplication.translate("AfterLogin", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_8.setText(QCoreApplication.translate("AfterLogin", u"Days", None))
#if QT_CONFIG(shortcut)
        self.SubjectsDaysBtn_8.setShortcut(QCoreApplication.translate("AfterLogin", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.Subject2DaysHeading.setText(QCoreApplication.translate("AfterLogin", u"Days 2", None))
        self.Subject2Sunday.setText(QCoreApplication.translate("AfterLogin", u"Sun", None))
        self.Subject2Monday.setText(QCoreApplication.translate("AfterLogin", u"Mon", None))
        self.Subject2Tuesday.setText(QCoreApplication.translate("AfterLogin", u"Tue", None))
        self.Subject2Wednesday.setText(QCoreApplication.translate("AfterLogin", u"Wed", None))
        self.Subject2Thursday.setText(QCoreApplication.translate("AfterLogin", u"Thu", None))
        self.Subject2Friday.setText(QCoreApplication.translate("AfterLogin", u"Fri", None))
        self.Subject2Saturday.setText(QCoreApplication.translate("AfterLogin", u"Sat", None))
        self.Subject3DaysHeading.setText(QCoreApplication.translate("AfterLogin", u"Days 3", None))
        self.Subject3Sunday.setText(QCoreApplication.translate("AfterLogin", u"Sun", None))
        self.Subject3Monday.setText(QCoreApplication.translate("AfterLogin", u"Mon", None))
        self.Subject3Tuesday.setText(QCoreApplication.translate("AfterLogin", u"Tue", None))
        self.Subject3Wednesday.setText(QCoreApplication.translate("AfterLogin", u"Wed", None))
        self.Subject3Thursday.setText(QCoreApplication.translate("AfterLogin", u"Thu", None))
        self.Subject3Friday.setText(QCoreApplication.translate("AfterLogin", u"Fri", None))
        self.Subject3Saturday.setText(QCoreApplication.translate("AfterLogin", u"Sat", None))
        self.Subject4DaysHeading.setText(QCoreApplication.translate("AfterLogin", u"Days 4", None))
        self.Subject4Sunday.setText(QCoreApplication.translate("AfterLogin", u"Sun", None))
        self.Subject4Monday.setText(QCoreApplication.translate("AfterLogin", u"Mon", None))
        self.Subject4Tuesday.setText(QCoreApplication.translate("AfterLogin", u"Tue", None))
        self.Subject4Wednesday.setText(QCoreApplication.translate("AfterLogin", u"Wed", None))
        self.Subject4Thursday.setText(QCoreApplication.translate("AfterLogin", u"Thu", None))
        self.Subject4Friday.setText(QCoreApplication.translate("AfterLogin", u"Fri", None))
        self.Subject4Saturday.setText(QCoreApplication.translate("AfterLogin", u"Sat", None))
        self.Subject5DaysHeading.setText(QCoreApplication.translate("AfterLogin", u"Days 5", None))
        self.Subject5Sunday.setText(QCoreApplication.translate("AfterLogin", u"Sun", None))
        self.Subject5Monday.setText(QCoreApplication.translate("AfterLogin", u"Mon", None))
        self.Subjcet5Tuesday.setText(QCoreApplication.translate("AfterLogin", u"Tue", None))
        self.Subject5Wednesday.setText(QCoreApplication.translate("AfterLogin", u"Wed", None))
        self.Subject5Thursday.setText(QCoreApplication.translate("AfterLogin", u"Thu", None))
        self.Subject5Friday.setText(QCoreApplication.translate("AfterLogin", u"Fri", None))
        self.Subject5Saturday.setText(QCoreApplication.translate("AfterLogin", u"Sat", None))
        self.Subject6DaysHeading.setText(QCoreApplication.translate("AfterLogin", u"Days 6", None))
        self.Subject6Sunday.setText(QCoreApplication.translate("AfterLogin", u"Sun", None))
        self.Subject6Monday.setText(QCoreApplication.translate("AfterLogin", u"Mon", None))
        self.Subject6Tuesday.setText(QCoreApplication.translate("AfterLogin", u"Tue", None))
        self.Subject6Wednesday.setText(QCoreApplication.translate("AfterLogin", u"Wed", None))
        self.Subject6Thursday.setText(QCoreApplication.translate("AfterLogin", u"Thu", None))
        self.Subject6Friday.setText(QCoreApplication.translate("AfterLogin", u"Fri", None))
        self.Subject6Saturday.setText(QCoreApplication.translate("AfterLogin", u"Sat", None))
        self.Subject7DaysHeading.setText(QCoreApplication.translate("AfterLogin", u"Days 7", None))
        self.Subject7Sunday.setText(QCoreApplication.translate("AfterLogin", u"Sun", None))
        self.Subject7Monday.setText(QCoreApplication.translate("AfterLogin", u"Mon", None))
        self.Subject7Tuesday.setText(QCoreApplication.translate("AfterLogin", u"Tue", None))
        self.Subject7Wednesday.setText(QCoreApplication.translate("AfterLogin", u"Wed", None))
        self.Subject7Thursday.setText(QCoreApplication.translate("AfterLogin", u"Thu", None))
        self.Subject7Friday.setText(QCoreApplication.translate("AfterLogin", u"Fri", None))
        self.Subject7Saturday.setText(QCoreApplication.translate("AfterLogin", u"Sat", None))
        self.Subject8DaysHeading.setText(QCoreApplication.translate("AfterLogin", u"Days 8", None))
        self.Subject8Sunday.setText(QCoreApplication.translate("AfterLogin", u"Sun", None))
        self.Subject8Monday.setText(QCoreApplication.translate("AfterLogin", u"Mon", None))
        self.Subject8Tuesday.setText(QCoreApplication.translate("AfterLogin", u"Tue", None))
        self.Subject8Wednesday.setText(QCoreApplication.translate("AfterLogin", u"Wed", None))
        self.Subject8Thursday.setText(QCoreApplication.translate("AfterLogin", u"Thu", None))
        self.Subject8Friday.setText(QCoreApplication.translate("AfterLogin", u"Fri", None))
        self.Subject8Saturday.setText(QCoreApplication.translate("AfterLogin", u"Sat", None))
        self.Description_2.setText(QCoreApplication.translate("AfterLogin", u"Leave Subjects Empty If You Don't Need Them", None))
        self.GoBackButton.setText(QCoreApplication.translate("AfterLogin", u"Go Back", None))
#if QT_CONFIG(shortcut)
        self.GoBackButton.setShortcut(QCoreApplication.translate("AfterLogin", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

