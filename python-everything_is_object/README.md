# Python - Everything is Object

## Understanding Python Objects:
### IDs, Mutability, and Function Arguments


## Introduction

In Python, the phrase "Everything is an object" is not just a slogan—it is the fundamental architecture of the language. Whether you are dealing with a simple integer, a complex function, or a class, Python treats them as objects. This project explores the inner workings of Python's memory management, focusing on how objects are identified, categorized as mutable or immutable, and how these distinctions dictate the behavior of your code.

---

## ID and Type

Every object in Python has a unique **identity** (ID), a **type**, and a **value**. 
* id(): Returns the "identity" of an object, which corresponds to its memory address in CPython.
* type(): Returns the class/type of the object.

Examples:

```python

x = 42
y = 42
print("x ID:", id(x))
print("y ID:", id(y))
print("x Type:", type(x))

```

# Output:

```python
x ID: 140706878123456
y ID: 140706878123456
x Type: <class 'int'>
```
Notice how x and y can share the same ID for immutable types like integers due to Python’s internal optimizations.

Another example:

```python

>>> a = [1, 2, 3]
>>> id(a)
139926795932424
>>> type(a)
<class 'list'>

```

Understanding id is crucial for distinguishing between two objects that look the same but occupy different spots in memory.

## Mutable Objects

Mutable objects are those that can be modified after they are created without changing their identity (id). The most common mutable types are lists, dictionaries, and sets.

Example:

```python

my_list = [1, 2, 3]
print("Original ID:", id(my_list))

my_list.append(4)
print("Modified List:", my_list)
print("ID After Modification:", id(my_list))

```

# Output:

```
Original ID: 140706878654321
Modified List: [1, 2, 3, 4]
ID After Modification: 140706878654321

```
The ID remains the same because the object itself did not change, only its content did. This is a hallmark of mutable objects.

Another example:

```python

>>> l1 = [1, 2, 3]
>>> id(l1)
140562828
>>> l1.append(4)
>>> id(l1)
140562828  # Identity remains the same!

```

## Immutable Objects

Immutable objects cannot be changed once created. If you try to modify one, Python actually creates a new object with a new id. These include integers, floats, strings, and tuples.

Example:

```python

a = "hello"
print("Original ID:", id(a))
a += " world"
print("Modified String:", a)
print("ID After Modification:", id(a))

```

# Output:

```
Original ID: 140706878987654
Modified String: hello world
ID After Modification: 140706879012345

```
Notice the ID changed—Python created a new string rather than modifying the original.

Another example:

```python

>>> x = 10
>>> id(x)
10105376
>>> x += 1
>>> id(x)
10105408  # Identity changed! A new object was created.

```

## Why Does It Matter?
# How Python Treats Mutable vs Immutable Objects
Python treats mutable and immutable objects differently to balance performance and safety.

1. Memory Efficiency: Immutable objects like small integers and strings are "interned" (reused) to save space.
2. Bugs: Mutability can lead to unintended side effects. If two variables point to the same mutable object, changing one changes both. Immutable objects prevent this risk.

Example:

```python

lst1 = [1, 2, 3]
lst2 = lst1
lst2.append(4)
print(lst1)  # Output: [1, 2, 3, 4]

```
Here, modifying lst2 also modifies lst1 because both reference the same object.

## How Arguments Are Passed to Functions

Python uses a mechanism called "Call by Object Reference." When you pass an argument to a function:

* If the object is mutable, the function can modify the original object.
* If the object is immutable, the function cannot change the original; it can only rebind the local name to a new object.

Example:

```python

def modify_number(n):
    n += 10
    print("Inside function:", n, id(n))

num = 5
print("Before function:", num, id(num))
modify_number(num)
print("After function:", num, id(num))

```

# Output:

```
Before function: 5 140706878123456
Inside function: 15 140706878123789
After function: 5 140706878123456

```
For immutable objects, changes inside the function do not affect the original object.

```
def modify_list(lst):
    lst.append(99)
    print("Inside function:", lst, id(lst))

my_list = [1, 2, 3]
print("Before function:", my_list, id(my_list))
modify_list(my_list)
print("After function:", my_list, id(my_list))
```

# Output:
```
Before function: [1, 2, 3] 140706878654321
Inside function: [1, 2, 3, 99] 140706878654321
After function: [1, 2, 3, 99] 140706878654321

```
For mutable objects, the changes persist outside the function because the function receives a reference to the same object.

Another example:

```python

def modify(my_list, my_int):
    my_list.append(4)
    my_int += 1

l = [1, 2, 3]
i = 1
modify(l, i)
print(l) # [1, 2, 3, 4] -> Changed!
print(i) # 1 -> Unchanged!

```

## Advanced Tasks: Memory Optimization
During this project, I explored advanced optimizations:

* Small Integer Caching: CPython pre-allocates integers from -5 to 256 (```NSMALLPOSINTS``` and ```NSMALLNEGINTS```).

* String Interning: Identical string literals are often stored once to save memory.

* ```__slots__```: By using ```__slots__``` in a class, we can prevent the creation of ```__dict__```, significantly reducing the memory footprint and locking the attributes allowed on an instance.


# Author

Thikera Ahmed
