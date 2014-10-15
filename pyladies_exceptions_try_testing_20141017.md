# PyLadies Intermediate Python class, 20141017

## Outline: Exceptions, Try-Except Blocks, and Testing

### Exceptions. 

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
        In [84]: lst = ['a', 'b' ,'c']
        
        In [85]: len(lst)
        Out[85]: 3
        
        In [86]: lst[4]
        ---------------------------------------------------------------------------
        IndexError                                Traceback (most recent call last)
        <ipython-input-86-810aaf3c175a> in <module>()
        ----> 1 lst[4]
        
        IndexError: list index out of range
        ```

   2. `SyntaxError`, for all sorts of small formal errors in composing expressions:

        ```python
        In [87]: print lst
          File "<ipython-input-87-a0a7d679bae6>", line 1
            print lst
                    ^
        SyntaxError: invalid syntax
        ```

   2. `NameError`, for when an unassigned variable name is called:

        ```python
        In [88]: print(q)
        ---------------------------------------------------------------------------
        NameError                                 Traceback (most recent call last)
        <ipython-input-88-9a2128501b7d> in <module>()
        ----> 1 print(q)
        
        NameError: name 'q' is not defined
        ```

   2. `KeyError`, for when a dictionary lacks a desired key:

        ```python
        In [89]: d = {'a': 1, 'b': 3}
        
        In [90]: d['c']
        ---------------------------------------------------------------------------
        KeyError                                  Traceback (most recent call last)
        <ipython-input-90-3e4d85f12902> in <module>()
        ----> 1 d['c']
        
        KeyError: 'c'
        ```

     and many others.


[end]
