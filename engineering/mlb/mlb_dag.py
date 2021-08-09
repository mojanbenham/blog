# import necessary libraries
import requests
import datetime

from get_team import get_team
from get_players import get_players
from get_games import get_games

season = datetime.datetime.now().year

# call functions 
team_id = get_team("Toronto Blue Jays", season, requests)
left_handed_players = get_players(team_id, requests)
home_games = get_games(team_id, season, requests)

#print(home_games)

with open('../../../Desktop/results.txt', 'w') as f:
    f.write("Left-handed players:\n--------------------\n")

    for player in left_handed_players:
        f.write(player['name_display_first_last'] + "\n")
    
    f.write("\n\nOpponents in first five home games:\n--------------------\n")
    for game in home_games:
        f.write(game + "\n")