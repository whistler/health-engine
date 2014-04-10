import post_processor
import pandas
import json
import math

table = pandas.read_csv("/home/swami/Desktop/PostProcessor.csv")

def read_recomendations(ppfeatures):
    
     recommendations = []
     for recommendation in table.iterrows():
         #print "type of recommendation %s"%type(recommendation)
         #print recommendation[1]['BPHigh']
         #print recommendation[0]
         if ppfeatures.get('BPHigh') == recommendation[1]['BPHigh'] and \
         ppfeatures.get('BPLow')== recommendation[1]['BPLow'] and \
         ppfeatures.get('HBHigh')== recommendation[1]['HBHigh'] and \
         ppfeatures.get('HBLow')==recommendation[1]['HBLow'] and \
         ppfeatures.get('SleepHigh')==recommendation[1]['SleepHigh'] and \
         ppfeatures.get('SleepLow')==recommendation[1]['SleepLow'] and \
         ppfeatures.get('ActivityHigh')==recommendation[1]['ActivityHigh'] and \
         ppfeatures.get('ActivityLow')==recommendation[1]['ActivityLow']:
            summary = {
                      'summary': recommendation[1]['Recommendation'],
                      }
     return summary
         
         
def convert_to_dict(recommendation):
    return dict(recommendation)
                       