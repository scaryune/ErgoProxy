# C# Variable Scope

A variable scope refers to the availability of variables in certain parts of the code.

In C#, a variable has three types of scope:

- Class Level Scope
- Method Level Scope
- Block Level Scope

---

## C# Class Level Variable Scope

In C#, when we declare a variable inside a class, the variable can be accessed within the class. This is known as **class level variable scope**.

Class level variables are known as fields and they are declared outside of methods, constructors, and blocks of the class. For example,

```
using System;
namespace VariableScope {
  class Program {

    // class level variable
    string str = "Class Level";

    public void display() {
      Console.WriteLine(str);
    }

    static void Main(string[] args) {
      Program ps = new Program();
      ps.display();

      Console.ReadLine();
    }
  }
}
```

**Output**

Class Level

In the above example, we have initialized a variable named str inside the Program class.

Since it is a class level variable, we can access it from a method present inside the class.

```
public void display() {
  Console.WriteLine(str);
}
```

This is because the class level variable is accessible throughout the class.

**Note**: We cannot access the class level variable through static methods. For example, suppose we have a static method inside the Program class.

```
static void display2() {

  // Access class level variable
  // Cause an Error
  Console.WriteLine(str);
}
```

---

## Method Level Variable Scope

When we declare a variable inside a method, the variable cannot be accessed outside of the method. This is known as **method level variable scope**. For example,

```
using System;

namespace VariableScope {
  class Program {

    public void method1() {
      // display variable inside method
      string str = "method level";
    }

    public void method2() {

      // accessing str from method2()
      Console.WriteLine(str);
    }

    static void Main(string[] args) {
      Program ps = new Program();
      ps.method2();

      Console.ReadLine();
    }
  }
}
```

In the above example, we have created a variable named str inside `method1()`.

```
// Inside method1()
string str = "method level";
```

Here, str is a method level variable. So, it cannot be accessed outside `method1()`.

However, when we try to access the `str` variable from the `method2()`

```
// Inside method2
Console.WriteLine(str);  // Error code
```

we get an error.

```
Error   CS0103     The name 'str' does not exist in the current context  
```

This is because method level variables have scope inside the method where they are created. For example,

```
using System;
namespace VariableScope {
  class Program {

    public void display() {
     string str = "inside method";

      // accessing method level variable
      Console.WriteLine(str);
    }

    static void Main(string[] args) {
    Program ps = new Program();
    ps.display();

    Console.ReadLine();
    }
  }
}
```

**Output**

inside method

Here, we have created the str variable and accessed it within the same method `display()`. Hence, the code runs without any error.

---

## Block Level Variable Scope in C#

When we declare a variable inside a block ([for loop](https://www.programiz.com/csharp-programming/for-loop), [while loop](https://www.programiz.com/csharp-programming/do-while-loop), [if..else](https://www.programiz.com/csharp-programming/if-else-statement)), the variable can only be accessed within the block. This is known as **block level variable scope**. For example,

```
using System;

namespace VariableScope {
  class Program {
    public void display() {

      for(int i=0;i<=3;i++) {
        	 
      }
    Console.WriteLine(i);
    }

    static void Main(string[] args) {
      Program ps = new Program();
      ps.display();

      Console.ReadLine();
    }
  }
}
```

In the above program, we have initialized a block level variable `i` inside the `for` loop.

```
for(int i=0;i<=3;i++) {
       	 
}
```

Since i is a block level variable, when we try to access the variable outside the for loop,

```
// Outside for loop
Console.WriteLine(i);
```

we get an error.

```
Error	 CS0103  The name 'i' does not exist in the current context
```

- [](https://www.programiz.com/csharp-programming/variable-scope#introduction)
- [](https://www.programiz.com/csharp-programming/variable-scope#class-level)
- [](https://www.programiz.com/csharp-programming/variable-scope#method-level)
- [](https://www.programiz.com/csharp-programming/variable-scope#block-level)

[

  


](https://www.programiz.com/csharp-programming/access-modifiers "C# Access Modifiers")