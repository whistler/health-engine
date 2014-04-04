""" Recommendation engine. Takes input as a python object of the format 
described in the API and returns a python object with recommendations in the 
format described by the API. """

"""
temporily comment the instance_recommendations out for testing

"""

import instance_recommendations
import timeseries_recommendations

def recommend(input):
    i_recommendations = instance_recommendations.process(input)
    ts_recommendations = timeseries_recommendations.process(input)
    recommendations = i_recommendations + ts_recommendations
    print recommendations
    return recommendations
#     recommendations = analyze_timeseries.getRecommendations(input)
#     return recommendations
