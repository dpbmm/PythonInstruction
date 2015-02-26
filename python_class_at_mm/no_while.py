def lt(a, b):
    numbers = range(a, b)
    for number in numbers:
        print "At the top is %d" % number
        print "Number now:", numbers[a:number]
        print "At the bottom a is %d" % number
    print numbers

b = raw_input("Please enter a number: ")
lt (0, int(b))

