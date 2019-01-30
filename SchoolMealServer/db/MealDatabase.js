var mongodb = require('mongodb')
var config = require('../config')
var mongoClient = mongodb.MongoClient
var mongoClientURI = config.MONGO_URI_MEAL_DATA

module.exports.getPNUMealDataForDay = function(day, callback) {
    mongoClient.connect(mongoClientURI, function(err, database) {
        if (err) {
            console.log('[Message] MongoDB Connect Error\n[Message] Error Code : ' + err)
            callback(false)
        } else {
            console.log('[Message] MongoDB Connect!')
            // TODO..
            database.db().collection(day).find({}).toArray(function(err, result) {
                if (err) {
                    console.log('[Message] MongoDB Find Error\n[Message] Error Code : ' + err)
                    callback(false)
                } else {
                    callback(result)
                }
                
                database.close()
            })
        }
    })
}