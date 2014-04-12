import json

try:
    input = json.load(open('tests/fixtures/input.json'))
    input9 = json.load(open('tests/fixtures/condition_9/input.json'))
    input53 = json.load(open('tests/fixtures/condition_53/input.json'))
    input72 = json.load(open('tests/fixtures/condition_72/input.json'))
except ValueError:
    print "could not read json file"