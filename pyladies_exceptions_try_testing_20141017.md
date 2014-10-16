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

        ...
        except (SyntaxError, IndexError, NameError):
            print('It could have been one of several exceptions.')

### Testing

 1. One of the most important principles in building and maintaining working code is the "unit test" — a program that tests the behavior of a meaningfully small unit of code in some other program. One very widespread principle of coding theory calls for code to be developed in tandem with and in response to unit tests for that code. The principle is called "test-driven development" (TDD).
 1. Python has many tools for writing test suites (sets of unit tests). Today I will introduce `pytest`, which is available through `pip`. 
 1. Imagine we have a program that sorts a list. I've supplied a simple one, `dubious_sort.py`. We don't need to know how it works — all we need to know is that it contains a function `sort()`, which takes a list as input and returns the list sorted. We can generate a list of random characters and try it out ourselves:

        In [1]: import dubious_sort as D
        
        In [2]: import random, string
        
        In [3]: lst = [random.choice(string.ascii_lowercase) for i in range(10)]
        
        In [4]: lst
        Out[4]: ['m', 'a', 'f', 't', 'v', 'k', 'd', 'd', 'a', 'd']
        
        In [5]: D.sort(lst)
        Out[5]: ['a', 'a', 'd', 'd', 'd', 'f', 'k', 'm', 't', 'v']

   Based on one look, it seems to work. It also contains a hidden option to allow us to wreck the sort:

        In [6]: D.sort(lst, broken=True)
        Out[6]: ['d', 't', 'm', 'a', 'v', 'd', 'a', 'd', 'k', 'f']

   Rather than relying on the judgement of our eyes, we're going to write a unit test to make sure that it works correctly under a variety of circumstances.

   I will do this by generating lists of random characters and then sorting them twice — once using the built-in `sorted()` function and once using `dubious_sort.py`. I will then `assert` that the two sorted versions are identical, and Pytest will tell me whether they are or not.

 1. Pytest tests are placed in a subdirectory `test`, and they need to be named `test_` prepended to the name of the program they are targeting. So we create a file called `test_dubious_sort.py` and put it in the subdirectory `test`. 
 1. Inside this file, I import the program I am going to test. Since it is located in the directory above the test program, I modify the Python path so that I can import it easily:

        import os
        import sys
        sys.path.append(os.path.join('..'))
        import dubious_sort as D 

   I want to be able to generate a random list of characters, so I place a function in the file:

        import random
        import string        
        
        def generate_random_list(n):
            return [random.choice(string.ascii_lowercase) for i in range(n)]

   With this I can generate random lists of any length.

 1. Now let me write a single unit test, a function beginning `test_`:

        def test_n_10():                  
            lst = generate_random_list(10)
            assert D.sort(lst) == sorted(lst)

   What this function does is to generate a ten-character random list, and then `assert` that `dubious_sort.sort()` produces the same list as the built-in `sorted` function. Now I run Pytest: I change into the `test` directory, import `pytest` (which I previously installed using `pip`), and run `pytest`:

        In [1]: cd test
        /Users/dpb/github_public/PythonInstruction/test
        
        In [2]: import pytest
        
        In [3]: pytest.main()
        ============================= test session starts ==============================
        platform darwin -- Python 3.4.2 -- py-1.4.25 -- pytest-2.6.3
        collected 1 items 
        
        test_dubious_sort.py .
        
        =========================== 1 passed in 0.01 seconds ===========================
        Out[3]: 0

   Pytest reports that it "collected 1 items" — it found one test function in all test programs in the directory. Then it showed the name of the test program, followed by a period. Each period represents one test passed. Finally, it reported a summary of its results: "1 passed in 0.01 seconds" and returned the value 0, which means all tests passed.

 1. Now let's see what happens if a test fails. We'll write a purposely unsuccessful test:

        def test_fail():                  
            lst = generate_random_list(10)
            assert lst == sorted(lst)                                                   

   Here is the output:

        In [4]: pytest.main()
        ============================= test session starts ==============================
        platform darwin -- Python 3.4.2 -- py-1.4.25 -- pytest-2.6.3
        collected 2 items 
        
        test_dubious_sort.py .F
        
        =================================== FAILURES ===================================
        __________________________________ test_fail ___________________________________
        
            def test_fail():
                lst = generate_random_list(10)
        >       assert lst == sorted(lst)
        E       assert ['f', 'm', 'w...'y', 'f', ...] == ['c', 'f', 'f'...'k', 'm', ...]
        E         At index 0 diff: 'f' != 'c'
        
        test_dubious_sort.py:22: AssertionError
        ====================== 1 failed, 1 passed in 0.02 seconds ======================
        Out[4]: 1
        
   Pytest found a total of two "items", test functions. You can guess that ".F" means the first test passed and the second test failed. Pytest then lists the test that failed (`test_fail()`) and shows the line that failed — first the line in code, and then the same line with actual values filled in. It names the first place where there was a problem: "At index 0 diff". It reports the line where an exception was thrown, and names the exception as `AssertionError`. Finally, it sums up `1 failed, 1 passed in 0.02 seconds" and returns a value of 1, meaning a failed test.

 1. Let's comment out `test_fail()` and write some longer tests. I want to test much longer lists, and I want to run those tests many times in each function, rather than just once. Here is the file now:

        import os
        import sys
        sys.path.append(os.path.join('..'))
        import dubious_sort as D
        import random
        import string
        
        def generate_random_list(n):
            return [random.choice(string.ascii_lowercase) for i in range(n)]
        
        def test_n_10():
            lst = generate_random_list(10)
            assert D.sort(lst) == sorted(lst)
        
        #def test_fail():
        #    lst = generate_random_list(10)
        #    assert lst == sorted(lst)
         
        def test_n_100():
            for i in range(100):
                lst = generate_random_list(100)
                assert D.sort(lst) == sorted(lst)
         
        def test_n_1000():
            for i in range(100):
                lst = generate_random_list(1000)
                assert D.sort(lst) == sorted(lst)                                           

   These tests generate the following output:

        In [1]: import pytest
        
        In [2]: pytest.main()
        ============================= test session starts ==============================
        platform darwin -- Python 3.4.2 -- py-1.4.25 -- pytest-2.6.3
        collected 3 items 
        
        test_dubious_sort.py ...
        
        =========================== 3 passed in 0.76 seconds ===========================
        Out[2]: 0

   All good. If we change `dubious_sort.py` at some time in the future, and these tests no longer pass, we will then know that we have broken functionality that used to work. The test suite serves as a check on how we expect our program to function. Of course, in a complex program it is best if functions are designed in a modular way, so that they can be tested individually.

 1. Now let's test the `broken=True` functionality. This setting should always return a list in other than sorted order. We are asserting that `dubious_sort.sort()` always produces something different from the sorted list, so our assertion contains `!=` where we had `==` earlier:

        def test_broken_n_1000():
            for i in range(100):
                lst = generate_random_list(1000)
                assert D.sort(lst, broken=True) != sorted(lst)

   Output:

        In [1]: import pytest
        
        In [2]: pytest.main()
        ============================= test session starts ==============================
        platform darwin -- Python 3.4.2 -- py-1.4.25 -- pytest-2.6.3
        collected 4 items 
        
        test_dubious_sort.py ....
        
        =========================== 4 passed in 1.08 seconds ===========================
        Out[2]: 0
        

   Success. Of course, a list must have no fewer than two elements for this to be possible. This is a special edge case, so let's also write a test with just two-element lists, just to be sure about this edge case.

        def test_broken_n_2():
            for i in range(100):
                lst = generate_random_list(2) 
                assert D.sort(lst, broken=True) == sorted(lst)                          



[end]
