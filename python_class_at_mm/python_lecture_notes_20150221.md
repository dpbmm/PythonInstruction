## Review of items from Exercise 37 (20150218)

### Keywords

 1. `and`:  Logical and.
    * `True and False == False`

 1. `def`:  Define a function.
    * `def X(): pass`

 1. `elif`:  Else if condition.
    * `if: X; elif: Y; else: J`
    * Less waste of space than `else` followed by `if`.

 1. `else`:  Else condition.
    * `if: X; elif: Y; else: J`

 1. `for`:  Loop over a collection of things.
    * `for X in Y: pass`

 1. `from`:  Importing specific parts of a module.
    * `import X from Y`

 1. `if`:  If condition.
    * `if: X; elif: Y; else: J`

 1. `import`:  Import a module into this one to use.
    * `import os`

 1. `in`:  Part of for-loops. Also a test of X in Y.
    * `for X in Y: pass also 1 in [1] == True`

 1. `is`:  Like == to test equality.
   * `1 is 1 == True`

 1. `not`:  Logical not.
    * `not True == False`

 1. `or`:  Logical or.
    * `True or False == True`

 1. `print`:  Print this string.
    * `print 'this string'`

 1. `return`:  Exit the function with a return value.
    * `def X(): return Y`

 1. `while`:  While loop.
    * `while X: pass`

### Data Types

 1. `bool`:

    * `True`

      * True boolean value. 
      * `True or False == True`
   
    * `False`

      * False boolean value. 
      * `False and True == False`

 1. `None` (`NoneType`):  Represents "nothing" or "no value". 
    * `x = None`

 1. `str`:  Stores textual information. 
    * `x = "hello"`

 1. `int`:  Stores integers. 
    * `i = 100`

 1. `float`:  Stores decimals. 
    * `i = 10.389`

 1. `list`:  Stores a list of things. 
    * `j = [1,2,3,4]`

### String Escape Sequences

 1. `\\`:  Backslash

 1. `\'`:  Single-quote

 1. `\"`:  Double-quote

 1. `\a`:  Bell

 1. `\b`:  Backspace

 1. `\f`:  Formfeed

 1. `\n`:  Newline

 1. `\r`:  Carriage return

 1. `\t`:  Tab

 1. `\v`:  Vertical tab


## Operators

 1. `Operator`:  Description 
    * `Example`

 1. `+`:  Addition 
    * `2 + 4 == 6`

 1. `-`:  Subtraction 
    * `2 - 4 == -2`

 1. `*`:  Multiplication 
    * `2 * 4 == 8`

 1. `**`:  Power of 
    * `2 ** 4 == 16`

 1. `/`:  Division 
    * `2 / 4.0 == 0.5`

 1. `//`:  Floor division 
    * `2 // 4.0 == 0.0`

 1. `%`:  String interpolate or modulus 
    * `2 % 4 == 2`

 1. `<`:  Less than 
    * `4 < 4 == False`

 1. `>`:  Greater than 
    * `4 > 4 == False`

 1. `<=`:  Less than equal 
    * `4 <= 4 == True`

 1. `>=`:  Greater than equal 
    * `4 >= 4 == True`

 1. `==`:  Equal 
    * `4 == 5 == False`

 1. `!=`:  Not equal 
    * `4 != 5 == True`

 1. `<>`:  Not equal 
    * `4 <> 5 == True`

 1. `( )`:  Parenthesis 
    * `len('hi') == 2`

 1. `[ ]`:  List brackets 
    * `[1,3,4]`

 1. `{ }`:  Dict curly braces 
    * `{'x': 5, 'y': 10}`

 1. `@`:  At (decorators) 
    * `@classmethod`

 1. `,`:  Comma 
    * `range(0, 10)`

 1. `:`:  Colon 
    * `def X():`

 1. `.`:  Dot 
    * `self.x = 10`
    * Accesses an attribute (like a variable) or method (like a function) of an object.

 1. `=`:  Assign equal 
    * `x = 10`

 1. `;`:  semi-colon 
    * `print "hi"; print "there"`

 1. `+=`:  Add and assign 
    * `x = 1; x += 2`

 1. `-=`:  Subtract and assign 
    * `x = 1; x -= 2`

 1. `*=`:  Multiply and assign 
    * `x = 1; x *= 2`

 1. `/=`:  Divide and assign 
    * `x = 1; x /= 2`

 1. `//=`:  Floor divide and assign 
    * `x = 1; x //= 2`

 1. `%=`:  Modulus assign 
    * `x = 1; x %= 2`

 1. `**=`:  Power assign 
    * `x = 1; x **= 2`

---

### Not yet covered in the book:

 1. `as`:  Part of the with-as statement.
    * `with X as Y: pass`

 1. `assert`:  Assert (ensure) that something is true.
    * `assert False, "Error!"`

 1. `break`:  Stop this loop right now.
    * `while True: break`

 1. `class`:  Define a class.
    * `class Person(object)`

 1. `continue`:  Don't process more of the loop, do it again.
    * `while True: continue`

 1. `del`:  Delete from dictionary.
    * `del X[Y]`

 1. `dict`:  Stores a key=value mapping of things. 
    * `e = {'x': 1, 'y': 2}`

 1. `except`:  If an exception happens, do this.
    * `except ValueError, e: print e`

 1. `exec`:  Run a string as Python.
    * `exec 'print "hello"'

 1. `finally`:  Exceptions or not, finally do this no matter what.
    * `finally: pass`

 1. `global`:  Declare that you want a global variable.
    * global X`

 1. `lambda`:  Create a short anonymous function.
    * `s = lambda y: y ** y; s(3)`

 1. `pass`:  This block is empty.
    * `def empty(): pass`

 1. `raise`:  Raise an exception when things go wrong.
    * `raise ValueError("No")`

 1. `try`:  Try this block, and if exception, go to except.
    * `try: pass`

 1. `with`:  With an expression as a variable "do".
    * `with X as Y: pass`

 1. `yield`:  Pause here and return to caller.
    * `def X(): yield Y; X().next()`

[end]