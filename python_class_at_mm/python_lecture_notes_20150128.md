## Python Class at MediaMath, 20150128

### Work due today in the regular exercises

 * [Exercise 15: Reading Files](http://learnpythongthehardway.org/book/ex15.html)

   * What is wrong with this?

        ```python
     from sys import argv
     script, filename = argv
     txt = open(filename)
     print txt.read
        ```

   * When would `raw_input` be better than using `argv` to get a filename? When would `argv` be better than using `raw_input`?


 * [Exercise 16: Reading And Writing Files](http://learnpythongthehardway.org/book/ex16.html)

   * When might you use `truncate()`?
   * To empty a file, use `truncate()` or `truncate(0)`.
   * To add binary junk to the end of a file use an argument larger than the size of the file.

 * [Exercise 17: More Files](http://learnpythongthehardway.org/book/ex17.html)

   * Why do you have to call `close()` on a file? What happens if you don't?
   * When can you get away without calling `close()` on a file?

 * [Exercise 18: Names, Variables, Code, Functions](http://learnpythongthehardway.org/book/ex18.html)

   * Explain what the asterisk does here:

    ```Python
    def print_two(*args):
        arg1, arg2 = args
        print "arg1: %r, arg2: %r" % (arg1, arg2)
    ```

   * What does this program do, and why?

    ```Python
    def fn():
        print 'First print statement.'

    print 'Second print statement.'
    fn()
    ```

 * [Exercise 19: Functions And Variables](http://learnpythongthehardway.org/book/ex19.html)

   * What do you expect to happen here:

    ```Python
    number = raw_input('Enter a number: ')
    print number + 5
    ```

 * [Exercise 20: Functions And Files](http://learnpythongthehardway.org/book/ex20.html)

   * What does `seek()` do? How do you use it?
   * What does `readline()` do?

 * [Exercise 21: Functions Can Return Something](http://learnpythongthehardway.org/book/ex21.html)

   * Explain what happens in this program:

    ```python
    def add(a, b):
        return a + b

    print add(7, 19)
    ```

   * If you don't put `return` at the end of a function, what is returned?

 * [Exercise 25: Even More Practice](http://learnpythongthehardway.org/book/ex25.html)

   * What does each line of the "Exercise 25 Python Session" do and what do you expect to see after it? (the session is reproduced below)

    ```python
    import ex25
    sentence = "All good things come to those who wait."
    words = ex25.break_words(sentence)
    words
    sorted_words = ex25.sort_words(words)
    sorted_words
    ex25.print_first_word(words)
    ex25.print_last_word(words)
    words
    ex25.print_first_word(sorted_words)
    ex25.print_last_word(sorted_words)
    sorted_words
    sorted_words = ex25.sort_sentence(sentence)
    sorted_words
    ex25.print_first_and_last(sentence)
    ex25.print_first_and_last_sorted(sentence)
    ```


### Work due today in the command-line crash-course

 * [Exercise 12: View a File (`less`, MORE)](http://learnpythonthehardway.org/book/appendix-a-cli/ex12.html)

    * What exactly do `less` and `more` do? Where did they get their names?

 * [Exercise 13: Stream a File (`cat`)](http://learnpythonthehardway.org/book/appendix-a-cli/ex13.html)

    * How does `cat` differ from `less`?

 * [Exercise 14: Removing a File (`rm`)](http://learnpythonthehardway.org/book/appendix-a-cli/ex14.html)

    * What happens if you use `rm` on a directory? 

 * [Exercise 15: Exiting Your Terminal (`exit`)](http://learnpythonthehardway.org/book/appendix-a-cli/ex15.html)

    * What did you find about these Unix shell commands?
    
        * `xargs`
        * `sudo`
        * `chmod`
        * `chown`

 * [Next Steps](http://learnpythonthehardway.org/book/appendix-a-cli/next.html). Examine the references the author points you to. Read in them (the manuals may be too long to read) and experiment with some of the things that interest you or look useful.

### Work due next time (20150202) in the regular exercises

 * First, if you haven't handed Exercise 26 in to me yet, please do so as soon as you can.

 * [Exercise 27: Memorizing Logic](http://learnpythongthehardway.org/book/ex27.html)

 * [Exercise 28: Boolean Practice](http://learnpythongthehardway.org/book/ex28.html)

 * Read ahead if you're able to.

[end]
