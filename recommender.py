""" Recommendation engine. Takes input as a python object of the format 
described in the API in the docs/api.md file and returns a python
object with recommendations in the format described by the API. """ 

import instance_recommender
import timeseries_recommender
import postprocessor

def recommend(inputs):
    """ Takes as input a python object similar to the JSON input defined in the 
    API and returns a python structure containing the recommendations """
    instance_recommendations = instance_recommender.recommend(inputs)
    ts_recommendations = timeseries_recommender.recommend(inputs)
    recommendations = postprocessor.process(instance_recommendations, 
            ts_recommendations)
    return recommendations