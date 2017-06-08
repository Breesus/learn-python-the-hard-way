# this one is like the scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
# def = define function, print_two = is name
# can name a function anything
# : ends line then indent 4 spaces after that
# line 3 unpacking arguments
# line 4 print arguments

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
# unpacking arguments on same line as define and name

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1
# function with one argument

# This one takes no arguments
def print_none():
    print "I got nothing."
# function with no arguments


print_two("zed","shaw")
# function name arguments
print_two_again("zed","shaw")
print_one("First!")
print_none()

# calling all 4 functions
