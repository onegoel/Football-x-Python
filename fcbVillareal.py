import json
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch
import seaborn as sns

df = pd.read_json('68320.json')
cols_to_keep = ['type', 'player', 'location']
all_cols = list(df.columns)
df = df.drop(list((set(all_cols) - set(cols_to_keep))), axis=1)
df = df.dropna(subset=cols_to_keep)
df = df.reset_index()

player_dict = dict(df['player'])
player = []

for idx in player_dict:
    del player_dict[idx]['id']

for idx in player_dict:
    player.append(player_dict[idx]['name'])

df['player'] = player
df.drop(df[df['player'] != 'Ronaldo de Assis Moreira'].index, inplace=True)
df = df.reset_index()
del df['player']


type_dict = dict(df['type'])
type = []

for idx in type_dict:
    del type_dict[idx]['id']

for idx in type_dict:
    type.append(type_dict[idx]['name'])

df['type'] = type
df.drop(df[df['type'] == 'Ball Receipt*'].index, inplace=True)
del df['level_0'], df['index']
df = df.reset_index()
print(df.head(20))

loc_list = list(df['location'])
x = []
y = []

for item in loc_list:
    x.append(item[0])
    y.append(item[1])

del df['location']
# del df['level_0'], df['index']
df['x'] = x
df['y'] = y

df = df.reset_index()

print(df)

fig, ax = plt.subplots(figsize=(13.5, 8))
fig.set_facecolor('#22312b')
ax.patch.set_facecolor('#22312b')

pitch = Pitch(pitch_type='statsbomb', orientation='horizontal',
              pitch_color='orange', line_color='#c7d5cc', figsize=(13.5, 8),
              constrained_layout=False, tight_layout=True)

pitch.draw(ax=ax)
plt.gca().invert_yaxis()

kde = sns.kdeplot(
    df['x'],
    df['y'],
    shade = True,
    shade_lowest = False,
    alpha = .5,
    n_levels = 10,
    cmap = 'ocean'
)

plt.title("Ronaldinho Heat Map vs Villareal", color = 'w', size = 10)
plt.show()
