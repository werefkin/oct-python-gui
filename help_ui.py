# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\QT\UPD\help.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_HelpWindow(object):
    def setupUi(self, HelpWindow):
        HelpWindow.setObjectName("HelpWindow")
        HelpWindow.resize(450, 560)
        HelpWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(HelpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 390, 311, 61))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.OKCLOSE = QtWidgets.QPushButton(self.centralwidget)
        self.OKCLOSE.setGeometry(QtCore.QRect(330, 480, 93, 28))
        self.OKCLOSE.setObjectName("OKCLOSE")
        self.logo_eu = QtWidgets.QLabel(self.centralwidget)
        self.logo_eu.setGeometry(QtCore.QRect(30, 390, 91, 61))
        self.logo_eu.setText("")
        self.logo_eu.setPixmap(QtGui.QPixmap("logo/ffg.png"))
        self.logo_eu.setScaledContents(True)
        self.logo_eu.setObjectName("logo_eu")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 401, 61))
        self.label_2.setMinimumSize(QtCore.QSize(300, 50))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        HelpWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HelpWindow)
        QtCore.QMetaObject.connectSlotsByName(HelpWindow)

    def retranslateUi(self, HelpWindow):
        _translate = QtCore.QCoreApplication.translate
        HelpWindow.setWindowTitle(_translate("HelpWindow", "About software"))
        self.label.setText(_translate("HelpWindow", "The DIQACAM project aims at improving the quality of Additive Manufacturing high-performance ceramics, thereby guaranteeing the highest quality standards, by developing an at- and inline process monitoring system.\n"""))
        self.OKCLOSE.setText(_translate("HelpWindow", "OK"))
        self.label_2.setText(_translate("HelpWindow", "Developed by Ivan Zorin in the framework of the DIQACAM Project \nivan.zorin@recendt.at"))
