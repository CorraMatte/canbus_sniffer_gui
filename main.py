#!/usr/bin/python3.4

import sys
from Utils import Utilities, Init
from PySide.QtGui import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide.phonon import Phonon

from qgmap import *

from ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    __is_active_ = False
    __dict_canbus_ = dict()
    __dict_gps_ = dict()
    __gmap_ = None
    __markers_ = set()

    def __init__(self, parent=None):
        '''Mandatory initialisation of a class.'''
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionOpen_archive.triggered.connect(self.select_file)
        self.btnStop.clicked.connect(self.stop_slider)
        self.txtCANBUS.setText("Click File -> Open Archive and the select a valid"
                               "archive in order to start the analysis")
        self.sldTime.valueChanged.connect(self.set_values_at_time)
        self.btnSxArrow.clicked.connect(self.decrease_time)
        self.btnDxArrow.clicked.connect(self.increase_time)
        self.__gmap_ = QGoogleMap(self.wdgGoogleMaps)

    def show_about(self):
        #Popup a box with about message.
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

    def set_values_at_time(self):
        time = int(self.sldTime.value())
        self.txtCANBUS.setText('')
        self.txtGpsData.setText('')
        self.lblTime.setText(str(time)+'s')
        #clear everything
        if time == 0:
            return
        
        canbus_values = self.__dict_canbus_[time]
        text = '<table>'
        for v in canbus_values:
            text += '<tr><td><b>ID</b>:' + v[0] + ' <td><b>PAYLOAD</b>: ' + v[1] + '<br>'
        self.txtCANBUS.setText(text)

        if time > max(self.__dict_gps_):
            gps_value = self.__dict_gps_[max(self.__dict_gps_)]
        elif time < min(self.__dict_gps_):
            gps_value = None
        else:
            gps_value = self.__dict_gps_[time]
        text = '<table>'

        if gps_value is not None:
            text = '<tr><td><b>Longitude</b>: ' + gps_value['lon'] + '° '+\
            '<td><b>Latitude</b>: ' + gps_value['lat'] + '°<br>'+\
            '<tr><td><b>Altitude</b>: ' + gps_value['alt'] + 'm ' +\
            '<td><b>Speed</b>: ' + gps_value['spd'] + 'm/s<br>'
            self.__gmap_.addMarker(time, gps_value['lat'], gps_value['lon'])
            self.__markers_.add(time)
        else:
            text= 'Data are not available'

        if self.__markers_ and time < max(self.__markers_):
            for i in range(time+1, max(self.__markers_)+1):
                if i in self.__markers_:
                    self.__gmap_.deleteMarker(i)
                    self.__markers_.remove(i)

        self.txtGpsData.setText(text)

    def stop_slider(self):
        self.sldTime.setValue(0)
        self.setValuesAtTime()

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