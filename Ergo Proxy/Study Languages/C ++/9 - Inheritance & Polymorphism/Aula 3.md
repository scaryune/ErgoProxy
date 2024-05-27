# C++ Multiple, Multilevel, Hierarchical and Virtual Inheritance

[Inheritance](https://www.programiz.com/cpp-programming/inheritance) is one of the core features of an [object-oriented](https://www.programiz.com/cpp-programming/oop) programming language. It allows software developers to derive a new [class](https://www.programiz.com/cpp-programming/object-class) from the existing class. The derived class inherits the features of the base class (existing class).

There are various models of inheritance in C++ programming.

---

## C++ Multilevel Inheritance

In C++ programming, not only can you derive a class from the base class but you can also derive a class from the derived class. This form of inheritance is known as multilevel inheritance.

class A { 
... .. ... 
};
class B: public A {
... .. ...
};
class C: public B {
... ... ...
};

Here, class B is derived from the base class A and the class C is derived from the derived class B.

---

### Example 1: C++ Multilevel Inheritance

```
#include <iostream>
using namespace std;

class A {
public:
    void display() {
        cout<<"Base class content.";
    }
};

class B : public A {};

class C : public B {};

int main() {
    C obj;
    obj.display();
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Base class content.

In this program, class C is derived from class B (which is derived from base class A).

The obj object of class C is defined in the `main()` function.

When the `display()` function is called, `display()` in class A is executed. It's because there is no `display()` function in class C and class B.

The compiler first looks for the `display()` function in class C. Since the [function](https://www.programiz.com/cpp-programming/function) doesn't exist there, it looks for the function in class B (as C is derived from B).

The function also doesn't exist in class B, so the compiler looks for it in class A (as B is derived from A).

If `display()` function exists in C, the compiler overrides `display()` of class A (because of [member function overriding](https://www.programiz.com/cpp-programming/function-overriding)).

---

## C++ Multiple Inheritance

In C++ programming, a class can be derived from more than one parent. For example, A class Bat is derived from base classes Mammal and WingedAnimal. It makes sense because bat is a mammal as well as a winged animal.

![C++ Multiple Inheritance Example](https://www.programiz.com/sites/tutorial2program/files/multiple-inheritance-example.png "C++ Multiple Inheritance Example")

Multiple Inheritance

---

### Example 2: Multiple Inheritance in C++ Programming

```
#include <iostream>
using namespace std;

class Mammal {
public:
    Mammal() {
        cout << "Mammals can give direct birth." << endl;
    }
};

class WingedAnimal {
public:
    WingedAnimal() {
        cout << "Winged animal can flap." << endl;
    }
};

class Bat: public Mammal, public WingedAnimal {};

int main() {
    Bat b1;
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Mammals can give direct birth.
Winged animal can flap.

---

### Ambiguity in Multiple Inheritance

The most obvious problem with multiple inheritance occurs during function overriding.

Suppose two base classes have the same function which is not overridden in the derived class.

If you try to call the function using the object of the derived class, the compiler shows error. It's because the compiler doesn't know which function to call. For example,

```
class base1 {
  public:
      void someFunction( ) {....}  
};
class base2 {
    void someFunction( ) {....} 
};
class derived : public base1, public base2 {};

int main() {
    derived obj;
    obj.someFunction() // Error!  
}
```

This problem can be solved using the scope resolution function to specify which function to class either base1 or base2.

```
int main() {
    obj.base1::someFunction( );  // function of base1 class is called
    obj.base2::someFunction();   // function of base2 class is called.
}
```

---

## C++ Hierarchical Inheritance

If more than one class is inherited from the base class, it's known as [hierarchical inheritance](http://www.programtopia.net/cplusplus/docs/hierarchical-inheritance-c-programming?utm_source=programiz&utm_campaign=display). In hierarchical inheritance, all features that are common in child classes are included in the base class.

For example, Physics, Chemistry, Biology are derived from Science class. Similarly, Dog, Cat, Horse are derived from Animal class.

---

### Syntax of Hierarchical Inheritance

```
class base_class {
     ... .. ...
}

class first_derived_class: public base_class {
     ... .. ...
}

class second_derived_class: public base_class {
     ... .. ...
}

class third_derived_class: public base_class {
     ... .. ...
}
```

---

### Example 3: Hierarchical Inheritance in C++ Programming

```
// C++ program to demonstrate hierarchical inheritance

#include <iostream>
using namespace std;

// base class
class Animal {
public:
    void info() {
        cout << "I am an animal." << endl;
    }
};

// derived class 1
class Dog : public Animal {
public:
    void bark() {
        cout << "I am a Dog. Woof woof." << endl;
    }
};

// derived class 2
class Cat : public Animal {
public:
    void meow() {
        cout << "I am a Cat. Meow." << endl;
    }
};

int main() {
    // create object of Dog class
    Dog dog1;
    cout << "Dog Class:" << endl;
    dog1.info();  // parent Class function
    dog1.bark();

    // create object of Cat class
    Cat cat1;
    cout << "\nCat Class:" << endl;
    cat1.info();  // parent Class function
    cat1.meow();

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Dog Class:
I am an animal.
I am a Dog. Woof woof.

Cat Class:
I am an animal.
I am a Cat. Meow.

Here, both the `Dog` and `Cat` classes are derived from the `Animal` class. As such, both the derived classes can access the `info()` function belonging to the `Animal` class.

---

## C++ Virtual Inheritance

Virtual inheritance is a C++ technique that makes sure that the grandchild derived classes inherit only one copy of a base class's member variables.

Let's consider the following class hierarchy.

![Diamond Problem in Inheritance](https://www.programiz.com/sites/tutorial2program/files/diamond-problem-inheritance.png "Diamond Problem in Inheritance")

Diamond Problem in Inheritance

Here, when `Bat` inherits from multiple classes; `Mammal` and `WingedAnimal` having the same base class; `Animal`, it may inherit multiple instances of the base class. This is known as the diamond problem.

We can avoid this problem using virtual inheritance.

```
class Base {
... .. ...
};

class Derived1 : virtual public Base {
... .. ...
};

class Derived2 : virtual public Base {
... .. ...
};

class Derived3 : public Derived1, public Derived2 {
... ... ...
};
```

Here, `Derived1` and `Derived2` both inherit from `Base` virtually, ensuring that `Derived3` will have only one set of `Base` member variables, even though it inherits from both `Derived1` and `Derived2`.

---

### Example 4: Virtual Inheritance

```
#include <iostream>
using namespace std;

// base class with a speciesName member variable
class Animal {
private:
    string species_name;

public:

    // constructor that accepts 
    // a species name for initialization
    Animal(const string& name) : species_name(name) {
        cout << "Animal constructor called" << endl;
    }

    void show_species() const {
        cout << "This animal belongs to the species: " << species_name << endl;
    }
};

// WingedAnimal class with virtual inheritance from Animal
class WingedAnimal : virtual public Animal {
public:
    // constructor that initializes 
    // the Animal part of WingedAnimal
    WingedAnimal(const string& name) : Animal(name) {
        cout << "WingedAnimal constructor called" << endl;
    }
};

// Mammal class with virtual inheritance from Animal
class Mammal : virtual public Animal {
public:
    // constructor that initializes 
    // the Animal part of Mammal
    Mammal(const string& name) : Animal(name) {
        cout << "Mammals constructor called" << endl;
    }
};

// Bat class inherits from WingedAnimal and Mammal
class Bat : public WingedAnimal, public Mammal {
public:
    // Bat constructor
    // note that Animal's constructor will only be called once
    // due to virtual inheritance.
    Bat() : Animal("Bat"), WingedAnimal("Bat"), Mammal("Bat") {
    }

    void show_info() {
        cout << endl << "It's a unique animal! Here are some details:" << endl;
        
          // show the species_name
          // demonstrating the shared member variable
        show_species();
    }
};

int main() {
    Bat my_bat;
    my_bat.show_info();
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Animal constructor called
WingedAnimal constructor called
Mammals constructor called

It's a unique animal! Here are some details:
This animal belongs to the species: Bat

In this example, the `Bat` class is derived from both `WingedAnimal` and `Mammal`, which are in turn derived from `Animal` using virtual inheritance.

This ensures that only one `Animal` base class constructor is called when an instance of `Bat` is created and the `species_name` is set to `"Bat"`.

**Note**: In the above program, if the `virtual` keyword was not used, the `Bat` class would inherit multiple copies of the member variable of the `Animal` class. This would result in an error.