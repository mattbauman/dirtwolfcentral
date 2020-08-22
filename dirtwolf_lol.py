import requests
import json
from time import time, ctime

summoners_url = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'

champions_url  = 'http://ddragon.leagueoflegends.com/cdn/10.16.1/data/en_US/champion.json'
champions_request = requests.get(champions_url)
champions_dict = json.loads(champions_request.text)



summoners = {'Phenway','dynglefrytz','chaisea'}

api_key = 'RGAPI-8569bd53-03ea-47e5-9777-164291a3f3ff'
headers = {'X-Riot-Token': api_key}

for summoner in summoners:
    summoner_request = requests.get(summoners_url+summoner, headers = headers)
    summoner_dict = json.loads(summoner_request.text)
    print(summoner_dict['name'], ' recent match history: ')

    #matchlists
    matchlists_request = requests.get('https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/'+summoner_dict['accountId'], headers = headers)
    matchlists_dict = json.loads(matchlists_request.text)

    for i, match in enumerate(matchlists_dict['matches']):
        if i < 5:
            for champion in champions_dict['data']:
                if str(match['champion']) == champions_dict['data'][champion]['key']:
                    match_champion = champion
            match_time = ctime(int(str(match['timestamp'])[:10]))
            match_request = requests.get('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(match['gameId']), headers = headers)
            match_dict = json.loads(match_request.text)
            print(match_champion, ',', match_time, ',', match_dict['gameMode'], ',', match_dict['gameType'])

    print()
