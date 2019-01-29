var config = require('../config')
var express = require('express')
var router = express.Router()
var dbConnector = require('../db/FCMDatabase')

router.get('/getClientTokens', function(req, res) {
    dbConnector.getClientTokens(function(result) {
        res.send(result)
    })
})

router.post('/setClientToken', function(req, res) {
    var requestTokenValue = req.body
    
    dbConnector.insertClientToken(requestTokenValue, function(result) {
        res.send(result)
    })
})

router.delete('/deleteToken/:token', function(req, res) {
    var requestTokenValue = req.params.token

    dbConnector.deleteClientToken(requestTokenValue, function(result) {
        res.send(result)
    })
})

module.exports = router