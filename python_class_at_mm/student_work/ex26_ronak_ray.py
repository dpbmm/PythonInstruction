
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    first_word = words.pop(0)
    print first_word

def print_last_word(words):
    """Prints the last word after popping it off."""
    last_word = words.pop(-1)
    print last_word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    sorted_sentence = break_words(sentence)
    return sort_words(sorted_sentence)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    individual_word = break_words(sentence)
    print_first_word(individual_word)
    print_last_word(individual_word)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    sorted_individual_words = sort_sentence(sentence)
    print_first_word(sorted_individual_words)
    print_last_word(sorted_individual_words)


print "Let's practice everything."
print 'You\'d need to know about escapes with \\ that do \n(\\n) newlines and \t(\\t) tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans/ 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
jelly_beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (jelly_beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)


sentence = "All good things come to those who wait."

words = break_words(sentence)
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)
print sorted_words

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)