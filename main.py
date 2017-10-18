#!/usr/bin/python3.4

import sys
from Utils import Utilities, Init
from PySide.QtGui import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide.phonon import Phonon
import threading
from qgmap import *
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    __is_active_ = False
    __dict_canbus_ = dict()
    __dict_gps_ = dict()
    __gmap_ = None
    __markers_ = set()
    __playing_ = False

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionOpen_archive.triggered.connect(self.select_file)
        self.btnStop.clicked.connect(self.stop_slider)
        self.txtCANBUS.setText("Click File -> Open Archive and the select a valid"
                               "archive in order to start the analysis")
        self.sldTime.valueChanged.connect(self.load_contents)
        self.btnSxArrow.clicked.connect(self.decrease_time)
        self.btnDxArrow.clicked.connect(self.increase_time)
        self.btnPlay.clicked.connect(self.play_slider)
        self.btnPause.clicked.connect(self.pause_slider)
        self.__gmap_ = QGoogleMap(self.wdgGoogleMaps)

    # Popup a box with about message.
    def show_about(self):
        QMessageBox.about(self, "About CANBUS Analyzer", Utilities.get_about())

    def select_file(self):
        #archiveName = str(expanduser("~") + "/Test/Test completi/nuove_guide_031017/prima guida/test.gz")
                        #QFileDialog.getOpenFileName(self,
                         #                         "Open gzip Archive",
                          #                        str(expanduser("~"),
                           #                       "Archive File (*.gz)"
                            #                      )[0]
        #if archiveName == '':
        #    return

        #if not Utilities.extract_files(archiveName):
        #    QMessageBox.critical(self, "Error", "Impossible to extract the archive!")
        #    return

        #QMessageBox.information(self, "Information", "Archive extracted!")
        self.__is_active_ = True
        self.txtCANBUS.setText("")
        Init.init_slider(self.sldTime)
        Init.init_time_labels(self)
        Init.init_dict_canbus(self.__dict_canbus_)
        Init.init_dict_gps(self.__dict_gps_)
        Init.init_google_maps(self.__gmap_, self.__dict_gps_)
        Init.init_time_buttons(self)

        #player = Phonon.VideoPlayer(Phonon.VideoCategory, self.wdgVideo)
        #player.play(Utilities.OUTPUT_FOLDER + 'video.mp4')

    # Load new contents when time changes
    def load_contents(self):
        time = int(self.sldTime.value())

        # Clear displays
        self.txtCANBUS.setText('')
        self.txtGpsData.setText('')
        self.lblTime.setText(str(time)+'s')

        # Nothing to load
        if time == 0:
            return

        # Select and show canbus data at certain time
        canbus_values = self.__dict_canbus_[time]
        text = '<table>'
        for v in canbus_values:
            text += '<tr><td><b>ID</b>:' + v[0] + ' <td><b>PAYLOAD</b>: ' + v[1] + '<br>'
        self.txtCANBUS.setText(text)

        # Select GPS data at certain time if present
        if time > max(self.__dict_gps_):
            gps_value = self.__dict_gps_[max(self.__dict_gps_)]
        elif time < min(self.__dict_gps_):
            gps_value = None
        else:
            gps_value = self.__dict_gps_[time]

        # Show GPS data
        if gps_value is not None:
            text = '<table><tr><td><b>Longitude</b>: ' + gps_value['lon'] + '° '+\
            '<td><b>Latitude</b>: ' + gps_value['lat'] + '°<br>'+\
            '<tr><td><b>Altitude</b>: ' + gps_value['alt'] + 'm ' +\
            '<td><b>Speed</b>: ' + gps_value['spd'] + 'm/s<br>'
            self.__gmap_.addMarker(time, gps_value['lat'], gps_value['lon'])
            self.__markers_.add(time)
        else:
            text = 'Data are not available'
        self.txtGpsData.setText(text)

        # Remove following markers on Google Maps
        if self.__markers_ and time < max(self.__markers_):
            for i in range(time+1, max(self.__markers_)+1):
                if i in self.__markers_:
                    self.__gmap_.deleteMarker(i)
                    self.__markers_.remove(i)

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
        for m in self.__markers_:
            self.__gmap_.deleteMarker(m)
        self.load_contents()

    def decrease_time(self):
        if self.sldTime.value() in self.__markers_:
            self.__gmap_.deleteMarker(self.sldTime.value())
            self.__markers_.remove(self.sldTime.value())
        self.sldTime.setValue(self.sldTime.value() - 1)

    def increase_time(self):
        self.sldTime.setValue(self.sldTime.value() + 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()

    sys.exit(app.exec_())