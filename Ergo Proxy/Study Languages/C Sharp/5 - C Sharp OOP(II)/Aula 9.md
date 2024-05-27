# C# Constructor Overloading

In C#, similar to [method overloading](https://www.programiz.com/csharp-programming/method-overloading), we can also overload constructors. For constructor overloading, there must be two or more constructors with the same name but different

- number of parameters
- types of parameters
- order of parameters

Before you learn about constructor overloading, make sure to know about [C# constructors](https://www.programiz.com/csharp-programming/constructors).

---

We can perform constructor overloading in the following ways:

## 1. Different number of parameters

We can overload the constructor if the number of parameters in a constructor are different.

```
 class Car {   

  Car() {
    ...
  }

  Car(string brand) {
    ...
  }
    
  Car(string brand, int price) {
    ...
  }

}
```

Here, we have three constructors in class Car. It is possible to have more than one constructor because the number of parameters in constructors is different.

Notice that,

- `Car() { }` - has no parameter
- `Car(string brand) { }` - has one parameter
- `Car(string brand, int price) { }` - has two parameters

### Example: Constructor Overloading with different number of parameter

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

      // call with no parameter
      Car car = new Car();

      Console.WriteLine();

      // call with one parameter 
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

1. one constructor has one parameter
2. another has two parameter

Based on the number of the argument passed during the constructor call, the corresponding constructor is called.

Here,

- Object car - calls constructor with one parameter
- Object car2 - calls constructor with two parameter

---

## 2. Different types of parameters

```
class Car {   

  Car(string brand) {
    ...
   }

  Car(int price) {
    ...
  }
}
```

Here, we have two Car constructors with the same number of parameters. We are able to create constructors with the same parameters because the data type inside the parameters is different.

Notice that,

- `Car(string brand) { }` - has parameter of `string` type
- `Car(int price) { }` - has parameter of `int` type

### Example: Constructor overloading with different types of parameters

```
using System;

namespace ConstructorOverload {

  class Car {   
    
    // constructor with string parameter
    Car(string brand) {
      Console.WriteLine("Brand: " + brand);
    }

    // constructor  with int parameter
    Car(int price) {
      Console.WriteLine("Price: " + price);
    }

    static void Main(string[] args) {

      // call constructor  with string parameter
      Car car = new Car("Lamborghini");
      
      Console.WriteLine();

      // call constructor  with int parameter
      Car car2 =new Car(50000);
    
      Console.ReadLine();
    }
  }
}
```

**Output**

Brand: Lamborghini

Price: 50000

In the above program, we have overloaded the constructor with different types of parameters.

Here,

1. Object car - calls constructor with `string` type parameter
2. Object car2 - calls constructor with `int` type parameter

---

## 3. Different order of parameters

```
Car {

  Car(string brand, int price) {
    ...
  }

  Car(int speed, string color) {
    ... 
  }

}
```

Here, we have two constructors with the same number of parameters. This is possible because the order of data type in parameters is different.

Notice that,

- `Car(string brand, int price) { }` - `string` data type comes before `int`
- `Car(int speed, string color) { }` - `int` data type comes before `string`

### Example: Constructor overloading with different order of parameters

```
using System;

namespace ConstructorOverload {

  class Car {   
    
    // constructor with string and int parameter
    Car(string brand, int price) {

      Console.WriteLine("Brand: " + brand);
      Console.WriteLine("Price: " + price);
    }
    
    // constructor with int and string parameter
    Car(int speed, string color) {
      
      Console.WriteLine("Speed: " + speed + " km/hr");
      Console.WriteLine("Color: " + color);
    }
    static void Main(string[] args) {

      // call constructor  with string and int parameter
      Car car = new Car("Bugatti", 50000);
      
      Console.WriteLine();

      // call constructor with int and string parameter
      Car car2 =new Car(60, "Red");
    
      Console.ReadLine();
    }
  }
}
```

**Output**

Brand: Bugatti
Price: 50000

Speed: 60 km/hr
Color: Red

In the above program, we have overloaded the constructors with different orders of parameters.

Here,

1. Object car - calls constructor with `string` and `int` parameter respectively
2. Object car2 - calls constructor with `int` and `string` parameter respectively