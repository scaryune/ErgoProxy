# C# interface

In C#, an interface is similar to abstract class. However, unlike abstract classes, all methods of an interface are fully abstract (method without body).

We use the `interface` keyword to create an interface. For example,

```
interface IPolygon {

  // method without body
  void calculateArea();
}
```

Here,

- IPolygon is the name of the interface.
- By convention, interface starts with I so that we can identify it just by seeing its name.
- We cannot use access modifiers inside an interface.
- All members of an interface are public by default.
- An interface doesn't allow fields.

---

## Implementing an Interface

We cannot create objects of an interface. To use an interface, other classes must implement it. Same as in [C# Inheritance](https://www.programiz.com/csharp-programming/inheritance), we use `:` symbol to implement an interface. For example,

```
using System;
namespace CsharpInterface {

  interface IPolygon {
    // method without body
    void calculateArea(int l, int b);

  }

  class Rectangle : IPolygon {

    // implementation of methods inside interface
    public void calculateArea(int l, int b) {

      int area = l * b;
      Console.WriteLine("Area of Rectangle: " + area);
    }
  }

  class Program {
    static void Main (string [] args) {

      Rectangle r1 = new Rectangle();
    
      r1.calculateArea(100, 200);

    }
  }
}
```

**Output**

Area of Rectangle: 20000

In the above example, we have created an interface named IPolygon. The interface contains a method `calculateArea(int a, int b)` without implementation.

Here, the Rectangle class implements IPolygon. And, provides the implementation of the `calculateArea(int a, int b)` method.

**Note**: We must provide the implementation of all the methods of interface inside the class that implements it.

---

## Implementing Multiple Interfaces

Unlike inheritance, a class can implement multiple interfaces. For example,

```
using System;
namespace CsharpInterface {

  interface IPolygon {
    // method without body
    void calculateArea(int a, int b);

  }

  interface IColor {

    void getColor();
  }
   
  // implements two interface
  class Rectangle : IPolygon, IColor {

    // implementation of IPolygon interface
    public void calculateArea(int a, int b) {

      int area = a * b;
      Console.WriteLine("Area of Rectangle: " + area);
    }

    // implementation of IColor interface
    public void getColor() {

      Console.WriteLine("Red Rectangle");
            
    }
  }

  class Program {
    static void Main (string [] args) {

      Rectangle r1 = new Rectangle();
    
      r1.calculateArea(100, 200);
      r1.getColor();
    }
  }
}
```

**Output**

Area of Rectangle: 20000
Red Rectangle

In the above example, we have two interfaces, IPolygon and IColor.

```
class Rectangle : IPolygon, IColor {
  …
}
```

We have implemented both interfaces in the Rectangle class separated by `,`.

Now, `Rectangle` has to implement the method of both interfaces.

---

## Using reference variable of an interface

We can use the reference variable of an interface. For example,

```
using System;
namespace CsharpInterface {

  interface IPolygon {
    // method without body
    void calculateArea(int l, int b);

  }

  class Rectangle : IPolygon {

    // implementation of methods inside interface
    public void calculateArea(int l, int b) {

      int area = l * b;
      Console.WriteLine("Area of Rectangle: " + area);
    }
  }

  class Program {
    static void Main (string [] args) {
       
      // using reference variable of interface
      IPolygon r1 = new Rectangle();
    
      r1.calculateArea(100, 200);
    }
  }
}
```

**Output**

Area of Rectangle: 20000

In the above example, we have created an interface named IPolygon. The interface contains a method `calculateArea(int l, int b)` without implementation.

```
IPolygon r1 = new Rectangle();
```

Notice, we have used the reference variable of interface IPolygon. It points to the class Rectangle that implements it.

Though we cannot create objects of an interface, we can still use the reference variable of the interface that points to its implemented class.

---

## Practical Example of Interface

Let's see a more practical example of C# Interface.

```
using System;
namespace CsharpInterface {

  interface IPolygon {
    // method without body
    void calculateArea();

  }   
  // implements interface
  class Rectangle : IPolygon {

    // implementation of IPolygon interface
    public void calculateArea() {
      
      int l = 30;
      int b = 90;
      int area = l * b;
      Console.WriteLine("Area of Rectangle: " + area);
    }
  }

  class Square : IPolygon {

    // implementation of IPolygon interface
    public void calculateArea() {
      
      int l = 30;
      int area = l * l;
      Console.WriteLine("Area of Square: " + area);
    }
  }

  class Program {
    static void Main (string [] args) {

      Rectangle r1 = new Rectangle();  
      r1.calculateArea();

      Square s1 = new Square();  
      s1.calculateArea();
    }
  }
}
```

**Output**

Area of Rectangle: 2700
Area of Square: 900

In the above program, we have created an interface named IPolygon. It has an abstract method `calculateArea()`.

We have two classes Square and Rectangle that implement the IPolygon interface.

The rule for calculating the area is different for each polygon. Hence, `calculateArea()` is included without implementation.

Any class that implements IPolygon must provide an implementation of `calculateArea()`. Hence, implementation of the method in class Rectangle is independent of the method in class Square.

---

## Advantages of C# interface

Now that we know what interfaces are, let's learn about why interfaces are used in C#.

- Similar to abstract classes, interfaces help us to achieve **abstraction in C#**.  
      
    Here, the method `calculateArea()` inside the interface, does not have a body. Thus, it hides the implementation details of the method.

- Interfaces provide **specifications** that a class (which implements it) must follow.  
      
    In our previous example, we have used `calculateArea()` as a specification inside the interface IPolygon. This is like setting a rule that we should calculate the area of every polygon.  
      
    Now any class that implements the IPolygon interface must provide an implementation for the calculateArea() method.

- Interfaces are used to achieve multiple inheritance in C#.

- Interfaces provide **loose coupling**(having no or least effect on other parts of code when we change one part of a code).  
      
    In our previous example, if we change the implementation of `calculateArea()` in the Square class it does not affect the Rectangle class.