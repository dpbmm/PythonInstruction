# PyLadies Intermediate Python class, 20141017

## Outline: Exceptions, Try-Except Blocks, and Testing

### Exceptions

 1. An "exception" is an error detected during execution of a program.

 1. Example: calling `next()` on a generator that has already closed:

        In [1]: gen = (i ** 2 for i in range(10))
        
        In [2]: gen.close()
        
        In [3]: next(gen)
        ---------------------------------------------------------------------------
        StopIteration                             Traceback (most recent call last)
        <ipython-input-40-8a6233884a6c> in <module>()
        ----> 1 next(gen)
        
        StopIteration: 

   This `StopIteration` is a type of built-in exception — it is "thrown" when something tries to call `next()` on a a generator that has already stopped iterating.

 1. Other examples:
 
   2. `IndexError`, when a list does not contain the requested index:

        ```python
        In [4]: lst = ['a', 'b' ,'c']
        
        In [5]: len(lst)
        Out[5]: 3
        
        In [6]: lst[4]
        ---------------------------------------------------------------------------
        IndexError                                Traceback (most recent call last)
        <ipython-input-86-810aaf3c175a> in <module>()
        ----> 1 lst[4]
        
        IndexError: list index out of range
        ```

   2. `SyntaxError`, for all sorts of small formal errors in composing expressions and statements:

        ```python
        In [7]: print lst
          File "<ipython-input-87-a0a7d679bae6>", line 1
            print lst
                    ^
        SyntaxError: invalid syntax
        ```

   2. `NameError`, for when an unassigned variable name is called:

        ```python
        In [8]: print(q)
        ---------------------------------------------------------------------------
        NameError                                 Traceback (most recent call last)
        <ipython-input-88-9a2128501b7d> in <module>()
        ----> 1 print(q)
        
        NameError: name 'q' is not defined
        ```

   2. `KeyError`, for when a dictionary lacks a desired key:

        ```python
        In [9]: d = {'a': 1, 'b': 3}
        
        In [10]: d['c']
        ---------------------------------------------------------------------------
        KeyError                                  Traceback (most recent call last)
        <ipython-input-90-3e4d85f12902> in <module>()
        ----> 1 d['c']
        
        KeyError: 'c'
        ```

     and many others.

 1. You can also write your own, custom exceptions and "raise" them (throw them by design). Here is a simple example:

        In [11]: class CustomException(Exception):
           ....:     pass # Keep it simple for demonstration purposes: empty class.
           ....: 
        
        In [12]: while True:
           ....:     n = input('What is your name? ')
           ....:     if n == 'Olive':
           ....:         raise CustomException('Garsh, Olive, what are we going to do?')
           ....:     else:
           ....:         print('\nHi, {}!'.format(n))
           ....: 
        
        What is your name? Tobi
        Hi, Tobi!
        
        What is your name? Kat
        Hi, Kat!
        
        What is your name? Olive
        ---------------------------------------------------------------------------
        CustomException                           Traceback (most recent call last)
        <ipython-input-92-bb39714cfeb9> in <module>()
              2     n = input('What is your name? ')
              3     if n == 'Olive':
        ----> 4         raise CustomException('Garsh, Olive, what are we going to do?')
              5     else:
              6         print('Hi, {}!'.format(n))
        
        CustomException: Garsh, Olive, what are we going to do?

   We subclass "CustomException" (or any name of your choice) from the "Exception" class.
   
   And note the `raise` keyword, to actually call the exception. When the exception is raised, program execution ends and whatever code is in the class definition gets run. 
   
   This time we had only `pass`, so nothing was run. You can also specify an error message whenever you raise the exception.
   
   You can raise any error you like, at will, also with a custom message:

        In [13]: raise SyntaxError('Youre syntax are okay but youre spelling and grammer needs work.')
          File "<string>", line unknown
        SyntaxError: Youre syntax are okay but youre spelling and grammer needs work.

### Try-Except blocks

 1. When an exception is "thrown", you can "catch" it and avoid having the program end if you so choose. For this you use a `try`-`except` block.

   Consider the following case:

        In [14]: d = {'a': 1, 'b': 2, 'c': 3}
        
        In [15]: keys = {'a', 'b', 'c', 's', 't', 'u', 'v', 'w'}
        
        In [16]: for item in keys:
           .....:     print(d[item])
           .....:     
        3
        ---------------------------------------------------------------------------
        KeyError                                  Traceback (most recent call last)
        <ipython-input-117-7f7bd8319877> in <module>()
              1 for item in keys:
        ----> 2     print(d[item])
              3 
        KeyError: 'v'

   Below we catch the `KeyError` exception in a `try`-`except` block:

        In [17]: for item in keys:
           .....:     try:
           .....:         print(d[item])
           .....:     except KeyError:
           .....:         print("Shucks, key '{}' isn't in this dictionary.".format(item))
           .....:         
        3
        Shucks, key 'v' isn't in this dictionary.
        Shucks, key 's' isn't in this dictionary.
        Shucks, key 'u' isn't in this dictionary.
        1
        Shucks, key 't' isn't in this dictionary.
        Shucks, key 'w' isn't in this dictionary.
        2

   It's considered best if only a single line of code appears within the `try` block, so that you can be very sure where any exception is being thrown.

 1. You don't actually need to specify the exception in the `except` block — you can just include the recovery code and it will be run no matter what exception is thrown:

        In [18]: for item in keys:
           .....:     try:
           .....:         print(d[item])
           .....:     except:
           .....:         print('Shucks! Trying again...')
           .....:         
        3
        Shucks!
        Shucks!
        Shucks!
        1
        Shucks!
        Shucks!
        2

 1. The `try` block and the `except` block are mandatory — using one requires the other. But a full `try`-`except` block has two other optional elements: `else` and `finally`. The `else` block is executed after the `try` block *if* there is no exception. The `finally` block is executed last, regardless of whether or not there was an exception. Here is an example:

        In [19]: d = {'a': 1, 'b': 2, 'c': 3}
        
        In [20]: keys = ['a', 'b', 'c', 'd', 'e']
        
        In [21]: while True:
           ....:     try:
           ....:         print(d[random.choice(keys)], end='')
           ....:     except KeyError:
           ....:         print('This is the "except" block.', end='')
           ....:     else:
           ....:         print(' -- This is the "else" block.', end='')
           ....:     finally:
           ....:         print(' This is the "finally" block.')
           ....:         
        3 -- This is the "else" block. This is the "finally" block.
        2 -- This is the "else" block. This is the "finally" block.
        This is the "except" block. This is the "finally" block.
        2 -- This is the "else" block. This is the "finally" block.
        2 -- This is the "else" block. This is the "finally" block.
        1 -- This is the "else" block. This is the "finally" block.
        3 -- This is the "else" block. This is the "finally" block.
        This is the "except" block. This is the "finally" block.
        3 -- This is the "else" block. This is the "finally" block.
        1 -- This is the "else" block. This is the "finally" block.
        ...

   To recapitulate:
   
   2. If there is no exception, the `try` block, the `else` block, and the `finally` block are executed. 
   2. If there is an exception and it can be caught by some `except` statement, then the block for that `except` statement is run, followed by the `finally` block. 
   2. If there is an exception that is not caught by some `except` statement, then program execution ends.

 1. You can have any number of `except` blocks, one after another. You can also check for any number of exceptions in a single `except` statement, assuming you want them handled all the same way:

        except (SyntaxError, IndexError, NameError):
            print('It could have been one of several exceptions.')

### Testing

 1. One of the most important principles in building and maintaining working code is the "unit test" — a program that tests the behavior of a meaningfully small unit of code in some other program. One very widespread principle of coding theory calls for code to be developed in tandem with and in response to unit tests for that code. The principle is called "test-driven development" (TDD).
 1. Python has many tools for writing test suites (sets of unit tests). Today I will introduce `pytest`, which is available through `pip`. 

[end]
