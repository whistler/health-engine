""" Recommendation engine. Takes input as a python object of the format 
described in the API and returns a python object with recommendations in the 
format described by the API. """

import instance_recommendations
import analyze_timeseries

def recommend(input):
    i_recommendations = instance_recommendations.process(input)
    ts_recommendations = analyze_timeseries.getRecommendations(input)
    recommendations = i_recommendations + ts_recommendations
    print recommendations
    return recommendations
