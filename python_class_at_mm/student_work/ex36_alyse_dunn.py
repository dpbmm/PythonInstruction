# To run, in the terminal, enter python ex36.py Zipcar.txt new.txt

from sys import exit
from sys import argv
from os.path import exists

script, zipcar_file, to_file = argv

zip = open(zipcar_file)
zip_string = zip.read()

raffle = ['Ticket_A', 'Ticket_B', 'Ticket_C', 'Ticket_D'] 


# First option with a sub-option nested in it
def option_1():
	print """Oh no! Your car breaks down as soon as you get to the 
	bridge! What do you do now?
	1. Start looking for last-minute bus tickets to Massachusetts.
	2. Start looking for rental cars to drive to Massachusetts.
	3. Turn around and go back home."""
	
	dead_car = raw_input("Enter choice here: ")
	if dead_car == "1":
		print "You found no bus tickets, so you end up being forced to" 
		print "stay at home :-("
	elif dead_car == "2":
		print "You find an available zip car! Now you just need to"
		print "pick it up, but what was that address again?"
		print zip_string
		print "Did you know that file is %d bytes long?" % len(zip_string)
		print "Anyway, the zipcar got you to Massachusetts with enough" 
		print "time to catch the ferry, and you and the girls have"
		print "a fantastic weekend!"
		zip.close()
	else:
		print "Too bad; maybe you and the girls can try again next year."
	 

# Second option with a sub-option nested in it	
def option_2():
	print """You make it to Martha's Vineyard as expected, but when you  
	get there, you realize that you REALLY need some kind of  
	transportation in order to successfully navigate the island. What do
	you do now?
	1. Rent bikes
	2. Enter a raffle to win a free rental car"""
	bikes = raw_input("Enter choice here: ")
	if bikes == "1":
		print "The bikes were a good bet; the rest of the trip goes off" 
		print "without a hitch!"
	elif bikes == "2":
		print """A little birdie told you that the ticket AT 3 (i.e.  
		cardinal number) is the winning raffle ticket. Review the list 
		below and enter the letter of the winning raffle ticket. Enter
		only the letter (no other text), in CAPS, (as opposed to lower 
		case)."""
		print raffle
		ticket = raw_input("Enter choice here: ")
		if ticket == "D":
			print "Congrats! You win the rental car, and it makes your" 
			print "trip that much better!!!"
		else:
			print "Wrong choice! Guess you'll have to tough it out for" 
			print "the rest of the trip..."
	else:
		print "? Guess you'll have to tough it out for the rest of"
		print "the trip..."
		
	
	
# Third option with a redirect at the end to option #2
def option_3():
	print """ You and the girls get to the bus station, but no one 
	remembers the number for the bus that you're supposed to take! 
	The number of the bus is your age + the year. What's that bus 
	number?"""
	Age = raw_input("Age: ")
	Year = raw_input("Year: ")
	print "Get ready to board bus number %r to Martha's Vineyard!" %(Age + Year)
	option_2()
	

# Fourth option with a redirect at the end to option #2
def option_4(): 
	print """This train ride is REALLY long, thank goodness you have your
	laptop! This gives you plenty of time to copy those files you've been
	meaning to copy. Let's do this now. 
	Copying %s to %s.""" % (zipcar_file, to_file)
	open_file = open(zipcar_file).read()
	new_file = open(to_file, 'w').write(open_file)
	print "Done! Open the new file just to make sure it has your" 
	print "zipcar deets."
	new = open(to_file).read()
	print new 
	print "Great! Before you know it,"
	option_2()
	



# Main  function
def main():
	print """You and the girls want to go to Martha's Vineyard for Labor 
	Day Weekend. You have several options for how to get there. You can:
	1. Drive to to Massachusetts, and then take a short ferry to 
	Martha's Vineyard. If you do this, then you'll have a car when 
	you're at Martha's Vineyard.
	
	2. Take a long ferry straight from Manhattan to Martha's Vineyard.
	If you do this, then you won't have a car when you're at Martha's 
	Vineyard.
	
	3. Take a BUS to Massachusetts and then take a short ferry to 
	Martha's Vineyard. If you do this, then you won't have a car when 
	you're at Martha's Vineyard.
	
	4. Take a TRAIN to Massachusetts and then take a short ferry to 
	Martha's Vineyard. If you do this, then you won't have a car when 
	you're at Martha's Vineyard.
	
	Which of the four options would you like to take? Type 1, 2, 3, or 4."""
	
# Prompts the user to enter a value, and assigns that value to "travel"
	travel = raw_input("Enter choice here: ")

# Specifies which functions should run depending on the value 
# That the user entered for the raw input in line 41 above
	if travel == "1":
		option_1()
	elif travel == "2":
		option_2()
	elif travel == "3":
		option_3()
	elif travel == "4":
		option_4()
	else:
		print "You couldn't make a clear decision, so looks like you're"
		print "staying home!"
		
zip.close()			
main()