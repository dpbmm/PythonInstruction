#have $60k to spend which do I fix first (basement, patio, or by a new car)

from sys import exit

options = ["basement", "deck", "basement & deck", "save my money"] 

print """
I have $60k to spend to address a few things of my own.
This includes a list of things I can choose from.
I am not sure what to do.  Please help!
"""
	
for list in options:
    print "Select from any one of these options: %s" % options
	
def start():	
	choice = raw_input("Which one would you do first? ")

	if choice.lower() == "basement":
		fix_basement()
	elif choice.lower() == "deck":
		deck_patio()
	elif choice.lower() == "basement and deck":
		do_both()
	else:
		save_money("save my money.")

		
def fix_basement():
	print "Great we will do basement first, but we will need to know the design required."
	print "Options are traditional, modern, and rustic."
	
	choice = raw_input("What design would you prefer? ")
	
	if choice.lower() == "traditional":
		do_both("Not bad.  This should not cost as much so maybe we can do both.")
	elif choice.lower() == "modern":
		deck_patio("That's more like it!  Maybe we can do the patio next.")
	else:
		save_money("I don't like your taste so I prefer to keep my money.")
	
	
def deck_patio():
	print "Deck can be great for social gathering or just relaxing outdoor."
	print "Sometimes it can be a pain to maintain, depending on materials used to build."
	
	choice = raw_input("What materials would you choose: stone, concrete, or wood? ")
	
	if choice.lower() == "stone":
		save_money("Great choice! However this is very expensive.")
	elif choice.lower() == "wood":
		fix_basement("Really?  Wood attracts termintes!  I prefer to fix the basemment.")
	elif choice.lower() == "concrete":
		do_both("There is a slim chance we can do basement too.")
	else:
		print "Obviously you know nothing about materials.  Why am I even talking to you?"

def do_both(msg=''):
	print msg
	print "We will attempt to do both patio and basement."
	print "Let's try to see what the estimate will be?"
	
	choice = ''
	while isinstance(choice, str):
		choice = raw_input("> ")
		try:
			choice = int(choice)
		except ValueError:
			print 'Please enter a valid number.'
	if choice < 60000:
		print "Then we can afford to do both. Let's proceed"
		return
	elif choice > 60000:
		fix_basement()
	else:
		save_money()
	
def save_money():
	print "I don't think my options are working out."
	print "I think it makes better sense to save my money."
	
if __name__ == '__main__':  #This is best practice to call start program as a program (not imported)
	start()
		
