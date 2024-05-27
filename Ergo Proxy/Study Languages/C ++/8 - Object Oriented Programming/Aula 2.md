# C++ Constructors

A constructor is a special member [function](https://www.programiz.com/cpp-programming/function) that is called automatically when an [object](https://www.programiz.com/cpp-programming/object-class#object) is created.

In C++, a constructor has the same name as that of the [class](https://www.programiz.com/cpp-programming/object-class#class), and it does not have a return type. For example,

```
class  Wall {
  public:
    // create a constructor
    Wall() {
      // code
    }
};
```

Here, the function `Wall()` is a constructor of the class `Wall`. Notice that the constructor

- has the same name as the class,
- does not have a return type, and
- is `public`

---

## C++ Default Constructor

A constructor with no parameters is known as a **default constructor**. For example,

```
// C++ program to demonstrate the use of default constructor

#include <iostream>
using namespace std;

// declare a class
class  Wall {
  private:
    double length;

  public:
    // default constructor to initialize variable
    Wall()
      : length{5.5} {
      cout << "Creating a wall." << endl;
      cout << "Length = " << length << endl;
    }
};

int main() {
  Wall wall1;
  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Creating a Wall
Length = 5.5

Here, when the wall1 object is created, the `Wall()` constructor is called. `length{5.5}` is invoked when the constructor is called, and sets the length [variable](https://www.programiz.com/cpp-programming/variables-literals#variables) of the object to `5.5`.

**Note:** If we have not defined any constructor, copy constructor, or move constructor in our class, then the C++ compiler will automatically create a default constructor with no parameters and empty body.

---

## Defaulted Constructor

When we have to rely on default constructor to initialize the member variables of a class, we should explicitly mark the constructor as default in the following way:

```
Wall() = default;
```

If we want to set a default value, then we should use value initialization. That is, we include the default value inside braces in the declaration of member variables in the follwing way.

```
double length {5.5};
```

Let's see an example:

```
// C++ program to demonstrate the use of defaulted constructor

#include <iostream>
using namespace std;

// declare a class
class  Wall {
  private:
    double length {5.5};

  public:
    // defaulted constructor to initialize variable
    Wall() = default;
    
    void print_length() {
    	cout << "length = " << length << endl;
    }
};

int main() {
  Wall wall1;
  wall1.print_length();
  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output:**

length = 5.5

---

## C++ Parameterized Constructor

In C++, a constructor with parameters is known as a parameterized constructor. This is the preferred method to initialize member data. For example,

```
// C++ program to calculate the area of a wall

#include <iostream>
using namespace std;

// declare a class
class Wall {
  private:
    double length;
    double height;

  public:
    // parameterized constructor to initialize variables
    Wall(double len, double hgt)
      : length{len}
      , height{hgt} {
    }

    double calculateArea() {
      return length * height;
    }
};

int main() {
  // create object and initialize data members
  Wall wall1(10.5, 8.6);
  Wall wall2(8.5, 6.3);

  cout << "Area of Wall 1: " << wall1.calculateArea() << endl;
  cout << "Area of Wall 2: " << wall2.calculateArea();

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Area of Wall 1: 90.3
Area of Wall 2: 53.55

Here, we have defined a parameterized constructor `Wall()` that has two parameters: `double len` and `double hgt`. The values contained in these parameters are used to initialize the member variables length and height.

`: length{len}, height{hgt}` is the member initializer list.

- `length{len}` initializes the member variable length with the value of the parameter len
- `height{hgt}` initializes the member variable height with the value of the parameter hgt.

When we create an object of the `Wall` class, we pass the values for the member variables as arguments. The code for this is:

```
Wall wall1(10.5, 8.6);
Wall wall2(8.5, 6.3);
```

With the member variables thus initialized, we can now calculate the area of the wall with the `calculateArea()` method.

**Note**: A constructor is primarily used to initialize objects. They are also used to run a default code when an object is created.

---

## C++ Member Initializer List

Consider the constructor:

```
Wall(double len, double hgt)
  : length{len}
  , height{hgt} {
}
```

Here,

```
: length{len} 
,  height{hgt}
```

is member initializer list.

The member initializer list is used to initialize the member variables of a class.

The order or initialization of the member variables is according to the order of their declaration in the class rather than their declaration in the member initializer list.

Since the member variables are declared in the class in the following order:

```
double length;
double height;
```

The length variable will be initialized first even if we define our constructor as following:

```
Wall(double hgt, double len)
  : height{hgt}
  , length{len} {
}
```

---

## C++ Copy Constructor

The copy constructor in C++ is used to copy data from one object to another. For example,

```
#include <iostream>
using namespace std;

// declare a class
class Wall {
  private:
    double length;
    double height;

  public:

    // initialize variables with parameterized constructor
    Wall(double len, double hgt)
      : length{len}
      , height{hgt} {
    }

    // copy constructor with a Wall object as parameter
    // copies data of the obj parameter
    Wall(const Wall& obj)
      : length{obj.length}
      , height{obj.height} {
    }

    double calculateArea() {
      return length * height;
    }
};

int main() {
  // create an object of Wall class
  Wall wall1(10.5, 8.6);

  // copy contents of wall1 to wall2
  Wall wall2 = wall1;

  // print areas of wall1 and wall2
  cout << "Area of Wall 1: " << wall1.calculateArea() << endl;
  cout << "Area of Wall 2: " << wall2.calculateArea();

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Area of Wall 1: 90.3
Area of Wall 2: 90.3

In this program, we have used a copy constructor to copy the contents of one object of the `Wall` class to another. The code of the copy constructor is:

```
Wall(const Wall& obj)
    : length{obj.length}
    , height{obj.height} {
}
```

Notice that the parameter of this constructor has the address of an object of the `Wall` class.

We then assign the values of the variables of the obj object to the corresponding variables of the object, calling the copy constructor. This is how the contents of the object are copied.

In `main()`, we then create two objects wall1 and wall2 and then copy the contents of wall1 to wall2:

```
// copy contents of wall1 to wall2
Wall wall2 = wall1;
```

Here, the wall2 object calls its copy constructor by passing the reference of the wall1 object as its argument.

---

## C++ Default Copy Constructor

If we don't define any copy constructor, move constructor, or move assignment in our class, then the C++ compiler will automatically create a default copy constructor that does memberwise copy assignment. It suffices in most cases. For example,

```
#include <iostream>
using namespace std;

// declare a class
class Wall {
  private:
    double length;
    double height;

  public:

    // initialize variables with parameterized constructor
    Wall(double len, double hgt)
      : length{len}
      , height{hgt} {
    }

    double calculateArea() {
      return length * height;
    }
};

int main() {
  // create an object of Wall class
  Wall wall1(10.5, 8.6);

  // copy contents of wall1 to wall2 by default copy constructor
  Wall wall2 = wall1;

  // print areas of wall1 and wall2
  cout << "Area of Wall 1: " << wall1.calculateArea() << endl;
  cout << "Area of Wall 2: " << wall2.calculateArea();

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Area of Wall 1: 90.3
Area of Wall 2: 90.3

In this program, we have not defined a copy constructor. The compiler used the default copy constructor to copy the contents of one object of the `Wall` class to another.

---

**Also Read**

- [C++ Destructors](https://www.programiz.com/cpp-programming/destructors)
- [C++ Constructor Overloading](https://www.programiz.com/cpp-programming/constructor-overloading)
- [C++ Friend Function and Classes](https://www.programiz.com/cpp-programming/friend-function-class)

- [](https://www.programiz.com/cpp-programming/constructors#introduction)
- [](https://www.programiz.com/cpp-programming/constructors#default-constructor)
- [](https://www.programiz.com/cpp-programming/constructors#parameterized-constructor)
- [](https://www.programiz.com/cpp-programming/constructors#initializer-list)
- [](https://www.programiz.com/cpp-programming/constructors#copy-constructor)
- [](https://www.programiz.com/cpp-programming/constructors#default-copy-constructor)