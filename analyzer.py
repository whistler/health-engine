'''
Created on 25-Feb-2014

@author: GaneshKumar Munusamy
'''
from Age import with_HBP_AgeL, with_HBP_AgeM, with_HBP_AgeH
import activity
import lookup_table_sleep


def count_none(input_count):
    count = 0
    for field in input_count:
        if input_count[field] == "None":
            count = count+1
    return count    

def check_bp(input_bp):
    checkBP = "false"
    for field in input_bp:
        if field == "bloodPressures":
            checkBP = "true"            
    return checkBP             

def check_activity(input_act):
    checkActivity = "false"
   
    if input_act['activities'] != -1:
        checkActivity = "true"            
    return checkActivity

def highPress(input_HBP):
    HBP_Age_High = []
    HBP_Age_Mid = []
    if input_HBP['userinfo']['age'] < 20:
        HBP_Age_Low = with_HBP_AgeL(input_HBP)
        return HBP_Age_Low
    elif input_HBP['userinfo']['age'] < 50:
        HBP_Age_Mid = with_HBP_AgeM(input_HBP)
        return HBP_Age_Mid
    else:
        HBP_Age_High = with_HBP_AgeH(input_HBP)
        return HBP_Age_High

def call_bp(input_with_bp):
    highRec = []
    highRec.append("600")
    if input_with_bp['bloodPressures'][0]['systolic'] > 140:
        highRec = highPress(input_with_bp)
        if not highRec.__contains__("601") and input_with_bp['BMI'] > 35 and input_with_bp['userinfo']['age'] > 40 and input_with_bp['activities'][0]['duration'] < 20:
            highRec.append("607")
    if not highRec.__contains__("601") and input_with_bp['sleep'][0]['minutesAsleep'] < 360:
        highRec.append("606")
    
    return highRec       

def recommend_start(input_rec):  
    """Check for Blood Pressure and number of not none
    Call the functions accordingly"""  
    recommendation = []
    Num_of_None = count_none(input_rec)
    if_bp = check_bp(input_rec)
    if_activity = check_activity(input_rec)
    if if_bp is "true":
        recommendation = call_bp(input_rec)
    
    """Irrespective of Blood Pressure Value given"""
    if if_activity is "true":
        recommend_activity = activity.call_activity(input_rec)
        recommendation.append(recommend_activity)
        
    """call the lookup table and search for recommendations"""
    length = recommendation.__len__()
    value = recommendation.count("600")
    if length == value:
        recommendation = []
        recommendation.append("600")    
    else:
        for rec_value in recommendation:
            if rec_value == "600":
                recommendation.remove("600")
        
    recommendation_list = lookup_table_sleep.lookup_value(recommendation)
    return recommendation_list
        
    