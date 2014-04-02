'''
Created on Mar 29, 2014

@author: judezhu
'''
import json
     
#Return: UserInfo Json
def generate_user_info(age, gender, height, weight=[], hypertension=True, diabetes=True, insomnia=True, cardio=True):
    user_info ={
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "hypertension" : hypertension,
        "diabetes" : diabetes,
        "insomnia" : insomnia,
        "cardio" : cardio
    }
    return user_info

    
#Read daily blood pressure template
#Return: daily bp json
def generate_daily_BP(date, systolic_bp, diastolic_bp):
    daily_bp={}
    if(date == "" or systolic_bp == "" or diastolic_bp == ""):
        return daily_bp;
    else:
        daily_bp = { 'date': date, 'systolic':int(systolic_bp), "diastolic":int(diastolic_bp)}
        return daily_bp

#Read daily heart beat template
#Return: daily hb json
def generate_daily_HB(date, hb_count):
    daily_hb = {}
    if(date == "" or hb_count == ""):
        return daily_hb;
    else:
        daily_hb = { 'date': date, 'count': int(hb_count)}
        return daily_hb

#Read daily activity template
#Return: daily activity json
def generate_daily_activity(date, duration):
    daily_activity={}
    if(date == "" or duration == ""):
        return daily_activity 
    else:
        daily_activity = { 'date': date, 'duration': int(duration)}
        return daily_activity 

#Read daily sleep template
#Return: daily sleep json
def generate_daily_sleep(date, minutes):
    daily_activity = {}
    if(date == "" or minutes == ""):
        return daily_activity
    else:
        daily_activity = { 'date': date, 'minutesAsleep': int(minutes)}
        return daily_activity 

#Read daily sleep template
#Return: daily sleep json
def generate_daily_weight(date, weight):
    daily_weight = {}
    if(date == "" or weight == ""):
        return daily_weight
    else:
        daily_weight = { 'date': date, 'weight': int(weight)}
        return daily_weight 
    
def get_input_json():
    
    data_table = None
    bp_json = []
    hb_json = []
    activity_json = []
    sleep_json = []
    weight_json = []
    input_json = {}
    
    import csv
    import sys
    try:
        with open('../db/Medical Research - SimulationData.csv', 'rb') as inf:
            #skip the header of csv file
            #http://stackoverflow.com/questions/11349333/using-python-to-analyze-csv-data-how-do-i-ignore-the-first-line-of-data
            has_header = csv.Sniffer().has_header(inf.read(1024))
            inf.seek(0)
            data_table = csv.reader(inf)
            if has_header:
                next(data_table)  # skip header row
            for row in data_table:
        
                bp_json.append(generate_daily_BP(row[1], row[5], row[6]))
                hb_json.append(generate_daily_HB(row[1], row[4]))
                activity_json.append(generate_daily_activity(row[1], row[2]))
                sleep_json.append(generate_daily_sleep(row[1],row[3]))
    
            input_json ={"userinfo":generate_user_info(45,"male",175), "activities":activity_json, "sleep":sleep_json, "heartBeats":hb_json, "bloodPressures":bp_json}  
            return input_json;       
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise 
       

print json.dumps(get_input_json(),sort_keys=True,indent=4, separators=(',', ': '))
