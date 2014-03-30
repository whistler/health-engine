MONOTONIC_INCREASING = 1
MONOTONIC_DECREASING = 1
MONOTONIC_NONE = 0

DIRECTION_POSITIVE = 1
DIRECTION_NEGATIVE = -1
DIRECTION_NONE = 0
DIRECTION_BOTH = 2

NO_RESULT = -1

import datetime

def main_analysis(score_list):
    sorted_score_list = sort_list_bytime(score_list)
    
    threeday_score = threeday_consecutive_score(sorted_score_list)
    fiveday_score = fiveday_consecutive_score(sorted_score_list)
    sevenday_score = sevenday_consecutive_score(sorted_score_list)
    
    worst_score = max(threeday_score, fiveday_score, sevenday_score)
    
    if worst_score == NO_RESULT:
        return (0, MONOTONIC_NONE, DIRECTION_NONE, False, NO_RESULT)
    
    if sevenday_score == worst_score:
        monotonic = sevenday_consecutive_monotonic(sorted_score_list)
        direction = sevenday_consecutive_direction(sorted_score_list)
        fluctuation = sevenday_consecutive_fluctuation(sorted_score_list)
        return [7, monotonic, direction, fluctuation, worst_score]
    elif fiveday_score == worst_score:
        monotonic = fiveday_consecutive_monotonic(sorted_score_list)
        direction = fiveday_consecutive_direction(sorted_score_list)
        fluctuation = fiveday_consecutive_fluctuation(sorted_score_list)
        return [5, monotonic, direction, fluctuation, worst_score]
    else:
        monotonic = threeday_consecutive_monotonic(sorted_score_list)
        direction = threeday_consecutive_direction(sorted_score_list)
        fluctuation = threeday_consecutive_fluctuation(sorted_score_list)
        return [3, monotonic, direction, fluctuation, worst_score]
    
def sort_list_bytime(score_list):
    return sorted(score_list, key=lambda data: data[0], reverse=True)

def threeday_consecutive_score(sorted_score_list):
    
    l = len(sorted_score_list)
    if l < 2:
        return NO_RESULT
    
    date_list = [x[0] for x in sorted_score_list]
    score_only_list = [x[1] for x in sorted_score_list]
        
    today = sorted_score_list[0][0]
    prev_day_list = [today - datetime.timedelta(days = i) for i in range(3)]
    
    if date_list[1] == prev_day_list[2]:
        avg_score = sum(score_only_list[0:2]) / 2.0
    elif date_list[1] == prev_day_list[1]:
        if l >= 3 and date_list[2] == prev_day_list[2]:
            avg_score = sum(score_only_list[0:3]) / 3.0
        else:
            avg_score = sum(score_only_list[0:2]) / 2.0
    else:
        return NO_RESULT
    
    return avg_score

def fiveday_consecutive_score (sorted_score_list):
    
    l = len(sorted_score_list)
    if l < 4:
        return NO_RESULT
    
    date_list = [x[0] for x in sorted_score_list]
    score_only_list = [x[1] for x in sorted_score_list]
        
    today = sorted_score_list[0][0]
    prev_day_list = [today - datetime.timedelta(days = i) for i in range(5)]
    
    if date_list[3] == prev_day_list[4]:
        avg_score = sum(score_only_list[0:4]) / 4.0
    elif date_list[3] == prev_day_list[3]:
        if l >= 5 and date_list[4] == prev_day_list[4]:
            avg_score = sum(score_only_list[0:5]) / 5.0
        else:
            avg_score = sum(score_only_list[0:4]) / 4.0
    else:
        return NO_RESULT
    
    return avg_score

def sevenday_consecutive_score(sorted_score_list):
    
    l = len(sorted_score_list)
    if l < 6:
        return NO_RESULT
    
    date_list = [x[0] for x in sorted_score_list]
    score_only_list = [x[1] for x in sorted_score_list]
        
    today = sorted_score_list[0][0]
    prev_day_list = [today - datetime.timedelta(days = i) for i in range(7)]
    
    if date_list[5] == prev_day_list[6]:
        avg_score = sum(score_only_list[0:6]) / 6.0
    elif date_list[5] == prev_day_list[5]:
        if l >= 7 and date_list[6] == prev_day_list[6]:
            avg_score = sum(score_only_list[0:7]) / 7.0
        else:
            avg_score = sum(score_only_list[0:6]) / 6.0
    else:
        return NO_RESULT
    
    return avg_score

def threeday_consecutive_monotonic(sorted_score_list):
    
    date_list = [x[0] for x in sorted_score_list]
    score_only_list = [x[1] for x in sorted_score_list]
    
    today = sorted_score_list[0][0]
    prev_day_list = [today - datetime.timedelta(days = i) for i in range(3)]
    
    if len(sorted_score_list) >= 3 and date_list[2] == prev_day_list[2]:
        size = 3
    else:
        size = 2
    
    monotonic = MONOTONIC_NONE
    
    for x in range(1, size):
        if score_only_list[x] > score_only_list[x-1]:
            if monotonic == MONOTONIC_NONE:
                monotonic = MONOTONIC_INCREASING
            elif monotonic == MONOTONIC_DECREASING:
                return MONOTONIC_NONE
        elif score_only_list[x] < score_only_list[x-1]:
            if monotonic == MONOTONIC_NONE:
                monotonic = MONOTONIC_DECREASING
            elif monotonic == MONOTONIC_INCREASING:
                return MONOTONIC_NONE
        else:
            return MONOTONIC_NONE
    
    return monotonic

def fiveday_consecutive_monotonic(sorted_score_list):
    
    date_list = [x[0] for x in sorted_score_list]
    score_only_list = [x[1] for x in sorted_score_list]
    
    today = sorted_score_list[0][0]
    prev_day_list = [today - datetime.timedelta(days = i) for i in range(5)]
    
    if len(sorted_score_list) >= 5 and date_list[4] == prev_day_list[4]:
        size = 5
    else:
        size = 4
    
    monotonic = MONOTONIC_NONE
    
    for x in range(1, size):
        if score_only_list[x] > score_only_list[x-1]:
            if monotonic == MONOTONIC_NONE:
                monotonic = MONOTONIC_INCREASING
            elif monotonic == MONOTONIC_DECREASING:
                return MONOTONIC_NONE
        elif score_only_list[x] < score_only_list[x-1]:
            if monotonic == MONOTONIC_NONE:
                monotonic = MONOTONIC_DECREASING
            elif monotonic == MONOTONIC_INCREASING:
                return MONOTONIC_NONE
        else:
            return MONOTONIC_NONE
    
    return monotonic
    
def sevenday_consecutive_monotonic(sorted_score_list):
    
    date_list = [x[0] for x in sorted_score_list]
    score_only_list = [x[1] for x in sorted_score_list]
    
    today = sorted_score_list[0][0]
    prev_day_list = [today - datetime.timedelta(days = i) for i in range(7)]
    
    if len(sorted_score_list) >= 7 and date_list[6] == prev_day_list[6]:
        size = 7
    else:
        size = 6
    
    monotonic = MONOTONIC_NONE
    
    for x in range(1, size):
        if score_only_list[x] > score_only_list[x-1]:
            if monotonic == MONOTONIC_NONE:
                monotonic = MONOTONIC_INCREASING
            elif monotonic == MONOTONIC_DECREASING:
                return MONOTONIC_NONE
        elif score_only_list[x] < score_only_list[x-1]:
            if monotonic == MONOTONIC_NONE:
                monotonic = MONOTONIC_DECREASING
            elif monotonic == MONOTONIC_INCREASING:
                return MONOTONIC_NONE
        else:
            return MONOTONIC_NONE
    
    return monotonic
    
def threeday_consecutive_direction(sorted_score_list):
    
    date_list = [x[0] for x in sorted_score_list]
    score_only_list = [x[1] for x in sorted_score_list]
    
    today = sorted_score_list[0][0]
    prev_day_list = [today - datetime.timedelta(days = i) for i in range(3)]
    
    if len(sorted_score_list) >= 3 and date_list[2] == prev_day_list[2]:
        size = 3
    else:
        size = 2
        
    direction = DIRECTION_NONE
    
    for x in range(size):
        if score_only_list[x] > 0:
            if direction == DIRECTION_NONE:
                direction = DIRECTION_POSITIVE
            elif direction == DIRECTION_NEGATIVE:
                direction = DIRECTION_BOTH
        elif score_only_list[x] < 0:
            if direction == DIRECTION_NONE:
                direction = DIRECTION_NEGATIVE
            elif direction == DIRECTION_POSITIVE:
                direction = DIRECTION_BOTH
    
    return direction
    
def fiveday_consecutive_direction(sorted_score_list):
    
    date_list = [x[0] for x in sorted_score_list]
    score_only_list = [x[1] for x in sorted_score_list]
    
    today = sorted_score_list[0][0]
    prev_day_list = [today - datetime.timedelta(days = i) for i in range(5)]
    
    if len(sorted_score_list) >= 5 and date_list[4] == prev_day_list[4]:
        size = 5
    else:
        size = 4
        
    direction = DIRECTION_NONE
    
    for x in range(size):
        if score_only_list[x] > 0:
            if direction == DIRECTION_NONE:
                direction = DIRECTION_POSITIVE
            elif direction == DIRECTION_NEGATIVE:
                direction = DIRECTION_BOTH
        elif score_only_list[x] < 0:
            if direction == DIRECTION_NONE:
                direction = DIRECTION_NEGATIVE
            elif direction == DIRECTION_POSITIVE:
                direction = DIRECTION_BOTH
    
    return direction    

def sevenday_consecutive_direction(sorted_score_list):
    
    date_list = [x[0] for x in sorted_score_list]
    score_only_list = [x[1] for x in sorted_score_list]
    
    today = sorted_score_list[0][0]
    prev_day_list = [today - datetime.timedelta(days = i) for i in range(7)]
    
    if len(sorted_score_list) >= 7 and date_list[6] == prev_day_list[6]:
        size = 7
    else:
        size = 6
        
    direction = DIRECTION_NONE
    
    for x in range(size):
        if score_only_list[x] > 0:
            if direction == DIRECTION_NONE:
                direction = DIRECTION_POSITIVE
            elif direction == DIRECTION_NEGATIVE:
                direction = DIRECTION_BOTH
        elif score_only_list[x] < 0:
            if direction == DIRECTION_NONE:
                direction = DIRECTION_NEGATIVE
            elif direction == DIRECTION_POSITIVE:
                direction = DIRECTION_BOTH
    
    return direction

def threeday_consecutive_fluctuation(sorted_score_list):
    
    date_list = [x[0] for x in sorted_score_list]
    score_only_list = [x[1] for x in sorted_score_list]
    
    today = sorted_score_list[0][0]
    prev_day_list = [today - datetime.timedelta(days = i) for i in range(3)]
    
    if len(sorted_score_list) >= 3 and date_list[2] == prev_day_list[2]:
        size = 3
    else:
        size = 2
    
    sign_change_count = 0
    
    for x in range(1, size):
        if score_only_list[x] == 0 and score_only_list[x-1] == 0:
            pass
        elif score_only_list[x] > 0 and score_only_list[x-1] > 0:
            pass
        elif score_only_list[x] < 0 and score_only_list[x-1] < 0:
            pass
        else:
            sign_change_count = sign_change_count + 1
    
    if sign_change_count >= 2:
        return True
    else:
        return False

def fiveday_consecutive_fluctuation(sorted_score_list):
    
    date_list = [x[0] for x in sorted_score_list]
    score_only_list = [x[1] for x in sorted_score_list]
    
    today = sorted_score_list[0][0]
    prev_day_list = [today - datetime.timedelta(days = i) for i in range(5)]
    
    if len(sorted_score_list) >= 5 and date_list[4] == prev_day_list[4]:
        size = 5
    else:
        size = 4
    
    sign_change_count = 0
    
    for x in range(1, size):
        if score_only_list[x] == 0 and score_only_list[x-1] == 0:
            pass
        elif score_only_list[x] > 0 and score_only_list[x-1] > 0:
            pass
        elif score_only_list[x] < 0 and score_only_list[x-1] < 0:
            pass
        else:
            sign_change_count = sign_change_count + 1
    
    if sign_change_count >= 3:
        return True
    else:
        return False

def sevenday_consecutive_fluctuation(sorted_score_list):
    
    date_list = [x[0] for x in sorted_score_list]
    score_only_list = [x[1] for x in sorted_score_list]
    
    today = sorted_score_list[0][0]
    prev_day_list = [today - datetime.timedelta(days = i) for i in range(7)]
    
    if len(sorted_score_list) >= 7 and date_list[4] == prev_day_list[6]:
        size = 7
    else:
        size = 6
    
    sign_change_count = 0
    
    for x in range(1, size):
        if score_only_list[x] == 0 and score_only_list[x-1] == 0:
            pass
        elif score_only_list[x] > 0 and score_only_list[x-1] > 0:
            pass
        elif score_only_list[x] < 0 and score_only_list[x-1] < 0:
            pass
        else:
            sign_change_count = sign_change_count + 1
    
    if sign_change_count >= 5:
        return True
    else:
        return False
        