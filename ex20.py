from sys import argv

script, input_file = argv

# create a function to display the text file
# f is the variable name for input_file
def print_all(f):
    print f.read()

# create a function to go to beginning of file
# i.e  byte 0
def rewind(f):
    f.seek(0)

# create a function to print one line,
# line_count is the line number we want to read
# f is name of file
# readline is a built-in function
def print_a_line(line_count, f):
    print line_count, f.readline()

# variable = open input_file
current_file = open(input_file)

print "First let's print the whole file:\n"

# Use function print_all
# with variable current_file
print_all(current_file)

print "Now lets rewind, kind of like a tape."

# Use function rewind to go back to beginning of file
rewind(current_file)

print "Let's print three lines:"

# Use function print_a_line to count one line at a time
# variable = current_line = line 1
current_line = 1
print_a_line(current_line, current_file)

# use function print_a_line to count one line at a time
# variable = currnet_line = line 2
# incrementing each time
current_line = current_line + 1
print_a_line(current_line, current_file)

# Using function print_a_line to count one line at a time
# variable = current_line = line 3
# incrementing again
current_line = current_line + 1
print_a_line(current_line, current_file)
