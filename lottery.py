#from random import randint, shuffle

#def luckyNumbers(rangeLeft, rangeRight, size):
   # """ determines the lucky numbers which win the lottery! """
    #originalRange = range(rangeLeft, rangeRight)
    #shuffle(originalRange)
    #return originalRange[:size]

#randomnumbers = luckyNumbers(1, 49, 6)
import random
lotteryrandom = []
a = range(1,50)
for i in range(6):
    b = a[random.randint(0,len(a))]
    a.remove(b)
    print b
    lotteryrandom.append(b)

randomnumbers = []

for z in range (0,6):

    try:
        number = int(raw_input("Choose six numbers and enter them one by one from 1 to 49:"))
        if not (1 <= number <= 49):
            raise ValueError()
    except ValueError:
        print "Invalid option, enter numbers from 1 to 49"
        number = raw_input
    else:
        randomnumbers.append(number)
        print "Your number is", number


for i in lotteryrandom: 
    for z in randomnumbers:
        if i == z:
            print "number %i matches %i" % (i, z)



