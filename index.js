const app = require('express')();
const https = require('https');
const fs = require('fs');

app.set('view engine', 'pug');
app.set('views','./views');

//GET home route
//app.get('/', (req, res) {
//    res.send('Welcome to Dirtwolf Central');
//});

app.get('/', function(req, res){
   res.render('index.pug');
});

var routes = require('./routes.js');
app.use('/routes', routes);

var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/my_db');

// we will pass our 'app' to 'https' server
https.createServer({
    key: fs.readFileSync('/opt/bitnami/letsencrypt/certificates/dirtwolfcentral.com.key'),
    cert: fs.readFileSync('/opt/bitnami/letsencrypt/certificates/dirtwolfcentral.com.crt')
//    passphrase: 'YOUR PASSPHRASE HERE'
}, app)
.listen(3000);
