BAD_SCORE = 60
VERY_BAD_SCORE = 50
EXTREMELY_BAD_SCORE = 30
NO_RESULT = 0

import random
import datetime

"""
Provide the previous consecutive three/five/seven day analysis

Input: 
data_list = [[datetime.date, Integer/Double], ...] for heartrate, activity, sleep
data_list = [[datetime.date, [Integer/Double, Integer/Double]], ...] for bloodpressures

Output:
BAD_SCORE
VERY_BAD_SCORE
EXTREMELY_BAD_SCORE
NO_RESULT: either in good condition or not enough data
"""


def heartrate_threeday_consecutive_analysis(data_list):
    sorted_data_list = sort_list_bytime(data_list)
    score_list = map(lambda data: [data[0], convert_heartrate_score(data[1])], sorted_data_list)
    severity = threeday_consecutive_analysis_helper(score_list)
    return severity
    
def bloodpressure_threeday_consecutive_analysis(data_list):
    sorted_data_list = sort_list_bytime(data_list)
    score_list = map(lambda data: [data[0], convert_heartrate_score(data[1][0], data[1][1])], sorted_data_list)
    severity = threeday_consecutive_analysis_helper(score_list)
    return severity
    
def activity_threeday_consecutive_analysis(data_list):
    sorted_data_list = sort_list_bytime(data_list)
    score_list = map(lambda data: [data[0], convert_heartrate_score(data[1])], sorted_data_list)
    severity = threeday_consecutive_analysis_helper(score_list)
    return severity

def sleep_threeday_consecutive_analysis(data_list):
    sorted_data_list = sort_list_bytime(data_list)
    score_list = map(lambda data: [data[0], convert_heartrate_score(data[1])], sorted_data_list)
    severity = threeday_consecutive_analysis_helper(score_list)
    return severity

def heartrate_fiveday_consecutive_analysis(data_list):
    sorted_data_list = sort_list_bytime(data_list)
    score_list = map(lambda data: [data[0], convert_heartrate_score(data[1])], sorted_data_list)
    severity = fiveday_consecutive_analysis_helper(score_list)
    return severity
    
def bloodpressure_fiveday_consecutive_analysis(data_list):
    sorted_data_list = sort_list_bytime(data_list)
    score_list = map(lambda data: [data[0], convert_heartrate_score(data[1][0], data[1][1])], sorted_data_list)
    severity = fiveday_consecutive_analysis_helper(score_list)
    return severity
    
def activity_fiveday_consecutive_analysis(data_list):
    sorted_data_list = sort_list_bytime(data_list)
    score_list = map(lambda data: [data[0], convert_heartrate_score(data[1])], sorted_data_list)
    severity = fiveday_consecutive_analysis_helper(score_list)
    return severity

def sleep_fiveday_consecutive_analysis(data_list):
    sorted_data_list = sort_list_bytime(data_list)
    score_list = map(lambda data: [data[0], convert_heartrate_score(data[1])], sorted_data_list)
    severity = fiveday_consecutive_analysis_helper(score_list)
    return severity    
    
def heartrate_sevenday_consecutive_analysis(data_list):
    sorted_data_list = sort_list_bytime(data_list)
    score_list = map(lambda data: [data[0], convert_heartrate_score(data[1])], sorted_data_list)
    severity = sevenday_consecutive_analysis_helper(score_list)
    return severity
    
def bloodpressure_sevenday_consecutive_analysis(data_list):
    sorted_data_list = sort_list_bytime(data_list)
    score_list = map(lambda data: [data[0], convert_heartrate_score(data[1][0], data[1][1])], sorted_data_list)
    severity = sevenday_consecutive_analysis_helper(score_list)
    return severity
    
def activity_sevenday_consecutive_analysis(data_list):
    sorted_data_list = sort_list_bytime(data_list)
    score_list = map(lambda data: [data[0], convert_heartrate_score(data[1])], sorted_data_list)
    severity = sevenday_consecutive_analysis_helper(score_list)
    return severity

def sleep_sevenday_consecutive_analysis(data_list):
    sorted_data_list = sort_list_bytime(data_list)
    score_list = map(lambda data: [data[0], convert_heartrate_score(data[1])], sorted_data_list)
    severity = sevenday_consecutive_analysis_helper(score_list)
    return severity    

# Compute the previous three day analysis
# Input: A sorted list of date-score pairs
# Output: An integer that represents status
# Notes: Dates in between may be missing
# If a date in between missing, take average, if missing two days, return NO_RESULT
# If date in between or end missing, take average of scores of neighbouring dates
# If no date missing: take the max number, if the max number >= 60 -> No result
# If the max number between an interval [), take the upper bound
def threeday_consecutive_analysis_helper(score_list):
    
    l = len(score_list)
    if l < 2:
        return NO_RESULT
    
    date_list = [x[0] for x in score_list]
    score_only_list = [x[1] for x in score_list]
        
    today = score_list[0][0]
    prev_day_list = [today - datetime.timedelta(days = i) for i in range(3)]
    
    if date_list[1] == prev_day_list[2]:
        # one day is missing, but not the prev_day_2
        # no need to interpolate as the missing day cannot be the max anyway
        max_score = max(score_only_list[0:2])
    elif date_list[1] == prev_day_list[1]:
        if l >= 3 and date_list[2] == prev_day_list[2]:
            # no day missing
            max_score = max(score_only_list[0:3])
        elif l >= 3 and date_list[2] != prev_day_list[2]:
            # prev_day_2 missing and interpolate it as average of scores of neighbouring dates
            interpolated_score = (score_only_list[1] + score_only_list[2]) / 2.0
            max_score = max(max(score_only_list[0:2]), interpolated_score)
        else:
            # length of the list = 2
            max_score = max(score_only_list[0:2])
    else:
        # more than one days missing
        return NO_RESULT
    
    return score_calculation_helper(max_score)

# Compute the previous five day analysis
# Input: A sorted list of date-score pairs
# Output: An integer that represents status
# Notes: Dates in between may be missing
# If a date in between missing, take average, if missing two days, return NO_RESULT
# If date in between or end missing, take average of scores of neighbouring dates
# If no date missing: take the max number, if the max number >= 60 -> No result
# If the max number between an interval [), take the upper bound
def fiveday_consecutive_analysis_helper(score_list):
    
    l = len(score_list)
    if l < 4:
        return NO_RESULT
    
    date_list = [x[0] for x in score_list]
    score_only_list = [x[1] for x in score_list]
        
    today = score_list[0][0]
    prev_day_list = [today - datetime.timedelta(days = i) for i in range(5)]
    
    if date_list[3] == prev_day_list[4]:
        # one day is missing, but not the prev_day_4
        # no need to interpolate as the missing day cannot be the max anyway
        max_score = max(score_only_list[0:4])
    elif date_list[3] == prev_day_list[3]:
        if l >= 5 and date_list[4] == prev_day_list[4]:
            # no day missing
            max_score = max(score_only_list[0:5])
        elif l >= 5 and date_list[4] != prev_day_list[4]:
            # prev_day_4 missing and interpolate it as average of scores of neighbouring dates
            interpolated_score = (score_only_list[3] + score_only_list[4]) / 2.0
            max_score = max(max(score_only_list[0:4]), interpolated_score)
        else:
            # length of the list = 4
            max_score = max(score_only_list[0:4])
    else:
        # more than one days missing
        return NO_RESULT
    
    return score_calculation_helper(max_score)

# Compute the previous seven day analysis
# Input: A sorted list of date-score pairs
# Output: An integer that represents status
# Notes: Dates in between may be missing
# If a date in between missing, take average, if missing two days, return NO_RESULT
# If date in between or end missing, take average of scores of neighbouring dates
# If no date missing: take the max number, if the max number >= 60 -> No result
# If the max number between an interval [), take the upper bound
def sevenday_consecutive_analysis_helper(score_list):
    
    l = len(score_list)
    if l < 6:
        return NO_RESULT
    
    date_list = [x[0] for x in score_list]
    score_only_list = [x[1] for x in score_list]
        
    today = score_list[0][0]
    prev_day_list = [today - datetime.timedelta(days = i) for i in range(7)]
    
    if date_list[5] == prev_day_list[6]:
        # one day is missing, but not the prev_day_6
        # no need to interpolate as the missing day cannot be the max anyway
        max_score = max(score_only_list[0:6])
    elif date_list[5] == prev_day_list[5]:
        if l >= 7 and date_list[6] == prev_day_list[6]:
            # no day missing
            max_score = max(score_only_list[0:7])
        elif l >= 7 and date_list[6] != prev_day_list[6]:
            # prev_day_6 missing and interpolate it as average of scores of neighbouring dates
            interpolated_score = (score_only_list[5] + score_only_list[6]) / 2.0
            max_score = max(max(score_only_list[0:6]), interpolated_score)
        else:
            # length of the list = 6
            max_score = max(score_only_list[0:6])
    else:
        # more than one days missing
        return NO_RESULT
    
    return score_calculation_helper(max_score)

# Convert max score to level of severity
# Input: Integer represents the max score
# Output: An integer that represents status
def score_calculation_helper(max_score):
    if max_score >= BAD_SCORE:
        return NO_RESULT
    elif max_score > VERY_BAD_SCORE:
        return BAD_SCORE
    elif max_score > EXTREMELY_BAD_SCORE:
        return VERY_BAD_SCORE
    else:
        return EXTREMELY_BAD_SCORE
    
def convert_heartrate_score(heartrate):
    # TODO
    return random.randint(0, 100)

def convert_bloodpressure_score(dia, sys):
    # TODO
    return random.randint(0, 100)

def convert_activity_score(duration):
    # TODO
    return random.randint(0, 100)

def convert_sleep_score(duration):
    # TODO
    return random.randint(0, 100)

def sort_list_bytime(data_list):
    return sorted(data_list, key=lambda data: data[0], reverse=True)
    

