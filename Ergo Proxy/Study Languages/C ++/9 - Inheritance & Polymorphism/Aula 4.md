# C++ Shadowing Base Class Member Function

As we know, [inheritance](https://www.programiz.com/cpp-programming/inheritance) is a feature of [OOP](https://www.programiz.com/cpp-programming/oop) that allows us to create derived classes from a base [class](https://www.programiz.com/cpp-programming/object-class). The derived classes inherit features of the base class.

Suppose we define the same [function](https://www.programiz.com/cpp-programming/function) in both the base class and the derived class. Now, when we call this function using the object of the derived class, the function of the derived class executes.

Here, the member function in the derived class shadows the member function in the base class. This is called shadowing the base class member function

---

## Example 1: C++ Shadowing Base Class Member Function

```
// C++ program to demonstrate shadowing base class member function

#include <iostream>
using namespace std;

class Base {
   public:
    void print() {
        cout << "Base Function" << endl;
    }
};

class Derived : public Base {
   public:
    void print() {
        cout << "Derived Function" << endl;
    }
};

int main() {
    Derived derived1;
    derived1.print();
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Derived Function

Here, the same function `print()` is defined in both `Base` and `Derived` classes.

So, when we call `print()` from the `Derived` object derived1, the `print()` from `Derived` is executed by shadowing the function in `Base`.

![Working of C++ Function Shadowing](https://www.programiz.com/sites/tutorial2program/files/cpp-function-overriding.png "Working of C++ Function Shadowing")

Working of function Shadowing in C++

As we can see, the function was shadowed because we called the function from an object of the `Derived` class.

Had we called the `print()` function from an object of the `Base` class, the function would not have been shadowed.

```
// Call function of Base class
Base base1;
base1.print(); // Output: Base Function
```

---

## Access Shadowed Function in C++

To access the shadowed function of the base class, we use the scope resolution operator `::`.

We can also access the shadowed function by using a [pointer](https://www.programiz.com/cpp-programming/pointers) of the base class to point to an object of the derived class and then calling the function from that pointer.

---

### Example 2: C++ Access Shadowed Function From the Base Class

```
// C++ program to access shadowed function
// in main() using the scope resolution operator ::

#include <iostream>
using namespace std;

class Base {
   public:
    void print() {
        cout << "Base Function" << endl;
    }
};

class Derived : public Base {
   public:
    void print() {
        cout << "Derived Function" << endl;
    }
};

int main() {
    Derived derived1, derived2;
    derived1.print();

    // access print() function of the Base class
    derived2.Base::print();

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Derived Function
Base Function

Here, the statement

```
derived2.Base::print();
```

accesses the `print()` function of the Base class.

![C++ Access Shadowed Function Using Derived Object](https://www.programiz.com/sites/tutorial2program/files/cpp-access-overridden-function-using-object.png "C++ Access Shadowed Function Using Derived Object")

Access Shadowed function using object of derived class in C++

---

### Example 3: C++ Call Shadowed Function From Derived Class

```
// C++ program to call the shadowed function
// from a member function of the derived class

#include <iostream>
using namespace std;

class Base {
   public:
    void print() {
        cout << "Base Function" << endl;
    }
};

class Derived : public Base {
   public:
    void print() {
        cout << "Derived Function" << endl;

        // call overridden function
        Base::print();
    }
};

int main() {
    Derived derived1;
    derived1.print();
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Derived Function
Base Function

In this program, we have called the base class member function inside the `Derived` class itself.

```
class Derived : public Base {
   public:
    void print() {
        cout << "Derived Function" << endl;
        Base::print();
    }
};
```

Notice the code `Base::print();`, which calls the member function `print()` from the `Base` class inside the `Derived` class.

![C++ Access Shadowed Function Inside Derived Class](https://www.programiz.com/sites/tutorial2program/files/cpp-access-overridden-function-inside-derived-class.png "C++ Access Shadowed Function Inside Derived Class")

Access overridden function inside derived class in C++

---

### Example 4: C++ Call Shadowed Function Using Pointer

```
// C++ program to access shadowed function using pointer
// of Base type that points to an object of Derived class

#include <iostream>
using namespace std;

class Base {
   public:
    void print() {
        cout << "Base Function" << endl;
    }
};

class Derived : public Base {
   public:
    void print() {
        cout << "Derived Function" << endl;
    }
};

int main() {
    Derived derived1;

    // pointer of Base type that points to derived1
    Base* ptr = &derived1;

    // call function of Base class using ptr
    ptr->print();

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Base Function

In this program, we have created a pointer of `Base` type named ptr. This pointer points to the `Derived` object derived1.

```
// pointer of Base type that points to derived1
Base* ptr = &derived1;
```

When we call the `print()` function using ptr, it calls the member function from `Base`.

```
// call function of Base class using ptr
ptr->print();
```

This is because even though ptr points to a `Derived` object, it is actually of `Base` type. So, it calls the member function of `Base`.

In order to override the `Base` function instead of accessing it, we need to use [virtual functions](https://www.programiz.com/cpp-programming/virtual-functions) in the `Base` class.

- [](https://www.programiz.com/cpp-programming/function-overriding#introduction)
- [](https://www.programiz.com/cpp-programming/function-overriding#example1)
- [](https://www.programiz.com/cpp-programming/function-overriding#shadowed-access)
- [](https://www.programiz.com/cpp-programming/function-overriding#shadowed-access-example)
- [](https://www.programiz.com/cpp-programming/function-overriding#example3)
- [](https://www.programiz.com/cpp-programming/function-overriding#example4)

[

  


](https://www.programiz.com/cpp-programming/multilevel-multiple-inheritance "C++ Multiple, Multilevel and Hierarchical Inheritance")