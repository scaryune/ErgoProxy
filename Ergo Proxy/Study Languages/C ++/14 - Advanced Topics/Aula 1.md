# C++ 11

C++11, officially known as **ISO/IEC 14882:2011**, was released in 2011 and was a significant milestone in the evolution of the C++ programming language.

It introduced a plethora of new features and enhancements that made C++ more powerful.

---

## Features Introduced in C++ 11

Here are the most important features introduced in C++ 11:

- The `auto` keyword
- Range based `for` loop
- Lambda Expressions
- Smart Pointers
- The `constexpr` keyword
- The `nullptr` keyword
- Type traits
- Thread support
- Delegating constructor
- Deleted and defaulted functions

Let's start by exploring the `auto` keyword.

---

## C++ auto Keyword

The `auto` keyword allows C++11 to automatically deduce the type of the variable from its initializer.

```
#include <iostream>
using namespace std;

int main() {

    // x is deduced as int
    auto x = 42;
    
    // pi is deduced as double
    auto pi = 3.1415926535;  

    cout << "x: " << x << endl;
    cout << "pi: " << pi << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

x: 42
pi: 3.14159

Here, the compiler is capable of deducing the type of both variable x and pi from their initializer, so we don't need to explicitly mention their type. However, when using `auto`, the variable must be always initialized.

```
auto x; // error: must be always initialized
```

**Note**: `auto` is a type placeholder in C++, not a type itself. So, it cannot be used in casts or operators like `sizeof` or `typeid`.

---

## Range Based for Loops

[Range based for loops](https://www.programiz.com/cpp-programming/ranged-for-loop) in C++ executes a loop for a range.

**Syntax**

```
for (range_initialization : range_container) {
    // loop statements
}
```

Here,

- range_initialization - creates an iterating variable.
- range_container - container to iterate over.

For example,

```
vector<int> numbers = {1, 2, 3};

// loop through the numbers vector
for (int num : numbers) {

    // print vector element
    cout << num << endl;
}
```

**Note:** range-based-loops should be preferred over normal [for loops](https://www.programiz.com/cpp-programming/for-loop) whenever possible to avoid out of bound errors.

---

### Example 1: C++ Range Based for Loop

```
#include <iostream>
#include <vector>
using namespace std;

int main() {

    // create a vector of integers
    vector<int> numbers = {1, 2, 3, 4, 5};

    // use a range-based for loop
    // to iterate through the vector
    for (const auto& num : numbers) {
        cout << num << " ";
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

1 2 3 4 5 

Here, we have declared the iterating variable num and iterated over the container numbers using a [range based for loop.](https://www.programiz.com/cpp-programming/ranged-for-loop)

---

## Lambda Expressions

Lambda expressions allow you to create anonymous functions in a concise manner. They are especially useful when you need to pass small functions as arguments to other functions.

**Syntax**

```
[capture_clause] (parameter_list) -> return_type {
    // lambda body: Code to be executed
}
```

Here,

- capture_clause - specifies which variables from the surrounding scope are accessible within the lambda function.
- parameter_list - defines the parameters the function accepts.
- -> return_type - declares the return type of the function.

**Note**: We can omit return_type for auto deduction of types unless there are multiple possible return values of different types.

To learn more, visit our [C++ Lambda](https://www.programiz.com/cpp-programming/lambda-expression) tutorial.

---

### Example 2: C++ Lambda Expression

```
#include <iostream>
using namespace std;

int main() {

    // define a lambda function named 'add'
    // that takes two integers  and returns their sum
    auto add = [] (int a, int b) {
        return a + b;
    };

    // call the lambda with arguments 3 and 4
    int result = add(3, 4);

    // print the result.
    cout << "Result: " << result << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Result: 7

Here, we created a lambda function add() that takes in two arguments a and b and returns their sum.

---

## Smart Pointers

C++11 introduced smart pointers that automatically manage memory and help prevent memory leaks. Basically, a smart pointer automatically releases the memory it manages when it goes out of scope.

Smart pointers are of two types:

- **Unique Pointers** have exclusive ownership of the objects they point to.
- **Shared Pointers** allow multiple shared pointers to own a single object.

**Syntax**

```
// unique pointer
std::unique_ptr<data_type> unique_pointer = std::make_unique<data_type>(args...);

// shared pointer
std::shared_ptr<Type> shared_pointer = std::make_shared<data_type>(args...);
```

**Note:** We need to import the `<memory>` header file to use smart pointers.

---

### Example 3: C++ Smart Pointers

```
#include <iostream>
#include <memory>
using namespace std;

int main() {

    // create a shared pointer to an integer with value 42
    shared_ptr<int> shared_pointer = make_shared<int>(42);

    // create a unique pointer to a double with value 3.14
    unique_ptr<double> unique_pointer = make_unique<double>(3.14);

    // print the value pointed to by shared_ptr
    cout << "shared_pointer: " << *shared_pointer << endl;

    // print the value pointed to by unique_ptr
    cout << "unique_pointer: " << *unique_pointer << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

shared_pointer: 42
unique_pointer: 3.14

---

## Move Semantics

Move semantics allows the resources owned by an object to be moved into another object instead of copying them. This optimizes performance by avoiding deep copies.

We use the `move()` function to implement move semantics. For example,

```
#include <iostream>
#include <vector>
using namespace std;

int main() {

    // create an integer vector
    vector<int> source = {1, 2, 3};

    // move the contents of source to another vector
    vector<int> destination = move(source);

    // print the destination vector
    cout << "Destination Vector Contents: ";
    for (const int num : destination) {
        cout << num << "  ";
    }
    
    // print the size of the destination vector
    cout << "\nDestination Vector Size: " << destination.size();

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Destination Vector Contents: 1  2  3  
Destination Vector Size: 3

Here, we have used the `move()` function to move the contents from source to destination.

```
vector<int> destination = move(source);
```

---

## C++ constexpr Keyword

The `constexpr` keyword allows you to specify that a variable or function can be evaluated at compile-time. For example,

```
constexpr int square(int x) {
    return x * x;
}

// computed at compile-time
int result = square(5);
```

Here, we have used the `constexpr` keyword with the `square()` function. As a result, `square(5)` can be evaluated at compile time rather than run time.

This can boost the performance of the code and ensures that the expressions are initialized with a value that is known at compile time.

---

## Null Pointer

The introduction of `nullptr` provides a safer alternative to using `NULL` for null pointers.

```
int* ptr = nullptr;
```

**Note**: Always prefer `nullptr` over `NULL` because of the safety `nullptr` provides over `NULL`.

---

## Type Traits

In C++, type traits are a group of templates that are used to gather information about types at compile time, and are a powerful tool for template metaprogramming.

This means that before your program runs, the compiler can understand things about the types you're using—like whether a type is an integer, if it can be copied, or if it's a class with a certain function.

They are part of the Standard Template Library (STL) and included within the `<type_traits>` header file.

Type traits are implemented using [class templates](https://www.programiz.com/cpp-programming/class-templates) or [function templates](https://www.programiz.com/cpp-programming/function-template). Here's a sample code of a function template.

```
template <typename T>
void process(T value) {

    if (std::is_pointer<T>::value) {
        // handle pointers
    }
    else if (std::is_integral<T>::value) {
        // handle integers
    }
}
```

---

## Thread Support

C++11 added a standardized threading library that allows you to create and manage threads.

```
#include <iostream>
#include <thread>

using namespace std;

void sayHello(){
  cout << "Hello, from the spawned thread\n";
}

int main(){
    // create a std::thread object
    std::thread t(sayHello);

    std::cout << "Hello, from the main thread\n";

    // wait for the thread to complete its job
    t.join();

}
```

**Output:**

Hello, from the main thread
Hello, from the spawned thread

**Note:** The output is execution dependent, so you may not get the same output every time you run it.

Every thread has to have an initial function, from where the execution of the new thread begins.

Thus we created a `std::thread` object t by passing in a function sayHello, which we want the thread to execute.

The program now has 2 threads - one executing the main function and the other executing the `sayHello` function.

---

## Delegating Constructors

In C++11, a constructor may call another constructor of the same class. For example,

```
#include <iostream>
using namespace std;

class Complex {
    int img;
    int real;

public:

    // constructor #1 (target constructor)
    Complex(int i, int r) : img(i), real(r) {}

    // constructor #2 (delegating constructor)
    // pass two zeroes as arguments to target constructor 
    Complex() : Complex(0, 0) {
        cout << "Delegating constructor" << endl;
        cout << "img = " << img << endl;
        cout << "real  = " << real << endl;
    }
};

int main() {

    // create an instance of class Complex
    // using the delegating constructor
    Complex obj; 

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Delegating constructor
img = 0
real = 0

Here, the delegating constructor invokes the target constructor.

---

## Deleted and Defaulted Functions

**1. Deleted Function**

They are member functions that have been intentionally marked as **deleted**. This means that the functions cannot be used, and any attempt to call them will result in a compilation error.

Deleting functions is useful when you want to prevent certain operations on your class.

```
class My_Class {
public:

    // delete the default constructor
    My_Class() = delete;

    // delete a member function
    void do_something() = delete; 
};
```

**2. Defaulted Function**

They are used to explicitly request the compiler to generate default implementations for certain member functions.

This is particularly useful when you want to take advantage of the compiler-generated versions while still providing custom behavior for other functions.

```
class Another_Class {
public:

    // use the compiler-generated default constructor
    Another_Class() = default;

    // define a custom constructor
    Another_Class(int x) : value(x) {} 

private:
    int value;
};
```

---

### Example 4: C++ Deleted and Defaulted Functions

```
class Example {
public:

    // defaulted default constructor
    Example() = default;
    
    // deleted copy constructor
    Example(const Example&) = delete; 
};

int main() {

    // allowed: default constructor is used
    Example obj1; 
    
    // error: copy constructor is deleted
    // Example obj2 = obj1;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

Here,

- We can create an object of the `Example` class using the default constructor.
- We cannot create a copy of an object of `Example` because the copy constructor is deleted.

- [](https://www.programiz.com/cpp-programming/cpp-11#introduction)
- [](https://www.programiz.com/cpp-programming/cpp-11#auto-keyword)
- [](https://www.programiz.com/cpp-programming/cpp-11#range-based-for-loops)
- [](https://www.programiz.com/cpp-programming/cpp-11#lambda-expressions)
- [](https://www.programiz.com/cpp-programming/cpp-11#smart-pointers)
- [](https://www.programiz.com/cpp-programming/cpp-11#move-semantics)
- [](https://www.programiz.com/cpp-programming/cpp-11#constexpr-keyword)
- [](https://www.programiz.com/cpp-programming/cpp-11#null-pointer)
- [](https://www.programiz.com/cpp-programming/cpp-11#type-traits)
- [](https://www.programiz.com/cpp-programming/cpp-11#thread-support)
- [](https://www.programiz.com/cpp-programming/cpp-11#delegating-constructors)
- [](https://www.programiz.com/cpp-programming/cpp-11#deleted-and-defaulted-functions)

[

  


](https://www.programiz.com/cpp-programming/operator-overloading "C++ Operator Overloading")