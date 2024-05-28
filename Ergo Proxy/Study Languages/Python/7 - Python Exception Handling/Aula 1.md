# Python Exceptions

An exception is an unexpected event that occurs during program execution. For example,

```
divide_by_zero = 7 / 0
```

The above code causes an exception as it is not possible to divide a number by **0**.

Let's learn about Python Exceptions in detail.

---

## Python Logical Errors (Exceptions)

Errors that occur at runtime (after passing the syntax test) are called **exceptions** or **logical errors**.

For instance, they occur when we

- try to open a file(for reading) that does not exist (`FileNotFoundError`)
- try to divide a number by zero (`ZeroDivisionError`)
- try to import a module that does not exist (`ImportError`) and so on.

Whenever these types of runtime errors occur, Python creates an exception object.

If not handled properly, it prints a traceback to that error along with some details about why that error occurred.

Let's look at how Python treats these errors:

```
divide_numbers = 7 / 0
print(divide_numbers)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

Traceback (most recent call last):
 File "<string>", line 1, in <module>
ZeroDivisionError: division by zero

Here, while trying to divide `7 / 0`, the program throws a system exception `ZeroDivisionError`

---

## Python Built-in Exceptions

Illegal operations can raise exceptions. There are plenty of built-in exceptions in Python that are raised when corresponding errors occur.

We can view all the built-in exceptions using the built-in `local()` function as follows:

```
print(dir(locals()['__builtins__']))
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

Here, `locals()['__builtins__']` will return a module of built-in exceptions, [functions](https://www.programiz.com/python-programming/function), and attributes and `dir` allows us to list these attributes as [strings](https://www.programiz.com/python-programming/string).

Some of the common built-in exceptions in Python programming along with the error that cause them are listed below:

|Exception|Cause of Error|
|---|---|
|`AssertionError`|Raised when an `assert` statement fails.|
|`AttributeError`|Raised when attribute assignment or reference fails.|
|`EOFError`|Raised when the `input()` function hits end-of-file condition.|
|`FloatingPointError`|Raised when a floating point operation fails.|
|`GeneratorExit`|Raise when a generator's `close()` method is called.|
|`ImportError`|Raised when the imported module is not found.|
|`IndexError`|Raised when the index of a sequence is out of range.|
|`KeyError`|Raised when a key is not found in a dictionary.|
|`KeyboardInterrupt`|Raised when the user hits the interrupt key (`Ctrl+C` or `Delete`).|
|`MemoryError`|Raised when an operation runs out of memory.|
|`NameError`|Raised when a variable is not found in local or global scope.|
|`NotImplementedError`|Raised by abstract methods.|
|`OSError`|Raised when system operation causes system related error.|
|`OverflowError`|Raised when the result of an arithmetic operation is too large to be represented.|
|`ReferenceError`|Raised when a weak reference proxy is used to access a garbage collected referent.|
|`RuntimeError`|Raised when an error does not fall under any other category.|
|`StopIteration`|Raised by `next()` function to indicate that there is no further item to be returned by iterator.|
|`SyntaxError`|Raised by parser when syntax error is encountered.|
|`IndentationError`|Raised when there is incorrect indentation.|
|`TabError`|Raised when indentation consists of inconsistent tabs and spaces.|
|`SystemError`|Raised when interpreter detects internal error.|
|`SystemExit`|Raised by `sys.exit()` function.|
|`TypeError`|Raised when a function or operation is applied to an object of incorrect type.|
|`UnboundLocalError`|Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.|
|`UnicodeError`|Raised when a Unicode-related encoding or decoding error occurs.|
|`UnicodeEncodeError`|Raised when a Unicode-related error occurs during encoding.|
|`UnicodeDecodeError`|Raised when a Unicode-related error occurs during decoding.|
|`UnicodeTranslateError`|Raised when a Unicode-related error occurs during translating.|
|`ValueError`|Raised when a function gets an argument of correct type but improper value.|
|`ZeroDivisionError`|Raised when the second operand of division or modulo operation is zero.|

If required, we can also define our own exceptions in Python. To learn more about them, visit [Python User-defined Exceptions](https://www.programiz.com/python-programming/user-defined-exception).

We can handle these built-in and user-defined exceptions in Python using `try`, `except` and `finally` statements. To learn more about them, visit [Python try, except and finally statements](https://www.programiz.com/python-programming/exception-handling).

---

## Python Error and Exception

**Errors** represent conditions such as compilation error, syntax error, error in the logical part of the code, library incompatibility, infinite recursion, etc.

Errors are usually beyond the control of the programmer and we should not try to handle errors.

**Exceptions** can be caught and handled by the program.

Now we know about exceptions, we will learn about handling exceptions in the next tutorial.

