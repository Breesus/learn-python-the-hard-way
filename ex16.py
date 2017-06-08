from sys import argv

scrpit, filename = argv
# arg variables
# name of scrpit
# name of file

print "We're going to erase %r." % filename
# print = string with variable
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that hit RETURN."
# user questions for data

raw_input("?")
# data from user
# prompt changed to ?

print "Opening the file..."
target = open(filename, 'w')
# target = variable/object
# open = open file
# w = write

print "Truncating the file.  Goodbye!"
target.truncate()
# truncate = delete contents of file

print "Now i'm going to ask you for these lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 2: ")
# raw_input = user data with
# changed prompt to line 1, 2, 3
print "I'm going to write these to a file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# target = variable/object
# . = command
# write = write to file
# \n = write new line

print "And finally, we close it."
target.close()
# close file

# w = write
# w+ = write and read
# a = append
# r+ = read and write
# r = read only default
# methods or functions for an object
