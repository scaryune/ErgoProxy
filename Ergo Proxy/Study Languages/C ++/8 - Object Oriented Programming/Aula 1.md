# C++ Classes and Objects

Objects and classes are used to wrap related [functions](https://www.programiz.com/cpp-programming/function) and data in one place in C++.

Suppose we need to store the length, breadth, and height of a rectangular room and calculate its area and volume.

To handle this task, we can create three [variables](https://www.programiz.com/cpp-programming/variables-literals#variables), say, length, breadth, and height, along with the functions `calculate_area()` and `calculate_volume()`.

However, in C++, rather than creating separate variables and functions, we can also wrap the related data and functions in a single place (by creating **objects**).

This programming paradigm is known as [object-oriented programming](https://www.programiz.com/cpp-programming/oop).

But before we can create **objects** and use them in C++, we first need to learn about **classes**.

---

## C++ Class

A class is a blueprint for the object.

We can think of a class as a sketch (prototype) of a house.

It contains all the details about the floors, doors, windows, etc - we build the house based on these descriptions.

The house is the object.

---

### Create a Class

A class is defined in C++ using the [keyword](https://www.programiz.com/cpp-programming/keywords-identifiers#keywords) `class` followed by the name of the class.

The body of the class is defined inside curly brackets and terminated by a semicolon at the end.

```
class ClassName {
   // some data
   // some functions
};
```

For example,

```
class Room {
    public:
        double length;
        double breadth;
        double height;   

        double calculate_area(){   
            return length * breadth;
        }

        double calculate_volume(){   
            return length * breadth * height;
        }

};
```

Here, we defined a class named `Room`.

The variables length, breadth, and height declared inside the class are known as **data members**.

And the functions `calculate_area()` and `calculate_volume ()` are known as **member functions** of a class.

---

## C++ Objects

When a class is defined, only the specification for the object is defined; no memory or storage is allocated.

To use the data and access functions defined in the class, we need to create objects.

---

### Syntax to Define Object in C++

```
ClassName object_name;
```

We can create objects of `Room` class (defined in the above example) as follows:

```
// sample function
void sample_function() {
    // create objects
    Room room1, room2;
}

int main(){
    // create objects 
    Room room3, room4;
}
```

Here, two objects room1 and room2 of the `Room` class are created in `sample_function()`.

Similarly, the objects room3 and room4 are created in `main()`.

As we can see, we can create objects of a class in any function of the program.

We can also create objects of a class within the class itself or in other classes.

Also, we can create as many objects as we want from a single class.

---

## C++ Access Data Members and Member Functions

We can access the data members and member functions of a class by using a `.` (dot) [operator](https://www.programiz.com/cpp-programming/operators).

For example,

```
room2.calculate_area();
```

This will call the `calculate_area()` function inside the `Room` class for object room2.

Similarly, the data members can be accessed as:

```
room1.length = 5.5;
```

In this case, it initializes the length variable of room1 to `5.5`.

---

## Example: Object and Class in C++ Programming

```
// Program to illustrate the working of
// objects and class in C++ Programming

#include <iostream>
using namespace std;

// create a class
class Room {

   public:
    double length;
    double breadth;
    double height;

    double calculate_area() {
        return length * breadth;
    }

    double calculate_volume() {
        return length * breadth * height;
    }
};

int main() {

    // create object of Room class
    Room room1;

    // assign values to data members
    room1.length = 42.5;
    room1.breadth = 30.8;
    room1.height = 19.2;

    // calculate and display the area and volume of the room
    cout << "Area of Room =  " << room1.calculate_area() << endl;
    cout << "Volume of Room =  " << room1.calculate_volume() << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Area of Room =  1309
Volume of Room =  25132.8

In this program, we have used the `Room` class and its object room1 to calculate the area and volume of a room.

In `main()`, we assigned the values of length, breadth, and height with the code:

```
room1.length = 42.5;
room1.breadth = 30.8;
room1.height = 19.2;
```

We then called the functions `calculate_area()` and `calculate_volume()` to perform the necessary calculations.

Note the use of the keyword `public` in the program. This means the members are public and can be accessed anywhere from the program.

To learn more about `public` and other access specifiers, please visit our [C++ Class Access Modifiers](https://www.programiz.com/cpp-programming/access-modifiers) tutorial.

---

**Also Read**

- [C++ Constructors](https://www.programiz.com/cpp-programming/constructors)
- [How to pass and return an object from a function?](https://www.programiz.com/cpp-programming/pass-return-object-function)

- [](https://www.programiz.com/cpp-programming/object-class#introduction)
- [](https://www.programiz.com/cpp-programming/object-class#class)
- [](https://www.programiz.com/cpp-programming/object-class#class-definition)
- [](https://www.programiz.com/cpp-programming/object-class#object)
- [](https://www.programiz.com/cpp-programming/object-class#object-syntax)
- [](https://www.programiz.com/cpp-programming/object-class#access)
- [](https://www.programiz.com/cpp-programming/object-class#example1)