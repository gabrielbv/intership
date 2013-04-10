'''Handle all the exceptions!'''
actor = {"name": "John Cleese", "rank": "awesome"}

#Function to modify, should return the last name of the actor - think back to previous lessons for how to get it
def get_last_name():
    try:
        return actor["last_name"]
    except:
        actor_name = actor["name"]
        first_name,last_name = actor_name.split()
        return last_name

#Test code
get_last_name()
print "All exceptions caught! Good job!"
print "The actor's last name is %s" % get_last_name()