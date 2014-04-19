'''
Created on Apr 4, 2014

@author: haijun
1xx activity
2xx blood pressure
3xx heart beat rate
4xx sleep
'''

import csv
import random
import sys
import math

keys = {1:"AC", 2:"BP", 3:"HB", 4:"SL"}
directions = {1:"High", -1:"Low", 0 : "Fluctuation"}

def loadTips():
    tips = {}
    try:
        with open('db/tips.csv', 'rb') as infile:
            tips_file = csv.reader(infile)
            for row in tips_file:
                if row != []:
                    if row[0] in tips:
                        tips[row[0]][row[1]] = row[2:]
                    else:
                        tips[row[0]] = {row[1]:row[2:]}
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise 
    return tips


def addtips(conditions):
    tips = loadTips()
    recommendations = []
    for cond in conditions:
        recom = {}
#         cond["condition"] += random.choice(tips[keys[int(cond["id"])/100]][directions[int(cond["direction"])]])
        recom=cond
        del recom["direction"]
        recom["recommendation"] = recom.pop("condition")
        if math.isnan(float(recom['url'])):
            recom['url'] = ''
        recommendations.append(recom)    
    return recommendations
    
