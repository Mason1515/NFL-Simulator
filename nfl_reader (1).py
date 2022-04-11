#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import random
import requests
import bs4





data = open('nfl_teams.csv')





csv_data = csv.reader(data)





data_lines = list(csv_data)




global teams
teams = []




teams = [line[2] for line in data_lines[1:]]
team_names = {}




def pick_teams():
    home_team = random.choice(teams)
    away_team = random.choice(teams)
    while home_team == away_team:
        away_team = random.choice(teams)
    return [home_team,away_team]




team_names = {line[1]: line[2] for line in data_lines[1:]}





global games_by_week






def find_name(home_team,away_team):
    for key, val in team_names.items():
        if val == home_team:
            home_team_name = key
        elif val == away_team:
            away_team_name = key
        

    return [home_team_name, away_team_name]


# In[12]:

res = requests.get('https://www.fftoday.com/nfl/schedule_grid_21.html')

soup = bs4.BeautifulSoup(res.text,'lxml')

# In[13]:

all_games = []
for item in soup.select('.smallestbody'):
    if len(item.text) <= 4:
        all_games.append(item.text)

for i in range(len(all_games)):
    if all_games[i] == 'JAC':
        all_games[i] = 'JAX'
    elif all_games[i] == '@JAC':
        all_games[i] = '@JAX'

        
        
        
games_by_team = [all_games[i * 18:(i + 1) * 18] for i in range((len(all_games) + 18 - 1) // 18 )]



team_schedules = {}
for i in range(len(teams)):
    team_schedules[teams[i]] = games_by_team[i]



# In[57]:
games_by_week = {}
for i in range(1,19):
    game_list = []
    for team in teams:
        if team not in game_list:
            game_list.append([team, team_schedules[team][i-1]])
            games_by_week[i] = game_list





# In[60]:

for val in games_by_week.values():
    for i in val:
        if i[1] == 'JAC':
            i[1] = 'JAX'
        elif i[1] == '@JAC':
            i[1] = '@JAX'



# In[61]:


for val in games_by_week.values():
    for i in val:
        for j in i:
            for k in j:
                if k == '@' or len(k) > 3:
                    val.remove(i)


# In[ ]:
divisions = [f'{line[3]} {line[4]}' for line in data_lines[1:]]

teams_by_division = {}
for i in set(divisions):
    team_list = []
    for line in data_lines[1:]:
        if f'{line[3]} {line[4]}' == i:
            team_list.append(line[2])
    teams_by_division[i] = team_list
    


records_by_team = {}
for i in teams:
    records_by_team[i] = [0,0]



# In[ ]:


division_records = {}
for i in teams:
    division_records[i] = [0,0]

division_winners = {}
for i in teams_by_division.keys():
    division_winners[i] = ''


# In[ ]:




