var config = require('../config')
var express = require('express')
var router = express.Router()
var mongodb = require('mongodb')
var mongoClient = mongodb.Client
var mongoClientURI = config.MONGO_URI_CLIENTS_ID

router.get('/', function(req, res) {
    //MongoDB Connecting(Client Token DB)
    mongoClient.connect(mongoClientURI, function(err, db) {
        if (err) {
            console.log('[Message] MongoDB Connect Error\n[Message] Error Code : ' + err)
        } else {
            console.log('[Message] MongoDB Connect!')
            // TODO..
            db.collection('user_token').find({}).toArray(function(err, result) {
                if (err) {
                    console.log('[Message] MongoDB Find Error\n[Message] Error Code : ' + err)
                } else {
                    res.send(result)
                }
                
                db.close()
            })
        }
    })
})

router.post('/', function(req, res) {
    var requestTokenValue = req.body
    
    mongoClient.connect(mongoClientURI, function(err, db) {
        if (err) {
            console.log('[Message] MongoDB Connect Error\n[Message] Error Code : ' + err)
        } else {
            console.log('[Message] MongoDB Connect!')
            // TODO..
            var findQuery = {token_value : requestTokenValue}
            db.collection('user_token').findOne(findQuery, function(err, doc) {
                if (err) {
                    console.log('[Message] MongoDB Find Error\n[Message] Error Code : ' + err)
                } else {
                    if (doc == null) {
                        // 입력된 Token 데이터가 DB에 저장되어있지 않음 ==> 새로 등록
                        var insertUserToken = {token_value : requestTokenValue}
                        db.collection('user_token').insertOne(insertUserToken, function(err, result) {
                            if (err) {
                                console.log('[Message] MongoDB User Insert Error\n[Message] Error Code : ' + err)
                            } else {
                                console.log("[Message] New User Token Insert Success")
                                res.send(result.insertedCount)
                            }
                            db.close()
                        })
                    }
                }
            })
        }
    })
})

router.delete('/:token', function(req, res) {
    var requestTokenValue = req.params.token

    mongoClient.connect(mongoClientURI, function(err, db) {
        if (err) {
            console.log('[Message] MongoDB Connect Error\n[Message] Error Code : ' + err)
        } else {
            console.log('[Message] MongoDB Connect!')
            // TODO..
            var removeToken = {token_value : requestTokenValue}
            db.collection('user_token').deleteOne(removeToken, function(err, result) {
                if (err) {
                    console.log('[Message] MongoDB Delete Error\n[Message] Error Code : ' + err)
                } else {
                    console.log('[Message] Delete Successed!\n[Message] ' + result.result.n + ' document Deleted');
                }

                db.close()
            })
        }
    })
})


module.exports = router