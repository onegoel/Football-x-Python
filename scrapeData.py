import requests
from bs4 import BeautifulSoup
import json 
import pandas as pd

base_url = 'https://understat.com/match/'
match_id = str(input('Enter match id : '))
url = base_url + match_id

res = requests.get(url)
soup = BeautifulSoup(res.content)

scripts = soup.find_all('script')

strings = scripts[1].string

ind_start = strings.index("('")+2 
ind_end = strings.index("')") 
json_data = strings[ind_start:ind_end] 
json_data = json_data.encode('utf8').decode('unicode_escape')
data = json.loads(json_data)

x = []
y = []
xG = []
player = [] 
result = []
team = []
data_away = data['a']
data_home = data['h']

# print(data_home)

for index in range(len(data_home)):
    for key in data_home[index]:
        if key == 'X':
            x.append(data_home[index][key])
        if key == 'Y':
            y.append(data_home[index][key])
        if key == 'h_team':
            team.append(data_home[index][key])
        if key == 'xG':
            xG.append(data_home[index][key])
        if key == 'result':
            result.append(data_home[index][key])
        if key == 'player':
            player.append(data_home[index][key])

''''
for index in range(len(data_away)):
    for key in data_away[index]:
        if key == 'X':
            x.append(data_away[index][key])
        if key == 'Y':
            y.append(data_away[index][key])
        if key == 'a_team':
            team.append(data_away[index][key])
        if key == 'xG':
            xG.append(data_away[index][key])
        if key == 'result':
            result.append(data_away[index][key])
        if key == 'player':
            player.append(data_away[index][key])

col_names = ['x','y','xG','result','player','team']
df = pd.DataFrame([x,y,xG,result,player,team],index=col_names)
df = df.T

print(df)
'''

ds = pd.DataFrame()

ds['player'] = player
ds['X'] = x
ds['Y'] = y
ds['result'] = result
ds['xG'] = xG

print(ds)