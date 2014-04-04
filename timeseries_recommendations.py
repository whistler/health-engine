""" Does time series based recommendations based on a lookup table as discussed
by the engine team on Apr 3rd 2014 """

import datetime
import pandas
import preprocessor

table = pandas.read_csv("db/timeseries_recommendations.py")

def process(input):
    """ Takes a python structure containing the input data from the REST API and
    returns a list of conditions based on the lookup table"""
    recommendations = []
    
    inputs = {
        'bloodpressure': preprocessor.getBloodPressuresList(inputs)
        'pulse': preprocessor.getHeartBeatsList(inputs)
        'activity': preprocessor.getActivitiesList(inputs)
        'sleep': preprocessor.getSleepList(inputs)
    }
    
    for _recommendation in table.iterrows():
        recommendation = _recommendation[1]
        days = recommedation['days']
        input = recommendation['input'][-days:] # use only the last n days
        input_values = inputs[input]
        
        if _satisfiesAge(inputs, recommendation['age']) and
            _satisfiesFluctuation(input, recommendation['fluctuation']) and
            _satisfiesGradient(input, recommendation['gradient']) and
            _satisfiesAllLess(input, recommendation['all less']) and
            _satisfiesAllMore(input, recommendation['all more']) and
            _satisfiesAvgLess(input, recommendation['avg less']) and
            _satisfiesAvgMore(input, recommendation['avg more']):
                recommendations.append(_recommendation_output(recommendation))
                
    return recommendations
    
def _recommendation_output(recommendation):
    """ Take in a padas row and return the format for the output recommendation 
    """
    return {
        'id': recommendation['id'],
        'condition': recommendation['condition'],
        'direction': recommendation['direction']
        }

def _satisfiesAge(inputs, age):
    return True
    
def _satisfiesFluctuation(input, fluctuation):
    return True
    
def _satisfiesGradient(input, gradient):
    return True
    
def _satisfiesAllLess(input, all_less):
    return True
    
def _satisfiesAllMore(input, all_more):
    return True
    
def _satisfiesAvgLess(input, avg_less):
    return True
    
def _satisfiesAvgMore(input, avg_more):
    return True