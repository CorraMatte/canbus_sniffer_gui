import platform
import pickle
import gzip
import os
import PySide
import ffmpy

GPS_FILE = 'gps.log'
CAMERA_FILE = 'video.h264'
CAMERA_MP4_FILE = 'video.mp4'
CAN_FILE = 'extracted.1.csv'
OUTPUT_FOLDER = '/home/corra/Scrivania/log_files/'
__version__ = "1.0"


# Get information string about the project
def get_about():
    return """<b>CANBUS Analyzer GUI</b> v{}
                <p>Copyright &copy; 2017 Matteo Corradini.
                All rights reserved in accordance with GPL v2 or later 
                - NO WARRANTIES! <p>This application can be used for
                displaying CANBUS data associated with GPS data and video. The
                project could be found at the following GIT repository:
                <a href='https://github.com/CorraMatte/buildroot-rpi3-sniffer'>
                buildroot-rpi3-sniffer</a>.
                <p>Python {} - PySide version {} 
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


# Get GPS values from the file line
def get_gps_values(line):
    return {
        'alt': line[1],
        'lat': line[2],
        'lon': line[3],
        'spd': line[4]
    }


# Get id and payload from file line
def get_id_payload(line):
    id = line[2]
    p = line[4]
    payload = ''
    for i in range(7):
        payload += format((int(p[i*8:(i+1)*8-1],2)), '02X') + ' '

    return [id, payload]


# Convert Video to MP4
def convert_video_to_mp4():
    if os.path.isfile(OUTPUT_FOLDER + CAMERA_MP4_FILE):
        os.remove(OUTPUT_FOLDER + CAMERA_MP4_FILE)

    ff = ffmpy.FFmpeg(
        inputs={OUTPUT_FOLDER + CAMERA_FILE: None},
        outputs={OUTPUT_FOLDER + CAMERA_MP4_FILE: None}
    )

    ff.run()