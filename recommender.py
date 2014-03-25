""" Recommendation engine. Takes input as a python object of the format 
described in the API at http://docs.healthengine.apiary.io/ and returns a python
object with recommendations in the format described by the API. """ 

import analyzer
import lookup_table
import preprocessor


def recommend(inputs):
    recommendation_list = []
    all_recommendation = analyzer.recommend_start(inputs)
    features = preprocessor.preprocess(inputs)
    recommendations = lookup_table.lookup(features)
    recommendations.append(all_recommendation)
    return all_recommendation