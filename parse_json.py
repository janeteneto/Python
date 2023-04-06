import json

json = json.loads(open("C:/Users/user/pythonProject/why_python/eg.json").read())
value = json['name']
print(value)