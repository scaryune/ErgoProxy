# C# Destructor

In C#, destructor (finalizer) is used to destroy objects of class when the scope of an object ends. It has the same name as the class and starts with a tilde `~`. For example,

```
class Test {
  ...
  //destructor
  ~Test() {
    ...
  }
}
```

Here, `~Test()` is the destructor.

---

### Example 1: Working of C# Destructor

```
using System;  
namespace CsharpDestructor {
  
  class Person {

    public Person() {
      Console.WriteLine("Constructor called.");
    }
    
    // destructor
    ~Person() {
      Console.WriteLine("Destructor called.");
    }

    public static void Main(string [] args) {

      //creates object of Person
      Person p1 = new Person();
    }
  } 
}
```

**Output**

Constructor called.
Destructor called.

In the above example, we have created a destructor `~Person` inside the `Person` class.

When we create an object of the `Person` class, the constructor is called. After the scope of the object ends, object p1 is no longer needed. So, the destructor is called implicitly which destroys object p1.

---

### Example 2: C# Destructor

```
using System;  
namespace CsharpDestructor {
  
  class Person {

    string name;

    void getName() {
      Console.WriteLine("Name: " + name);
    }

    // destructor
    ~Person() {
      Console.WriteLine("Destructor called.");
    }

    public static void Main(string [] args) {

      // creates object of Person
      Person p1 = new Person();

      p1.name = "Ed Sheeran";
      p1.getName();
    }
  } 
}
```

**Output**

Name: Ed Sheeran
Destructor called.

---

## Features of Destructors

There are some important features of the C# destructor. They are as follows:

- We can only have one destructor in a class.
- A destructor cannot have access modifiers, parameters, or return types.
- A destructor is called implicitly by the Garbage collector of the .NET Framework.
- We cannot overload or inherit destructors.
- We cannot define destructors in structs.