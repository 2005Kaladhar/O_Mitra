# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'regularstartpagecqpfZS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RegularWindow(object):
    def setupUi(self, RegularWindow):
        if not RegularWindow.objectName():
            RegularWindow.setObjectName(u"RegularWindow")
        RegularWindow.resize(811, 502)
        RegularWindow.setMinimumSize(QSize(811, 502))
        RegularWindow.setMaximumSize(QSize(811, 502))
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        RegularWindow.setWindowIcon(icon)
        RegularWindow.setStyleSheet(u"QMainWindow{\n"
"\n"
"}\n"
"\n"
"QMainWindow::hover{\n"
"\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 215), stop:1 rgba(11, 15, 50, 194));\n"
"}")
        self.centralwidget = QWidget(RegularWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 831, 511))
        self.label.setPixmap(QPixmap(u"25864037242020b0c4a5baed125bad00-700.jpg"))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 811, 502))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 131), stop:1 rgba(0, 0, 0, 97));\n"
"	\n"
"	border-radius:10px;\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.StartButtonsecond = QPushButton(self.frame)
        self.StartButtonsecond.setObjectName(u"StartButtonsecond")
        self.StartButtonsecond.setGeometry(QRect(670, 450, 111, 31))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.StartButtonsecond.setFont(font)
        self.StartButtonsecond.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.653, x2:1, y2:0.631, stop:0 rgba(255, 0, 255, 255), stop:1 rgba(166, 43, 200, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(75, 200, 100);\n"
"\n"
"}")
        self.Heading = QLabel(self.frame)
        self.Heading.setObjectName(u"Heading")
        self.Heading.setGeometry(QRect(170, 0, 471, 41))
        font1 = QFont()
        font1.setPointSize(24)
        self.Heading.setFont(font1)
        self.Heading.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(84, 15, 60);\n"
"border-radius:10px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(93, 0, 86, 122), stop:1 rgba(241, 0, 31, 90));\n"
"}")
        self.Heading.setMidLineWidth(4)
        self.Heading.setAlignment(Qt.AlignCenter)
        self.Description = QLabel(self.frame)
        self.Description.setObjectName(u"Description")
        self.Description.setGeometry(QRect(130, 160, 571, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.Description.setFont(font2)
        self.Description.setLayoutDirection(Qt.LeftToRight)
        self.Description.setAutoFillBackground(False)
        self.Description.setStyleSheet(u"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00568182 rgba(116, 255, 54, 136), stop:1 rgba(255, 170, 0, 135));")
        self.Description.setTextFormat(Qt.RichText)
        self.Description.setScaledContents(False)
        self.Description.setAlignment(Qt.AlignCenter)
        self.AddUrgentMeeting = QPushButton(self.frame)
        self.AddUrgentMeeting.setObjectName(u"AddUrgentMeeting")
        self.AddUrgentMeeting.setGeometry(QRect(600, 240, 131, 23))
        font3 = QFont()
        font3.setPointSize(11)
        self.AddUrgentMeeting.setFont(font3)
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
        self.UrgentMeeting = QLineEdit(self.frame)
        self.UrgentMeeting.setObjectName(u"UrgentMeeting")
        self.UrgentMeeting.setGeometry(QRect(560, 270, 191, 21))
        font4 = QFont()
        font4.setPointSize(9)
        self.UrgentMeeting.setFont(font4)
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
        self.ChangeEmailPass = QPushButton(self.frame)
        self.ChangeEmailPass.setObjectName(u"ChangeEmailPass")
        self.ChangeEmailPass.setGeometry(QRect(30, 310, 181, 31))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setWeight(50)
        self.ChangeEmailPass.setFont(font5)
        self.ChangeEmailPass.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.653, x2:1, y2:0.631, stop:0 rgba(255, 0, 255, 255), stop:1 rgba(166, 43, 200, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(75, 200, 100);\n"
"\n"
"}")
        self.ContactDeveloper = QPushButton(self.frame)
        self.ContactDeveloper.setObjectName(u"ContactDeveloper")
        self.ContactDeveloper.setGeometry(QRect(30, 390, 131, 31))
        self.ContactDeveloper.setFont(font5)
        self.ContactDeveloper.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.653, x2:1, y2:0.631, stop:0 rgba(255, 0, 255, 255), stop:1 rgba(166, 43, 200, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(75, 200, 100);\n"
"\n"
"}")
        self.ClearSavedData = QPushButton(self.frame)
        self.ClearSavedData.setObjectName(u"ClearSavedData")
        self.ClearSavedData.setGeometry(QRect(30, 350, 131, 31))
        self.ClearSavedData.setFont(font5)
        self.ClearSavedData.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.653, x2:1, y2:0.631, stop:0 rgba(255, 0, 255, 255), stop:1 rgba(166, 43, 200, 255));\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(75, 200, 100);\n"
"\n"
"}")
        self.Title = QLabel(self.frame)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(330, 50, 171, 61))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(36)
        font6.setBold(False)
        font6.setWeight(50)
        self.Title.setFont(font6)
        self.Title.setLayoutDirection(Qt.LeftToRight)
        self.Title.setAutoFillBackground(False)
        self.Title.setStyleSheet(u"QLabel{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"\n"
"}")
        self.Title.setTextFormat(Qt.RichText)
        self.Title.setScaledContents(False)
        self.Credits = QLabel(self.frame)
        self.Credits.setObjectName(u"Credits")
        self.Credits.setGeometry(QRect(320, 460, 131, 31))
        font7 = QFont()
        font7.setFamily(u"Segoe UI Semibold")
        font7.setPointSize(8)
        font7.setBold(True)
        font7.setWeight(75)
        self.Credits.setFont(font7)
        self.Credits.setLayoutDirection(Qt.LeftToRight)
        self.Credits.setAutoFillBackground(False)
        self.Credits.setStyleSheet(u"color: rgb(149, 149, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.Credits.setTextFormat(Qt.PlainText)
        self.Credits.setScaledContents(False)
        self.Description_2 = QLabel(self.frame)
        self.Description_2.setObjectName(u"Description_2")
        self.Description_2.setGeometry(QRect(180, 110, 461, 41))
        font8 = QFont()
        font8.setFamily(u"Segoe UI Semibold")
        font8.setPointSize(14)
        font8.setBold(True)
        font8.setWeight(75)
        self.Description_2.setFont(font8)
        self.Description_2.setLayoutDirection(Qt.LeftToRight)
        self.Description_2.setAutoFillBackground(False)
        self.Description_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(93, 0, 86, 122), stop:1 rgba(241, 0, 31, 90));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(93, 0, 86, 122), stop:1 rgba(241, 0, 31, 90));")
        self.Description_2.setTextFormat(Qt.RichText)
        self.Description_2.setScaledContents(False)
        self.Description_2.setAlignment(Qt.AlignCenter)
        self.StartButtonMain = QPushButton(self.frame)
        self.StartButtonMain.setObjectName(u"StartButtonMain")
        self.StartButtonMain.setGeometry(QRect(250, 300, 261, 101))
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(26)
        font9.setBold(False)
        font9.setWeight(50)
        self.StartButtonMain.setFont(font9)
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
        self.Time = QLabel(self.frame)
        self.Time.setObjectName(u"Time")
        self.Time.setGeometry(QRect(220, 220, 311, 61))
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(18)
        font10.setBold(False)
        font10.setWeight(50)
        self.Time.setFont(font10)
        self.Time.setLayoutDirection(Qt.LeftToRight)
        self.Time.setAutoFillBackground(False)
        self.Time.setStyleSheet(u"QLabel{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"}")
        self.Time.setTextFormat(Qt.RichText)
        self.Time.setScaledContents(False)
        self.Time.setAlignment(Qt.AlignCenter)
        self.CloseButton = QPushButton(self.frame)
        self.CloseButton.setObjectName(u"CloseButton")
        self.CloseButton.setGeometry(QRect(760, 0, 51, 21))
        font11 = QFont()
        font11.setBold(True)
        font11.setWeight(75)
        self.CloseButton.setFont(font11)
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
        self.UrgentMeetingStartBtn = QPushButton(self.frame)
        self.UrgentMeetingStartBtn.setObjectName(u"UrgentMeetingStartBtn")
        self.UrgentMeetingStartBtn.setGeometry(QRect(590, 300, 131, 23))
        font12 = QFont()
        font12.setPointSize(10)
        self.UrgentMeetingStartBtn.setFont(font12)
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
        self.DeleteAllAlertFrame = QFrame(self.frame)
        self.DeleteAllAlertFrame.setObjectName(u"DeleteAllAlertFrame")
        self.DeleteAllAlertFrame.setGeometry(QRect(0, 140, 811, 361))
        self.DeleteAllAlertFrame.setFrameShape(QFrame.StyledPanel)
        self.DeleteAllAlertFrame.setFrameShadow(QFrame.Raised)
        self.DeleteMessage = QLabel(self.DeleteAllAlertFrame)
        self.DeleteMessage.setObjectName(u"DeleteMessage")
        self.DeleteMessage.setGeometry(QRect(20, 20, 771, 321))
        font13 = QFont()
        font13.setPointSize(12)
        self.DeleteMessage.setFont(font13)
        self.DeleteMessage.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.71, x2:1, y2:0.670636, stop:0 rgba(0, 0, 0, 190), stop:1 rgba(13, 13, 13, 187));\n"
"\n"
"}")
        self.DeleteMessage.setAlignment(Qt.AlignCenter)
        self.YesDelete = QPushButton(self.DeleteAllAlertFrame)
        self.YesDelete.setObjectName(u"YesDelete")
        self.YesDelete.setGeometry(QRect(310, 220, 91, 23))
        self.YesDelete.setFont(font3)
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
        self.NoDelete = QPushButton(self.DeleteAllAlertFrame)
        self.NoDelete.setObjectName(u"NoDelete")
        self.NoDelete.setGeometry(QRect(420, 220, 91, 23))
        self.NoDelete.setFont(font3)
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
        self.UrgentLinkAlert = QFrame(self.frame)
        self.UrgentLinkAlert.setObjectName(u"UrgentLinkAlert")
        self.UrgentLinkAlert.setGeometry(QRect(50, 260, 721, 81))
        self.UrgentLinkAlert.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 215), stop:1 rgba(11, 15, 50, 194));")
        self.UrgentLinkAlert.setFrameShape(QFrame.StyledPanel)
        self.UrgentLinkAlert.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.UrgentLinkAlert)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 30, 421, 31))
        self.label_2.setFont(font13)
        self.label_2.setStyleSheet(u"QLabel{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.UrgentLinkClose = QPushButton(self.UrgentLinkAlert)
        self.UrgentLinkClose.setObjectName(u"UrgentLinkClose")
        self.UrgentLinkClose.setGeometry(QRect(550, 30, 41, 31))
        self.UrgentLinkClose.setFont(font11)
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
        self.StartButtonsecond.raise_()
        self.Heading.raise_()
        self.Description.raise_()
        self.AddUrgentMeeting.raise_()
        self.UrgentMeeting.raise_()
        self.ChangeEmailPass.raise_()
        self.ContactDeveloper.raise_()
        self.ClearSavedData.raise_()
        self.Title.raise_()
        self.Credits.raise_()
        self.Description_2.raise_()
        self.StartButtonMain.raise_()
        self.Time.raise_()
        self.CloseButton.raise_()
        self.UrgentMeetingStartBtn.raise_()
        self.UrgentLinkAlert.raise_()
        self.DeleteAllAlertFrame.raise_()
        RegularWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegularWindow)

        QMetaObject.connectSlotsByName(RegularWindow)
    # setupUi

    def retranslateUi(self, RegularWindow):
        RegularWindow.setWindowTitle(QCoreApplication.translate("RegularWindow", u"O-Mitra", None))
        self.label.setText("")
        self.StartButtonsecond.setText(QCoreApplication.translate("RegularWindow", u"Start", None))
        self.Heading.setText(QCoreApplication.translate("RegularWindow", u"Ready For Your Service...", None))
        self.Description.setText(QCoreApplication.translate("RegularWindow", u"You can Trust me, I'm here to Manage all your Meetings.", None))
        self.AddUrgentMeeting.setText(QCoreApplication.translate("RegularWindow", u"Urgent Meeting", None))
        self.UrgentMeeting.setPlaceholderText(QCoreApplication.translate("RegularWindow", u"Add a Meeting Link", None))
        self.ChangeEmailPass.setText(QCoreApplication.translate("RegularWindow", u"Change Email and Password", None))
#if QT_CONFIG(shortcut)
        self.ChangeEmailPass.setShortcut(QCoreApplication.translate("RegularWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.ContactDeveloper.setText(QCoreApplication.translate("RegularWindow", u"Contact Developer", None))
#if QT_CONFIG(shortcut)
        self.ContactDeveloper.setShortcut(QCoreApplication.translate("RegularWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.ClearSavedData.setText(QCoreApplication.translate("RegularWindow", u"Clear Saved Data", None))
#if QT_CONFIG(shortcut)
        self.ClearSavedData.setShortcut(QCoreApplication.translate("RegularWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.Title.setText(QCoreApplication.translate("RegularWindow", u"O-Mitra", None))
        self.Credits.setText(QCoreApplication.translate("RegularWindow", u"Created: Kaladhar Gopal ", None))
        self.Description_2.setText(QCoreApplication.translate("RegularWindow", u"Online Meetings Manager In Tiny Robust Application", None))
        self.StartButtonMain.setText(QCoreApplication.translate("RegularWindow", u"Start", None))
#if QT_CONFIG(shortcut)
        self.StartButtonMain.setShortcut(QCoreApplication.translate("RegularWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.Time.setText("")
        self.CloseButton.setText(QCoreApplication.translate("RegularWindow", u" X", None))
        self.UrgentMeetingStartBtn.setText(QCoreApplication.translate("RegularWindow", u"Start Urgent Meeting", None))
        self.DeleteMessage.setText(QCoreApplication.translate("RegularWindow", u"Do You Really Want to Delete All Your Saved Data ? ", None))
        self.YesDelete.setText(QCoreApplication.translate("RegularWindow", u"Yes ", None))
        self.NoDelete.setText(QCoreApplication.translate("RegularWindow", u"No", None))
        self.label_2.setText(QCoreApplication.translate("RegularWindow", u"Please Provide A Valid Link For THe Meeting...", None))
        self.UrgentLinkClose.setText(QCoreApplication.translate("RegularWindow", u"X", None))
    # retranslateUi

