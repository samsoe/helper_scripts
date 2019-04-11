import json

# load api key
file = '../Private/keys.json'
with open(file) as json_file:
    data = json.load(json_file)
    KEY = data['name_key']
