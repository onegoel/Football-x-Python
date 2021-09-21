import json
from numpy.core.fromnumeric import size
from numpy.core.numeric import NaN 
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch
import seaborn as sns

dt = pd.read_json('jPass.json')
del dt['ball_receipt']

df = pd.DataFrame(dt)

player_dict = dict(df['player'])
players = []

for idx in player_dict:
    del player_dict[idx]['id']

for idx in player_dict:
    for idx1 in player_dict[idx]:
        if idx1 == 'name':
            players.append(player_dict[idx][idx1])

df['player'] = players

pass_dict = dict(df['pass'])

for idx in pass_dict:
    del pass_dict[idx]['length']
    del pass_dict[idx]['angle']

pass_type = []
start_loc = []
foot = []
end_loc = []
x1 = []
y1 = []
x2 = []
y2 = []

for key in pass_dict:
    for key1 in pass_dict[key]:
        if key1 == 'height':
            for key2 in pass_dict[key][key1]:
                if key2 == 'name':
                    pass_type.append(pass_dict[key][key1][key2])
        if key1 == 'end_location':
            x2.append(pass_dict[key][key1][0])
            y2.append(pass_dict[key][key1][1])
            end_loc.append(pass_dict[key][key1])

pass_loc = list(df['location'])

for key in pass_loc:
    x1.append(key[0])
    y1.append(key[1])
    start_loc.append(key)

del df['pass'], df['location'], df['type']

df['pass_type'] = pass_type
df['x1'] = x1
df['y1'] = y1
df['x2'] = x2
df['y2'] = y2

df.drop(df[df['player'] != 'Lionel Andrés Messi Cuccittini'].index, inplace = True)
del df['player']

df = df.reset_index()


fig, ax = plt.subplots(figsize=(13.5,8))
fig.set_facecolor('white')
ax.patch.set_facecolor('white')
pitch = Pitch(pitch_color='grass', line_color='white', stripe=True)
pitch.draw(ax=ax)
plt.gca().invert_yaxis()

for idx in range(len(df)):
    plt.plot((df['x1'][idx],df['x2'][idx]),(df['y1'][idx],df['y2'][idx]), '--r')
    plt.scatter(df['x1'][idx],df['y1'][idx], color='red') 

plt.show()


























'''
x1 = []
y1 = []
x2 = []
y2 = []
type = []
minute = []

for index in range(len(data)) :
    for key in data[index] :
        if key == 'minute' :
            minute.append(data[index][key])
        if key == 'type' :
            for key1 in range(2) :
                if key1 == 'name' :
                    if data[index][key][key1] == 'Pass' or data[index][key][key1] == 'High Pass' or data[index][key][key1] == 'Ground Pass' :
                        type.append(data[index][key][key1]) 
        if key == 'player' :
            for key2 in range(2) :
                if key2 == 'name' :
                    if data[index][key][key1] == 'Lionel Andrés Messi Cuccittini' :
                        pass
                    else :
                        type.pop
                        minute.pop
                        continue
        if key == 'pass' :
            for key3 in range(len(data[index][key])) : 
                if key3 == 'location' :
                    x1.append(data[index][key][key3][0])
                    y1.append(data[index][key][key3][1])
                if key3 == 'end_location' :
                    x2.append(data[index][key][key3][0])
                    y2.append(data[index][key][key3][1])

print(x1)
'''