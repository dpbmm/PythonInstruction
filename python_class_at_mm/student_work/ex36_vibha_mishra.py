'''This is a game to guess Solar System Planets'''
import random

def GuessPlanet():
    with open ('SolarSystemPlanets.txt') as listofPlanets:
        allPlanets = listofPlanets.readlines()
        for planet in allPlanets:
            print(planet)
    listofPlanets = list()
    playagain = True #User wants to play the game again
    while playagain:
        guessPlanet = random.choice(allPlanets).strip() # Choose planet randomly
        print("Guessed Planet is :", guessPlanet)
        lengthPlanet = len(guessPlanet)
        enteredPlanet = "-" * lengthPlanet # It will print no. of letters
        print('Length of guess planet is :', lengthPlanet)
        guessName = set()
        mistakes = 9
        print(" ".join(enteredPlanet))
        guessed = False
        while not guessed and mistakes > 0:
            guess = raw_input("Guess a letter:")
            if guess in guessPlanet:
                guessName.add(guess)
                enteredPlanet = "".join([char if char in guessName else "-" for char in guessPlanet])
                if enteredPlanet == guessPlanet:
                    guessed = True
            else:
                mistakes -= 1
                print("This is not correct.", mistakes, "mistakes left.")
            print("".join(enteredPlanet))
        print("You did good job!")
        playagain = raw_input("Would you like to play again [y/n]: ")
        if playagain.lower() != 'y':
            break

GuessPlanet()


