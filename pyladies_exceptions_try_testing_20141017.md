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

   2. `SyntaxError`, for all sorts of small formal errors in composing expressions:

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

        In [13]: raise SyntaxError('Your syntax are lousy.')
          File "<string>", line unknown
        SyntaxError: Your syntax are lousy.

### Try-Except blocks

 1. 

[end]
