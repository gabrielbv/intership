'''Make a decorator factory which returns a decorator that decorates functions with one argument. 
The factory should take one argument, a type, and then returns a decorator that makes function should 
check if the input is the correct type. If it is wrong, it should print "Bad Type". (In reality, it 
    should raise an error, but error raising isn't in this tutorial.) Look at the tutorial code and 
expected output to see what it is if you are confused (I know I would be.) Using isintance(object, 
    type_of_object) or type(object) might help.'''

def Type_Check(correct_type):
    def check(old_function):
        def new_function(var):
            if isinstance (var,correct_type):
                return old_function(var)
            else:
                print "Bad Type"
        return new_function
    return check
      

@Type_Check(int)
def Times2(num):
    return num*2

print Times2(2)
Times2('Not A Number')

@Type_Check(str)
def First_Letter(word):
    return word[0]

print First_Letter('Hello World')
First_Letter(['Not', 'A', 'String'])