# C# Constructor

In C#, a constructor is similar to a method that is invoked when an object of the class is created.

However, unlike methods, a constructor:

- has the same name as that of the class
- does not have any return type

---

## Create a C# constructor

Here's how we create a constructor in C#

```
class Car {
  
  // constructor
  Car() {
    //code
  }

}
```

Here, Car() is a constructor. It has the same name as its class.

**Call a constructor**

Once we create a constructor, we can call it using the `new` keyword. For example,

```
new Car();
```

In C#, a constructor is called when we try to create an object of a class. For example,

```
Car car1 = new Car();
```

Here, we are calling the Car() constructor to create an object car1. To learn more about objects, visit [C# Class and Objects](https://www.programiz.com/csharp-programming/class-objects).

---

## Types of Constructors

There are the following types of constructors:

- Parameterless Constructor
- Parameterized Constructor
- Default Constructor

---

## 1. Parameterless Constructor

When we create a constructor without parameters, it is known as a parameterless constructor. For example,

```
using System;

namespace Constructor {

  class Car {   

    // parameterless constructor
    Car() {
      Console.WriteLine("Car Constructor");
    }
 
    static void Main(string[] args) {

      // call constructor
      new Car();
      Console.ReadLine();
     
    }
  }
}
```

**Output**

Car Constructor

In the above example, we have created a constructor named Car().

```
new Car();
```

We can call a constructor by adding a `new` keyword to the constructor name.

---

## 2. C# Parameterized Constructor

In C#, a constructor can also accept parameters. It is called a parameterized constructor. For example,

```
using System;

namespace Constructor {

  class Car {   

    string brand;
    int price;

    // parameterized constructor
    Car(string theBrand, int thePrice) {

      brand = theBrand;
      price = thePrice;
    }
  
    static void Main(string[] args) {

      // call parameterized constructor
      Car car1 = new Car("Bugatti", 50000);

      Console.WriteLine("Brand: " + car1.brand);
      Console.WriteLine("Price: " + car1.price);
      Console.ReadLine();
     
    }
  }
}
```

**Output**

Brand: Bugatti
Price: 50000

In the above example, we have created a constructor named Car(). The constructor takes two parameters: theBrand and thePrice.

Notice the statement,

```
Car car1 = new Car("Bugatti", 50000);
```

Here, we are passing the two values to the constructor.

The values passed to the constructor are called arguments. We must pass the same number and type of values as parameters.

---

## 3. Default Constructor

If we have not defined a constructor in our class, then the C# will automatically create a default constructor with an empty code and no parameters. For example,

```
using System;

namespace Constructor {

  class Program {  

    int a;

    static void Main(string[] args) {

      // call default constructor
      Program p1 = new Program();

      Console.WriteLine("Default value of a: " + p1.a);
      Console.ReadLine();
     
    }
  }
}
```

**Output**

Default value of a: 0

In the above example, we have not created any constructor in the Program class. However, while creating an object, we are calling the constructor.

`Program p1 = new Program();`

Here, C# automatically creates a default constructor. The default constructor initializes any uninitialized variable with the default value.

Hence, we get **0** as the value of the `int` variable a.

**Note**: In the default constructor, all the numeric fields are initialized to 0, whereas string and object are initialized as null.

---

## 4. Copy Constructor in C#

We use a copy constructor to create an object by copying data from another object. For example,

```
using System;

namespace Constructor {

  class Car {  
    string brand;

    // constructor
    Car (string theBrand) {
      brand = theBrand;
    }

    // copy constructor
    Car(Car c1) {
      brand = c1.brand;
    }

    static void Main(string[] args) {
      // call constructor
      Car car1 = new Car("Bugatti");

      Console.WriteLine("Brand of car1: " + car1.brand);

      // call the copy constructor
      Car car2 = new Car(car1);
      Console.WriteLine("Brand of car2: " + car2.brand);

      Console.ReadLine();
     
    }
  }
}
```

**Output**

Brand of car1: Bugatti
Brand of car2: Bugatti

In the above program, we have used a copy constructor.

```
Car(Car c1) {
  brand = c1.brand;
}
```

Here, this constructor accepts an object of Car as its parameter. So, when creating the car2 object, we have passed the car1 object as an argument to the copy constructor.

```
Car car2 = new Car(car1);
```

Inside the copy constructor, we have assigned the value of the brand for car1 object to the brand variable for car2 object. Hence, both objects have the same value of the brand.

---

## 5. Private Constructor

We can create a private constructor using the `private` [access specifier](https://www.programiz.com/csharp-programming/access-modifiers). This is known as a private constructor in C#.

Once the constructor is declared private, we cannot create objects of the class in other classes.

### Example 1: Private Constructor

```
using System;

namespace Constructor {

  class Car {  
  
   // private constructor
   private Car () {
    Console.WriteLine("Private Constructor");    
    }
  }
    
    class CarDrive {

      static void Main(string[] args) {

      // call private constructor
      Car car1 = new Car();
      Console.ReadLine();
    }
  }
}
```

In the above example, we have created a private constructor Car(). Since private members are not accessed outside of the class, when we try to create an object of Car

```
// inside CarDrive class
Car car1 = new Car();
```

we get an error

```
error CS0122: 'Car.Car()' is inaccessible due to its protection level
```

**Note**: If a constructor is private, we cannot create objects of the class. Hence, all fields and methods of the class should be declared static, so that they can be accessed using the class name.

---

## 6. C# Static Constructor

In C#, we can also make our constructor static. We use the `static` keyword to create a static constructor. For example,

```
using System;

namespace Constructor {

  class Car {  
  
   // static constructor
   static Car () {
    Console.WriteLine("Static Constructor");    
   }

    // parameterless constructor
    Car() {
     Console.WriteLine("Default Constructor");
   } 

    static void Main(string[] args) {

      // call parameterless constructor
      Car car1 = new Car();

      // call parameterless constructor again
      Car car2 = new Car();

      Console.ReadLine();
    }
  }
}
```

In the above example, we have created a static constructor.

```
static Car () {
  Console.WriteLine("Static Constructor");    
}
```

We cannot call a static constructor directly. However, when we call a regular constructor, the static constructor gets called automatically.

```
Car car1 = new Car();
```

Here, we are calling the Car() constructor. You can see that the static constructor is also called along with the regular constructor.

**Output**

Static Constructor
Default Constructor
Default Constructor

The static constructor is called only once during the execution of the program. That's why when we call the constructor again, only the regular constructor is called.

**Note**: We can have only one static constructor in a class. It cannot have any parameters or access modifiers.

---

## C# Constructor Overloading

In C#, we can create two or more constructor in a class. It is known as constructor overloading. For example,

```
using System;

namespace ConstructorOverload {

  class Car {   
    
    // constructor with no parameter
    Car() {
      Console.WriteLine("Car constructor");
    }
     
    // constructor with one parameter
    Car(string brand) {
      Console.WriteLine("Car constructor with one parameter");
      Console.WriteLine("Brand: " + brand);
    }

    static void Main(string[] args) {

      // call constructor with no parameter
      Car car = new Car();

      Console.WriteLine();

      // call constructor with parameter
      Car car2 =  new Car("Bugatti");
     
      Console.ReadLine();
    }
  }
}
```

**Output**

Car constructor

Car constructor with one parameter
Brand: Bugatti

In the above example, we have overloaded the Car constructor:

- one constructor has one parameter
- another has two parameter

Based on the number of the argument passed during the constructor call, the corresponding constructor is called.

Here,

- Object car - calls constructor with one parameter
- Object car2 - calls constructor with two parameter

To learn more visit C# [Constructor Overloading](https://www.programiz.com/csharp-programming/constructor-overloading).