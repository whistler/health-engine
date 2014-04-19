import timeseries_recommendations
import json
import match_recommendations as match_reco


ACTIVITY_INDEX = 0
BLOODPRESSURE_INDEX = 1
HEARTBEAT_INDEX = 2
SLEEP_INDEX = 3

def process(input,user_input):
 
    ppfeatures = {'BPHigh':0,'BPFluct':0,'BPLow':0,'HBHigh':0,'HBFluct':0,'HBLow':0,'SleepHigh':0,'SleepFluct':0,'SleepLow':0,'ActivityHigh':0,'ActivityFluct':0,'ActivityLow':0,'Insomnia':0,'Hypertension':0,'Diabetes':0,'Cardio':0}        
    import pdb
    priority_list = _filter_priority(input)
#     print priority_list
    bpValues = _filter_BP_values(priority_list)
    hbValues = _filter_HB_values(priority_list)
    sleepValues = _filter_sleep_values(priority_list)
    activityValues = _filter_activity_values(priority_list)
    if len(bpValues)>1:
        max_BP_severity = _determine_max_severity(bpValues)
        if max_BP_severity.get('direction')==1:
            ppfeatures['BPHigh'] = max_BP_severity.get('max_severity')
        elif max_BP_severity.get('direction')==0:
            ppfeatures['BPFluct']= max_BP_severity.get('max_severity')
        else:
            ppfeatures['BPLow'] = max_BP_severity.get('max_severity')
            
    if len(hbValues)>1:
        max_HB_severity = _determine_max_severity(hbValues)
        if max_HB_severity.get('direction')==1:
            ppfeatures['HBHigh'] = max_HB_severity.get('max_severity')
        elif max_HB_severity.get('direction')==0:
            ppfeatures['HBFluct'] = max_HB_severity.get('max_severity')  
        else:
            ppfeatures['HBLow'] = max_HB_severity.get('max_severity')
            
    if len(sleepValues)>1:    
        max_sleep_severity = _determine_max_severity(sleepValues)
        if max_sleep_severity.get('direction')==1:
            ppfeatures['SleepHigh'] = max_sleep_severity.get('max_severity') 
        elif max_sleep_severity.get('direction')==0:
            ppfeatures['SleepFluct'] = max_sleep_severity.get('max_severity')   
        else:
            ppfeatures['SleepLow'] = max_sleep_severity.get('max_severity')  
    if len(activityValues)>1:    
        max_active_severity = _determine_max_severity(activityValues)
        if max_active_severity.get('direction')==1:
            ppfeatures['ActivityHigh'] = max_active_severity.get('max_severity') 
        elif max_active_severity.get('direction')==0:
            ppfeatures['ActivityFluct']= max_active_severity.get('max_severity')
        else:
            ppfeatures['ActivityLow'] = max_active_severity.get('max_severity') 
    
   # print 'maximum severity for BP is %d',max_BP_severity

    if "userinfo" in user_input:
        userinfo = user_input["userinfo"]    
        if "hypertension" in userinfo and userinfo["hypertension"]: 
            ppfeatures['Hypertension']=1
        if "diabetes" in userinfo and userinfo["diabetes"]:
            ppfeatures['Diabetes']=1
        if "insomnia" in userinfo and userinfo["insomnia"]:
            ppfeatures['Insomnia']=1
        if "cardio" in userinfo and userinfo["cardio"]:
            ppfeatures['Cardio']=1
    #print ppfeatures  
    return match_reco.read_recomendations(ppfeatures)     
    
 # filter out severity 1 and 2    
    
def _filter_priority(input):
    
    filteredlist = [elem for elem in input if ((elem['severity']== 5) or (elem['severity']== 4) or (elem['severity']== 3))]
    return filteredlist

def _determine_max_severity(input):
    bp_array= {}
    max = input[0]
    for x in input:
        if x['severity']>max['severity']:
            max = x
    bp_array['max_severity'] = max['severity']
    bp_array['direction']= max['direction']        
    return bp_array 
#max(input['severity'].values())

  
def _filter_BP_values(input):
    
    filterBP = [elem for elem in input if str(elem['id'])[:1]== '2']
    return filterBP;
    
def _filter_HB_values(input):
    
    filterHB = [elem for elem in input if str(elem['id'])[:1]== '3']
    return filterHB;

def _filter_sleep_values(input):
    
    filterSleep = [elem for elem in input if str(elem['id'])[:1]== '4']
    return filterSleep; 
      
def _filter_activity_values(input):
    
    filterActivity = [elem for elem in input if str(elem['id'])[:1]== '1']
    return filterActivity;     
    