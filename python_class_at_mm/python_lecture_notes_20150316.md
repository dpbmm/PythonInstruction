## Python class notes, 20150316

### Classes and Objects

 1. Blueprint for an object. 
 1. Many different objects ("instances of a class") can be created ("instantiated") from the same class.
 1. syntax:

        class PowerTool(object):
            """Model behaviors related to raising a number to a power."""
            def __init__(self, x):
                self.x = x

            def raise(self, n):
                """Return value of self.x raised to power n; don't change it."""
                return self.x ** n

            def replace_with_power(self, n):
                """Replace self.x w/ itself raised to power n; don't return it."""
                self.x **= n

 1. Attributes are variables whose specific value is attached to one instance.
 1. Methods are functions belong to a class and that normally act on whatever particular instance of the class they are "called on".
 1. The generic name within a class for every object created by that class is `self`. It is not a reserved word, but `self` is conventional.
 1. The `__init__` method typically sets up the class
 1. Classes can inherit from other classes. When we say `class PowerTool(object)`, we mean that every object instantiated from this class inherits whatever `object` has.

[end]