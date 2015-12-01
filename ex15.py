from sys import argv
# use sys argv get the filename
script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

# let user input filename by using raw_input(">")
print "Type the filename again:"
file_again = raw_input(">")
txt_again = open(file_again)
print txt_again.read()
