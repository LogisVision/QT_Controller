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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1246, 674)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tabWidget.setIconSize(QSize(50, 50))
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout_6 = QGridLayout(self.tab_1)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_cam_up = QPushButton(self.tab_1)
        self.btn_cam_up.setObjectName(u"btn_cam_up")
        sizePolicy.setHeightForWidth(self.btn_cam_up.sizePolicy().hasHeightForWidth())
        self.btn_cam_up.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        self.btn_cam_up.setFont(font)

        self.verticalLayout_7.addWidget(self.btn_cam_up)

        self.label_cam_angle = QLabel(self.tab_1)
        self.label_cam_angle.setObjectName(u"label_cam_angle")
        sizePolicy.setHeightForWidth(self.label_cam_angle.sizePolicy().hasHeightForWidth())
        self.label_cam_angle.setSizePolicy(sizePolicy)
        self.label_cam_angle.setStyleSheet(u"background-color:white;")
        self.label_cam_angle.setFrameShape(QFrame.Shape.NoFrame)
        self.label_cam_angle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_cam_angle)

        self.slider_cam = QSlider(self.tab_1)
        self.slider_cam.setObjectName(u"slider_cam")
        sizePolicy.setHeightForWidth(self.slider_cam.sizePolicy().hasHeightForWidth())
        self.slider_cam.setSizePolicy(sizePolicy)
        self.slider_cam.setStyleSheet(u"QSlider::handle:vertical {\n"
"    width: 15px; /* \uc6d0\ud558\ub294 \uac00\ub85c \ud06c\uae30 */\n"
"    height: 20px; /* \uc6d0\ud558\ub294 \uc138\ub85c \ud06c\uae30 */\n"
"    background-color: black; /* \ud578\ub4e4 \uc0c9\uc0c1 */\n"
"    border-radius: 1px; /* \ub465\uadfc \ubaa8\uc11c\ub9ac */\n"
"}")
        self.slider_cam.setMinimum(-40)
        self.slider_cam.setMaximum(25)
        self.slider_cam.setSingleStep(1)
        self.slider_cam.setValue(-7)
        self.slider_cam.setSliderPosition(-7)
        self.slider_cam.setTracking(True)
        self.slider_cam.setOrientation(Qt.Orientation.Vertical)
        self.slider_cam.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.verticalLayout_7.addWidget(self.slider_cam)

        self.label_angle = QLabel(self.tab_1)
        self.label_angle.setObjectName(u"label_angle")
        sizePolicy.setHeightForWidth(self.label_angle.sizePolicy().hasHeightForWidth())
        self.label_angle.setSizePolicy(sizePolicy)
        self.label_angle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_angle)

        self.btn_cam_down = QPushButton(self.tab_1)
        self.btn_cam_down.setObjectName(u"btn_cam_down")
        sizePolicy.setHeightForWidth(self.btn_cam_down.sizePolicy().hasHeightForWidth())
        self.btn_cam_down.setSizePolicy(sizePolicy)
        self.btn_cam_down.setFont(font)

        self.verticalLayout_7.addWidget(self.btn_cam_down)

        self.verticalLayout_7.setStretch(2, 7)

        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_x_up = QPushButton(self.tab_1)
        self.btn_x_up.setObjectName(u"btn_x_up")
        sizePolicy.setHeightForWidth(self.btn_x_up.sizePolicy().hasHeightForWidth())
        self.btn_x_up.setSizePolicy(sizePolicy)
        self.btn_x_up.setFont(font)

        self.verticalLayout_4.addWidget(self.btn_x_up)

        self.label_arm_1_value = QLabel(self.tab_1)
        self.label_arm_1_value.setObjectName(u"label_arm_1_value")
        sizePolicy.setHeightForWidth(self.label_arm_1_value.sizePolicy().hasHeightForWidth())
        self.label_arm_1_value.setSizePolicy(sizePolicy)
        self.label_arm_1_value.setStyleSheet(u"background-color:white;")
        self.label_arm_1_value.setFrameShape(QFrame.Shape.NoFrame)
        self.label_arm_1_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_arm_1_value)

        self.slider_arm_1 = QSlider(self.tab_1)
        self.slider_arm_1.setObjectName(u"slider_arm_1")
        sizePolicy.setHeightForWidth(self.slider_arm_1.sizePolicy().hasHeightForWidth())
        self.slider_arm_1.setSizePolicy(sizePolicy)
        self.slider_arm_1.setStyleSheet(u"QSlider::handle:vertical {\n"
"    width: 15px; /* \uc6d0\ud558\ub294 \uac00\ub85c \ud06c\uae30 */\n"
"    height: 15px; /* \uc6d0\ud558\ub294 \uc138\ub85c \ud06c\uae30 */\n"
"    background-color: black; /* \ud578\ub4e4 \uc0c9\uc0c1 */\n"
"    border-radius: 7px; /* \ub465\uadfc \ubaa8\uc11c\ub9ac */\n"
"}")
        self.slider_arm_1.setMinimum(-90)
        self.slider_arm_1.setMaximum(90)
        self.slider_arm_1.setPageStep(1)
        self.slider_arm_1.setValue(0)
        self.slider_arm_1.setSliderPosition(0)
        self.slider_arm_1.setOrientation(Qt.Orientation.Vertical)
        self.slider_arm_1.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.verticalLayout_4.addWidget(self.slider_arm_1)

        self.label_arm_1 = QLabel(self.tab_1)
        self.label_arm_1.setObjectName(u"label_arm_1")
        sizePolicy.setHeightForWidth(self.label_arm_1.sizePolicy().hasHeightForWidth())
        self.label_arm_1.setSizePolicy(sizePolicy)
        self.label_arm_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_arm_1)

        self.btn_x_down = QPushButton(self.tab_1)
        self.btn_x_down.setObjectName(u"btn_x_down")
        sizePolicy.setHeightForWidth(self.btn_x_down.sizePolicy().hasHeightForWidth())
        self.btn_x_down.setSizePolicy(sizePolicy)
        self.btn_x_down.setFont(font)

        self.verticalLayout_4.addWidget(self.btn_x_down)

        self.verticalLayout_4.setStretch(2, 7)

        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_y_up = QPushButton(self.tab_1)
        self.btn_y_up.setObjectName(u"btn_y_up")
        sizePolicy.setHeightForWidth(self.btn_y_up.sizePolicy().hasHeightForWidth())
        self.btn_y_up.setSizePolicy(sizePolicy)
        self.btn_y_up.setFont(font)

        self.verticalLayout_6.addWidget(self.btn_y_up)

        self.label_arm_2_value = QLabel(self.tab_1)
        self.label_arm_2_value.setObjectName(u"label_arm_2_value")
        sizePolicy.setHeightForWidth(self.label_arm_2_value.sizePolicy().hasHeightForWidth())
        self.label_arm_2_value.setSizePolicy(sizePolicy)
        self.label_arm_2_value.setStyleSheet(u"background-color:white;")
        self.label_arm_2_value.setFrameShape(QFrame.Shape.NoFrame)
        self.label_arm_2_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_arm_2_value)

        self.slider_arm_2 = QSlider(self.tab_1)
        self.slider_arm_2.setObjectName(u"slider_arm_2")
        sizePolicy.setHeightForWidth(self.slider_arm_2.sizePolicy().hasHeightForWidth())
        self.slider_arm_2.setSizePolicy(sizePolicy)
        self.slider_arm_2.setStyleSheet(u"QSlider::handle:vertical {\n"
"    width: 15px; /* \uc6d0\ud558\ub294 \uac00\ub85c \ud06c\uae30 */\n"
"    height: 15px; /* \uc6d0\ud558\ub294 \uc138\ub85c \ud06c\uae30 */\n"
"    background-color: black; /* \ud578\ub4e4 \uc0c9\uc0c1 */\n"
"    border-radius: 7px; /* \ub465\uadfc \ubaa8\uc11c\ub9ac */\n"
"}")
        self.slider_arm_2.setMinimum(-90)
        self.slider_arm_2.setMaximum(90)
        self.slider_arm_2.setPageStep(10)
        self.slider_arm_2.setOrientation(Qt.Orientation.Vertical)
        self.slider_arm_2.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.verticalLayout_6.addWidget(self.slider_arm_2)

        self.label_arm_2 = QLabel(self.tab_1)
        self.label_arm_2.setObjectName(u"label_arm_2")
        sizePolicy.setHeightForWidth(self.label_arm_2.sizePolicy().hasHeightForWidth())
        self.label_arm_2.setSizePolicy(sizePolicy)
        self.label_arm_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_arm_2)

        self.btn_y_down = QPushButton(self.tab_1)
        self.btn_y_down.setObjectName(u"btn_y_down")
        sizePolicy.setHeightForWidth(self.btn_y_down.sizePolicy().hasHeightForWidth())
        self.btn_y_down.setSizePolicy(sizePolicy)
        self.btn_y_down.setFont(font)

        self.verticalLayout_6.addWidget(self.btn_y_down)

        self.verticalLayout_6.setStretch(2, 7)

        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_grab_2 = QPushButton(self.tab_1)
        self.btn_grab_2.setObjectName(u"btn_grab_2")
        sizePolicy.setHeightForWidth(self.btn_grab_2.sizePolicy().hasHeightForWidth())
        self.btn_grab_2.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.btn_grab_2)

        self.btn_reset = QPushButton(self.tab_1)
        self.btn_reset.setObjectName(u"btn_reset")
        sizePolicy.setHeightForWidth(self.btn_reset.sizePolicy().hasHeightForWidth())
        self.btn_reset.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.btn_reset)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_agv1 = QPushButton(self.tab_1)
        self.btn_agv1.setObjectName(u"btn_agv1")
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(False)
        self.btn_agv1.setFont(font1)
        icon = QIcon()
        icon.addFile(u"icons/robotic.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_agv1.setIcon(icon)
        self.btn_agv1.setIconSize(QSize(50, 50))
        self.btn_agv1.setCheckable(True)
        self.btn_agv1.setChecked(True)

        self.horizontalLayout_7.addWidget(self.btn_agv1)

        self.btn_agv2 = QPushButton(self.tab_1)
        self.btn_agv2.setObjectName(u"btn_agv2")
        font2 = QFont()
        font2.setBold(True)
        self.btn_agv2.setFont(font2)
        self.btn_agv2.setIcon(icon)
        self.btn_agv2.setIconSize(QSize(50, 50))
        self.btn_agv2.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.btn_agv2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.verticalLayout_8.setStretch(0, 4)

        self.gridLayout_6.addLayout(self.verticalLayout_8, 0, 1, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_13 = QLabel(self.tab_1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setPixmap(QPixmap(u"icons/Basic Theme.png"))

        self.verticalLayout_3.addWidget(self.label_13)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 5, -1)
        self.btn_auto = QPushButton(self.tab_1)
        self.btn_auto.setObjectName(u"btn_auto")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_auto.sizePolicy().hasHeightForWidth())
        self.btn_auto.setSizePolicy(sizePolicy1)
        self.btn_auto.setCheckable(True)
        self.btn_auto.setChecked(False)

        self.verticalLayout.addWidget(self.btn_auto)

        self.btn_manual = QPushButton(self.tab_1)
        self.btn_manual.setObjectName(u"btn_manual")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_manual.sizePolicy().hasHeightForWidth())
        self.btn_manual.setSizePolicy(sizePolicy2)
        self.btn_manual.setCheckable(True)
        self.btn_manual.setChecked(True)

        self.verticalLayout.addWidget(self.btn_manual)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.label_cam = QLabel(self.tab_1)
        self.label_cam.setObjectName(u"label_cam")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_cam.sizePolicy().hasHeightForWidth())
        self.label_cam.setSizePolicy(sizePolicy3)
        self.label_cam.setStyleSheet(u"background-color : gray;")

        self.horizontalLayout_4.addWidget(self.label_cam)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_grab = QPushButton(self.tab_1)
        self.btn_grab.setObjectName(u"btn_grab")
        sizePolicy2.setHeightForWidth(self.btn_grab.sizePolicy().hasHeightForWidth())
        self.btn_grab.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.btn_grab)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 7)
        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_9.addLayout(self.verticalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_right = QPushButton(self.tab_1)
        self.btn_right.setObjectName(u"btn_right")
        self.btn_right.setFont(font)

        self.gridLayout_4.addWidget(self.btn_right, 1, 2, 1, 1)

        self.btn_mid = QPushButton(self.tab_1)
        self.btn_mid.setObjectName(u"btn_mid")
        self.btn_mid.setFont(font)

        self.gridLayout_4.addWidget(self.btn_mid, 1, 1, 1, 1)

        self.btn_go = QPushButton(self.tab_1)
        self.btn_go.setObjectName(u"btn_go")
        self.btn_go.setFont(font)

        self.gridLayout_4.addWidget(self.btn_go, 0, 1, 1, 1)

        self.btn_back = QPushButton(self.tab_1)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setFont(font)

        self.gridLayout_4.addWidget(self.btn_back, 2, 1, 1, 1)

        self.btn_left = QPushButton(self.tab_1)
        self.btn_left.setObjectName(u"btn_left")
        self.btn_left.setFont(font)

        self.gridLayout_4.addWidget(self.btn_left, 1, 0, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout_4)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.slider_grab = QSlider(self.tab_1)
        self.slider_grab.setObjectName(u"slider_grab")
        sizePolicy.setHeightForWidth(self.slider_grab.sizePolicy().hasHeightForWidth())
        self.slider_grab.setSizePolicy(sizePolicy)
        self.slider_grab.setStyleSheet(u"QSlider::handle:horizontal {\n"
"    width: 15px; /* \uc6d0\ud558\ub294 \uac00\ub85c \ud06c\uae30 */\n"
"    height: 15px; /* \uc6d0\ud558\ub294 \uc138\ub85c \ud06c\uae30 */\n"
"    background-color: black; /* \ud578\ub4e4 \uc0c9\uc0c1 */\n"
"    border-radius: 7px; /* \ub465\uadfc \ubaa8\uc11c\ub9ac */\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    width: 15px; /* \uc6d0\ud558\ub294 \uac00\ub85c \ud06c\uae30 */\n"
"    height: 15px; /* \uc6d0\ud558\ub294 \uc138\ub85c \ud06c\uae30 */\n"
"    background-color: #3498db; /* \ud578\ub4e4 \uc0c9\uc0c1 */\n"
"    border-radius: 7px; /* \ub465\uadfc \ubaa8\uc11c\ub9ac */\n"
"}")
        self.slider_grab.setMinimum(-90)
        self.slider_grab.setMaximum(90)
        self.slider_grab.setSliderPosition(0)
        self.slider_grab.setOrientation(Qt.Orientation.Horizontal)
        self.slider_grab.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider_grab.setTickInterval(20)

        self.gridLayout_5.addWidget(self.slider_grab, 1, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_arm_left_2 = QLabel(self.tab_1)
        self.label_arm_left_2.setObjectName(u"label_arm_left_2")
        sizePolicy.setHeightForWidth(self.label_arm_left_2.sizePolicy().hasHeightForWidth())
        self.label_arm_left_2.setSizePolicy(sizePolicy)
        self.label_arm_left_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_arm_left_2)

        self.btn_turn_left = QPushButton(self.tab_1)
        self.btn_turn_left.setObjectName(u"btn_turn_left")
        sizePolicy.setHeightForWidth(self.btn_turn_left.sizePolicy().hasHeightForWidth())
        self.btn_turn_left.setSizePolicy(sizePolicy)

        self.verticalLayout_14.addWidget(self.btn_turn_left)


        self.horizontalLayout_17.addLayout(self.verticalLayout_14)

        self.slider_arm = QSlider(self.tab_1)
        self.slider_arm.setObjectName(u"slider_arm")
        sizePolicy.setHeightForWidth(self.slider_arm.sizePolicy().hasHeightForWidth())
        self.slider_arm.setSizePolicy(sizePolicy)
        self.slider_arm.setStyleSheet(u"QSlider::handle:horizontal {\n"
"    width: 15px; /* \uc6d0\ud558\ub294 \uac00\ub85c \ud06c\uae30 */\n"
"    height: 15px; /* \uc6d0\ud558\ub294 \uc138\ub85c \ud06c\uae30 */\n"
"    background-color: black; /* \ud578\ub4e4 \uc0c9\uc0c1 */\n"
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

        self.horizontalLayout_17.addWidget(self.slider_arm)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_arm_left_3 = QLabel(self.tab_1)
        self.label_arm_left_3.setObjectName(u"label_arm_left_3")
        sizePolicy.setHeightForWidth(self.label_arm_left_3.sizePolicy().hasHeightForWidth())
        self.label_arm_left_3.setSizePolicy(sizePolicy)
        self.label_arm_left_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_arm_left_3)

        self.btn_arm_right = QPushButton(self.tab_1)
        self.btn_arm_right.setObjectName(u"btn_arm_right")
        sizePolicy.setHeightForWidth(self.btn_arm_right.sizePolicy().hasHeightForWidth())
        self.btn_arm_right.setSizePolicy(sizePolicy)

        self.verticalLayout_15.addWidget(self.btn_arm_right)


        self.horizontalLayout_17.addLayout(self.verticalLayout_15)

        self.horizontalLayout_17.setStretch(1, 6)

        self.gridLayout_5.addLayout(self.horizontalLayout_17, 2, 0, 1, 1)

        self.label_grab = QLabel(self.tab_1)
        self.label_grab.setObjectName(u"label_grab")
        self.label_grab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_grab, 0, 0, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout_5)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 3)

        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.verticalLayout_9.setStretch(0, 1)

        self.gridLayout_6.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.gridLayout_6.setColumnStretch(0, 7)
        self.gridLayout_6.setColumnStretch(1, 1)
        icon1 = QIcon()
        icon1.addFile(u"icons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab_1, icon1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_refresh = QPushButton(self.tab_2)
        self.btn_refresh.setObjectName(u"btn_refresh")
        sizePolicy.setHeightForWidth(self.btn_refresh.sizePolicy().hasHeightForWidth())
        self.btn_refresh.setSizePolicy(sizePolicy)
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.btn_refresh.setIcon(icon2)

        self.gridLayout_2.addWidget(self.btn_refresh, 0, 2, 1, 1)

        self.btn_next = QPushButton(self.tab_2)
        self.btn_next.setObjectName(u"btn_next")
        sizePolicy.setHeightForWidth(self.btn_next.sizePolicy().hasHeightForWidth())
        self.btn_next.setSizePolicy(sizePolicy)
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoNext))
        self.btn_next.setIcon(icon3)

        self.gridLayout_2.addWidget(self.btn_next, 0, 1, 1, 1)

        self.btn_prev = QPushButton(self.tab_2)
        self.btn_prev.setObjectName(u"btn_prev")
        sizePolicy.setHeightForWidth(self.btn_prev.sizePolicy().hasHeightForWidth())
        self.btn_prev.setSizePolicy(sizePolicy)
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoPrevious))
        self.btn_prev.setIcon(icon4)

        self.gridLayout_2.addWidget(self.btn_prev, 0, 0, 1, 1)

        self.lineEdit_url = QLineEdit(self.tab_2)
        self.lineEdit_url.setObjectName(u"lineEdit_url")
        sizePolicy.setHeightForWidth(self.lineEdit_url.sizePolicy().hasHeightForWidth())
        self.lineEdit_url.setSizePolicy(sizePolicy)
        self.lineEdit_url.setFont(font2)

        self.gridLayout_2.addWidget(self.lineEdit_url, 0, 3, 1, 1)

        self.btn_url_enter = QPushButton(self.tab_2)
        self.btn_url_enter.setObjectName(u"btn_url_enter")
        sizePolicy.setHeightForWidth(self.btn_url_enter.sizePolicy().hasHeightForWidth())
        self.btn_url_enter.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.btn_url_enter, 0, 4, 1, 1)

        self.widget_web = QWidget(self.tab_2)
        self.widget_web.setObjectName(u"widget_web")
        sizePolicy.setHeightForWidth(self.widget_web.sizePolicy().hasHeightForWidth())
        self.widget_web.setSizePolicy(sizePolicy)
        self.widget_web.setAutoFillBackground(False)
        self.widget_web.setStyleSheet(u"background-color:white;")

        self.gridLayout_2.addWidget(self.widget_web, 1, 0, 1, 5)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 20)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setColumnStretch(3, 10)
        self.gridLayout_2.setColumnStretch(4, 1)
        icon5 = QIcon()
        icon5.addFile(u"icons/database.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab_2, icon5, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(25)
        font3.setBold(True)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
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
        self.table_log.setColumnCount(4)
        self.table_log.horizontalHeader().setVisible(True)
        self.table_log.horizontalHeader().setMinimumSectionSize(34)
        self.table_log.horizontalHeader().setHighlightSections(True)

        self.horizontalLayout_2.addWidget(self.table_log)

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
        self.table_sensing.setColumnCount(5)
        self.table_sensing.horizontalHeader().setVisible(True)
        self.table_sensing.horizontalHeader().setHighlightSections(True)

        self.horizontalLayout_2.addWidget(self.table_sensing)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        icon6 = QIcon()
        icon6.addFile(u"icons/log.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab_3, icon6, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_7 = QGridLayout(self.tab_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_14 = QLabel(self.tab_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setPixmap(QPixmap(u"icons/Basic Theme.png"))

        self.gridLayout_7.addWidget(self.label_14, 0, 0, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_8 = QLabel(self.tab_4)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_8)

        self.spinbox_forward = QDoubleSpinBox(self.tab_4)
        self.spinbox_forward.setObjectName(u"spinbox_forward")
        sizePolicy.setHeightForWidth(self.spinbox_forward.sizePolicy().hasHeightForWidth())
        self.spinbox_forward.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setPointSize(28)
        font4.setBold(True)
        self.spinbox_forward.setFont(font4)
        self.spinbox_forward.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinbox_forward.setValue(2.000000000000000)

        self.horizontalLayout_12.addWidget(self.spinbox_forward)


        self.verticalLayout_13.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_9 = QLabel(self.tab_4)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_9)

        self.spinbox_backward = QDoubleSpinBox(self.tab_4)
        self.spinbox_backward.setObjectName(u"spinbox_backward")
        sizePolicy.setHeightForWidth(self.spinbox_backward.sizePolicy().hasHeightForWidth())
        self.spinbox_backward.setSizePolicy(sizePolicy)
        self.spinbox_backward.setFont(font4)
        self.spinbox_backward.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinbox_backward.setValue(2.000000000000000)

        self.horizontalLayout_13.addWidget(self.spinbox_backward)


        self.verticalLayout_13.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_10 = QLabel(self.tab_4)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_10)

        self.spinbox_turn = QDoubleSpinBox(self.tab_4)
        self.spinbox_turn.setObjectName(u"spinbox_turn")
        sizePolicy.setHeightForWidth(self.spinbox_turn.sizePolicy().hasHeightForWidth())
        self.spinbox_turn.setSizePolicy(sizePolicy)
        self.spinbox_turn.setFont(font4)
        self.spinbox_turn.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinbox_turn.setValue(5.000000000000000)

        self.horizontalLayout_14.addWidget(self.spinbox_turn)


        self.verticalLayout_13.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_11 = QLabel(self.tab_4)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_11)

        self.spinbox_rotate = QDoubleSpinBox(self.tab_4)
        self.spinbox_rotate.setObjectName(u"spinbox_rotate")
        sizePolicy.setHeightForWidth(self.spinbox_rotate.sizePolicy().hasHeightForWidth())
        self.spinbox_rotate.setSizePolicy(sizePolicy)
        self.spinbox_rotate.setFont(font4)
        self.spinbox_rotate.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinbox_rotate.setValue(5.000000000000000)

        self.horizontalLayout_15.addWidget(self.spinbox_rotate)


        self.verticalLayout_13.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.btn_set_reset = QPushButton(self.tab_4)
        self.btn_set_reset.setObjectName(u"btn_set_reset")
        sizePolicy.setHeightForWidth(self.btn_set_reset.sizePolicy().hasHeightForWidth())
        self.btn_set_reset.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.btn_set_reset)

        self.label_12 = QLabel(self.tab_4)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_16.addWidget(self.label_12)

        self.btn_set_save = QPushButton(self.tab_4)
        self.btn_set_save.setObjectName(u"btn_set_save")
        sizePolicy.setHeightForWidth(self.btn_set_save.sizePolicy().hasHeightForWidth())
        self.btn_set_save.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.btn_set_save)


        self.verticalLayout_13.addLayout(self.horizontalLayout_16)


        self.gridLayout_7.addLayout(self.verticalLayout_13, 2, 0, 1, 2)

        self.label_setting_agv = QLabel(self.tab_4)
        self.label_setting_agv.setObjectName(u"label_setting_agv")
        font5 = QFont()
        font5.setPointSize(36)
        font5.setBold(True)
        self.label_setting_agv.setFont(font5)
        self.label_setting_agv.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.label_setting_agv, 1, 0, 1, 1)

        icon7 = QIcon()
        icon7.addFile(u"icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab_4, icon7, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1246, 22))
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
        self.btn_x_down.clicked.connect(MainWindow.slide_x_minus)
        self.btn_x_up.clicked.connect(MainWindow.slide_x_plus)
        self.btn_y_up.clicked.connect(MainWindow.slide_y_plus)
        self.btn_y_down.clicked.connect(MainWindow.slide_y_minus)
        self.btn_reset.clicked.connect(MainWindow.set_reset)
        self.btn_auto.toggled.connect(MainWindow.mode_auto)
        self.btn_manual.toggled.connect(MainWindow.mode_manual)
        self.btn_grab_2.clicked.connect(MainWindow.arm_set)
        self.btn_prev.clicked.connect(MainWindow.web_prev)
        self.btn_refresh.clicked.connect(MainWindow.web_refresh)
        self.btn_url_enter.clicked.connect(MainWindow.web_go)
        self.btn_next.clicked.connect(MainWindow.web_next)
        self.btn_agv1.toggled.connect(MainWindow.select_agv1)
        self.btn_agv2.toggled.connect(MainWindow.select_agv2)
        self.btn_grab.clicked.connect(MainWindow.target_grab)
        self.btn_cam_down.clicked.connect(MainWindow.slide_cam_minus)
        self.btn_cam_up.clicked.connect(MainWindow.slide_cam_plus)
        self.btn_turn_left.clicked.connect(MainWindow.slide_turn_minus)
        self.btn_arm_right.clicked.connect(MainWindow.slide_turn_plus)
        self.btn_set_reset.clicked.connect(MainWindow.setting_reset)
        self.btn_set_save.clicked.connect(MainWindow.setting_save)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_cam_up.setText(QCoreApplication.translate("MainWindow", u"\u25b2", None))
        self.label_cam_angle.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_angle.setText(QCoreApplication.translate("MainWindow", u"CAM Angle", None))
        self.btn_cam_down.setText(QCoreApplication.translate("MainWindow", u"\u25bc", None))
        self.btn_x_up.setText(QCoreApplication.translate("MainWindow", u"\u25b2", None))
        self.label_arm_1_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_arm_1.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.btn_x_down.setText(QCoreApplication.translate("MainWindow", u"\u25bc", None))
        self.btn_y_up.setText(QCoreApplication.translate("MainWindow", u"\u25b2", None))
        self.label_arm_2_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_arm_2.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.btn_y_down.setText(QCoreApplication.translate("MainWindow", u"\u25bc", None))
        self.btn_grab_2.setText(QCoreApplication.translate("MainWindow", u"SET ARM", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"SERVO RESET", None))
        self.btn_agv1.setText(QCoreApplication.translate("MainWindow", u"AGV 1", None))
        self.btn_agv2.setText(QCoreApplication.translate("MainWindow", u"AGV 2", None))
        self.label_13.setText("")
        self.btn_auto.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.btn_manual.setText(QCoreApplication.translate("MainWindow", u"MANUAL", None))
        self.label_cam.setText("")
        self.btn_grab.setText(QCoreApplication.translate("MainWindow", u"GRAB", None))
        self.btn_right.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.btn_mid.setText(QCoreApplication.translate("MainWindow", u"Mid", None))
        self.btn_go.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.btn_left.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.label_arm_left_2.setText(QCoreApplication.translate("MainWindow", u"LEFT", None))
        self.btn_turn_left.setText(QCoreApplication.translate("MainWindow", u"\u25c0", None))
        self.label_arm_left_3.setText(QCoreApplication.translate("MainWindow", u"RIGHT", None))
        self.btn_arm_right.setText(QCoreApplication.translate("MainWindow", u"\u25b6", None))
        self.label_grab.setText(QCoreApplication.translate("MainWindow", u"GRAB", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), "")
        self.btn_refresh.setText("")
        self.btn_next.setText("")
        self.btn_prev.setText("")
        self.btn_url_enter.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "")
        self.label.setText(QCoreApplication.translate("MainWindow", u"COMMAND LOG", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SENSING LOG", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), "")
        self.label_14.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"FORWARD SPEED", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"BACKWARD SPEED", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"TURN SPEED", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"ARM ROTATE SPEED", None))
        self.btn_set_reset.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.label_12.setText("")
        self.btn_set_save.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.label_setting_agv.setText(QCoreApplication.translate("MainWindow", u"AGV1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), "")
    # retranslateUi

