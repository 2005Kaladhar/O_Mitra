# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aftersplashscreenvNkaDs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(601, 360)
        Login.setMinimumSize(QSize(601, 360))
        Login.setMaximumSize(QSize(601, 360))
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Login.setWindowIcon(icon)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 611, 381))
        self.label.setPixmap(QPixmap(u"541196-istock-668710858.jpg"))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 601, 351))
        self.frame.setMaximumSize(QSize(601, 351))
        self.frame.setStyleSheet(u"QFrame{\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 131), stop:1 rgba(0, 0, 0, 97));\n"
"	border-radius:10px;\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.NextButton = QPushButton(self.frame)
        self.NextButton.setObjectName(u"NextButton")
        self.NextButton.setGeometry(QRect(450, 320, 131, 31))
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
        self.CloseButton = QPushButton(self.frame)
        self.CloseButton.setObjectName(u"CloseButton")
        self.CloseButton.setGeometry(QRect(540, 0, 51, 21))
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
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 10, 201, 41))
        font2 = QFont()
        font2.setPointSize(24)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	\n"
"color: rgb(241, 44, 172);\n"
"border-radius:10px;\n"
"\n"
"}")
        self.label_2.setMidLineWidth(4)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.Description = QLabel(self.frame)
        self.Description.setObjectName(u"Description")
        self.Description.setGeometry(QRect(110, 80, 401, 41))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.Description.setFont(font3)
        self.Description.setLayoutDirection(Qt.LeftToRight)
        self.Description.setAutoFillBackground(False)
        self.Description.setStyleSheet(u"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));")
        self.Description.setTextFormat(Qt.RichText)
        self.Description.setScaledContents(False)
        self.Description.setAlignment(Qt.AlignCenter)
        self.Description_4 = QLabel(self.frame)
        self.Description_4.setObjectName(u"Description_4")
        self.Description_4.setGeometry(QRect(80, 271, 121, 31))
        self.Description_4.setFont(font3)
        self.Description_4.setLayoutDirection(Qt.LeftToRight)
        self.Description_4.setAutoFillBackground(False)
        self.Description_4.setStyleSheet(u"QLabel{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
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
        self.Description_5 = QLabel(self.frame)
        self.Description_5.setObjectName(u"Description_5")
        self.Description_5.setGeometry(QRect(80, 221, 121, 31))
        self.Description_5.setFont(font3)
        self.Description_5.setLayoutDirection(Qt.LeftToRight)
        self.Description_5.setAutoFillBackground(False)
        self.Description_5.setStyleSheet(u"QLabel{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
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
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 171, 121, 31))
        self.label_3.setFont(font3)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"QLabel{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(145, 223, 37, 255), stop:0.892045 rgba(255, 255, 52, 232));\n"
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
        self.MaleRadioBtn = QRadioButton(self.frame)
        self.MaleRadioBtn.setObjectName(u"MaleRadioBtn")
        self.MaleRadioBtn.setGeometry(QRect(450, 180, 101, 21))
        self.MaleRadioBtn.setLayoutDirection(Qt.LeftToRight)
        self.MaleRadioBtn.setAutoFillBackground(False)
        self.MaleRadioBtn.setStyleSheet(u"QRadioButton{\n"
"border-radius:10px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.568, x2:1, y2:0.517, stop:0 rgba(0, 115, 255, 255), stop:1 rgba(219, 179, 234, 255));\n"
"\n"
"}")
        self.MaleRadioBtn.setCheckable(True)
        self.MaleRadioBtn.setChecked(False)
        self.FemaleRadioBtn = QRadioButton(self.frame)
        self.FemaleRadioBtn.setObjectName(u"FemaleRadioBtn")
        self.FemaleRadioBtn.setGeometry(QRect(450, 210, 111, 21))
        self.FemaleRadioBtn.setStyleSheet(u"QRadioButton{\n"
"border-radius:10px;\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.568, x2:1, y2:0.517, stop:0 rgba(255, 0, 237, 255), stop:1 rgba(219, 179, 234, 255));\n"
"}")
        self.Name = QLineEdit(self.frame)
        self.Name.setObjectName(u"Name")
        self.Name.setGeometry(QRect(230, 180, 181, 21))
        font4 = QFont()
        font4.setPointSize(9)
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
        self.Email = QLineEdit(self.frame)
        self.Email.setObjectName(u"Email")
        self.Email.setGeometry(QRect(230, 230, 181, 21))
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
        self.Password = QLineEdit(self.frame)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(230, 280, 181, 21))
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
        self.NotFilledAlertFrame = QFrame(self.frame)
        self.NotFilledAlertFrame.setObjectName(u"NotFilledAlertFrame")
        self.NotFilledAlertFrame.setGeometry(QRect(80, 80, 471, 41))
        self.NotFilledAlertFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 215), stop:1 rgba(11, 15, 50, 194));\n"
"border-radius:10px;")
        self.NotFilledAlertFrame.setFrameShape(QFrame.StyledPanel)
        self.NotFilledAlertFrame.setFrameShadow(QFrame.Raised)
        self.NotFilledClose = QPushButton(self.NotFilledAlertFrame)
        self.NotFilledClose.setObjectName(u"NotFilledClose")
        self.NotFilledClose.setGeometry(QRect(440, 10, 20, 21))
        self.NotFilledClose.setFont(font1)
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
        self.NotFilledAlertText = QLabel(self.NotFilledAlertFrame)
        self.NotFilledAlertText.setObjectName(u"NotFilledAlertText")
        self.NotFilledAlertText.setGeometry(QRect(0, 0, 431, 41))
        font5 = QFont()
        font5.setPointSize(11)
        self.NotFilledAlertText.setFont(font5)
        self.NotFilledAlertText.setStyleSheet(u"QLabel{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.NotFilledAlertText.setAlignment(Qt.AlignCenter)
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.label.setText("")
        self.NextButton.setText(QCoreApplication.translate("Login", u"Next", None))
        self.CloseButton.setText(QCoreApplication.translate("Login", u" X", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"LOGIN", None))
        self.Description.setText(QCoreApplication.translate("Login", u" Your Information is required by the Automation Software", None))
        self.Description_4.setText(QCoreApplication.translate("Login", u"Password", None))
        self.Description_5.setText(QCoreApplication.translate("Login", u"E-mail", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"Name", None))
        self.MaleRadioBtn.setText(QCoreApplication.translate("Login", u"Male", None))
        self.FemaleRadioBtn.setText(QCoreApplication.translate("Login", u"Female", None))
        self.Name.setPlaceholderText(QCoreApplication.translate("Login", u"Enter Your Name", None))
        self.Email.setPlaceholderText(QCoreApplication.translate("Login", u"Enter Your Email", None))
        self.Password.setPlaceholderText(QCoreApplication.translate("Login", u"Enter Your Password", None))
        self.NotFilledClose.setText(QCoreApplication.translate("Login", u"X", None))
        self.NotFilledAlertText.setText(QCoreApplication.translate("Login", u"Please Filll All The Required Fields And Checks Correctly", None))
    # retranslateUi

