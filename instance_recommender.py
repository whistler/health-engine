""" Reads recommendation table from disk and returns recommendations which meet the criteria 
described in the features"""

table = None # Stores all the recommendations

from features import Features

def recommend(inputs):
    return None

def lookup(features):
    
    keys = []
    recommendations = []
    stub = {}
    id = 0
    
    # check if table is already loaded
    if 'table' in globals():
        global table
        table = load_recommendations()
            
    # generate keys from input features object
    keys = make_keys(features)
    if(keys):
        for key in keys:
            # Loop over the recommendations table and append the ones the meet the criteria in features
            # to recommendations list
            if table.has_key(key):
                stub = { 'id': id, 'recommendation':table[key][0], "url":table[key][1]}
                recommendations.append(stub)  
                id = id+1
            else:
                print "not found"
    return recommendations

def load_recommendations():
    table_temp = {};
    
    """ Reads the recommendations table from disk and returns it """
    import csv
    
    #Todo: add try block
    with open('db/instance_recommendations.csv', 'rb') as f:
        reader = csv.reader(f)
        # skip the first line
        # Todo: Check how many roles there 
        for row in reader:
            value_temp =['',''];
            key = Features(row[1], row[2], row[3], row[4],
                 row[5], row[6], row[7], row[8], row[9], row[10],
                 row[11], row[12])
            value_temp[0] =row[13] 
            value_temp[1]=row[14] 
            table_temp[key] = value_temp;
        return table_temp;
    