'''The target of this exercise is to create two lists called x_list and y_list,
 which contain 10 instances of the variables x and y, respectively. You are also 
 required to create a list called "big_list", which contains the variables "x" 
 and "y", 10 times each, by concatenating the two lists you have created.'''


object_1 = object()
object_2 = object()

first_list = [object_1]*10
second_list = [object_2]*10
big_list = first_list + second_list

print "first_list contains %d objects" % len(first_list)
print "second_list contains %d objects" % len(second_list)
print "big_list contains %d objects" %len(big_list)

if first_list.count(object_1) == 10 and second_list.count(object_2) == 10:
 	print "Almost there..."
if big_list.count(object_1) == 10 and big_list.count(object_2) ==10:
 	print "Great!"