# 100 Days of Python Learning || Day2

- List is a collection which is ordered and changeable. Allows duplicate members `mutable`
- Tuple is a collection which is ordered and unchangeable. Allows duplicate members. `immutable`
- Dictionary is a collection which is ordered\*\* and changeable. No duplicate members.
- Set is a collection which is unordered, unchangeable\*, and unindexed. No duplicate members.

## Modules

    help("modules") # lists all the avaliable modules
    import os # importing
    help(os) # docs

Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.

- os
- Math
- Time
- Random

## Strings

Strings are sequence of Characters

### String Funtions

- capitalize()/title()/lower()
- count()
- find()/index()
- endswith()/startswith()
- format()
- split()
- join()
- replace()
- strip()

## Lists

| Method    | Description                                                    |
| --------- | -------------------------------------------------------------- |
| append()  | adds an element to the end of the list                         |
| extend()  | adds all elements of a list to another list                    |
| insert()  | inserts an item at the defined index                           |
| remove()  | removes an item from the list                                  |
| pop()     | returns and removes an element at the given index              |
| clear()   | removes all items from the list                                |
| index()   | returns the index of the first matched item                    |
| count()   | returns the count of the number of items passed as an argument |
| sort()    | sort items in a list in ascending order                        |
| reverse() | reverse the order of items in the list                         |
| copy()    | returns a shallow copy of the list                             |

## Tuples

A `tuple` in Python is similar to a `list`. The difference between the two is that we cannot change the elements of a `tuple` once it is assigned whereas we can change the elements of a `list`.

- Tuples are read only data type.
- We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
- Since tuples are immutable, iterating through a tuple is faster than with list. So there is a slight performance boost.

## Sets

A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements.\

- The elements in the set cannot be duplicates.
- The elements in the set are immutable but the set as a whole is mutable.
- There is no index attached to any element in a python set. So they do not support any indexing or slicing operation.

## Dictionary

Python dictionary is an unordered collection of items. Each item of a dictionary has a `key/value` pair.\
Dictionaries are optimized to retrieve values when the key is known.
