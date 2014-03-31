""" Takes inputs and extracts features that are useful for recommendations"""

from features import Features
import lookup_table
from datetime import datetime

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
    
#Check to see if the given sleep is in the range
def checkSleep(feature, eachLine):
    if (int)(feature["sleep"][dailydata]["efficiency"])>=(int)(eachLine.sleep_min) and (int)(feature["sleep"][dailydata]["efficiency"])<=(int)(eachLine.sleep_max):
        return True
    else:
        return False
    
#Check to see if the given activity is in the range
def checkActivity(feature, eachLine):
    if (int)(feature["activities"][dailydata]["duration"])>=(int)(eachLine.activity_min) and (int)(feature["activities"][dailydata]["duration"])<=(int)(eachLine.activity_max):
        return True
    else:
        return False
 
#Check to see if the given age is in the range
def checkAge(feature, eachLine):
    if (int)(feature["userinfo"]["age"])>=(int)(eachLine.age_min) and (int)(feature["userinfo"]["age"])<=(int)(eachLine.age_max):
        return True
    else:
        return False

#Get the array of Activities List
def getActivitiesList(feature):
    
    if not(feature.has_key("activities")):
        return []
    
    activitiesData = feature["activities"] 
    activitiesList=[]
    for i in range(len(activitiesData)):
        if (activitiesData[i].has_key("date") and activitiesData[i].has_key("duration")):
            activitiesList.append([datetime.strptime(activitiesData[i]["date"],"%Y-%m-%d"), activitiesData[i]["duration"]])
#     print activitiesList
    return activitiesList

#Get the array of Sleep List
def getSleepList(feature):
    
    if not(feature.has_key("sleep")):
        return []
    
    sleepData = feature["sleep"]
    sleepList=[]
    for i in range(len(sleepData)):
        if (sleepData[i].has_key("date") and sleepData[i].has_key("minutesAsleep")):
            sleepList.append([datetime.strptime(sleepData[i]["date"],"%Y-%m-%d"), sleepData[i]["minutesAsleep"]])
#     print sleepList
    return sleepList
 
#Get the array of HeartBeats List
def getHeartBeatsList(feature):
    
    if not(feature.has_key("heartBeats")):
        return []
    
    heartBeatsData = feature["heartBeats"]
    heartBeatsList=[]
    for i in range(len(heartBeatsData)):
        if (heartBeatsData[i].has_key("date") and heartBeatsData[i].has_key("count")):
            heartBeatsList.append([datetime.strptime(heartBeatsData[i]["date"],"%Y-%m-%d"), heartBeatsData[i]["count"]])
#     print heartBeatsList
    return heartBeatsList
 
#Get the array of BloodPressures List
def getBloodPressuresList(feature):
    
    if not(feature.has_key("bloodPressures")):
        return []
    
    bloodPressuresData = feature["bloodPressures"]
    bloodPressuresList=[]
    for i in range(len(bloodPressuresData)):
        if (bloodPressuresData[i].has_key("date") and bloodPressuresData[i].has_key("systolic") and bloodPressuresData[i].has_key("diastolic")):
            bloodPressuresList.append([datetime.strptime(bloodPressuresData[i]["date"],"%Y-%m-%d"), bloodPressuresData[i]["systolic"], bloodPressuresData[i]["diastolic"]])
#     print bloodPressuresList
    return bloodPressuresList
 
      
def evaluateActivities(activitiesList):
    min=60
    hour=60*60
    activitiesEvaluation=[]
    for i in range(len(activitiesList)):
        date=activitiesList[i][0]
        activities=activitiesList[i][1]
        if(activities>70*min and activities<=2*hour):
            activitiesEvaluation.append(0)
                
        elif(activities>60*min and activities<=70*min):
            activitiesEvaluation.append([date, -10])
        elif(activities>50*min and activities<=60):
            activitiesEvaluation.append([date, -20])
        elif(activities>40*min and activities<=50*min):
            activitiesEvaluation.append([date, -30])
        elif(activities>30*min and activities<=40*min):
            activitiesEvaluation.append([date, -40])
        elif(activities>20*min and activities<=30*min):
            activitiesEvaluation.append([date, -60])
        elif(activities>10*min and activities<=20*min):
            activitiesEvaluation.append([date, -80])
        elif(activities<=10*min):
            activitiesEvaluation.append([date, -100])
              

        elif(activities>2*hour and activities<=4*hour):
            activitiesEvaluation.append([date, 10])
        elif(activities>4*hour and activities<=6*hour):
            activitiesEvaluation.append([date, 20])
        elif(activities>6*hour and activities<=8*hour):
            activitiesEvaluation.append([date, 30])
        elif(activities>8*hour and activities<=12*hour):
            activitiesEvaluation.append([date, 40])
        elif(activities>12*hour and activities<=14*hour):
            activitiesEvaluation.append([date, 50])
        elif(activities>14*hour and activities<=16*hour):
            activitiesEvaluation.append([date, 60])
        elif(activities>16*hour and activities<=18*hour):
            activitiesEvaluation.append([date, 70])
        elif(activities>18*hour and activities<=20*hour):
            activitiesEvaluation.append([date, 80])
        elif(activities>20*hour and activities<=22*hour):
            activitiesEvaluation.append([date, 90])
        elif(activities>22*hour):
            activitiesEvaluation.append([date, 100])
            
#     print activitiesEvaluation
    return activitiesEvaluation
            
 
def evaluateSleep(sleepList):
    hour=60 
    sleepEvaluation=[]
    for i in range(len(sleepList)):
        date=sleepList[i][0]
        sleepTime=sleepList[i][1]
        if(sleepTime>6*hour and sleepTime<=8*hour):
            sleepEvaluation.append([date, 0])
        elif(sleepTime>5.5*hour and sleepTime<=6*hour):
            sleepEvaluation.append([date, -10])
        elif(sleepTime>4.5*hour and sleepTime<=5.5*hour):
            sleepEvaluation.append([date, -25])
        elif(sleepTime>3.5*hour and sleepTime<=4.5*hour):
            sleepEvaluation.append([date, -45])
        elif(sleepTime>2.5*hour and sleepTime<=3.5*hour):
            sleepEvaluation.append([date, -50])
        elif(sleepTime>2*hour and sleepTime<=2.5*hour):
            sleepEvaluation.append([date, -60])
        elif(sleepTime>1.5*hour and sleepTime<=2*hour):
            sleepEvaluation.append([date, -70])
        elif(sleepTime>1*hour and sleepTime<=1.5*hour):
            sleepEvaluation.append([date, -80])
        elif(sleepTime>0.5*hour and sleepTime<=1*hour):
            sleepEvaluation.append([date, -90])
        elif(sleepTime>0*hour and sleepTime<=0.5*hour):
            sleepEvaluation.append([date, -100])
            
        elif(sleepTime>8*hour and sleepTime<=10*hour):
            sleepEvaluation.append([date, 10])
        elif(sleepTime>10*hour and sleepTime<=12*hour):
            sleepEvaluation.append([date, 20])
        elif(sleepTime>12*hour and sleepTime<=14*hour):
            sleepEvaluation.append([date, 30])
        elif(sleepTime>14*hour and sleepTime<=16*hour):
            sleepEvaluation.append([date, 40])
        elif(sleepTime>16*hour and sleepTime<=18*hour):
            sleepEvaluation.append([date, 55])
        elif(sleepTime>18*hour and sleepTime<=20*hour):
            sleepEvaluation.append([date, 70])
        elif(sleepTime>20*hour and sleepTime<=22*hour):
            sleepEvaluation.append([date, 75])
        elif(sleepTime>22*hour and sleepTime<=24*hour):
            sleepEvaluation.append([date, 100])
             
#     print sleepEvaluation

    return sleepEvaluation
      
def evaluateHeartBeats(heartBeatsList):
    heartBeatsEvaluation=[]
    for i in range(len(heartBeatsList)):
        date=heartBeatsList[i][0]
        heartBeats=heartBeatsList[i][1]
        if(heartBeats>60 and heartBeats<=90):
            heartBeatsEvaluation.append([date, 0])
        elif(heartBeats>55 and heartBeats<=60):
            heartBeatsEvaluation.append([date, -10])
        elif(heartBeats>50 and heartBeats<=55):
            heartBeatsEvaluation.append([date, -20])
        elif(heartBeats>45 and heartBeats<=50):
            heartBeatsEvaluation.append([date, -30])
        elif(heartBeats>40 and heartBeats<=45):
            heartBeatsEvaluation.append([date, -50])
        elif(heartBeats>30 and heartBeats<=40):
            heartBeatsEvaluation.append([date, -70])
        elif(heartBeats>20 and heartBeats<=30):
            heartBeatsEvaluation.append([date, -80])
        elif(heartBeats>10 and heartBeats<=20):
            heartBeatsEvaluation.append([date, -90])
        elif(heartBeats<10):
            heartBeatsEvaluation.append([date, -100])
         
        
        elif(heartBeats>100 and heartBeats<=110):
            heartBeatsEvaluation.append([date, 10])
        elif(heartBeats>110 and heartBeats<=120):
            heartBeatsEvaluation.append([date, 20])
        elif(heartBeats>120 and heartBeats<=130):
            heartBeatsEvaluation.append([date, 30])
        elif(heartBeats>130 and heartBeats<=140):
            heartBeatsEvaluation.append([date, 40])
        elif(heartBeats>140 and heartBeats<=150):
            heartBeatsEvaluation.append([date, 50])
        elif(heartBeats>150 and heartBeats<=160):
            heartBeatsEvaluation.append([date, 60])
        elif(heartBeats>160 and heartBeats<=170):
            heartBeatsEvaluation.append([date, 80])
        elif(heartBeats>170 and heartBeats<=180):
            heartBeatsEvaluation.append([date, 90])
        elif(heartBeats>180):
            heartBeatsEvaluation.append([date, 100])
            
#     print heartBeatsEvaluation
    return heartBeatsEvaluation


def evaluateBloodPressures(bloodPressuresList):
    systolicEvaluation=[]
    diastolicEvaluation=[]
    overallEvaluation=[]
    for i in range(len(bloodPressuresList)):
        date=bloodPressuresList[i][0]
        systolic=bloodPressuresList[i][1]
        if(systolic>=10 and systolic<=120):
            systolicEvaluation.append([date, 0])
            
        elif(systolic<=10):
            systolicEvaluation.append([date, -100])
            
        elif(systolic>120 and systolic<=130):
            systolicEvaluation.append([date, 5])
        elif(systolic>130 and systolic<=140):
            systolicEvaluation.append([date, 15])
        elif(systolic>140 and systolic<=150):
            systolicEvaluation.append([date, 30])
        elif(systolic>150 and systolic<=160):
            systolicEvaluation.append([date, 45])
        elif(systolic>160 and systolic<=170):
            systolicEvaluation.append([date, 60]) 
        elif(systolic>170 and systolic<=180):
            systolicEvaluation.append([date, 80])
        elif(systolic>180):
            systolicEvaluation.append([date, 100])
        
        
    for i in range(len(bloodPressuresList)):
        date=bloodPressuresList[i][0]
        diastolic=bloodPressuresList[i][2]
        if(diastolic>=10 and diastolic<=120):
            diastolicEvaluation.append([date, 0])
            
        elif(systolic<=10):
            diastolicEvaluation.append([date, -100])
            
        elif(diastolic>120 and diastolic<=130):
            diastolicEvaluation.append([date, 5])
        elif(diastolic>130 and diastolic<=140):
            diastolicEvaluation.append([date, 15])
        elif(diastolic>140 and diastolic<=150):
            diastolicEvaluation.append([date, 30])
        elif(diastolic>150 and diastolic<=160):
            diastolicEvaluation.append([date, 45])
        elif(diastolic>160 and diastolic<=170):
            diastolicEvaluation.append([date, 60])
        elif(diastolic>170 and diastolic<=180):
            diastolicEvaluation.append([date, 80])
        elif(diastolic>180):
            diastolicEvaluation.append([date, 100])
            
    for i in range(len(diastolicEvaluation)):
        overallEvaluation.append([diastolicEvaluation[i][0], (diastolicEvaluation[i][1]+systolicEvaluation[i][1])/2])
    
#     print overallEvaluation
    return overallEvaluation 


def getAllLists(inputs):      
    bloodPressuresList = getBloodPressuresList(inputs)
    heartBeatsList = getHeartBeatsList(inputs)
    activitiesList = getActivitiesList(inputs)
    sleepList = getSleepList(inputs)
    bloodPressuresEvaluation = evaluateBloodPressures(bloodPressuresList)
    heartBeatsEvaluation = evaluateHeartBeats(heartBeatsList)
    activitiesEvaluation = evaluateActivities(activitiesList)
    sleepEvaluation = evaluateSleep(sleepList)
    
    return activitiesList, bloodPressuresList, heartBeatsList, sleepList, activitiesEvaluation, bloodPressuresEvaluation, heartBeatsEvaluation, sleepEvaluation


# TODO: find the following values from inputs
def preprocess(inputs):
    
    print '-------Sleep--------'
    sleepList=getSleepList(inputs)
    evaluateSleep(sleepList)
    print '-------Activities--------'
    activitiesList=getActivitiesList(inputs)
    evaluateActivities(activitiesList)
    print '-------Heart Beats--------'
    heartBeatsList=getHeartBeatsList(inputs)
    evaluateHeartBeats(heartBeatsList)
    print '-------Blood Pressure--------'
    bloodPressuresList=getBloodPressuresList(inputs)
    evaluateBloodPressures(bloodPressuresList)
     
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
         
#         print "-------- ----"
#         print eachLine.bp_systolic_min
#         print eachLine.bp_systolic_max
#         print (inputs["bloodPressures"][dailydata]["systolic"]>=eachLine.bp_systolic_min and inputs["bloodPressures"][dailydata]["systolic"]<=eachLine.bp_systolic_max)or((eachLine.bp_systolic_min=='')and(eachLine.bp_systolic_max==''))
#         print inputs["bloodPressures"][dailydata]["systolic"]
#         print "------------"
        
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
