import post_processor
import pandas
import json
import math

table = pandas.read_csv("db/PostProcessor.csv")

def read_recomendations(ppfeatures):
    
     recommendations = []
     for recommendation in table.iterrows():
         #print "type of recommendation %s"%type(recommendation)
         print recommendation[1]['BPFluct']
         #print recommendation[0]
         summary = {
                    'id':900,
                    'condition':'No post processor output',
                    'severity':0,
                    'url':'http:////'
                    }
         if ppfeatures.get('BPHigh') == recommendation[1]['BPHigh'] and \
         ppfeatures.get('BPFluct')== recommendation[1]['BPFluct'] and \
         ppfeatures.get('BPLow')== recommendation[1]['BPLow'] and \
         ppfeatures.get('HBHigh')== recommendation[1]['HBHigh'] and \
         ppfeatures.get('HBFluct')== recommendation[1]['HBFluct'] and \
         ppfeatures.get('HBLow')==recommendation[1]['HBLow'] and \
         ppfeatures.get('SleepHigh')==recommendation[1]['SleepHigh'] and \
         ppfeatures.get('SleepFluct')== recommendation[1]['SleepFluct'] and \
         ppfeatures.get('SleepLow')==recommendation[1]['SleepLow'] and \
         ppfeatures.get('ActivityHigh')==recommendation[1]['ActivityHigh'] and \
         ppfeatures.get('ActivityFluct')== recommendation[1]['ActivityFluct'] and \
         ppfeatures.get('ActivityLow')==recommendation[1]['ActivityLow'] and \
         ppfeatures.get('Insomnia')==recommendation[1]['Insomnia'] and \
         ppfeatures.get('Hypertension')==recommendation[1]['Hypertension'] and \
         ppfeatures.get('Diabetes')==recommendation[1]['Diabetes'] and \
         ppfeatures.get('Cardio')== recommendation[1]['Cardio']:
            summary = {
                       'id':recommendation[1]['ID'],
                       'condition': recommendation[1]['Recommendation'],
                       'severity':5,
                       'url':recommendation[1]['URL']
                      }
     print summary
     return summary
         
         
def convert_to_dict(recommendation):
    return dict(recommendation)
                       