# C++ Type Conversion

C++ allows us to convert data of one type to that of another. This is known as type conversion.

There are two types of type conversion in C++:

1. Implicit Conversion
2. Explicit Conversion (also known as Type Casting)

---

## Implicit Type Conversion

The type conversion that is automatically done by the compiler is known as implicit type conversion. This type of conversion is also known as automatic conversion.

---

### Example 1: Conversion From int to double

```
// Working of implicit type-conversion

#include <iostream>
using namespace std;

int main() {
   // assigning an int value to num_int
   int num_int = 9;

   // declaring a double type variable
   double num_double;
 
   // implicit conversion
   // assigning int value to a double variable
   num_double = num_int;

   cout << "num_int = " << num_int << endl;
   cout << "num_double = " << num_double << endl;

   return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

num_int = 9
num_double = 9

In the program, we have assigned an `int` data to a `double` variable.

```
num_double = num_int;
```

Here, the `int` value is automatically converted to `double` by the compiler before it is assigned to the num_double variable. This is an example of implicit type conversion.

---

### Example 2: Automatic Conversion from double to int

```
#include <iostream>
using namespace std;

int main() {

   int num_int;
   double num_double = 9.99;

   // implicit conversion
   // assigning a double value to an int variable
   num_int = num_double;

   cout << "num_int = " << num_int << endl;
   cout << "num_double = " << num_double << endl;

   return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

num_int = 9
num_double = 9.99

In the program, we have assigned a `double` data to an `int` variable.

```
num_int = num_double;
```

Here, the `double` value is automatically converted to `int` by the compiler before it is assigned to the num_int variable. This is also an example of implicit type conversion.

**Note:** Since `int` cannot have a decimal part, the digits after the decimal point are truncated in the above example.

---

### Data Loss During Conversion (Narrowing Conversion)

As we have seen from the above example, conversion from one [data type](https://www.programiz.com/cpp-programming/data-types) to another is prone to data loss. This happens when data of a larger type is converted to data of a smaller type.

Let's see the data loss during type conversion in integer data types.

![Possible Data Loss During Type Conversion in Integer Data Type](https://www.programiz.com/sites/tutorial2program/files/cpp-type-conversion-integer.png "Possible Data Loss During Type Conversion in Integer Data Type")

Possible Data Loss During Type Conversion in Integer Data Type

Now, let's see the data loss during type conversion in floating point data types.

![Possible Data Loss During Type Conversion in Floating Point Data Type](https://www.programiz.com/sites/tutorial2program/files/cpp-type-conversion-float.png "Possible Data Loss During Type Conversion in Floating Point Data Type")

Possible Data Loss During Type Conversion in Floating Point Data Type

**Note:** The data loss may occur during conversion between integer and floating point data types.

---

## C++ Explicit Conversion

When a programmer manually changes data from one type to another, this is known as **explicit conversion**. This type of conversion is also known as **type casting**.

There are three major ways in which we can use explicit conversion in C++:

1. C++ named casts
2. C-style type casting (also known as **cast notation**)
3. Function notation (also known as **old C++ style type casting**)

**Warning**: C-style and function-style casting should not be used in modern C++ code.

---

## C++ Named Casts

C++ has four expressions for explicit type conversion. They are known as **C++ named casts**. They are:

- `static_cast`
- `dynamic_cast`
- `const_cast`
- `reinterpret_cast`

To learn about each operator, visit [C++ Named Casts](http://programiz.com/cpp-programming/type-conversion-operators).

---

## C-style Type Casting

As the name suggests, this type of casting is favored by the **C programming language**. It is also known as **cast notation**.

**Syntax**

```
(data_type)expression;
```

For example,

```
// initializing int variable
int num_int = 26;

// declaring double variable
double num_double;

// converting from int to double
num_double = (double)num_int;
```

---

## Function-style Casting

We can also use the function-like notation to cast data from one type to another.

**Syntax**

```
data_type(expression);
```

For example,

```
// initializing int variable
int num_int = 26;

// declaring double variable
double num_double;

// converting from int to double
num_double = double(num_int);
```

---

## Example 3: Type Casting

```
#include <iostream>

using namespace std;

int main() {
    // initializing a double variable
    double num_double = 3.56;
    cout << "num_double = " << num_double << endl;

    // C-style conversion from double to int
    int num_int1 = (int)num_double;
    cout << "num_int1   = " << num_int1 << endl;

    // function-style conversion from double to int
    int num_int2 = int(num_double);
    cout << "num_int2   = " << num_int2 << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

num_double = 3.56
num_int1   = 3
num_int2   = 3

We used both the **C style type conversion** and the **function-style casting for type conversion** and displayed the results. Since they perform the same task, both give us the same output.

Warning on Using C-style and Function-style Casting

---

**Also Read:**

- [C++ string to int and Vice-versa](https://www.programiz.com/cpp-programming/string-int-conversion)
- [C++ string to float, double and Vice-versa](https://www.programiz.com/cpp-programming/string-float-conversion)
- [C++ Type Modifiers](https://www.programiz.com/cpp-programming/type-modifiers)
- [C++ float and double](https://www.programiz.com/cpp-programming/float-double)

- [](https://www.programiz.com/cpp-programming/type-conversion#introduction)
- [](https://www.programiz.com/cpp-programming/type-conversion#implicit)
- [](https://www.programiz.com/cpp-programming/type-conversion#example1)
- [](https://www.programiz.com/cpp-programming/type-conversion#example2)
- [](https://www.programiz.com/cpp-programming/type-conversion#data-loss)
- [](https://www.programiz.com/cpp-programming/type-conversion#explicit)
- [](https://www.programiz.com/cpp-programming/type-conversion#named-casts)
- [](https://www.programiz.com/cpp-programming/type-conversion#c-style-casting)
- [](https://www.programiz.com/cpp-programming/type-conversion#function-notation)
- [](https://www.programiz.com/cpp-programming/type-conversion#example3)

[

  


](https://www.programiz.com/cpp-programming/class-templates "C++ Class Templates")