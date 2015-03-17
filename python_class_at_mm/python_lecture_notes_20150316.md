## Python class notes, 20150316

### Classes and Objects

 1. Blueprint for an object. 
 1. Many different objects ("instances of a class") can be created ("instantiated") from the same class.
 1. syntax:

        class PowerTool(object):
            """Model behaviors related to raising a number to a power."""
            def __init__(self, x):
                self.x = x

            def raise_me(self, n):
                """Return value of self.x raised to power n; don't change it."""
                return self.x ** n

            def replace_with_power(self, n):
                """Replace self.x w/ itself raised to power n; don't return it."""
                self.x **= n

 1. Attributes are variables whose specific value is attached to one instance.
 1. Methods are functions belong to a class and that normally act on whatever particular instance of the class they are "called on".
 1. The generic name within a class for every object created by that class is `self`. It is not a reserved word, but `self` is conventional.
 1. The `__init__` method typically sets up the class.
 1. The variable `self` is used to allow the class to talk about each and every object instantiated from it. I can make this clearer using examples. 
    2. I save the file above as `classes.py`. Below I will explain each line in step by step.
    2. First, I import the whole program as a module.

        ```python
>>> import classes 
        ```

    2. Then I create ("instantiate") an object ("instance") of the PowerTools class.

        ```python
>>> power_tools = classes.PowerTools(2)
        ```

       Note four points about what I've just done: 
       * I have to name `PowerTools` as part of the namespace of the module `classes`: `classes.PowerTools...`.
       * I have to "call" `PowerTools` by using parenthesis after it: `classes.PowerTools(...)`. 
       * Since `__init__` requires a variable `x` in addition to `self`, I have to pass an argument into `classes.PowerTools()` — here I pass in `2`: `classes.PowerTools(2)`. 
       * I am assigning the resulting `PowerTools` object to the variable `power_tools`. In future, I will always refer to this particular object as `power_tools`. I could instantiate any number of others, but although they would have the same construction as `power_tools`, the "state" (data) they contain could well be different.

    2. At this point, the object `power_tools` exists and possesses three things. It possesses an "attribute" `x`, a "method" `raise_me`, and another "method" `replace_with_power`.
    2. The class `PowerTools` doesn't know anything about my variable `power_tools` — that variable is known to me alone. But when the class `PowerTools` interacts with the typical object it is able to create, it calls that object `self` — `self` inside of the code of `PowerTools` refers to my `power_tools`, and also to every other object that could be created from the class.
    2. If I want to see what value the attribute `x` has, I get it from my copy of the object:

        ```python
>>> power_tools.x
2
        ```

       Here my `power_tools.x` has the value of `2` because when I instantiated `power_tools` I did it as `classes.PowerTools(2)`. My `2` was passed into `__init__` as the argument `x`, and that `x` was assigned to `self.x`. When we're talking about `power_tools`, `self.x` (that is, `power_tools.x`) has the value `2`.

    2. If I call the method `raise_me`, I need to call it on `power_tools` and pass in an argument `n` — here I'll use the value `3`:

        ```python
>>> power_tools.raise_me(3)
8
        ```

       This method contains a `return` value, so Python returns to me the value of `power_tools.x` (= 2) raised to the value of `n` (= 3), for a total of `8`. But the value of `power_tools.x` is unchanged, as I can show:

        ```python
>>> power_tools.x
2
        ```

       That's because `power_tools.raise_me` does a calculation using `self.x` and returns the result, but doesn't make any changes to `self.x`. 

    2. However, the method `replace_with_power` is different: it doesn't return anything, but it changes the value of `self.x`. Watch:

        ```python
>>> power_tools.replace_with_power(5)
>>> 
        ```

       Nothing is returned. But now if I ask to see the value of `power_tools.x`, I find that the old value has been replaced with a new value:

        ```python
>>> power_tools.x
32
        ```

       The replacement happened in the line `self.x **= n`, which means "take `self.x` (which David calls `power_tools.x`) and replace it with the value of itself raised to the power `n`. Since `power_tools.x` was `2` and `n` was 5, `power_tools.x` becomes `32.

    2. `raise_me` is an example of a method that returns something, just like an ordinary function. But `replace_with_power` is an example of a method that alters the "state" of the object. That's totally unlike most of the other functions we've seen, and it represents one of the powerful things you can do with object-oriented programming. You don't even have to return anything when you do this!

 1. Classes can inherit from other classes. When we say `class PowerTool(object)`, we mean that every object instantiated from this class inherits whatever `object` has. More on this later.

[end]