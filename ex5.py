# assigning variables
my_name = 'Zed A Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print
print "Lets talk about %s." % my_name
# Put %s in string
# put % space variable name after string
# %s is string variable

print "He's %d inches tall." % my_height
# put %d in string
# Put % space variable name after string
# %d is a decimal variable
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
# For multiple varibales, put in parentheses
print "His teeth are usually %s depending on coffee" % my_teeth
print
print "If I add %d, %d, and %d I get %d." % (
my_age, my_height, my_weight, my_age + my_height + my_weight
)
# Doing math within varibles list
