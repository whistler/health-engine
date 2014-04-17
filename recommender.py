""" Recommendation engine. Takes input as a python object of the format 
described in the API and returns a python object with recommendations in the 
format described by the API. """

"""
temporily comment the instance_recommendations out for testing

"""

import instance_recommendations
import timeseries_recommendations
import post_processor
import append_tips

def recommend(input):
    recommendations = []
    in_recommendations = instance_recommendations.process(input)
    ts_recommendations = timeseries_recommendations.process(input)
    pp_recommendations = post_processor.process(ts_recommendations, input)
#     ts_recommendations = append_tips.addtips(ts_recommendations)

    if in_recommendations != []:
        recommendations.extend(in_recommendations)  
    
    if ts_recommendations != []:
        recommendations.extend(ts_recommendations)

    if pp_recommendations != {}:
        recommendations.append(pp_recommendations)
        
    return recommendations
