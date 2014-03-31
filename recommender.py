""" Recommendation engine. Takes input as a python object of the format 
described in the API and returns a python object with recommendations in the 
format described by the API. """

import analyzer
import instance_recommendations
import preprocessor
import analyze_timeseries

def recommend(inputs):

    recommendations = analyze_timeseries.getRecommendations(inputs)
    return recommendations
#     recommendation_list = []
#     all_recommendation = analyzer.recommend_start(inputs)
#     features = preprocessor.preprocess(inputs)
#     recommendations = instance_recommendations.process(features)
#     recommendations.append(all_recommendation)
#     return all_recommendation
