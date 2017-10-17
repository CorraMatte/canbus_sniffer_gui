# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Tue Oct 17 19:57:53 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(826, 540)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblCANBUS = QtGui.QLabel(self.centralwidget)
        self.lblCANBUS.setGeometry(QtCore.QRect(120, 0, 51, 16))
        self.lblCANBUS.setObjectName("lblCANBUS")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 420, 821, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.sldTime = QtGui.QSlider(self.centralwidget)
        self.sldTime.setGeometry(QtCore.QRect(20, 450, 771, 20))
        self.sldTime.setOrientation(QtCore.Qt.Horizontal)
        self.sldTime.setObjectName("sldTime")
        self.lblTime = QtGui.QLabel(self.centralwidget)
        self.lblTime.setGeometry(QtCore.QRect(150, 470, 59, 21))
        self.lblTime.setObjectName("lblTime")
        self.txtCANBUS = QtGui.QTextEdit(self.centralwidget)
        self.txtCANBUS.setGeometry(QtCore.QRect(0, 20, 311, 211))
        self.txtCANBUS.setReadOnly(True)
        self.txtCANBUS.setObjectName("txtCANBUS")
        self.lblMinTime = QtGui.QLabel(self.centralwidget)
        self.lblMinTime.setEnabled(False)
        self.lblMinTime.setGeometry(QtCore.QRect(20, 470, 16, 16))
        self.lblMinTime.setObjectName("lblMinTime")
        self.lblMaxTime = QtGui.QLabel(self.centralwidget)
        self.lblMaxTime.setEnabled(False)
        self.lblMaxTime.setGeometry(QtCore.QRect(770, 470, 51, 16))
        self.lblMaxTime.setObjectName("lblMaxTime")
        self.btnPlay = QtGui.QPushButton(self.centralwidget)
        self.btnPlay.setGeometry(QtCore.QRect(50, 470, 21, 22))
        self.btnPlay.setObjectName("btnPlay")
        self.btnStop = QtGui.QPushButton(self.centralwidget)
        self.btnStop.setGeometry(QtCore.QRect(110, 470, 21, 22))
        self.btnStop.setObjectName("btnStop")
        self.brnPause = QtGui.QPushButton(self.centralwidget)
        self.brnPause.setGeometry(QtCore.QRect(80, 470, 21, 22))
        self.brnPause.setObjectName("brnPause")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 826, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.infoMenu = QtGui.QMenu(self.menubar)
        self.infoMenu.setObjectName("infoMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_archive = QtGui.QAction(MainWindow)
        self.actionOpen_archive.setObjectName("actionOpen_archive")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionOpen_archive)
        self.infoMenu.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.infoMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "CANBUS Analyzer", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCANBUS.setText(QtGui.QApplication.translate("MainWindow", "CANBUS", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTime.setText(QtGui.QApplication.translate("MainWindow", "00:0000", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMinTime.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMaxTime.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPlay.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStop.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.brnPause.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.infoMenu.setTitle(QtGui.QApplication.translate("MainWindow", "?", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_archive.setText(QtGui.QApplication.translate("MainWindow", "Open archive", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))

