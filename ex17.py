# you could put all this code on one line using-
# an  ;  after every line

from sys import argv
from os.path import exists
# import modules

script, from_file, to_file = argv
# argument variable

print "copying from %s to %s" % (from_file, to_file)
# print string with argv variables

# we could do these two on one line, how?
in_file = open(from_file)
# object/variable in_file = open file
indata = in_file.read()
# indata = read in_file

# how to do above in one line

# indata = open(from_file).read()
# if done this way you don't need in_file.close()-
# will cause an error if you use .close

print "The input data is %d bytes long" % len(indata)
# print string with variable
# len it takes string you pass and returns as number

print "does the output file exist? %r" % exists(to_file)
# print with variable in string
# exists import used = True/False
print "Ready, hit RETURN to continue, CTRL-C to abort."
# user question
raw_input()
# user data

out_file = open(to_file, 'w')
# variable/object = open to_file and write to it
out_file.write(indata)
# take the indata and write to_file

print "Alright all done."

out_file.close()
in_file.close()
# to close files
