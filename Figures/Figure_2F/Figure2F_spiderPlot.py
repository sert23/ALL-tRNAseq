import numpy as np
import matplotlib.pyplot as plt
import sys
import pandas as pd
import math

###Read data

file_path = sys.argv[1]

exp_df = pd.read_csv(file_path, sep="\t")

# Set data
df = pd.DataFrame({
    'group': ['A', 'B', 'C', 'D'],
    'var1': [38, 1.5, 30, 4],
    'var2': [29, 10, 9, 34],
    'var3': [8, 39, 23, 24],
    'var4': [7, 31, 33, 14],
    'var5': [28, 15, 32, 14]
})

t_df = exp_df.T
t_df.columns = t_df.iloc[0]
t_df = t_df[1:]
t_df = t_df.reindex(sorted(t_df.columns), axis=1)
t_df = t_df+1
t_df = t_df.applymap(math.log10)

values_dict = {}
for i,row in t_df.iterrows():
    values = t_df.loc[i].values.flatten().tolist()
    values += values[:1]
    values_dict[row.name] = values

maxi = t_df.max().max()

categories = list(t_df)
N = len(categories)
angles = [n / float(N) * 2 * math.pi for n in range(N)]
angles += angles[:1]

ax = plt.subplot(111, projection='polar')


for sample,values in values_dict.items():
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=sample)

# Draw one axe per variable + add labels
plt.xticks(angles[:-1], categories, color='grey', size=10)

##Set angle in labels
plt.gcf().canvas.draw()
angles = np.linspace(0,2*np.pi,len(ax.get_xticklabels())+1)
angles[np.cos(angles) < 0] = angles[np.cos(angles) < 0] + np.pi
angles = np.rad2deg(angles)
labels = []
for label, angle in zip(ax.get_xticklabels(), angles):
    x,y = label.get_position()
    lab = ax.text(x,y-.08, label.get_text(), transform=label.get_transform(),
                  ha=label.get_ha(), va=label.get_va())
    lab.set_rotation(angle)
    labels.append(lab)
ax.set_xticklabels([])
#
real_maxi = 10**maxi
possible_steps = [100,1000,10000,100000]
steps = []
for s in possible_steps:
    if s < real_maxi:
        steps.append(s)
        last_small = True
    if s > real_maxi and last_small:
        steps.append(s)
        last_small = False

trans_steps = [math.log10(x) for x in steps]
possible_ticks = ["","","",""]

ticks = possible_ticks[:len(steps)]

plt.yticks(trans_steps, ticks, color="grey", size=7)
plt.ylim(0, max(trans_steps)+0.10*max(trans_steps))

#Legend

plt.legend(loc='lower right', bbox_to_anchor=(0.85, -0.1, 0.6, 0.8))


plt.show()

