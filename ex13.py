from sys import argv # modules
# This is an import that adds functions to python
# argv is the argument variable that holds
# arguments you pass to python scrpt

script, first, second, third = argv
# this unpacks argv and assign it to these variables
# above in order left to right

print "the script is called:", script
print "Your first variable is:", first
print "Your second varible is:", second
print "Your third variable is:", third
# prints string with argv variables
