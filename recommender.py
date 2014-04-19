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
#     ts_recommendations = append_tips.addtips(ts_recommendations)

    if in_recommendations != []:
        recommendations.extend(in_recommendations)  
    
    if ts_recommendations != []:
        recommendations.extend(ts_recommendations)

    pp_recommendations = post_processor.process(recommendations, input)
#     print pp_recommendations
 
    if pp_recommendations != {}:
        recommendations.append(pp_recommendations)
        
    recommendations = append_tips.addtips(recommendations)
    return _filter_off_low_severity_recommendation(recommendations)

def _filter_off_low_severity_recommendation(recommendations):
    filtered_recommendations = []
    for recom in recommendations:
        if recom['severity'] >= 2:
#             if "direction" in recom:
#                 del recom["direction"]
            filtered_recommendations.append(recom)
    return filtered_recommendations