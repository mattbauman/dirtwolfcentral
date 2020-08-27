import pymongo

password = open('mongodb_lol_user.txt').read()
myclient = pymongo.MongoClient("mongodb://lol_user:"+password+"@localhost:27017/")
mydb = myclient["lol"]
mycol = mydb["summoners"]

#use lol
#db.summoners.find({}, {accountId:1, _id:0})
#mydoc = mycol.find("{}, {accountId:1, _id:0}")

mydoc = mycol.find()

for x in mydoc:
  print(x) 
