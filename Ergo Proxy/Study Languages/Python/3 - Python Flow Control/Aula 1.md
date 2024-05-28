# Python if...else Statement

In computer programming, the `if` statement is a conditional statement. It is used to execute a block of code only when a specific condition is met. For example,

Suppose we need to assign different grades to students based on their scores.

1. If a student scores above **90**, assign grade **A**
2. If a student scores above **75**, assign grade **B**
3. If a student scores above **65**, assign grade **C**

These conditional tasks can be achieved using the `if` statement.

---

## Python if Statement

An `if` statement executes a block of code only if the specified condition is met.

**Syntax**

```
if condition:
    # body of if statement
```

Here, if the condition of the `if` statement is:

- **True** - the body of the `if` statement executes.
- **False** - the body of the `if` statement is skipped from execution.

Let's look at an example.

![Working of if Statement](https://www.programiz.com/sites/tutorial2program/files/python-if.png "Working of if Statement")

Working of if Statement

**Note:** Be mindful of the indentation while writing the `if` statements. Indentation is the whitespace at the beginning of the code.

```
if number > 0:
    print('Number is positive')
```

Here, the spaces before the [print()](https://www.programiz.com/python-programming/methods/built-in/print "Python print()") statement denote that it's the body of the `if` statement.

---

### Example: Python if Statement

```
number = 10

# check if number is greater than 0
if number > 0:
    print('Number is positive')

print('This statement always executes')
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Sample Output 1**

Number is positive
This statement always executes

In the above example, we have created a [variable](https://www.programiz.com/python-programming/variables-constants-literals) named number. Notice the test `condition`,

```
number > 0 
```

As the number is greater than **0**, the condition evaluates `True`. Hence, the body of the `if` statement executes.

**Sample Output 2**

Now, let's change the value of the number to a negative integer, say **-5**.

```
number = -5
```

Now, when we run the program, the output will be:

This statement always executes

This is because the value of the number is less than **0**. Hence, the condition evaluates to `False`. And, the body of the `if` statement is skipped.

---

## Python if...else Statement

An `if` statement can have an optional `else` clause. The `else` statement executes if the condition in the `if` statement evaluates to `False`.

**Syntax**

```
if condition:
    # body of if statement

else:
    # body of else statement
```

Here, if the `condition` inside the `if` statement evaluates to

- **True** - the body of `if` executes, and the body of `else` is skipped.
- **False** - the body of `else` executes, and the body of `if` is skipped

Let's look at an example.

![Working of if…else Statement](https://www.programiz.com/sites/tutorial2program/files/python-if-else.png "Working of if…else Statement")

Working of if…else Statement

---

### Example: Python if…else Statement

```
number = 10

if number > 0:
    print('Positive number')

else:
    print('Negative number')

print('This statement always executes')
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Sample Output 1**

Positive number
This statement always executes

In the above example, we have created a variable named number.

Since the value of the number is **10**, the `condition` evaluates to `True`. Hence, code inside the body of `if` is executed.

**Sample Output 2**

If we change the value of the variable to a negative integer, let's say **-5**, our output will be:

Negative number
This statement always executes

Here, the test condition evaluates to `False`. Hence code inside the body of `else` is executed.

---

## Python if…elif…else Statement

The `if...else` statement is used to execute a block of code among two alternatives.

However, if we need to make a choice between more than two alternatives, we use the `if...elif...else` statement.

**Syntax**

```
if condition1:
    # code block 1

elif condition2:
    # code block 2

else: 
    # code block 3
```

Here,

- `if condition1` - This checks if `condition1` is `True`. If it is, the program executes **code block 1**.

- `elif condition2` - If `condition1` is not `True`, the program checks `condition2`. If `condition2` is `True`, it executes **code block 2**.

- `else` - If neither `condition1` nor `condition2` is `True`, the program defaults to executing **code block 3**.

Let's look at an example.

![Working of if…elif…else Statement](https://www.programiz.com/sites/tutorial2program/files/python-elif.png "Working of if…elif…else Statement")

Working of if…elif…else Statement

---

### Example: Python if…elif…else Statement

```
number = 0

if number > 0:
    print('Positive number')

elif number <0:
    print('Negative number')

else:
    print('Zero')

print('This statement is always executed')
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

Zero
This statement is always executed

In the above example, we have created a variable named number.

Since the value of the number is **0**, both the test conditions evaluate to `False`.

Hence, the statement inside the body of `else` is executed.

---

## Python Nested if Statements

It is possible to include an `if` statement inside another `if` statement. For example,

```
number = 5

# outer if statement
if number >= 0:
    # inner if statement
    if number == 0:
      print('Number is 0')
    
    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

Number is positive

Here's how this program works.

![Working of Nested if Statement](https://www.programiz.com/sites/tutorial2program/files/python-nested-if.png "Working of Nested if Statement")

Working of Nested if Statement

---

## More on Python if…else Statement

Python`if`Shorthand

[](https://www.programiz.com/python-programming/online-compiler)

[](https://www.programiz.com/python-programming/online-compiler)

Ternary Operator in Python`if...else`

[](https://www.programiz.com/python-programming/online-compiler)

[](https://www.programiz.com/python-programming/online-compiler)

Logical Operators to Add Multiple Conditions

[](https://www.programiz.com/python-programming/online-compiler)

[](https://www.programiz.com/python-programming/operators#logical)

---

## Also Read

- [Python pass Statement](https://www.programiz.com/python-programming/pass-statement)
- [Python break and continue](https://www.programiz.com/python-programming/break-continue)

- [](https://www.programiz.com/python-programming/if-elif-else#introduction)
- [](https://www.programiz.com/python-programming/if-elif-else#if)
- [](https://www.programiz.com/python-programming/if-elif-else#example)
- [](https://www.programiz.com/python-programming/if-elif-else#if-else)
- [](https://www.programiz.com/python-programming/if-elif-else#example)
- [](https://www.programiz.com/python-programming/if-elif-else#if-elif-else)
- [](https://www.programiz.com/python-programming/if-elif-else#example)
- [](https://www.programiz.com/python-programming/if-elif-else#nested-if-statements)
- [](https://www.programiz.com/python-programming/if-elif-else#recommended)

 Challenge

Write a function to check whether a student passed or failed his/her examination.

- Assume the pass marks to be **50**.
- Return `Passed` if the student scored more than 50. Otherwise, return `Failed`.

1

2

def pass_fail(score):

