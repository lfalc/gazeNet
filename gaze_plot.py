import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


path = Path('etdata/tobii_gazeNet/')
files = path.glob('*.npy')

for fname in files:
    with fname.open() as file:
        gaze_data = np.load('etdata/tobii_gazeNet/Kreuze_Random Recording2.npy')

        plt.plot(gaze_data['x'], gaze_data['y'])
        plt.savefig('foo.png')
print('Done.')