var config = require('../config')
var express = require('express')
var router = express.Router()
var dbConnector = require('../db/MealDatabase')

router.get('/:date', function(req, res, next) {
    var requestDateValue = req.params.date

    dbConnector.getPNUMealDataForDay(requestDateValue, function(result) {
        res.send(result)
    })
})

module.exports = router