""" Takes inputs and extracts features that are useful for recommendations"""

from features import Features

def preprocess(inputs):
    
    # TODO: find the following values from inputs
    bp_systolic_min = None
    bp_systolic_max = None
    bp_diastolic_min = None
    bp_diastolic_max = None
    heartbeat_min = None
    heartbeat_max = None
    sleep_min = None
    sleep_max = None
    activity_min = None
    activity_max = None
    age_min = None
    age_max = None
    
    if inputs["age"]>=19 and inputs["age"]<=64:
        age_min=19
        age_max=64
    if inputs["age"]>=65:
        age_min=65
        
    if inputs["activities"]["distance"]>=0 and inputs["activities"]["distance"]<=150:
        activity_min = 0
        activity_max = 150
    
    if inputs["heartBeats"]["count"]>=100:
        heartbeat_max = 100
        
    if inputs["bloodPressures"]["systolic"]>=100 and inputs["bloodPressures"]["systolic"]<=120:
        activity_min = 100
        activity_max = 120
    if inputs["bloodPressures"]["systolic"]>=120 and inputs["bloodPressures"]["systolic"]<=139:
        activity_min = 120
        activity_max = 139
    if inputs["bloodPressures"]["systolic"]>=140 and inputs["bloodPressures"]["systolic"]<=159:
        activity_min = 140
        activity_max = 159 
    if inputs["bloodPressures"]["systolic"]>=160 and inputs["bloodPressures"]["systolic"]<=179:
        activity_min = 160
        activity_max = 179
    if inputs["bloodPressures"]["systolic"]>=180:
        activity_min = 180

    if inputs["bloodPressures"]["diastolic"]>=60 and inputs["bloodPressures"]["diastolic"]<=79:
        activity_min = 60
        activity_max = 79
    if inputs["bloodPressures"]["diastolic"]>=80 and inputs["bloodPressures"]["diastolic"]<=89:
        activity_min = 80
        activity_max = 89
    if inputs["bloodPressures"]["diastolic"]>=90 and inputs["bloodPressures"]["diastolic"]<=99:
        activity_min = 90
        activity_max = 99 
    if inputs["bloodPressures"]["diastolic"]>=100 and inputs["bloodPressures"]["diastolic"]<=109:
        activity_min = 100
        activity_max = 109
    if inputs["bloodPressures"]["diastolic"]>=110:
        activity_min = 110
    
    features = Features(bp_systolic_min, bp_systolic_max, bp_diastolic_min, bp_diastolic_max,
            heartbeat_min, heartbeat_max, sleep_min, sleep_max, activity_min, activity_max,
            age_min, age_max)

    return features

