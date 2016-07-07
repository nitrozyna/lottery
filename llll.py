from random import randint
randomnumbers = []
for y in range (0, 6):
    y = randint(1,50)
    randomnumbers.append(y)
    print(y)

randomnumbers1 = []
for z in range (0,6):

    try:
        number = int(raw_input("Choose six numbers and enter them one by one ffrom 1 to 49:"))
        if not (1 <= number <= 49):

    
            print "Invalid option, enter numbers form 1 to 49"
            number = raw_input
        else:
            randomnumbers1.append(number)
            print "Your number is", number

    for i in randomnumbers:
        for j in randomnumbers1:
            if i == j:
                print "number %i matches %i" % (i, j)

