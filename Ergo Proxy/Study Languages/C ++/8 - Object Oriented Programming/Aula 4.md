# C++ Destructors

A destructor is a special member [function](https://www.programiz.com/cpp-programming/function) that is called automatically when an [object](https://www.programiz.com/cpp-programming/object-class#object) goes out of scope or when we delete the object with the delete expression.

In C++, a destructor has the same name as that of the [class](https://www.programiz.com/cpp-programming/object-class#class), and it does not have a return type. `~` precedes the identifier to indicate destructor. For example,

```
class  Wall {
  public:
    // create a destructor
    ~Wall() {
      // code
    }
};
```

Here, `~Wall()` is a destructor of the class `Wall`.

**Note:** If we don't define any destructor, move assignment, or move constructor in our class, then the C++ compiler will automatically create a default destructor with an empty body. It suffices in most cases.

However, if our class involves resource handling like dynamic memory allocation, we have to define a destructor and deallocate the resources in the destructor body.

---

## Dynamic Memory Allocation in Class

When our class has pointer members, the default copy constructor just assigns the value of member pointers of one object to the member pointers of another object, rather than allocating different memory addresses and copying the value pointed by the member pointers.

To allocate new memory address for the variable and copy the data, we have to declare a copy constructor. Moreover, we have to deallocate the memory using destructor.

```
#include <iostream>
using namespace std;

// declare a class
class Wall {
  private:
    double* length;
    double* height;

  public:

    // initialize variables with parameterized constructor
    Wall(double len = 1.0, double hgt = 1.0)
      : length{new double{len}}
      , height{new double{hgt}} {
    }
    
    // copy constructor with a Wall object as parameter
    // copies data of the obj parameter
    Wall(const Wall& obj)
      : length{new double{*(obj.length)}}
      , height{new double{*(obj.height)}} {
    }
    
    void setLength(double len) {
        *length = len;
    }
    
    double calculateArea() {
      return *length * *height;
    }
    
    // destructor to deallocate memory
    ~Wall() {
        delete length;
        delete height;
    }
};

int main() {
  // create an object of Wall class
  Wall wall1(10.5, 8.6);

  // copy contents of wall1 to wall2 by copy constructor
  Wall wall2 = wall1;
  
  // change the length of wall2
  wall2.setLength(11.5);

  // print areas of wall1 and wall2
  cout << "Area of Wall 1: " << wall1.calculateArea() << endl;
  cout << "Area of Wall 2: " << wall2.calculateArea();

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Area of Wall 1: 90.3
Area of Wall 2: 98.9

Here,

```
Wall(const Wall& obj)
  :length{new double{*(obj.length)}}
  , height{new double{*(obj.height)}} {
}
```

is the copy constructor. It takes an object obj of `Wall` as a `const` reference.

```
: length{new double{*(obj.length)}}
, height{new double{*(obj.height)}} 
```

is the initializer list that copies the data to new memory locations and initializes the length and height pointers accordingly.

- `*(obj.length)` is the value pointed by `length` pointer member of the argument object obj
- `new double{*(obj.length)}` dynamically allocates memory for `double` datatype with the value `*(obj.length)` and returns the memory address
- `length{new double {*obj.length)}}` initializes the `length` variable of the new object with the new memory address.

Similarly,

```
height{new double{*(obj.height)}}
```

initializes the `height` pointer member of the new object.

When the objects wall1 and wall2 go out of scope, their respective destructor is invoked. The destructor deallocates the dynamic memory acquired by the objects.

---

**Also Read**

- [C++ Constructors](https://www.programiz.com/cpp-programming/constructors)
- [C++ Constructor Overloading](https://www.programiz.com/cpp-programming/constructor-overloading)
- [C++ Friend Function and Classes](https://www.programiz.com/cpp-programming/friend-function-class)