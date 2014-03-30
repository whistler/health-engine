There is a single API point with the following URL:

POST http://health-engine.herokuapp.com/

TODO[Huang]: Please describe the inputs and outputs for the engine

#Input:

Content-Type: application/json
{
    "userinfo": {
        "age": 45,
        "gender": "male",   //not required
        "height": 168,    //not required
        "weight": [
            {
                "value": 65.3,
                "date": "2012-04-24"
            },
            {
                "value": 65.3,
                "date": "2012-04-17"
            },
            {
                "value": 65.3,
                "date": "2012-03-24"
            }
    	],                //not required
        "hypertension" : true,    //not required
        "diabetes" : true,    //not required
        "insomnia" : true,    //not required
        "cardio" : true    //not required
    },
    "activities": [
        {
            "duration": 7.3,
            "date": "2012-04-24",
        },
        {
            "duration": 140,
            "date": "2012-04-17",
        },
        {
            "duration": 1430,
            "date": "2012-03-24",
        }
    ],
    "sleep": [
        {
            "minutesAsleep": 453,
            "date": "2012-04-26"
        },
        {
            "minutesAsleep": 453,
            "date": "2012-04-25"
        },
        {
            "minutesAsleep": 453,
            "date": "2012-04-24"
        }
    ],
    "heartBeats": [
        {
            "count": 56,      
            "date": "2012-04-24",
        },
        {
            "count": 60,       
            "date": "2012-04-17",
        },
        {
            "count": 59,      
            "date": "2012-03-24"
        }
    ],
    "bloodPressures": [
        {
            "systolic": 100,         
            "diastolic": 71,
            "date": "2012-04-23"
        },
        {
            "systolic": 100,         
            "diastolic": 71,
            "date": "2012-04-22"   
        },
        {
            "systolic": 100,         
            "diastolic": 71,
            "date": "2012-04-21"
        }
    ]
}

#Output: 

Content-Type: application/json

[
    { 
        "id": 0, 
        "recommendation": "This is a recommendation.", 
        "url": "www.health.ca"
    }, 
    { 
        "id": 1, 
        "recommendation": "This is another recommendation.",
        "url": "www.carethy.com" 
    }
]
