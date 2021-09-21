import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch
import seaborn as sns

df = pd.read_csv('messibetis.csv')
del df['player'], df['type']

df['x'] = df['x']*1.2
df['y'] = df['y']*0.8
df['endX'] = df['endX']*1.2
df['endY'] = df['endY']*0.8

fig, ax = plt.subplots(figsize=(13.5,8))
fig.set_facecolor('white')
ax.patch.set_facecolor('white')

#this is how we create the pitch
pitch = Pitch(pitch_color='grass', line_color='white', stripe=True)

#Draw the pitch on the ax figure as well as invert the axis for this specific pitch
pitch.draw(ax=ax)
plt.gca().invert_yaxis()

#use a for loop to plot each pass

print(df)

for x in range(len(df['x'])):
    if df['outcome'][x] == 'Successful':
        plt.plot((df['x'][x],df['endX'][x]),(df['y'][x],df['endY'][x]),color='blue')
        plt.scatter(df['x'][x],df['y'][x],color='blue')
    if df['outcome'][x] == 'Unsuccessful':
        plt.plot((df['x'][x],df['endX'][x]),(df['y'][x],df['endY'][x]),color='red')
        plt.scatter(df['x'][x],df['y'][x],color='red')

plt.title('Messi Passes vs Betis',color='black',size=20)
plt.show()