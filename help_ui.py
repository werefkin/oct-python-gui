# -*- coding: utf-8 -*-
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
        self.label_about = QtWidgets.QLabel(self.centralwidget)
        self.label_about.setGeometry(QtCore.QRect(130, 390, 311, 61))
        self.label_about.setMinimumSize(QtCore.QSize(0, 0))
        self.label_about.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_about.setScaledContents(True)
        self.label_about.setWordWrap(True)
        self.label_about.setObjectName("About")
        self.OKCloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.OKCloseButton.setGeometry(QtCore.QRect(330, 480, 93, 28))
        self.OKCloseButton.setObjectName("OKCloseButton")
        self.label_byme = QtWidgets.QLabel(self.centralwidget)
        self.label_byme.setGeometry(QtCore.QRect(30, 30, 401, 61))
        self.label_byme.setMinimumSize(QtCore.QSize(300, 50))
        self.label_byme.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_byme.setFont(font)
        self.label_byme.setScaledContents(True)
        self.label_byme.setWordWrap(True)
        self.label_byme.setObjectName("label_byme")
        HelpWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HelpWindow)
        QtCore.QMetaObject.connectSlotsByName(HelpWindow)

    def retranslateUi(self, HelpWindow):
        _translate = QtCore.QCoreApplication.translate
        HelpWindow.setWindowTitle(_translate("HelpWindow", "About software"))
        self.label_about.setText(_translate("HelpWindow", "Aimed for a quick integration\n in various FDOCT Systems.\n"""))
        self.OKCloseButton.setText(_translate("HelpWindow", "OK"))
        self.label_byme.setText(_translate("HelpWindow", "Developed by Ivan Zorin in the framework of PhD Project \nzorin.ial@gmail.com"))
