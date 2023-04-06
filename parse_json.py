import json
import os

# json = json.loads(open("C:/Users/user/pythonProject/why_python/eg.json").read())
# value = json['name']
# print(value)
# script to create absolute path variable

script_dir = os.path.dirname(__file__)
print("The script is located at:" + script_dir)
script_absolute_path = os.path.join(script_dir, 'eg.json')
print("The script path is:" + script_absolute_path)

# script parse
json = json.loads(open(script_absolute_path).read())
value = json['name']
print(value)

# loop through json keys and values, print them out
for key in json:
    print(key + ': ' + json[key])