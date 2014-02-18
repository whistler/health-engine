#!/usr/bin/env python

import os
import json
from flask import Flask
from flask import request

app = Flask(__name__)

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
    if not request.json or not 'steps' in request.json:
       abort(400)
    response = {
        'id': 0,
        'recommendation': 'You are in a good situation'
    }
    return json.dumps(response)

