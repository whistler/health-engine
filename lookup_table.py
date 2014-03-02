""" Reads recommendation table from disk and returns recommendations which meet the criteria 
described in the features"""

table = None # Stores all the recommendations

from features import Features

def lookup(features):
    
    keys = []
    recommendations = []
    stub = {}
    # check if table is already loaded
    if 'table' in vars() or 'table' in globals():
        table = load_recommendations()
        for k in table.keys():
            print table[k]
    
    keys = make_keys(features)
    

    #TODO: check whether keys is empty
    for key in keys:
    # Loop over the recommendations table and append the ones the meet the criteria in features
    # to recommendations list
        if key in table.keys():
            print "found key!"
            print table[key]
            stub = { 'recommendation': table[key]}
            recommendations.append(stub)  
        else:
            print "no key!"
    '''   
        if(table[key] != None):
            print table[key]
            stub = {'id':features.id, 'recommendation': table[key]}  
            recommendations.append(stub)
     '''
    return recommendations    

  

def make_keys(features):
    keys_temp = []
    
    #making blood pressure key    
    bp_key = Features(features.bp_systolic_min, features.bp_systolic_max, features.bp_diastolic_min, 
            features.bp_diastolic_max, '', '', '', '', '', '',
            '', '')
    print "bp_key"
    bp_key.print_features()
    #makng heart beat key
    hb_key = Features('', '', '','',
            features.heartbeat_min, features.heartbeat_max, '', '', '', '', 
            '', '')
    print "hb_key"
    hb_key.print_features()
    
    #making activity key
    activity_key = Features('', '', '','',
            '', '', '', '', features.activity_min,features.activity_max,
            features.age_min, features.age_max)
    print "activity_key"
    activity_key.print_features()
    
    
    #add key to the key list
    keys_temp.append(bp_key)
    keys_temp.append(hb_key)
    keys_temp.append(activity_key)    
    return keys_temp

def load_recommendations():
    table_temp = {};
    """ Reads the recommendations table from disk and returns it """
    import csv
    
    #Todo: add try block
    with open('recom.csv', 'rb') as f:
        reader = csv.reader(f)
        #Todo: Check how many roles there 
        for row in reader:
            print "row: "
            print row
            key = Features(row[1], row[2], row[3], row[4],
                 row[5], row[6], row[7], row[8], row[9], row[10],
                 row[11], row[12])
            print "key in table"    
            print key.print_features()
            table_temp[key] = row[13];
        #return "hello"
        return table_temp;
    