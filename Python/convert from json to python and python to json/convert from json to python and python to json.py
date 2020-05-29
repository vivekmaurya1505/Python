"""
if you have a JSON string , you can parse it by using the json.loads() method.
"""

import json
#some JSON:
x = '{"name":"vivek","age":23,"city":"Pune"}'

#parse x:
y = json.loads(x)

#the result is a python ditionary:

print(y["name"])


"""
if you have a Python Object, you can convert it into a JSON string by using the json.dumps() method.
"""

import json

# a python object (dict):
x = {"name":"vivek",
     "age":23,
     "city":"Pune"
    }

#convert into JSON
y = json.dumps(x)

#the result is json string

print(y)
