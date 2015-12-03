'''
# original exercise code
i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num
'''

'''
# exercise with for_loop and range()
def add_element(N,gap):
    numbers = []
    for i in range(0, N, gap):
        print "Adding %d to the list." % i
        numbers.append(i)

    return numbers
'''


# exercise with while_loop
def add_element(N, gap):
    i = 0
    numbers = []
    while i < N:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + gap
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers


N = 6
gap = 2
num = add_element(N, gap)
print "The numbers: "

for n in num:
    print n
