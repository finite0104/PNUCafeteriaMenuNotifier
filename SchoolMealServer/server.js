var express = require('express')
var bodyParser = require('body-parser')
var config = require('./config')

var app = express()

//Request Processing
app.use(bodyParser.urlencoded({extended : true}))
app.use(bodyParser.json())
app.use(function (req, res) {
    //요청 허용 URL 설정
    res.header('Access-Control-Allow-Origin', '*')
    //요청 허용 Method 설정
    res.header('Access-Control-Allow-Methods', 'GET, POST, DELETE')
    //요청 허용 Header 타입 설정
    res.header('Access-Control-Allow-Headers', 'content-type')
})

//API Connect
var FCMClientAPI = require('./api/FCMClient')
app.use('/client', FCMClientAPI)

var MealDataAPI = require('./api/MealData')
app.use('/meal', MealDataAPI)

//Create Server
var port = config.PORT
app.listen(port, '0.0.0.0', function() {
    console.log('[Message] Server Start - Listening Port : ' + port)
})