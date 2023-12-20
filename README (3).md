
# Python control flow
## Python Loops
In python loops ar used to repeat block of code a certain nuumber of times. Thereare twoo types of loops in python:
1. for loops
2. while loops 
### 1. for loop:
for loop is used to execute block of code for each element in the sequence. 
### 2. while loop
while loop is used to execute statement or set of statements when given condition is true, when condition is false inertpreter will comes out of the loop.
## Loops and control statements
Control statements are used to control flow of the loop. There are continue, break and pass statements in python.
#### continue:
continue statement is used to skip the iteration and move the control to the nexy iteration .
#### break:
break statement is used to exit the loop permanently.
#### pass:
It is used to write empty loops. It works like a place holder.
## Looping techniques in python
There are many looping techniques to used with loops in python.
#### Using *sorted()* and *set()*:
*sorted()* function is used with for loop to arrange values in container and *set()* function is used to remove duplicate values from the container.
#### using *inumerate()*:
It is used to print element with its index number.
#### using *zip()*
*zip()* is used to print 2 sequences combine.
#### *items()* and iteritems
*iteritems()* is used to  print the dictionary items key-value pairs. *items()* works same as iteritems but it has some disadvantages as compared to iteritems().
## *range()* vs *xrange()* in python
These both functions are used to iterate a specific number of times in a loop.
xrange was used in python 2. In python 3 xrange() was replaced with range().
## Chaining comparison in python
Chaining comparisons is used to combine multiple comparison operations into a single line of code.
## Switch function
Python doas not have any switch function like other programming languages. We can achieve functionality of it by Using if elif else statement or by using dictionaries.
## Python Itertools
Itertools is a module in python's liberary thhat provides different tools for iterator. Here are some common functions from itetools module:
count(sart , step), cycle(), repeat(), and chain().
## Python iter and next() | Converting an object into an iterator
The __iter__ method returns the iterator object itself.
The __next__ method returns the next value in the iteration. When there are no more values it displays Stopiteration.
## Difference between iteraor and iterable
Iterator is an object that implements  __iter__() and __next__() methods.

Iterable is an object that can be iterated over, meaning you can traverse through all its elements.
Iterable must implement the __iter__() method.
## Generators in python
Generators are special type of functions that are used to create iterables. yeild keyword is used t create Generators. yeild return a value of generator.
### Generator expression
They are similar to list comprehensions but with parentheses instead of square brackets. Generator expression generates values rather than whole list.






