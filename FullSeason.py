#!/usr/bin/env python
# coding: utf-8

# In[2]:


from nfl_reader import find_name, teams, team_names,teams_by_division
from playGameAndWeek import roll
from writeSchedule import games_by_week


# In[3]:


records_by_team = {}
for i in teams:
    records_by_team[i] = [0,0]
    
division_records = {}
for i in teams:
    division_records[i] = [0,0]

division_winners = {}
for i in teams_by_division.keys():
    division_winners[i] = ''

conferences = {}
for i in teams_by_division:
    conferences[i[0:3]] = []


# In[4]:


def playGame(home_team,away_team):
    quarters = 8
    global home_score
    global away_score
    home_score = 0
    away_score = 0
    
    
    
    global home_team_a
    global away_team_a
    global box_score_home
    global box_score_away
    box_score_home = []
    box_score_away = []
    
    
    
    home_team_a = find_abb(current_game[0],current_game[1])[0]
    away_team_a = find_abb(current_game[0],current_game[1])[1]
    print(f"{away_team} @ {home_team}")


    while quarters > 0:
        
        
            
        score = roll()
        box_score_home.append(score)
        home_score += score
        if home_score > away_score:
            print(f"{home_score}-{away_score} {home_team_a}")
        elif away_score > home_score:
            print(f"{home_score}-{away_score} {away_team_a}")
        else:
            print(f"{home_score}-{away_score}")
        quarters -= 1
            
                
      
       
        score = roll()
        box_score_away.append(score)
        away_score += score
        if home_score > away_score:
            print(f"{home_score}-{away_score} {home_team_a}")
        elif away_score > home_score:
            print(f"{home_score}-{away_score} {away_team_a}")
        else:
            print(f"{home_score}-{away_score}")
        quarters -= 1
        if quarters == 4:
            print("Halftime.")
                
    if home_score == away_score:
        print("Overtime!\n")
        
        OTroll1 = roll()
        OTroll2 = roll()
        while OTroll1 == OTroll2:
            OTroll1 = roll()
            OTroll2 = roll()
        if OTroll2 >= 7:
            home_score += 6
            box_score_home.append(6)
            box_score_away.append(0)
        elif OTroll1 >= 7:
            away_score += 6
            box_score_away.append(6)
            box_score_home.append(0)
        elif OTroll2 == 3 and OTroll1 < 7:
            home_score += 3
            box_score_home.append(3)
            box_score_away.append(0)
        elif OTroll2 < 7 and OTroll1 == 3:
            away_score += 3
            box_score_away.append(3)
            box_score_home.append(0)
    
    
    if home_score > away_score:
        print(f"{home_team} win {home_score}-{away_score}")
        print_box_score(box_score_home,box_score_away)
        print("\n")
    elif away_score > home_score:
        print(f"{away_team} win {away_score}-{home_score}")
        print_box_score(box_score_home,box_score_away)
        print("\n")
    
                
def find_abb(home_name,away_name):
    for key,val in team_names.items():
        if home_name == key:
            home_a = val
        elif away_name == key:
            away_a = val
    return[home_a, away_a]                    

def print_box_score(box_score1,box_score2):
    print("Box Score: ")
    if len(box_score_home) == 4:
        print("     1   2   3   4")
        print(f"{home_team_a}: {box_score_home[0]}   {box_score_home[1]}   {box_score_home[2]}   {box_score_home[3]}")
        print(f"{away_team_a}: {box_score_away[0]}   {box_score_away[1]}   {box_score_away[2]}   {box_score_away[3]}")
    elif len(box_score_home) > 4:
        print("     1   2   3   4   OT")
        print(f"{home_team_a}: {box_score_home[0]}   {box_score_home[1]}   {box_score_home[2]}   {box_score_home[3]}   {box_score_home[4]}")
        print(f"{away_team_a}: {box_score_away[0]}   {box_score_away[1]}   {box_score_away[2]}   {box_score_away[3]}   {box_score_away[4]}")
    if home_score > away_score:
        print("\n")
        for key,val in records_by_team.items():
            if home_team_a == key:
                val[0] += 1
                print(f'{home_team_a} improves to {val[0]}-{val[1]}')
            elif away_team_a == key:
                val[1] += 1
                print(f'{away_team_a} falls to {val[0]}-{val[1]}')
               
        for division,team in teams_by_division.items():
            if home_team_a in teams_by_division[division] and away_team_a in teams_by_division[division]:
                division_records[home_team_a][0] += 1
                division_records[away_team_a][1] += 1
    else:
        print("\n")
        for key,val in records_by_team.items():
            if away_team_a == key:
                val[0] += 1
                print(f'{away_team_a} improves to {val[0]}-{val[1]}')
            elif home_team_a == key:
                val[1] += 1
                print(f'{home_team_a} falls to {val[0]}-{val[1]}')
                
        for division,team in teams_by_division.items():
            if home_team_a in teams_by_division[division] and away_team_a in teams_by_division[division]:
                division_records[home_team_a][1] += 1
                division_records[away_team_a][0] += 1  
                
def playWeek(week):
    for i in games_by_week[week]:
        global current_game
        current_game = i
        playGame(current_game[0],current_game[1])
        
def playSeason():
    for i in games_by_week:
        playWeek(i)


# In[5]:


playSeason()


# In[6]:



# going through the teams that won their division taking into account the division record tiebreaker #
# also initializing a dictionary consisting of the top seven teams from each conference #

for i in division_winners:
    most_wins = 0
    winner = ''
    for team in teams:
        if team in teams_by_division[i] and records_by_team[team][0] > most_wins:
            most_wins = records_by_team[team][0]
            winner = team
        elif team in teams_by_division[i] and records_by_team[team][0] == most_wins:
            if division_records[team][0] > division_records[winner][0]:
                winner = team
    division_winners[i] = winner
for conference in conferences:
    for division in division_winners:
        if division[0:3] == conference:
            conferences[conference].append(division_winners[division])
for conference in conferences:
    while len(conferences[conference]) < 7:
        most_wins = 0
        wildcard = ''
        for division in teams_by_division:
            if division[0:3] == conference:
                for team in teams_by_division[division]:
                    if records_by_team[team][0] > most_wins and team not in conferences[conference]:
                        most_wins = records_by_team[team][0]
                        wildcard = team
        conferences[conference].append(wildcard)
conferences


# In[7]:



# seeding each team for both conferences #

nfc_seeding = {}
for i in range(1,8):
    nfc_seeding[i] = ''
    
afc_seeding = {}
for i in range(1,8):
    afc_seeding[i] = ''

teams_used = []
for i in range(4):
    current_best = max(list(records_by_team[team][0] for team in conferences['AFC'][:4] if team not in teams_used))
    for team in conferences['AFC'][:4]:
        if records_by_team[team][0] == current_best and team not in teams_used:
            best_team = team
    if best_team not in afc_seeding.values():
        afc_seeding[min(list(i for i in afc_seeding.keys() if afc_seeding[i] == ''))] = best_team
        teams_used.append(best_team)
for team in conferences['AFC'][4:]:
     if team not in teams_used:   
        afc_seeding[min(list(i for i in afc_seeding.keys() if afc_seeding[i] == ''))] = team
        
for i in range(4):
    current_best = max(list(records_by_team[team][0] for team in conferences['NFC'][:4] if team not in teams_used))
    for team in conferences['NFC'][:4]:
        if records_by_team[team][0] == current_best and team not in teams_used:
            best_team = team
    if best_team not in nfc_seeding.values():
        nfc_seeding[min(list(i for i in nfc_seeding.keys() if nfc_seeding[i] == ''))] = best_team
        teams_used.append(best_team)
for team in conferences['NFC'][4:]:
    if team not in teams_used:   
        nfc_seeding[min(list(i for i in nfc_seeding.keys() if nfc_seeding[i] == ''))] = team
afc_seeds = dict((val,key) for key,val in afc_seeding.items())
nfc_seeds = dict((val,key) for key,val in nfc_seeding.items())
afc_seeds.update(nfc_seeds)
all_seeds = afc_seeds
global teams_lost
teams_lost = []


# In[8]:


nfc_seeding


# In[9]:


afc_seeding


# In[10]:


def playPostseasonGame(high_seed,low_seed):
    quarters = 8
    global home_score
    global away_score
    home_score = 0
    away_score = 0
    
    global home_name
    global away_name
    global home_team_a
    global away_team_a
    global box_score_home
    global box_score_away
    box_score_home = []
    box_score_away = []
    
    home_name = find_name(high_seed,low_seed)[0]
    away_name = find_name(high_seed,low_seed)[1]
    home_team_a = find_abb(home_name,away_name)[0]
    away_team_a = find_abb(home_name,away_name)[1]
    
    
    print(f'#{all_seeds[low_seed]} {away_name} @ #{all_seeds[high_seed]} {home_name}')
    
    while quarters > 0:
        
        score = roll()
        box_score_home.append(score)
        home_score += score
        if home_score > away_score:
            print(f"{home_score}-{away_score} {home_team_a}")
        elif away_score > home_score:
            print(f"{home_score}-{away_score} {away_team_a}")
        else:
            print(f"{home_score}-{away_score}")
        quarters -= 1
            
                
        score = roll()
        box_score_away.append(score)
        away_score += score
        if home_score > away_score:
            print(f"{home_score}-{away_score} {home_team_a}")
        elif away_score > home_score:
            print(f"{home_score}-{away_score} {away_team_a}")
        else:
            print(f"{home_score}-{away_score}")
        quarters -= 1
        if quarters == 4:
            print("Halftime.")
                
    if home_score == away_score:
        print("Overtime!\n")
        
        OTroll1 = roll()
        OTroll2 = roll()
        while OTroll1 == OTroll2:
            OTroll1 = roll()
            OTroll2 = roll()
        if OTroll2 >= 7:
            home_score += 6
            box_score_home.append(6)
            box_score_away.append(0)
        elif OTroll1 >= 7:
            away_score += 6
            box_score_away.append(6)
            box_score_home.append(0)
        elif OTroll2 == 3 and OTroll1 < 7:
            home_score += 3
            box_score_home.append(3)
            box_score_away.append(0)
        elif OTroll2 < 7 and OTroll1 == 3:
            away_score += 3
            box_score_away.append(3)
            box_score_home.append(0)
    
    
    if home_score > away_score:
        teams_lost.append(away_team_a)
        print(f"{home_name} win {home_score}-{away_score}")
        postseason_box_score(box_score_home,box_score_away)
        print("\n")
    elif away_score > home_score:
        teams_lost.append(home_team_a)
        print(f"{away_name} win {away_score}-{home_score}")
        postseason_box_score(box_score_home,box_score_away)
        print("\n")
        
    
        
def postseason_box_score(box_score1,box_score2):
    print("Box Score: ")
    if len(box_score_home) == 4:
        print("     1   2   3   4")
        print(f"{home_team_a}: {box_score_home[0]}   {box_score_home[1]}   {box_score_home[2]}   {box_score_home[3]}")
        print(f"{away_team_a}: {box_score_away[0]}   {box_score_away[1]}   {box_score_away[2]}   {box_score_away[3]}")
    elif len(box_score_home) > 4:
        print("     1   2   3   4   OT")
        print(f"{home_team_a}: {box_score_home[0]}   {box_score_home[1]}   {box_score_home[2]}   {box_score_home[3]}   {box_score_home[4]}")
        print(f"{away_team_a}: {box_score_away[0]}   {box_score_away[1]}   {box_score_away[2]}   {box_score_away[3]}   {box_score_away[4]}")
    if home_score > away_score and len(teams_lost) <= 12:
        print(f"#{all_seeds[home_team_a]} {home_name} move on!")
    elif away_score > home_score and len(teams_lost) <= 12:
        print(f"#{all_seeds[away_team_a]} {away_name} move on!")
    elif home_score > away_score and len(teams_lost) > 12:
        print(f"#{all_seeds[home_team_a]} {home_name} have won the Super Bowl!")
    elif away_score > home_score and len(teams_lost) > 12:
        print(f"#{all_seeds[away_team_a]} {away_name} have won the Super Bowl!")
        
        
def check_seed():
    nfc = [all_seeds[i] for i in conferences['NFC'] if i not in teams_lost] 
    afc = [all_seeds[j] for j in conferences['AFC'] if j not in teams_lost]
    nfc.sort()
    afc.sort()
    return nfc,afc

def playRound():
    if len(teams_lost) == 0:
        playPostseasonGame(nfc_seeding[2],nfc_seeding[7])
        playPostseasonGame(afc_seeding[2],afc_seeding[7])
        playPostseasonGame(nfc_seeding[3],nfc_seeding[6])
        playPostseasonGame(afc_seeding[3],afc_seeding[6])
        playPostseasonGame(nfc_seeding[4],nfc_seeding[5])
        playPostseasonGame(afc_seeding[4],afc_seeding[5])
    elif len(teams_lost) == 6:
        nfc = check_seed()[0]
        afc = check_seed()[1]
        playPostseasonGame(nfc_seeding[1],nfc_seeding[max(check_seed()[0])])
        playPostseasonGame(afc_seeding[1],afc_seeding[max(check_seed()[1])])
        playPostseasonGame(nfc_seeding[nfc[1]],nfc_seeding[nfc[2]])
        playPostseasonGame(afc_seeding[afc[1]],afc_seeding[afc[2]])
    elif len(teams_lost) == 10:
        playPostseasonGame(nfc_seeding[min(check_seed()[0])],nfc_seeding[max(check_seed()[0])])
        playPostseasonGame(afc_seeding[min(check_seed()[1])],afc_seeding[max(check_seed()[1])])
    elif len(teams_lost) == 12:
        playPostseasonGame(nfc_seeding[check_seed()[0][0]],afc_seeding[check_seed()[1][0]])
        
        
def playPostseason():
    for i in range(4):
        playRound()


# In[11]:


playPostseason()


# In[11]:





# In[ ]:





# In[ ]:




