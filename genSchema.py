import genson
import json
import os

s = genson.Schema()

for root, dirs, files in os.walk('<path to /jsons>'):          #file path to jsons folder
  for file in files:
    if file.endswith('.json'):
      with open(root+"/"+file) as json_data:
        d = json.load(json_data)
        s.add_object(d)

print s.to_json()

schema_file = open('schema.json', 'w')
schema_file.write(s.to_json())
schema_file.close