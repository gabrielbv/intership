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

#Basic Operators
'''The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances 
of the variables x and y, respectively. You are also required to create a list called "big_list", which 
contains the variables "x" and "y", 10 times each, by concatenating the two lists you have created.'''
x = object()
y = object()

# change this code
x_list = [x]*10
y_list = [y]*10
big_list = x_list + y_list

print "x_list contains %d objects" % len(x_list)
print "y_list contains %d objects" % len(y_list)
print "big_list contains %d objects" % len(big_list)

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print "Almost there..."
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print "Great!"

  #String operators"
'''You will need to write a format string which prints out the data using the following syntax: Hello John Doe. 
Your current balance is 53.44$.'''

data = ("John", "Doe", 53.44)
format_string = "Hello"

print "Hello %s %s. Your current balance is %.2f$." % (data)

#Basic String Operations"
'''Try to fix the code to print out the correct information by changing the string.'''
s = "Strings are awesome!"

# Length should be 20
print "Length of s = %d" % len(s)

# First occurrence of "a" should be at index 8
print "The first occurrence of the letter a = %d" % s.index("a")

# Number of a's should be 2
print "a occurs %d times" % s.count("a")

# Slicing the string into bits
print "The first five characters are '%s'" % s[:5] # Start to 5
print "The next five characters are '%s'" % s[5:10] # 5 to 10
print "The twelfth character is '%s'" % s[12] # Just number 12

print "The last five characters are '%s'" % s[-5:] # 5th-from-last to end

# Convert everything to uppercase
print "String in uppercase: %s" % s.upper()

# Convert everything to lowercase
print "String in lowercase: %s" % s.lower()

# Check how a string starts
if s.startswith("Str"):
    print "String starts with 'Str'. Good!"

# Check how a string ends
if s.endswith("ome!"):
    print "String ends with 'ome!'. Good!"

# Split the string into three separate strings, 
# each containing only a word
print "Split the words of the string: %s" % s.split(" ")


