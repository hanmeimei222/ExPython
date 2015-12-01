from sys import argv

script, input_file = argv


def print_all(f):
    print f.read()


# the seek() function is dealing in bytes, not lines.
# It's going to the 0 byte (first byte) in the file
def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print line_count, f.readline()


current_file = open(input_file)
print "First let's print the whole file:\n"
print_all(current_file)
print "Now let's rewind, kind of like a tape."
rewind(current_file)
print "Let's print three lines:"

# The readline() function returns the \n that's
# in the file at the end of that line.So there
# are empty lines between the lines in the file
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
