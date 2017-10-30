import PySide
import math
from PySide.phonon import Phonon
from Utils import Utilities


# Set slider settings
def init_slider(slider):
    slider.setMinimum(0)
    slider.setValue(0)
    slider.setPageStep(1)


# Enable and set timer labels
def init_time_labels(main_window):
    main_window.lblTime.setVisible(True)
    main_window.lblMaxTime.setVisible(True)
    main_window.lblTime.setEnabled(True)
    main_window.lblMinTime.setEnabled(True)
    main_window.lblMaxTime.setEnabled(True)


# Enable timer buttons
def init_time_buttons(main_window):
    main_window.btnStop.setEnabled(True)
    main_window.btnPlay.setEnabled(True)
    main_window.btnSxArrow.setEnabled(True)
    main_window.btnDxArrow.setEnabled(True)


# Create the canbus data structure in order to retrieve information at runtime
# at O(1) cost
def init_dict_canbus(dict_canbus):
    f = open(Utilities.OUTPUT_FOLDER + Utilities.CAN_FILE).readlines()
    sec = int(math.ceil(float(f[-1].split(',')[0])))
    ids = set()
    values = []
    for l in reversed(f[1:]):
        l = l.split(',')
        c = Utilities.get_id_payload(l)
        s = int(math.ceil(float(l[0])))

        if sec != s:
            dict_canbus[sec] = values
            sec = s
            ids = set()
            values = []

        if c[0] not in ids:
            ids.add(c[0])
            values.append(c)


# Create the GPS data structure in order to retrieve information at runtime
# at O(1) cost
def init_dict_gps(dict_gps):
    f = open(Utilities.OUTPUT_FOLDER + Utilities.GPS_FILE).readlines()

    for l in f[1:]:
        l = l.split(',')
        d = Utilities.get_gps_values(l)
        s = int(math.ceil(float(l[0])))
        dict_gps[s] = d

    last_key = min(dict_gps)
    for i in range(min(dict_gps), max(dict_gps)):
        if i not in dict_gps.keys():
            dict_gps[i] = dict_gps[last_key]
        else:
            last_key = i


# Create Google Maps witht centered at the initial position
def init_google_maps(gmap):
    gmap.setSizePolicy(
        PySide.QtGui.QSizePolicy.MinimumExpanding,
        PySide.QtGui.QSizePolicy.MinimumExpanding
    )
    gmap.waitUntilReady()
    gmap.setZoom(13)


# Create video and make it seekable
def init_video(main_window):
    file_path = Utilities.OUTPUT_FOLDER + Utilities.CAMERA_FILE
    media_src = Phonon.MediaSource(file_path)
    main_window.media_obj = Phonon.MediaObject(main_window.wdgVideo)
    main_window.media_obj.setCurrentSource(media_src)
    main_window.video_widget = Phonon.VideoWidget(main_window.wdgVideo)
    Phonon.createPath(main_window.media_obj, main_window.video_widget)
    main_window.video_widget.setGeometry(main_window.wdgVideo.geometry())
    main_window.video_widget.show()
    main_window.media_obj.play()
    main_window.media_obj.pause()
