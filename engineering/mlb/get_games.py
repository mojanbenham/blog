def get_games(team_id, season, requests):
    # get player data from API
    response = requests.get(f"https://lookup-service-prod.mlb.com/json/named.mlb_broadcast_info.bam?sort_by='game_time_et_asc'&season='{season}'")
    broadcasts = response.json()['mlb_broadcast_info']['queryResults']['row']

    # filter to team-specified games
    team_broadcasts = list(x for x in broadcasts if x['home_team_id'] == team_id)

    games = []
    for i in range(10):
        games.append(team_broadcasts[i]['away_team_full'])
    
    return(set(games))
