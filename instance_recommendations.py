import datetime
# import pandas


# table = pandas.read_csv("db/instance_recommendations.csv")

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
        
    if feature and min_val and feature < min_val: return False
    if feature and max_val and feature > max_val: return False
    return True

def _get_slug(str):
    """ Returns string with spaces replaced by underscores """
    return str.replace(" ", "_")
    
def _append_recommendation(recommendation_row, recommendations):
    recommendation = {
        'id': recommendation_row[1]['ID'],
        'recommendation': recommendation_row[1]['recommendation'],
        'source': recommendation_row[1]['source'],
        'severity': recommendation_row[1]['severity']
    }
    recommendations = recommendations + [recommendation]
    return recommendations
    

def extract_features(input):
    """ Returns a feature vector with the same fields as the recommendation 
    table so that they can be compared """
    # TODO: sort before selecting the last item in list
    
    disease = gender = bmi = age = step = activity_week = activity_day \
            = sleep = heartbeat = bp_diastolic = bp_systolic = None
    
    if input["userinfo"]:
        age = input["userinfo"]["age"]
        height = input["userinfo"]["height"]
        if input["userinfo"]["weight"]:
            weight = input["userinfo"]["weight"][-1]["value"]
        
        disease = []
        if input["userinfo"]["hypertension"]: 
            disease = disease + ["hypertension"]
        if input["userinfo"]["diabetes"]:
            disease = disease + ["diabetes"]
        if input["userinfo"]["insomnia"]:
            disease = disease + ["insomnia"]
        if input["userinfo"]["cardio"]:
            disease = disease + ["cardio"]
            
        if height and weight: bmi = height / weight
        gender = input["userinfo"]["gender"]
    
    if input["bloodPressures"]:
        bp_systolic = input["bloodPressures"][-1]["systolic"]
        bp_diastolic = input["bloodPressures"][-1]["diastolic"]
        
    if input["heartBeats"]:
        heartbeat = input["heartBeats"][-1]["pulse"]

    if input["sleep"]:
        sleep = input["sleep"][-1]["minutesAsleep"]
    
    if input["activities"]:
        activity_day = input["activities"][-1]["duration"]
        # filter the week
        week_ago = datetime.datetime.today() - datetime.timedelta(7)
        activity_week = sum([activity["duration"] for activity in \
                input["activities"] if _datetime(activity["date"]) > week_ago])
    
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
    return datetime.datetime.strptime(str, "%Y-%m-%d")