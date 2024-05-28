# Python Functions

A function is a block of code that performs a specific task.

Suppose we need to create a program to make a circle and color it. We can create two functions to solve this problem:

1. function to create a circle
2. function to color the shape

Dividing a complex problem into smaller chunks makes our program easy to understand and reuse.

---

## Create a Function

Let's create our first function.

```
def greet():
    print('Hello World!')
```

Here are the different parts of the program:

![Create a Python Function](https://www.programiz.com/sites/tutorial2program/files/create-function-python.png "Create a Python Function")

Create a Python Function

Here, we have created a simple function named `greet()` that prints **Hello World!**

**Note:** When writing a function, pay attention to indentation, which are the spaces at the start of a code line.

In the above code, the `print()` statement is indented to show it's part of the function body, distinguishing the function's definition from its body.

---

## Calling a Function

In the above example, we have declared a function named `greet()`.

```
def greet():
    print('Hello World!')
```

If we run the above code, we won't get an output.

It's because creating a function doesn't mean we are executing the code inside it. It means the code is there for us to use if we want to.

To use this function, we need to call the function.

**Function Call**

```
greet()
```

---

## Example: Python Function Call

```
def greet():
    print('Hello World!')

# call the function
greet()

print('Outside function')
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

Hello World!
Outside function

In the above example, we have created a function named `greet()`. Here's how the control of the program flows:

![Python Function Working](https://www.programiz.com/sites/tutorial2program/files/working-of-function-python.png "Python Function Working")

Working of Python Function

Here,

1. When the function `greet()` is called, the program's control transfers to the function definition.
2. All the code inside the function is executed.
3. The control of the program jumps to the next statement after the function call.

---

## Python Function Arguments

Arguments are inputs given to the function.

```
def greet(name):
    print("Hello", name)

# pass argument
greet("John")
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Sample Output 1**

Hello John

Here, we passed '`John'` as an argument to the `greet()` function.

We can pass different arguments in each call, making the function re-usable and dynamic.

Let's call the function with a different argument.

```
greet("David")
```

**Sample Output 2**

Hello David

---

## Example: Function to Add Two Numbers

```
# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

# function call with two values
add_numbers(5, 4)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

Sum: 9

In the above example, we have created a function named `add_numbers()` with arguments: num1 and num2.

![Python Function Argument](https://www.programiz.com/sites/tutorial2program/files/function-argument-python.png "Python Function Argument")

Python Function with Arguments

---

Parameters and Arguments

[](https://www.programiz.com/python-programming/variables-constants-literals "Python variables")

---

## The return Statement

We return a value from the function using the `return` statement.

```
# function definition
def find_square(num):
    result = num * num
    return result

# function call
square = find_square(3)

print('Square:', square)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

Square: 9

In the above example, we have created a function named `find_square()`. The function accepts a number and returns the square of the number.

![How function works in Python?](https://www.programiz.com/sites/tutorial2program/files/function-return-value-python-updated.png "Working of Python Functions")

Working of functions in Python

**Note:** The `return` statement also denotes that the function has ended. Any code after `return` is not executed.

---

## The pass Statement

The `pass` statement serves as a placeholder for future code, preventing errors from empty code blocks.

It's typically used where code is planned but has yet to be written.

```
def future_function():
    pass

# this will execute without any action or error
future_function()  
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Note**: To learn more, visit [Python Pass Statement](https://www.programiz.com/python-programming/pass-statement).

---

## Python Library Functions

Python provides some built-in functions that can be directly used in our program.

We don't need to create the function, we just need to call them.

Some Python library functions are:

1. [print()](https://www.programiz.com/python-programming/methods/built-in/print) - prints the string inside the quotation marks
2. `sqrt()` - returns the square root of a number
3. [pow()](https://www.programiz.com/python-programming/methods/built-in/pow) - returns the power of a number

These library functions are defined inside the module. And to use them, we must include the module inside our program.

For example, `sqrt()` is defined inside the [math](https://www.programiz.com/python-programming/modules/math) module.

**Note**: To learn more about library functions, please visit [Python Library Functions](https://www.programiz.com/python-programming/methods).

---

## Example: Python Library Function

```
import math

# sqrt computes the square root
square_root = math.sqrt(4)

print("Square Root of 4 is",square_root)

# pow() comptes the power
power = pow(2, 3)

print("2 to the power 3 is",power)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

Square Root of 4 is 2.0
2 to the power 3 is 8

Here, we imported a `math` module to use the library functions `sqrt()` and `pow()`.

---

