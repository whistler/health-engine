'''
1xx activity
2xx blood pressure
3xx heart beat rate
4xx sleep

x0x less severe
x1x more

SCORE syntax [0357, monotonic, direction, fluctuation, result]

'''
ACTIVITY_INDEX = 0
BLOODPRESSURE_INDEX = 1
HEARTBEAT_INDEX = 2
SLEEP_INDEX = 3

PEROID = 0
MONOTINIC = 1
DIRECTION = 2
FLUCTUATION = 3
RESULT = 4

import preprocessor
import consecutive_analysis
import json

def getRecommendations(inputs):
    activitiesList, bloodPressuresList, heartBeatsList, sleepList, activitiesEvaluation, bloodPressuresEvaluation, heartBeatsEvaluation, sleepEvaluation = preprocessor.getAllLists(inputs)

    activitiesScores = consecutive_analysis.main_analysis(activitiesEvaluation, activitiesList)
    bloodPressuresScores = consecutive_analysis.main_analysis(bloodPressuresEvaluation, bloodPressuresList)
    heartBeatScores = consecutive_analysis.main_analysis(heartBeatsEvaluation, heartBeatsList)
    sleepScores = consecutive_analysis.main_analysis(sleepEvaluation, sleepList)

    print [x[1] for x in activitiesList]
    print [(x[1],x[2]) for x in bloodPressuresList]
    print [x[1] for x in heartBeatsList]
    print [x[1] for x in sleepList]
    
    print [x[1] for x in activitiesEvaluation]
    print [x[1] for x in bloodPressuresEvaluation]
    print [x[1] for x in heartBeatsEvaluation] 
    print [x[1] for x in sleepEvaluation] 

    print activitiesScores
    print bloodPressuresScores
    print heartBeatScores
    print sleepScores 
    
    recoms = []
    recoms.append(makeRecommendations(ACTIVITY_INDEX, activitiesScores, activitiesList, activitiesEvaluation))
    recoms.append(makeRecommendations(BLOODPRESSURE_INDEX, bloodPressuresScores, bloodPressuresList, bloodPressuresEvaluation))
    recoms.append(makeRecommendations(HEARTBEAT_INDEX, heartBeatScores, heartBeatsList, heartBeatsEvaluation))
    recoms.append(makeRecommendations(SLEEP_INDEX, sleepScores, sleepList, sleepEvaluation))
    
    return [recom for recom in recoms if (int(recom["id"]) % 100 != 0)]
#     return recoms
    
def makeRecommendations(index, score, list, evalue):
    fobj = file("db/recommendationTemplates.json")
    template = json.load(fobj)
    
    recom = {}
    recom["id"] = (index+1) * 100
    # massage the ids
    
    if score[DIRECTION] == 0:
        if index == ACTIVITY_INDEX or index == SLEEP_INDEX:
            recom["recommendation"] = template[index]["normal_template"]
        else :
            if score[MONOTINIC] == 0:
                recom["recommendation"] = template[index]["normal_template"]
            elif score[MONOTONIC] == 1:
                recom["recommendation"] = template[index]["increasing_template"] % makeTuple(score[PEROID],getMin(index, list),getMax(index, list))
                recom["id"] += 10;
            else :
                recom["recommendation"] = template[index]["decreasing_template"] % makeTuple(score[PEROID],getMax(index, list),getMin(index, list))
                recom["id"] += 10;
    elif score[DIRECTION] == 2:      
        recom["recommendation"] = template[index]["fluctuating_template"] % (score[PEROID])
        recom["id"] += int(abs(score[RESULT]));

    elif score[DIRECTION] == 1:
        maxEval = getMax(0, evalue)[0]
        minEval = getMin(0, evalue)[0]
        if maxEval - minEval > 40 and score[FLUCTUATION]:
            recom["recommendation"] = template[index]["fluctuating_template"] % (score[PEROID])
            recom["id"] += int(abs(score[RESULT]));
        else:
            if minEval > 40:
                recom["recommendation"] = template[index]["consecutive_positive_template"] % makeTuple(score[PEROID], getMin(index, list))
                recom["id"] += int(abs(score[RESULT]));
            else:
                recom["recommendation"] = template[index]["consecutive_positive_avg_template"] % makeTuple(score[PEROID], getAvg(index, list))
                recom["id"] += int(abs(score[RESULT]));
    else: 
        maxEval = getMax(0, evalue)[0]
        minEval = getMin(0, evalue)[0]
        if maxEval - minEval > 40 and score[FLUCTUATION]:
            recom["recommendation"] = template[index]["fluctuating_template"] % (score[PEROID])
            recom["id"] += int(abs(score[RESULT]));

        else:
            if maxEval < -40:
                recom["recommendation"] = template[index]["consecutive_negative_template"] % makeTuple(score[PEROID], getMax(index, list))
                recom["id"] += int(abs(score[RESULT]));
            else:
                recom["recommendation"] = template[index]["consecutive_negative_avg_template"] % makeTuple(score[PEROID], getAvg(index, list))        
                recom["id"] += int(abs(score[RESULT]));
                                            
    recom["url"] = template[index]["url_template"]      
    return recom    
            
def getMin(index, list):
    if index == BLOODPRESSURE_INDEX:
        data_list = [[x[1:2]] for x in list] 
        return [min(data_list)[0], min(data_list)[1]]
    else:
        data_list = [x[1] for x in list]
        return [min(data_list)]            
            
def getMax(index, list):
    if index == BLOODPRESSURE_INDEX:
        data_list = [[x[1:2]] for x in list] 
        return [max(data_list)[0], max(data_list)[1]]
    else:
        data_list = [x[1] for x in list]
        return [max(data_list)]
    
def getAvg(index, list):
    if index == BLOODPRESSURE_INDEX:
        data_list1 = [x[1] for x in list] 
        data_list2 = [x[2] for x in list] 
        
        return [int(float(sum(data_list1))/len(data_list1)), int(float(sum(data_list2))/len(data_list2))]
    else:
        data_list = [x[1] for x in list]
        return [float(sum(data_list))/len(data_list)]
    
    
def makeTuple(period, list1, list2=None):
    temp = list1
    temp.insert(0, period)
    if list2 == None:
        return tuple(temp)
    else:
        for x in list2:
            temp.append(x)
        return tuple(temp)
    