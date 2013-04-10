'''We have a class defined for vehicles. Create two new vehicles called MyCar1 and MyCar2. 
Set MyCar1 to be a red convertible worth $60,000 with a name of Fer, and MyCar2 to be a blue 
van named Jump worth $10,000.'''

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00 
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
#your code goes here
MyCar1 =Vehicle()
MyCar1.name="Fer"
MyCar1.kind="convertivle"
MyCar1.color="red"
MyCar1.value=60000
MyCar2 =Vehicle()
MyCar2.name="Jump"
MyCar2.kind="van"
MyCar2.color="blue"
MyCar2.value=10000

#checking code
print MyCar1.description()
print MyCar2.description()
