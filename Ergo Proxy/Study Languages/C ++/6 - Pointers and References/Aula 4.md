# C++ Pass by Reference

In the [C++ Functions](https://www.programiz.com/cpp-programming/function) tutorial, we learned about passing arguments to a function. This method used is called pass by value because the actual value is passed.

However, there is another way of passing arguments called **pass by reference**.

Pass by reference is a method of argument passing in functions where the _references_ of actual parameters are passed to the function, rather than their values.

For example,

```
// function that takes value as parameter

void func1(int num_val) {
    // code
}

// function that takes reference as parameter
// notice the & before the parameter
void func2(int& num_ref) {
    // code
}

int main() {
    int num = 5;

    // pass by value
    func1(num);

    // pass by reference
    func2(num);

    return 0;
}
```

Notice the `&` in `void func2(int& num_ref)`. This denotes that we are using the reference of the [variable](https://www.programiz.com/cpp-programming/variables-literals) as our parameter.

So, when we call the `func2()` function in `main()` by passing the variable num as an argument, we are actually passing the reference of the num variable instead of the value **5**.

---

## Example: Pass by Reference

```
#include <iostream>
using namespace std;

// function definition to swap values
void swap(int& n1, int& n2) {
    int temp;
    temp = n1;
    n1 = n2;
    n2 = temp;
}

int main() {

    // initialize variables
    int a = 1, b = 2;

    cout << "Before swapping" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    // call function to swap numbers
    swap(a, b);

    cout << "\nAfter swapping" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Before swapping
a = 1
b = 2

After swapping
a = 2
b = 1

In this program, we passed the variables a and b to the `swap()` function. Notice the function definition,

```
void swap(int& n1, int& n2)
```

Here, we used `&` to denote that the function accepts references as its parameters.

Hence, the compiler can identify that instead of actual values, the reference of the variables is passed to function parameters.

In the `swap()` function, the function parameters n1 and n2 are pointing to the same value as the variables a and b respectively. Hence the swapping takes place on actual value.

---

## Pass by const Reference

When the values of variables do not need to be changed, we can pass them as `const` references.

Let's look at an example.

```
#include <iostream>
using namespace std;

// function to add two numbers 
// using const references
int add(const int& num1, const int& num2) {
    return num1 + num2;
}

int main() {
    int number1, number2;

    // take input
    cout << "Enter the first number: ";
    cin >> number1;

    cout << "Enter the second number: ";
    cin >> number2;

    // call add function
    int sum = add(number1, number2);

    // displaying the result
    cout << "The sum of " << number1 << " and " << number2 << " is " << sum << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Enter the first number: 1
Enter the second number: 2
The sum of 1 and 2 is 3

Here, we've used the `const` keyword to pass values using `const` references.

Using `const` references prevents the values from being changed inside the function. For example, let's try to use const references to swap two numbers.

```
#include <iostream>
using namespace std;

// function definition to swap values
// using const references
void swap(const int& n1,const int& n2) {
    int temp;
    temp = n1;
    n1 = n2;
    n2 = temp;
}

int main() {

    // initialize variables
    int a = 1, b = 2;

    cout << "Before swapping" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    // call function to swap numbers
    swap(a, b);

    cout << "\nAfter swapping" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

ERROR!
/tmp/RXT9OkJpWq.cpp: In function 'void swap(const int&, const int&)':
/tmp/RXT9OkJpWq.cpp:9:8: error: assignment of read-only reference 'n1'
    9 |     n1 = n2;
      |     ~~~^~~~
/tmp/RXT9OkJpWq.cpp:10:8: error: assignment of read-only reference 'n2'
   10 |     n2 = temp;
      |     ~~~^~~~~~

Here, we got an error because we tried to change the values of variables passed using `const` references.

**Note**: By using `const` references, we get more control over our code as we can explicitly determine which functions can and cannot change the values of variables. This enhances code safety and makes it easier to debug.

---

## Pass by Pointers (Discouraged)

The above task can be done using the pointers. To learn about pointers, visit [C++ Pointers](https://www.programiz.com/cpp-programming/pointers).

Let's look at an example.

```
#include <iostream>
using namespace std;

// function prototype with pointers as parameters
void swap(int*, int*);

int main() {

    // initialize variables
    int a = 1, b = 2;

    cout << "Before swapping" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    // call function by passing variable addresses
    swap(&a, &b);

    cout << "\nAfter swapping" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;
    return 0;
}

// function definition to swap numbers
void swap(int* n1, int* n2) {
    int temp;
    temp = *n1;
    *n1 = *n2;
    *n2 = temp;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Before swapping
a = 1
b = 2

After swapping
a = 2
b = 1

Here, we can see the output is the same as in the previous example. Notice the line,

```
// &a is address of a
// &b is address of b
swap(&a, &b);
```

Here, the address of the variable is passed during the function call rather than the variable.

Since the address is passed instead of the value, a dereference operator `*` must be used to access the value stored in that address.

```
temp = *n1;
*n1 = *n2;
*n2 = temp;
```

`*n1` and `*n2` gives the value stored at address n1 and n2 respectively.

Since n1 and n2 contain the addresses of a and b, anything is done to `*n1` and *n2 will change the actual values of a and b.

Hence, when we print the values of a and b in the `main()` function, the values are changed.

**Warning**: Using references instead of pointers is generally easier and less error-prone as it doesn't involve direct pointer operations.

Pointers should only be used to pass arguments in contexts where pointers are specifically needed or when interacting with C libraries.