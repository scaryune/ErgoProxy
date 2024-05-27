# C# Exception and It's Types

An exception is an unexpected event that occurs during program execution. For example,

```
int divideByZero = 7 / 0;
```

The above code causes an exception as it is not possible to divide a number by **0**.

Let's learn about C# Exceptions in detail.

---

## C# Exception Hierarchy

![two classes derived from the base class - Exception](https://www.programiz.com/sites/tutorial2program/files/csharp-exception-hierarchy.png "exception hierarchy in C#")

exception hierarchy in C#

The above image shows the exception hierarchy in C#. C# provides a base class named `Exception` which is later derived into other classes.

The major two exception classes derived from the `Exception` class are:

- `SystemException` - also called built-in exceptions
- `ApplicationException` - also called user-defined exceptions

Let's learn about both of them in detail.

---

## C# Built-in Exception

The built-in exceptions are also called `SystemException` exceptions. In C#, all the built-in exception classes are derived from the `SystemException` class. This class handles all the system-related exceptions.

Some of the common system exceptions are:

1. `StackOverflowException` - This exception is thrown when the execution stack exceeds the stack size. Normally occurs when we use an infinite loop in the program.

2. `ArithmeticException` - This exception is thrown for errors in arithmetic, casting, or conversion. It is a base class for exception classes like:

- `DivideByZeroException` - This exception is thrown when an integer is divided by **0**. For example, when we try to perform **5** divided by **0**.

- `NotFiniteNumberException` - This exception is thrown when a floating-point value is positive or negative infinity or NaN (Not-a-Number).

- `OverFlowException` - This exception is thrown when the result produced by the operation is out of range. For example,

3. `ValidationException` - This exception is thrown when an input value is not valid. For example, if we enter an integer value in a field that expects a `DateTime` value, this exception is thrown.

4. `ArgumentException` - This exception is thrown when we provide one invalid argument in a method. For example, when we pass an argument of a data type that doesn't match specified parameters during a method's call, then this exception occurs.

---

## Example: C# SystemException

```
using System;
class Program
{
    // an array containing string values
    static string[] colors = { "Red", "Green", "Pink" };
    static void Main()
    {
        // print the array element present at 3rd index position 
        Console.WriteLine(colors[3]);
    }
}
```

**Output**

Unhandled exception. System.IndexOutOfRangeException: Index was outside the bounds of the array.

In the above example, we are trying to access the index **3** element of the `colors` array element.

Since there is no element at index **3**, the program throws a system exception `IndexOutOfRangeException`.

---

## C# User-defined Exception

Till now we learned about built-in exceptions in C#. We can also create user-defined exceptions which are known as Application level exceptions.

The `ApplicationException` class is the base class from which we can derive application-level exceptions.

Suppose we want to create an exception in an application that does not allow the age of a participant to be more than **18**. Let's name that exception - `InvalidAgeException`.

To create the `InvalidAgeException` exception, we derive it from the `ApplicationException` class as,

```
// user-defined exception class derived from 
// the ApplicationException base class  
class InvalidAgeException : ApplicationException
{
    // constructor for the InvalidAgeException class
    InvalidAgeException()
    {
        Console.WriteLine("Exception occurred: Invalid Age");
    }
}
```

Here, we have defined a user-defined exception class named `InvalidAgeException` which is derived from the `ApplicationException` class.

We can write custom codes inside user-defined `InvalidAgeException` class and define the nature of that exception class.

Now we can raise the `InvalidAgeException` exception whenever the age restriction is violated.

---

## C# Error and Exception

**Errors** represent conditions such as compilation error, syntax error, error in the logical part of the code, library incompatibility, infinite recursion, etc.

Errors are usually beyond the control of the programmer and we should not try to handle errors.

**Exceptions** can be caught and handled by the program.

Now we know about exceptions, we will learn about [External Handling](https://www.programiz.com/csharp-programming/exception-handling) in the next tutorial.