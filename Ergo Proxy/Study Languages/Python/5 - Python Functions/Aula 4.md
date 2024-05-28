# Python Global Keyword

In Python, the `global` keyword allows us to modify the variable outside of the current scope.

It is used to create a global variable and make changes to the variable in a local context.

Before we learn about the `global` keyword, make sure you have got some basics of [Python Variable Scope](https://www.programiz.com/python-programming/global-local-nonlocal-variables).

---

## Access and Modify Python Global Variable

First let's try to access a global variable from the inside of a [function](https://www.programiz.com/python-programming/function),

```
c = 1 # global variable

def add():
    print(c)

add()

# Output: 1
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

Here, we can see that we have accessed a global variable from the inside of a function.

However, if we try to modify the global variable from inside a function as:

```
# global variable
c = 1 

def add():

     # increment c by 2
    c = c + 2

    print(c)

add()
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

UnboundLocalError: local variable 'c' referenced before assignment

This is because we can only access the global variable but cannot modify it from inside the function.

The solution for this is to use the `global` keyword.

---

### Example: Changing Global Variable From Inside a Function using global

```
# global variable
c = 1 

def add():

    # use of global keyword
    global c

    # increment c by 2
    c = c + 2 

    print(c)

add()

# Output: 3 
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

In the above example, we have defined c as the `global` keyword inside `add()`.

Then, we have incremented the variable c by **2**, i.e `c = c + 2`.

As we can see while calling `add()`, the value of global variable c is modified from **1** to **3**.

---

## Global in Nested Functions

In Python, we can also use the `global` keyword in a nested function. For example,

```
def outer_function():
    num = 20

    def inner_function():
        global num
        num = 25
    
    print("Before calling inner_function(): ", num)
    inner_function()
    print("After calling inner_function(): ", num)

outer_function()
print("Outside both function: ", num)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

Before calling inner_function():  20
After calling inner_function():  20
Outside both function:  25

In the above example, we declared a global variable inside the nested function `inner_function()`.

Inside `outer_function()`, num has no effect of the `global` keyword.

Before and after calling `inner_function()`, num takes the value of the local variable i.e `num = 20`.

Outside of the `outer_function()` function, num will take the value defined in the `inner_function()` function i.e `x = 25`.

This is because we have used the `global` keyword in num to create a global variable inside the `inner_function()` function (local scope).

So, if we make any changes inside the `inner_function()` function, the changes appear outside the local scope, i.e. `outer_function()`.

---

## Rules of global Keyword

The basic rules for `global` keyword in Python are:

- When we create a variable inside a function, it is local by default.
- When we define a variable outside of a function, it is global by default. You don't have to use the `global` keyword.
- We use the `global` keyword to read and write a global variable inside a function.
- Use of the `global` keyword outside a function has no effect.

---

