import datetime
from datetime import datetime
import pandas
import math

table = pandas.read_csv("db/instance_recommendations.csv")

def process(input):
    
    recommendations = []
    features = extract_features(input)
    for recommendation in table.iterrows():
        #TODO: Add disease and gender matching
        if _satisfies("bp systolic", features, recommendation) and \
                _satisfies("bp diastolic", features, recommendation) and \
                _satisfies("heartbeat", features, recommendation) and \
                _satisfies("sleep", features, recommendation) and \
                _satisfies("activity day", features, recommendation) and \
                _satisfies("activity week", features, recommendation) and \
                _satisfies("step", features, recommendation) and \
                _satisfies("age", features, recommendation) and \
                _satisfies("bmi", features, recommendation):
            recommendations = _append_recommendation(recommendation, 
                                                     recommendations)
                                                     
    return recommendations

            
def _satisfies(feature_name, features, recommendation_row):
    """ Checks if a certain feature in the features vector satisfies the 
    recommendation row """
    
    min_key = feature_name + " min"
    max_key = feature_name + " max"
    min_val = recommendation_row[1][min_key]
    max_val = recommendation_row[1][max_key]
    feature = features.get(feature_name)

    if not feature or (feature is None):
        return True
    if min_val and feature < min_val: 
        return False
    if max_val and feature > max_val: 
        return False
    return True

def _get_slug(str):
    """ Returns string with spaces replaced by underscores """
    return str.replace(" ", "_")
    
def _append_recommendation(recommendation_row, recommendations):
    recommendation = {
        'id': recommendation_row[1]['ID'],
        'condition': recommendation_row[1]['recommendation'],
        'url': recommendation_row[1]['source'],
        'severity': int(recommendation_row[1]['severity']),
        'direction': recommendation_row[1]['direction'],
    }
    if math.isnan(float(recommendation['url'])):
        recommendation['url'] = ''
    recommendations = recommendations + [recommendation]
    return recommendations
    

def extract_features(input):
    """ Returns a feature vector with the same fields as the recommendation 
    table so that they can be compared """
    # TODO: sort before selecting the last item in list
    
    disease = gender = bmi = age = step = activity_week = activity_day \
            = sleep = heartbeat = bp_diastolic = bp_systolic \
            = weight = height = None
    
    if "userinfo" in input:
        
        userinfo = input["userinfo"]
        
        if "age" in userinfo:
            age = userinfo["age"]
        if "height" in userinfo:
            height = userinfo["height"]
        if "gender" in userinfo:
            gender = userinfo["gender"]
        if "weight" in userinfo:
            if "weight" in userinfo:
                weights = userinfo["weight"]
                prev_date = None
                for item in weights:
                    if "date" in item and "value" in item:
                        if prev_date is None or item["date"] > prev_date:
                            weight = item["value"]
                            prev_date = item["date"]
        
        if height and weight: bmi = height / weight
        
        disease = []
        if "hypertension" in userinfo and userinfo["hypertension"]: 
            disease = disease + ["hypertension"]
        if "diabetes" in userinfo and userinfo["diabetes"]:
            disease = disease + ["diabetes"]
        if "insomnia" in userinfo and userinfo["insomnia"]:
            disease = disease + ["insomnia"]
        if "cardio" in userinfo and userinfo["cardio"]:
            disease = disease + ["cardio"]
            
    if "bloodPressures" in input:
        bloodPressures = input["bloodPressures"]
        prev_date = None
        for item in bloodPressures:
            if "date" in item and "systolic" in item and "diastolic" in item:
                if prev_date is None or _datetime(item["date"]) > prev_date:
                    bp_systolic = item["systolic"]
                    bp_diastolic = item["diastolic"]
                    prev_date = _datetime(item["date"])


    if "heartBeats" in input:
        heartBeats = input["heartBeats"]
        prev_date = None
        for item in heartBeats:
            if "date" in item and "count" in item:
                if prev_date is None or _datetime(item["date"]) > prev_date:
                    heartbeat = item["count"]
                    prev_date = _datetime(item["date"])
                    
    if "sleep" in input:
        sleeps = input["sleep"]
        prev_date = None
        for item in sleeps:
            if "date" in item and "minutesAsleep" in item:
                if prev_date is None or _datetime(item["date"]) > prev_date:
                    sleep = item["minutesAsleep"]
                    prev_date = _datetime(item["date"])
    
    if "activities" in input:
        activities = input["activities"]
        prev_date = None
        for item in activities:
            if "date" in item and "duration" in item:
                if prev_date is None or _datetime(item["date"]) > prev_date:
                    activity_day = item["duration"]
                    prev_date = _datetime(item["date"])
        
        # filter the week
#         week_ago = datetime.today() - datetime.timedelta(7)
#         activity_week = sum([activity["duration"] for activity in \
#                 input["activities"] if _datetime(activity["date"]) > week_ago])
    
    features = {
        "bp systolic": bp_systolic,
        "bp diastolic": bp_diastolic,
        "heartbeat": heartbeat,
        "sleep": sleep,
        "activity day": activity_day,
        "activity week": activity_week,
        "step": step,
        "age": age,
        "bmi": bmi,
        "gender": gender,
        "disease": disease
    }
    return features
    
def _datetime(str):
    return datetime.strptime(str, "%Y-%m-%d")