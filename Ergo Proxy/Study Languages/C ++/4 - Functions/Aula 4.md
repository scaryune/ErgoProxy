# C++ Inline Functions

In C++, we can declare a function as inline. This copies the function to the location of the function call in compile-time and may make the program execution faster.

Before following this tutorial, be sure to visit the [C++](https://www.programiz.com/cpp-programming/function) [Functions](https://www.programiz.com/cpp-programming/function).

---

## Inline Functions

To create an inline function, we use the `inline` keyword. For example,

```
inline returnType functionName(parameters) {
    // code
}
```

Notice the use of keyword `inline` before the function definition.

---

## C++ Inline Function

```
#include <iostream>
using namespace std;

inline void displayNum(int num) {
    cout << num << endl;
}

int main() {
    // first function call
    displayNum(5);

    // second function call
    displayNum(8);

    // third function call
    displayNum(666);

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

5
8
666

Here is how this program works:

![Working of inline functions in C++](https://cdn.programiz.com/sites/tutorial2program/files/cpp-inline-functions.png)

Working of inline functions in C++

Here, we created an inline function named `displayNum()` that takes a single integer as a parameter.

We then called the function 3 times in the `main()` function with different arguments. Each time `displayNum()` is called, the compiler copies the code of the function to that call location.