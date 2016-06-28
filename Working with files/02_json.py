#using .json (through demjson)

import demjson

#encoding json
data=[{'a':1, 'b':2, 'c':3, 'd':4, 'e':5}]
json=demjson.encode(data)
print(json)

#decoding json
json1='{"a":1,"b":2,"c":3,"d":4,"e":5}';
text=demjson.decode(json1)
print(text)
