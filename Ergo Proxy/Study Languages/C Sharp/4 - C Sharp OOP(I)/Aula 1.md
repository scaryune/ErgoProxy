# C# Class and Object

C# is an object-oriented program. In object-oriented programming(OOP), we solve complex problems by dividing them into objects.

To work with objects, we need to perform the following activities:

- create a class
- create objects from the class

---

## C# Class

Before we learn about objects, we need to understand the working of classes. Class is the blueprint for the object.

We can think of the class as a **sketch (prototype) of a house**. It contains all the details about the floors, doors, windows, etc. We can build a house based on these descriptions. **House** is the object.

Like many houses can be made from the sketch, we can create many objects from a class.

**Create a class in C#**

We use the class keyword to create an object. For example,

```
class ClassName {

}
```

Here, we have created a class named ClassName. A class can contain

- **fields** - variables to store data
- **methods** - functions to perform specific tasks

Let's see an example,

```
class Dog {
 
  //field
  string breed;
 
  //method
  public void bark() {

  }
 
}
```

In the above example,

- Dog - class name
- breed - field
- bark() - method

**Note**: In C#, fields and methods inside a class are called members of a class.

---

## C# Objects

An object is an instance of a class. Suppose, we have a class Dog. Bulldog, German Shepherd, Pug are objects of the class.

**Creating an Object of a class**

In C#, here's how we create an object of the class.

```
ClassName obj = new ClassName();
```

Here, we have used the `new` keyword to create an object of the class. And, obj is the name of the object. Now, let us create an object from the Dog class.

```
Dog bullDog = new Dog();
```

Now, the bullDog object can access the fields and methods of the Dog class.

---

## Access Class Members using Object

We use the name of objects along with the `.` operator to access members of a class. For example,

```
using System;

namespace ClassObject {

  class Dog {
    string breed;

    public void bark() {
      Console.WriteLine("Bark Bark !!");
      
    }

    static void Main(string[] args) {

      // create Dog object 
      Dog bullDog = new Dog();

      // access breed of the Dog 
      bullDog.breed = "Bull Dog";
      Console.WriteLine(bullDog.breed);

      // access method of the Dog
      bullDog.bark();   

      Console.ReadLine();
     
    }
  }
}
```

**Output**

Bull Dog
Bark Bark !!

In the above program, we have created an object named bullDog from the Dog class. Notice that we have used the object name and the `.` (dot operator) to access the breed field

```
// access breed of the Dog
bullDog.breed = "Bull Dog";
```

and the bark() method

```
// access method of the Dog
bullDog.bark();
```

---

## Creating Multiple Objects of a Class

We can create multiple objects from the same class. For example,

```
using System;

namespace ClassObject {

  class Employee {

    string department;

    static void Main(string[] args) {

      // create Employee object 
      Employee sheeran = new Employee();

      // set department for sheeran
      sheeran.department = "Development";
      Console.WriteLine("Sheeran: " + sheeran.department);

      // create second object of Employee
      Employee taylor = new Employee();

      // set department for taylor
      taylor.department = "Content Writing";
      Console.WriteLine("Taylor: " + taylor.department);

      Console.ReadLine();
    }
  }
}
```

**Output**

Sheeran: Development
Taylor: Content Writing

In the above example, we have created two objects: sheeran and taylor from the Employee class.

Here, you can see both the objects have their own version of the department field with different values.

---

## Creating objects in a different class

In C#, we can also create an object of a class in another class. For example,

For example,

```
using System;

namespace ClassObject {

  class Employee {
    public string name;

    public void work(string work) {
      Console.WriteLine("Work: " + work);
      
    }
  }

  class EmployeeDrive {
    static void Main(string[] args) {

      // create Employee object 
      Employee e1= new Employee();

      Console.WriteLine("Employee 1");

      // set name of the Employee 
      e1.name="Gloria";
      Console.WriteLine("Name: " + e1.name);

      //call method of the Employee
      e1.work("Coding"); 

      Console.ReadLine();
     
    }
  }
}
```

**Output**

Employee 1
Name: Gloria
Work: Coding

In the above example, we have two classes: Employee and EmployeeDrive. Here, we are creating an object e1 of the Employee class in the EmployeeDrive class.

We have used the e1 object to access the members of the Employee class from EmployeeDrive. This is possible because the members in the Employee class are `public`.

Here, `public` is an access specifier that means the class members are accessible from any other classes. To learn more, visit [C# Access Modifiers](https://www.programiz.com/csharp-programming/access-modifiers).

---

## Why Objects and Classes?

Objects and classes help us to divide a large project into smaller sub-problems.

Suppose you want to create a game that has hundreds of enemies and each of them has fields like health, ammo, and methods like shoot() and run().

With OOP we can create a single Enemy class with required fields and methods. Then, we can create multiple enemy objects from it.

Each of the enemy objects will have its own version of health and ammo fields. And, they can use the common shoot() and run() methods.

Now, instead of thinking of projects in terms of variables and methods, we can think of them in terms of objects.

This helps to manage complexity as well as make our code reusable.

- [](https://www.programiz.com/csharp-programming/class-objects#introduction)
- [](https://www.programiz.com/csharp-programming/class-objects#class)
- [](https://www.programiz.com/csharp-programming/class-objects#object)
- [](https://www.programiz.com/csharp-programming/class-objects#access-members)
- [](https://www.programiz.com/csharp-programming/class-objects#multiple-object)
- [](https://www.programiz.com/csharp-programming/class-objects#different-class)

[

  


](https://www.programiz.com/csharp-programming/foreach-loop "C# foreach loop")