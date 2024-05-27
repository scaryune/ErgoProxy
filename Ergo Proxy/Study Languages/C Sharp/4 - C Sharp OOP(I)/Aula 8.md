# C# static Keyword

In C#, if we use a `static` keyword with class members, then there will be a single copy of the type member.

And, all objects of the class share a single copy instead of creating individual copies.

---

## C# Static Variables

If a variable is declared `static`, we can access the variable using the class name. For example,

```
using System;

namespace StaticKeyword {

  class Student {

    // static variable
    public static string department = "Computer Science";
  }

  class Program {
    static void Main(string[] argos) {
    
      // access static variable
      Console.WriteLine("Department: " + Student.department);
     
      Console.ReadLine();
    }
  }
}
```

**Output**

Department: Computer Science

In the above example, we have created a static variable named department. Since the variable is static, we have used the class name Student to access the variable.

---

### Static Variables Vs Instance Variables

In C#, every object of a class will have its own copy of instance variables. For example,

```
class Student {

  // instance variable
  public string studentName;
 }

class Program {
  static void Main(string[] args) {

    Student s1 = new Student();
    Student s2 = new Student();
  }
}
```

Here, both the objects s1 and s2 will have separate copies of the variable studentName. And, they are different from each other.

However, if we declare a variable static, all objects of the class share the same static variable. And, we don't need to create objects of the class to access the static variables.

### Example: C# Static Variable Vs. Instance Variable

```
using System;
 
namespace StaticKeyword {
 
  class Student {
    static public string schoolName = "Programiz School";
    public string studentName;
 
  }
 
    class Program {
    static void Main(string[] args) {
       
      Student s1 = new Student();
      s1.studentName = "Ram";

      // calls instance variable
      Console.WriteLine("Name: " + s1.studentName);
      // calls static variable
      Console.WriteLine("School: " + Student.schoolName);
 
      Student s2 = new Student();
      s2.studentName = "Shyam";
   
       // calls instance variable
      Console.WriteLine("Name: " + s2.studentName);
      // calls static variable
      Console.WriteLine("School: " + Student.schoolName);
      
      Console.ReadLine();
    }
  }
}
```

**Output**

Name: Ram
School: Programiz School
Name: Shyam
School: Programiz School

In the above program, the Student class has a non-static variable named studentName and a static variable named schoolName.

Inside the Program class,

- `s1.studentName` / `s2.studentName` - calls the non-static variable using objects s1 and s2 respectively
- `Student.schoolName` - calls the static variable by using the class name

Since the schoolName is the same for all students, it is good to make the schoolName static. It saves memory and makes the program more efficient.

---

## C# Static Methods

Just like static variables, we can call the static methods using the class name.

```
class Test {

  public static void display() {....}

}

class Program {
  static void Main(string[] args) {

    Test.display();
  }
}
```

Here, we have accessed the static method directly from Program classes using the class name.

When we declare a method static, all objects of the class share the same static method.

### Example: C# Static and Non-static Methods

```
using System;
 
namespace StaticKeyword {
 
  class Test {
 
    public void display1() {
 
      Console.WriteLine("Non static method");
    }
    public static void display2() {
 
      Console.WriteLine("Static method");
    }
  }
 
  class Program {
    static void Main(string[] args) {
 
      Test t1 = new Test();
      t1.display1();
      Test.display2();    
      Console.ReadLine();
    }
  }
}
```

**Output**

Non static method
Static method

In the above program, we have declared a non-static method named display1() and a static method named display2() inside the class Test.

Inside the Program class,

- `t1.display1()` - access the non-static method using s1 object
- `Test.display2()` - access the static method using the class name Test

**Note**: In C#, the Main method is static. So, we can call it without creating the object.

---

## C# Static Class

In C#, when we declare a class as static, we cannot create objects of the class. For example,

```
using System;

namespace StaticKeyword {

  static class Test {
    static int a = 5;
    static void display() {

      Console.WriteLine("Static method");
    }
  
    static void Main(string[] args) {

      // creating object of Test
      Test t1 = new Test();
      Console.WriteLine(a);
      display();
    }
  }
}
```

In the above example, we have a static class Test. We have created an object t1 of the class Test.

Since we cannot make an object of the static class, we get the following error:

```
error CS0723: Cannot declare a variable of static type 'Test' 
error CS0712: Cannot create an instance of the static class
```

Notice the field and method of the static class are also static because we can only have static members inside the static class.

**Note**: We cannot inherit a static class in C#. For example,

```
static class A {
  ...
}

// Error Code
class B : A {
  ...
}
```

---

## Access static Members within the Class

If we are accessing the static variables and methods inside the same class, we can directly access them without using the class name. For example,

```
using System;
 
namespace StaticKeyword {
 
  class Test {
 
    static int age = 25;
    public static void display() {
 
      Console.WriteLine("Static method");
    }
   
    static void Main(string[] args) {
 
      Console.WriteLine(age);
      display();
      Console.ReadLine();
    }
  }
}
```

**Output**

25
Static method

Here, we are accessing the static field age and static method `display()` without using the class name.