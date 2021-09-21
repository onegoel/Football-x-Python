import json
from numpy.core.numeric import NaN
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch
import seaborn as sns

df = pd.read_json('3750200.json')

# df.drop(df[df['type']['name'] != 'shot'].index, inplace=True)

cols_to_drop = ['id', 'index', 'period', 'timestamp', 'minute', 'second',
                'possession', 'possession_team', 'duration',
                'tactics', 'related_events', 'pass',
                'carry', 'under_pressure', 'duel', 'off_camera', 'ball_receipt',
                'foul_won', 'clearance', 'counterpress', 'interception', 'dribble',
                'out', 'goalkeeper', 'foul_committed', 'ball_recovery', '50_50',
                'miscontrol', 'block', 'substitution', 'type']

df = df.drop(cols_to_drop, axis=1)
df = df.dropna(subset=['shot'])

play_dict = dict(df['play_pattern'])
play = []

for idx in play_dict:
    del play_dict[idx]['id']

for idx in play_dict:
    play.append(play_dict[idx]['name'])

df['play_pattern'] = play

player_dict = dict(df['player'])
player = []

for idx in player_dict:
    del player_dict[idx]['id']

for idx in player_dict:
    player.append(player_dict[idx]['name'])

df['player'] = player

shot_dict = dict(df['shot'])
xG = []
outcome = []

for idx in shot_dict:
    del shot_dict[idx]['freeze_frame']

for idx in shot_dict:
    for key in shot_dict[idx]:
        if key == 'statsbomb_xg':
            xG.append(shot_dict[idx][key])
        # if key == 'end_location':
            # end_loc.append(shot_dict[idx][key])
        if key == 'outcome':
            for key1 in shot_dict[idx][key]:
                if key1 == 'name':
                    outcome.append(shot_dict[idx][key][key1])

del df['shot'], df['position']
df['xG'] = xG
# df['end_loc'] = end_loc
df['outcome'] = outcome

# print(df)

loc_list = list(df['location'])
x = []
y = []

for item in loc_list:
    x.append(item[0])
    y.append(item[1])

# print(x)
# print(y)

del df['location']
df['x'] = x
df['y'] = y

df = df.reset_index()

team = []

for idx in range(len(df)):
    for key in df['team'][idx]:
        if key == 'name':
            team.append(df['team'][idx][key])

print(team)


ds = pd.DataFrame()
dp = pd.DataFrame()

ds = df.loc[df['player'] == 'Steven Gerrard']
dp = df.loc[df['player'] == 'Filippo Inzaghi']
ds = ds.reset_index()
dp = dp.reset_index()

# print(ds)
# Steven Gerrard
# print(dp)
# Pippo Inzaghi
'''
fig, ax = plt.subplots(figsize=(13.5, 8))
fig.set_facecolor('white')
ax.patch.set_facecolor('white')

pitch = Pitch(pitch_color='grass', line_color='white', stripe=True)
pitch.draw(ax=ax)

plt.gca().invert_yaxis()


for x in range(len(ds['x'])):
    if ds['outcome'][x] == 'Goal':
        plt.scatter(ds['x'][x], ds['y'][x], color='blue')
    else:
        plt.scatter(ds['x'][x], ds['y'][x], color='red')

plt.title('Gerrard Shots vs Milan (2007 UCL Final)',color='black',size=20)
plt.show()


for x in range(len(dp['x'])):
    if dp['outcome'][x] == 'Goal':
        plt.scatter(dp['x'][x], dp['y'][x], color='blue')
    else:
        plt.scatter(dp['x'][x], dp['y'][x], color='red')

plt.title('Inzaghi Shots vs Liverpool (2007 UCL Final)',color='black',size=20)
plt.show()
'''