# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vol_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

from pyqtgraph.opengl import GLViewWidget

class Ui_VolumetricWidget(object):
    def setupUi(self, VolumetricWidget):
        if not VolumetricWidget.objectName():
            VolumetricWidget.setObjectName(u"VolumetricWidget")
        VolumetricWidget.resize(654, 577)
        self.centralwidget = QWidget(VolumetricWidget)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.CscanWidget = GLViewWidget(self.centralwidget)
        self.CscanWidget.setObjectName(u"CscanWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CscanWidget.sizePolicy().hasHeightForWidth())
        self.CscanWidget.setSizePolicy(sizePolicy)
        self.CscanWidget.setMinimumSize(QSize(640, 300))
        self.CscanWidget.setMaximumSize(QSize(16777215, 16777215))
        self.CscanWidget.setStyleSheet(u"")

        self.gridLayout.addWidget(self.CscanWidget, 1, 1, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_dr_3d = QLabel(self.groupBox)
        self.label_dr_3d.setObjectName(u"label_dr_3d")

        self.gridLayout_2.addWidget(self.label_dr_3d, 0, 0, 1, 1)

        self.ApplyRenderingButton = QPushButton(self.groupBox)
        self.ApplyRenderingButton.setObjectName(u"ApplyRenderingButton")

        self.gridLayout_2.addWidget(self.ApplyRenderingButton, 0, 3, 1, 1)

        self.label_3d_angles = QLabel(self.groupBox)
        self.label_3d_angles.setObjectName(u"label_3d_angles")

        self.gridLayout_2.addWidget(self.label_3d_angles, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_azi = QLabel(self.groupBox)
        self.label_azi.setObjectName(u"label_azi")

        self.horizontalLayout_6.addWidget(self.label_azi)

        self.x_angle_ui = QLineEdit(self.groupBox)
        self.x_angle_ui.setObjectName(u"x_angle_ui")

        self.horizontalLayout_6.addWidget(self.x_angle_ui)

        self.label_ele = QLabel(self.groupBox)
        self.label_ele.setObjectName(u"label_ele")

        self.horizontalLayout_6.addWidget(self.label_ele)

        self.y_angle_ui = QLineEdit(self.groupBox)
        self.y_angle_ui.setObjectName(u"y_angle_ui")

        self.horizontalLayout_6.addWidget(self.y_angle_ui)

        self.label_distance = QLabel(self.groupBox)
        self.label_distance.setObjectName(u"label_distance")

        self.horizontalLayout_6.addWidget(self.label_distance)

        self.distance_ui = QLineEdit(self.groupBox)
        self.distance_ui.setObjectName(u"distance_ui")

        self.horizontalLayout_6.addWidget(self.distance_ui)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)

        self.log10_coef_3d_ui = QLineEdit(self.groupBox)
        self.log10_coef_3d_ui.setObjectName(u"log10_coef_3d_ui")

        self.gridLayout_2.addWidget(self.log10_coef_3d_ui, 0, 1, 1, 1)

        self.SetAnglesButton = QPushButton(self.groupBox)
        self.SetAnglesButton.setObjectName(u"SetAnglesButton")

        self.gridLayout_2.addWidget(self.SetAnglesButton, 1, 3, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 2, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        VolumetricWidget.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(VolumetricWidget)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 654, 18))
        VolumetricWidget.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(VolumetricWidget)
        self.statusbar.setObjectName(u"statusbar")
        VolumetricWidget.setStatusBar(self.statusbar)

        self.retranslateUi(VolumetricWidget)

        QMetaObject.connectSlotsByName(VolumetricWidget)
    # setupUi

    def retranslateUi(self, VolumetricWidget):
        VolumetricWidget.setWindowTitle(QCoreApplication.translate("VolumetricWidget", u"C-scan Volume Viewer", None))
        self.groupBox.setTitle(QCoreApplication.translate("VolumetricWidget", u"Rendering parameters", None))
        self.label_dr_3d.setText(QCoreApplication.translate("VolumetricWidget", u"Dynamic range offset", None))
        self.ApplyRenderingButton.setText(QCoreApplication.translate("VolumetricWidget", u"Apply", None))
        self.label_3d_angles.setText(QCoreApplication.translate("VolumetricWidget", u"Positioning", None))
        self.label_azi.setText(QCoreApplication.translate("VolumetricWidget", u"Azimuth", None))
        self.x_angle_ui.setText(QCoreApplication.translate("VolumetricWidget", u"-60", None))
        self.label_ele.setText(QCoreApplication.translate("VolumetricWidget", u"Elevation", None))
        self.y_angle_ui.setText(QCoreApplication.translate("VolumetricWidget", u"-55", None))
        self.label_distance.setText(QCoreApplication.translate("VolumetricWidget", u"Distance", None))
        self.distance_ui.setText(QCoreApplication.translate("VolumetricWidget", u"1000", None))
        self.log10_coef_3d_ui.setText(QCoreApplication.translate("VolumetricWidget", u"100", None))
        self.SetAnglesButton.setText(QCoreApplication.translate("VolumetricWidget", u"Set", None))
    # retranslateUi

