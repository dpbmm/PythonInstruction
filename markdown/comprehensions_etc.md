# Intermediate Python material, 20141017

## Outline: Comprehensions, Timing, and Generators

### Loops: `while`, `for`. 

 1. Sample `while`-loop:

        In [1]: lst = []
        
        In [2]: i = 0
        
        In [3]: while i < 10:
           ...:     lst.append(i)
           ...:     i += 1
           ...:     
        
        In [4]: print(lst)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

 1. The same result with a `for`-loop:

        In [1]: lst = []
        
        In [2]: for i in range(10):
           ...:     lst.append(i)
           ...:     
        
        In [3]: print(lst)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

 1. Replacing a loop with a comprehension: 

   2. list-comprehensions. Syntax:

        ```python
        In [4]: lst = [i for i in range(10)]
        
        In [5]: print(lst)
        Out[5]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        ```

   2. set-comprehensions

        ```python
        In [6]: s = {i for i in range(10)}
        
        In [7]: print(s)
        Out[7]: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        ```

   2. dict-comprehensions

        ```python
        In [11]: d = {i: i ** 2 for i in range(10)}
        
        In [12]: print(d)
        {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
        ```

       Further: use `zip(list1, list2)` to draw keys and values from different lists:

        ```python
        In [13]: d2 = {i: j for i,j in zip(['a', 'b', 'c'], [1, 2, 3])}
        
        In [14]: print(d2)
        {'c': 3, 'a': 1, 'b': 2}
        ```

   2. tuple-comprehensions

     How would you produce something like `(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)`?
     
     You would make a list and then convert it into a tuple:

        ```python
        In [15]: t= tuple([i for i in range(10)])
        
        In [16]: print(t)
        Out[16]: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        ```

     If you tried the obvious thing, you would get a surprise:

        ```python
        In [17]: (i for i in range(10))
        Out[17]: <generator object <genexpr> at 0x10a8d0ab0>
        ```

     We'll talk about these "generator expressions" a little later. But anyway, you wouldn't get a tuple expression — at the moment there is no such thing.

 1. Nesting

   2. nested loops

        ```python
        In [1]: lst = []
        
        In [2]: letters = ['a', 'b', 'c']
        
        In [3]: numbers = [1, 2, 3]
        
        In [4]: for i in numbers:
        ....:        for j in letters:
        ....:            lst.append((i, j))
        ....:         
        
        In [5]: print(lst)
        [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]
        ```

   2. nested comprehensions

        ```python
        In [6]: lst = [(i, j) for i in numbers for j in letters]
        
        In [7]: print(lst)
        [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]
        ```

       Notice the structure of the nested comprehension: `[... <outer for expression> <inner for expression>]`.

 1. Filtering

   2. `if`-blocks and `continue` within a loop

        ```python
        In [8]: lst = []
        
        In [9]: for i in range(25):
        ....:        if i % 6:
        ....:            continue
        ....:        else:
        ....:            lst.append(i)
        ....:      
        
        In [10]: print(lst)
        [0, 6, 12, 18, 24]

        ```

   2. Filtering within a comprehension

     3. Filtering with `if`: Syntax: `[... <for expression> <if expression>]`.

        ```python
        In [11]: lst = [i for i in range(25) if not i % 6]
        
        In [12]: print(lst)
        [0, 6, 12, 18, 24]
        ```

     3. Filtering with `if-else`: Syntax: `[... <if-else expression> <for expression>]` (notice the difference from filtering with plain `if`).

        ```python
        In [13]: lst1 = []
        
        In [14]: for i in range(10):
        ....:        if i % 3:
        ....:            lst1.append(i)
        ....:        else:
        ....:            lst1.append(i ** 2)
        ....:      
        
        In [15]: print(lst1)
        [0, 1, 2, 9, 4, 5, 36, 7, 8, 81]
        
        In [16]: lst2 = [i if i % 3 else i ** 2 for i in range(10)]
        
        In [17]: print(lst2)
        [0, 1, 2, 9, 4, 5, 36, 7, 8, 81]
        
        In [18]: lst1 == lst2
        Out[18]: True
        ```

### Reasons for using comprehensions.

 1. More declarative style: models `map`, `filter` and anonymous `lambda` functionality in condensed syntax.
  
 1. Efficiency (speed).

### How do we measure speed? Timing

 1. Using `timeit` (`%timeit` in Ipython) to find the average time to run a code block. `timeit` is always followed by a one-liner:

        In [1]: def f(n):
           ....:     lst = []
           ....:     for i in range(n):
           ....:         lst.append(n)
           ....:         
        
        In [2]: def g(n):
           ....:     lst = [i for i in range(n)]
           ....:     
        
        In [3]: %timeit f(100)
        100000 loops, best of 3: 9.15 µs per loop
        
        In [4]: %timeit g(100)
        100000 loops, best of 3: 5.34 µs per loop

 1. Timing differences between comprehensions and `for`-loops.

### Generators: "lazy" evaluation

 1. What is constructed is not the whole sequence but an object that can produce the sequence bit by bit as needed ("lazily") rather than all at once. Consider the speed of constructing a list — it varies depending on the size of the list:

        In [1]: %timeit list(range(10))
        1000000 loops, best of 3: 655 ns per loop
        
        In [2]: %timeit list(range(1000000))
        10 loops, best of 3: 34.7 ms per loop

     Compare that with the speed of constructing only a generator:

        In [3]: %timeit range(10)
        1000000 loops, best of 3: 263 ns per loop
        
        In [4]: %timeit range(1000000)
        1000000 loops, best of 3: 299 ns per loop

     Generators take almost the same amount of time regardless of the size.

 1. Syntax of the one-liner form ("generator expression"): `(<comprehension-structure)`; successive items are called by `next()`:

        In [5]: gen = (i ** 2 for i in range(10000))
        
        In [6]: next(gen)
        Out[6]: 0
        
        In [7]: next(gen)
        Out[7]: 1
        
        In [8]: next(gen)
        Out[8]: 4
        
        In [9]: next(gen)
        Out[9]: 9
        
        In [10]: next(gen)
        Out[10]: 16
        
        In [11]: next(gen)
        Out[11]: 25

 1. When the generator is used up, you get `StopIteration` exception.

        In [12]: gen = (i ** 2 for i in range(3))
        
        In [13]: next(gen)
        Out[13]: 0
        
        In [14]: next(gen)
        Out[14]: 1
        
        In [15]: next(gen)
        Out[15]: 4
        
        In [16]: next(gen)
        ---------------------------------------------------------------------------
        StopIteration                             Traceback (most recent call last)
        <ipython-input-47-8a6233884a6c> in <module>()
        ----> 1 next(gen)
        
        StopIteration: 

 1. Shut down a generator manually with `.close()`:

        In [17]: gen = (i ** 2 for i in range(10))
        
        In [18]: gen.close()
        
        In [19]: next(gen)
        ---------------------------------------------------------------------------
        StopIteration                             Traceback (most recent call last)
        <ipython-input-40-8a6233884a6c> in <module>()
        ----> 1 next(gen)
        
        StopIteration: 

 1. More complex generators can be written out as functions, with the `yield` keyword used to produce the value that will be returned by `next()`. A simple example:

        In [20]: def gen(n):
           ....:     for i in range(n):
           ....:         yield i ** 2
           ....:         
        
        In [21]: g = gen(10)
        
        In [22]: next(g)
        Out[22]: 0
        
        In [23]: next(g)
        Out[23]: 1
        
        In [24]: next(g)
        Out[24]: 4
        
        In [25]: next(g)
        Out[25]: 9
        
        In [26]: g.close()
        
        In [27]: next(g)
        ---------------------------------------------------------------------------
        StopIteration                             Traceback (most recent call last)
        <ipython-input-77-5f315c5de15b> in <module>()
        ----> 1 next(g)
        
        StopIteration: 


[end]
