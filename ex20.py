# Ex20.py: Functions and files
# import the argv function from the sys library
from sys import argv

# assign values to argv (specifically the script ie ex20.py and the file)
script, input_file = argv

# define a function to print an entire file
# pass f (file) as an argument
# read the entire file and print it all out
def print_all(f):
	print f.read()

# define a rewind function ie go back to the start of the file
# seek moves the internal file pointer to a specified point of the file; in this csse, the very beginning.
# so seek(0) is the first *byte*, not first line
def rewind(f):
	f.seek(0)

# function to print a single line - takes 2 args: the line count and the file
# readline function reads the line, not the entire file. looks for the \n so knows where the line ends 
# and a new one begins
def print_a_line(line_count, f):
	print line_count, f.readline()

# set var called current file
current_file = open(input_file)

print "First let's print the whole file:\n"

# print the entire file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# go back to the start of the file
rewind(current_file)

print "Let's print three lines:"

# declare current line number
# and print the line 
# stop at three lines
#  x = x + y is the same as x += y
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)



# current_line = current_line + 1
# print_a_line(current_line, current_file)

# current_line = current_line + 1
# print_a_line(current_line, current_file)