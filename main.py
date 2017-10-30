#!/usr/bin/python3.4
#
# Author: Matteo Corradini
#
# This application realizes a GUI with PySide in order to display the data
# acquired with the logger. It is possible to play and stop the video, or
# select the image frame by frame. The canbus data and the GPS data show the
# last value captured in that moment.

# IMPORT #######################################################################

import sys
from Utils import Utilities, Init
from PySide.QtGui import QApplication, QMainWindow, QMessageBox, QFileDialog
import threading
from qgmap import *
from ui_main import Ui_MainWindow
import os


# CLASSES ######################################################################

class MainWindow(QMainWindow, Ui_MainWindow):
    __playing_ = False
    dict_canbus = dict()
    dict_gps = dict()
    gmap = None
    markers = set()
    media_obj = None
    video_widget = None

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionOpen_archive.triggered.connect(self.select_file)
        self.btnStop.clicked.connect(self.stop_slider)
        self.sldTime.valueChanged.connect(self.load_contents)
        self.btnSxArrow.clicked.connect(self.decrease_time)
        self.btnDxArrow.clicked.connect(self.increase_time)
        self.btnPlay.clicked.connect(self.play_slider)
        self.btnPause.clicked.connect(self.pause_slider)
        self.gmap = QGoogleMap(self.wdgGoogleMaps)
        self.lblTime.setVisible(False)
        self.lblMaxTime.setVisible(False)
        self.pgrLoadData.setVisible(False)

    # Popup a box with about message.
    def show_about(self):
        QMessageBox.about(self, "About CANBUS Analyzer", Utilities.get_about())

    def select_file(self):
        self.__init_var_()
        archive_name = QFileDialog.getOpenFileName(self,
                                                   "Open gzip Archive",
                                                   str(os.path.expanduser("~")),
                                                   "Archive File (*.gz)"
                                                   )[0]

        if archive_name == '':
            return

        self.pgrLoadData.setVisible(True)
        if not Utilities.extract_files(archive_name):
            QMessageBox.critical(self, "Error",
                                 "Impossible to extract the archive!")
            self.pgrLoadData.setVisible(False)
            return

        QMessageBox.information(self, "Information",
                                "Archive extracted!\n"
                                "Wait that the archive is load")

        # Init data structures
        Init.init_dict_canbus(self.dict_canbus, self.pgrLoadData)
        Init.init_dict_gps(self.dict_gps, self.pgrLoadData)
        Init.init_google_maps(self.gmap)
        Init.init_video(self)

        # Init interface objects
        self.gmap.centerAt(float(self.dict_gps[min(self.dict_gps)]['lat']),
                           float(self.dict_gps[min(self.dict_gps)]['lon']))
        self.sldTime.setMaximum(max(self.dict_canbus))
        self.lblMaxTime.setText(
            Utilities.get_time_from_seconds(str(self.sldTime.maximum()))
        )
        self.txtCANBUS.setText('')
        self.txtGpsData.setText('')
        Init.init_time_labels(self)
        Init.init_slider(self.sldTime)
        Init.init_time_buttons(self)

        self.pgrLoadData.setVisible(False)

    # Load new contents when time changes
    def load_contents(self):
        time = int(self.sldTime.value())

        # Clear displays
        self.txtCANBUS.setText('')
        self.txtGpsData.setText('')
        self.lblTime.setText(Utilities.get_time_from_seconds(time))

        # Nothing to load
        if time == 0:
            return

        # Select and show canbus data at certain time
        canbus_values = self.dict_canbus[time]
        text = '<table>'
        for v in canbus_values:
            text += '<tr><td><b>ID</b>:' + v[0] + ' <td><b>PAYLOAD</b>: ' + v[
                1] + '<br>'
        self.txtCANBUS.setText(text)

        # Select GPS data at certain time if present
        if time > max(self.dict_gps):
            gps_value = self.dict_gps[max(self.dict_gps)]
        elif time < min(self.dict_gps):
            gps_value = None
        else:
            gps_value = self.dict_gps[time]

        # Show GPS data
        if gps_value is not None:
            text = '<table><tr><td><b>Longitude</b>: ' + gps_value[
                'lon'] + '° ' + \
                   '<td><b>Latitude</b>: ' + gps_value['lat'] + '°<br>' + \
                   '<tr><td><b>Altitude</b>: ' + gps_value['alt'] + 'm ' + \
                   '<td><b>Speed</b>: ' + gps_value['spd'] + 'm/s<br>'
            self.gmap.addMarker(time, gps_value['lat'], gps_value['lon'])
            self.markers.add(time)
        else:
            text = 'Data are not available'
        self.txtGpsData.setText(text)

        # Remove following markers on Google Maps
        if self.markers and time < max(self.markers):
            for i in range(time + 1, max(self.markers) + 1):
                if i in self.markers:
                    self.gmap.deleteMarker(i)
                    self.markers.remove(i)

        # Time multiplies 1000 to get the seconds
        self.media_obj.seek(time * 1000)

    def play_slider(self):
        self.btnPlay.setEnabled(False)
        self.btnPause.setEnabled(True)
        self.__playing_ = True
        self.thr_increase_slider()

    # Thread containing the timer
    def thr_increase_slider(self):
        if self.__playing_:
            threading.Timer(1.0, self.thr_increase_slider).start()
            self.increase_time()

    def pause_slider(self):
        self.__playing_ = False
        self.btnPlay.setEnabled(True)
        self.btnPause.setEnabled(False)

    def stop_slider(self):
        self.__playing_ = False
        self.sldTime.setValue(0)
        for m in self.markers:
            self.gmap.deleteMarker(m)
        self.load_contents()
        self.media_obj.seek(0)

    def decrease_time(self):
        if self.sldTime.value() in self.markers:
            self.gmap.deleteMarker(self.sldTime.value())
            self.markers.remove(self.sldTime.value())
        self.sldTime.setValue(self.sldTime.value() - 1)

    def increase_time(self):
        self.sldTime.setValue(self.sldTime.value() + 1)

    def __init_var_(self):
        self.dict_canbus = dict()
        self.dict_gps = dict()
        self.markers = set()
        self.__playing_ = False
        self.media_obj = None
        self.video_widget = None


# MAIN #########################################################################

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()

    sys.exit(app.exec_())
