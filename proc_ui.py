# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design_gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget
from pyqtgraph import ImageView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 900)
        MainWindow.setMinimumSize(QSize(1280, 900))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"../../Users/r.zor/.designer/backup/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave.setCheckable(False)
        self.actionSave.setEnabled(True)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_20 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.VisSaveBox = QGroupBox(self.centralwidget)
        self.VisSaveBox.setObjectName(u"VisSaveBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VisSaveBox.sizePolicy().hasHeightForWidth())
        self.VisSaveBox.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.VisSaveBox.setFont(font1)
        self.gridLayout_2 = QGridLayout(self.VisSaveBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer = QSpacerItem(250, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.aspect_desc = QLabel(self.VisSaveBox)
        self.aspect_desc.setObjectName(u"aspect_desc")
        self.aspect_desc.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setWeight(75)
        self.aspect_desc.setFont(font2)
        self.aspect_desc.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.aspect_desc)

        self.aspectr = QLineEdit(self.VisSaveBox)
        self.aspectr.setObjectName(u"aspectr")
        self.aspectr.setMaximumSize(QSize(16777215, 16777215))
        self.aspectr.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.aspectr)


        self.gridLayout.addLayout(self.horizontalLayout_10, 1, 2, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.coeff_desc = QLabel(self.VisSaveBox)
        self.coeff_desc.setObjectName(u"coeff_desc")
        self.coeff_desc.setMaximumSize(QSize(70, 16777215))
        self.coeff_desc.setFont(font2)
        self.coeff_desc.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.coeff_desc)

        self.inlog_coef = QLineEdit(self.VisSaveBox)
        self.inlog_coef.setObjectName(u"inlog_coef")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.inlog_coef.sizePolicy().hasHeightForWidth())
        self.inlog_coef.setSizePolicy(sizePolicy1)
        self.inlog_coef.setMaximumSize(QSize(16777215, 16777215))
        self.inlog_coef.setStyleSheet(u"4D0")

        self.horizontalLayout_9.addWidget(self.inlog_coef)


        self.gridLayout.addLayout(self.horizontalLayout_9, 1, 3, 1, 2)

        self.filenameline = QLineEdit(self.VisSaveBox)
        self.filenameline.setObjectName(u"filenameline")
        self.filenameline.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.filenameline, 3, 4, 1, 1)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.FolderLine = QLineEdit(self.VisSaveBox)
        self.FolderLine.setObjectName(u"FolderLine")
        self.FolderLine.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_39.addWidget(self.FolderLine)

        self.FolderButton = QToolButton(self.VisSaveBox)
        self.FolderButton.setObjectName(u"FolderButton")
        self.FolderButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_39.addWidget(self.FolderButton)


        self.gridLayout.addLayout(self.horizontalLayout_39, 3, 2, 1, 1)

        self.FileName_label = QLabel(self.VisSaveBox)
        self.FileName_label.setObjectName(u"FileName_label")
        self.FileName_label.setFont(font2)

        self.gridLayout.addWidget(self.FileName_label, 3, 1, 1, 1)

        self.SAVE_button = QPushButton(self.VisSaveBox)
        self.SAVE_button.setObjectName(u"SAVE_button")
        self.SAVE_button.setEnabled(False)
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setWeight(50)
        self.SAVE_button.setFont(font3)
        self.SAVE_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.SAVE_button.setStyleSheet(u"round-color: rgb(85, 196, 255); }\n"
"")

        self.gridLayout.addWidget(self.SAVE_button, 3, 5, 1, 1)

        self.PLOT_BUTTON = QPushButton(self.VisSaveBox)
        self.PLOT_BUTTON.setObjectName(u"PLOT_BUTTON")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.PLOT_BUTTON.sizePolicy().hasHeightForWidth())
        self.PLOT_BUTTON.setSizePolicy(sizePolicy2)
        self.PLOT_BUTTON.setFont(font3)
        self.PLOT_BUTTON.setCursor(QCursor(Qt.PointingHandCursor))
        self.PLOT_BUTTON.setStyleSheet(u"")

        self.gridLayout.addWidget(self.PLOT_BUTTON, 1, 5, 1, 1)

        self.FileNamelabel = QLabel(self.VisSaveBox)
        self.FileNamelabel.setObjectName(u"FileNamelabel")
        self.FileNamelabel.setMaximumSize(QSize(60, 16777215))
        self.FileNamelabel.setFont(font2)

        self.gridLayout.addWidget(self.FileNamelabel, 3, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.VisSaveBox, 3, 1, 1, 1)

        self.BscanWidget = ImageView(self.centralwidget)
        self.BscanWidget.setObjectName(u"BscanWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.BscanWidget.sizePolicy().hasHeightForWidth())
        self.BscanWidget.setSizePolicy(sizePolicy3)
        self.BscanWidget.setMinimumSize(QSize(250, 0))
        self.BscanWidget.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.BscanWidget, 0, 0, 1, 2)

        self.group_Scanning = QGroupBox(self.centralwidget)
        self.group_Scanning.setObjectName(u"group_Scanning")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.group_Scanning.sizePolicy().hasHeightForWidth())
        self.group_Scanning.setSizePolicy(sizePolicy4)
        self.group_Scanning.setMinimumSize(QSize(0, 130))
        self.group_Scanning.setMaximumSize(QSize(16777215, 200))
        self.group_Scanning.setFont(font1)
        self.gridLayout_10 = QGridLayout(self.group_Scanning)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.group_Bscan = QGroupBox(self.group_Scanning)
        self.group_Bscan.setObjectName(u"group_Bscan")
        sizePolicy3.setHeightForWidth(self.group_Bscan.sizePolicy().hasHeightForWidth())
        self.group_Bscan.setSizePolicy(sizePolicy3)
        self.verticalLayout_17 = QVBoxLayout(self.group_Bscan)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scan_label = QLabel(self.group_Bscan)
        self.scan_label.setObjectName(u"scan_label")
        self.scan_label.setFont(font2)
        self.scan_label.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.scan_label)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.instarttp = QLineEdit(self.group_Bscan)
        self.instarttp.setObjectName(u"instarttp")
        font4 = QFont()
        font4.setBold(False)
        font4.setWeight(50)
        self.instarttp.setFont(font4)
        self.instarttp.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.instarttp)

        self.instopp = QLineEdit(self.group_Bscan)
        self.instopp.setObjectName(u"instopp")
        self.instopp.setFont(font4)
        self.instopp.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.instopp)

        self.Button_ZmoveTo = QPushButton(self.group_Bscan)
        self.Button_ZmoveTo.setObjectName(u"Button_ZmoveTo")
        self.Button_ZmoveTo.setEnabled(False)
        self.Button_ZmoveTo.setFont(font4)

        self.horizontalLayout_8.addWidget(self.Button_ZmoveTo)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_9 = QLabel(self.group_Bscan)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.label_9)

        self.instep = QLineEdit(self.group_Bscan)
        self.instep.setObjectName(u"instep")
        self.instep.setFont(font4)
        self.instep.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.instep)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.Measure_button = QPushButton(self.group_Bscan)
        self.Measure_button.setObjectName(u"Measure_button")
        self.Measure_button.setEnabled(False)
        self.Measure_button.setFont(font3)
        self.Measure_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Measure_button.setMouseTracking(False)
        self.Measure_button.setFocusPolicy(Qt.StrongFocus)
        self.Measure_button.setStyleSheet(u"olor: rgb(85, 196, 255); }\n"
"")
        self.Measure_button.setCheckable(False)
        self.Measure_button.setAutoRepeat(False)
        self.Measure_button.setAutoDefault(False)
        self.Measure_button.setFlat(False)

        self.verticalLayout_3.addWidget(self.Measure_button)


        self.horizontalLayout_33.addLayout(self.verticalLayout_3)


        self.verticalLayout_17.addLayout(self.horizontalLayout_33)


        self.gridLayout_10.addWidget(self.group_Bscan, 0, 0, 1, 1)

        self.group_Cscan = QGroupBox(self.group_Scanning)
        self.group_Cscan.setObjectName(u"group_Cscan")
        self.horizontalLayout_32 = QHBoxLayout(self.group_Cscan)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.YscanStep = QLabel(self.group_Cscan)
        self.YscanStep.setObjectName(u"YscanStep")
        sizePolicy.setHeightForWidth(self.YscanStep.sizePolicy().hasHeightForWidth())
        self.YscanStep.setSizePolicy(sizePolicy)
        self.YscanStep.setMinimumSize(QSize(1, 0))
        self.YscanStep.setFont(font2)

        self.horizontalLayout_21.addWidget(self.YscanStep)


        self.verticalLayout_14.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.Y_start_pos = QLineEdit(self.group_Cscan)
        self.Y_start_pos.setObjectName(u"Y_start_pos")
        self.Y_start_pos.setFont(font4)

        self.horizontalLayout_28.addWidget(self.Y_start_pos)

        self.Y_stop_pos = QLineEdit(self.group_Cscan)
        self.Y_stop_pos.setObjectName(u"Y_stop_pos")
        sizePolicy2.setHeightForWidth(self.Y_stop_pos.sizePolicy().hasHeightForWidth())
        self.Y_stop_pos.setSizePolicy(sizePolicy2)
        self.Y_stop_pos.setMinimumSize(QSize(5, 0))
        self.Y_stop_pos.setFont(font4)

        self.horizontalLayout_28.addWidget(self.Y_stop_pos)


        self.verticalLayout_14.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.YstepNumberLabel = QLabel(self.group_Cscan)
        self.YstepNumberLabel.setObjectName(u"YstepNumberLabel")
        sizePolicy.setHeightForWidth(self.YstepNumberLabel.sizePolicy().hasHeightForWidth())
        self.YstepNumberLabel.setSizePolicy(sizePolicy)
        self.YstepNumberLabel.setFont(font2)

        self.horizontalLayout_24.addWidget(self.YstepNumberLabel)

        self.Y_step = QLineEdit(self.group_Cscan)
        self.Y_step.setObjectName(u"Y_step")
        sizePolicy2.setHeightForWidth(self.Y_step.sizePolicy().hasHeightForWidth())
        self.Y_step.setSizePolicy(sizePolicy2)
        self.Y_step.setMinimumSize(QSize(5, 0))
        self.Y_step.setFont(font4)

        self.horizontalLayout_24.addWidget(self.Y_step)


        self.verticalLayout_14.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.InitializeYstageButton = QPushButton(self.group_Cscan)
        self.InitializeYstageButton.setObjectName(u"InitializeYstageButton")
        self.InitializeYstageButton.setFont(font3)
        self.InitializeYstageButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.InitializeYstageButton)

        self.StartCscanBUTTON = QPushButton(self.group_Cscan)
        self.StartCscanBUTTON.setObjectName(u"StartCscanBUTTON")
        self.StartCscanBUTTON.setEnabled(False)
        self.StartCscanBUTTON.setFont(font3)
        self.StartCscanBUTTON.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.StartCscanBUTTON)


        self.verticalLayout_14.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_32.addLayout(self.verticalLayout_14)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label = QLabel(self.group_Cscan)
        self.label.setObjectName(u"label")
        font5 = QFont()
        font5.setPointSize(8)
        font5.setBold(True)
        font5.setWeight(75)
        font5.setKerning(True)
        self.label.setFont(font5)
#if QT_CONFIG(statustip)
        self.label.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label)

        self.Button_YmoveTo = QPushButton(self.group_Cscan)
        self.Button_YmoveTo.setObjectName(u"Button_YmoveTo")
        self.Button_YmoveTo.setEnabled(False)
        self.Button_YmoveTo.setFont(font4)

        self.verticalLayout_13.addWidget(self.Button_YmoveTo)

        self.YStageUP = QPushButton(self.group_Cscan)
        self.YStageUP.setObjectName(u"YStageUP")
        self.YStageUP.setEnabled(False)
        self.YStageUP.setFont(font4)
        self.YStageUP.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.YStageUP)

        self.YStageDOWN = QPushButton(self.group_Cscan)
        self.YStageDOWN.setObjectName(u"YStageDOWN")
        self.YStageDOWN.setEnabled(False)
        self.YStageDOWN.setFont(font4)
        self.YStageDOWN.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.YStageDOWN)


        self.horizontalLayout_32.addLayout(self.verticalLayout_13)


        self.gridLayout_10.addWidget(self.group_Cscan, 0, 1, 1, 1)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.MeasurementProgressLine = QLabel(self.group_Scanning)
        self.MeasurementProgressLine.setObjectName(u"MeasurementProgressLine")
        sizePolicy.setHeightForWidth(self.MeasurementProgressLine.sizePolicy().hasHeightForWidth())
        self.MeasurementProgressLine.setSizePolicy(sizePolicy)
        self.MeasurementProgressLine.setMaximumSize(QSize(16777215, 16777215))
        self.MeasurementProgressLine.setFont(font2)

        self.horizontalLayout_34.addWidget(self.MeasurementProgressLine)

        self.scanprogressBar = QProgressBar(self.group_Scanning)
        self.scanprogressBar.setObjectName(u"scanprogressBar")
        self.scanprogressBar.setStyleSheet(u"")
        self.scanprogressBar.setValue(0)

        self.horizontalLayout_34.addWidget(self.scanprogressBar)

        self.StopButton = QPushButton(self.group_Scanning)
        self.StopButton.setObjectName(u"StopButton")
        self.StopButton.setFont(font3)
        self.StopButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_34.addWidget(self.StopButton)


        self.gridLayout_10.addLayout(self.horizontalLayout_34, 1, 0, 1, 2)


        self.gridLayout_5.addWidget(self.group_Scanning, 1, 1, 1, 1)


        self.horizontalLayout_20.addLayout(self.gridLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy3.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy3)
        self.groupBox_4.setMinimumSize(QSize(200, 0))
        self.groupBox_4.setMaximumSize(QSize(350, 16777215))
        self.groupBox_4.setFont(font1)
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.InitBUTTON = QPushButton(self.groupBox_4)
        self.InitBUTTON.setObjectName(u"InitBUTTON")
        sizePolicy3.setHeightForWidth(self.InitBUTTON.sizePolicy().hasHeightForWidth())
        self.InitBUTTON.setSizePolicy(sizePolicy3)
        self.InitBUTTON.setMinimumSize(QSize(0, 0))
        self.InitBUTTON.setFont(font3)
        self.InitBUTTON.setCursor(QCursor(Qt.PointingHandCursor))
        self.InitBUTTON.setMouseTracking(False)
        self.InitBUTTON.setFocusPolicy(Qt.StrongFocus)
        self.InitBUTTON.setStyleSheet(u"olor: rgb(85, 196, 255); }\n"
"")
        self.InitBUTTON.setCheckable(False)
        self.InitBUTTON.setAutoRepeat(False)
        self.InitBUTTON.setAutoDefault(False)
        self.InitBUTTON.setFlat(False)

        self.verticalLayout_16.addWidget(self.InitBUTTON)

        self.logbrowser = QTextBrowser(self.groupBox_4)
        self.logbrowser.setObjectName(u"logbrowser")
        self.logbrowser.setMinimumSize(QSize(150, 0))
        self.logbrowser.setMaximumSize(QSize(350, 16777215))

        self.verticalLayout_16.addWidget(self.logbrowser)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.ACQ_parameters = QGroupBox(self.centralwidget)
        self.ACQ_parameters.setObjectName(u"ACQ_parameters")
        sizePolicy3.setHeightForWidth(self.ACQ_parameters.sizePolicy().hasHeightForWidth())
        self.ACQ_parameters.setSizePolicy(sizePolicy3)
        self.ACQ_parameters.setMinimumSize(QSize(100, 0))
        self.ACQ_parameters.setMaximumSize(QSize(350, 16777215))
        self.ACQ_parameters.setFont(font1)
        self.ACQ_parameters.setMouseTracking(False)
        self.ACQ_parameters.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.ACQ_parameters)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.freq_label = QLabel(self.ACQ_parameters)
        self.freq_label.setObjectName(u"freq_label")
        font6 = QFont()
        font6.setBold(True)
        font6.setWeight(75)
        self.freq_label.setFont(font6)
        self.freq_label.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.freq_label)

        self.IP_var = QLineEdit(self.ACQ_parameters)
        self.IP_var.setObjectName(u"IP_var")
        font7 = QFont()
        font7.setBold(False)
        font7.setWeight(50)
        font7.setKerning(False)
        self.IP_var.setFont(font7)
        self.IP_var.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.IP_var)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.delay_label = QLabel(self.ACQ_parameters)
        self.delay_label.setObjectName(u"delay_label")
        self.delay_label.setFont(font2)
        self.delay_label.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.delay_label)

        self.delay_var = QLineEdit(self.ACQ_parameters)
        self.delay_var.setObjectName(u"delay_var")
        self.delay_var.setFont(font7)
        self.delay_var.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.delay_var)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.DEC_label = QLabel(self.ACQ_parameters)
        self.DEC_label.setObjectName(u"DEC_label")
        self.DEC_label.setFont(font6)
        self.DEC_label.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.DEC_label)

        self.decimation_var = QLineEdit(self.ACQ_parameters)
        self.decimation_var.setObjectName(u"decimation_var")
        self.decimation_var.setFont(font7)
        self.decimation_var.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.decimation_var)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.APPLY_button = QPushButton(self.ACQ_parameters)
        self.APPLY_button.setObjectName(u"APPLY_button")
        sizePolicy2.setHeightForWidth(self.APPLY_button.sizePolicy().hasHeightForWidth())
        self.APPLY_button.setSizePolicy(sizePolicy2)
        self.APPLY_button.setFont(font3)
        self.APPLY_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.APPLY_button.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.APPLY_button)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)


        self.verticalLayout.addWidget(self.ACQ_parameters)

        self.OCT_Params = QGroupBox(self.centralwidget)
        self.OCT_Params.setObjectName(u"OCT_Params")
        sizePolicy3.setHeightForWidth(self.OCT_Params.sizePolicy().hasHeightForWidth())
        self.OCT_Params.setSizePolicy(sizePolicy3)
        self.OCT_Params.setMinimumSize(QSize(200, 0))
        self.OCT_Params.setMaximumSize(QSize(350, 16777215))
        self.OCT_Params.setFont(font1)
        self.OCT_Params.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.OCT_Params)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.Aver_checkBox = QCheckBox(self.OCT_Params)
        self.Aver_checkBox.setObjectName(u"Aver_checkBox")
        self.Aver_checkBox.setFont(font2)
        self.Aver_checkBox.setStyleSheet(u"")
        self.Aver_checkBox.setChecked(True)

        self.horizontalLayout_19.addWidget(self.Aver_checkBox)

        self.Zero_padding_checkBox = QCheckBox(self.OCT_Params)
        self.Zero_padding_checkBox.setObjectName(u"Zero_padding_checkBox")
        self.Zero_padding_checkBox.setEnabled(False)
        self.Zero_padding_checkBox.setFont(font2)
        self.Zero_padding_checkBox.setStyleSheet(u"")

        self.horizontalLayout_19.addWidget(self.Zero_padding_checkBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_19)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_8 = QLabel(self.OCT_Params)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.label_8)

        self.intid = QLineEdit(self.OCT_Params)
        self.intid.setObjectName(u"intid")
        self.intid.setFont(font4)
        self.intid.setStyleSheet(u"r: #D5D4D0")

        self.horizontalLayout_11.addWidget(self.intid)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.aver_num_label = QLabel(self.OCT_Params)
        self.aver_num_label.setObjectName(u"aver_num_label")
        self.aver_num_label.setFont(font2)
        self.aver_num_label.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.aver_num_label)

        self.innum = QLineEdit(self.OCT_Params)
        self.innum.setObjectName(u"innum")
        self.innum.setFont(font7)
        self.innum.setStyleSheet(u"4D0")

        self.horizontalLayout_5.addWidget(self.innum)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.SET_OCTParams = QPushButton(self.OCT_Params)
        self.SET_OCTParams.setObjectName(u"SET_OCTParams")
        sizePolicy2.setHeightForWidth(self.SET_OCTParams.sizePolicy().hasHeightForWidth())
        self.SET_OCTParams.setSizePolicy(sizePolicy2)
        self.SET_OCTParams.setFont(font3)
        self.SET_OCTParams.setCursor(QCursor(Qt.PointingHandCursor))
        self.SET_OCTParams.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.SET_OCTParams)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)


        self.verticalLayout.addWidget(self.OCT_Params)

        self.Process_params = QGroupBox(self.centralwidget)
        self.Process_params.setObjectName(u"Process_params")
        sizePolicy3.setHeightForWidth(self.Process_params.sizePolicy().hasHeightForWidth())
        self.Process_params.setSizePolicy(sizePolicy3)
        self.Process_params.setMinimumSize(QSize(200, 0))
        self.Process_params.setMaximumSize(QSize(350, 16777215))
        self.Process_params.setFont(font1)
        self.Process_params.setFlat(False)
        self.Process_params.setCheckable(False)
        self.verticalLayout_9 = QVBoxLayout(self.Process_params)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.NIR_radio = QRadioButton(self.Process_params)
        self.NIR_radio.setObjectName(u"NIR_radio")
        self.NIR_radio.setFont(font2)
        self.NIR_radio.setStyleSheet(u"")
        self.NIR_radio.setChecked(False)

        self.horizontalLayout_16.addWidget(self.NIR_radio)

        self.MIR_radio = QRadioButton(self.Process_params)
        self.MIR_radio.setObjectName(u"MIR_radio")
        self.MIR_radio.setFont(font2)
        self.MIR_radio.setStyleSheet(u"")
        self.MIR_radio.setChecked(True)

        self.horizontalLayout_16.addWidget(self.MIR_radio)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)

        self.label_7 = QLabel(self.Process_params)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.label_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.inwl = QLineEdit(self.Process_params)
        self.inwl.setObjectName(u"inwl")
        self.inwl.setFont(font4)
        self.inwl.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.inwl)

        self.inwh = QLineEdit(self.Process_params)
        self.inwh.setObjectName(u"inwh")
        self.inwh.setFont(font4)
        self.inwh.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.inwh)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.Process_params)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.ingw = QLineEdit(self.Process_params)
        self.ingw.setObjectName(u"ingw")
        self.ingw.setFont(font4)
        self.ingw.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.ingw)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_10 = QLabel(self.Process_params)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.label_10)

        self.ina = QLineEdit(self.Process_params)
        self.ina.setObjectName(u"ina")
        self.ina.setFont(font4)
        self.ina.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.ina)


        self.verticalLayout_6.addLayout(self.horizontalLayout_15)

        self.APPLY_procparams = QPushButton(self.Process_params)
        self.APPLY_procparams.setObjectName(u"APPLY_procparams")
        sizePolicy2.setHeightForWidth(self.APPLY_procparams.sizePolicy().hasHeightForWidth())
        self.APPLY_procparams.setSizePolicy(sizePolicy2)
        self.APPLY_procparams.setFont(font3)
        self.APPLY_procparams.setCursor(QCursor(Qt.PointingHandCursor))
        self.APPLY_procparams.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.APPLY_procparams)

        self.ApplyPPC = QPushButton(self.Process_params)
        self.ApplyPPC.setObjectName(u"ApplyPPC")
        sizePolicy2.setHeightForWidth(self.ApplyPPC.sizePolicy().hasHeightForWidth())
        self.ApplyPPC.setSizePolicy(sizePolicy2)
        self.ApplyPPC.setFont(font3)

        self.verticalLayout_6.addWidget(self.ApplyPPC)


        self.verticalLayout_9.addLayout(self.verticalLayout_6)


        self.verticalLayout.addWidget(self.Process_params)

        self.ReferencingBox = QGroupBox(self.centralwidget)
        self.ReferencingBox.setObjectName(u"ReferencingBox")
        sizePolicy3.setHeightForWidth(self.ReferencingBox.sizePolicy().hasHeightForWidth())
        self.ReferencingBox.setSizePolicy(sizePolicy3)
        self.ReferencingBox.setMinimumSize(QSize(200, 0))
        self.ReferencingBox.setMaximumSize(QSize(350, 16777215))
        self.ReferencingBox.setFont(font1)
        self.gridLayout_4 = QGridLayout(self.ReferencingBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(10)
        self.ref_BUTTON = QPushButton(self.ReferencingBox)
        self.ref_BUTTON.setObjectName(u"ref_BUTTON")
        self.ref_BUTTON.setEnabled(False)
        self.ref_BUTTON.setFont(font3)
        self.ref_BUTTON.setCursor(QCursor(Qt.PointingHandCursor))
        self.ref_BUTTON.setStyleSheet(u"round-color: rgb(85, 196, 255); }\n"
"")

        self.gridLayout_3.addWidget(self.ref_BUTTON, 3, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.aver_num_label_3 = QLabel(self.ReferencingBox)
        self.aver_num_label_3.setObjectName(u"aver_num_label_3")
        self.aver_num_label_3.setFont(font2)
        self.aver_num_label_3.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.aver_num_label_3)

        self.inrefnum = QLineEdit(self.ReferencingBox)
        self.inrefnum.setObjectName(u"inrefnum")
        sizePolicy2.setHeightForWidth(self.inrefnum.sizePolicy().hasHeightForWidth())
        self.inrefnum.setSizePolicy(sizePolicy2)
        self.inrefnum.setMaximumSize(QSize(16777215, 16777215))
        font8 = QFont()
        font8.setPointSize(8)
        font8.setKerning(False)
        self.inrefnum.setFont(font8)
        self.inrefnum.setStyleSheet(u"d-color: #D5D4D0")

        self.horizontalLayout_13.addWidget(self.inrefnum)


        self.gridLayout_3.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)

        self.refprogressBar = QProgressBar(self.ReferencingBox)
        self.refprogressBar.setObjectName(u"refprogressBar")
        self.refprogressBar.setStyleSheet(u"")
        self.refprogressBar.setValue(100)

        self.gridLayout_3.addWidget(self.refprogressBar, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.ResetRef_button = QPushButton(self.ReferencingBox)
        self.ResetRef_button.setObjectName(u"ResetRef_button")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.ResetRef_button.sizePolicy().hasHeightForWidth())
        self.ResetRef_button.setSizePolicy(sizePolicy5)
        self.ResetRef_button.setFont(font3)
        self.ResetRef_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.ResetRef_button.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.ResetRef_button, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.ReferencingBox)


        self.horizontalLayout_20.addLayout(self.verticalLayout)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.raw_signal_plot = PlotWidget(self.centralwidget)
        self.raw_signal_plot.setObjectName(u"raw_signal_plot")
        sizePolicy3.setHeightForWidth(self.raw_signal_plot.sizePolicy().hasHeightForWidth())
        self.raw_signal_plot.setSizePolicy(sizePolicy3)
        self.raw_signal_plot.setMinimumSize(QSize(100, 0))
        self.raw_signal_plot.setMaximumSize(QSize(450, 16777215))

        self.verticalLayout_12.addWidget(self.raw_signal_plot)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy6)
        self.groupBox_2.setMinimumSize(QSize(100, 5))
        self.groupBox_2.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_2.setFont(font1)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.ACQ_range_label = QLabel(self.groupBox_2)
        self.ACQ_range_label.setObjectName(u"ACQ_range_label")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.ACQ_range_label.sizePolicy().hasHeightForWidth())
        self.ACQ_range_label.setSizePolicy(sizePolicy7)
        self.ACQ_range_label.setMinimumSize(QSize(100, 0))
        font9 = QFont()
        font9.setPointSize(10)
        self.ACQ_range_label.setFont(font9)

        self.verticalLayout_10.addWidget(self.ACQ_range_label)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.rang_start = QLineEdit(self.groupBox_2)
        self.rang_start.setObjectName(u"rang_start")
        sizePolicy5.setHeightForWidth(self.rang_start.sizePolicy().hasHeightForWidth())
        self.rang_start.setSizePolicy(sizePolicy5)
        self.rang_start.setMinimumSize(QSize(15, 0))
        self.rang_start.setFont(font4)

        self.horizontalLayout_30.addWidget(self.rang_start)

        self.rang_stop = QLineEdit(self.groupBox_2)
        self.rang_stop.setObjectName(u"rang_stop")
        sizePolicy5.setHeightForWidth(self.rang_stop.sizePolicy().hasHeightForWidth())
        self.rang_stop.setSizePolicy(sizePolicy5)
        self.rang_stop.setFont(font4)

        self.horizontalLayout_30.addWidget(self.rang_stop)


        self.verticalLayout_10.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.stop_acq_BUTTON = QPushButton(self.groupBox_2)
        self.stop_acq_BUTTON.setObjectName(u"stop_acq_BUTTON")
        sizePolicy5.setHeightForWidth(self.stop_acq_BUTTON.sizePolicy().hasHeightForWidth())
        self.stop_acq_BUTTON.setSizePolicy(sizePolicy5)
        self.stop_acq_BUTTON.setMinimumSize(QSize(15, 10))
        self.stop_acq_BUTTON.setFont(font3)
        self.stop_acq_BUTTON.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_acq_BUTTON.setMouseTracking(False)
        self.stop_acq_BUTTON.setFocusPolicy(Qt.StrongFocus)
        self.stop_acq_BUTTON.setStyleSheet(u"olor: rgb(85, 196, 255); }\n"
"")
        self.stop_acq_BUTTON.setCheckable(False)
        self.stop_acq_BUTTON.setAutoRepeat(False)
        self.stop_acq_BUTTON.setAutoDefault(False)
        self.stop_acq_BUTTON.setFlat(False)

        self.horizontalLayout_12.addWidget(self.stop_acq_BUTTON)

        self.start_acq_BUTTON = QPushButton(self.groupBox_2)
        self.start_acq_BUTTON.setObjectName(u"start_acq_BUTTON")
        sizePolicy5.setHeightForWidth(self.start_acq_BUTTON.sizePolicy().hasHeightForWidth())
        self.start_acq_BUTTON.setSizePolicy(sizePolicy5)
        self.start_acq_BUTTON.setMinimumSize(QSize(15, 10))
        self.start_acq_BUTTON.setFont(font3)
        self.start_acq_BUTTON.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_acq_BUTTON.setMouseTracking(False)
        self.start_acq_BUTTON.setFocusPolicy(Qt.StrongFocus)
        self.start_acq_BUTTON.setStyleSheet(u"olor: rgb(85, 196, 255); }\n"
"")
        self.start_acq_BUTTON.setCheckable(False)
        self.start_acq_BUTTON.setAutoRepeat(False)
        self.start_acq_BUTTON.setAutoDefault(False)
        self.start_acq_BUTTON.setFlat(False)

        self.horizontalLayout_12.addWidget(self.start_acq_BUTTON)


        self.verticalLayout_10.addLayout(self.horizontalLayout_12)


        self.verticalLayout_12.addWidget(self.groupBox_2)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.labelsupuvir_2 = QLabel(self.centralwidget)
        self.labelsupuvir_2.setObjectName(u"labelsupuvir_2")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.labelsupuvir_2.sizePolicy().hasHeightForWidth())
        self.labelsupuvir_2.setSizePolicy(sizePolicy8)
        font10 = QFont()
        font10.setFamily(u"Segoe UI Light")
        font10.setPointSize(10)
        font10.setBold(True)
        font10.setWeight(75)
        self.labelsupuvir_2.setFont(font10)
        self.labelsupuvir_2.setStyleSheet(u"color:white;")

        self.verticalLayout_11.addWidget(self.labelsupuvir_2)


        self.horizontalLayout_17.addLayout(self.verticalLayout_11)

        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QSize(0, 0))
        self.logo.setMaximumSize(QSize(50, 60))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setPixmap(QPixmap(u"../../Users/r.zor/.designer/backup/logo/rlogo.png"))
        self.logo.setScaledContents(True)
        self.logo.setMargin(10)

        self.horizontalLayout_17.addWidget(self.logo)


        self.verticalLayout_12.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_20.addLayout(self.verticalLayout_12)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 18))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.Measure_button.setDefault(False)
        self.InitBUTTON.setDefault(False)
        self.stop_acq_BUTTON.setDefault(False)
        self.start_acq_BUTTON.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"teOCTControl - Version-1.65 May-2022", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save parameters", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(shortcut)
        self.actionAbout.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+H", None))
#endif // QT_CONFIG(shortcut)
        self.VisSaveBox.setTitle(QCoreApplication.translate("MainWindow", u"Visualization and saving", None))
        self.aspect_desc.setText(QCoreApplication.translate("MainWindow", u"Aspect ratio", None))
        self.aspectr.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.coeff_desc.setText(QCoreApplication.translate("MainWindow", u"DR log coeff.", None))
        self.inlog_coef.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.filenameline.setText(QCoreApplication.translate("MainWindow", u"scan", None))
        self.FolderButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.FileName_label.setText(QCoreApplication.translate("MainWindow", u"File directory", None))
        self.SAVE_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.PLOT_BUTTON.setText(QCoreApplication.translate("MainWindow", u"Plot scan", None))
        self.FileNamelabel.setText(QCoreApplication.translate("MainWindow", u"Filename", None))
        self.group_Scanning.setTitle(QCoreApplication.translate("MainWindow", u"Scanning", None))
        self.group_Bscan.setTitle(QCoreApplication.translate("MainWindow", u"B-scan", None))
        self.scan_label.setText(QCoreApplication.translate("MainWindow", u"X scanning interval (mm)", None))
        self.instarttp.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.instopp.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Button_ZmoveTo.setText(QCoreApplication.translate("MainWindow", u"Move to", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"X scanning step (mm)", None))
        self.instep.setText(QCoreApplication.translate("MainWindow", u"0.04", None))
        self.Measure_button.setText(QCoreApplication.translate("MainWindow", u"B-scan measure", None))
#if QT_CONFIG(shortcut)
        self.Measure_button.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.group_Cscan.setTitle(QCoreApplication.translate("MainWindow", u"Volume scan", None))
        self.YscanStep.setText(QCoreApplication.translate("MainWindow", u"Y interval (mm)", None))
        self.Y_start_pos.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.Y_stop_pos.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.YstepNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Y scanning step (mm)", None))
        self.Y_step.setText(QCoreApplication.translate("MainWindow", u"0.04", None))
        self.InitializeYstageButton.setText(QCoreApplication.translate("MainWindow", u"Initialize Y stage", None))
        self.StartCscanBUTTON.setText(QCoreApplication.translate("MainWindow", u"Start 3D scan", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Y stage", None))
        self.Button_YmoveTo.setText(QCoreApplication.translate("MainWindow", u"Move to", None))
        self.YStageUP.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.YStageDOWN.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.MeasurementProgressLine.setText(QCoreApplication.translate("MainWindow", u"Measurement progress", None))
        self.StopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Initialization and logs", None))
        self.InitBUTTON.setText(QCoreApplication.translate("MainWindow", u"Initialize", None))
#if QT_CONFIG(shortcut)
        self.InitBUTTON.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.logbrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt; font-weight:400;\">Initialization required</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt; font-weight:400;\"><br /></p></body></html>", None))
        self.ACQ_parameters.setTitle(QCoreApplication.translate("MainWindow", u" DAQ parameters", None))
        self.freq_label.setText(QCoreApplication.translate("MainWindow", u"IP", None))
        self.IP_var.setText(QCoreApplication.translate("MainWindow", u"10.40.47.135", None))
        self.delay_label.setText(QCoreApplication.translate("MainWindow", u"Trig. delay", None))
        self.delay_var.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.DEC_label.setText(QCoreApplication.translate("MainWindow", u"Decimation", None))
        self.decimation_var.setText(QCoreApplication.translate("MainWindow", u"256", None))
        self.APPLY_button.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.OCT_Params.setTitle(QCoreApplication.translate("MainWindow", u"Scanning parameters", None))
        self.Aver_checkBox.setText(QCoreApplication.translate("MainWindow", u"Averaging", None))
        self.Zero_padding_checkBox.setText(QCoreApplication.translate("MainWindow", u"Zero padding", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"A-scan delay (s)", None))
        self.intid.setText(QCoreApplication.translate("MainWindow", u"0.2", None))
        self.aver_num_label.setText(QCoreApplication.translate("MainWindow", u"Averaging", None))
        self.innum.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.SET_OCTParams.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.Process_params.setTitle(QCoreApplication.translate("MainWindow", u"Post-processing", None))
        self.NIR_radio.setText(QCoreApplication.translate("MainWindow", u"Range1", None))
        self.MIR_radio.setText(QCoreApplication.translate("MainWindow", u"Range2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Sampling bandwidth (nm)", None))
        self.inwl.setText(QCoreApplication.translate("MainWindow", u"3235", None))
        self.inwh.setText(QCoreApplication.translate("MainWindow", u"4472", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Gaussian window (px)", None))
        self.ingw.setText(QCoreApplication.translate("MainWindow", u"1500", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Window position", None))
        self.ina.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.APPLY_procparams.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.ApplyPPC.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.ReferencingBox.setTitle(QCoreApplication.translate("MainWindow", u"Referenceing", None))
        self.ref_BUTTON.setText(QCoreApplication.translate("MainWindow", u"Referencing", None))
        self.aver_num_label_3.setText(QCoreApplication.translate("MainWindow", u"Spectra integrated (num)    ", None))
        self.inrefnum.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.ResetRef_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Spectra aquisition", None))
        self.ACQ_range_label.setText(QCoreApplication.translate("MainWindow", u"Range in samples", None))
        self.rang_start.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.rang_stop.setText(QCoreApplication.translate("MainWindow", u"16384", None))
        self.stop_acq_BUTTON.setText(QCoreApplication.translate("MainWindow", u"Set delay", None))
#if QT_CONFIG(shortcut)
        self.stop_acq_BUTTON.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.start_acq_BUTTON.setText(QCoreApplication.translate("MainWindow", u"Set range", None))
#if QT_CONFIG(shortcut)
        self.start_acq_BUTTON.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.labelsupuvir_2.setText(QCoreApplication.translate("MainWindow", u"Digital Inspection and Quality Assurance\n"
"for Lithography-based Ceramics Additive Manufacturing", None))
        self.logo.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

