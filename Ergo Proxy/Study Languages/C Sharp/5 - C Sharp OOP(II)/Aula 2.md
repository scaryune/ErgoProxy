# C# abstract class and method

## Abstract Class

In C#, we cannot create objects of an abstract class. We use the `abstract` keyword to create an abstract class. For example,

```
// create an abstract class
abstract class Language {
  // fields and methods
}
...

// try to create an object Language
// throws an error
Language obj = new Language();
```

An abstract class can have both abstract methods (method without body) and [non-abstract methods](https://www.programiz.com/csharp-programming/methods) (method with the body). For example,

```
abstract class Language {

  // abstract method
  public abstract void display1();

  // non-abstract method
  public void display2() {
    Console.WriteLine("Non abstract method");
  }
}
```

Before moving forward, make sure to know about [C# inheritance](https://www.programiz.com/csharp-programming/inheritance).

---

## Inheriting Abstract Class

As we cannot create objects of an abstract class, we must create a derived class from it. So that we can access members of the abstract class using the object of the derived class. For example,

```
using System;
namespace AbstractClass {

  abstract class Language {

    // non-abstract method
    public void display() {
      Console.WriteLine("Non abstract method");
    }
  }

  // inheriting from abstract class
  class Program : Language {

    static void Main (string [] args) {
      
      // object of Program class
      Program obj = new Program();

      // access method of an abstract class
      obj.display();

      Console.ReadLine();
    }
  }
}
```

**Output**

Non abstract method

In the above example, we have created an abstract class named Language. The class contains a non-abstract method display().

We have created the Program class that inherits the abstract class. Notice the statement,

```
obj.display();
```

Here, obj is the object of the derived class Program. We are calling the method of the abstract class using the object obj.

**Note**: We can use abstract class only as a base class. This is why abstract classes cannot be sealed. To know more, visit [C# sealed class and method.](https://www.programiz.com/csharp-programming/sealed-class)

---

## C# Abstract Method

A method that does not have a body is known as an abstract method. We use the `abstract` keyword to create abstract methods. For example,

```
public abstract void display();
```

Here, display() is an abstract method. An abstract method can only be present inside an abstract class.

When a non-abstract class inherits an abstract class, it should provide an implementation of the abstract methods.

### Example: Implementation of the abstract method

```
using System;
namespace AbstractClass {

  abstract class Animal {

    // abstract method
    public abstract void makeSound();
  }

  // inheriting from abstract class
  class Dog : Animal {

    // provide implementation of abstract method
    public override void makeSound() {

      Console.WriteLine("Bark Bark");

    }
  }
  class Program  {
    static void Main (string [] args) {
      // create an object of Dog class
      Dog obj = new Dog();
      obj.makeSound();    

      Console.ReadLine(); 
    }
  }
}
```

**Output**

Bark Bark 

In the above example, we have created an abstract class named Animal. We have an abstract method makeSound() inside the class.

We have a Dog class that inherits from the Animal class. Dog class provides the implementation of the abstract method makeSound().

```
// provide implementation of abstract method
public override void makeSound() {

  Console.WriteLine("Bark Bark");

}
```

Notice, we have used `override` with the makeSound() method. This indicates the method is overriding the method from the base class.

We then used the object of the Dog class to access makeSound().

If the Dog class had not provided the implementation of the abstract method makeSound(), Dog class should have been marked abstract as well.

**Note**: Unlike the C# inheritance, we cannot use `virtual` with the abstract methods of the base class. This is because an abstract class is implicitly virtual.

---

## Abstract class with get and set accessors

We can mark get and set accessors as abstract. For example,

```
using System;
namespace AbstractClass {
  abstract class Animal {
    
    protected string name;
    // abstract method
    public abstract string Name {
      get;
      set;
    }
  }

  // inheriting from abstract class
  class Dog : Animal {

    // provide implementation of abstract method
    public override string Name {
      get {
        return name;
      }
      set {
        name = value; 
      }
    }
   
  }
  class Program  {
    static void Main (string [] args) {
      // create an object of Dog class
      Dog obj = new Dog();  
      obj.Name = "Tom";
      Console.WriteLine("Name: " + obj.Name); 

      Console.ReadLine();
    }
  }
}
```

**Output**

Name: Tom

In the above example, we have marked the get and set accessor as abstract.

```
obj.Name = "Tom";
Console.WriteLine("Name: " + obj.Name);
```

We are setting and getting the value of the name field of the abstract class Animal using the object of the derived class Dog.

---

## Access Constructor of Abstract Classes

An abstract class can have constructors as well. For example,

```
using System;
namespace AbstractClass {
  abstract class Animal {
    
    public Animal() {
      Console.WriteLine("Animal Constructor");
    }
  }

  class Dog : Animal {
    public Dog() {
      Console.WriteLine("Dog Constructor");
    }   
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

**Output**

Animal Constructor
Dog Constructor

In the above example, we have created a constructor inside the abstract class Animal.

```
Dog d1 = new Dog();
```

Here, when we create an object of the derived class Dog the constructor of the abstract class Animal gets called as well.

**Note**: We can also use destructors inside the abstract class.

---

## C# Abstraction

The abstract classes are used to achieve abstraction in C#.

Abstraction is one of the important concepts of object-oriented programming. It allows us to hide unnecessary details and only show the needed information.

This helps us to manage complexity by hiding details with a simpler, higher-level idea.

A practical example of abstraction can be motorbike brakes. We know what a brake does. When we apply the brake, the motorbike will stop. However, the working of the brake is kept hidden from us.

The major advantage of hiding the working of the brake is that now the manufacturer can implement brakes differently for different motorbikes. However, what brake does will be the same.

### Example: C# Abstraction

```
using System;
namespace AbstractClass {
  abstract class MotorBike {
    
    public abstract void brake();
  }

  class SportsBike : MotorBike {

    // provide implementation of abstract method
    public override void brake() {
      Console.WriteLine("Sports Bike Brake");
    }
   
  }

  class MountainBike : MotorBike {

    // provide implementation of abstract method
    public override void brake() {      
      Console.WriteLine("Mountain Bike Brake");
    }
   
  }
  class Program  {
    static void Main (string [] args) {
      // create an object of SportsBike class
      SportsBike s1 = new SportsBike();  
      s1.brake();

      // create an object of MountainBike class
      MountainBike m1 = new MountainBike();
      m1.brake();

      Console.ReadLine();
    }
  }
}
```

**Output**

Sports Bike Brake
Mountain Bike Brake

In the above example, we have created an abstract class MotorBike. It has an abstract method brake().

As brake() is an abstract method the implementation of brake() in MotorBike is kept hidden.

Every motorbike has a different implementation of the brake. This is why SportsBike makes its own implementation of brake() and MountainBike makes its own implementation of brake().

**Note**: We use interfaces to achieve complete abstraction in C#. To learn more, visit [C# Interface](https://www.programiz.com/csharp-programming/interface).