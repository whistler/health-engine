""" Reads recommendation table from disk and returns recommendations which meet the criteria 
described in the features"""

table = None # Stores all the recommendations

def lookup(features):
    
    recommendations = []
    
    # check if table is already loaded
    if 'table' in vars() or 'table' in globals():
        table = load_recommendations()
        
    #TODO: Loop over the recommendations table and append the ones the meet the criteria in features
    # to recommendations list
    
    stub = {'id': 1, 'recommendation': "Test recommendation" }
    recommendations.append(stub)
    
    return recommendations
    

def load_recommendations():
    """ Reads the recommendations table from disk and returns it """
    pass