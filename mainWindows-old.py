# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Ui_MainWindow(QObject):
    _clickedSignal = pyqtSignal()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1128, 729)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Video = QtWidgets.QLabel(self.centralwidget)
        self.label_Video.setGeometry(QtCore.QRect(470, 60, 591, 421))
        self.label_Video.setAutoFillBackground(False)
        self.label_Video.setStyleSheet("\n" "boder:1px\n" "")
        self.label_Video.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_Video.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Video.setObjectName("label_Video")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 530, 1071, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcdNumber_xinlv = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber_xinlv.setSmallDecimalPoint(True)
        self.lcdNumber_xinlv.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_xinlv.setProperty("value", 81.0)
        self.lcdNumber_xinlv.setProperty("intValue", 81)
        self.lcdNumber_xinlv.setObjectName("lcdNumber_xinlv")
        self.verticalLayout.addWidget(self.lcdNumber_xinlv)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lcdNumber_tiwen = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber_tiwen.setSmallDecimalPoint(True)
        self.lcdNumber_tiwen.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_tiwen.setProperty("value", 81.0)
        self.lcdNumber_tiwen.setProperty("intValue", 81)
        self.lcdNumber_tiwen.setObjectName("lcdNumber_tiwen")
        self.verticalLayout_2.addWidget(self.lcdNumber_tiwen)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lcdNumber_shengao = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber_shengao.setSmallDecimalPoint(True)
        self.lcdNumber_shengao.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_shengao.setProperty("value", 81.0)
        self.lcdNumber_shengao.setProperty("intValue", 81)
        self.lcdNumber_shengao.setObjectName("lcdNumber_shengao")
        self.verticalLayout_3.addWidget(self.lcdNumber_shengao)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lcdNumber_tizhong = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber_tizhong.setSmallDecimalPoint(True)
        self.lcdNumber_tizhong.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_tizhong.setProperty("value", 81.0)
        self.lcdNumber_tizhong.setProperty("intValue", 81)
        self.lcdNumber_tizhong.setObjectName("lcdNumber_tizhong")
        self.verticalLayout_4.addWidget(self.lcdNumber_tizhong)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lcdNumber_timer = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber_timer.setSmallDecimalPoint(True)
        self.lcdNumber_timer.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_timer.setProperty("value", 81.0)
        self.lcdNumber_timer.setProperty("intValue", 81)
        self.lcdNumber_timer.setObjectName("lcdNumber_timer")
        self.verticalLayout_5.addWidget(self.lcdNumber_timer)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 60, 381, 361))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.lineEdit_Name = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_Name.setFont(font)
        self.lineEdit_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.horizontalLayout_2.addWidget(self.lineEdit_Name)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.lineEdit_ID = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_ID.setFont(font)
        self.lineEdit_ID.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.horizontalLayout_3.addWidget(self.lineEdit_ID)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.lineEdit_Sex = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_Sex.setFont(font)
        self.lineEdit_Sex.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Sex.setObjectName("lineEdit_Sex")
        self.horizontalLayout_4.addWidget(self.lineEdit_Sex)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.textEdit_Other = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit_Other.setObjectName("textEdit_Other")
        self.horizontalLayout_5.addWidget(self.textEdit_Other)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.pushButton_getinfo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_getinfo.setParent(self.centralwidget)
        self.pushButton_getinfo.setGeometry(QtCore.QRect(30, 430, 381, 51))
        self.pushButton_getinfo.setObjectName("pushButton_getinfo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1128, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.label_tips = QtWidgets.QLabel(MainWindow)

        self.label_tips.setGeometry(QtCore.QRect(0, 0, 591, 421))
        self.label_tips.setAutoFillBackground(True)

        self.label_tips.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_tips.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tips.setObjectName("label_tips")
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_tips.setFont(font)
        self.label_tips.setText(">>即将采集舌苔，倒计时5秒<<")
        self.label_tips.setVisible(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Video.setText(_translate("MainWindow", "video"))
        self.label.setText(_translate("MainWindow", "心率"))
        self.label_2.setText(_translate("MainWindow", "体温"))
        self.label_3.setText(_translate("MainWindow", "身高"))
        self.label_4.setText(_translate("MainWindow", "体重"))
        self.label_5.setText(_translate("MainWindow", "倒计时"))
        self.label_11.setText(_translate("MainWindow", "个人信息"))
        self.label_7.setText(_translate("MainWindow", "姓名："))
        self.label_8.setText(_translate("MainWindow", "编号："))
        self.label_9.setText(_translate("MainWindow", "性别："))
        self.label_10.setText(_translate("MainWindow", "备注："))
        self.pushButton_getinfo.setText(_translate("MainWindow", "人脸识别"))
        self.pushButton_getinfo.clicked.connect(self.onClick)

    def onClick(self):
        self._clickedSignal.emit()
