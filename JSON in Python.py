#JSON in Python
import python 
#some json 
x='{'name':'charaf','age':30,'city':'new York'}'
#parse x that is in json to python to work with the data in
y = json.loads(x)

#the result is a python dictionary 
print(y["age"])




#and to convert from python to json 
#a python object (dict)
X={
    'name':'amien',
    'age':30,
    'city':'New York',
}
#convert into json
Y=json.dumps(X)

#the result is a json string 
print(Y)

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))
# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))