import json

try:
    input = json.load(open('tests/fixtures/input.json'))
except ValueError:
    print "could not read json file"