# C# using

In C#, we use the using keyword to import external resources (namespaces, classes, etc) inside a program. For example,

```
// using System namespace
using System;

namespace Program {

  class Program1 {
    static void Main(string[] args) {
      Console.WriteLine("Hello World!");   
    }
  }
}
```

**Output**

Hello World!

In the above example, notice the line

```
using System;
```

Here, we are importing the `System` namespace inside our program. This helps us to directly use the classes present in the `System` namespace.

Also, because of this, we don't have to write the fully qualified name of the print statement.

```
// full print statement
System.Console.WriteLine("Hello World!");

// print statement with using System;
Console.WriteLine("Hello World!");
```

To learn more about the namespace, visit [C# namespaces](https://www.programiz.com/csharp-programming/namespaces).

---

## C# using to create an alias

We can also create aliases with the help of `using` in C#. For example,

```
// creating alias for System.Console
using Programiz = System.Console;

namespace HelloWorld {

  class Program {
    static void Main(string[] args) {

      // using Programiz alias instead of System.Console
      Programiz.WriteLine("Hello World!");    
    }
  }
}
```

**Output**

Hello World!

In the above program, we have created an alias for `System.Console`.

```
using Programiz = System.Console;
```

This allows us to use the alias Programiz instead of `System.Console`.

```
Programiz.WriteLine("Hello World!");
```

Here, Programiz will work just like `System.Console`.

---

## C# using static directive

In C#, we can also import classes in our program. Once we import these classes, we can use the static members (fields, methods) of the class.

We use the `using static` directive to import classes in our program.

### Example: C# using static with System.Math

```
using System;

// using static directive
using static System.Math;

namespace Program {  

  class Program1  {  
    public static void Main(string[] args)  {  
       	 
      double n  = Sqrt(9);
      Console.WriteLine("Square root of 9 is " + n);  
      	 
    }  
  }  
}
```

**Output**

Square root of 9 is 3

In the above example, notice the line,

```
using static System.Math;
```

Here, this line helps us to directly access the methods of the `Math` class.

```
double n = Sqrt(9);
```

We have used the `Sqrt()` method directly without specifying the `Math` class.

If we don't use the `using static System.Math` in our program, we have to include the class name `Math` while using `Sqrt()`. For example,

```
using System; 
 
namespace Program {  

  class Program1 {  
    public static void Main(string[] args) {  

      // using the class name Math
      double n  = Math.Sqrt(9);
      Console.WriteLine("Square root of 9 is " + n);  
    }  
  }  
} 
```

**Output**

Square root of 9 is 3

In the above example, notice the line,

```
double n = Math.Sqrt(9);
```

Here, we are using `Math.Sqrt()` to compute the square root of **9**. This is because we haven't imported the `System.Math` in this program.

- [](https://www.programiz.com/csharp-programming/using#introduction)
- [](https://www.programiz.com/csharp-programming/using#using-alias)
- [](https://www.programiz.com/csharp-programming/using#using-static)

[

  


](https://www.programiz.com/csharp-programming/bitwise-operators "C# Bitwise and Bit Shift Operators")