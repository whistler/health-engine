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
    
    dailydata=0
    weeklydata=1
    monthlydata=2
    
    # check user info
    if inputs.has_key("userinfo"):
        if inputs["userinfo"].has_key("age"):
            if inputs["userinfo"]["age"]>=19 and inputs["userinfo"]["age"]<=64:
                age_min='19'
                age_max='64'
                #at this age, 30 mins at least
                if inputs.has_key("activities"):
                    if inputs["activities"][dailydata]["distance"]<30:
                        activity_min = '30'
            if inputs["userinfo"]["age"]<=18:
                age_max='18'
                #at this age, 60 mins at least
                if inputs.has_key("activities"):
                    if inputs["activities"][dailydata]["distance"]<60:
                        activity_min = '60'
            
            # check heartbeats, age between 2 to 6
            if inputs["userinfo"]["age"]>=2 and inputs["userinfo"]["age"]<=6 and inputs.has_key("heartBeats"):
                if inputs["heartBeats"][dailydata]["count"]>=121:
                    heartbeat_min = '121'
                if inputs["heartBeats"][dailydata]["count"]>=75 and inputs["heartBeats"][dailydata]["count"]<121:
                    heartbeat_min = '75'
                    heartbeat_max = '120'
                    
            # check heartbeats, age between 7 to 17
            if inputs["userinfo"]["age"]>=7 and inputs["userinfo"]["age"]<=17 and inputs.has_key("heartBeats"):
                if inputs["heartBeats"][dailydata]["count"]>=111:
                    heartbeat_min = '111'
                if inputs["heartBeats"][dailydata]["count"]>=75 and inputs["heartBeats"][dailydata]["count"]<111:
                    heartbeat_min = '75'
                    heartbeat_max = '110'
                    
            # check heartbeats age above 18
            if inputs["userinfo"]["age"]>=18 and inputs.has_key("heartBeats"):
                if inputs["heartBeats"][dailydata]["count"]>=101:
                    heartbeat_min = '101'
                if inputs["heartBeats"][dailydata]["count"]>=60 and inputs["heartBeats"][dailydata]["count"]<101:
                    heartbeat_min = '60'
                    heartbeat_max = '100'

    #check bloodpressure
    if inputs.has_key("bloodPressures"):
        if inputs["bloodPressures"][dailydata].has_key("systolic") and inputs["bloodPressures"][dailydata].has_key("diastolic"):
            if inputs["bloodPressures"][dailydata]["systolic"]<=119:
                bp_systolic_max = '119'
            if inputs["bloodPressures"][dailydata]["systolic"]>=120 and inputs["bloodPressures"][dailydata]["systolic"]<=139:
                bp_systolic_min = '120'
                bp_systolic_max = '139'
            if inputs["bloodPressures"][dailydata]["systolic"]>=140 and inputs["bloodPressures"][dailydata]["systolic"]<=159:
                bp_systolic_min = '140'
                bp_systolic_max = '159' 
            if inputs["bloodPressures"][dailydata]["systolic"]>=160 and inputs["bloodPressures"][dailydata]["systolic"]<=179:
                bp_systolic_min = '160'
                bp_systolic_max = '179'
            if inputs["bloodPressures"][dailydata]["systolic"]>=180:
                bp_systolic_min = '180'
        
            if inputs["bloodPressures"][dailydata]["diastolic"]<=79:
                bp_diastolic_max = '79'
            if inputs["bloodPressures"][dailydata]["diastolic"]>=80 and inputs["bloodPressures"][dailydata]["diastolic"]<=89:
                bp_diastolic_min = '80'
                bp_diastolic_max = '89'
            if inputs["bloodPressures"][dailydata]["diastolic"]>=90 and inputs["bloodPressures"][dailydata]["diastolic"]<=99:
                bp_diastolic_min = '90'
                bp_diastolic_max = '99' 
            if inputs["bloodPressures"][dailydata]["diastolic"]>=100 and inputs["bloodPressures"][dailydata]["diastolic"]<=109:
                bp_diastolic_min = '100'
                bp_diastolic_max = '109'
            if inputs["bloodPressures"][dailydata]["diastolic"]>=110:
                bp_diastolic_min = '110'
    
    features = Features(bp_systolic_min, bp_systolic_max, bp_diastolic_min, bp_diastolic_max,
            heartbeat_min, heartbeat_max, sleep_min, sleep_max, activity_min, activity_max,
            age_min, age_max)

    features.print_features()
    return features

