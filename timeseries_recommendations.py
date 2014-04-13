""" Does time series based recommendations based on a lookup table as discussed
by the engine team on Apr 3rd 2014 """

import datetime
import math
import pandas
import preprocessor
import fluctuation_analysis

table = pandas.read_csv("db/timeseries_recommendations.csv")

def process(input):
    """ Takes a python structure containing the input data from the REST API and
    returns a list of conditions based on the lookup table"""
    recommendations = []
    
    features = _build_features(input)
    
    for _recommendation in table.iterrows():
        recommendation = _recommendation[1]
        days = int(recommendation['days'])
        feature = recommendation['input'] # use only the last n days
        values = features[feature][-days:]
        
        conditions = [_satisfiesAge(input, recommendation['age']),
            _satisfiesFluctuation(values, recommendation['fluctuation']),
            _satisfiesGradient(values, recommendation['gradient']),
            _satisfiesAllLess(values, recommendation['all less']),
            _satisfiesAllMore(values, recommendation['all more']),
            _satisfiesAvgLess(values, recommendation['avg less']),
            _satisfiesAvgMore(values, recommendation['avg more'])
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
        'severity' : recommendation['severity'],
        'url' : recommendation['url']
        }

def _satisfiesAge(inputs, age):
    if math.isnan(age): return True
    if inputs["userinfo"] and inputs["userinfo"]["age"]:
        return _in_range(age, inputs["userinfo"]["age"])
    else:
        return True
    
def _satisfiesFluctuation(input, fluctuation):
    if math.isnan(fluctuation): return True
    fluctuations = fluctuation_analysis.analyze_fluctuation(input)
    return fluctuations >= fluctuation
    return False
    
def _satisfiesGradient(input, gradient):
    if math.isnan(gradient): return True
    #TODO: we are not using this right now but use padas or numpy to find
    # gradient using linear regression
    return True
    
def _satisfiesAllLess(input, all_less):
    if math.isnan(all_less): return True
    return all([value < all_less for value in input])
    
def _satisfiesAllMore(input, all_more):
    if math.isnan(all_more): return True
    return all([value > all_more for value in input])
    
def _satisfiesAvgLess(input, avg_less):
    if math.isnan(avg_less): return True
    avg = sum(input)/len(input)
    return avg < avg_less
    
def _satisfiesAvgMore(input, avg_more):
    
    if math.isnan(avg_more): return True
    avg = sum(input)/len(input)
    return avg > avg_more
    
def _in_range(value, range):
    """ Checks if value is in range
    value - numeric value
    range - string in the format 'start_number-end_number'
    """
    # TODO: Implement this
    return True
    
def _build_features(input):
    """ Generate dictionary containing a list of data sorted by date for each 
    time series input being used"""
    # Note the preprocessor was not used because it also returns dates
    
    #TODO: Lists should be sorted by date
    bp_systolic = bp_diastolic = pulse = sleep = activity = []

    if "bloodPressures" in input:
        bp_systolic = [bp["systolic"] for bp in input["bloodPressures"]]
        bp_disastolic = [bp["diastolic"] for bp in input["bloodPressures"]]

    if "heartBeats" in input:
        pulse = [value["count"] for value in input["heartBeats"]]
        
    if "activities" in input:
        activity = [value["duration"] for value in input["activities"]]
        
    if "sleep" in input:
        sleep = [value["minutesAsleep"] for value in input["sleep"]]
    
    features = {
        'bloodpressure': bp_systolic,
        'pulse': pulse,
        'activity': activity,
        'sleep': sleep
    }
    return features