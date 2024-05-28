# Python for Loop

In Python, a `for` loop is used to iterate over sequences such as [lists](https://www.programiz.com/python-programming/list "Python Lists"), [strings](https://www.programiz.com/python-programming/string), [tuples](https://www.programiz.com/python-programming/tuple), etc.

```
languages = ['Swift', 'Python', 'Go']

# access elements of the list one by one
for i in languages:
    print(i)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

Swift
Python
Go

In the above example, we have created a list called languages. As the list has 3 elements, the loop iterates **3** times.

The value of `i` is

- `Swift` in the first iteration.
- `Python` in the second iteration.
- `Go` in the third iteration.

---

## for loop Syntax

```
for val in sequence:
    # statement(s)
```

Here, val accesses each item of the `sequence` on each iteration. The loop continues until we reach the last item in the sequence.

---

## Flowchart of Python for Loop

![Working of Python for Loop](https://www.programiz.com/sites/tutorial2program/files/python-for-loop-working.png "Working of Python for Loop")

Flowchart of Python for Loop

---

## Example: Loop Through a String

```
language = 'Python'

# iterate over each character in language
for x in language:
    print(x)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

P
y
t
h
o
n

Here, we have printed each character of the string language using a `for` loop.

---

## for Loop with Python range()

In Python, the [range()](https://www.programiz.com/python-programming/methods/built-in/range) function returns a sequence of numbers. For example,

```
values = range(4)
```

Here, `range(4)` returns a sequence of **0**, **1**, **2** ,and **3**.

Since the `range()` function returns a sequence of numbers, we can iterate over it using a `for` loop. For example,

```
# iterate from i = 0 to i = 3
for i in range(4):
    print(i)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

0
1
2
3

Here, we used the `for` loop to iterate over a range from **0** to **3**.

This is how the above program works.

|Iteration|Value of `i`|`print(i)`|Last item in sequence?|
|---|---|---|---|
|1st|`0`|Prints `0`|No|
|2nd|`1`|Prints `1`|No|
|3rd|`2`|Prints `2`|No|
|4th|`3`|Prints `3`|Yes  <br>The loop terminates.|

---

## More on Python for Loop

Python for loop with`else`clause

[](https://www.programiz.com/python-programming/online-compiler)

[](https://www.programiz.com/python-programming/break-continue)

Using for loop without accessing items

[](https://www.programiz.com/python-programming/online-compiler)

[](https://www.programiz.com/python-programming/online-compiler)

Nested for loops

[](https://www.programiz.com/python-programming/online-compiler)

**