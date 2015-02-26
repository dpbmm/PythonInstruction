#This is my guess game

from sys import exit
from random import randint
number = randint(1, 10)

print number # I had used this to debug the program. Commenting it now

print "Welcome to the guess game. You will get 3 chances to guess the right number"

guesses = 0

while guesses < 3:
	guesses = guesses + 1
	print "Guess a number between 1 and 10"
	guess = raw_input("> ")
        try:
            guess = int(guess)
        except ValueError:
            print "You think you're so smart..."
            continue

	if guess < number:
		print "Guess is too low"
	elif guess > number:
		print "Guess is too high"
	else:
		print "You guessed the right number! Bravo!"
		break

	if guesses == 3:
		print "Hard luck, try next time!"

	#print guesses #I just used this print statement to debug my program


