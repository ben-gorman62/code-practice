**Python Data Types:**
- str - text
- int, float, complex - numeric
- list, tuple, range - sequence
- dict - mapping
- set, frozenset - sets
- bool - boolean
- bytes, bytearray, memoryview - binary
- NoneType - None

Integers are integers.
Floating points numbers contain the decimal point.
Bools are either True or False.

**Functions & Methods:**
Functions are processes that take an input (or inputs) and returns an output (or outputs).
Arguments are the inputs that functions take.
To use a function, type the function followed by () brackets, in which go the arguments, separated by a comma.

Methods are similar to functions, however they apply directly to pieces of data.

**Indexing:**
Zero indexing is where the first element of a selection starts at zero, rather than one.
To access the first character in a string, you can run `str[0]`
Second character - `str[1]`
Last character - `str[-1]`
Several characters - you need to specify a start and stop index
e.g. `str[0:5]`. Note that the stop index is exclusive.


**Lists:**
`list = []` creates an empty list.
You can add to a list with `list.append()`
To access elements in the list, grab as normal using `[]` e.g. `list[0]`

_List methods:_
- `list.clear()` - removes all elements from a list.
- `list.reverse()` reverses the position of all elements in a list.
- `list.pop(index)` - retrieves the item at the specified index (default = -1) and removes it from the list
- `list.index(item)` - lists the index of the first occurrence of item.
- `list.sort()` - sorts the list in alphabetical/numerical order.

**Dictionaries:**
Similar to lists, but with key-value pairs rather than a single value.
`dict = {}` for an empty dictionary.
You can add to a dict by doing `dict["key"] = "value"`.
You can access values by doing `dict["key"]`

_Dict methods:_
- `dict.keys()` - prints the stored keys
- `dict.values()`- prints the stored values
- `dict.get(keys)` - returns the value for the key. if not present, returns `None`.
- `dict.items()` - returns the key-value pairs as tuples.
- `dict.pop(key)` - returns the specified key and removes the pair from the dictionary
- `dict.clear()` - clears the dictionary
- `dict.setdefault(key, default)` - adds to the dictionary if the key is not present. Does nothing otherwise. default is set to `None` unless specified.

**Classes:**
You can define a class through `class`.
```
class = name_of_class():
    pass
```
Before we use a class we need to instantiate it.
This can be done by declaring the class as a variable, e.g. 
`class_name = name_of_class()`

An example of this together would be:
```
class Greeter():
    def hello(self):
        return "hello"

greeter = Greeter():
greeter.hello()

>>> 'hello'
```

If we want something to happen automatically, we can put the instructions inside `__init__()`.
