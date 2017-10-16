import sys
from Utils import Utilities
from os.path import expanduser

from PySide.QtGui import QApplication, QMainWindow, QMessageBox, QFileDialog

from ui_main import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        '''Mandatory initialisation of a class.'''
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionOpen_archive.triggered.connect(self.select_file)

    def show_about(self):
        #Popup a box with about message.
        QMessageBox.about(self, "About CANBUS Analyzer", Utilities.get_about())

    def select_file(self):
        archiveName = QFileDialog.getOpenFileName(self,
                                                  "Open gzip Archive",
                                                  str(expanduser("~")),
                                                  "Archive File (*.gz)"
                                                  )[0]
        if archiveName != '':
            Utilities.extract_files(archiveName)
            QMessageBox.information(self, "Information", "Archive extracted!")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()

    sys.exit(app.exec_())