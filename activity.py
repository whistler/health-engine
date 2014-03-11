'''
Created on 01-Mar-2014

@author: GaneshKumar Munusamy
'''
def call_activity(input_act):
    if input_act['activities'][0]['duration'] < 20 and input_act['sleep'][0]['minutesAsleep']<360:
        if input_act['userinfo']['age'] > 60:
            return "608"
        else:
            return "609"
    else:
        return "600"
    