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
    
    features = Features(bp_systolic_min, bp_systolic_max, bp_diastolic_min, bp_diastolic_max,
            heartbeat_min, heartbeat_max, sleep_min, sleep_max, activity_min, activity_max,
            age_min, age_max)

    return features

