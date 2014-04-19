""" Does time series based recommendations based on a lookup table as discussed
by the engine team on Apr 3rd 2014 """

import datetime
import math
import pandas
import preprocessor
import fluctuation_analysis

table = pandas.read_csv("db/timeseries_recommendations.csv")
table[['age', 'gender']] = table[['age', 'gender']].astype(str)

def process(inputs):
    """ Takes a python structure containing the input data from the REST API and
    returns a list of conditions based on the lookup table"""
    recommendations = []
    
    features = _build_features(inputs)

    age = None
    gender = None

    if 'userinfo' in inputs:
        userinfo = inputs['userinfo']
        if 'age' in userinfo:
            age = userinfo['age']
        if 'gender' in userinfo:
            gender = userinfo['gender']
    
    for _recommendation in table.iterrows():
        recommendation = _recommendation[1]
        days = int(recommendation['days'])
        feature = recommendation['input'] # use only the last n days
        values = features[feature][0:days]
#         print values
#         print _satisfiesAvgLess([80], recommendation['avg less'])
        conditions = [
            _satisfiesFluctuation(values, recommendation['fluctuation']),
            _satisfiesGradient(values, recommendation['gradient']),
            _satisfiesAllLess(values, recommendation['all less']),
            _satisfiesAllMore(values, recommendation['all more']),
            _satisfiesAvgLess(values, recommendation['avg less']),
            _satisfiesAvgMore(values, recommendation['avg more']),
            _satisfiesAge(age, recommendation['age']),
            _satisfiesGender(gender, recommendation['gender'])
        ]
        
        if all(conditions):
            recommendations.append(_recommendation_output(recommendation))
    return recommendations
    
def _recommendation_output(recommendation):
    """ Take in a pandas row and return the format for the output recommendation 
    """
    return {
        'id': recommendation['id'],
        'condition': recommendation['condition'],
        'direction': recommendation['direction'],
        'severity' : int(round(recommendation['severity'])),
        'url' : ''
        }
    
def _satisfiesFluctuation(input_val, fluctuation):
    if math.isnan(fluctuation): return True
    fluctuations = fluctuation_analysis.analyze_fluctuation(input_val)
    return fluctuations >= fluctuation
    return False
    
def _satisfiesGradient(input_val, gradient):
    if math.isnan(gradient): return True
    #TODO: we are not using this right now but use padas or numpy to find
    # gradient using linear regression
    return True
    
def _satisfiesAllLess(input_val, all_less):
    if math.isnan(all_less): return True
    return all([value < all_less for value in input_val])
    
def _satisfiesAllMore(input_val, all_more):
    if math.isnan(all_more): return True
    return all([value > all_more for value in input_val])
    
def _satisfiesAvgLess(input_val, avg_less):
    if math.isnan(avg_less): return True
    avg = sum(input_val)/len(input_val)
    return avg < avg_less
    
def _satisfiesAvgMore(input_val, avg_more):
    if math.isnan(avg_more): return True
    avg = sum(input_val)/len(input_val)
    return avg > avg_more
    
def _satisfiesAge(userage, age):
    if age == 'nan' or not age or not userage: return True
    return _in_range(userage, age)

def _satisfiesGender(usergender, gender):
    if gender == 'nan' or not gender or not usergender: return True
    inp = usergender.lower()[0] 
    gen = gender.lower()[0]
    return inp == gen

def _in_range(value, range):
    """ Checks if value is in range
    value - numeric value
    range - string in the format 'start_number-end_number'
    """
    min_val, max_val = (int(x) for x in "16-60".split("-"))
    return int(value) > min_val and int(value) < max_val
    
def _build_features(inputs):
    """ Generate dictionary containing a list of data sorted by date for each 
    time series input being used"""
    # Note the preprocessor was not used because it also returns dates
    
    #TODO: Lists should be sorted by date
    bp_systolic = bp_diastolic = pulse = sleep = activity = []

    if "bloodPressures" in inputs:
        bp_systolic = [bp["systolic"] for bp in inputs["bloodPressures"]]
        bp_disastolic = [bp["diastolic"] for bp in inputs["bloodPressures"]]

    if "heartBeats" in inputs:
        pulse = [value["count"] for value in inputs["heartBeats"]]
        
    if "activities" in inputs:
        activity = [value["duration"] for value in inputs["activities"]]
        
    if "sleep" in inputs:
        sleep = [value["minutesAsleep"] for value in inputs["sleep"]]
    
    features = {
        'bloodpressure': bp_systolic,
        'pulse': pulse,
        'activity': activity,
        'sleep': sleep
    }
    return features