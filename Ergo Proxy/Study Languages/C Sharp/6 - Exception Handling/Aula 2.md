# C# Exception Handling

An exception is an unexpected event that occurs during program execution. For example,

```
int divideByZero = 7 / 0;
```

The above code causes an exception as it is not possible to divide a number by **0**.

Exceptions abnormally terminate the flow of the program instructions, we need to handle those exceptions. Responding or handling exceptions is called **Exception Handling**.

---

## C# Exception Handling Blocks

C# provides built-in blocks to handle exceptions. They are: `try..catch` and `finally`.

### try…catch block

The `try..catch` block is used to handle exceptions in C#. Here's the syntax of `try...catch` block:

```
try
{
    // code that may raise an exception 
}
catch (Exception e)
{
    // code that handles the exception
}
```

Here, we place the code that might generate an exception inside the `try` block. The `try` block then throws the exception to the `catch` block which handles the raised exception. For example,

```
try
{
    int num = 0;
    // code that may raise an exception 
    int divideByZero = 7 / num;
}
catch (Exception e)
{
    Console.WriteLine("Exception has occurred");
}
```

Here, we are trying to divide a number by **zero**. In this case, an exception occurs. Hence, we have enclosed this code inside the `try` block. The `catch` block notifies the user about the occurred exception.

---

## Example: Exception Handling Using try…catch

```
using System;
class Program
{
    static void Main()
    {
        string[] colors = { "Red", "Blue", "Green" };

        try
        {
            // code that may raise an exception 
            Console.WriteLine(colors[5]);
        }
        catch (IndexOutOfRangeException e)
        {
            Console.WriteLine("An exception occurred: " + e.Message);
        }
    }
}
```

**Output**

An exception occurred: Index was outside the bounds of the array.

In the above example, notice the code,

```
Console.WriteLine(colors[5]);
```

Since there is no element at index **5** of the `colors` array, the above code raises an exception. So we have enclosed this code in the `try` block.

When the program encounters this code, `IndexOutOfRangeException` occurs. And, the exception is caught by the `catch` block and executes the code inside the `catch` block.

Notice the code,

```
catch (IndexOutOfRangeException e)
{
    Console.WriteLine("An exception occurred: " + e.Message);
}
```

Here, `catch` is taking an instance of the `IndexOutOfRangeException` class. And inside the block we have used the `Message` property of this class to display a message.

**Note:** If you want to learn more about the `Exception` class methods and properties visit here.

---

## try…catch…finally block

We can also use `finally` block with `try` and `catch` block. The `finally` block is always executed whether there is an exception or not.

The syntax of the `try…catch…finally` block is:

```
try
{
    // code that may raise an exception
}
catch (Exception e)
{
    // code that handles the exception 
}
finally
{
    // this code is always executed
}
```

![finally block is always getting executed](https://www.programiz.com/sites/tutorial2program/files/csharp-finally-block.png "C# finally block")

C# finally block

We can see in the above image that the `finally` block is executed in both cases. The `finally` block is executed:

- after `try` and `catch` block - when exception has occurred
- after `try` block - when exception doesn't occur

The `try..catch..finally` block can be collectively used to handle exceptions.

Now let's look at an example of exception handling using `try…catch…finally`.

---

## Example: Exception Handling Using try…catch…finally block

```
using System;
public class Program
{
    static void Main()
    {
        // take first int input from user
        Console.WriteLine("Enter first number:");
        int firstNumber = int.Parse(Console.ReadLine());

        // take second int input from user
        Console.WriteLine("Enter second number:");
        int secondNumber = int.Parse(Console.ReadLine());

        try
        {
            // code that may raise raise an exception 
            int divisionResult = firstNumber / secondNumber;
            Console.WriteLine("Division of two numbers is: " + divisionResult);
        }

        // this catch block gets executed only when an exception is raised
        catch (Exception e)
        {
            Console.WriteLine("An exception occurred: " + e.Message);
        }

        finally
        {
            // this code is always executed whether of exception occurred or not 
            Console.WriteLine("Sum of two numbers is: " + (firstNumber + secondNumber));
        }
    }
}
```

**Output**

Enter first number:
8
Enter second number:
0
An exception occurred: Attempted to divide by zero.
Sum of two numbers is: 8

In the above example, we have tried to perform division and addition operations to two `int` input values using `try...catch…finally`.

Notice the code,

```
try
{
    // code that may raise raise an exception 
    int divisionResult = firstNumber / secondNumber;
}
```

Here, we have enclosed the code that performs division operation inside `try` because this code may raise the `DivideByZeroException` exception.

There are two cases in this program:

**Case I** - When exception occurs in `try`, the `catch` block is executed followed by the `finally` block.

**Case II** - The `finally` block is directly executed after the `try` block if an exception doesn't occur. For example, if we enter **9** and **2**, exception doesn't occur in the `try` block and we get the following output:

```
// Output when exception doesn't occur 
Enter first number:
9
Enter second number:
2
Division of two numbers is: 4
Sum of two numbers is: 11
```

---

## Frequently Asked Questions

C# Nested try-catch

C# Generic catch block

Exception Handling Using Two catch Blocks

- [](https://www.programiz.com/csharp-programming/exception-handling#introduction)
- [](https://www.programiz.com/csharp-programming/exception-handling#exception-handling-blocks)
- [](https://www.programiz.com/csharp-programming/exception-handling#exception-handling-using-try-catch)
- [](https://www.programiz.com/csharp-programming/exception-handling#try-catch-finally)
- [](https://www.programiz.com/csharp-programming/exception-handling#exception-handling-using-try-catch-finally)

[

  


](https://www.programiz.com/csharp-programming/exception "C# Exception and It's Types")