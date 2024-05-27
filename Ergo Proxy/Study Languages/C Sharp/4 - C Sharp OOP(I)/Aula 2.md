# C# Method

A method is a block of code that performs a specific task. Suppose you need to create a program to create a circle and color it. You can create two methods to solve this problem:

- a method to draw the circle
- a method to color the circle

Dividing a complex problem into smaller chunks makes your program easy to understand and reusable.

---

## Declaring a Method in C#

Here's the syntax to declare a method in C#.

```
returnType methodName() {
  // method body
}
```

Here,

- **returnType** - It specifies what type of value a method returns. For example, if a method has an `int` return type then it returns an `int` value.

If the method does not return a value, its return type is `void`.

- **methodName** - It is an identifier that is used to refer to the particular method in a program.

- **method body** - It includes the programming statements that are used to perform some tasks. The method body is enclosed inside the curly braces `{ }`

Let's see an example,

```
void display() {
// code
}
```

Here, the name of the method is display(). And, the return type is void.

---

## Calling a Method in C#

In the above example, we have declared a method named display(). Now, to use the method, we need to call it.

Here's how we can call the display() method.

```
// calls the method
display();
```

![Working of C# method call](https://www.programiz.com/sites/tutorial2program/files/csharp-methods.png "Working of C# method call")

Working of C# method call

---

### Example: C# Method

```
using System;

namespace Method {

  class Program {  
 
    // method declaration
    public void display() {
      Console.WriteLine("Hello World");   
    }

    static void Main(string[] args) {

      // create class object 
      Program p1 = new Program();

      //call method 
      p1.display();   
  
      Console.ReadLine();
     
    }
  }
}
```

**Output**

Hello World

In the above example, we have created a method named display(). We have created an object p1 of the Program class.

Notice the line,

```
p1.display();
```

Here, we are using the object to call the display() method.

---

## C# Method Return Type

A C# method may or may not return a value. If the method doesn't return any value, we use the `void` keyword (shown in the above example).

If the method returns any value, we use the return statement to return any value. For example,

```
int addNumbers() {
  ...
  return sum;
}
```

Here, we are returning the variable sum. One thing you should always remember is that the return type of the method and the returned value should be of the same type.

In our code, the return type is `int`. Hence, the data type of sum should be of `int` as well.

### Example: Method Return Type

```
using System;

namespace Method {

  class Program {   

    // method declaration
    static int addNumbers() {
      int sum = 5 + 14;
      return sum;
      
    }

    static void Main(string[] args) {

      // call method 
      int sum = addNumbers();

      Console.WriteLine(sum);
  
      Console.ReadLine();
     
    }
  }
}
```

**Output**

19

In the above example, we have a method named addNumbers() with the `int` return type.

```
int sum = addNumbers();
```

Here, we are storing the returned value from the addNumbers() to sum. We have used `int` data type to store the value because the method returns an `int` value.

**Note**: As the method is static we do not create a class object before calling the method. The static method belongs to the class rather than the object of a class.

---

## C# Methods Parameters

In C#, we can also create a method that accepts some value. These values are called method parameters. For example,

```
int addNumber(int a, int b) {
//code
}
```

Here, a and b are two parameters passed to the addNumber() function.

If a method is created with parameters, we need to pass the corresponding values(arguments) while calling the method. For example,

```
// call the method
addNumber(100, 100);
```

![Representation of the C# method returning a value](https://www.programiz.com/sites/tutorial2program/files/csharp-methods-parameters.png "Representation of the C# method returning a value")

Representation of the C# method returning a value

Here, We have passed 2 arguments (100, 100).

### Example 1: C# Methods with Parameters

```
using System;

namespace Method {

  class Program {   
    int addNumber (int a, int b) {
      
      int sum = a + b;

      return sum;
      
    }

    static void Main(string[] args) {

      // create class object 
      Program p1 = new Program();

      //call method 
      int sum = p1.addNumber(100,100);   

      Console.WriteLine("Sum: " + sum);
  
      Console.ReadLine();
     
    }
  }
}
```

**Output**

Sum: 200

---

### C# Methods with Single Parameter

In C#, we can also create a method with a single parameter. For example,

```
using System;

namespace Method {

  class Program {   

    string work(string work) {
     return work;
      
    }

    static void Main(string[] args) {

      // create class object 
      Program p1 = new Program();

      //call method 
      string work = p1.work("Cleaning"); ;   

      Console.WriteLine("Work: " + work);
  
      Console.ReadLine();
     
    }
  }
}
```

**Output**

Work: Cleaning

Here, the work() method has a single parameter work.

---

## Built-in methods

So far we have defined our own methods. These are called **user-defined methods**.

However, in C#, there are various methods that can be directly used in our program. They are called **built-in methods**. For example,

- `Sqrt()` - computes the square root of a number
- `ToUpper()` - converts a string to uppercase

### Example: Math.Sqrt() Method

```
using System;

namespace Method {

  class Program {   
    static void Main(string[] args) {
     
      // Built in method
      double a = Math.Sqrt(9);
      Console.WriteLine("Square root of 9: " + a);
    }
  }
}
```

**Output**

Square root of 9: 3

In the above program, we have used

```
double a = Math.Sqrt(9);
```

to compute the square root of 9. Here, the `Sqrt()` is a built-in method that is defined inside the `Math` class.

We can simply use built-in methods in our program without writing the method definition. To learn more, visit _C# built-in methods_.

---

## Method Overloading in C#

In C#, we can create two or more methods with the same name. It is known as method overloading. For example,

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

In the above example, we have overloaded the display() method. It is possible because:

- one method has one parameter
- another has two parameter

To know more visit C# [Method Overloading](https://www.programiz.com/csharp-programming/method-overloading)