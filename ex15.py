from sys import argv # module

script, filename = argv
# argv variable
txt = open(filename)
# variable with open command
# open command reads a text file with argument in ()
print "Here's your file %r:" % filename
# prints message with variable filename
print txt.read()
# prints variable txt the
# . = add command, the read command

# Same as above but this time calling
# file from in the script


print "Type the filename again:"
# print message
file_again = raw_input(">")
# variable = data from user
# change prompt to >
txt_again = open(file_again)
# variable = open file () = argument variable above
print txt_again.read()
# print variable
# txt_again = variable above
# . = command read file
txt.close
txt_again.close
# to close files
