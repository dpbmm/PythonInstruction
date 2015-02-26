x = raw_input('> ')
# Second way, with `elif`.

if x < 'l':
    print x, 'is less than "l".'
elif x == 'l':
    print x, 'is exactly "l".'
elif x == 'm':
    print "I hate m."
elif 'p' < x < 'y':
    print "In between Pee and Why."
else:
    print x, 'is not less than "l".'

