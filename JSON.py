'''he aim of this exercise is to print out the JSON string with key-value pair "Me" : 800 added to it.'''

import json
def add_employee(jsonSalaries, name, salary): #Exercise fix this function, so it adds the given name and salary pair to the json it returns
    jsonSalaries=json.loads(jsonSalaries)
    jsonSalaries[name] = salary
    jsonSalaries=json.dumps(jsonSalaries)
    
    return jsonSalaries 

#Test code - shouldn't need to be modified
originalJsonSalaries = '{"Alfred" : 300, "Jane" : 301 }'
newJsonSalaries = add_employee(originalJsonSalaries, "Me", 800)
print(newJsonSalaries)