# Python List

In Python, lists allow us to store a sequence of items in a single variable.

---

## Create a Python List

We create a list by placing elements inside square brackets `[]`, separated by commas. For example,

```
 # a list of three elements
ages = [19, 26, 29]
print(ages)

# Output: [19, 26, 29]
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

Here, the `ages` list has three items.

More on List Creation

[](https://www.programiz.com/python-programming/online-compiler)

Using list() to Create Lists

[](https://www.programiz.com/python-programming/methods/built-in/list)

[](https://www.programiz.com/python-programming/online-compiler)

---

## List Characteristics

Lists are:

- **Ordered** - They maintain the order of elements.
- **Mutable** - Items can be changed after creation.
- **Allow duplicates** - They can contain duplicate values.

---

## Access List Elements

Each element in a list is associated with a number, known as a **index**.

The index always starts from **0**. The first element of a list is at index **0**, the second element is at index **1**, and so on.

![Index of List Elements](https://www.programiz.com/sites/tutorial2program/files/list-index-python.png "Index of List Elements")

Index of List Elements

### Access Elements Using Index

We use index numbers to access list elements. For example,

```
languages = ['Python', 'Swift', 'C++']

# access the first element
print(languages[0])   # Python

# access the third element
print(languages[2])   # C++
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

![Access List Elements](https://www.programiz.com/sites/tutorial2program/files/access-list-item-python.png "Access List Elements")

Access List Elements

---

## More on Accessing List Elements

Negative Indexing in Python

![Python Negative Indexing](https://www.programiz.com/sites/tutorial2program/files/list-negative-index-in-python.png "Python Negative Indexing")

[](https://www.programiz.com/python-programming/online-compiler)

Slicing of a List in Python

[](https://www.programiz.com/python-programming/online-compiler)

[](https://www.programiz.com/python-programming/examples/list-slicing)

**Note**: If the specified index does not exist in a list, Python throws the `IndexError` exception.

---

## Add Elements to a Python List

We use the [append()](https://www.programiz.com/python-programming/methods/list/append) method to add an element to the end of a Python list. For example,

```
fruits = ['apple', 'banana', 'orange']
print('Original List:', fruits)

# using append method 
fruits.append('cherry')

print('Updated List:', fruits)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

Original List: ['apple', 'banana', 'orange']
Updated List: ['apple', 'banana', 'orange', 'cherry']

Add Elements at the Specified Index

[](https://www.programiz.com/python-programming/methods/list/insert)

[](https://www.programiz.com/python-programming/online-compiler)

Add Elements to a List From Other Iterables

[](https://www.programiz.com/python-programming/methods/list/extend)

[](https://www.programiz.com/python-programming/online-compiler)

---

## Change List Items

We can change the items of a list by assigning new values using the `=` operator. For example,

```
colors = ['Red', 'Black', 'Green']
print('Original List:', colors)

# changing the third item to 'Blue'
colors[2] = 'Blue'

print('Updated List:', colors)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

Original List: ['Red', 'Black', 'Green']
Updated List: ['Red', 'Black', 'Blue']

Here, we have replaced the element at index 2: `'Green'` with `'Blue'`.

---

## Remove an Item From a List

We can remove an item from a list using the [remove()](https://www.programiz.com/python-programming/methods/list/remove) method. For example,

```
numbers = [2,4,7,9]

# remove 4 from the list
numbers.remove(4)

print(numbers) 

# Output: [2, 7, 9]
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

Remove One or More Elements of a List

[](https://www.programiz.com/python-programming/del)

[](https://www.programiz.com/python-programming/online-compiler)

[](https://www.programiz.com/python-programming/online-compiler)

---

## Python List Length

We can use the built-in [len()](https://www.programiz.com/python-programming/methods/built-in/len) function to find the number of elements in a list. For example,

```
cars = ['BMW', 'Mercedes', 'Tesla']

print('Total Elements: ', len(cars))  
  
# Output: Total Elements:  3
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

---

## Iterating Through a List

We can use a [for loop](https://www.programiz.com/python-programming/for-loop) to iterate over the elements of a list. For example,

```
fruits = ['apple', 'banana', 'orange']

# iterate through the list
for fruit in fruits:
    print(fruit)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

apple
banana
orange

---

## Python List Methods

Python has many useful [list methods](https://www.programiz.com/python-programming/methods/list) that make it really easy to work with lists.

|Method|Description|
|---|---|
|[append()](https://www.programiz.com/python-programming/methods/list/append)|Adds an item to the end of the list|
|[extend()](https://www.programiz.com/python-programming/methods/list/extend)|Adds items of lists and other iterables to the end of the list|
|[insert()](https://www.programiz.com/python-programming/methods/list/insert)|Inserts an item at the specified index|
|[remove()](https://www.programiz.com/python-programming/methods/list/remove)|Removes item present at the given index|
|[pop()](https://www.programiz.com/python-programming/methods/list/pop)|Returns and removes item present at the given index|
|[clear()](https://www.programiz.com/python-programming/methods/list/clear)|Removes all items from the list|
|[index()](https://www.programiz.com/python-programming/methods/list/index)|Returns the index of the first matched item|
|[count()](https://www.programiz.com/python-programming/methods/list/count)|Returns the count of the specified item in the list|
|[sort()](https://www.programiz.com/python-programming/methods/list/sort)|Sorts the list in ascending/descending order|
|[reverse()](https://www.programiz.com/python-programming/methods/list/reverse)|Reverses the item of the list|
|[copy()](https://www.programiz.com/python-programming/methods/list/copy)|Returns the shallow copy of the list|

**Note:** Lists are similar to arrays (or dynamic arrays) in other programming languages. When people refer to arrays in Python, they often mean lists, even though there is a numeric array type in Python.