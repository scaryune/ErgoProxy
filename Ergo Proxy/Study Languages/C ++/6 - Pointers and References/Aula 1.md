# C++ Pointers

In C++, pointers are variables that store the memory addresses of other variables.

---

## Address in C++

Every [variable](https://www.programiz.com/cpp-programming/variables-literals) we declare in our program has an associated location in the memory, which we call the memory address of the variable.

If we have a variable var in our program, &var returns its memory address. For example,

```
#include <iostream>
using namespace std;

int main()
{
    // declare variables
    int var1 = 3;
    int var2 = 24;
    int var3 = 17;

    // print address of var1
    cout << "Address of var1: "<< &var1 << endl;

    // print address of var2
    cout << "Address of var2: " << &var2 << endl;

    // print address of var3
    cout << "Address of var3: " << &var3 << endl;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Address of var1: 0x7fff5fbff8ac
Address of var2: 0x7fff5fbff8a8
Address of var3: 0x7fff5fbff8a4

Here, `0x` at the beginning represents the address in the hexadecimal form.

Notice that the first address differs from the second by **4** bytes, and the second address differs from the third by **4** bytes.

The difference is because the size of an `int` is **4** bytes in a **64-bit** system.

**Note:** You may not get the same results when you run the program. This is because the address depends on the environment in which the program runs.

---

## C++ Pointers

Here is how we can declare pointers:

```
int *point_var;
```

Here, we have declared a variable point_var which is a pointer to an `int`.

We can also declare pointers in the following way:

```
int* point_var; // preferred syntax
```

---

## Assigning Addresses to Pointers

Here is how we can assign addresses to pointers:

```
int var = 5;
int* point_var = &var;
```

Here, `5` is assigned to the variable var. And the address of var is assigned to the point_var pointer with the code `point_var = &var`.

**Note:** It is a good practice to initialize pointers as soon as they are declared.

---

## Get the Value from the Address Using Pointers

To get the value pointed by a pointer, we use the `*` operator. For example:

```
int var = 5;

// assign address of var to point_var
int* point_var = &var;

// access value pointed by point_var
cout << *point_var << endl;   // Output: 5
```

In the above code, the address of var is assigned to point_var. We have used the `*point_var` to get the value stored in that address.

When `*` is used with pointers, it's called the **dereference operator**. It operates on a pointer and gives the value pointed by the address stored in the pointer. That is, `*point_var = var`.

**Note:** In C++, point_var and *point_var are completely different. We cannot do something like `*point_var = &var;`. Here, point_var is a pointer that stores the address of variable it points to while `*point_var` returns the value stored at the address pointed by point_var.

---

## Example 1: Working of C++ Pointers

```
#include <iostream>
using namespace std;
int main() {
    int var = 5;

    // store address of var
    int* point_var = &var;

    // print value of var
    cout << "var = " << var << endl;

    // print address of var
    cout << "Address of var (&var) = " << &var << endl
         << endl;

    // print pointer point_var
    cout << "point_var = " << point_var << endl;

    // print the content of the address point_var points to
    cout << "Content of the address pointed to by point_var (*point_var) = " << *point_var << endl;
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

var = 5
Address of var (&var) = 0x61ff08

point_var = 0x61ff08
Content of the address pointed to by point_var (*point_var) = 5

![Working of C++ Pointers](https://www.programiz.com/sites/tutorial2program/files/cpp-pointer-working_0.png "Working of C++ Pointers")

Working of C++ pointers

---

## Changing Value Pointed by Pointers

If point_var points to the address of var, we can change the value of var by using *point_var.

For example,

```
int var = 5;
int* point_var = *var;

// change value at address point_var
*point_var = 1;

cout << var << endl; // Output: 1
```

Here, point_var and `&var` have the same address; the value of var will also be changed when *point_var is changed.

---

## Example 2: Changing Value Pointed by Pointers

```
#include <iostream>
using namespace std;
int main() {
    int var = 5;

    // store address of var
    int* point_var = &var;

    // print var
    cout << "var = " << var << endl;

    // print *point_var
    cout << "*point_var = " << *point_var << endl
         << endl;

    cout << "Changing value of var to 7:" << endl;

    // change value of var to 7
    var = 7;

    // print var
    cout << "var = " << var << endl;

    // print *point_var
    cout << "*point_var = " << *point_var << endl
         << endl;

    cout << "Changing value of *point_var to 16:" << endl;

    // change value of var to 16
    *point_var = 16;

    // print var
    cout << "var = " << var << endl;

    // print *point_var
    cout << "*point_var = " << *point_var << endl;
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

var = 5
*point_var = 5

Changing value of var to 7:
var = 7
*point_var = 7

Changing value of *point_var to 16:
var = 16
*point_var = 16

Here point_var holds the address of var, and by dereferencing point_var with `*point_var`, we can access and modify the value stored at that address, which in turn affects the original variable var.

---

## Common Mistakes When Working with Pointers

Suppose we want a pointer point_var to point to the address of var. Then,

```
int var = 5;

// Wrong! 
// point_var is an address but var is not
int* point_var = var;

// Wrong!
// &var is an address
// *point_var is the value stored in &var
*point_var = &var;

// Correct! 
// point_var is an address and so is &var
point_var = &var;

 // Correct!
// both *point_var and var are values
*point_var = var;
```

---

**Also Read:**

- [How to represent an array using a pointer?](https://www.programiz.com/cpp-programming/pointers-arrays)
- [How to use pointers with functions?](https://www.programiz.com/cpp-programming/pointers-function)
- [How to use pointers with structures?](https://www.programiz.com/cpp-programming/structure-pointer)
- [C++Pass by Reference](https://www.programiz.com/cpp-programming/pointers-function)

- [](https://www.programiz.com/cpp-programming/pointers#introduction)
- [](https://www.programiz.com/cpp-programming/pointers#address)
- [](https://www.programiz.com/cpp-programming/pointers#pointer-variable)
- [](https://www.programiz.com/cpp-programming/pointers#assign)
- [](https://www.programiz.com/cpp-programming/pointers#get-value)
- [](https://www.programiz.com/cpp-programming/pointers#example1)
- [](https://www.programiz.com/cpp-programming/pointers#changing-value)
- [](https://www.programiz.com/cpp-programming/pointers#example2)
- [](https://www.programiz.com/cpp-programming/pointers#common-mistakes)

[

  


](https://www.programiz.com/cpp-programming/string-class "C++ String Class")