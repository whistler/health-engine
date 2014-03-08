""" Takes inputs and extracts features that are useful for recommendations"""

from features import Features
import lookup_table

dailydata=0
weeklydata=1
monthlydata=2
#Load the table
table = lookup_table.load_recommendations()
tableContent=table.keys()

#Check to see if the given systolic is in the range
def checkSystolic(feature, eachLine):
    if (int)(feature["bloodPressures"][dailydata]["systolic"])>=(int)(eachLine.bp_systolic_min) and (int)(feature["bloodPressures"][dailydata]["systolic"])<=(int)(eachLine.bp_systolic_max):
        return True
    else:
        return False

#Check to see if the given diastolic is in the range
def checkDiastolic(feature, eachLine):
    if (int)(feature["bloodPressures"][dailydata]["diastolic"])>=(int)(eachLine.bp_diastolic_min) and (int)(feature["bloodPressures"][dailydata]["diastolic"])<=(int)(eachLine.bp_diastolic_max):
        return True
    else:
        return False

#Check to see if the given heartBeats is in the range
def checkHeartBeats(feature, eachLine):
    if (int)(feature["heartBeats"][dailydata]["count"])>=(int)(eachLine.heartbeat_min) and (int)(feature["heartBeats"][dailydata]["count"])<=(int)(eachLine.heartbeat_max):
        return True
    else:
        return False
    
#Check to see if the given distance is in the range
def checkSleep(feature, eachLine):
    if (int)(feature["sleep"][dailydata]["efficiency"])>=(int)(eachLine.sleep_min) and (int)(feature["sleep"][dailydata]["efficiency"])<=(int)(eachLine.sleep_max):
        return True
    else:
        return False
    
    
#Check to see if the given distance is in the range
def checkActivity(feature, eachLine):
    if (int)(feature["activities"][dailydata]["distance"])>=(int)(eachLine.activity_min) and (int)(feature["activities"][dailydata]["distance"])<=(int)(eachLine.activity_max):
        return True
    else:
        return False

#Check to see if the given age is in the range
def checkAge(feature, eachLine):
    if (int)(feature["userinfo"]["age"])>=(int)(eachLine.age_min) and (int)(feature["userinfo"]["age"])<=(int)(eachLine.age_max):
        return True
    else:
        return False



# TODO: find the following values from inputs
def preprocess(inputs):
    
    featureList=[]
    
    for eachLine in tableContent:
        bp_diastolic_min = ''
        bp_diastolic_max = ''
        heartbeat_min = ''
        heartbeat_max = ''
        sleep_min = ''
        sleep_max = ''
        bp_systolic_min = ''
        bp_systolic_max = ''
        activity_min = ''
        activity_max = ''
        age_min = ''
        age_max = ''
        
        toBeSelected=True
         
        print "-------- ----"
        print eachLine.bp_systolic_min
        print eachLine.bp_systolic_max
        print (inputs["bloodPressures"][dailydata]["systolic"]>=eachLine.bp_systolic_min and inputs["bloodPressures"][dailydata]["systolic"]<=eachLine.bp_systolic_max)or((eachLine.bp_systolic_min=='')and(eachLine.bp_systolic_max==''))
        print inputs["bloodPressures"][dailydata]["systolic"]
        print "------------"
        
        if (((eachLine.bp_systolic_min=='')and(eachLine.bp_systolic_max=='')) or checkSystolic(inputs, eachLine)):
            bp_systolic_min = eachLine.bp_systolic_min
            bp_systolic_max = eachLine.bp_systolic_max
        else:
            toBeSelected=False
            
        if (((eachLine.bp_diastolic_min=='')and(eachLine.bp_diastolic_max=='')) or checkDiastolic(inputs, eachLine)):
            bp_diastolic_min = eachLine.bp_diastolic_min
            bp_diastolic_max = eachLine.bp_diastolic_max
        else:
            toBeSelected=False
            
        if (((eachLine.heartbeat_min=='')and(eachLine.heartbeat_max=='')) or checkHeartBeats(inputs, eachLine)):
            heartbeat_min = eachLine.heartbeat_min
            heartbeat_max = eachLine.heartbeat_max
        else:
            toBeSelected=False
            
        if (((eachLine.sleep_min=='')and(eachLine.sleep_max=='')) or checkSleep(inputs, eachLine)):
            sleep_min = eachLine.sleep_min
            sleep_max = eachLine.sleep_max
        else:
            toBeSelected=False
            
        if (((eachLine.activity_min=='')and(eachLine.activity_max=='')) or checkActivity(inputs, eachLine)):
            activity_min = eachLine.activity_min
            activity_max = eachLine.activity_max
        else:
            toBeSelected=False
            
        if (((eachLine.age_min=='')and(eachLine.age_max=='')) or checkAge(inputs, eachLine)):
            age_min = eachLine.age_min
            age_max = eachLine.age_max
        else:
            toBeSelected=False
            
        if toBeSelected:
            oneFeature = Features(bp_systolic_min, bp_systolic_max, bp_diastolic_min, bp_diastolic_max,
            heartbeat_min, heartbeat_max, sleep_min, sleep_max, activity_min, activity_max,
            age_min, age_max)

            oneFeature.print_features()
            featureList.append(oneFeature)
            
    else:
        if(len(featureList)>0):
            return featureList[0]
        else:
            return None
    
    
#     # check user info
#     if inputs.has_key("userinfo"):
#         if inputs["userinfo"].has_key("age"):
#             if inputs["userinfo"]["age"]>=19 and inputs["userinfo"]["age"]<=64:
#                 age_min='19'
#                 age_max='64'
#                 #at this age, 30 mins at least
#                 if inputs.has_key("activities"):
#                     if inputs["activities"][dailydata]["distance"]<30:
#                         activity_min = '30'
#             if inputs["userinfo"]["age"]<=18:
#                 age_max='18'
#                 #at this age, 60 mins at least
#                 if inputs.has_key("activities"):
#                     if inputs["activities"][dailydata]["distance"]<60:
#                         activity_min = '60'
#             
#             # check heartbeats, age between 2 to 6
#             if inputs["userinfo"]["age"]>=2 and inputs["userinfo"]["age"]<=6 and inputs.has_key("heartBeats"):
#                 if inputs["heartBeats"][dailydata]["count"]>=121:
#                     heartbeat_min = '121'
#                 if inputs["heartBeats"][dailydata]["count"]>=75 and inputs["heartBeats"][dailydata]["count"]<121:
#                     heartbeat_min = '75'
#                     heartbeat_max = '120'
#                     
#             # check heartbeats, age between 7 to 17
#             if inputs["userinfo"]["age"]>=7 and inputs["userinfo"]["age"]<=17 and inputs.has_key("heartBeats"):
#                 if inputs["heartBeats"][dailydata]["count"]>=111:
#                     heartbeat_min = '111'
#                 if inputs["heartBeats"][dailydata]["count"]>=75 and inputs["heartBeats"][dailydata]["count"]<111:
#                     heartbeat_min = '75'
#                     heartbeat_max = '110'
#                     
#             # check heartbeats age above 18
#             if inputs["userinfo"]["age"]>=18 and inputs.has_key("heartBeats"):
#                 if inputs["heartBeats"][dailydata]["count"]>=101:
#                     heartbeat_min = '101'
#                 if inputs["heartBeats"][dailydata]["count"]>=60 and inputs["heartBeats"][dailydata]["count"]<101:
#                     heartbeat_min = '60'
#                     heartbeat_max = '100'
# 
#     #check bloodpressure
#     if inputs.has_key("bloodPressures"):
#         if inputs["bloodPressures"][dailydata].has_key("systolic") and inputs["bloodPressures"][dailydata].has_key("diastolic"):
#             if inputs["bloodPressures"][dailydata]["systolic"]<=119:
#                 bp_systolic_max = '119'
#             if inputs["bloodPressures"][dailydata]["systolic"]>=120 and inputs["bloodPressures"][dailydata]["systolic"]<=139:
#                 bp_systolic_min = '120'
#                 bp_systolic_max = '139'
#             if inputs["bloodPressures"][dailydata]["systolic"]>=140 and inputs["bloodPressures"][dailydata]["systolic"]<=159:
#                 bp_systolic_min = '140'
#                 bp_systolic_max = '159' 
#             if inputs["bloodPressures"][dailydata]["systolic"]>=160 and inputs["bloodPressures"][dailydata]["systolic"]<=179:
#                 bp_systolic_min = '160'
#                 bp_systolic_max = '179'
#             if inputs["bloodPressures"][dailydata]["systolic"]>=180:
#                 bp_systolic_min = '180'
#         
#             if inputs["bloodPressures"][dailydata]["diastolic"]<=79:
#                 bp_diastolic_max = '79'
#             if inputs["bloodPressures"][dailydata]["diastolic"]>=80 and inputs["bloodPressures"][dailydata]["diastolic"]<=89:
#                 bp_diastolic_min = '80'
#                 bp_diastolic_max = '89'
#             if inputs["bloodPressures"][dailydata]["diastolic"]>=90 and inputs["bloodPressures"][dailydata]["diastolic"]<=99:
#                 bp_diastolic_min = '90'
#                 bp_diastolic_max = '99' 
#             if inputs["bloodPressures"][dailydata]["diastolic"]>=100 and inputs["bloodPressures"][dailydata]["diastolic"]<=109:
#                 bp_diastolic_min = '100'
#                 bp_diastolic_max = '109'
#             if inputs["bloodPressures"][dailydata]["diastolic"]>=110:
#                 bp_diastolic_min = '110'
