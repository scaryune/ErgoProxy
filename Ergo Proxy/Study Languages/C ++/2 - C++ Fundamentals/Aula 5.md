# C++ Constants

The `const` keyword (which stands for **constant**) is used to specify that the value of a variable cannot be changed anywhere in the program, either intentionally or accidentally. For example,

```
// makes PI a constant
const double PI = 3.14;
```

**Note:** The standard naming convention for constants is that they must all be in uppercase letters. For example,

```
const int MAGIC_NUMBER = 42;
```

---

## Create const Variables

A `const` variable must be initialized during declaration and cannot be changed later.

```
// invalid since PI is not initialized
const double PI;
```

Here, we get an error because the `const` variable PI has not been initialized.

Instead, we should create `const` variables by initializing them in the following way:

```
// initialize const with a value
const double PI = 3.14;
```

---

## Example 1: C++ const

```
#include <iostream>
using namespace std;

int main() {
    
    // initialize a const PI
    const double PI = 3.14;
    
    int radius = 4;

    // use the const in a calculation
    double area = PI * radius * radius;
    
    cout << "Area of circle with radius " << radius << " is: " << area;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Area of circle with radius 4 is: 50.24

In the above example, we have initialized a constant variable PI.

```
const double PI = 3.14;
```

Then, we have used this constant variable to calculate the area of a circle:

```
double area = PI * radius * radius;
```

---

## Const References

We can also make references using the `const` keyword. There are different types of such references with different behaviors. These are

|Reference Type|Description|
|---|---|
|Constant reference to a constant variable|Both the variable and the reference are constant.|
|Constant reference to a non-constant variable|The variable is non-constant but the reference is constant.|

---

## Const Reference to a Const Variable

In C++, we can create a `const` reference to a `const` variable using a reference variable. For example,

```
#include <iostream>
using namespace std;

int main() {

    // initialize a constant PI  
    const double PI = 3.14;
  
    // create a read-only reference to PI
    const double &PI_REF = PI;
  
    cout << "PI: " << PI;
    cout << "\nPI_REF: " << PI_REF;
  
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

PI: 3.14
PI_REF: 3.14

In the above example, we have created a constant reference to a constant or a constant reference.

So, we'll get an error if we try to modify the value of PI_REF.

```
// error: assignment of read-only reference 'PI_REF'
PI_REF = 90;
```

---

## Frequently Asked Question

Is it possible to create a constant reference to a non-constant variable?

[](https://www.programiz.com/cpp-programming/online-compiler)

---

## Passing as a Constant Reference

We can use a constant parameter to ensure that the passed argument is not modified by the function body.

For instance, we can ensure that the vector we pass is not modified by using the following code:

```
int sum(const vector<int> nums) {
    // function body
}
```

Although the `const` keyword in the above code guarantees that nums cannot be modified, it creates a local copy of nums, which costs memory.

A better way to handle this is passing as a **constant reference** using the following code:

```
int sum(const vector<int> &nums) {
    // function body
}
```

Here, &nums is a reference, and the `const` keyword signifies that it is a constant.

---

### Example 3: Passing as a Constant Reference

```
#include <iostream>
#include <vector>
using namespace std;

// take a const reference as argument
int sum(const vector<int> &nums) {
    int total = 0;

    for(auto num: nums){
        total += num;
    }

    return total;
}

int main() {

    vector<int> nums = {1, 2, 3, 4, 5};

    cout << "Sum: " << sum(nums);

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Sum: 15

In the above example, we have passed the nums vector as a constant reference:

```
int sum(const vector<int> &nums) {
    // code
}
```

Here, instead of creating a local copy of the nums vector, we are passing a reference that cannot be modified. This is faster as well as more space efficient.

---

## Const and Pointers

Like with references, we can also make different types of pointers using the `const` keyword. These are:

|Pointer Type|Description|
|---|---|
|Pointers to a Const|The pointer is a non-constant but the value being pointed to is a constant.|
|Const Pointer|The pointer is a constant but the value being pointed is a non-constant.|
|Const Pointer to a Const|Both the pointer and the value being pointed are constant.|

---

## Pointers to a Const

A pointer to a const is a [pointer](https://www.programiz.com/cpp-programming/pointers) variable that points to a constant variable. These pointers

- allow us to change the address the pointer is pointing to,
- don't allow us to change the value stored in those constant variables.

For example,

```
#include <iostream>
using namespace std;

int main() {

    // initialize a constant TOTAL_MONTHS  
    const int TOTAL_MONTHS = 12;
 
    // MONTHS_PTR is a pointer to an int const
    const int *MONTHS_PTR = &TOTAL_MONTHS;
  
    cout << "TOTAL_MONTHS: " << TOTAL_MONTHS << endl;
    cout << "*MONTHS_PTR: " << *MONTHS_PTR << endl;

    // create another int constant
    const int HALF_MONTHS = 6;

    // MONTHS_PTR now points to HALF_MONTHS
    MONTHS_PTR = &HALF_MONTHS;

    cout << endl;
  
    cout << "HALF_MONTHS: " << HALF_MONTHS << endl;
    cout << "*MONTHS_PTR: " << *MONTHS_PTR;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

TOTAL_MONTHS: 12
*MONTHS_PTR: 12

HALF_MONTHS: 6
*MONTHS_PTR: 6

In the above example, we have created an integer constant TOTAL_MONTHS. Then, we created a pointer to that constant called MONTHS_PTR**.**

```
// points to const int TOTAL_MONTHS
const int *MONTHS_PTR = &TOTAL_MONTHS;
```

We'll get an error if we try to modify the value at MONTHS_PTR.

```
// error: assignment of read-only location '* TOTAL_MONTHS_PTR'
*TOTAL_MONTHS_PTR = 10;
```

This is because the value TOTAL_MONTHS is a constant and cannot be modified.

However, we can change the address pointed by MONTHS_PTR to point to some other variable without any error.

```
const int HALF_MONTHS = 6;
MONTHS_PTR = &HALF_MONTHS;
```

---

## Const Pointer

A **const pointer** is a [pointer](https://www.programiz.com/cpp-programming/pointers) in which we can change the value pointed by the pointer, but cannot change the variable it points to. For example,

```
#include <iostream>
using namespace std;

int main() {
    
    string country1 = "Nepal";
    string country2 = "USA";
  
    cout << "Initially, country1: " << country1 << endl;
  
    // PTR1 is a const pointer to country1
    string *const PTR1 = &country1;
  
    // change the value of country1 using PTR1
    *PTR1 = country2;
  
    cout << "Finally, country1: " << country1;
  
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Initially, country1: Nepal
Finally, country1: USA

In the above example, we have created a **const pointer.**

```
// PTR1 is a const pointer to a string
string *const PTR1 = &country1;
```

Initially, the value of country1 is `Nepal`. Then, we have modified the value of country1 using PTR1:

```
// change the value of variable pointed by PTR1
*PTR1 = country2;
```

So the new value of country1 becomes `USA`.

But we'll get an error if we try changing the variable pointed by PTR1 from country1 to country2:

```
// error: assignment of read-only variable 'PTR1'
PTR1 = &country2;
```

---

## Const Pointer to a Const

A **const pointer to a const** is a pointer through which we can neither change the variable it points to nor its value. For example,

```
#include <iostream>
using namespace std;

int main() {
    
    // create a const variable
    const string COUNTRY1 = "Nepal";
    
    // create a const pointer to const
    const string *const PTR = &COUNTRY1;

    cout << *PTR;
  
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Nepal

---

## Frequently Asked Question

What are the differences between pointer to const and const pointer?

  
  

---

## Const Expression

Constant expressions were introduced in C++ 11. They are expressions whose:

- value cannot change,
- and can be evaluated at compile time.

The reason we want to use them in C++ is to avoid calculation being done multiple times at runtime.

We use the `constexpr` keyword to create constant expressions. For example,

```
// declare a function as constexpr
constexpr int add_numbers(int a, int b) {...}

// declare a variable as constexpr
constexpr int sum = add_numbers(660, 6);
```

**Note:** We can't use `constexpr` variables to call functions that are not declared as `constexpr`:

---

### Example 4: C++ Const Expression

```
#include <iostream>
using namespace std;

// a constexpr function that
// returns nth fibonacci number
constexpr int fib(int n) {

    // returns n if n <= 1
    // else, recursively calls fib(n - 1) + fib(n - 2)
    return n <= 1 ? n: fib(n - 1) + fib(n - 2);   
}

int main() {

    // two constexpr variables that store
    // the return values of constexpr function
    constexpr int fibonacci_five = fib(5);
    constexpr int fibonacci_ten = fib(10);

    cout << "fib(5) : "<< fibonacci_five << endl;
    cout << "fib(10) : "<< fibonacci_ten;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

fib(5) : 5
fib(10) : 55

In the above example, we have created a constant expression (in the form of a function) to evaluate the **nth** fibonacci number.

```
constexpr int fib(int n) {    
    return n <= 1 ? n: fib(n - 1) + fib(n - 2);   
}
```

Notice that we have added the `constexpr` keyword before the return type which tells the compiler that the function to be evaluated at compile time.

Then we calculate the **5th** and **10th** fibonacci numbers using two `constexpr` variables:

```
constexpr int fibonacci_five = fib(5);
constexpr int fibonacci_ten = fib(10);
```

Now, notice that we are making the normal function call. The only difference is that the calculation is done at compile time.

```
// function not declared as constexpr
int fib(int n) {...}

// error: call to non-'constexpr' function 'int fib(int)'
constexpr int fibonacci_five = fib(5);
```

However, we can use **non-constexpr** variables to call `constexpr` functions:

```
constexpr int fib(int n) {...}

// valid code
int fibonacci_five = fib(5);
```

---

## Const Member Functions

Const member functions ensure that the data members of an object are not changed. We create such functions with the following syntax:

```
return_type function_name() const {
    // function body
}
```

**Properties of Const Member Functions**

- We cannot change the values of the member variables inside a const member function.
- We can only call const member functions from a **constant object**.

---

### Example 5: Const Member Functions

```
#include <iostream>
using namespace  std;

class Rectangle {
private:
    int breadth, length;

public:
    Rectangle(int length, int breadth){
        this->breadth = breadth;
        this->length = length;
    }

     // constant member function
    int get_area() const {
        return length * breadth;
    }

    // non-constant member function
    int get_perimeter() {
        return 2 * (length + breadth);
    }
};

int main() {

    // create a const Rectangle object
    const Rectangle RECT = Rectangle(7, 6);

    // call the const member function
    cout << "Area: " << RECT.get_area() << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Area: 42

In the above example, we have created a class `Rectangle` with the following member functions:

- `get_area()` - a constant member function
- `get_perimeter()`- a normal member function

In `main()`, we created a **constant object** named RECT:

```
// create a const Rectangle object
const Rectangle RECT = Rectangle(7, 6);
```

Then, we called the **const member function** `get_area()` using the constant object RECT**:**

```
// code to call const member function
RECT.get_area();
```

**Calling Non-Constant Member Functions**

However, we will get an error if we try to call the non-const member function `get_perimeter()`:

```
// error
RECT.get_perimeter();
```

This is because a constant object cannot call a non-constant member function.

However, a non-constant object can call both constant and non-constant member functions.

The reasoning behind this is simple: we create a constant object so that the data members are not modified. But non-constant member functions have the capability to modify the data members.

Thus, the purpose of a constant object is at odds with the purpose of a non-constant member function, which is why we can't perform the function call.

- [](https://www.programiz.com/cpp-programming/constants#introduction)
- [](https://www.programiz.com/cpp-programming/constants#example)
- [](https://www.programiz.com/cpp-programming/constants#const-reference)
- [](https://www.programiz.com/cpp-programming/constants#reference-variable)
- [](https://www.programiz.com/cpp-programming/constants#pass-by-const)
- [](https://www.programiz.com/cpp-programming/constants#const-and-pointers)
- [](https://www.programiz.com/cpp-programming/constants#pointer-to-const)
- [](https://www.programiz.com/cpp-programming/constants#const-pointer)
- [](https://www.programiz.com/cpp-programming/constants#const-pointer-const)
- [](https://www.programiz.com/cpp-programming/constants#const-expression)
- [](https://www.programiz.com/cpp-programming/constants#const-member-function)

[

  


](https://www.programiz.com/cpp-programming/type-modifiers "C++ Type Modifiers")