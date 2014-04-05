'''
Created on Mar 29, 2014

@author: judezhu
'''
import json
     
#Return: UserInfo Json
def generate_user_info(age, gender, height, weight=[], hypertension=True, diabetes=True, insomnia=True, cardio=True):
    user_info ={
        "age": int(age),
        "gender": gender,
        "height": int(height),
        "weight": weight,
        "hypertension" : True if(hypertension.lower() == 'true') else False,
        "diabetes" : True if(diabetes.lower() == 'true') else False,
        "insomnia" : True if(insomnia.lower() == 'true') else False,
        "cardio" : True if(cardio.lower() == 'true') else False
    }
    return user_info

    
#Read daily blood pressure template
#Return: daily bp json
def generate_daily_BP(date, systolic_bp, diastolic_bp):
    daily_bp={}
    if(date == "" or systolic_bp == "" or diastolic_bp == ""):
        return None
    else:
        daily_bp = { 'date': date, 'systolic':int(systolic_bp), "diastolic":int(diastolic_bp)}
        return daily_bp

#Read daily heart beat template
#Return: daily hb json
def generate_daily_HB(date, hb_count):
    daily_hb = {}
    if(date == "" or hb_count == ""):
        return None
    else:
        daily_hb = { 'date': date, 'count': int(hb_count)}
        return daily_hb

#Read daily activity template
#Return: daily activity json
def generate_daily_activity(date, duration):
    daily_activity={}
    if(date == "" or duration == ""):
        return None
    else:
        daily_activity = { 'date': date, 'duration': int(duration)}
        return daily_activity 

#Read daily sleep template
#Return: daily sleep json
def generate_daily_sleep(date, minutes):
    daily_activity = {}
    if(date == "" or minutes == ""):
        return None
    else:
        daily_activity = { 'date': date, 'minutesAsleep': int(minutes)}
        return daily_activity 

#Read daily sleep template
#Return: daily sleep json
def generate_daily_weight(date, weight):
    daily_weight = {}
    if(date == "" or weight == ""):
        return None
    else:
        daily_weight = { 'date': date, 'value': int(weight)}
        return daily_weight 
    
#Read inputs from "/db/Medical Research - SimulationData.csv", use help functions
#to assemble test json   
#Return: input_json
def get_input_json():
    
    data_table = None
    bp_json = []
    hb_json = []
    activity_json = []
    sleep_json = []
    weight_json = []
    input_json = {}
    
    info_type = ''
    user_row = None
    user_info_json = {}
    
    import csv
    import sys
    try:
        with open('Medical Research - SimulationData.csv', 'rb') as inf:
            data_table = csv.reader(inf)
            for row in data_table:
                if(row != [] and row[0] != ''):
                    if(row[0] == 'User_Info'):
                        info_type = row[0]
                        continue
                    elif(row[0] == 'Device_Info'):
                        info_type = row[0]
                        continue
                    
                    if(info_type == 'User_Info'):
                        user_row = row
                    elif(info_type == 'Device_Info'):
                        if (generate_daily_BP(row[1], row[5], row[6])!=None):
                            bp_json.append(generate_daily_BP(row[1], row[5], row[6]))
                        if (generate_daily_HB(row[1], row[4])!=None):
                            hb_json.append(generate_daily_HB(row[1], row[4]))
                        if (generate_daily_activity(row[1], row[2])!=None):
                            activity_json.append(generate_daily_activity(row[1], row[2]))
                        if (generate_daily_sleep(row[1],row[3])!=None):
                            sleep_json.append(generate_daily_sleep(row[1],row[3]))
                        if (generate_daily_weight(row[1],row[7])!=None):
                            weight_json.append(generate_daily_weight(row[1],row[7]))
                else:
                    continue
            user_info_json =generate_user_info(user_row[1], user_row[2], user_row[3], weight_json, user_row[4], user_row[5], user_row[6], user_row[7])     
            input_json ={"userinfo":user_info_json, "activities":activity_json, "sleep":sleep_json, "heartBeats":hb_json, "bloodPressures":bp_json}  
            return input_json;       
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise 
       

print json.dumps(get_input_json(),sort_keys=True,indent=4, separators=(',', ': '))
