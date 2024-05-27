# C# sealed class and method

## Sealed Class

In C#, when we don't want a class to be inherited by another class, we can declare the class as **a sealed class**.

A sealed class cannot have a derived class. We use the `sealed` keyword to create a sealed class. For example,

```
using System;
namespace SealedClass {
  sealed class Animal {
    
  }

  // trying to inherit sealed class
  // Error Code
  class Dog : Animal {
    
  }   

  class Program  {
    static void Main (string [] args) {

      // create an object of Dog class
      Dog d1 = new Dog();  
      Console.ReadLine();
    }
  }
}
```

In the above example, we have created a sealed class Animal. Here, we are trying to derive Dog class from the Animal class.

Since a sealed class cannot be inherited, the program generates the following error:

```
error CS0509: 'Dog': cannot derive from sealed type 'Animal'
```

---

## Sealed Method

During method overriding, if we don't want an overridden method to be further overridden by another class, we can declare it as a **sealed method**.

We use a `sealed` keyword with an overridden method to create a sealed method. For example,

```
using System;
namespace SealedClass {

  class Animal {
    public virtual void makeSound() {
    Console.WriteLine("Animal Sound");
    }
  }

  class Dog : Animal {

    // sealed method
    sealed public override void makeSound() {

      Console.WriteLine("Dog Sound");
    }
  }

  class Puppy : Dog {

    // trying to override sealed method
    public override void makeSound() {
      Console.WriteLine("Puppy Sound");
    }
  }   

  class Program  {
    static void Main (string [] args) {
      
      // create an object of Puppy class
      Puppy d1 = new Puppy();  
      Console.ReadLine();
    }
  }
}
```

In the above example, we have overridden the makeSound() method inside the Dog class.

```
// Inside the Dog class
sealed public override void makeSound() {
  Console.WriteLine("Dog Sound");
}
```

Notice that we have used the `sealed` keyword with makeSound(). This means the Puppy class that inherits the Dog class is not allowed to override makeSound().

Hence, we get an error

```
error CS0239: 'Puppy.makeSound()': cannot override inherited member 'Dog.makeSound()' because it is sealed
```

when we try to further override the makeSound() method inside the Puppy class.

**Note**: Sealing an overridden method prevents method overriding in multilevel inheritance.

---

## Why Sealed Class?

1. We use sealed classes to prevent inheritance. As we cannot inherit from a sealed class, the methods in the sealed class cannot be manipulated from other classes.

It helps to prevent security issues. For example,

```
sealed class A { 
  ...
}

// error code
class B : A {
  ...
}
```

As class A cannot be inherited, class B cannot override and manipulate the methods of class A.

2. One of the best uses of sealed classes is when you have a class with static members.

The Pens class of the `System.Drawing` namespace is one of the examples of the sealed class. The Pens class has static members that represent the pens with standard colors. `Pens.Blue` represents a pen with blue color.

- [](https://www.programiz.com/csharp-programming/sealed-class#sealed-class)
- [](https://www.programiz.com/csharp-programming/sealed-class#sealed-method)
- [](https://www.programiz.com/csharp-programming/sealed-class#why-sealed-class)

[

  


](https://www.programiz.com/csharp-programming/partial-class-and-methods "C# Partial Class and Partial Method")