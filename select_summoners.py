import pymongo
import requests
import json

#mongodb
password = open('mongodb_lol_user.txt').read()
password = password.replace('\n','')
client = pymongo.MongoClient("mongodb://lol_user:"+password+"@localhost:27017/")
database = client["lol"]
summoners = database["summoners"]
matchlists = database["matchlists"]
query = summoners.find()


#riot games api
api_key = open('riot_games_api_key.txt').read()
api_key = api_key.replace('\n','')
headers = {'X-Riot-Token': api_key}



# loop summoners
for summoner_dict in query:
    print(summoner_dict['name'], summoner_dict['accountId'])
    #matchlists
    matchlists_request = requests.get('https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/'+summoner_dict['accountId'], headers = headers)
    if matchlists_request.status_code == 200:
        matchlists_dict = json.loads(matchlists_request.text)
        matchlists_dict['name'] = summoner_dict['name'] #add summoner name to matchlist dictionary
        try:
            matchlists_existing_query = { "name": matchlists_dict['name'] }
            matchlists.delete_many(matchlists_existing_query)
            print("old matchlist deleted")
        except:
            print("new matchlist")
        x = matchlists.insert_one(matchlists_dict)
        print(x)

