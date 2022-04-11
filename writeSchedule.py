#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
from nfl_reader import teams,games_by_team,team_schedules,all_games,team_names

for i in range(len(all_games)):
    if all_games[i] == 'JAC':
        all_games[i] = 'JAX'
    elif all_games[i] == '@JAC':
        all_games[i] = '@JAX'


# In[ ]:





# In[ ]:





# In[3]:


games_by_week = {}
for i in range(1,19):
    games_by_week[i] = []


# In[ ]:





# In[4]:


data = open('nflschedule.csv')
csv_data = csv.reader(data)
data_lines = list(csv_data)


# In[5]:


games = list([f'{line[4]}' , f'{line[5]}'] for line in data_lines[1:])


# In[6]:


matchups = []
for i in games:
    game = []
    for j in i:
        for key, val in team_names.items():
            if j == key:
                game.append(val)
    matchups.append(game)
                       


# In[22]:


for key, val in games_by_week.items():
    weekly_matchups = []
    for line in data_lines[1:]:
        if int(line[1]) == key:
            weekly_matchups.append([line[4],line[5]])
    games_by_week[key] = weekly_matchups
    


# In[23]:


games_by_week


# In[ ]:

def find_abb(home_name,away_name):
    for key,val in team_names.items():
        if home_name == key:
            home_a = val
        elif away_name == key:
            away_a = val
    return[home_a, away_a]


