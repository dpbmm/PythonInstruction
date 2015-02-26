from sys import exit
import sys
import math
import time

aladin = raw_input ("Let me get your name first :" )

def jeannie():
    '''Introduce the jeannie to the player'''
    print "*" * 40
    print "Hello ! I am jeannie"
    print "Unlike other jeannies I give you options"
    print "All you have to do is pick one"
    
def display_options():
    ''' Display all available options to the user '''
    print "*" * 40
    print "Well %s here you go then " %aladin
    print "1 Do you want to calculate anything?"
    print "2 Do you want to make travel plans ?"
    print "3 Do you want to listen to a joke?"
    print "4 Want me to prepare to-do list to make your life easier"
    print "5 Should I just go back to the lamp?"
    pick = raw_input ("")
    print "Great ! so you chose" , pick
    return pick


def choice_function(pick) :
    '''Call respective functions based on user's choice'''
    if pick == "1" :
        calculate()
    elif pick == "2":
        print "I am in option 2"
        #travel()
    elif pick == "3" :
        print "I am in option 3"
        #joke()
    elif pick == "4":
        print "I am in option 4"
        #to-do()
    elif pick == "5":
        print "good bye"

def calculate() :
    '''Calculate all possible values with the numbers entered'''
    print "**** CALCULATOR **** "
    print "Enter first number "
    first = float (raw_input(""))
    print "Enter second number"
    second = float (raw_input(""))
    print "First number" , first
    print "Second number" , second
    addition = first + second
    if first > second :
        subtraction = first - second
    elif second > first :
        subtraction = second - first
    else :
        subtraction = 0
    multiplication = first * second
    division = first / second
    modulo = first % second
    print "Got it ! I am working on the calculation feel free to take \
a power nap for 5 seconds.. Thank you"
    print "."
    print "."
    print "."
    time.sleep(5)
    print "****** C A L C U L A T I O N S **************"
    print "Addition of these two numbers give" , addition
    print "Subtraction of these two numbers give" , subtraction
    print "multiplying these two gives" , multiplication
    print "Dividing %r by %r gives %r" %(first, second, division)
    print "Modulo %r by %r gives %r" %(first, second, modulo)
            
    

jeannie()
pick1 = display_options()
choice_function(pick1)


