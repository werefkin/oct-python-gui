# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_HelpWindow(object):
    def setupUi(self, HelpWindow):
        if not HelpWindow.objectName():
            HelpWindow.setObjectName(u"HelpWindow")
        HelpWindow.resize(400, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HelpWindow.sizePolicy().hasHeightForWidth())
        HelpWindow.setSizePolicy(sizePolicy)
        HelpWindow.setMaximumSize(QSize(400, 500))
        self.centralwidget = QWidget(HelpWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(400, 500))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.main_layout = QFormLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.label_by_me = QLabel(self.centralwidget)
        self.label_by_me.setObjectName(u"label_by_me")

        self.main_layout.setWidget(0, QFormLayout.FieldRole, self.label_by_me)

        self.label_email = QLabel(self.centralwidget)
        self.label_email.setObjectName(u"label_email")

        self.main_layout.setWidget(1, QFormLayout.FieldRole, self.label_email)

        self.verticalSpacer = QSpacerItem(20, 300, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.main_layout.setItem(2, QFormLayout.FieldRole, self.verticalSpacer)

        self.label_general = QLabel(self.centralwidget)
        self.label_general.setObjectName(u"label_general")
        self.label_general.setMinimumSize(QSize(0, 50))

        self.main_layout.setWidget(3, QFormLayout.FieldRole, self.label_general)

        self.layout_aroundButton = QHBoxLayout()
        self.layout_aroundButton.setObjectName(u"layout_aroundButton")
        self.buttonSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_aroundButton.addItem(self.buttonSpacer)

        self.OKCloseButton = QPushButton(self.centralwidget)
        self.OKCloseButton.setObjectName(u"OKCloseButton")

        self.layout_aroundButton.addWidget(self.OKCloseButton)


        self.main_layout.setLayout(4, QFormLayout.FieldRole, self.layout_aroundButton)


        self.horizontalLayout.addLayout(self.main_layout)

        HelpWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HelpWindow)

        QMetaObject.connectSlotsByName(HelpWindow)
    # setupUi

    def retranslateUi(self, HelpWindow):
        HelpWindow.setWindowTitle(QCoreApplication.translate("HelpWindow", u"About software", None))
        self.label_by_me.setText(QCoreApplication.translate("HelpWindow", u"Developed by Ivan Zorin in the framework of PhD project", None))
        self.label_email.setText(QCoreApplication.translate("HelpWindow", u"contact email: zorin.ial@gmail.com", None))
        self.label_general.setText(QCoreApplication.translate("HelpWindow", u"This simple python GUI aimed at quick prototyping, experimenting \n"
" and straightforward integration into various FD-OCT systems", None))
        self.OKCloseButton.setText(QCoreApplication.translate("HelpWindow", u"OK", None))
    # retranslateUi

