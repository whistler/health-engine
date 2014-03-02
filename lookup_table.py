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
        print key
        print table[key]
    '''   
        if(table[key] != None):
            print table[key]
            stub = {'id':features.id, 'recommendation': table[key]}  
            recommendations.append(stub)
     '''
#     return recommendations    

  

def make_keys(features):
    keys_temp = []
    
    '''
    # check if table is already loaded
    if 'table' in vars() or 'table' in globals():
        table = load_recommendations()
        for k in table.keys():
            match=True
            if k.bp_systolic_min != features.bp_systolic_min and features.bp_systolic != None:
                match=False
            if k.bp_systolic_max != features.bp_systolic_max and features.bp_systolic_max != None:
                match=False
            if k.bp_diastolic_min != features.bp_diastolic_min and features.bp_diastolic_min != None:
                match=False
            if k.bp_diastolic_max != features.bp_diastolic_max and features.bp_diastolic_max != None:
                match=False
            if k.heartbeat_min != features.heartbeat_min and features.heartbeat_min != None:
                match=False
            if k.heartbeat_max != features.heartbeat_max and features.heartbeat_max != None:
                match=False
            if k.sleep_min != features.sleep_min and features.sleep_min != None:
                match=False
            if k.sleep_max != features.sleep_max and features.sleep_max != None:
                match=False
            if k.activity_min != features.activity_min and features.activity_min != None:
                match=False
            if k.activity_max != features.activity_max and features.activity_max != None:
                match=False
            if k.age_min != features.age_min and features.age_min != None:
                match=False
            if k.age_max != features.age_max and features.age_max != None:
                match=False
            if match==True:
    '''    
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
#     hb_key.print_features()
    #making activity key
    activity_key = Features('', '', '','',
            '', '', '', '', features.activity_min,features.activity_max,
            features.age_min, features.age_max)
#     activity_key.print_features()
    
    
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
            print "row"
            print row
            key = Features(row[1], row[2], row[3], row[4],
                 row[5], row[6], row[7], row[8], row[9], row[10],
                 row[11], row[12])
            print "key in table"    
            print key.print_features()
            table_temp[key] = row[13];
        #return "hello"
        return table_temp;
    