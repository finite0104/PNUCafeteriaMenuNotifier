var mongodb = require('mongodb')
var config = require('../config')
var mongoClient = mongodb.Client
var mongoClientURI = config.MONGO_URI_CLIENTS_ID

module.exports.getClientTokens = function(callback) {
    mongoClient.connect(mongoClientURI, function(err, database) {
        if (err) {
            console.log('[Message] MongoDB Connect Error\n[Message] Error Code : ' + err)
            callback(false)
        } else {
            console.log('[Message] MongoDB Connect!')
            // TODO..
            database.db().collection('user_token').find({}).toArray(function(err, result) {
                if (err) {
                    console.log('[Message] MongoDB Find Error\n[Message] Error Code : ' + err)
                    callback(false)
                } else {
                    callback(result)
                }
                
                db.close()
            })
        }
    })
}

module.exports.insertClientToken = function(token, callback) {
    mongoClient.connect(mongoClientURI, function(err, database) {
        if (err) {
            console.log('[Message] MongoDB Connect Error\n[Message] Error Code : ' + err)
            callback(false)
        } else {
            console.log('[Message] MongoDB Connect!')
            // TODO..
            var tokenValue = {token_value : token}
            database.db().collection('user_token').findOne(tokenValue, function(err, doc) {
                if (err) {
                    console.log('[Message] MongoDB Find Error\n[Message] Error Code : ' + err)
                    callback(false)
                } else {
                    if (doc == null) {
                        // 입력된 Token 데이터가 DB에 저장되어있지 않음 ==> 새로 등록
                        db.collection('user_token').insertOne(tokenValue, function(err, result) {
                            if (err) {
                                console.log('[Message] MongoDB User Insert Error\n[Message] Error Code : ' + err)
                                callback(false)
                            } else {
                                console.log("[Message] New User Token Insert Success")
                                callback(true)
                            }

                            db.close()
                        })
                    }
                }
            })
        }
    })
}

module.exports.deleteClientToken = function(token, callback) {
    mongoClient.connect(mongoClientURI, function(err, database) {
        if (err) {
            console.log('[Message] MongoDB Connect Error\n[Message] Error Code : ' + err)
            callback(false)
        } else {
            console.log('[Message] MongoDB Connect!')
            // TODO..
            var tokenValue = {token_value : token}
            database.collection('user_token').deleteOne(tokenValue, function(err, result) {
                if (err) {
                    console.log('[Message] MongoDB Delete Error\n[Message] Error Code : ' + err)
                    callback(false)
                } else {
                    console.log('[Message] Delete Successed!\n[Message] ' + result.result.n + ' document Deleted');
                    callback(true)
                }

                db.close()
            })
        }
    })
}