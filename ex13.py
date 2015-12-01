from sys import argv
# unpacks argv,run python like "python ex13.py 1 second 3th"
file_name, year, month = argv

print "The script is called:", file_name
print "Your first variable is:", year
print "Your second variable is:", month
# input() return int
day = input("what's the date today")
# raw_input() return str
# day = raw_input("what's the date today")
print "So today is %s-%02s-%02d" % (year, month, day)
