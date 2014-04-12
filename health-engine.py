#!/usr/bin/env python

""" A Flask wrapper around the Recommender to create a simple web API endpoint """

import os
import json
from StringIO import StringIO
from flask import Flask
from flask import request
import recommender
import lookup_table

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def recommend():

     try:
         inputs = json.loads(request.data)
     except ValueError:
         return "Unable to parse input data", 400
          
     response = recommender.recommend(inputs)
     headers = {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods' : 'POST' } 
     return json.dumps(response), 201, headers

if __name__ == "__main__":
    app.run()
