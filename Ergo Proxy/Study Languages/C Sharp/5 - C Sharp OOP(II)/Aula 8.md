# C# Method Overloading

In C#, there might be two or more methods in a class with the same name but different numbers, types, and order of parameters, it is called method overloading. For example:

```
void display() { ... }
void display(int a) { ... }
float display(double a) { ... }
float display(int a, float b) { ... }
```

Here, the display() method is overloaded. These methods have the same name but accept different arguments.

**Note**: The return types of the above methods are not the same. It is because method overloading is not associated with return types. Overloaded methods may have the same or different return types, but they must have different parameters.

---

We can perform method overloading in the following ways:

## 1. By changing the Number of Parameters

We can overload the method if the number of parameters in the methods is different.

```
void display(int a) {
  ...
} 
...
void display(int a, int b) {
  ...
} 
```

Here, we have two methods in a class with the same name - display(). It is possible to have more than one method with the same name because the number of parameters in methods is different. For example,

```
using System;

namespace MethodOverload {

  class Program {  

    // method with one parameter
    void display(int a) {
      Console.WriteLine("Arguments: " + a);
    }
 
    // method with two parameters
    void display(int a, int b) {
      Console.WriteLine("Arguments: " + a + " and " + b);
    } 
    static void Main(string[] args) {

      Program p1 = new Program();
      p1.display(100);
      p1.display(100, 200);
      Console.ReadLine();
    }
  }
}
```

**Output**

Arguments: 100
Arguments: 100 and 200

In the above example, we have overloaded the display() method:

- one method has one parameter
- another has two parameter

Based on the number of the argument passed during the method call, the corresponding method is called.

- `p1.display(100)` - calls the method with single parameter
- `p1.display(100, 200)` - calls the method with two parameters

---

## 2. By changing the Data types of the parameters

```
void display(int a) {
  ...
} 
...
void display(string b) {
  ...
} 
```

Here, we have two methods - display() with the same number of parameters. It is possible to have more than one display() method with the same number of parameters because the data type of parameters in methods is different. For example,

```
using System;

namespace MethodOverload {

  class Program {  

    // method with int parameter
    void display(int a) {
      Console.WriteLine("int type: " + a);
    } 

    // method with string parameter
    void display(string b) {
      Console.WriteLine("string type: " + b);
    } 
    static void Main(string[] args) {

      Program p1 = new Program();
      p1.display(100);
      p1.display("Programiz");
      Console.ReadLine();
    }
  }
}
```

**Output**

int type: 100
string type: Programiz

In the above program, we have overloaded the display() method with different types of parameters.

Based on the type of arguments passed during the method call, the corresponding method is called.

- `p1.display(100)` - calls method with `int` type parameter
- `p1.display("Programiz")` - calls method with `string` type parameter

---

## 3. By changing the Order of the parameters

```
void display(int a, string b) {
  ...
} 
...
void display(string b, int a) {
  ...
}
```

Here, we have two methods - display(). It is possible to have more than one display() method with the same number and type of parameter because the order of data type of parameters in methods is different. For example,

```
using System;

namespace MethodOverload {

  class Program {  

    // method with int and string parameters 
    void display(int a, string b) {
      Console.WriteLine("int: " + a);
      Console.WriteLine("string: " + b);
    } 

    // method with string andint parameter
    void display(string b, int a) {
      Console.WriteLine("string: " + b);
      Console.WriteLine("int: " + a);
    } 
    static void Main(string[] args) {

      Program p1 = new Program();
      p1.display(100, "Programming");
      p1.display("Programiz", 400);
      Console.ReadLine();
    }
  }
}
```

**Output**

int: 100
string: Programming
string: Programiz
int: 400

In the above program, we have overloaded the display() method with different orders of parameters.

Based on the order of arguments passed during the method call, the corresponding method is called.

- `p1.display(100, "Programming")` - calls method with `int` and `string` parameter respectively
- `p1.display("Programiz", 400)` - calls method with `string` and `int` parameter respectively

- [](https://www.programiz.com/csharp-programming/method-overloading#introduction)
- [](https://www.programiz.com/csharp-programming/method-overloading#number)
- [](https://www.programiz.com/csharp-programming/method-overloading#datatype)
- [](https://www.programiz.com/csharp-programming/method-overloading#order)

[

  


](https://www.programiz.com/csharp-programming/polymorphism "C# Polymorphism")