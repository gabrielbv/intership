'''In this exercise, you will need to print an alphabetically sorted list of all functions in the re module, which contain the word find.'''

import re
list =[]
for function in dir(re):
    if re.match("find",function):
        list.append(function)
print list