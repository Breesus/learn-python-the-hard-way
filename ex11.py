print "How old are you?",
age = raw_input()
# comma prevents new line
# variable asking for data raw_input()
# You can put any kind of data in raw_input()

print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "so, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
# print string with variables inside-
# Calling variables at the end of string
