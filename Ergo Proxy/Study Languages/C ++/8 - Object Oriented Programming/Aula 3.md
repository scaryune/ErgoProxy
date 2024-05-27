# C++ Constructor Overloading

Constructors can be overloaded in a similar way as [function overloading](https://www.programiz.com/cpp-programming/function-overloading).

Overloaded constructors have the same name (name of the class) but the different number of arguments. Depending upon the number and type of arguments passed, the corresponding constructor is called.

---

## Example 1: Constructor overloading

```
// C++ program to demonstrate constructor overloading
#include <iostream>
using namespace std;

class Person {
   private:
    int age;

   public:
    // 1. Constructor with no arguments
    Person() {
        age = 20;
    }

    // 2. Constructor with an argument
    Person(int a) {
        age = a;
    }

    int getAge() {
        return age;
    }
};

int main() {
    Person person1, person2(45);

    cout << "Person1 Age = " << person1.getAge() << endl;
    cout << "Person2 Age = " << person2.getAge() << endl;

    return 0;
}
```

**Output**

Person1 Age = 20
Person2 Age = 45

In this program, we have created a class `Person` that has a single variable age.

We have also defined two constructors `Person()` and `Person(int a)`:

- When the object person1 is created, the first constructor is called because we have not passed any argument. This constructor initializes age to `20`.
- When person2 is created, the second constructor is called since we have passed `45` as an argument. This constructor initializes age to `45`.

The function `getAge()` returns the value of age, and we use it to print the age of person1 and person2.

---

## Example 2: Constructor overloading

```
// C++ program to demonstrate constructor overloading
#include <iostream>
using namespace std;

class Room {
   private:
    double length;
    double breadth;

   public:
    // 1. Constructor with no arguments
    Room() {
        length = 6.9;
        breadth = 4.2;
    }

    // 2. Constructor with two arguments
    Room(double l, double b) {
        length = l;
        breadth = b;
    }
    // 3. Constructor with one argument
    Room(double len) {
        length = len;
        breadth = 7.2;
    }

    double calculateArea() {
        return length * breadth;
    }
};

int main() {
    Room room1, room2(8.2, 6.6), room3(8.2);

    cout << "When no argument is passed: " << endl;
    cout << "Area of room = " << room1.calculateArea() << endl;

    cout << "\nWhen (8.2, 6.6) is passed." << endl;
    cout << "Area of room = " << room2.calculateArea() << endl;

    cout << "\nWhen breadth is fixed to 7.2 and (8.2) is passed:" << endl;
    cout << "Area of room = " << room3.calculateArea() << endl;

    return 0;
}
```

**Output**

When no argument is passed: 
Area of room = 28.98

When (8.2, 6.6) is passed.
Area of room = 54.12

When breadth is fixed to 7.2 and (8.2) is passed:
Area of room = 59.04

- When room1 is created, the first constructor is called. length is initialized to `6.9` and breadth is initialized to `4.2`.
- When room2 is created, the second constructor is called. We have passed the arguments `8.2` and `6.6`. length is initialized to the first argument `8.2` and breadth is initialized to `6.6`.
- When room3 is created, the third constructor is called. We have passed one argument `8.2`. length is initialized to the argument `8.2`. breadth is initialized to the `7.2` by default.

**Recommended Tutorial**: [C++ Function Overloading](https://www.programiz.com/cpp-programming/function-overloading).