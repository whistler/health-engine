import json
from flask import Flask
from flask import request

app = Flask("health-engine")

def run():
    #app.debug = False
    app.run(host='0.0.0.0')

@app.route("/")
def recommend():
    print request
    response = {
        'id': 0,
        'recommendation': 'Hello World!'
    }
    return json.dumps(response)