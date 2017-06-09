#API stands for application programing interface.
#Accessing an API is no different from accessing a web page via a URL, it's just the information is sent back via JSON
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
import JSON
jsonDataAsPythonValue = json.loads(stringOfJsonData)
jsonDataAsPythonValue
#Note that JSON strings always use double quotes.

#This is for converting python data into JSON values.
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie',
'felineIQ': None}
import json
stringOfJsonData = json.dumps(pythonValue)
#The value can only be one of the following basic Python data types:
#dictionary, list, integer, float, string, boolean, or none.
