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

   This `StopIteration` is a type of built-in exception.

 1. Other examples:
 
   2. `IndexError`:

        In [84]: lst = ['a', 'b' ,'c']
        
        In [85]: len(lst)
        Out[85]: 3
        
        In [86]: lst[4]
        ---------------------------------------------------------------------------
        IndexError                                Traceback (most recent call last)
        <ipython-input-86-810aaf3c175a> in <module>()
        ----> 1 lst[4]
        
        IndexError: list index out of range

