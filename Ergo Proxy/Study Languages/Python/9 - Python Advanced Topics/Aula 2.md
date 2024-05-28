# Python Lambda/Anonymous Function

In Python, a lambda function is a special type of function without the function name. For example,

```
lambda : print('Hello World')
```

Here, we have created a lambda function that prints `'Hello World'`.

Before you learn about lambdas, make sure to know about [Python Functions](https://www.programiz.com/python-programming/function).

---

## Python Lambda Function Declaration

We use the `lambda` [keyword](https://www.programiz.com/python-programming/keywords-identifier) instead of `def` to create a lambda function. Here's the syntax to declare the lambda function:

```
lambda argument(s) : expression 
```

Here,

- `argument(s)` - any value passed to the lambda function
- `expression` - expression is executed and returned

Let's see an example,

```
greet = lambda : print('Hello World')
```

Here, we have defined a lambda function and assigned it to the [variable](https://www.programiz.com/python-programming/variables-constants-literals) named greet.

To execute this lambda function, we need to call it. Here's how we can call the lambda function

```
# call the lambda
greet()
```

The lambda function above simply prints the text `'Hello World'`.

**Note**: This lambda function doesn't have any [argument](https://www.programiz.com/python-programming/function-argument).

---

## Example: Python Lambda Function

```
# declare a lambda function
greet = lambda : print('Hello World')

# call lambda function
greet()

# Output: Hello World
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

In the above example, we have defined a lambda function and assigned it to the greet variable.

When we call the lambda function, the [print()](https://www.programiz.com/python-programming/methods/built-in/print) statement inside the lambda function is executed.

---

## Python lambda Function with an Argument

Similar to normal functions, a `lambda` function can also accept arguments. For example,

```
# lambda that accepts one argument
greet_user = lambda name : print('Hey there,', name)

# lambda call
greet_user('Delilah')

# Output: Hey there, Delilah
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

In the above example, we have assigned a lambda function to the greet_user variable.

Here, `name` after the `lambda` keyword specifies that the lambda function accepts the argument named `name`.

Notice the call of the lambda function,

```
greet_user('Delilah')
```

Here, we have passed a [string](https://www.programiz.com/python-programming/string) value `'Delilah'` to our lambda function.

Finally, the statement inside the lambda function is executed.