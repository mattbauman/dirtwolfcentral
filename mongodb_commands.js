mongo admin --username root --password Zw7VVcTSXbCK
use lol
db.createUser({user:'lol_user',pwd:'br15iyen',roles:[{role:'readWrite',db:'lol'}]})
mongo --username lol_user --password br15iyen
