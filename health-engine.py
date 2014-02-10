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
        'recommendation': 'Hello World!'
    }
    return json.dumps(response)