# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appuiiFpdgD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(582, 351)
        MainWindow.setMinimumSize(QSize(582, 351))
        MainWindow.setMaximumSize(QSize(582, 351))
        MainWindow.setMouseTracking(True)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(17.998999999999999)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(582, 351))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 641, 371))
        self.label.setPixmap(QPixmap(u"magician-sorcerer-moon-night-lake-hood-cloak-magic-man-figur.jpg"))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 582, 351))
        self.frame.setMinimumSize(QSize(582, 351))
        self.frame.setMaximumSize(QSize(582, 351))
        self.frame.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 131), stop:1 rgba(0, 0, 0, 97));\n"
"	border-radius:10px;\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Title = QLabel(self.frame)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(200, 80, 191, 61))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.Title.setFont(font)
        self.Title.setLayoutDirection(Qt.LeftToRight)
        self.Title.setAutoFillBackground(False)
        self.Title.setStyleSheet(u"QLabel{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(241, 44, 172);\n"
"border-radius:10px;\n"
"\n"
"}")
        self.Title.setTextFormat(Qt.RichText)
        self.Title.setScaledContents(False)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 200, 501, 23))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	border-radius:10px;\n"
"	background-color: rgb(114, 121, 217);\n"
"	border-style:none;\n"
"	text-align:centre;	\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius:10px;\n"
"	text-align:centre;\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.653, x2:1, y2:0.631, stop:0 rgba(255, 0, 255, 255), stop:1 rgba(166, 43, 200, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.Description = QLabel(self.frame)
        self.Description.setObjectName(u"Description")
        self.Description.setGeometry(QRect(110, 140, 361, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.Description.setFont(font1)
        self.Description.setLayoutDirection(Qt.LeftToRight)
        self.Description.setAutoFillBackground(False)
        self.Description.setStyleSheet(u"color: rgb(255, 239, 19);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.994318 rgba(255, 255, 255, 0));")
        self.Description.setTextFormat(Qt.RichText)
        self.Description.setScaledContents(False)
        self.Loading = QLabel(self.frame)
        self.Loading.setObjectName(u"Loading")
        self.Loading.setGeometry(QRect(260, 240, 51, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setWeight(75)
        self.Loading.setFont(font2)
        self.Loading.setLayoutDirection(Qt.LeftToRight)
        self.Loading.setAutoFillBackground(False)
        self.Loading.setStyleSheet(u"color: rgb(149, 149, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.Loading.setTextFormat(Qt.PlainText)
        self.Loading.setScaledContents(False)
        self.Credits = QLabel(self.frame)
        self.Credits.setObjectName(u"Credits")
        self.Credits.setGeometry(QRect(220, 300, 131, 31))
        self.Credits.setFont(font2)
        self.Credits.setLayoutDirection(Qt.LeftToRight)
        self.Credits.setAutoFillBackground(False)
        self.Credits.setStyleSheet(u"color: rgb(149, 149, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.Credits.setTextFormat(Qt.PlainText)
        self.Credits.setScaledContents(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Loading...", None))
        self.label.setText("")
        self.Title.setText(QCoreApplication.translate("MainWindow", u"O-Mitra", None))
        self.Description.setText(QCoreApplication.translate("MainWindow", u"Online Meetings Manager In Tiny Robust Application", None))
        self.Loading.setText(QCoreApplication.translate("MainWindow", u"Loding...", None))
        self.Credits.setText(QCoreApplication.translate("MainWindow", u"Created: Kaladhar Gopal ", None))
    # retranslateUi

