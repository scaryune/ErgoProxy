# C++ Type Conversion Operators

Using named casts is considered a safer and reliable method of [type conversion](https://www.programiz.com/cpp-programming/type-conversion) in C++ compared to other methods. In C++, there are four main named type-casting expressions:

- `static_cast`
- `dynamic_cast`
- `const_cast`
- `reinterpret_cast`

---

## C++ static_cast

We use `static_cast` for standard type conversions, such as converting from `float` to `int`.

Let's look at an example.

```
#include <iostream>
using namespace std;

int main() {
    float my_float = 3.14;
    
    // convert float to int
    int my_int = static_cast<int>(my_float);
    cout << "Float: " << my_float << " -> Int: " << my_int << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Float: 3.14 -> Int: 3

The `static_cast<int>(my_float)` expression converts the float value stored in my_float to an integer and stores it in my_int.

Because floating-point values can have decimal components and integers cannot, this conversion removes the decimal part, converting **3.14** to **3**.

---

## C++ dynamic_cast

We mainly use `dynamic_cast` for [polymorphic](https://www.programiz.com/cpp-programming/polymorphism) type conversions, especially when dealing with [inheritance](https://www.programiz.com/cpp-programming/inheritance) hierarchies. It's typically used in scenarios where a base class [pointer](https://www.programiz.com/cpp-programming/pointers) needs to be converted to a derived class pointer.

Let's look at an example.

```
#include <iostream>
using namespace std;

class Base {
public:
    // base class print function
    virtual void print() {
        cout << "Base class" << endl;
    }
};

class Derived : public Base {
public:
    // derived class print function overriding the base class
    void print() override {
        cout << "Derived class" << endl;
    }
};

int main() {
    // create a Base class pointer 
    // pointing to a Derived object
    Base *base_ptr = new Derived();
    
    // use dynamic_cast to cast the 
    // Base pointer to a Derived pointer
    Derived *derived_ptr = dynamic_cast<Derived*>(base_ptr);
    
    // call the print function through the derived pointer
    if (derived_ptr) {
        derived_ptr->print();
    }

    // delete the dynamically allocated object
    delete base_ptr;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Derived class

In this example,

- We defined a base class `Base` and a derived class `Derived`, where `Derived` inherits from `Base`.
- In `main()`, we created a pointer `base_ptr` of type `Base*` pointing to a `Derived` object.
- We then used `dynamic_cast` to cast `base_ptr` to a `Derived*` pointer and assign it to `derived_ptr`.
- Finally, we called the `print()` function through `derived_ptr`, which means that we can access the `Derived` class function through the `Base` class pointer after the dynamic cast.

**Note**: If the base class pointer doesn't point to an object of the derived class, `dynamic_cast` returns `nullptr`.

---

## C++ const_cast

We use `const_cast` to cast away the [const](https://www.programiz.com/cpp-programming/variables-literals#constants) qualifier from a [variable](https://www.programiz.com/cpp-programming/variables-literals#variables).

One common scenario where we can use `const_cast` is when working with third-party libraries that have [functions](https://www.programiz.com/cpp-programming/function) which take non-const pointers as arguments, but we need to pass in `const` data.

Let's look at an example.

```
#include <iostream>
using namespace std;

// function that takes a non-const pointer
void modify_data(int* data) {
    // modify the data
    *data *= 2;
}

int main() {
    int x = 10;
    
    // a const pointer for variable x
    const int* ptr = &x;

    // use const_cast to 
    // remove const qualifier and allow modification
    int* mutable_ptr = const_cast<int*>(ptr);

    // call the function
    modify_data(mutable_ptr);

    // value is modified successfully
    cout << "Modified value: " << x << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Modified value: 20

In this example, we used the `const_cast` expression to remove the `const` qualifier from a pointer to pass it through a function that takes non-const pointer as an argument.

Here,

- `modify_data(int* data)`: is a function that takes non-const pointer as an argument
- ptr: is a const pointer that we need to pass to `modify_data`
- `const_cast<int*>(ptr)`: casts ptr as a non-const pointer and assigns it to mutable_ptr

---

## C++ reinterpret_cast

`reinterpret_cast` is used to convert one pointer type to another pointer type or one reference type to another reference type.

Unlike `static_cast`, `reinterpret_cast` doesn't actually convert the data types but reinterprets one pointer type as another at compile time.

Let's look at an example.

```
#include <iostream>
using namespace std;

int main() {
    // create an integer variable
    int x = 67;

    // pointer to an integer
    int* ptr_to_int = &x;

    // reinterpret the pointer to an integer 
    // as a pointer to char
    char* ptr_to_char = reinterpret_cast<char*>(ptr_to_int);

    // dereference the double pointer
    // originally holding an integer as if it contains a double
    cout << "Dereferencing ptr_to_char: " << *ptr_to_char << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Dereferencing ptr_to_char: C

Here, we used `reinterpret_cast` to reinterpret the pointer `ptr_to_int`, which originally pointed to an integer, as a pointer to a character.

This means that the memory location pointed by `ptr_to_int` still holds an integer value. But it will be treated as a character.

**Warning**: `reinterpret_cast` allows for almost any pointer or integer type conversion without any type safety checks. This can result in undefined behavior.

So, `reinterpret_cast` should be used with caution.

- [](https://www.programiz.com/cpp-programming/type-conversion-operators#introduction)
- [](https://www.programiz.com/cpp-programming/type-conversion-operators#static-cast)
- [](https://www.programiz.com/cpp-programming/type-conversion-operators#dynamic-cast)
- [](https://www.programiz.com/cpp-programming/type-conversion-operators#const_cast)
- [](https://www.programiz.com/cpp-programming/type-conversion-operators#reinterpret_cast)

[

  


](https://www.programiz.com/cpp-programming/type-conversion "C++ Type Conversion")