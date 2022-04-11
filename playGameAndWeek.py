import random
import bs4
import requests
from nfl_reader import teams,find_name,team_names
from writeSchedule import games_by_week


# dice rolling function determining score per quarter/OT #

def roll():
    score = 0
    for i in range(1):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        if dice1 == 6 and dice2 == 6:
            score += 14
            extra = random.randint(1,6)
            if extra == 6:
                score += 7
            elif extra == 3:
                score += 3
        elif dice1 == 1 and dice2 == 1:
            score += 14
            extra = random.randint(1,6)
            if extra == 1:
                score += 7
            elif extra == 3:
                score += 3
        elif dice1 == 3 and dice2 == 3:
            score += 6
            extra = random.randint(1,6)
            if extra == 3:
                score += 3
        elif dice1 == 2 and dice2 == 2:
            score += 0
        elif dice1 == 4 and dice2 == 4:
            score += 0
        elif dice1 == 5 and dice2 == 5:
            score += 0
        elif dice1 == 6 and dice2 == 1 or dice2 == 1 and dice1 == 6:
            score += 14
        elif dice1 == 1 and dice2 == 3 or dice2 == 1 and dice1 == 3:
            score += 10
        elif dice1 == 6 and dice2 == 3 or dice2 == 6 and dice1 == 3:
            score += 10
        elif dice1 == 6 and dice2 == 2 or dice2 == 6 and dice1 == 2:
            score += 7
        elif dice1 == 6 and dice2 == 4 or dice2 == 6 and dice1 == 4:
            score += 7
        elif dice1 == 6 and dice2 == 5 or dice2 == 6 and dice2 == 5:
            score += 7
        elif dice1 == 3 and dice2 == 2 or dice2 == 3 and dice1 == 3:
            score += 3
        elif dice1 == 3 and dice2 == 4 or dice2 == 3 and dice1 == 4:
            score += 3
        elif dice1 == 3 and dice2 == 5 or dice2 == 3 and dice1 == 5:
            score += 3
        elif dice1 == 1 and dice2 == 2 or dice2 == 1 and dice1 == 2:
            score += 7
        elif dice1 == 1 and dice2 == 4 or dice2 == 1 and dice2 == 4:
            score += 7
        elif dice1 == 1 and dice2 == 5 or dice2 == 1 and dice1 == 5:
            score += 7
        else:
            score += 0
        return score
    


    


# Full game function



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
    
    
    
    home_team_a = find_abb(home_team,away_team)[0]
    away_team_a = find_abb(home_team,away_team)[1]
    print(f"{away_team} @ {home_team}")


    while quarters > 0:
        
        #home_roll = input("Press 'r' to roll: ").lower()
        #while home_roll != 'r':
            #home_roll = input("Press 'r' to roll: ").lower()
            
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
            
                
        
        #away_roll = input("Press 'r' to roll: ").lower()
        #while away_roll != 'r':
            #away_roll = input("Press 'r' to roll: ").lower()
       
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
        playOT = input("Press 'r' to play overtime: ").lower()
        while playOT != 'r':
            playOT = input("Press 'r' to play overtime: ")
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
    
    
   
    if home_score > away_score:
        for key,val in records_by_team.items():
            if home_team == key:
                val[0] += 1
                print(f'{home_team} improves to {val[0]}-{val[1]}')
            elif away_team == key:
                val[1] += 1
                print(f'{away_team} falls to {val[0]}-{val[1]}')
                print("\n")
    else:
        for key,val in records_by_team.items():
            if away_team == key:
                val[0] += 1
                print(f'{away_team} improves to {val[0]}-{val[1]}')
            elif home_team == key:
                val[1] += 1
                print(f'{home_team} falls to {val[0]}-{val[1]}')
                print("\n")

        

        
def print_box_score(box_score1,box_score2):
    print("Box Score: ")
    if len(box_score_home) == 4:
        print("     1   2   3   4")
        print(f"{away_team_a}: {box_score_home[0]}   {box_score_home[1]}   {box_score_home[2]}   {box_score_home[3]}")
        print(f"{home_team_a}: {box_score_away[0]}   {box_score_away[1]}   {box_score_away[2]}   {box_score_away[3]}")
    elif len(box_score_home) > 4:
        print("     1   2   3   4   OT")
        print(f"{away_team_a}: {box_score_home[0]}   {box_score_home[1]}   {box_score_home[2]}   {box_score_home[3]}   {box_score_home[4]}")
        print(f"{home_team_a}: {box_score_away[0]}   {box_score_away[1]}   {box_score_away[2]}   {box_score_away[3]}   {box_score_away[4]}")


global current_game
global games_by_week

def playWeek():
    week = int(input("Which week would you like to play?: "))
    for i in games_by_week[week]:
        
        current_game = i
        play_game = input(f'Play {current_game[1]} @ {current_game[0]}?')
        if play_game == 'y':
            playGame(current_game[0],current_game[1])


def find_abb(home_team,away_team):
    for key,val in team_names.items():
        if home_team == key:
            home_a = val
        elif away_team == key:
            away_a = val
    return[home_a, away_a]
