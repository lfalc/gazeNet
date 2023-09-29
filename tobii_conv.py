import pandas
import numpy as np
import csv

from utils_lib.etdata import ETData

fpath = 'Kreuze_Random Recording1.tsv'

with open(fpath, 'r') as f:
    tobii_raw = csv.DictReader(f, delimiter='\t')



t = tobii_raw['Recording timestamp']
fs = 1000
t = np.arange(0, len(t)).astype(np.float64)/fs

x = tobii_raw['Gaze point X']
y = tobii_raw['Gaze point Y']

status = np.arange(0, len(t)).astype(np.bool_)
evt = np.arange(0, len(t)).astype(np.uint8)

data = np.vstack((t, x, y, status, evt)).T

etdata = ETData()
etdata.load(data, **{'source': 'np_array'})

print("Done")
