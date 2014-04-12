There is a single API point with the following URL:

POST http://health-engine.herokuapp.com/

#Input:

    Content-Type: application/json

    {
        "userinfo": {
            "age": 45,
            "gender": "male", // optional "male" or "female"
            "height": 168, // optional in cms
            "weight": [ // optional
                {
                    "value": 65.3, // in kgs
                    "date": "2012-04-24"
                }, {
                    "value": 65.3,
                    "date": "2012-04-17"
                }, {
                    "value": 65.3,
                    "date": "2012-03-24"
                }
            ],
            "hypertension": true, // optional patient has hyper tension
            "diabetes": true, // optional patient has diabetes
            "insomnia": true, // optional patient has insomnia
            "cardio": true // optional patient heart disease
        },
        "activities": [{
            "duration": 7.3, // in minutes
            "date": "2012-04-24",
        }, {
            "duration": 140,
            "date": "2012-04-17",
        }, {
            "duration": 1430,
            "date": "2012-03-24",
        }],
        "sleep": [{
            "minutesAsleep": 453,
            "date": "2012-04-26"
        }, {
            "minutesAsleep": 453,
            "date": "2012-04-25"
        }, {
            "minutesAsleep": 453,
            "date": "2012-04-24"
        }],
        "heartBeats": [{
            "pulse": 56, // heart beats per minute
            "date": "2012-04-24",
        }, {
            "pulse": 60,
            "date": "2012-04-17",
        }, {
            "pulse": 59,
            "date": "2012-03-24"
        }],
        "bloodPressures": [{
            "systolic": 100, // mm/Hg
            "diastolic": 71,
            "date": "2012-04-23"
        }, {
            "systolic": 100,
            "diastolic": 71,
            "date": "2012-04-22"
        }, {
            "systolic": 100,
            "diastolic": 71,
            "date": "2012-04-21"
        }]
    }


#Output: 

Content-Type: application/json

    [
        { 
            "id": 0, 
            "recommendation": "This is a recommendation.", 
            "url": "www.health.ca",
            "severity": 1 // 1-3, with 1 being lowest and 3 being highest
        }, 
        { 
            "id": 1, 
            "recommendation": "This is another recommendation.",
            "url": "www.carethy.com",
            "severity": 1
        }
    ]
    
#Testing

To test out this endpoint with curl run:

    curl -i -H "Content-Type: application/json" -X POST -d @input.json http://health-engine.herokuapp.com/
