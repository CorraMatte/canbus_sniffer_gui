import PySide
import math

GPS_FILE = 'gps.log'
CAMERA_FILE = 'video.h264'
CAN_FILE = 'extracted.1.csv'
OUTPUT_FOLDER = 'log_files/'


def init_slider(slider):
    f = open(OUTPUT_FOLDER + CAN_FILE)
    last_line = f.readlines()[-1]
    slider.setMinimum(0)
    slider.setMaximum(int(math.ceil(float(last_line.split(',')[0]))))
    slider.setValue(0)
    slider.setPageStep(1)


def init_time_labels(main_window):
    main_window.lblTime.setText('0s')
    main_window.lblTime.setEnabled(True)
    main_window.lblMinTime.setEnabled(True)
    main_window.lblMaxTime.setEnabled(True)
    main_window.lblMaxTime.setText(str(main_window.sldTime.maximum())+'s')


def init_time_buttons(main_window):
    main_window.btnStop.setEnabled(True)
    main_window.btnPlay.setEnabled(True)
    main_window.btnSxArrow.setEnabled(True)
    main_window.btnDxArrow.setEnabled(True)


def get_id_payload(line):
    id = line[2]
    p = line[4]
    payload = ''
    for i in range(7):
        payload += format((int(p[i*8:(i+1)*8-1],2)), '02X') + ' '

    return [id, payload]


def init_dict_canbus(dict_canbus):
    f = open(OUTPUT_FOLDER + CAN_FILE).readlines()
    sec = int(math.ceil(float(f[-1].split(',')[0])))
    ids = set()
    values = []
    for l in reversed(f[1:]):
        l = l.split(',')
        c = get_id_payload(l)
        s = int(math.ceil(float(l[0])))

        if sec != s:
            dict_canbus[sec] = values
            sec = s
            ids = set()
            values = []

        if c[0] not in ids:
            ids.add(c[0])
            values.append(c)


def get_gps_values(line):
    return {
        'alt': line[1],
        'lat': line[2],
        'lon': line[3],
        'spd': line[4]
    }


def init_dict_gps(dict_gps):
    f = open(OUTPUT_FOLDER + GPS_FILE).readlines()

    for l in f[1:]:
        l = l.split(',')
        d = get_gps_values(l)
        s = int(math.ceil(float(l[0])))
        dict_gps[s] = d

    last_key = min(dict_gps)
    for i in range(min(dict_gps), max(dict_gps)-1):
        if i not in dict_gps.keys():
            dict_gps[i] = dict_gps[last_key]
        else:
            last_key = i


def init_google_maps(gmap, dict_gps):
    gmap.setSizePolicy(
        PySide.QtGui.QSizePolicy.MinimumExpanding,
        PySide.QtGui.QSizePolicy.MinimumExpanding)
    gmap.waitUntilReady()
    lons = []
    lats = []
    for g in dict_gps.values():
        lons.append(float(g['lon']))
        lats.append(float(g['lat']))
    gmap.centerAt(max(lats),max(lons))
    gmap.setZoom(11)