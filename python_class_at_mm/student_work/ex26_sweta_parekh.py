# All the functions are defined at the top of the script
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# Just printing lines using newline, tab and escape character
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

# Defining variable poem. Triple quotes will allow to print multiple stmts like a para
poem = """
The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
where there is none.
"""

#printing variable poem
print "--------------"
print poem
print "--------------"

#Defining variable five using the math and print the variable
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

#Defining variable start_point and calling function secret_formula.
#The value returned by the function secret_formula is assigned to variables bean, jars, crates
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

#Another way of calling function secret_formula
start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

#Defining variable sentence
sentence = "All good things come to those who wait."

#Calling function break_words and then print the variable words
words = break_words(sentence)
print words

#Calling function sort_words by sending the output of break_words function
sorted_words = sort_words(words)
print sorted_words

#Calling function print_first_word by sending the output from break_words function
print_first_word(words)

#Calling function print_last_word by sending the output from break_words function
print_last_word(words)

#Calling function sort_sentence by sending variable sentence
sorted_words = sort_sentence(sentence)
print sorted_words

#Calling function print_first_word by sending the output from sort_sentence function
print_first_word(sorted_words)

#Calling function print_last_word by sending the output from sort_sentence function
print_last_word(sorted_words)

print sorted_words

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)
