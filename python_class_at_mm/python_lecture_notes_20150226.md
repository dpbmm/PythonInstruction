Limitations of a list

 * A Python list is a stack: it is very fast for actions on the "top" (the right end); very slow for actions on the "bottom" (the left end).
 * Lists are the main tool for holding a bunch of things, but those things necessarily have some order, which affects what you can do with the list.

When to use a dictionary and when to use a list?

 * exact position of an item:
   * if known: list
   * if you don't care: dict (or set)
 * duplicates:
   * if wanted: list
   * if not wanted: dict (or set)
   * if you want to count how many of each: dict

Classes

 1. A class is a blueprint of an object, and in Python everything is an object. So to make your own objects, you write a class. In practice, this isn't very different from writing functions and variable-assignments, as you've been doing, but in a class these functions ("methods") and variables ("attributes") are all bound to the objects that the class creates ("instantiates"). Without creating an object, these things are not accessible.
 
Modules
 
 1. Every module contains a dictionary of its methods and attributes, which you can access using `.__dict__`.
 
[end]