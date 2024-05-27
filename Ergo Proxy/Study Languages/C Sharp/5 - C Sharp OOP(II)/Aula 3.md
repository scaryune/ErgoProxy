# C# Nested Class

In C#, we can define a class within another class. It is known as a nested class. For example,

```
class OuterClass {
  ...
  class InnerClass {
    ...
  }
}
```

Here, we have created the class `InnerClass` inside the class `OuterClass`. The `InnerClass` is called the nested class.

---

## Access Members

To access members of the nested classes we first need to create their objects.

**1.Create object of Outer class**

```
OuterClass obj1 = new OuterClass();
```

Here, we have created the obj1 object of the class `OuterClass`.

**2. Create object of Inner Class**

```
OuterClass.InnerClass obj2 = new OuterClass.InnerClass();
```

You can see that we have used `OuterClass.InnerClass` to create the obj2 object of the inner class. This is because `InnerClass` is the nested class of `OuterClass`.

Once we have created the object of individual classes, we can use the object name and dot operator to access members of each class.

### Example: C# Nested Class

```
using System;
namespace CsharpNestedClass {
 
  // outer class
  public class Car {

    public void displayCar() {
      Console.WriteLine("Car: Bugatti");
    }
 
    // inner class
    public class Engine {
      public void displayEngine() {
        Console.WriteLine("Engine: Petrol Engine");
      }
    }
  }
  class Program {
    static void Main(string[] args) {

      // create object of outer class
      Car sportsCar = new Car();

      // access method of outer class
      sportsCar.displayCar();
 
      // create object of inner class
      Car.Engine petrolEngine = new Car.Engine();
      
      // access member of inner class
      petrolEngine.displayEngine();
 
      Console.ReadLine();
 
    }
  }
}
```

**Output**

Car: Bugatti
Engine: Petrol Engine

In the above program, we have nested the `Engine` class inside the `Car` class.

Inside the `Program` class, we have created objects of both the outer class and the inner class.

```
// object of outer class
Car sportsCar = new Car();

// object of nested class
Car.Engine petrolEngine = new Car.Engine();
```

We then used these objects to access methods of each class.

- `sportsCar.displayCar()` - access outer class method using the object of `Car`
- `petrolEngine.displayEngine()` - access inner class method using the object of `Engine`

**Note**: We cannot access the members of the inner class using the object of the outer class. For example,

```
// error code
sportsCar.displayEngine();
```

Here, we cannot access the `displayEngine()` method of the inner class `Engine` using the sportsCar object of the outer class.

---

## Access Outer Class Members Inside Inner Class

We can access members of the outer class inside the inner class. For this we use an object of the outer class. For example,

```
using System;
namespace CsharpNestedClass {

  // outer class
  public class Car {
 
    public string brand = "Bugatti";

    // nested  class
    public class Engine {
      public void displayCar() {

        // object of outer class
        Car sportsCar = new Car();
        Console.WriteLine("Brand: " + sportsCar.brand);
      }
    }
  }

  class Program {
    static void Main(string[] args) {

       // object of inner class
       Car.Engine engineObj = new Car.Engine();
       engineObj.displayCar();

      Console.ReadLine();
    }
  }
}
```

**Output**

Brand: Bugatti

In the above example, we have nested the `Engine` class inside the `Car` class. Notice the line,

```
// inside Engine class
Car sportsCar = new Car();
Console.WriteLine("Brand: " + sportsCar.brand);
```

Here, we have used the object of the class `Car` to access field brand.

---

## Access static Members of Outer Class Inside Inner Class

If we need to access static members of the outer class, we don't need to create its object. Instead, we can directly use the name of the outer class. For example,

```
using System;
namespace CsharpNestedClass {

  // outer class
  public class Car {
    //static member of outer class
    public static string brand = "Bugatti";

    // nested class
    public class Engine {
      public void display() {
        
        // access static member of outer class
        Console.WriteLine("Brand: " + Car.brand);
      }
    }
  }
  class Program {
    static void Main(string[] args) {

      // object of inner class
       Car.Engine obj = new Car.Engine();
       obj.display();

      Console.ReadLine();
    }
  }
}
```

**Output**

Brand: Bugatti

In the above example, we have nested the `Engine` class inside the `Car` class. `Car` has a static field brand.

Here, we have accessed the static field brand inside the inner class (`Engine`) using the name of the outer class (`Car`).

```
Console.WriteLine("Brand: " + Car.brand);
```

---

## Inheriting Outer Class

Like a regular class, we can also inherit the outer class. For example,

```
using System;
namespace CsharpNestedClass {
 
  // outer class
  class Computer {

    public void display() {
      Console.WriteLine("Method of Computer class");
    }
 
    // nested class
    public class CPU {
 
    }
   }

    class Laptop : Computer {
 
    }

  class Program  {
    static void Main(string[] args) {
 
      // object of derived class
      Laptop obj = new Laptop();
      obj.display();     
 
      Console.ReadLine();
    }
  }
}
```

**Output**

Method of Computer class

In the above example, we have derived the class `Laptop` from the outer class `Computer`.

Because of this we are able to access the `display()` method of class `Computer` using the object of the class `Laptop`.

---

## Inheriting inner class

In C#, we can inherit the inner class as well. For example,

```
using System;
namespace CsharpNestedClass {

  // outer class
  class Computer {

    // nested  class
    public class CPU {
      public void display() {
        Console.WriteLine("Method of CPU class");
      }

    }
  }
    
  // inheriting inner class
  class Laptop : Computer.CPU {

  }

  class Program  {
    static void Main(string[] args) {

      // object of derived class
      Laptop obj = new Laptop();
      obj.display();     

      Console.ReadLine();
    }
  }
}
```

**Output**

Method of CPU class

In the above example, we have derived the `Laptop` class from the inner class `CPU`.

Notice that we have used the name of the outer class along with the nested class to inherit the inner class.

```
class Laptop : Computer.CPU {}
```