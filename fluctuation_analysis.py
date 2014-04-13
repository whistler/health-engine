import datetime

def analyze_fluctuation(sorted_score_list):
    
    l = len(sorted_score_list)
    
    total = 0
    last_scope = 0
    
    for i in range(l):
        score = sorted_score_list[i]
        
        scope = convert_score_to_scope(score)
        if scope != last_scope:
            total = total + 1
        last_scope = scope
    
    if total > 0:     
        total = total - 1
    
    return total
    
def convert_score_to_scope(score):
    if (score < -75):
        return 1
    elif (score < -50):
        return 2
    elif (score < -25):
        return 3
    elif (score < 0):
        return 4
    elif (score == 0):
        return 5
    elif (score < 25):
        return 6
    elif (score < 50):
        return 7
    elif (score < 75):
        return 8
    else:
        return 9
