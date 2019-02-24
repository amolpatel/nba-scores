import requests, datetime, pytz
from django.shortcuts import render

def games(request):
    date = datetime.datetime.now(pytz.timezone('America/New_York')).strftime('%Y%m%d')
    url = 'http://data.nba.net/10s/prod/v1/' + date + '/scoreboard.json'
    r = requests.get(url).json()
    num_games = r['numGames']
    games_info = []

    for x in range(num_games):
        curr = r['games'][x]

        curr_dict = {
            'home' : curr['hTeam'],
            'away' : curr['vTeam'],
            'status': curr['statusNum'],
            'startTime': curr['startTimeEastern'],
            'period': curr['period'],
            'clock': curr['clock']
        }
        games_info.append(curr_dict)

    context = {
        'games_info' : games_info
    }

    return render(request, 'games/games.html', context)