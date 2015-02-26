print ("""
You run into a friend from college on the street on your way to the
laundromat.  She suggests that you two of you grab brunch together
around the corner to catch up.  This friend is known for
unpredictability and wild antics.

How do you respond?

1. Sure, let's grab brunch!
2. I was on my way to the laundromat, but let's catch up some other
   time!
3. Pretend that you have amnesia and walk away awkwardly.
""")

friend = raw_input (">>> ") 

if friend == "1":
	print "You find yourself at a dance club that happens to serve french toast."
	print "How do you proceed?"
	print "1. Befriend the go-go dancer"
	print "2. Take your leave." 
	
	club = raw_input (">> ")
	if club == "1":
		print "The go-go dancer scores you and your free mimosas!"
	elif club == "2":
		print "You go to finish your laundry, but the laundromat is closed"
	else:
		print "You spot your ex boyfriend out of the corner of your eye and"
		print "You make up an excuse to leave."
		
elif friend == "2":
	print """"You go to finish your laundry, but when you get there, you realize
	that you don't have any laundry detergent or quarters, so you turn around and 
	go back home. """
	
elif friend == "3":
	print "Your friend blasts you on Facebook the minute you reach the next block."
	
else:
	print """You stand making small talk for a bit longer and then you both go your
	separate ways."""
