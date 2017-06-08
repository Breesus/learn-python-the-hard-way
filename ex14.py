from sys import argv # modules

scrpit, user_name = argv
# argument variable
prompt = '> '
# changing prompt to > sign

print "Hi %s, I'm the %s scrpit." % (user_name, scrpit)
# print string with argv variables left to right

print "I'd like to ask you a few questions."

print "Do you like me %s?" % user_name
# print string with variable %s = user_name
# argv variable used
likes = raw_input(prompt)
# variable takes data from raw_input
# and prompts >

print "where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright so you said %r about liking me.
you live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
# print with """ quotes so you can type what you want
# variables inserted at the end of line 
