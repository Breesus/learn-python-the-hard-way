x = "there are %d types of people." % 10
# variable with string inside
# Defining decimal variable %d at end of string

binary = "binary"

do_not = "don't"

y = "Those who know %s and those who %s." % (binary, do_not)
# variable with strings inside
# defining multiple string variables %s

print x
# print varible x

print y
# print variable y

print "I said: %r." % x
# %r raw data for debugging
# calling variable x with %r defining variable at end of line
# variables that use other variables

print "I also said: '%s'." % y
# calling for string variable %s difining variable at end of line
# using string variable that has multiple variables in string

hilarious = False
# variable with boolean value   True or False
joke_evaluation = "Isn't that joke so funny?! %r"
# variable with string. %r in string not defined yet

print joke_evaluation % hilarious
# calling variable joke_evaluation
# calling for variable hilarious
# %r is defind after joke_evaluation
# %r stands for repr or a string containing a printable-
# representaion of an object

w = "This is the left side of..."
e = "a string with a right side"

print w + e
# prints without space

print w, e
# prints with space 
