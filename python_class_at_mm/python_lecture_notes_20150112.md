## Python Class at MediaMath, 20150112

### Work due today in the regular lessons

 * [Exercise 4: Variables And Names](http://learnpythonthehardway.org/book/ex4.html)

     * Explain the error

        ```py
        Traceback (most recent call last):
          File "ex4.py", line 8, in <module>
            average_passengers_per_car = car_pool_capacity / passenger
        NameError: name 'car_pool_capacity' is not defined
        ```

     * I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?
     * Why don't we write `x=100`?

 * [Exercise 5: More Variables And Printing](http://learnpythonthehardway.org/book/ex5.html)

     * Try to write some variables that convert the inches and pounds to centimeters and kilograms.
     * Where is there a list of all of the Python format characters? (https://docs.python.org/2/library/stdtypes.html#string-formatting). Note that in Python there is a different system for formatting data in strings.
     * Are strings mutable or immutable?
     * What does `%r` do as a string formatting conversion type?
     * How can I round a floating point number? Suppose I want to round it to 2 decimal points? How about no decimal points?
     * What is wrong with these variables?
     
         * `1 = 'Zed Shaw'`
         * `a1 = 'Zed Shaw'`
         * `1a = 'Zed Shaw'`
         * `_1a = 'Zed Shaw'`
         * `_ = 'Zed Shaw'`
         * `__1a = 'Zed Shaw'`

 * [Exercise 6: Strings And Text](http://learnpythonthehardway.org/book/ex6.html)

     * What is the difference between `'` and `"`? When do you use one and when the other?
     * Where in the book's code are there nested strings?
     * What happens if you add two strings?
     * What is the difference between `%r` and `%s`?

 * [Exercise 7: More Printing](http://learnpythonthehardway.org/book/ex7.html)

     * What happens if you multiply a string by a number?
     * What happens if you remove the comma at the end of the second-to-last line of the code in this exercise?

 * [Exercise 8: Printing, Printing](http://learnpythonthehardway.org/book/ex8.html)

     * What is happening here:

        formatter = "%r %r %r %r"
        print formatter % (1, 2, 3, 4)

     * Explain the output of

        print formatter % (formatter, formatter, formatter, formatter)

     * Explain the output of 

        ```python
        print formatter % (
		"I had this thing.",
        	"That you could type up right.",
        	"But it didn't sing.",
        	"So I said goodnight."
        	)
        ```

     * Explain why the print statement above can cross so many lines.

 * [Exercise 9: Printing, Printing, Printing](http://learnpythonthehardway.org/book/ex9.html)

     * What is the difference between `"""` and `"`?
     * What is `\n`? 
     * How does `\n` show up when used with `%r`?

 * [Exercise 10: What Was That?](http://learnpythonthehardway.org/book/ex10.html)

     * What is escaping?
     * How do you print a literal `\`?
     * How do you print a tab?
     * How do you make a string of ten tabs?
     * Did you try this, and what happened?

        ```python
        while True:
            for i in ["/","-","|","\\","|"]:
                print "%s\r" % i,
        ```

     * Ask questions about the table of Escape Sequences.

### Any questions about the command-line material?

 * [Exercise 7: Remove Directory (`rmdir`)](http://learnpythonthehardway.org/book/appendix-a-cli/ex7.html)
 * [Exercise 8: Moving Around (`pushd`, `popd`)](http://learnpythonthehardway.org/book/appendix-a-cli/ex8.html)
 * [Exercise 9: Making Empty Files (`touch`, New-Item)](http://learnpythonthehardway.org/book/appendix-a-cli/ex9.html)
     * Why do you get an error if you use `touch` to create a file, then `cd ..` and `rmdir`?
 * [Exercise 10: Copy a File (`cp`)](http://learnpythonthehardway.org/book/appendix-a-cli/ex10.html)
 * [Exercise 11: Moving a File (`mv`)](http://learnpythonthehardway.org/book/appendix-a-cli/ex11.html)
     * What is the difference between `cp` and `mv`?

### Work due next time (20150114) in the regular exercises

 * [Exercise 11: Asking Questions](http://learnpythonthehardway.org/book/ex11.html)
 * [Exercise 12: Prompting People](http://learnpythonthehardway.org/book/ex12.html)
 * [Exercise 13: Parameters, Unpacking, Variables](http://learnpythonthehardway.org/book/ex13.html)
 * [Exercise 14: Prompting And Passing](http://learnpythonthehardway.org/book/ex14.html)

### Work due next time (20150114) in the command-line crash-course

 * [Exercise 12: View a File (`less`, MORE)](http://learnpythonthehardway.org/book/appendix-a-cli/ex12.html)
 * [Exercise 13: Stream a File (`cat`)](http://learnpythonthehardway.org/book/appendix-a-cli/ex13.html)
 * [Exercise 14: Removing a File (`rm`)](http://learnpythonthehardway.org/book/appendix-a-cli/ex14.html)
 * [Exercise 15: Exiting Your Terminal (`exit`)](http://learnpythonthehardway.org/book/appendix-a-cli/ex15.html)

[end]
