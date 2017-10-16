import platform
import pickle
import gzip
import os

import PySide

GPS_FILE = 'gps.log'
CAMERA_FILE = 'video.h264'
CAN_FILE = 'extracted.1.csv'
OUTPUT_FOLDER = 'log_files/'

__version__ = "1.0"

# Get the about text
def get_about():
    return """<b>CANBUS Analyzer GUI</b> v{}
                <p>Copyright &copy; 2010 Joe Bloggs.
                All rights reserved in accordance with GPL v2 or later 
                - NO WARRANTIES! <p>This application can be used for
                displaying platform details. <p>Python {} - PySide version {} 
                - Qt version {} on {}""".format(__version__,
                                            platform.python_version(),
                                            PySide.__version__,
                                            PySide.QtCore.__version__,
                                            platform.system())

def extract_files(archive_name):
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    with gzip.open(archive_name, 'rb') as f:
        c = pickle.loads(f.read())

    f = open(OUTPUT_FOLDER + GPS_FILE, 'w')
    f.writelines(l for l in c['gps'])
    f.close()

    f = open(OUTPUT_FOLDER + CAN_FILE, 'w')
    f.writelines(l for l in c['can'])
    f.close()

    f = open(OUTPUT_FOLDER + CAMERA_FILE, 'wb')
    f.write(c['camera'])
    f.close()

