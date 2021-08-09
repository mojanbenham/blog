def get_players(team_id, requests):
    # get player data from API
    response = requests.get(f"https://lookup-service-prod.mlb.com/json/named.roster_40.bam?team_id='{team_id}'")
    players = response.json()['roster_40']['queryResults']['row']

    # filter to left-handed batters
    return list(x for x in players if x['bats'] == 'L')
