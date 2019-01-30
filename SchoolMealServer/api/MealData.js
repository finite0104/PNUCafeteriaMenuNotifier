var config = require('../config')
var express = require('express')
var router = express.Router()
var dbConnector = require('../db/MealDatabase')

router.get('/:date', function(req, res, next) {
    //var now = new Date(Date.now())
    //var dateString = getDateString(now)
    var dateString = req.params.date

    dbConnector.getPNUMealDataForDay(dateString, function(result) {
        res.send(result)
    })
})

function getDateString(now) {
    var date  = now.getDate()
    var month = now.getMonth() + 1
    var year  = now.getFullYear()

    return '' + year + '.' + (month <= 9 ? '0' + month : month) + '.' + (date <= 9 ? '0' + date : date)
}

module.exports = router