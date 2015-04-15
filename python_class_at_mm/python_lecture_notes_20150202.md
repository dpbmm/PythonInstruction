## Python Class at MediaMath, 20150202

Reading the code, what are the errors? And what could be done differently?

```python
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words)
    """Prints the first word after popping it off."""
    word = words.poop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1
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


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

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

five = 10 - 2 + 3 - 5
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans \ 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates == secret_formula(start-point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont


sentence = "All god\tthings come to those who weight."

words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

print_first_word(words)
print_last_word(words)
.print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
prin sorted_words

print_irst_and_last(sentence)

   print_first_a_last_sorted(senence)
```

Here is my version of the solution — do you think I omitted anything?

 1. In `break_words`: 
    2. `stuff.split(' ')` could be written `stuff.split()`, since (quoting from the docs) "If sep is not specified or is None, any whitespace string is a separator and empty strings are removed from the result."
    2. Since we write

          ```python
words = stuff.split()
return words
          ```
       we could just condense the two lines as

          ```python
return stuff.split()
          ```
       There would perhaps be some infinitesimal savings in time by not assigning the value of `stuff.split()` to a named variable. The main reason to do this, though, is that that named variable is never going to be used again. Since it has no use anywhere else in the program, we may as well eliminated it.
    2. The argument `stuff` is sort of abstract. Wouldn't we like to know that a sentence is expected? That would be easier to know if the argument were named `sentence`, as in some of the other functions.

 1. In `print_first_word`:

    2. We need a colon after `def print_first_word(words)`.
    2. `poop(0)` should be `pop(0)`
    2. We can condense

          ```python
word = words.pop(0)
print word
          ```
       to
          ```python
print words.pop(0)
          ```
       But do notice that in either case, `words` is changed: the popped element is no longer found in `words`. That could become an issue below.

 1. In `print_last_word`:

    2. `words.pop(-1` should be `words.pop(-1)`; and note that `words.pop()` alone has the same effect because `pop` without an argument defaults to popping the last element of the list.
    2. The two lines of this function can likewise be condensed into one, as above.

 1. In `sort_sentence`:

    2. The two lines of this function can again be condensed, if you like:

        ```python
return sort_words(break_words(sentence))
        ```
 1. In `print_first_and_last` and `print_first_and_last_sorted`, if by chance our sentence has only one word, we will get an error at `print_last_word(words)`. Why? (Hint: the error will be `IndexError`)
 1. In this line:
    ```python
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
    ```
    am I trying to produce an actual newline and tab? or just the readable escaped forms `\n` and `\t`? My guess is the latter, since an actual newline and tab have no function in the sentence. So it has to be changed to

    ```python
print 'You\'d need to know \'bout escapes with \\ that do \\n newlines and \\t tabs.'
    ```
 1. In the poem:
    2. I suppose we are intended to correct the spelling of `explantion` to `explanation`.
    2. Since we are using triple quotes, I see little need for the mid-line newline written as `\n`; it would be more natural just to break the lines there:
        ```python
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern
the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""
        ```
     That will also keep us from getting a funny space before `the needs of love`.
 1. The three lines

    ```python
    print "--------------"
    print poem
    print "--------------"
    ```
    could be condensed to
    ```python
    print "--------------\n%s\n--------------" % (poem)
    ```
    Note that the poem itself already begins and ends with a newline, but we need an additional newline before and after it in order to replicate the effect of the three print statements.
 1. The arithmetic in `five = 10 - 2 + 3 - 5` is wrong and should be changed to `five = 10 - 2 + 3 - 6`, since we presumably expect `five` to be equal to `5`.
 1. In `secret_formula`, change `jelly_beans \ 1000` to `jelly_beans / 1000`. (What does `\` mean in Python?)
 1. There are three problems in `beans, jars, crates == secret_formula(start-point)`:
    2. The argument `start-point` should be `start_point`; if we write `start-point`, Python thinks we are trying to subtract `point` from `start`, and it has never heard of either of those variables.
    2. The double-equals sign `==` means we are asking whether the 3-tuple `beans, jars, crates` is or is not equal to the return value of `secret_formula(start_point)`. But Python has never heard of `beans, jars, crates` before, so it can't answer that question. 
    2. Presumably `jeans` should be `beans`. Boy, someone is a lousy typist.
 1. There are three problems in `print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont`:
    2. Change `start_pont` to `start_point`.
    2. Close the parentheses calling `secret_formula`: `secret_formula(start_point` => `secret_formula(start_point)`
    2. Surely `crabapples` should be `crates`.
 1. In `sentence = "All god\tthings come to those who weight."` you better change three things:
    2. `god` => `good`
    2. Replace `\t` with a space.
    2. `weight` => `wait`.
    Earlier I mentioned that `str.split()` splits on _any_ whitespace. Notice the difference between these two slightly different results

        ```python
        >>> sentence = "All good\tthings come to those who wait."
        >>> sentence.split()
        ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
        
        >>> sentence.split(' ')
        ['All', 'good\tthings', 'come', 'to', 'those', 'who', 'wait.']
        ```
     If we pass `' '` as the argument of `split()`, the `\t` remains in the second element of the split string; if we pass no argument, the `\t` (as whitespace) is removed and `'good'` and `'things'` are treated as separate elements.

 1. In these lines

    ```python
words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)
    ```
    Python is going to scream because it doesn't know what `ex25` means — you have to import it first. The same thing happens a little further down, in the line `sorted_words = ex25.sort_sentence(sentence)`. (Notice that `split()` and `split(' ')` will do different things with a sentence like `"All god\tthings come to those who weight."`.)
 1. In `.print_first_word(sorted_words)` what is that period doing before `print_first_word`?
 1. In `prin sorted_words`, change `prin` to `print`.
 1. In `print_irst_and_last(sentence)`, change `print_irst_and_last` to `print_first_and_last`.
 1. In `print_first_a_last_sorted(senence)`:
    2. Change `_a_` to `_and_`.
    2. Eliminate the three spaces at the beginning of the line.
    2. Change `senence` to `sentence`.

[end]
