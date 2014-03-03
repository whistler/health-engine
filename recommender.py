""" Recommendation engine. Takes input as a python object of the format described in the API at 
http://docs.healthengine.apiary.io/ and returns a python object with recommendations in the 
format described by the API. """ 

import preprocessor
import lookup_table

def recommend(inputs):
    features = preprocessor.preprocess(inputs)
    recommendations = lookup_table.lookup(features)
    return recommendations
