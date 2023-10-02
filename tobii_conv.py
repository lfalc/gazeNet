'''
This script converts Tobii eyetracking data from a .tsv file to a .npy file.
The samples are stored in a numpy array of ETData format.
'''
import pandas as pd
import numpy as np

from utils_lib.etdata import ETData, get_px2deg

fpath = 'etdata\\tobii\\Kreuze_Random Recording1_filtered.tsv'
raw_data = pd.read_csv(fpath, sep='\t', header=0)

#%% remove mouse samples and invalid samples
mask = (raw_data['Sensor'] == 'Eye Tracker') \
    & (raw_data['Validity left'] == 'Valid') \
    & (raw_data['Validity right'] == 'Valid')
raw_data = raw_data[mask]
raw_data.reset_index(drop=True, inplace=True)

geom = {
    'screen_width' : 16,
    'screen_height': 9,
    'display_width_pix' : raw_data['Recording resolution width'][0],
    'display_height_pix' : raw_data['Recording resolution height'][0],
    'eye_distance' : 80,
}
px2deg = get_px2deg(geom)

t = raw_data['Recording timestamp']
fs = 1000
t = np.arange(0, len(t)).astype(np.float64)/fs
x = raw_data['Gaze point X']
y = raw_data['Gaze point Y']
x = (x - geom['display_width_pix']/2) / px2deg
y = (y - geom['display_height_pix']/2) / px2deg

status = np.arange(0, len(t)).astype(np.bool_)
status[:] = True
evt = np.arange(0, len(t)).astype(np.uint8)
evt[:] = True
data = np.vstack((t, x, y, status, evt)).T

etdata = ETData()
etdata.load(data, **{'source': 'np_array'})
etdata.save('etdata\\tobii\\Kreuze_Random Recording1.npy')

print("Done")
