# C# Access Modifiers

In C#, access modifiers specify the accessibility of types (classes, interfaces, etc) and type members (fields, methods, etc). For example,

```
class Student {

  public string name;
    
  private int num;

  }
```

Here,

- name - public field that can be accessed from anywhere
- num - private field can only be accessed within the Student class

**Types of Access Modifiers**

In C#, there are 4 basic types of access modifiers.

- public
- private
- protected
- internal

---

## 1. public access modifier

When we declare a type or type member `public`, it can be accessed from anywhere. For example,

```
using System;

namespace MyApplication {

  class Student {
    public string name = "Sheeran";
      
    public void print() {
      Console.WriteLine("Hello from Student class");
     }
  }

  class Program {
    static void Main(string[] args) {
    
      // creating object of Student class
      Student student1 = new Student();
      
      // accessing name field and printing it
      Console.WriteLine("Name: " + student1.name);

      // accessing print method from Student
      student1.print();
      Console.ReadLine();
    }
  }
}
```

**Output**

Name: Sheeran
Hello from Student class

In the above example, we have created a class named Student with a field name and a method print().

```
// accessing name field and printing it
Console.WriteLine("Name: " + student1.name);

// accessing print method from Student
student1.print();
```

Since the field and method are public, we are able to access them from the Program class.

**Note**: We have used the object student1 of the Student class to access its members. To learn more, visit the _C# class and objects_.

---

## 2. private access modifier

When we declare a type member with the `private` access modifier, it can only be accessed within the same `class` or `struct`. For example,

```
using System;

namespace MyApplication {

  class Student {
    private string name = "Sheeran";
      
    private void print() {
      Console.WriteLine("Hello from Student class");
     }
  }

  class Program {
    static void Main(string[] args) {
    
      // creating object of Student class
      Student student1 = new Student();
      
      // accessing name field and printing it
      Console.WriteLine("Name: " + student1.name);

      // accessing print method from Student
      student1.print();

      Console.ReadLine();
    }
  }
}
```

In the above example, we have created a class named Student with a field name and a method print().

```
// accessing name field and printing it
Console.WriteLine("Name: " + student1.name);

// accessing print method from Student
student1.print();
```

Since the field and method are private, we are not able to access them from the Program class. Here, the code will generate the following error.

```
Error    CS0122    'Student.name' is inaccessible due to its protection level    
Error    CS0122    'Student.print()' is inaccessible due to its protection level    
```

---

## 3. protected access modifier

When we declare a type member as `protected`, it can only be accessed from the same class and its derived classes. For example,

```
using System;

namespace MyApplication {

  class Student {
    protected string name = "Sheeran";
  }

  class Program {
    static void Main(string[] args) {
    
      // creating object of student class
      Student student1 = new Student();
      
      // accessing name field and printing it
      Console.WriteLine("Name: " + student1.name);
      Console.ReadLine();
    }
  }
}
```

In the above example, we have created a class named Student with a field name. Since the field is protected, we are not able to access it from the Program class.

Here, the code will generate the following error.

```
Error    CS0122    'Student.name' is inaccessible due to its protection level    
```

Now, let's try to access the `protected` member from a derived class.

```
using System;

namespace MyApplication {

  class Student {
    protected string name = "Sheeran";
  }
  
  // derived class
  class Program : Student {
    static void Main(string[] args) {

      // creating object of derived class
      Program program = new Program();
      
      // accessing name field and printing it
      Console.WriteLine("Name: " + program.name);
      Console.ReadLine();
    }
  }
}
```

**Output**

Name: Sheeran

In the above example, we have created a class Student with a protected field name. Notice that we have inherited the Program class from the Student class.

```
// accessing name field and printing it
Console.WriteLine("Name: " + program.name);
```

Since the `protected` member can be accessed from derived classes, we are able to access name from the Program class.

---

## 4. internal access modifier

When we declare a type or type member as `internal`, it can be accessed only within the same assembly.

An assembly is a collection of types (classes, interfaces, etc) and resources (data). They are built to work together and form a logical unit of functionality.

That's why when we run an assembly all classes and interfaces inside the assembly run together. To learn more, visit the [C# Assembly](https://docs.microsoft.com/en-us/dotnet/standard/assembly/).

---

### Example: internal within the same Assembly

```
using System;

namespace Assembly {

  class Student {
   internal string name = "Sheeran";
  }

  class Program {
    static void Main(string[] args) {
    
      // creating object of Student class
      Student theStudent = new Student();
      
      // accessing name field and printing it
      Console.WriteLine("Name: " + theStudent.name);
      Console.ReadLine();
    }
  }
}
```

**Output**

Name: Sheeran

In the above example, we have created a class named Student with a field name. Since the field is `internal`, we are able to access it from the Program class as they are in the same assembly.

If we use `internal` within a single assembly, it works just like the `public` access modifier.

---

### Example: internal in different Assembly

Let's create one assembly first.

```
// Code on Assembly1
using System;

namespace Assembly1 {

  public class StudentName {
    internal string name = "Sheeran";
  }

  class Program {
    static void Main(string[] args) {
    }
  }
}
```

Here, this code is in **Assembly1**. We have created an internal field name inside the class StudentName. Now, this field can only be accessed from the same assembly **Assembly1**.

Now, let's create another assembly.

```
// Code on Assembly2
using System;

// access Assembly1
using Assembly1;

namespace Assembly2 {
  class Program {
    static void Main(string[] args) {
      StudentName student = new StudentName();

      // accessing name field from Assembly1
      Console.Write(student.name);
      Console.ReadLine();
     }
  }
}
```

Here, this code is in **Assembly2**. We are trying to access the name field of the StudentName class(**Assembly1**).

To access fields from **Assembly1**, we first need to set the reference of **Assembly1** in **Assembly2**. Now the code

```
using Assembly1;
```

allows us to use the code from **Assembly1** to **Assembly2**.

Here, when we try to access the name field from **Assembly2**, we get an error.

```
Error    CS0122    'StudentName.name' is inaccessible due to its protection level
```

This is because name is an internal field present in **Assembly1**.

---

## 5. protected internal access modifier

The `protected internal` is a combination of `protected` and `internal` access modifiers.

When we declare a member `protected internal`, it can be accessed from the same assembly and the derived class of the containing class from any other assembly.

```
// Code on Assembly1
using System;

namespace Assembly1 {
  public class Greet {
    protected internal string msg="Hello";
  }

  class Program {
    static void Main(string[] args) {
      Greet greet = new Greet();
      Console.WriteLine(greet.msg);
      Console.ReadLine();
     }
  }
}
```

**Output**

Hello

The above code is in **Assembly1**.

In the above example, we have created a class named Greet with a field msg. Since the field is protected internal, we are able to access it from the Program class as they are in the same assembly.

Let's derive a class from Greet in another assembly and try to access the protected internal field msg from it.

```
// Code on Assembly2
using System;

// access Assembly1
using Assembly1;

namespace Assembly2 {

  // derived class of Greet
  class Program: Greet {
    static void Main(string[] args) {
      Program greet = new Program();

      // accessing name field from Assembly1
      Console.Write(greet.msg);
      Console.ReadLine();
    }
  }
}
```

**Output**

Hello

The above code is in **Assembly2**.

In the above example, we have inherited the Program class from the Greet class(from **Assembly1**).

```
// accessing name field from Assembly1
Console.Write(greet.msg);
```

We are able to access the msg from the Greet class of **Assembly1** from **Assembly2**.

This is because the msg is a protected internal field and we are trying to access it from the child class of Greet.

---

## 6. private protected access modifier

The `private protected` access modifier is a combination of `private` and `protected`. It is available from the C# version 7.2 and later.

When we declare a member `private protected`, it can only be accessed within the same class, and its derived class within the same assembly. For example,

```
// Code in Assembly1
using System;

namespace Assembly1 {
  public class StudentName {
    private protected string name = "Sheeran";
  }

  //derived class of StudentName class
  class Program1 : StudentName {

    static void Main(string[] args) {

      Program1 student = new Program1();

      //  accessing name field from base class
      Console.Write(student.name);
      Console.ReadLine();
    }
  }
}
```

**Output**

Sheeran

The above code is in **Assembly1**

In the above example, we have created a class StudentName with a `private protected` field name.

Notice that we have inherited the Program1 class from the StudentName class.

Since the `private protected` member can be accessed from derived classes within the same assembly, we are able to access name from the Program1 class.

Let's derive a class from StudentName in another assembly and try to access the private protected field name from it. For example,

```
// Code in Assembly2
using System;
//access Assembly1
using Assembly1;

namespace Assembly2 {

  //derived class of StudentName
  class Program : StudentName {
    static void Main(string[] args) {
      Program student = new Program();
    
      // accessing name field from Assembly1
      Console.Write(student.name);
      Console.ReadLine();
     }
  }
}
```

The above code is in **Assembly2**

In the above example, when we try to access the name field from the derived class of StudentName, we get an error.

```
Error    CS0122    'StudentName.name' is inaccessible due to its protection level    
```

This is because the name field is in **Assembly1** and the derived class is in **Assembly2**.

**Note**: We can also use access modifiers with types (classes, interface, etc). However, we can only use types with public and internal access modifiers.

- [](https://www.programiz.com/csharp-programming/access-modifiers#introduction)
- [](https://www.programiz.com/csharp-programming/access-modifiers#public)
- [](https://www.programiz.com/csharp-programming/access-modifiers#private)
- [](https://www.programiz.com/csharp-programming/access-modifiers#protected)
- [](https://www.programiz.com/csharp-programming/access-modifiers#internal)
- [](https://www.programiz.com/csharp-programming/access-modifiers#protected-internal)
- [](https://www.programiz.com/csharp-programming/access-modifiers#private-protected)