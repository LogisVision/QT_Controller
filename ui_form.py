# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSlider, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 608)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 10, 991, 521))
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.btn_right = QPushButton(self.tab)
        self.btn_right.setObjectName(u"btn_right")
        self.btn_right.setGeometry(QRect(270, 350, 121, 51))
        font = QFont()
        font.setPointSize(20)
        self.btn_right.setFont(font)
        self.btn_mid = QPushButton(self.tab)
        self.btn_mid.setObjectName(u"btn_mid")
        self.btn_mid.setGeometry(QRect(140, 350, 121, 51))
        self.btn_mid.setFont(font)
        self.btn_go = QPushButton(self.tab)
        self.btn_go.setObjectName(u"btn_go")
        self.btn_go.setGeometry(QRect(140, 290, 121, 51))
        self.btn_go.setFont(font)
        self.btn_left = QPushButton(self.tab)
        self.btn_left.setObjectName(u"btn_left")
        self.btn_left.setGeometry(QRect(10, 350, 121, 51))
        self.btn_left.setFont(font)
        self.btn_back = QPushButton(self.tab)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(140, 410, 121, 51))
        self.btn_back.setFont(font)
        self.slider_cam = QSlider(self.tab)
        self.slider_cam.setObjectName(u"slider_cam")
        self.slider_cam.setGeometry(QRect(760, 250, 51, 160))
        self.slider_cam.setStyleSheet(u"QSlider::handle:vertical {\n"
"    width: 15px; /* \uc6d0\ud558\ub294 \uac00\ub85c \ud06c\uae30 */\n"
"    height: 15px; /* \uc6d0\ud558\ub294 \uc138\ub85c \ud06c\uae30 */\n"
"    background-color: white; /* \ud578\ub4e4 \uc0c9\uc0c1 */\n"
"    border-radius: 7px; /* \ub465\uadfc \ubaa8\uc11c\ub9ac */\n"
"}")
        self.slider_cam.setMinimum(-40)
        self.slider_cam.setMaximum(25)
        self.slider_cam.setSingleStep(1)
        self.slider_cam.setValue(-7)
        self.slider_cam.setSliderPosition(-7)
        self.slider_cam.setTracking(True)
        self.slider_cam.setOrientation(Qt.Orientation.Vertical)
        self.slider_cam.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.label_angle = QLabel(self.tab)
        self.label_angle.setObjectName(u"label_angle")
        self.label_angle.setGeometry(QRect(740, 420, 81, 21))
        self.label_angle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.slider_arm_1 = QSlider(self.tab)
        self.slider_arm_1.setObjectName(u"slider_arm_1")
        self.slider_arm_1.setGeometry(QRect(830, 250, 51, 160))
        self.slider_arm_1.setStyleSheet(u"QSlider::handle:vertical {\n"
"    width: 15px; /* \uc6d0\ud558\ub294 \uac00\ub85c \ud06c\uae30 */\n"
"    height: 15px; /* \uc6d0\ud558\ub294 \uc138\ub85c \ud06c\uae30 */\n"
"    background-color: white; /* \ud578\ub4e4 \uc0c9\uc0c1 */\n"
"    border-radius: 7px; /* \ub465\uadfc \ubaa8\uc11c\ub9ac */\n"
"}")
        self.slider_arm_1.setMinimum(85)
        self.slider_arm_1.setMaximum(500)
        self.slider_arm_1.setPageStep(1)
        self.slider_arm_1.setValue(100)
        self.slider_arm_1.setSliderPosition(100)
        self.slider_arm_1.setOrientation(Qt.Orientation.Vertical)
        self.slider_arm_1.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.label_arm_1 = QLabel(self.tab)
        self.label_arm_1.setObjectName(u"label_arm_1")
        self.label_arm_1.setGeometry(QRect(810, 420, 81, 21))
        self.label_arm_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_arm_2 = QLabel(self.tab)
        self.label_arm_2.setObjectName(u"label_arm_2")
        self.label_arm_2.setGeometry(QRect(880, 420, 81, 21))
        self.label_arm_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.slider_arm_2 = QSlider(self.tab)
        self.slider_arm_2.setObjectName(u"slider_arm_2")
        self.slider_arm_2.setGeometry(QRect(900, 250, 51, 160))
        self.slider_arm_2.setStyleSheet(u"QSlider::handle:vertical {\n"
"    width: 15px; /* \uc6d0\ud558\ub294 \uac00\ub85c \ud06c\uae30 */\n"
"    height: 15px; /* \uc6d0\ud558\ub294 \uc138\ub85c \ud06c\uae30 */\n"
"    background-color: white; /* \ud578\ub4e4 \uc0c9\uc0c1 */\n"
"    border-radius: 7px; /* \ub465\uadfc \ubaa8\uc11c\ub9ac */\n"
"}")
        self.slider_arm_2.setMinimum(-50)
        self.slider_arm_2.setMaximum(50)
        self.slider_arm_2.setPageStep(10)
        self.slider_arm_2.setOrientation(Qt.Orientation.Vertical)
        self.slider_arm_2.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider_grab = QSlider(self.tab)
        self.slider_grab.setObjectName(u"slider_grab")
        self.slider_grab.setGeometry(QRect(440, 320, 261, 41))
        self.slider_grab.setStyleSheet(u"QSlider::handle:horizontal {\n"
"    width: 15px; /* \uc6d0\ud558\ub294 \uac00\ub85c \ud06c\uae30 */\n"
"    height: 15px; /* \uc6d0\ud558\ub294 \uc138\ub85c \ud06c\uae30 */\n"
"    background-color: white; /* \ud578\ub4e4 \uc0c9\uc0c1 */\n"
"    border-radius: 7px; /* \ub465\uadfc \ubaa8\uc11c\ub9ac */\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    width: 15px; /* \uc6d0\ud558\ub294 \uac00\ub85c \ud06c\uae30 */\n"
"    height: 15px; /* \uc6d0\ud558\ub294 \uc138\ub85c \ud06c\uae30 */\n"
"    background-color: #3498db; /* \ud578\ub4e4 \uc0c9\uc0c1 */\n"
"    border-radius: 7px; /* \ub465\uadfc \ubaa8\uc11c\ub9ac */\n"
"}")
        self.slider_grab.setMinimum(0)
        self.slider_grab.setMaximum(90)
        self.slider_grab.setSliderPosition(0)
        self.slider_grab.setOrientation(Qt.Orientation.Horizontal)
        self.slider_grab.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider_grab.setTickInterval(20)
        self.label_cam_angle = QLabel(self.tab)
        self.label_cam_angle.setObjectName(u"label_cam_angle")
        self.label_cam_angle.setGeometry(QRect(760, 220, 51, 20))
        self.label_cam_angle.setStyleSheet(u"background-color:white;")
        self.label_cam_angle.setFrameShape(QFrame.Shape.NoFrame)
        self.label_cam_angle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_arm_1_value = QLabel(self.tab)
        self.label_arm_1_value.setObjectName(u"label_arm_1_value")
        self.label_arm_1_value.setGeometry(QRect(830, 220, 51, 20))
        self.label_arm_1_value.setStyleSheet(u"background-color:white;")
        self.label_arm_1_value.setFrameShape(QFrame.Shape.NoFrame)
        self.label_arm_1_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_arm_2_value = QLabel(self.tab)
        self.label_arm_2_value.setObjectName(u"label_arm_2_value")
        self.label_arm_2_value.setGeometry(QRect(900, 220, 51, 20))
        self.label_arm_2_value.setStyleSheet(u"background-color:white;")
        self.label_arm_2_value.setFrameShape(QFrame.Shape.NoFrame)
        self.label_arm_2_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.slider_arm = QSlider(self.tab)
        self.slider_arm.setObjectName(u"slider_arm")
        self.slider_arm.setGeometry(QRect(440, 390, 261, 41))
        self.slider_arm.setStyleSheet(u"QSlider::handle:horizontal {\n"
"    width: 15px; /* \uc6d0\ud558\ub294 \uac00\ub85c \ud06c\uae30 */\n"
"    height: 15px; /* \uc6d0\ud558\ub294 \uc138\ub85c \ud06c\uae30 */\n"
"    background-color: white; /* \ud578\ub4e4 \uc0c9\uc0c1 */\n"
"    border-radius: 7px; /* \ub465\uadfc \ubaa8\uc11c\ub9ac */\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    width: 15px; /* \uc6d0\ud558\ub294 \uac00\ub85c \ud06c\uae30 */\n"
"    height: 15px; /* \uc6d0\ud558\ub294 \uc138\ub85c \ud06c\uae30 */\n"
"    background-color: #3498db; /* \ud578\ub4e4 \uc0c9\uc0c1 */\n"
"    border-radius: 7px; /* \ub465\uadfc \ubaa8\uc11c\ub9ac */\n"
"}")
        self.slider_arm.setMinimum(-80)
        self.slider_arm.setMaximum(80)
        self.slider_arm.setSliderPosition(0)
        self.slider_arm.setOrientation(Qt.Orientation.Horizontal)
        self.slider_arm.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.label_arm_left = QLabel(self.tab)
        self.label_arm_left.setObjectName(u"label_arm_left")
        self.label_arm_left.setGeometry(QRect(410, 430, 81, 21))
        self.label_arm_left.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_arm_right = QLabel(self.tab)
        self.label_arm_right.setObjectName(u"label_arm_right")
        self.label_arm_right.setGeometry(QRect(660, 430, 81, 21))
        self.label_arm_right.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_grab = QLabel(self.tab)
        self.label_grab.setObjectName(u"label_grab")
        self.label_grab.setGeometry(QRect(660, 310, 81, 21))
        self.label_grab.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_auto = QPushButton(self.tab)
        self.btn_auto.setObjectName(u"btn_auto")
        self.btn_auto.setGeometry(QRect(750, 20, 191, 71))
        self.btn_manual = QPushButton(self.tab)
        self.btn_manual.setObjectName(u"btn_manual")
        self.btn_manual.setGeometry(QRect(750, 100, 191, 71))
        self.label_cam = QLabel(self.tab)
        self.label_cam.setObjectName(u"label_cam")
        self.label_cam.setGeometry(QRect(290, 20, 401, 261))
        self.label_cam.setFrameShape(QFrame.Shape.Box)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.widget_web = QWidget(self.tab_2)
        self.widget_web.setObjectName(u"widget_web")
        self.widget_web.setGeometry(QRect(10, 10, 921, 451))
        self.widget_web.setAutoFillBackground(True)
        self.widget_web.setStyleSheet(u"")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.logText = QPlainTextEdit(self.tab_3)
        self.logText.setObjectName(u"logText")
        self.logText.setGeometry(QRect(880, 10, 41, 21))
        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 50, 321, 31))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(580, 40, 189, 41))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sensingText = QPlainTextEdit(self.tab_3)
        self.sensingText.setObjectName(u"sensingText")
        self.sensingText.setGeometry(QRect(880, 50, 51, 31))
        self.stopButton = QPushButton(self.tab_3)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(540, 420, 171, 40))
        self.stopButton.setFont(font)
        self.startButton = QPushButton(self.tab_3)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(260, 420, 187, 40))
        self.startButton.setFont(font)
        self.table_log = QTableWidget(self.tab_3)
        if (self.table_log.columnCount() < 4):
            self.table_log.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_log.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_log.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_log.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_log.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_log.setObjectName(u"table_log")
        self.table_log.setGeometry(QRect(10, 100, 401, 311))
        self.table_log.setColumnCount(4)
        self.table_log.horizontalHeader().setVisible(True)
        self.table_log.horizontalHeader().setHighlightSections(True)
        self.table_sensing = QTableWidget(self.tab_3)
        if (self.table_sensing.columnCount() < 5):
            self.table_sensing.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_sensing.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_sensing.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_sensing.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_sensing.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_sensing.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.table_sensing.setObjectName(u"table_sensing")
        self.table_sensing.setGeometry(QRect(430, 100, 481, 311))
        self.table_sensing.setColumnCount(5)
        self.table_sensing.horizontalHeader().setVisible(True)
        self.table_sensing.horizontalHeader().setHighlightSections(True)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 38))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_left.clicked.connect(MainWindow.left)
        self.btn_right.clicked.connect(MainWindow.right)
        self.btn_go.clicked.connect(MainWindow.go)
        self.btn_mid.clicked.connect(MainWindow.mid)
        self.btn_back.clicked.connect(MainWindow.back)
        self.slider_cam.valueChanged.connect(self.label_cam_angle.setNum)
        self.slider_arm_1.valueChanged.connect(self.label_arm_1_value.setNum)
        self.slider_arm_2.valueChanged.connect(self.label_arm_2_value.setNum)
        self.slider_cam.valueChanged.connect(MainWindow.camera_angle)
        self.slider_grab.valueChanged.connect(MainWindow.grab)
        self.slider_arm.valueChanged.connect(MainWindow.turn_angle)
        self.slider_arm_1.valueChanged.connect(MainWindow.arm_1)
        self.slider_arm_2.valueChanged.connect(MainWindow.arm_2)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_right.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.btn_mid.setText(QCoreApplication.translate("MainWindow", u"Mid", None))
        self.btn_go.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.btn_left.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_angle.setText(QCoreApplication.translate("MainWindow", u"CAM Angle", None))
        self.label_arm_1.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_arm_2.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_cam_angle.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_arm_1_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_arm_2_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_arm_left.setText(QCoreApplication.translate("MainWindow", u"LEFT", None))
        self.label_arm_right.setText(QCoreApplication.translate("MainWindow", u"RIGHT", None))
        self.label_grab.setText(QCoreApplication.translate("MainWindow", u"GRAB", None))
        self.btn_auto.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.btn_manual.setText(QCoreApplication.translate("MainWindow", u"MANUAL", None))
        self.label_cam.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"MAIN", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"DATA BASE", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"command Table", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"sensing Table", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        ___qtablewidgetitem = self.table_log.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem1 = self.table_log.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Command", None));
        ___qtablewidgetitem2 = self.table_log.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtablewidgetitem3 = self.table_log.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"State", None));
        ___qtablewidgetitem4 = self.table_sensing.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem5 = self.table_sensing.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Num1", None));
        ___qtablewidgetitem6 = self.table_sensing.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Num2", None));
        ___qtablewidgetitem7 = self.table_sensing.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Is_Finish", None));
        ___qtablewidgetitem8 = self.table_sensing.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Mode", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"LOG DATA", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Page", None))
    # retranslateUi

