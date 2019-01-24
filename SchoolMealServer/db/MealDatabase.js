var mongodb = require('mongodb')
var config = require('../config')
var mongoClient = mongodb.Client
var mongoClientURI = config.MONGO_URI_MEAL_DATA

module.exports.getPNUMealData = function(callback) {
    mongoClient.connect(mongoClientURI, function(err, db) {
        if (err) {
            console.log('[Message] MongoDB Connect Error\n[Message] Error Code : ' + err)
            callback(false)
        } else {
            console.log('[Message] MongoDB Connect!')
            // TODO..
            db.collection('user_token').find({}).toArray(function(err, result) {
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