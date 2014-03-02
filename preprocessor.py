""" Takes inputs and extracts features that are useful for recommendations"""

from features import Features

def preprocess(inputs):
    
    # TODO: find the following values from inputs
    bp_systolic_min = ''
    bp_systolic_max = ''
    bp_diastolic_min = ''
    bp_diastolic_max = ''
    heartbeat_min = ''
    heartbeat_max = ''
    sleep_min = ''
    sleep_max = ''
    bp_systolic_min = ''
    bp_systolic_max = ''
    activity_min = ''
    activity_max = ''
    age_min = ''
    age_max = ''
    
    if inputs["age"]>=19 and inputs["age"]<=64:
        age_min='19'
        age_max='64'
    if inputs["age"]>=65:
        age_min='65'
        
    if inputs["activities"]["distance"]>=0 and inputs["activities"]["distance"]<=150:
        activity_min = '0'
        activity_max = '150'
    
    if inputs["heartBeats"]["count"]>=100:
        heartbeat_max = '100'
        
    if inputs["bloodPressures"]["systolic"]>=100 and inputs["bloodPressures"]["systolic"]<=120:
        bp_systolic_min = '100'
        bp_systolic_max = '120'
    if inputs["bloodPressures"]["systolic"]>=120 and inputs["bloodPressures"]["systolic"]<=139:
        bp_systolic_min = '120'
        bp_systolic_max = '139'
    if inputs["bloodPressures"]["systolic"]>=140 and inputs["bloodPressures"]["systolic"]<=159:
        bp_systolic_min = '140'
        bp_systolic_max = '159' 
    if inputs["bloodPressures"]["systolic"]>=160 and inputs["bloodPressures"]["systolic"]<=179:
        bp_systolic_min = '160'
        bp_systolic_max = '179'
    if inputs["bloodPressures"]["systolic"]>=180:
        bp_systolic_min = '180'

    if inputs["bloodPressures"]["diastolic"]>=60 and inputs["bloodPressures"]["diastolic"]<=79:
        bp_diastolic_min = '60'
        bp_diastolic_max = '79'
    if inputs["bloodPressures"]["diastolic"]>=80 and inputs["bloodPressures"]["diastolic"]<=89:
        bp_diastolic_min = '80'
        bp_diastolic_max = '89'
    if inputs["bloodPressures"]["diastolic"]>=90 and inputs["bloodPressures"]["diastolic"]<=99:
        bp_diastolic_min = '90'
        bp_diastolic_max = '99' 
    if inputs["bloodPressures"]["diastolic"]>=100 and inputs["bloodPressures"]["diastolic"]<=109:
        bp_diastolic_min = '100'
        bp_diastolic_max = '109'
    if inputs["bloodPressures"]["diastolic"]>=110:
        bp_diastolic_min = '110'
    
    features = Features(bp_systolic_min, bp_systolic_max, bp_diastolic_min, bp_diastolic_max,
            heartbeat_min, heartbeat_max, sleep_min, sleep_max, activity_min, activity_max,
            age_min, age_max)

    features.print_features()
    return features

