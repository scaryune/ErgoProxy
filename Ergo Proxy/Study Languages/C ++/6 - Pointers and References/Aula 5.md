# C++ Memory Management

C++ allows us to allocate the memory dynamically in run time. This is known as dynamic memory allocation.

In other programming languages such as [Java](https://www.programiz.com/java-programming) and [Python](https://www.programiz.com/python-programming), the compiler automatically manages the memories allocated to variables. But this is not the case in C++.

In C++, we need to deallocate the dynamically allocated memory manually after we have no use for the variable.

We can allocate and then deallocate memory dynamically using the `new` and `delete` operators respectively.

---

## C++ new Expression

We can use the `new` expression to allocate memory in run time. For example,

```
// declare an int pointer
int* point_var;

// dynamically allocate memory
// using the new keyword 
point_var = new int;

// assign value to allocated memory
*point_var = 45;
```

Here, we have dynamically allocated memory for an `int` variable using the `new` expression.

Notice that we have used the pointer point_var to allocate the memory dynamically. This is because the `new` expression returns the address of the memory location.

We can also allocate memory and initialize the value in the same step as:

```
// dynamically allocate memory
// and assign value
int* point_var = new int{45};
```

Using this syntax avoids uninitialized pointers. Uninitialized pointers may cause undefined behavior when dereferenced. So this is the preferred syntax.

The syntax for using the `new` expression is:

```
data_type* pointer_variable = new data_type{value};
```

---

## delete Expression

Once we no longer need to use a variable that we have declared dynamically, we can deallocate the memory occupied by the variable.

For this, we can use the `delete` expression. It returns the memory back to the operating system. This is known as **memory deallocation**.

The syntax for `delete` expression is:

```
delete pointer_variable;
```

Let's look at an example.

```
// dynamically allocate memory
// and assign int variable 
int* point_var = new int{45};

// print the value stored in memory
cout << *point_var; // Output: 45

// deallocate the memory
delete point_var;

// set pointer to nullptr
point_var = nullptr;
```

Here, we have dynamically allocated memory for an `int` variable using the pointer point_var.

After printing the contents of point_var, we deallocated the memory using `delete`.

It is a good practice to set pointer to `nullptr` after deallocating the memory to avoid undefined behavior if the pointer is dereferenced.

**Note**: Not deallocating memory properly can cause memory leaks which in turn causes the program to consume a large amount of memory. Proper use of the `delete` expression is essential to prevent memory leaks and ensure efficient memory management.

---

## Example 1: C++ Dynamic Memory Allocation

```
#include <iostream>
using namespace std;

int main() {

    // dynamically allocate memory
    int* point_int = new int{45};
    float* point_float = new float{45.45f};

    cout << *point_int << endl;
    cout << *point_float << endl;

    // deallocate the memory
    // set pointers to nullptr
    delete point_int;

    delete point_float;
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

45
45.45

In this program, we dynamically allocated memory to two variables of `int` and `float` types.

After assigning values to them and printing them, we finally deallocate the memories using the `delete` expression.

**Note**: Dynamic memory allocation can make memory management more efficient, especially for arrays, where many times we may not know the size of the array until runtime.

---

## Example 2: C++ new and delete Expression for Arrays

```
// C++ program to store GPA of n number of students and display it
// where n is the number of students entered by the user

#include <iostream>
using namespace std;

int main() {

    int num;
    cout << "Enter total number of students: ";
    cin >> num;
    float* ptr;
    
    // memory allocation of num number of floats
    ptr = new float[num];
    
    cout << "Enter GPA of students." << endl;
    for (int i = 0; i < num; ++i) {
    cout << "Student" << i + 1 << ": ";
    cin >> *(ptr + i);
    }
    
    cout << "\nDisplaying GPA of students." << endl;
    for (int i = 0; i < num; ++i) {
    cout << "Student" << i + 1 << ": " << *(ptr + i) << endl;
    }
    
    // ptr memory is released
    delete[] ptr;
    ptr = nullptr;
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Enter total number of students: 4
Enter GPA of students.
Student1: 3.6
Student2: 3.1
Student3: 3.9
Student4: 2.9

Displaying GPA of students.
Student1: 3.6
Student2: 3.1
Student3: 3.9
Student4: 2.9

In this program, we have asked the user to enter the number of students and store it in the num variable.

Then, we have allocated the memory dynamically for the `float` array using new.

We enter data into the array (and later print them) using pointer notation.

After we no longer needed the array, we deallocated the array memory using the code:

```
delete[] ptr;.
```

Notice the use of `[]` after `delete`. We use the square brackets `[]` in order to denote that the memory deallocation is that of an array.

---

## Example 3: C++ new and delete Expression for Objects

```
#include <iostream>
using namespace std;

class Student {
    private:
    int age;
    
    public:
    
    // constructor initializes age to 12
    Student() : age(12) {}
    
    void get_age() {
      cout << "Age = " << age << endl;
    }
};

int main() {

    // dynamically declare student object
    Student* ptr = new Student();
    
    // call get_age() function
    ptr->get_age();
    
    // ptr memory is released
    delete ptr;
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Age = 12

In this program, we have created a `Student` class that has a private variable age.

We have initialized age to `12` in the [default constructor](https://www.programiz.com/cpp-programming/constructors#default-constructor) `Student()` and printed its value with the function `get_age()`.

In `main()`, we have created a `Student` object using the `new` expression and use the pointer ptr to point to its address.

The moment the object is created, the `Student()` constructor initializes age to `12`.

We then call the `get_age()` function using the code:

```
ptr->get_age();
```

Notice the arrow operator `->`. This operator is used to access class members using pointers.

---

## Why Use Dynamic Memory Allocation?

Dynamic memory allocation has several advantages, such as:

- **Flexibility**: Dynamic memory allocation allows us to allocate memory as needed during runtime. This flexibility is useful when the size of data structures is not known at compile time or when the size changes during program execution.

- **Data Structures**: Data structures such as linked lists, trees, graphs, and resizable arrays (vectors in C++) often need to allocate memory dynamically to accommodate varying amounts of data.

- **Resource Management**: We can allocate memory when needed and deallocate it when it's no longer required. This leads to better resource utilization.

- **Dynamic Arrays**: In languages like C++, static arrays have fixed sizes determined at compile time. Dynamic memory allocation allows us to create arrays whose size can be determined during runtime.

---

**Read More:**

- [C++ std::vector](https://www.programiz.com/cpp-programming/vectors)

- [](https://www.programiz.com/cpp-programming/memory-management#introduction)
- [](https://www.programiz.com/cpp-programming/memory-management#new-expression)
- [](https://www.programiz.com/cpp-programming/memory-management#delete-expression)
- [](https://www.programiz.com/cpp-programming/memory-management#example1)
- [](https://www.programiz.com/cpp-programming/memory-management#example2)
- [](https://www.programiz.com/cpp-programming/memory-management#example3)
- [](https://www.programiz.com/cpp-programming/memory-management#why)

[

  


](https://www.programiz.com/cpp-programming/pointers-function "C++ Call by Reference: Using Pointers")