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
    """ instant and time series analysis """
    in_recommendations = instance_recommendations.process(input)
    ts_recommendations = timeseries_recommendations.process(input)
    recommendations.extend(in_recommendations)  
    recommendations.extend(ts_recommendations)

    """ processes and combine the recommendation list"""
    recommendations = _sort_recommendations(recommendations)
    recommendations = _combine_recommendations(recommendations, input)
    
    """ append tips to the recommendations"""
    recommendations = append_tips.addtips(recommendations)
    
    return recommendations
    
def _sort_recommendations(recommendations):
    """ Only return the highest severity for one input
    """
    sorted_recoms = [{}]*4
    for recom in recommendations:
        if sorted_recoms[int(recom['id'])/100-1] == {}:
            sorted_recoms[int(recom['id'])/100-1] = recom;
        else:
            if sorted_recoms[int(recom['id'])/100-1]['severity'] < recom['severity']:
                sorted_recoms[int(recom['id'])/100-1] = recom
            if sorted_recoms[int(recom['id'])/100-1]['severity'] == recom['severity']:
                if sorted_recoms[int(recom['id'])/100-1]['id'] < recom['id']:
                    sorted_recoms[int(recom['id'])/100-1] = recom
    return [item for item in sorted_recoms if item != {}]

def _combine_recommendations(recommendations, input):
    """ When there is a combination recommendation, delete the original one with combined_id (sourceGroup in PostProcess.csv.
    """
    pp_recommendations, combined_id = post_processor.process(recommendations, input)
    if pp_recommendations == {}:
        return recommendations
    else:
        recoms = []
        for recom in recommendations:
            if int(recom['id'])/100 != int(combined_id):
                recom['condition'] = recom['condition'].capitalize()
                recoms.append(recom)
            else:
                pp_recommendations['condition'] += ", probably because your " +  recom['condition']
        recoms.append(pp_recommendations)
        return recoms
     
#     return _filter_off_low_severity_recommendation(recommendations)
# 
# def _filter_off_low_severity_recommendation(recommendations):
#     filtered_recommendations = []
#     for recom in recommendations:
#         if recom['severity'] >= 2:
# #             if "direction" in recom:
# #                 del recom["direction"]
#             filtered_recommendations.append(recom)
#     return filtered_recommendations
            