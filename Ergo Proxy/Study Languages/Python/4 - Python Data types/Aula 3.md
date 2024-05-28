# Python Tuple

A tuple is a collection similar to a [Python list](https://www.programiz.com/python-programming/list). The primary difference is that we cannot modify a tuple once it is created.

---

## Create a Python Tuple

We create a tuple by placing items inside parentheses `()`. For example,

```
numbers = (1, 2, -5)
print(numbers)

# Output: (1, 2, -5)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

## More on Tuple Creation

Create a Tuple Using tuple() Constructor

[](https://www.programiz.com/python-programming/methods/built-in/tuple)

[](https://www.programiz.com/python-programming/online-compiler)

Different Types of Python Tuples

[](https://www.programiz.com/python-programming/online-compiler)

[](https://www.programiz.com/python-programming/online-compiler)

[](https://www.programiz.com/python-programming/online-compiler)

---

## Tuple Characteristics

Tuples are:

- **Ordered** - They maintain the order of elements.
- **Immutable** - They cannot be changed after creation.
- **Allow duplicates** - They can contain duplicate values.

---

## Access Tuple Items

Each item in a tuple is associated with a number, known as a **index**.

The index always starts from **0**, meaning the first item of a tuple is at index **0**, the second item is at index **1,** and so on.

![Index of Tuple Item](https://www.programiz.com/sites/tutorial2program/files/tuple-index-item-python.png "Index of Tuple Item")

Index of Tuple Item

### Access Items Using Index

We use index numbers to access tuple items. For example,

```
languages = ('Python', 'Swift', 'C++')

# access the first item
print(languages[0])   # Python

# access the third item
print(languages[2])   # C++
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

![Access Tuple Items](https://www.programiz.com/sites/tutorial2program/files/access-python-tuple-item.png "Access Tuple Items")

Access Tuple Items

---

## Tuple Cannot be Modified

Python tuples are immutable (unchangeable). We cannot add, change, or delete items of a tuple.

If we try to modify a tuple, we will get an error. For example,

```
cars = ('BMW', 'Tesla', 'Ford', 'Toyota')

# trying to modify a tuple
cars[0] = 'Nissan'    # error
       
print(cars)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

---

## Python Tuple Length

We use the [len()](https://www.programiz.com/python-programming/methods/built-in/len) function to find the number of items present in a tuple. For example,

```
cars = ('BMW', 'Tesla', 'Ford', 'Toyota')
print('Total Items:', len(cars)) 
       
# Output: Total Items: 4
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

---

## Iterate Through a Tuple

We use the [for loop](https://www.programiz.com/python-programming/for-loop) to iterate over the items of a tuple. For example,

```
fruits = ('apple','banana','orange')

# iterate through the tuple
for fruit in fruits:
    print(fruit)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

apple
banana
orange