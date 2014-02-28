""" Reads recommendation table from disk and returns recommendations which meet the criteria 
described in the features"""

table = None # Stores all the recommendations

from features import Features

def lookup(features):
    
    recommendations = []
    
    #Some data of feature, For testing
    feature=[]
    feature[0]=Features(100, 120, 60, 80, None, None, None, None, 0, 105, 65, 200)
    feature[1]=Features(120, 139, 80, 89, None, None, None, None, 0, 105, 19, 65)
    feature[2]=Features(140, 159, 90, 99, None, None, None, None, None, None, None, None)
   

    # check if table is already loaded
    if 'table' in vars() or 'table' in globals():
        table = load_recommendations()
        
    #TODO: Loop over the recommendations table and append the ones the meet the criteria in features
    # to recommendations list
    
    stub = {'feature0': feature[0], 'recommendation0': "Test recommendation" }
    stub = {'feature1': feature[1], 'recommendation1': "Test recommendation" }
    stub = {'feature2': feature[2], 'recommendation2': "Test recommendation" }

    recommendations.append(stub)
    
    return recommendations
    

def load_recommendations():
    """ Reads the recommendations table from disk and returns it """
    import csv

    pass

