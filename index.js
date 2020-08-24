const app = require('express')();
const https = require('https');
const fs = require('fs');

app.set('view engine', 'pug');
app.set('views','./views');

//GET home route
app.get('/', (req, res) => {
    res.send('Welcome to Dirtwolf Central');
});

var routes = require('./routes.js');

//both index.js and routes.js should be in same directory
app.use('/routes', routes);

// we will pass our 'app' to 'https' server
https.createServer({
    key: fs.readFileSync('/opt/bitnami/letsencrypt/certificates/dirtwolfcentral.com.key'),
    cert: fs.readFileSync('/opt/bitnami/letsencrypt/certificates/dirtwolfcentral.com.crt')
//    passphrase: 'YOUR PASSPHRASE HERE'
}, app)
.listen(3000);
