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


# Get information string about the project
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


# Extract files from the archive
def extract_files(archive_name):
    try:
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
        return True
    except Exception:
        return False


# Change seconds to the formatted time
def get_time_from_seconds(time):
    time = int(time)
    m, s = divmod(time, 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)