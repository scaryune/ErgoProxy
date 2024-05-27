# C++ Exception Handling

An exception is an unexpected event that occurs during program execution. For example,

```
divide_by_zero = 7 / 0;
```

The above code causes an exception as it is not possible to divide a number by **0**.

The process of handling these types of errors in C++ is known as exception handling.

In C++, we handle exceptions with the help of the `try` and `catch` blocks, along with the `throw` keyword.

- `try` **-** code that may raise an exception
- `throw` - throws an exception when an error is detected
- `catch` - code that handles the exception thrown by the `throw` keyword

**Note:** The `throw` statement is not compulsory, especially if we use standard C++ exceptions.

---

## Syntax for Exception Handling in C++

The basic syntax for exception handling in C++ is given below:

```
try {

    // code that may raise an exception
    throw argument;
}

catch (exception) {
    // code to handle exception
} 
```

Here, we have placed the code that might generate an exception inside the `try` block. Every `try` block is followed by the `catch` block.

When an exception occurs, the `throw` statement throws an exception, which is caught by the `catch` block.

The `catch` block cannot be used without the `try` block.

---

## Example 1: C++ Exception Handling

```
// program to divide two numbers
// throws an exception when the divisor is 0

#include <iostream>
using namespace std;

int main() {

    double numerator, denominator, divide;

    cout << "Enter numerator: ";
    cin >> numerator;

    cout << "Enter denominator: ";
    cin >> denominator;

    try {

        // throw an exception if denominator is 0
        if (denominator == 0)
            throw 0;

        // not executed if denominator is 0
        divide = numerator / denominator;
        cout << numerator << " / " << denominator << " = " << divide << endl;
    } 

    catch (int num_exception) {
        cout << "Error: Cannot divide by " << num_exception << endl;
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output 1**

Enter numerator: 72
Enter denominator: 0
Error: Cannot divide by 0

**Output 2**

Enter numerator: 72
Enter denominator: 3
72 / 3 = 24

The above program divides two numbers and displays the result. But an exception occurs if the denominator is **0**.

To handle the exception, we have put the code `divide = numerator / denominator;` inside the try block. Now, when an exception occurs, the rest of the code inside the `try` block is skipped.

The `catch` block catches the thrown exception and executes the statements inside it.

If none of the statements in the `try` block generates an exception, the `catch` block is skipped.

![C++ try, throw and catch Statements](https://www.programiz.com/sites/tutorial2program/files/cpp-try-catch.png "C++ try, throw and catch Statements")

Working of try, throw, and catch statements in C++

Notice that we have thrown the `int` literal **0** with the code `throw 0;`.

We can throw any literal or variable or class, depending on the situation and depending on what we want to execute inside the `catch` block.

The `catch` parameter `int num_exception` takes the value passed by the `throw` statement i.e. the literal **0**.

---

## Catching All Types of Exceptions

In exception handling, it is important that we know the types of exceptions that can occur due to the code in our `try` statement.

This is so that we can use the appropriate `catch` parameters. Otherwise, the `try...catch` statements might not work properly.

If we do not know the types of exceptions that can occur in our `try` block, then we can use the ellipsis symbol `...` as our `catch` parameter.

```
try {
    // code
}
catch (...) {
    // code
} 
```

---

## C++ Multiple catch Statements

In C++, we can use multiple `catch` statements for different kinds of exceptions that can result from a single block of code.

```
try {
    // code
} 
catch (exception1) {
    // code
} 
catch (exception2) {
    // code
} 
catch (...) {
    // code
}
```

Here, our program catches `exception1` if that exception occurs. If not, it will catch `exception2` if it occurs.

If there is an error that is neither `exception1` nor `exception2`, then the code inside of `catch (...) {}` is executed.

**Notes:**

- `catch (...) {}` should always be the final block in our `try...catch` statement. This is because this block catches all possible exceptions and acts as the default `catch` block.

- It is not compulsory to include the default `catch` block in our code.

---

### Example 2: C++ Multiple catch Statements

This program divides two numbers and stores the result in an array element. There are two possible exceptions that can occur in this program:

- If the array is out of bounds i.e. if the index of the array is greater than the size of the array
- If a number is divided by **0**

These exceptions are caught in multiple `catch` statements.

```
#include <iostream>
using namespace std;

int main() {
    
    double numerator, denominator, arr[4] = {0.0, 0.0, 0.0, 0.0};
    int index;
    
    cout << "Enter array index: ";
    cin >> index;
    
    try {
        
        // throw exception if array out of bounds
        if (index >= 4)
            throw "Error: Array out of bounds!";
            
        // not executed if array is out of bounds
        cout << "Enter numerator: ";
        cin >> numerator;
    
        cout << "Enter denominator: ";
        cin >> denominator;

        // throw exception if denominator is 0
        if (denominator == 0)
            throw 0;

        // not executed if denominator is 0
        arr[index] = numerator / denominator;
        cout << arr[index] << endl;
    }

    // catch "Array out of bounds" exception
    catch (const char* msg) {
        cout << msg << endl;
    }

    // catch "Divide by 0" exception
    catch (int num) {
        cout << "Error: Cannot divide by " << num << endl;
    }

    // catch any other exception
    catch (...) {
        cout << "Unexpected exception!" << endl;
    }
    
    return 0;    
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output 1**

Enter array index: 5
Error: Array out of bounds!

Here, the array arr only has **4** elements. So, index cannot be greater than **3**.

In this case, index is **5**. So we throw a string literal `"Error: Array out of bounds!"`. This exception is caught by the first `catch` block.

Notice the `catch` parameter `const char* msg`. This indicates that the `catch` statement takes a `string` literal as an argument.

**Output 2**

Enter array index: 2
Enter numerator: 5
Enter denominator: 0
Error: Cannot divide by 0

Here, the denominator is **0**. So we throw the `int` literal **0**. This exception is caught by the second `catch` block.

If any other exception occurs, it is caught by the default `catch` block.

**Output 3**

Enter array index: 2
Enter numerator: 5
Enter denominator: 2
2.5

Here, the program runs without any problem as no exception occurs.

---

## C++ Standard Exception

C++ has provided us with a number of standard exceptions that we can use in our exception handling. Some of them are shown in the table below.

|Exception|Description|
|---|---|
|`std::exception`|The parent class of all C++ exceptions.|
|`std::bad_alloc`|Thrown when a dynamic memory allocation fails.|
|`std::bad_cast`|Thrown by C++ when an attempt is made to perform a `dynamic_cast` to an invalid type.|
|`std::bad_exception`|Typically thrown when an exception is thrown and it cannot be rethrown.|

There are many other standard exceptions in C++.

These exceptions are defined in the `exception` header file.

To learn more, visit our _C++ Standard Exceptions_ tutorial.

- [](https://www.programiz.com/cpp-programming/exception-handling#introduction)
- [](https://www.programiz.com/cpp-programming/exception-handling#syntax)
- [](https://www.programiz.com/cpp-programming/exception-handling#example1)
- [](https://www.programiz.com/cpp-programming/exception-handling#catch-all)
- [](https://www.programiz.com/cpp-programming/exception-handling#multiple-catch)
- [](https://www.programiz.com/cpp-programming/exception-handling#example2)
- [](https://www.programiz.com/cpp-programming/exception-handling#standard-exceptions)

[

  


](https://www.programiz.com/cpp-programming/functors "C++ Functor")