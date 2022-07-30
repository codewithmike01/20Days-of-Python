# We have json objects dict {"key" : "values"}
# we need the json module

import json
import xmltodict

file = open('sample.json','r')
content = file.read()


# print(content)

# We need to get the json file in dictionary format

d = json.loads(content)
# Loads convert to dictionary
# dumps convert to json format

print(d["database"]["host"])
# get Localhost

print(d["database"]["port"])

# Modifying the value but it wont change the value in the file
d["database"]["port"] = 4040
print(d)
file.close()


handle = open('sample.xml', 'r')
content = handle.read()
# print(content)

# converting to dictionary (Ordered dict)

d = xmltodict.parse(content)
# Converting back to xml use xmltodict.unparse()

print(d)
print(d['Result'])
