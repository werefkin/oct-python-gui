# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QTextBrowser, QToolButton, QVBoxLayout,
    QWidget)

from pyqtgraph import (ImageView, PlotWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 920)
        MainWindow.setMinimumSize(QSize(1280, 920))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
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
        self.actionVolumetric_plotter = QAction(MainWindow)
        self.actionVolumetric_plotter.setObjectName(u"actionVolumetric_plotter")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_20 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 16, 16, 5)
        self.gridMain = QGridLayout()
        self.gridMain.setObjectName(u"gridMain")
        self.group_VisualizationSaving = QGroupBox(self.centralwidget)
        self.group_VisualizationSaving.setObjectName(u"group_VisualizationSaving")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_VisualizationSaving.sizePolicy().hasHeightForWidth())
        self.group_VisualizationSaving.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setStrikeOut(False)
        self.group_VisualizationSaving.setFont(font1)
        self.gridLayout_2 = QGridLayout(self.group_VisualizationSaving)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_VisualizationSaving = QGridLayout()
        self.gridLayout_VisualizationSaving.setObjectName(u"gridLayout_VisualizationSaving")
        self.horizontalLayout_ApectRatio = QHBoxLayout()
        self.horizontalLayout_ApectRatio.setObjectName(u"horizontalLayout_ApectRatio")
        self.label_Aspect = QLabel(self.group_VisualizationSaving)
        self.label_Aspect.setObjectName(u"label_Aspect")
        self.label_Aspect.setMinimumSize(QSize(0, 15))
        self.label_Aspect.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setStrikeOut(False)
        self.label_Aspect.setFont(font2)
        self.label_Aspect.setStyleSheet(u"")

        self.horizontalLayout_ApectRatio.addWidget(self.label_Aspect)

        self.aspect_ratio = QLineEdit(self.group_VisualizationSaving)
        self.aspect_ratio.setObjectName(u"aspect_ratio")
        self.aspect_ratio.setMinimumSize(QSize(0, 20))
        self.aspect_ratio.setMaximumSize(QSize(16777215, 16777215))
        self.aspect_ratio.setStyleSheet(u"")

        self.horizontalLayout_ApectRatio.addWidget(self.aspect_ratio)


        self.gridLayout_VisualizationSaving.addLayout(self.horizontalLayout_ApectRatio, 1, 2, 1, 1)

        self.horizontalLayout_Log10Coef = QHBoxLayout()
        self.horizontalLayout_Log10Coef.setObjectName(u"horizontalLayout_Log10Coef")
        self.label_Log10Coef = QLabel(self.group_VisualizationSaving)
        self.label_Log10Coef.setObjectName(u"label_Log10Coef")
        sizePolicy.setHeightForWidth(self.label_Log10Coef.sizePolicy().hasHeightForWidth())
        self.label_Log10Coef.setSizePolicy(sizePolicy)
        self.label_Log10Coef.setMinimumSize(QSize(80, 15))
        self.label_Log10Coef.setMaximumSize(QSize(16777215, 16777215))
        self.label_Log10Coef.setFont(font2)
        self.label_Log10Coef.setStyleSheet(u"")
        self.label_Log10Coef.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_Log10Coef.addWidget(self.label_Log10Coef)

        self.log10_coef = QLineEdit(self.group_VisualizationSaving)
        self.log10_coef.setObjectName(u"log10_coef")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.log10_coef.sizePolicy().hasHeightForWidth())
        self.log10_coef.setSizePolicy(sizePolicy1)
        self.log10_coef.setMinimumSize(QSize(0, 20))
        self.log10_coef.setMaximumSize(QSize(16777215, 16777215))
        self.log10_coef.setStyleSheet(u"")

        self.horizontalLayout_Log10Coef.addWidget(self.log10_coef)


        self.gridLayout_VisualizationSaving.addLayout(self.horizontalLayout_Log10Coef, 1, 3, 1, 2)

        self.filenameline = QLineEdit(self.group_VisualizationSaving)
        self.filenameline.setObjectName(u"filenameline")
        self.filenameline.setMinimumSize(QSize(0, 20))
        self.filenameline.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_VisualizationSaving.addWidget(self.filenameline, 3, 4, 1, 1)

        self.horizontalLayout_directory = QHBoxLayout()
        self.horizontalLayout_directory.setObjectName(u"horizontalLayout_directory")
        self.FolderLine = QLineEdit(self.group_VisualizationSaving)
        self.FolderLine.setObjectName(u"FolderLine")
        self.FolderLine.setMinimumSize(QSize(200, 20))

        self.horizontalLayout_directory.addWidget(self.FolderLine)

        self.FolderButton = QToolButton(self.group_VisualizationSaving)
        self.FolderButton.setObjectName(u"FolderButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.FolderButton.sizePolicy().hasHeightForWidth())
        self.FolderButton.setSizePolicy(sizePolicy2)
        self.FolderButton.setMinimumSize(QSize(0, 20))
        self.FolderButton.setMaximumSize(QSize(16777215, 20))
        self.FolderButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_directory.addWidget(self.FolderButton)


        self.gridLayout_VisualizationSaving.addLayout(self.horizontalLayout_directory, 3, 2, 1, 1)

        self.label_DirName = QLabel(self.group_VisualizationSaving)
        self.label_DirName.setObjectName(u"label_DirName")
        self.label_DirName.setMinimumSize(QSize(0, 15))
        self.label_DirName.setFont(font2)

        self.gridLayout_VisualizationSaving.addWidget(self.label_DirName, 3, 1, 1, 1)

        self.SaveButton = QPushButton(self.group_VisualizationSaving)
        self.SaveButton.setObjectName(u"SaveButton")
        self.SaveButton.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.SaveButton.sizePolicy().hasHeightForWidth())
        self.SaveButton.setSizePolicy(sizePolicy3)
        self.SaveButton.setMinimumSize(QSize(0, 20))
        self.SaveButton.setMaximumSize(QSize(16777215, 20))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStrikeOut(False)
        self.SaveButton.setFont(font3)
        self.SaveButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.SaveButton.setStyleSheet(u"")

        self.gridLayout_VisualizationSaving.addWidget(self.SaveButton, 3, 5, 1, 1)

        self.PlotButton = QPushButton(self.group_VisualizationSaving)
        self.PlotButton.setObjectName(u"PlotButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.PlotButton.sizePolicy().hasHeightForWidth())
        self.PlotButton.setSizePolicy(sizePolicy4)
        self.PlotButton.setMinimumSize(QSize(0, 20))
        self.PlotButton.setMaximumSize(QSize(16777215, 20))
        self.PlotButton.setFont(font3)
        self.PlotButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.PlotButton.setStyleSheet(u"")

        self.gridLayout_VisualizationSaving.addWidget(self.PlotButton, 1, 5, 1, 1)

        self.label_FileName = QLabel(self.group_VisualizationSaving)
        self.label_FileName.setObjectName(u"label_FileName")
        self.label_FileName.setMinimumSize(QSize(0, 15))
        self.label_FileName.setMaximumSize(QSize(60, 16777215))
        self.label_FileName.setFont(font2)

        self.gridLayout_VisualizationSaving.addWidget(self.label_FileName, 3, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_VisualizationSaving, 0, 1, 1, 1)


        self.gridMain.addWidget(self.group_VisualizationSaving, 3, 1, 1, 1)

        self.BscanWidget = ImageView(self.centralwidget)
        self.BscanWidget.setObjectName(u"BscanWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.BscanWidget.sizePolicy().hasHeightForWidth())
        self.BscanWidget.setSizePolicy(sizePolicy5)
        self.BscanWidget.setMinimumSize(QSize(250, 0))
        self.BscanWidget.setMaximumSize(QSize(16777215, 16777215))

        self.gridMain.addWidget(self.BscanWidget, 0, 0, 1, 2)

        self.group_Scanning = QGroupBox(self.centralwidget)
        self.group_Scanning.setObjectName(u"group_Scanning")
        sizePolicy5.setHeightForWidth(self.group_Scanning.sizePolicy().hasHeightForWidth())
        self.group_Scanning.setSizePolicy(sizePolicy5)
        self.group_Scanning.setMinimumSize(QSize(0, 130))
        self.group_Scanning.setMaximumSize(QSize(16777215, 200))
        self.group_Scanning.setFont(font1)
        self.gridLayout_10 = QGridLayout(self.group_Scanning)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.group_Bscan = QGroupBox(self.group_Scanning)
        self.group_Bscan.setObjectName(u"group_Bscan")
        sizePolicy4.setHeightForWidth(self.group_Bscan.sizePolicy().hasHeightForWidth())
        self.group_Bscan.setSizePolicy(sizePolicy4)
        self.verticalLayout_17 = QVBoxLayout(self.group_Bscan)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_XScanParams = QHBoxLayout()
        self.horizontalLayout_XScanParams.setObjectName(u"horizontalLayout_XScanParams")
        self.verticalLayout__XScanParams = QVBoxLayout()
        self.verticalLayout__XScanParams.setObjectName(u"verticalLayout__XScanParams")
        self.scan_label = QLabel(self.group_Bscan)
        self.scan_label.setObjectName(u"scan_label")
        self.scan_label.setMinimumSize(QSize(0, 15))
        self.scan_label.setFont(font2)
        self.scan_label.setStyleSheet(u"")

        self.verticalLayout__XScanParams.addWidget(self.scan_label)

        self.horizontalLayout_XRange = QHBoxLayout()
        self.horizontalLayout_XRange.setObjectName(u"horizontalLayout_XRange")
        self.horizontalLayout_XRange.setContentsMargins(-1, -1, -1, 4)
        self.x_start_pos_ui = QLineEdit(self.group_Bscan)
        self.x_start_pos_ui.setObjectName(u"x_start_pos_ui")
        self.x_start_pos_ui.setMinimumSize(QSize(0, 20))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStrikeOut(False)
        self.x_start_pos_ui.setFont(font4)
        self.x_start_pos_ui.setStyleSheet(u"")

        self.horizontalLayout_XRange.addWidget(self.x_start_pos_ui)

        self.x_stop_pos_ui = QLineEdit(self.group_Bscan)
        self.x_stop_pos_ui.setObjectName(u"x_stop_pos_ui")
        self.x_stop_pos_ui.setMinimumSize(QSize(0, 20))
        self.x_stop_pos_ui.setFont(font4)
        self.x_stop_pos_ui.setStyleSheet(u"")

        self.horizontalLayout_XRange.addWidget(self.x_stop_pos_ui)

        self.Button_XMoveTo = QPushButton(self.group_Bscan)
        self.Button_XMoveTo.setObjectName(u"Button_XMoveTo")
        self.Button_XMoveTo.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.Button_XMoveTo.sizePolicy().hasHeightForWidth())
        self.Button_XMoveTo.setSizePolicy(sizePolicy3)
        self.Button_XMoveTo.setMinimumSize(QSize(0, 20))
        self.Button_XMoveTo.setMaximumSize(QSize(16777215, 20))
        self.Button_XMoveTo.setFont(font4)

        self.horizontalLayout_XRange.addWidget(self.Button_XMoveTo)


        self.verticalLayout__XScanParams.addLayout(self.horizontalLayout_XRange)

        self.horizontalLayout_XStep = QHBoxLayout()
        self.horizontalLayout_XStep.setObjectName(u"horizontalLayout_XStep")
        self.label_XStep = QLabel(self.group_Bscan)
        self.label_XStep.setObjectName(u"label_XStep")
        self.label_XStep.setMinimumSize(QSize(0, 15))
        self.label_XStep.setFont(font2)
        self.label_XStep.setStyleSheet(u"")

        self.horizontalLayout_XStep.addWidget(self.label_XStep)

        self.x_step_ui = QLineEdit(self.group_Bscan)
        self.x_step_ui.setObjectName(u"x_step_ui")
        self.x_step_ui.setMinimumSize(QSize(0, 20))
        self.x_step_ui.setFont(font4)
        self.x_step_ui.setStyleSheet(u"")

        self.horizontalLayout_XStep.addWidget(self.x_step_ui)


        self.verticalLayout__XScanParams.addLayout(self.horizontalLayout_XStep)

        self.horizontalLayout_bscan_buttons = QHBoxLayout()
        self.horizontalLayout_bscan_buttons.setObjectName(u"horizontalLayout_bscan_buttons")
        self.Bscan_MeasureButton = QPushButton(self.group_Bscan)
        self.Bscan_MeasureButton.setObjectName(u"Bscan_MeasureButton")
        self.Bscan_MeasureButton.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.Bscan_MeasureButton.sizePolicy().hasHeightForWidth())
        self.Bscan_MeasureButton.setSizePolicy(sizePolicy3)
        self.Bscan_MeasureButton.setMinimumSize(QSize(0, 20))
        self.Bscan_MeasureButton.setMaximumSize(QSize(16777215, 20))
        self.Bscan_MeasureButton.setFont(font3)
        self.Bscan_MeasureButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.Bscan_MeasureButton.setMouseTracking(False)
        self.Bscan_MeasureButton.setFocusPolicy(Qt.StrongFocus)
        self.Bscan_MeasureButton.setStyleSheet(u"")
        self.Bscan_MeasureButton.setCheckable(False)
        self.Bscan_MeasureButton.setAutoRepeat(False)
        self.Bscan_MeasureButton.setAutoDefault(False)
        self.Bscan_MeasureButton.setFlat(False)

        self.horizontalLayout_bscan_buttons.addWidget(self.Bscan_MeasureButton)

        self.ContinousBscancheckBox = QCheckBox(self.group_Bscan)
        self.ContinousBscancheckBox.setObjectName(u"ContinousBscancheckBox")
        self.ContinousBscancheckBox.setFont(font2)

        self.horizontalLayout_bscan_buttons.addWidget(self.ContinousBscancheckBox)


        self.verticalLayout__XScanParams.addLayout(self.horizontalLayout_bscan_buttons)


        self.horizontalLayout_XScanParams.addLayout(self.verticalLayout__XScanParams)


        self.verticalLayout_17.addLayout(self.horizontalLayout_XScanParams)


        self.gridLayout_10.addWidget(self.group_Bscan, 0, 0, 1, 1)

        self.group_Cscan = QGroupBox(self.group_Scanning)
        self.group_Cscan.setObjectName(u"group_Cscan")
        sizePolicy4.setHeightForWidth(self.group_Cscan.sizePolicy().hasHeightForWidth())
        self.group_Cscan.setSizePolicy(sizePolicy4)
        self.horizontalLayout_32 = QHBoxLayout(self.group_Cscan)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.verticalLayout_YScanParams = QVBoxLayout()
        self.verticalLayout_YScanParams.setObjectName(u"verticalLayout_YScanParams")
        self.horizontalLayout_YScanParams = QHBoxLayout()
        self.horizontalLayout_YScanParams.setObjectName(u"horizontalLayout_YScanParams")
        self.label_YscanStep = QLabel(self.group_Cscan)
        self.label_YscanStep.setObjectName(u"label_YscanStep")
        sizePolicy.setHeightForWidth(self.label_YscanStep.sizePolicy().hasHeightForWidth())
        self.label_YscanStep.setSizePolicy(sizePolicy)
        self.label_YscanStep.setMinimumSize(QSize(1, 15))
        self.label_YscanStep.setFont(font2)

        self.horizontalLayout_YScanParams.addWidget(self.label_YscanStep)


        self.verticalLayout_YScanParams.addLayout(self.horizontalLayout_YScanParams)

        self.horizontalLayout_YScanRange = QHBoxLayout()
        self.horizontalLayout_YScanRange.setObjectName(u"horizontalLayout_YScanRange")
        self.ui_y_start_pos = QLineEdit(self.group_Cscan)
        self.ui_y_start_pos.setObjectName(u"ui_y_start_pos")
        self.ui_y_start_pos.setMinimumSize(QSize(0, 20))
        self.ui_y_start_pos.setFont(font4)

        self.horizontalLayout_YScanRange.addWidget(self.ui_y_start_pos)

        self.ui_y_stop_pos = QLineEdit(self.group_Cscan)
        self.ui_y_stop_pos.setObjectName(u"ui_y_stop_pos")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.ui_y_stop_pos.sizePolicy().hasHeightForWidth())
        self.ui_y_stop_pos.setSizePolicy(sizePolicy6)
        self.ui_y_stop_pos.setMinimumSize(QSize(5, 20))
        self.ui_y_stop_pos.setFont(font4)

        self.horizontalLayout_YScanRange.addWidget(self.ui_y_stop_pos)


        self.verticalLayout_YScanParams.addLayout(self.horizontalLayout_YScanRange)

        self.horizontalLayout_YStep = QHBoxLayout()
        self.horizontalLayout_YStep.setObjectName(u"horizontalLayout_YStep")
        self.label_Ystep = QLabel(self.group_Cscan)
        self.label_Ystep.setObjectName(u"label_Ystep")
        sizePolicy.setHeightForWidth(self.label_Ystep.sizePolicy().hasHeightForWidth())
        self.label_Ystep.setSizePolicy(sizePolicy)
        self.label_Ystep.setMinimumSize(QSize(0, 15))
        self.label_Ystep.setFont(font2)

        self.horizontalLayout_YStep.addWidget(self.label_Ystep)

        self.y_step = QLineEdit(self.group_Cscan)
        self.y_step.setObjectName(u"y_step")
        sizePolicy6.setHeightForWidth(self.y_step.sizePolicy().hasHeightForWidth())
        self.y_step.setSizePolicy(sizePolicy6)
        self.y_step.setMinimumSize(QSize(5, 20))
        self.y_step.setFont(font4)

        self.horizontalLayout_YStep.addWidget(self.y_step)


        self.verticalLayout_YScanParams.addLayout(self.horizontalLayout_YStep)

        self.horizontalLayout_YStageAndMeas = QHBoxLayout()
        self.horizontalLayout_YStageAndMeas.setObjectName(u"horizontalLayout_YStageAndMeas")
        self.InitializeYstageButton = QPushButton(self.group_Cscan)
        self.InitializeYstageButton.setObjectName(u"InitializeYstageButton")
        sizePolicy3.setHeightForWidth(self.InitializeYstageButton.sizePolicy().hasHeightForWidth())
        self.InitializeYstageButton.setSizePolicy(sizePolicy3)
        self.InitializeYstageButton.setMinimumSize(QSize(0, 20))
        self.InitializeYstageButton.setMaximumSize(QSize(16777215, 20))
        self.InitializeYstageButton.setFont(font3)
        self.InitializeYstageButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_YStageAndMeas.addWidget(self.InitializeYstageButton)

        self.StartCscanButton = QPushButton(self.group_Cscan)
        self.StartCscanButton.setObjectName(u"StartCscanButton")
        self.StartCscanButton.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.StartCscanButton.sizePolicy().hasHeightForWidth())
        self.StartCscanButton.setSizePolicy(sizePolicy3)
        self.StartCscanButton.setMinimumSize(QSize(0, 20))
        self.StartCscanButton.setMaximumSize(QSize(16777215, 20))
        self.StartCscanButton.setFont(font3)
        self.StartCscanButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_YStageAndMeas.addWidget(self.StartCscanButton)


        self.verticalLayout_YScanParams.addLayout(self.horizontalLayout_YStageAndMeas)


        self.horizontalLayout_32.addLayout(self.verticalLayout_YScanParams)

        self.verticalLayout_YStageRoughControl = QVBoxLayout()
        self.verticalLayout_YStageRoughControl.setObjectName(u"verticalLayout_YStageRoughControl")
        self.label = QLabel(self.group_Cscan)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 15))
        font5 = QFont()
        font5.setPointSize(8)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setStrikeOut(False)
        font5.setKerning(True)
        self.label.setFont(font5)
#if QT_CONFIG(statustip)
        self.label.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_YStageRoughControl.addWidget(self.label)

        self.YStageMoveToButton = QPushButton(self.group_Cscan)
        self.YStageMoveToButton.setObjectName(u"YStageMoveToButton")
        self.YStageMoveToButton.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.YStageMoveToButton.sizePolicy().hasHeightForWidth())
        self.YStageMoveToButton.setSizePolicy(sizePolicy3)
        self.YStageMoveToButton.setMinimumSize(QSize(0, 20))
        self.YStageMoveToButton.setMaximumSize(QSize(16777215, 20))
        self.YStageMoveToButton.setFont(font4)

        self.verticalLayout_YStageRoughControl.addWidget(self.YStageMoveToButton)

        self.YStageUpButton = QPushButton(self.group_Cscan)
        self.YStageUpButton.setObjectName(u"YStageUpButton")
        self.YStageUpButton.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.YStageUpButton.sizePolicy().hasHeightForWidth())
        self.YStageUpButton.setSizePolicy(sizePolicy3)
        self.YStageUpButton.setMinimumSize(QSize(0, 20))
        self.YStageUpButton.setMaximumSize(QSize(16777215, 20))
        self.YStageUpButton.setFont(font4)
        self.YStageUpButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_YStageRoughControl.addWidget(self.YStageUpButton)

        self.YStageDownButton = QPushButton(self.group_Cscan)
        self.YStageDownButton.setObjectName(u"YStageDownButton")
        self.YStageDownButton.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.YStageDownButton.sizePolicy().hasHeightForWidth())
        self.YStageDownButton.setSizePolicy(sizePolicy3)
        self.YStageDownButton.setMinimumSize(QSize(0, 20))
        self.YStageDownButton.setMaximumSize(QSize(16777215, 20))
        self.YStageDownButton.setFont(font4)
        self.YStageDownButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_YStageRoughControl.addWidget(self.YStageDownButton)


        self.horizontalLayout_32.addLayout(self.verticalLayout_YStageRoughControl)


        self.gridLayout_10.addWidget(self.group_Cscan, 0, 1, 1, 1)

        self.horizontalLayout_MeasurementProgress = QHBoxLayout()
        self.horizontalLayout_MeasurementProgress.setObjectName(u"horizontalLayout_MeasurementProgress")
        self.MeasurementProgressLine = QLabel(self.group_Scanning)
        self.MeasurementProgressLine.setObjectName(u"MeasurementProgressLine")
        sizePolicy.setHeightForWidth(self.MeasurementProgressLine.sizePolicy().hasHeightForWidth())
        self.MeasurementProgressLine.setSizePolicy(sizePolicy)
        self.MeasurementProgressLine.setMinimumSize(QSize(0, 15))
        self.MeasurementProgressLine.setMaximumSize(QSize(16777215, 16777215))
        self.MeasurementProgressLine.setFont(font2)

        self.horizontalLayout_MeasurementProgress.addWidget(self.MeasurementProgressLine)

        self.scanprogressBar = QProgressBar(self.group_Scanning)
        self.scanprogressBar.setObjectName(u"scanprogressBar")
        self.scanprogressBar.setMinimumSize(QSize(0, 15))
        self.scanprogressBar.setStyleSheet(u"")
        self.scanprogressBar.setValue(0)

        self.horizontalLayout_MeasurementProgress.addWidget(self.scanprogressBar)

        self.StopButton = QPushButton(self.group_Scanning)
        self.StopButton.setObjectName(u"StopButton")
        sizePolicy3.setHeightForWidth(self.StopButton.sizePolicy().hasHeightForWidth())
        self.StopButton.setSizePolicy(sizePolicy3)
        self.StopButton.setMinimumSize(QSize(0, 20))
        self.StopButton.setMaximumSize(QSize(16777215, 20))
        self.StopButton.setFont(font3)
        self.StopButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_MeasurementProgress.addWidget(self.StopButton)


        self.gridLayout_10.addLayout(self.horizontalLayout_MeasurementProgress, 1, 0, 1, 2)


        self.gridMain.addWidget(self.group_Scanning, 1, 1, 1, 1)


        self.horizontalLayout_20.addLayout(self.gridMain)

        self.Layout_Parameters = QVBoxLayout()
        self.Layout_Parameters.setObjectName(u"Layout_Parameters")
        self.Layout_Parameters.setSizeConstraint(QLayout.SetMinimumSize)
        self.groupBox_InitAndLogs = QGroupBox(self.centralwidget)
        self.groupBox_InitAndLogs.setObjectName(u"groupBox_InitAndLogs")
        sizePolicy5.setHeightForWidth(self.groupBox_InitAndLogs.sizePolicy().hasHeightForWidth())
        self.groupBox_InitAndLogs.setSizePolicy(sizePolicy5)
        self.groupBox_InitAndLogs.setMinimumSize(QSize(200, 200))
        self.groupBox_InitAndLogs.setMaximumSize(QSize(350, 16777215))
        self.groupBox_InitAndLogs.setFont(font1)
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_InitAndLogs)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.InitButton = QPushButton(self.groupBox_InitAndLogs)
        self.InitButton.setObjectName(u"InitButton")
        sizePolicy4.setHeightForWidth(self.InitButton.sizePolicy().hasHeightForWidth())
        self.InitButton.setSizePolicy(sizePolicy4)
        self.InitButton.setMinimumSize(QSize(0, 24))
        self.InitButton.setMaximumSize(QSize(16777215, 20))
        self.InitButton.setFont(font3)
        self.InitButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.InitButton.setMouseTracking(False)
        self.InitButton.setFocusPolicy(Qt.StrongFocus)
        self.InitButton.setStyleSheet(u"")
        self.InitButton.setCheckable(False)
        self.InitButton.setAutoRepeat(False)
        self.InitButton.setAutoDefault(False)
        self.InitButton.setFlat(False)

        self.verticalLayout_16.addWidget(self.InitButton)

        self.logbrowser = QTextBrowser(self.groupBox_InitAndLogs)
        self.logbrowser.setObjectName(u"logbrowser")
        self.logbrowser.setMinimumSize(QSize(150, 50))
        self.logbrowser.setMaximumSize(QSize(350, 16777215))

        self.verticalLayout_16.addWidget(self.logbrowser)


        self.Layout_Parameters.addWidget(self.groupBox_InitAndLogs)

        self.group_AcquisitionParameters = QGroupBox(self.centralwidget)
        self.group_AcquisitionParameters.setObjectName(u"group_AcquisitionParameters")
        sizePolicy4.setHeightForWidth(self.group_AcquisitionParameters.sizePolicy().hasHeightForWidth())
        self.group_AcquisitionParameters.setSizePolicy(sizePolicy4)
        self.group_AcquisitionParameters.setMinimumSize(QSize(100, 0))
        self.group_AcquisitionParameters.setMaximumSize(QSize(350, 16777215))
        self.group_AcquisitionParameters.setFont(font1)
        self.group_AcquisitionParameters.setMouseTracking(False)
        self.group_AcquisitionParameters.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.group_AcquisitionParameters)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_AcquisitionParameters = QVBoxLayout()
        self.verticalLayout_AcquisitionParameters.setObjectName(u"verticalLayout_AcquisitionParameters")
        self.horizontalLayout_Param1 = QHBoxLayout()
        self.horizontalLayout_Param1.setObjectName(u"horizontalLayout_Param1")
        self.label_param1 = QLabel(self.group_AcquisitionParameters)
        self.label_param1.setObjectName(u"label_param1")
        self.label_param1.setMinimumSize(QSize(0, 15))
        self.label_param1.setFont(font1)
        self.label_param1.setStyleSheet(u"")

        self.horizontalLayout_Param1.addWidget(self.label_param1)

        self.param1 = QLineEdit(self.group_AcquisitionParameters)
        self.param1.setObjectName(u"param1")
        self.param1.setMinimumSize(QSize(0, 20))
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setStrikeOut(False)
        font6.setKerning(False)
        self.param1.setFont(font6)
        self.param1.setStyleSheet(u"")

        self.horizontalLayout_Param1.addWidget(self.param1)


        self.verticalLayout_AcquisitionParameters.addLayout(self.horizontalLayout_Param1)

        self.horizontalLayout_TrigDelay = QHBoxLayout()
        self.horizontalLayout_TrigDelay.setObjectName(u"horizontalLayout_TrigDelay")
        self.label_delay = QLabel(self.group_AcquisitionParameters)
        self.label_delay.setObjectName(u"label_delay")
        self.label_delay.setMinimumSize(QSize(0, 15))
        self.label_delay.setFont(font1)
        self.label_delay.setStyleSheet(u"")

        self.horizontalLayout_TrigDelay.addWidget(self.label_delay)

        self.trig_delay = QLineEdit(self.group_AcquisitionParameters)
        self.trig_delay.setObjectName(u"trig_delay")
        self.trig_delay.setMinimumSize(QSize(0, 20))
        self.trig_delay.setFont(font6)
        self.trig_delay.setStyleSheet(u"")

        self.horizontalLayout_TrigDelay.addWidget(self.trig_delay)


        self.verticalLayout_AcquisitionParameters.addLayout(self.horizontalLayout_TrigDelay)

        self.horizontalLayout_param2 = QHBoxLayout()
        self.horizontalLayout_param2.setObjectName(u"horizontalLayout_param2")
        self.label_param2 = QLabel(self.group_AcquisitionParameters)
        self.label_param2.setObjectName(u"label_param2")
        self.label_param2.setMinimumSize(QSize(0, 15))
        self.label_param2.setFont(font1)
        self.label_param2.setStyleSheet(u"")

        self.horizontalLayout_param2.addWidget(self.label_param2)

        self.param2 = QLineEdit(self.group_AcquisitionParameters)
        self.param2.setObjectName(u"param2")
        self.param2.setMinimumSize(QSize(0, 20))
        self.param2.setFont(font6)
        self.param2.setStyleSheet(u"")

        self.horizontalLayout_param2.addWidget(self.param2)


        self.verticalLayout_AcquisitionParameters.addLayout(self.horizontalLayout_param2)

        self.ApplyButton = QPushButton(self.group_AcquisitionParameters)
        self.ApplyButton.setObjectName(u"ApplyButton")
        sizePolicy4.setHeightForWidth(self.ApplyButton.sizePolicy().hasHeightForWidth())
        self.ApplyButton.setSizePolicy(sizePolicy4)
        self.ApplyButton.setMinimumSize(QSize(0, 20))
        self.ApplyButton.setMaximumSize(QSize(16777215, 20))
        self.ApplyButton.setFont(font3)
        self.ApplyButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ApplyButton.setStyleSheet(u"")

        self.verticalLayout_AcquisitionParameters.addWidget(self.ApplyButton)


        self.verticalLayout_8.addLayout(self.verticalLayout_AcquisitionParameters)


        self.Layout_Parameters.addWidget(self.group_AcquisitionParameters)

        self.group_OCTParams = QGroupBox(self.centralwidget)
        self.group_OCTParams.setObjectName(u"group_OCTParams")
        sizePolicy4.setHeightForWidth(self.group_OCTParams.sizePolicy().hasHeightForWidth())
        self.group_OCTParams.setSizePolicy(sizePolicy4)
        self.group_OCTParams.setMinimumSize(QSize(200, 0))
        self.group_OCTParams.setMaximumSize(QSize(350, 16777215))
        self.group_OCTParams.setFont(font1)
        self.group_OCTParams.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.group_OCTParams)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_OCTParams = QVBoxLayout()
        self.verticalLayout_OCTParams.setObjectName(u"verticalLayout_OCTParams")
        self.verticalLayout_Averaging = QVBoxLayout()
        self.verticalLayout_Averaging.setObjectName(u"verticalLayout_Averaging")
        self.horizontalLayout_OCTCheckBoxes = QHBoxLayout()
        self.horizontalLayout_OCTCheckBoxes.setObjectName(u"horizontalLayout_OCTCheckBoxes")
        self.AveragingCheckBox = QCheckBox(self.group_OCTParams)
        self.AveragingCheckBox.setObjectName(u"AveragingCheckBox")
        self.AveragingCheckBox.setMinimumSize(QSize(0, 15))
        self.AveragingCheckBox.setFont(font2)
        self.AveragingCheckBox.setStyleSheet(u"")
        self.AveragingCheckBox.setChecked(True)

        self.horizontalLayout_OCTCheckBoxes.addWidget(self.AveragingCheckBox)

        self.ZeroPaddingCheckBox = QCheckBox(self.group_OCTParams)
        self.ZeroPaddingCheckBox.setObjectName(u"ZeroPaddingCheckBox")
        self.ZeroPaddingCheckBox.setEnabled(False)
        self.ZeroPaddingCheckBox.setMinimumSize(QSize(0, 15))
        self.ZeroPaddingCheckBox.setFont(font2)
        self.ZeroPaddingCheckBox.setStyleSheet(u"")

        self.horizontalLayout_OCTCheckBoxes.addWidget(self.ZeroPaddingCheckBox)


        self.verticalLayout_Averaging.addLayout(self.horizontalLayout_OCTCheckBoxes)


        self.verticalLayout_OCTParams.addLayout(self.verticalLayout_Averaging)

        self.horizontalLayout_ATimeSleep = QHBoxLayout()
        self.horizontalLayout_ATimeSleep.setObjectName(u"horizontalLayout_ATimeSleep")
        self.label_idle_time = QLabel(self.group_OCTParams)
        self.label_idle_time.setObjectName(u"label_idle_time")
        self.label_idle_time.setMinimumSize(QSize(0, 15))
        self.label_idle_time.setFont(font2)
        self.label_idle_time.setStyleSheet(u"")

        self.horizontalLayout_ATimeSleep.addWidget(self.label_idle_time)

        self.a_idle_time = QLineEdit(self.group_OCTParams)
        self.a_idle_time.setObjectName(u"a_idle_time")
        self.a_idle_time.setMinimumSize(QSize(0, 20))
        self.a_idle_time.setFont(font4)
        self.a_idle_time.setStyleSheet(u"")

        self.horizontalLayout_ATimeSleep.addWidget(self.a_idle_time)


        self.verticalLayout_OCTParams.addLayout(self.horizontalLayout_ATimeSleep)

        self.horizontalLayout_Averaging = QHBoxLayout()
        self.horizontalLayout_Averaging.setObjectName(u"horizontalLayout_Averaging")
        self.aver_num_label = QLabel(self.group_OCTParams)
        self.aver_num_label.setObjectName(u"aver_num_label")
        self.aver_num_label.setMinimumSize(QSize(0, 15))
        self.aver_num_label.setFont(font2)
        self.aver_num_label.setStyleSheet(u"")

        self.horizontalLayout_Averaging.addWidget(self.aver_num_label)

        self.avg_num_ui = QLineEdit(self.group_OCTParams)
        self.avg_num_ui.setObjectName(u"avg_num_ui")
        self.avg_num_ui.setMinimumSize(QSize(0, 20))
        self.avg_num_ui.setFont(font6)
        self.avg_num_ui.setStyleSheet(u"")

        self.horizontalLayout_Averaging.addWidget(self.avg_num_ui)


        self.verticalLayout_OCTParams.addLayout(self.horizontalLayout_Averaging)

        self.SetOCTParamsButton = QPushButton(self.group_OCTParams)
        self.SetOCTParamsButton.setObjectName(u"SetOCTParamsButton")
        sizePolicy4.setHeightForWidth(self.SetOCTParamsButton.sizePolicy().hasHeightForWidth())
        self.SetOCTParamsButton.setSizePolicy(sizePolicy4)
        self.SetOCTParamsButton.setMinimumSize(QSize(0, 20))
        self.SetOCTParamsButton.setMaximumSize(QSize(16777215, 20))
        self.SetOCTParamsButton.setFont(font3)
        self.SetOCTParamsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.SetOCTParamsButton.setStyleSheet(u"")

        self.verticalLayout_OCTParams.addWidget(self.SetOCTParamsButton)


        self.verticalLayout_7.addLayout(self.verticalLayout_OCTParams)


        self.Layout_Parameters.addWidget(self.group_OCTParams)

        self.group_PostProcessParams = QGroupBox(self.centralwidget)
        self.group_PostProcessParams.setObjectName(u"group_PostProcessParams")
        sizePolicy4.setHeightForWidth(self.group_PostProcessParams.sizePolicy().hasHeightForWidth())
        self.group_PostProcessParams.setSizePolicy(sizePolicy4)
        self.group_PostProcessParams.setMinimumSize(QSize(200, 0))
        self.group_PostProcessParams.setMaximumSize(QSize(350, 16777215))
        self.group_PostProcessParams.setFont(font1)
        self.group_PostProcessParams.setFlat(False)
        self.group_PostProcessParams.setCheckable(False)
        self.verticalLayout_9 = QVBoxLayout(self.group_PostProcessParams)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_PostProcessParams = QVBoxLayout()
        self.verticalLayout_PostProcessParams.setObjectName(u"verticalLayout_PostProcessParams")
        self.horizontalLayout_PresetParams = QHBoxLayout()
        self.horizontalLayout_PresetParams.setObjectName(u"horizontalLayout_PresetParams")
        self.Preset2Radio = QRadioButton(self.group_PostProcessParams)
        self.Preset2Radio.setObjectName(u"Preset2Radio")
        self.Preset2Radio.setMinimumSize(QSize(0, 15))
        self.Preset2Radio.setFont(font2)
        self.Preset2Radio.setStyleSheet(u"")
        self.Preset2Radio.setChecked(False)

        self.horizontalLayout_PresetParams.addWidget(self.Preset2Radio)

        self.Preset1Radio = QRadioButton(self.group_PostProcessParams)
        self.Preset1Radio.setObjectName(u"Preset1Radio")
        self.Preset1Radio.setMinimumSize(QSize(0, 15))
        self.Preset1Radio.setFont(font2)
        self.Preset1Radio.setStyleSheet(u"")
        self.Preset1Radio.setChecked(True)

        self.horizontalLayout_PresetParams.addWidget(self.Preset1Radio)


        self.verticalLayout_PostProcessParams.addLayout(self.horizontalLayout_PresetParams)

        self.label_Bandwidth = QLabel(self.group_PostProcessParams)
        self.label_Bandwidth.setObjectName(u"label_Bandwidth")
        self.label_Bandwidth.setMinimumSize(QSize(0, 15))
        self.label_Bandwidth.setFont(font2)
        self.label_Bandwidth.setStyleSheet(u"")

        self.verticalLayout_PostProcessParams.addWidget(self.label_Bandwidth)

        self.horizontalLayout_Bandwidth = QHBoxLayout()
        self.horizontalLayout_Bandwidth.setObjectName(u"horizontalLayout_Bandwidth")
        self.wave_left_ui = QLineEdit(self.group_PostProcessParams)
        self.wave_left_ui.setObjectName(u"wave_left_ui")
        self.wave_left_ui.setMinimumSize(QSize(0, 20))
        self.wave_left_ui.setFont(font4)
        self.wave_left_ui.setStyleSheet(u"")

        self.horizontalLayout_Bandwidth.addWidget(self.wave_left_ui)

        self.wave_right_ui = QLineEdit(self.group_PostProcessParams)
        self.wave_right_ui.setObjectName(u"wave_right_ui")
        self.wave_right_ui.setMinimumSize(QSize(0, 20))
        self.wave_right_ui.setFont(font4)
        self.wave_right_ui.setStyleSheet(u"")

        self.horizontalLayout_Bandwidth.addWidget(self.wave_right_ui)


        self.verticalLayout_PostProcessParams.addLayout(self.horizontalLayout_Bandwidth)

        self.horizontalLayout_GaussianSigma = QHBoxLayout()
        self.horizontalLayout_GaussianSigma.setObjectName(u"horizontalLayout_GaussianSigma")
        self.label_6 = QLabel(self.group_PostProcessParams)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 15))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"")

        self.horizontalLayout_GaussianSigma.addWidget(self.label_6)

        self.gaussian_std_ui = QLineEdit(self.group_PostProcessParams)
        self.gaussian_std_ui.setObjectName(u"gaussian_std_ui")
        self.gaussian_std_ui.setMinimumSize(QSize(0, 20))
        self.gaussian_std_ui.setFont(font4)
        self.gaussian_std_ui.setStyleSheet(u"")

        self.horizontalLayout_GaussianSigma.addWidget(self.gaussian_std_ui)


        self.verticalLayout_PostProcessParams.addLayout(self.horizontalLayout_GaussianSigma)

        self.horizontalLayout_GaussianWindowPos = QHBoxLayout()
        self.horizontalLayout_GaussianWindowPos.setObjectName(u"horizontalLayout_GaussianWindowPos")
        self.label_GaussianPos = QLabel(self.group_PostProcessParams)
        self.label_GaussianPos.setObjectName(u"label_GaussianPos")
        self.label_GaussianPos.setMinimumSize(QSize(0, 15))
        self.label_GaussianPos.setFont(font2)
        self.label_GaussianPos.setStyleSheet(u"")

        self.horizontalLayout_GaussianWindowPos.addWidget(self.label_GaussianPos)

        self.gaussian_pos_ui = QLineEdit(self.group_PostProcessParams)
        self.gaussian_pos_ui.setObjectName(u"gaussian_pos_ui")
        self.gaussian_pos_ui.setMinimumSize(QSize(0, 20))
        self.gaussian_pos_ui.setFont(font4)
        self.gaussian_pos_ui.setStyleSheet(u"")

        self.horizontalLayout_GaussianWindowPos.addWidget(self.gaussian_pos_ui)


        self.verticalLayout_PostProcessParams.addLayout(self.horizontalLayout_GaussianWindowPos)

        self.SetProcParamsButton = QPushButton(self.group_PostProcessParams)
        self.SetProcParamsButton.setObjectName(u"SetProcParamsButton")
        sizePolicy4.setHeightForWidth(self.SetProcParamsButton.sizePolicy().hasHeightForWidth())
        self.SetProcParamsButton.setSizePolicy(sizePolicy4)
        self.SetProcParamsButton.setMinimumSize(QSize(0, 20))
        self.SetProcParamsButton.setMaximumSize(QSize(16777215, 20))
        self.SetProcParamsButton.setFont(font3)
        self.SetProcParamsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.SetProcParamsButton.setStyleSheet(u"")

        self.verticalLayout_PostProcessParams.addWidget(self.SetProcParamsButton)

        self.ApplyProcButton = QPushButton(self.group_PostProcessParams)
        self.ApplyProcButton.setObjectName(u"ApplyProcButton")
        sizePolicy4.setHeightForWidth(self.ApplyProcButton.sizePolicy().hasHeightForWidth())
        self.ApplyProcButton.setSizePolicy(sizePolicy4)
        self.ApplyProcButton.setMinimumSize(QSize(0, 20))
        self.ApplyProcButton.setMaximumSize(QSize(16777215, 20))
        self.ApplyProcButton.setFont(font3)

        self.verticalLayout_PostProcessParams.addWidget(self.ApplyProcButton)


        self.verticalLayout_9.addLayout(self.verticalLayout_PostProcessParams)


        self.Layout_Parameters.addWidget(self.group_PostProcessParams)

        self.group_ReferencingBox = QGroupBox(self.centralwidget)
        self.group_ReferencingBox.setObjectName(u"group_ReferencingBox")
        sizePolicy4.setHeightForWidth(self.group_ReferencingBox.sizePolicy().hasHeightForWidth())
        self.group_ReferencingBox.setSizePolicy(sizePolicy4)
        self.group_ReferencingBox.setMinimumSize(QSize(200, 0))
        self.group_ReferencingBox.setMaximumSize(QSize(350, 150))
        self.group_ReferencingBox.setFont(font1)
        self.gridLayout_4 = QGridLayout(self.group_ReferencingBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(10)
        self.ReferenceButton = QPushButton(self.group_ReferencingBox)
        self.ReferenceButton.setObjectName(u"ReferenceButton")
        self.ReferenceButton.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.ReferenceButton.sizePolicy().hasHeightForWidth())
        self.ReferenceButton.setSizePolicy(sizePolicy3)
        self.ReferenceButton.setMinimumSize(QSize(0, 20))
        self.ReferenceButton.setMaximumSize(QSize(16777215, 20))
        self.ReferenceButton.setFont(font3)
        self.ReferenceButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ReferenceButton.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.ReferenceButton, 3, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_RefAvergNumber = QLabel(self.group_ReferencingBox)
        self.label_RefAvergNumber.setObjectName(u"label_RefAvergNumber")
        self.label_RefAvergNumber.setMinimumSize(QSize(0, 15))
        self.label_RefAvergNumber.setFont(font2)
        self.label_RefAvergNumber.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.label_RefAvergNumber)

        self.ref_avg_num_ui = QLineEdit(self.group_ReferencingBox)
        self.ref_avg_num_ui.setObjectName(u"ref_avg_num_ui")
        sizePolicy6.setHeightForWidth(self.ref_avg_num_ui.sizePolicy().hasHeightForWidth())
        self.ref_avg_num_ui.setSizePolicy(sizePolicy6)
        self.ref_avg_num_ui.setMinimumSize(QSize(0, 20))
        self.ref_avg_num_ui.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setPointSize(8)
        font7.setBold(True)
        font7.setItalic(False)
        font7.setStrikeOut(False)
        font7.setKerning(False)
        self.ref_avg_num_ui.setFont(font7)
        self.ref_avg_num_ui.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.ref_avg_num_ui)


        self.gridLayout_3.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)

        self.refprogressBar = QProgressBar(self.group_ReferencingBox)
        self.refprogressBar.setObjectName(u"refprogressBar")
        self.refprogressBar.setMinimumSize(QSize(0, 20))
        self.refprogressBar.setStyleSheet(u"")
        self.refprogressBar.setValue(100)

        self.gridLayout_3.addWidget(self.refprogressBar, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.ResetReferenceButton = QPushButton(self.group_ReferencingBox)
        self.ResetReferenceButton.setObjectName(u"ResetReferenceButton")
        sizePolicy3.setHeightForWidth(self.ResetReferenceButton.sizePolicy().hasHeightForWidth())
        self.ResetReferenceButton.setSizePolicy(sizePolicy3)
        self.ResetReferenceButton.setMinimumSize(QSize(0, 20))
        self.ResetReferenceButton.setMaximumSize(QSize(16777215, 20))
        self.ResetReferenceButton.setFont(font3)
        self.ResetReferenceButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ResetReferenceButton.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.ResetReferenceButton, 1, 0, 1, 1)


        self.Layout_Parameters.addWidget(self.group_ReferencingBox)


        self.horizontalLayout_20.addLayout(self.Layout_Parameters)

        self.Layout_Signal = QVBoxLayout()
        self.Layout_Signal.setObjectName(u"Layout_Signal")
        self.raw_signal_plot = PlotWidget(self.centralwidget)
        self.raw_signal_plot.setObjectName(u"raw_signal_plot")
        sizePolicy5.setHeightForWidth(self.raw_signal_plot.sizePolicy().hasHeightForWidth())
        self.raw_signal_plot.setSizePolicy(sizePolicy5)
        self.raw_signal_plot.setMinimumSize(QSize(350, 0))
        self.raw_signal_plot.setMaximumSize(QSize(450, 16777215))

        self.Layout_Signal.addWidget(self.raw_signal_plot)

        self.groupBox_SamplingParams = QGroupBox(self.centralwidget)
        self.groupBox_SamplingParams.setObjectName(u"groupBox_SamplingParams")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.groupBox_SamplingParams.sizePolicy().hasHeightForWidth())
        self.groupBox_SamplingParams.setSizePolicy(sizePolicy7)
        self.groupBox_SamplingParams.setMinimumSize(QSize(100, 5))
        self.groupBox_SamplingParams.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_SamplingParams.setFont(font1)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_SamplingParams)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_AcqRange = QLabel(self.groupBox_SamplingParams)
        self.label_AcqRange.setObjectName(u"label_AcqRange")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_AcqRange.sizePolicy().hasHeightForWidth())
        self.label_AcqRange.setSizePolicy(sizePolicy8)
        self.label_AcqRange.setMinimumSize(QSize(100, 0))
        self.label_AcqRange.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_AcqRange)

        self.horizontalLayout_SamplingRange = QHBoxLayout()
        self.horizontalLayout_SamplingRange.setObjectName(u"horizontalLayout_SamplingRange")
        self.sampling_start_ui = QLineEdit(self.groupBox_SamplingParams)
        self.sampling_start_ui.setObjectName(u"sampling_start_ui")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.sampling_start_ui.sizePolicy().hasHeightForWidth())
        self.sampling_start_ui.setSizePolicy(sizePolicy9)
        self.sampling_start_ui.setMinimumSize(QSize(15, 20))
        self.sampling_start_ui.setFont(font4)

        self.horizontalLayout_SamplingRange.addWidget(self.sampling_start_ui)

        self.sampling_stop_ui = QLineEdit(self.groupBox_SamplingParams)
        self.sampling_stop_ui.setObjectName(u"sampling_stop_ui")
        sizePolicy9.setHeightForWidth(self.sampling_stop_ui.sizePolicy().hasHeightForWidth())
        self.sampling_stop_ui.setSizePolicy(sizePolicy9)
        self.sampling_stop_ui.setMinimumSize(QSize(0, 20))
        self.sampling_stop_ui.setFont(font4)

        self.horizontalLayout_SamplingRange.addWidget(self.sampling_stop_ui)


        self.verticalLayout_10.addLayout(self.horizontalLayout_SamplingRange)

        self.horizontalLayout_SamplingButtons = QHBoxLayout()
        self.horizontalLayout_SamplingButtons.setObjectName(u"horizontalLayout_SamplingButtons")
        self.StopAcqButton = QPushButton(self.groupBox_SamplingParams)
        self.StopAcqButton.setObjectName(u"StopAcqButton")
        sizePolicy3.setHeightForWidth(self.StopAcqButton.sizePolicy().hasHeightForWidth())
        self.StopAcqButton.setSizePolicy(sizePolicy3)
        self.StopAcqButton.setMinimumSize(QSize(15, 20))
        self.StopAcqButton.setMaximumSize(QSize(16777215, 20))
        self.StopAcqButton.setFont(font3)
        self.StopAcqButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.StopAcqButton.setMouseTracking(False)
        self.StopAcqButton.setFocusPolicy(Qt.StrongFocus)
        self.StopAcqButton.setStyleSheet(u"")
        self.StopAcqButton.setCheckable(False)
        self.StopAcqButton.setAutoRepeat(False)
        self.StopAcqButton.setAutoDefault(False)
        self.StopAcqButton.setFlat(False)

        self.horizontalLayout_SamplingButtons.addWidget(self.StopAcqButton)

        self.SetRangeButton = QPushButton(self.groupBox_SamplingParams)
        self.SetRangeButton.setObjectName(u"SetRangeButton")
        sizePolicy3.setHeightForWidth(self.SetRangeButton.sizePolicy().hasHeightForWidth())
        self.SetRangeButton.setSizePolicy(sizePolicy3)
        self.SetRangeButton.setMinimumSize(QSize(15, 20))
        self.SetRangeButton.setMaximumSize(QSize(16777215, 20))
        self.SetRangeButton.setFont(font3)
        self.SetRangeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.SetRangeButton.setMouseTracking(False)
        self.SetRangeButton.setFocusPolicy(Qt.StrongFocus)
        self.SetRangeButton.setStyleSheet(u"")
        self.SetRangeButton.setCheckable(False)
        self.SetRangeButton.setAutoRepeat(False)
        self.SetRangeButton.setAutoDefault(False)
        self.SetRangeButton.setFlat(False)

        self.horizontalLayout_SamplingButtons.addWidget(self.SetRangeButton)


        self.verticalLayout_10.addLayout(self.horizontalLayout_SamplingButtons)


        self.Layout_Signal.addWidget(self.groupBox_SamplingParams)

        self.by_me_section = QHBoxLayout()
        self.by_me_section.setObjectName(u"by_me_section")
        self.verticalLayout_by_me = QVBoxLayout()
        self.verticalLayout_by_me.setSpacing(7)
        self.verticalLayout_by_me.setObjectName(u"verticalLayout_by_me")
        self.by_me = QLabel(self.centralwidget)
        self.by_me.setObjectName(u"by_me")
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.by_me.sizePolicy().hasHeightForWidth())
        self.by_me.setSizePolicy(sizePolicy10)
        font8 = QFont()
        font8.setFamilies([u"MS Shell Dlg 2"])
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setStrikeOut(False)
        self.by_me.setFont(font8)
        self.by_me.setStyleSheet(u"")
        self.by_me.setTextFormat(Qt.PlainText)
        self.by_me.setScaledContents(False)
        self.by_me.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_by_me.addWidget(self.by_me)


        self.by_me_section.addLayout(self.verticalLayout_by_me)

        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QSize(0, 0))
        self.logo.setMaximumSize(QSize(50, 50))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setPixmap(QPixmap(u"icon.ico"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.logo.setMargin(5)

        self.by_me_section.addWidget(self.logo)


        self.Layout_Signal.addLayout(self.by_me_section)


        self.horizontalLayout_20.addLayout(self.Layout_Signal)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 18))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuHelp.addAction(self.actionAbout)
        self.menuTools.addAction(self.actionVolumetric_plotter)

        self.retranslateUi(MainWindow)

        self.Bscan_MeasureButton.setDefault(False)
        self.InitButton.setDefault(False)
        self.StopAcqButton.setDefault(False)
        self.SetRangeButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"OCTControl", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save parameters", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(shortcut)
        self.actionAbout.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+H", None))
#endif // QT_CONFIG(shortcut)
        self.actionVolumetric_plotter.setText(QCoreApplication.translate("MainWindow", u"Volume viewer", None))
        self.group_VisualizationSaving.setTitle(QCoreApplication.translate("MainWindow", u"Visualization and saving", None))
        self.label_Aspect.setText(QCoreApplication.translate("MainWindow", u"Aspect Ratio", None))
        self.aspect_ratio.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_Log10Coef.setText(QCoreApplication.translate("MainWindow", u"LOG10 Factor ", None))
        self.log10_coef.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.filenameline.setText(QCoreApplication.translate("MainWindow", u"scan", None))
        self.FolderButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_DirName.setText(QCoreApplication.translate("MainWindow", u"File directory", None))
        self.SaveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.PlotButton.setText(QCoreApplication.translate("MainWindow", u"Plot scan", None))
        self.label_FileName.setText(QCoreApplication.translate("MainWindow", u"Filename", None))
        self.group_Scanning.setTitle(QCoreApplication.translate("MainWindow", u"Scanning", None))
        self.group_Bscan.setTitle(QCoreApplication.translate("MainWindow", u"B-scan", None))
        self.scan_label.setText(QCoreApplication.translate("MainWindow", u"X scanning interval (mm)", None))
        self.x_start_pos_ui.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.x_stop_pos_ui.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Button_XMoveTo.setText(QCoreApplication.translate("MainWindow", u"Move to", None))
        self.label_XStep.setText(QCoreApplication.translate("MainWindow", u"X scanning step (mm)", None))
        self.x_step_ui.setText(QCoreApplication.translate("MainWindow", u"0.04", None))
        self.Bscan_MeasureButton.setText(QCoreApplication.translate("MainWindow", u"B-scan measure", None))
#if QT_CONFIG(shortcut)
        self.Bscan_MeasureButton.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.ContinousBscancheckBox.setText(QCoreApplication.translate("MainWindow", u"Continous measurement", None))
        self.group_Cscan.setTitle(QCoreApplication.translate("MainWindow", u"Volume scan", None))
        self.label_YscanStep.setText(QCoreApplication.translate("MainWindow", u"Y scanning interval (mm)", None))
        self.ui_y_start_pos.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.ui_y_stop_pos.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_Ystep.setText(QCoreApplication.translate("MainWindow", u"Y scanning step (mm)", None))
        self.y_step.setText(QCoreApplication.translate("MainWindow", u"0.04", None))
        self.InitializeYstageButton.setText(QCoreApplication.translate("MainWindow", u"Initialize Y stage", None))
        self.StartCscanButton.setText(QCoreApplication.translate("MainWindow", u"Start 3D scan", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Y stage", None))
        self.YStageMoveToButton.setText(QCoreApplication.translate("MainWindow", u"Move to", None))
        self.YStageUpButton.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.YStageDownButton.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.MeasurementProgressLine.setText(QCoreApplication.translate("MainWindow", u"Measurement progress", None))
        self.StopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.groupBox_InitAndLogs.setTitle(QCoreApplication.translate("MainWindow", u"Initialization and logs", None))
        self.InitButton.setText(QCoreApplication.translate("MainWindow", u"Initialize", None))
#if QT_CONFIG(shortcut)
        self.InitButton.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.logbrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">Initialization required</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p></body></html>", None))
        self.group_AcquisitionParameters.setTitle(QCoreApplication.translate("MainWindow", u"Acquisition parameters", None))
        self.label_param1.setText(QCoreApplication.translate("MainWindow", u"PARAM1", None))
        self.param1.setText(QCoreApplication.translate("MainWindow", u"1024", None))
        self.label_delay.setText(QCoreApplication.translate("MainWindow", u"TRIG. DELAY", None))
        self.trig_delay.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_param2.setText(QCoreApplication.translate("MainWindow", u"PARAM2", None))
        self.param2.setText(QCoreApplication.translate("MainWindow", u"256", None))
        self.ApplyButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.group_OCTParams.setTitle(QCoreApplication.translate("MainWindow", u"Scanning parameters", None))
        self.AveragingCheckBox.setText(QCoreApplication.translate("MainWindow", u"Averaging", None))
        self.ZeroPaddingCheckBox.setText(QCoreApplication.translate("MainWindow", u"Zero padding", None))
        self.label_idle_time.setText(QCoreApplication.translate("MainWindow", u"A-scan idle (s)", None))
        self.a_idle_time.setText(QCoreApplication.translate("MainWindow", u"0.2", None))
        self.aver_num_label.setText(QCoreApplication.translate("MainWindow", u"Averaging", None))
        self.avg_num_ui.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.SetOCTParamsButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.group_PostProcessParams.setTitle(QCoreApplication.translate("MainWindow", u"Post-processing", None))
        self.Preset2Radio.setText(QCoreApplication.translate("MainWindow", u"PRESET2", None))
        self.Preset1Radio.setText(QCoreApplication.translate("MainWindow", u"PRESET1", None))
        self.label_Bandwidth.setText(QCoreApplication.translate("MainWindow", u"Sampling bandwidth (nm)", None))
        self.wave_left_ui.setText(QCoreApplication.translate("MainWindow", u"3235", None))
        self.wave_right_ui.setText(QCoreApplication.translate("MainWindow", u"4220", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Gaussian sigma (spl)", None))
        self.gaussian_std_ui.setText(QCoreApplication.translate("MainWindow", u"1500", None))
        self.label_GaussianPos.setText(QCoreApplication.translate("MainWindow", u"Window position", None))
        self.gaussian_pos_ui.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.SetProcParamsButton.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.ApplyProcButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.group_ReferencingBox.setTitle(QCoreApplication.translate("MainWindow", u"Referenceing", None))
        self.ReferenceButton.setText(QCoreApplication.translate("MainWindow", u"Referencing", None))
        self.label_RefAvergNumber.setText(QCoreApplication.translate("MainWindow", u"Spectra integrated (num)    ", None))
        self.ref_avg_num_ui.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.ResetReferenceButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.groupBox_SamplingParams.setTitle(QCoreApplication.translate("MainWindow", u"Spectra aquisition", None))
        self.label_AcqRange.setText(QCoreApplication.translate("MainWindow", u"Range in samples", None))
        self.sampling_start_ui.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.sampling_stop_ui.setText(QCoreApplication.translate("MainWindow", u"16384", None))
        self.StopAcqButton.setText(QCoreApplication.translate("MainWindow", u"Unused Button", None))
#if QT_CONFIG(shortcut)
        self.StopAcqButton.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.SetRangeButton.setText(QCoreApplication.translate("MainWindow", u"Set range", None))
#if QT_CONFIG(shortcut)
        self.SetRangeButton.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.by_me.setText(QCoreApplication.translate("MainWindow", u"2023 by Ivan Zorin", None))
        self.logo.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

