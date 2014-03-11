'''
Created on 25-Feb-2014

@author: GaneshKumar Munusamy
'''
def check_BMI_TTSleep(in_BMI_TTSleep):
    rec_array = []
    if in_BMI_TTSleep['BMI'] > 35 and in_BMI_TTSleep['sleep'][0]['TTSleep'] > 35:
        rec_array.append("601")
        if in_BMI_TTSleep['activities'][0]['duration'] < 20:
            rec_array.append("603")
        if in_BMI_TTSleep['userinfo']['age']>60:
            rec_array.append("604")
    if rec_array.__contains__("601") and in_BMI_TTSleep['userinfo']['gender'] == "Male":
        rec_array.append("602")
    if in_BMI_TTSleep['sleep'][0]['TTSleep'] < 6 and in_BMI_TTSleep['activities'][0]['duration'] < 20 and in_BMI_TTSleep['BMI'] > 35:
        rec_array.append("605")
    return rec_array

def with_HBP_AgeL(inputs):
    return "600"

def with_HBP_AgeM(inputs):
    rec_array = []
    rec_array.append("600")
    return rec_array

def with_HBP_AgeH(inputs):
    checkRec = []
    if inputs['BMI'] != "None" and inputs['sleep'][0]['TTSleep'] != "None":
        checkRec = check_BMI_TTSleep(inputs)
        return checkRec
    else:
        return 1