#!/usr/bin/env python

import os
import json
from flask import Flask
from flask import request

app = Flask(__name__)

#
recommendations = {203:'Prehypertention Symptoms found! Please check your BP again after 6 hrs.', 
                   318:'Sleep at least 8 hrs, take rest, your bones and joints needs extra care that have arthiritis problem'}

@app.route('/')
def recommend():
    print request
    response = {
        'id': 0,
        'recommendation': 'Hello, Welcome to our search engine!'
    }
    return json.dumps(response)

@app.route('/', methods = ['POST'])
def recommend_post():
    response = [];
    
    #sympton 0
    #Recomendation 0
    #redirect to internal api 0 
    
    #sympton 1
  
    #Recomendation 1
    #redirect to internal api 1
    
     #...
    
    #sympton n
    #Recomendation n
    if not request.json or not 'sleep' in request.json:
       abort(400);
       
    if int(request.json['sleep']) < 8:
       response.append({'id':318, 'recommendation': recommendations.get(318)})

    else:
        response.append({'id':0, 'recommendation':'Congratulations,You have a good sleep!'})
    return json.dumps(response[0])

