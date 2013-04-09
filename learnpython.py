#First Exercise

print "Hello, World!"

#Variables and Types
'''The target of this exercise is to create a string, an integer, and a floating point number. 
The string should be named mystring and should contain the word "hello". The floating point number 
should be named myfloat and should contain the number 10, and the integer should be named myint 
and should contain the number 20. '''

mystring = "hello"
myfloat = float(10)
myint = 20

if mystring == "hello":
	print "String: %s" % mystring
if isinstance(myfloat, float) and myfloat == 10.0:
	print "Float: %d" % myfloat
if isinstance (myint, int) and myint == 0:
	print "Integer: %d" % myint


#Lists
'''In this exercise, you will need to add numbers and strings to the correct lists using the "append" 
list method. You must add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' 
to the strings variable.You will also have to fill in the variable second_name with the second name in 
the names list, using the brackets operator []. Note that the index is zero-based, so if you want to 
access the second item in the list, its index will be 1.'''

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")
second_name = names [1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)