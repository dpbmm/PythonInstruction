def raise_to_power(x, n):
    """Raise x to power n and return."""
    return x ** n

class PowerTool(object):
    """Model behaviors related to raising a number to a power."""
    def __init__(self, x):
        self.x = x

    def raise_me(self, n):
        """Return value of x raised to power n; don't change x."""
        return self.x ** n

    def replace_with_power(self, n):
        """Replace x with x raised to power n; don't return it."""
        self.x **= n

