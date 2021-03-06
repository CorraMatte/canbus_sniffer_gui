# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Dec  3 15:48:42 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 593)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 470, 931, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lblTime = QtGui.QLabel(self.centralwidget)
        self.lblTime.setEnabled(False)
        self.lblTime.setGeometry(QtCore.QRect(50, 510, 71, 21))
        self.lblTime.setObjectName("lblTime")
        self.txtCANBUS = QtGui.QTextEdit(self.centralwidget)
        self.txtCANBUS.setGeometry(QtCore.QRect(500, 0, 451, 181))
        self.txtCANBUS.setReadOnly(True)
        self.txtCANBUS.setObjectName("txtCANBUS")
        self.lblMaxTime = QtGui.QLabel(self.centralwidget)
        self.lblMaxTime.setEnabled(False)
        self.lblMaxTime.setGeometry(QtCore.QRect(830, 510, 61, 16))
        self.lblMaxTime.setObjectName("lblMaxTime")
        self.btnPlay = QtGui.QPushButton(self.centralwidget)
        self.btnPlay.setEnabled(False)
        self.btnPlay.setGeometry(QtCore.QRect(140, 519, 31, 31))
        self.btnPlay.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlay.setIcon(icon)
        self.btnPlay.setObjectName("btnPlay")
        self.btnStop = QtGui.QPushButton(self.centralwidget)
        self.btnStop.setEnabled(False)
        self.btnStop.setGeometry(QtCore.QRect(240, 519, 31, 31))
        self.btnStop.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStop.setIcon(icon1)
        self.btnStop.setObjectName("btnStop")
        self.btnPause = QtGui.QPushButton(self.centralwidget)
        self.btnPause.setEnabled(False)
        self.btnPause.setGeometry(QtCore.QRect(190, 520, 31, 31))
        self.btnPause.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPause.setIcon(icon2)
        self.btnPause.setObjectName("btnPause")
        self.btnSxArrow = QtGui.QPushButton(self.centralwidget)
        self.btnSxArrow.setEnabled(False)
        self.btnSxArrow.setGeometry(QtCore.QRect(10, 490, 31, 31))
        self.btnSxArrow.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/sx_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSxArrow.setIcon(icon3)
        self.btnSxArrow.setObjectName("btnSxArrow")
        self.btnDxArrow = QtGui.QPushButton(self.centralwidget)
        self.btnDxArrow.setEnabled(False)
        self.btnDxArrow.setGeometry(QtCore.QRect(900, 490, 31, 31))
        self.btnDxArrow.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/dx_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDxArrow.setIcon(icon4)
        self.btnDxArrow.setObjectName("btnDxArrow")
        self.sldTime = QtGui.QSlider(self.centralwidget)
        self.sldTime.setGeometry(QtCore.QRect(50, 490, 841, 31))
        self.sldTime.setOrientation(QtCore.Qt.Horizontal)
        self.sldTime.setObjectName("sldTime")
        self.wdgVideo = QtGui.QWidget(self.centralwidget)
        self.wdgVideo.setGeometry(QtCore.QRect(0, 0, 491, 391))
        self.wdgVideo.setObjectName("wdgVideo")
        self.txtGpsData = QtGui.QTextEdit(self.centralwidget)
        self.txtGpsData.setGeometry(QtCore.QRect(0, 400, 491, 71))
        self.txtGpsData.setReadOnly(True)
        self.txtGpsData.setObjectName("txtGpsData")
        self.wdgGoogleMaps = QtGui.QWidget(self.centralwidget)
        self.wdgGoogleMaps.setGeometry(QtCore.QRect(500, 190, 451, 281))
        self.wdgGoogleMaps.setObjectName("wdgGoogleMaps")
        self.pgrLoadData = QtGui.QProgressBar(self.centralwidget)
        self.pgrLoadData.setGeometry(QtCore.QRect(350, 520, 471, 23))
        self.pgrLoadData.setMaximum(100)
        self.pgrLoadData.setProperty("value", -1)
        self.pgrLoadData.setObjectName("pgrLoadData")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 19))
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
        self.lblTime.setText(QtGui.QApplication.translate("MainWindow", "00:00:00", None, QtGui.QApplication.UnicodeUTF8))
        self.txtCANBUS.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans Mono\'; color:#000000;\">Click </span><span style=\" font-family:\'DejaVu Sans Mono\'; font-weight:600; color:#000000;\">&quot;File&quot;-&gt;&quot;Open Archive&quot;</span><span style=\" font-family:\'DejaVu Sans Mono\'; color:#000000;\"> and select a valid archive in order to start the analysis</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'DejaVu Sans Mono\'; color:#000000; background-color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'DejaVu Sans Mono\'; color:#000000; background-color:#ffffff;\">The </span><span style=\" font-family:\'DejaVu Sans Mono\'; font-weight:600; color:#000000; background-color:#ffffff;\">CANBUS</span><span style=\" font-family:\'DejaVu Sans Mono\'; color:#000000; background-color:#ffffff;\"> messages will shown here</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMaxTime.setText(QtGui.QApplication.translate("MainWindow", "00:00:00", None, QtGui.QApplication.UnicodeUTF8))
        self.txtGpsData.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The <span style=\" font-weight:600;\">GPS</span> data will shown here</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.infoMenu.setTitle(QtGui.QApplication.translate("MainWindow", "?", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_archive.setText(QtGui.QApplication.translate("MainWindow", "Open archive", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))

