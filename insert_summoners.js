use lol
db.createCollection('summoners')
db.summoners.insert({"id":"CSYRI0W26eLnFzUI5cUknIGW0sFpheB-ZC5b77S4sxSUseo","accountId":"lWGFL-ea2GTvyOXk8-t8dyLg9o2ftJ084cQm7LIgcgjG_A","puuid":"MPUePAZ1PhXbStThwRPKEm0XJs7ZwGUU-_ZbVs7_jou34zBhopqxVW5xG5ayeZeui8baY_pCKvu_dQ","name":"DyngleFrytz","profileIconId":4027,"revisionDate":1598115618000,"summonerLevel":47})
db.summoners.insert({"id":"Dufji1mQ5pz7Z-pKSZ0s37mMr144QHXUvSy3AAH-DlmzifU","accountId":"tgoAA-B-VLOtHvmjeEwxMrAXZeBQj4kWjTY3m53PtXwmEg","puuid":"4Hi8D3PdVLRFpDHRtoQqDGLIFPebe4-XL9PAOWvH03WHfAjaHyElCJe_SJS9o5oIV8S0wqgMJFYWDg","name":"chaisea","profileIconId":4568,"revisionDate":1598295901000,"summonerLevel":236})
db.summoners.insert({"id":"m-_75Kwa16i68lSfsIYXBi3BkUAaVKqb5JpJ0U_lFtr5K3w","accountId":"AaeIBeSm6RM6QUoVMWb0Ioa-1VOHGT4_h-QXoUA8YebiRQ","puuid":"bnBQYRAtS67pv3pPpJ8tFrgOkPgFBM0Q6MepcvvaGfhULFLq716E0HIWV73dnVYLQds8JNGOP4tCuw","name":"Phenway","profileIconId":4279,"revisionDate":1597974087000,"summonerLevel":146})

db.summoners.find({type:'accountId'})

db.summoners.find({}, {accountId:1, _id:0})
