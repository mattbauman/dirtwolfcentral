import requests

summoners = {'Phenway','dynglefrytz','chaisea'}
summoners_url = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'

api_key = open('api_key.txt').read()
headers = {'X-Riot-Token': api_key}

for summoner in summoners:
  summoner_request = requests.get(summoners_url+summoner, headers = headers)
  print(summoner_request.status_code)
  if summoner_request.status_code == 200:
    print('writing summoners_by_name',summoner)
    out = open('summoners_by_name_'+summoner+'.json','w')
    out.write(summoner_request.text)
  else:
    print(summoner, 'failed')
