# TODO: To be deleted

'''
Created on 05-Mar-2014

@author: GaneshKumar Munusamy
'''
def load_recommendations():
    import csv
    temp_table = {}
    with open('db/lookup_sleep.csv','rb') as line:
        reader = csv.reader(line)
        
        
        for row in reader:
            temp_table[row[0]]=row[1]
        return temp_table
    

def lookup_value(recommend_key):
    
    recommendation_stub = []
    
    value_pair = load_recommendations()
    
    for key in recommend_key:
        stub = {'id':key,'recommendation':value_pair[key]}
        recommendation_stub.append(stub)
    return recommendation_stub