""" Recommendation engine. Takes input as a python object of the format 
described in the API and returns a python object with recommendations in the 
format described by the API. """

"""
temporily comment the instance_recommendations out for testing

"""

import instance_recommendations
import timeseries_recommendations
import append_tips

def recommend(input):
#     i_recommendations = instance_recommendations.process(input)
    ts_recommendations = timeseries_recommendations.process(input)
    print ts_recommendations
    ts_recommendations = append_tips.addtips(ts_recommendations)
    print ts_recommendations 
#     recommendations = i_recommendations + ts_recommendations
    return ts_recommendations
