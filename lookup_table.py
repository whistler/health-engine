""" Reads recommendation table from disk and returns recommendations which meet
the criteria described in the features"""

table = None # Stores all the recommendations

from features import Features

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
            # Loop over the recommendations table and 
            # append the ones the meet the criteria to recommendations list
            if table.has_key(key):
                stub = { 'id': id, 'recommendation':table[key][0], "url":table[key][1]}
                recommendations.append(stub)  
                id = id+1
            else:
                print "not found"
    return recommendations    

  
#Extract keys for various input
#Return a list of features(keys)
def make_keys(features):
    keys_temp = []
    
    if(features != None):
        #making blood pressure key    
        bp_key = Features(features.bp_systolic_min, features.bp_systolic_max, features.bp_diastolic_min, 
                features.bp_diastolic_max, '', '', '', '', '', '',
                '', '')
        #makng heart beat key
        hb_key = Features('', '', '','',
                features.heartbeat_min, features.heartbeat_max, '', '', '', '', 
                '', '')
        
        #making activity key
        activity_key = Features('', '', '','',
                '', '', '', '', features.activity_min,features.activity_max,
                features.age_min, features.age_max)
        
        #add key to the key list
        keys_temp.append(bp_key)
        keys_temp.append(hb_key)
        keys_temp.append(activity_key)    
        return keys_temp
    


#Load the recommendation table from csv file
#Return: a dictionary {features(key): recommendation(value)}

def load_recommendations():
    table_temp = {};
    import csv
    
    #Todo: add try block
    with open('db/recom_v1.csv', 'rb') as f:
        reader = csv.reader(f)
        # Todo: skip the first line
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
    