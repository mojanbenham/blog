def get_team(team_name, season, requests):
    # define API parameters
    parameters = {
        "sports_code": "mlb",
        "season": season
    }

    # get team data from API
    response = requests.get("http://lookup-service-prod.mlb.com/json/named.team_all_season.bam", params=parameters)
    print(f"MLB lookup service API response code: {response.status_code}")
    teams = response.json()['team_all_season']['queryResults']['row']

    # filter to find desired team id
    team = list(x['team_id'] for x in teams if x['name_display_full'] == team_name)
    print(f"The team id for the {team_name} is {team[0]}.")
    return team[0]
