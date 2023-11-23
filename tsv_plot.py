import matplotlib.pyplot as plt
import pandas as pd

# Read csv file
fpath = 'etdata/timur_gazeNet/ohne_kal.tsv'
with open(fpath, 'r') as f:
    df = pd.read_csv(f, sep='\t', header=0)

evt_color_map = dict({
        0: 'gray',  # 0. Undefined
        1: 'b',  # 1. Fixation
        2: 'r',  # 2. Saccade
        3: 'y',  # 3. Post-saccadic oscillation
        4: 'm',  # 4. Smooth pursuit
        5: 'k',  # 5. Blink
        9: 'k',  # 9. Other
    })
#%% Plot
fig, ax = plt.subplots()
# ax.plot(df['Recording timestamp'], df['Gaze point X'], label='x')

for e, c in evt_color_map.items():
    ax.scatter(df['Recording timestamp'][df['evt'] == e], df['Gaze point X'][df['evt'] == e], c=c, label=e)

# %%
