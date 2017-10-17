#!/usr/bin/python3.4

import sys
from Utils import Utilities
from os.path import expanduser
from PySide.QtGui import QApplication, QMainWindow, QMessageBox, QFileDialog
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    __is_active_ = False
    __dict_canbus_ = dict()

    def __init__(self, parent=None):
        '''Mandatory initialisation of a class.'''
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionOpen_archive.triggered.connect(self.select_file)
        self.btnStop.clicked.connect(self.stop_slider)
        self.txtCANBUS.setText("Click File -> Open Archive and the select a valid"
                               "archive in order to start the analysis")
        self.sldTime.valueChanged.connect(self.setValuesAtTime)

    def show_about(self):
        #Popup a box with about message.
        QMessageBox.about(self, "About CANBUS Analyzer", Utilities.get_about())

    def select_file(self):
        archiveName = str(expanduser("~") + "/Test/Test completi/nuove_guide_031017/prima guida/test.gz")
                        #QFileDialog.getOpenFileName(self,
                         #                         "Open gzip Archive",
                          #                        str(expanduser("~")+"/Test/Test completi/nuove_guide_031017/prima guida"),
                           #                       "Archive File (*.gz)"
                            #                      )[0]
        if archiveName == '':
            return

        if not Utilities.extract_files(archiveName):
            QMessageBox.critical(self, "Error", "Impossible to extract the archive!")
            return

        #QMessageBox.information(self, "Information", "Archive extracted!")
        self.__is_active_ = True
        self.txtCANBUS.setText("")
        Utilities.init_slider(self.sldTime)
        Utilities.init_time_labels(self)
        Utilities.init_dict_canbus(self.__dict_canbus_)

    def setValuesAtTime(self):
        time = int(self.sldTime.value())
        self.txtCANBUS.setText('')
        self.lblTime.setText(str(time)+'s')
        #clear everything
        if time == 0:

            return
        values = self.__dict_canbus_[time]
        text = ''

        for v in values:
            text += '<b>ID</b>:' + v[0] + ' <b>PAYLOAD</b>: ' + v[1] + '<br>'

        self.txtCANBUS.setText(text)

    def stop_slider(self):
        self.sldTime.setValue(0)
        self.setValuesAtTime()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()

    sys.exit(app.exec_())