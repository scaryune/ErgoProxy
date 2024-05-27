# C# this Keyword

In C#, `this` keyword refers to the current instance of a class. For example,

```
using System;
 
namespace ThisKeyword {
  class Test {

    int num;
    Test(int num) {
      // this.num refers to the instance field
      this.num = num;
      Console.WriteLine("object of this: " + this);
    }

    static void Main(string[] args) {

      Test t1 = new Test(4);
      Console.WriteLine("object of t1: " + t1);
      Console.ReadLine();
    }
  }
}
```

**Output**

object of this: ThisKeyword.Test
object of t1: ThisKeyword.Test

In the above example, we have created an object named t1 of the class Test. We have printed the name of the object t1 and `this` keyword of the class.

Here, we can see the name of both t1 and `this` is the same. This is because `this` keyword refers to the current instance of the class which is t1.

---

Here are some of the major uses of `this` keyword in C#.

## C# this with Same Name Variables

We cannot declare two or more variables with the same name inside a scope (class or method). However, instance variables and parameters may have the same name. For example,

```
using System;
 
namespace ThisKeyword {
  class Test {

    int num;
    Test(int num) {

      num = num;
    }

    static void Main(string[] args) {

      Test t1 = new Test(4);
      Console.WriteLine("value of num: " + t1.num);
      Console.ReadLine();
    }
  }
}
```

**Output**

0

In the above program, the instance variable and the parameter have the same name: num. We have passed 4 as a value to the constructor.

However, we are getting **0** as an output. This is because the C# gets confused because the names of the instance variable and the parameter are the same.

We can solve this issue by using `this`.

### Example: this with Same Name Variables

```
using System;
 
namespace ThisKeyword {
  class Test {

    int num;
    Test(int num) {
      
      // this.num refers to the instance field
      this.num = num;
    }

    static void Main(string[] args) {

      Test t1 = new Test(4);
      Console.WriteLine("value of num: " +t1.num);
      Console.ReadLine();
    }
  }
}
```

**Output**

value of num: 4

Now, we are getting the expected output that is **4**. It is because `this.num` refers to the instance variable of the class.

So, there is no confusion between the names of the instance variable and the parameter.

---

## Invoke Constructor of the Same Class Using this

While working with constructor overloading, we might have to invoke one constructor from another constructor. In this case, we can use `this` keyword. For example,

```
using System;
 
namespace ThisKeyword {
  class Test {
    
    Test(int num1, int num2) {

      Console.WriteLine("Constructor with two parameter");
    }
    
    // invokes the constructor with 2 parameters
    Test(int num) : this(33, 22) {

      Console.WriteLine("Constructor with one parameter");
    }

    public static void Main(String[] args) {

      Test t1 = new Test(11); 
      Console.ReadLine();   
    }
  }
}
```

**Output**

Constructor with two parameter
Constructor with one parameter

In the above example, we have used `:` followed by `this` keyword to call constructor `Test(int num1, num2)` from the constructor `Test(int num)`.

When we call the `Test(int num)` constructor the `Test(int num1, int num2)` constructor executes first.

**Note**: Calling one constructor from another constructor is known as constructor chaining.

---

## C# this as an object argument

We can use `this` keyword to pass the current object as an argument to a method. For example,

```
using System;
 
namespace ThisKeyword {
  class Test {
    int num1;
    int num2;
      
    Test() {
      num1 = 22;
      num2 = 33;
    }

    // method that accepts this as argument   
    void passParameter(Test t1) {
      Console.WriteLine("num1: " + num1);
      Console.WriteLine("num2: " + num2);
    }

    void display() {
      // passing this as a parameter
      passParameter(this);
    }
  
    public static void Main(String[] args) {
      Test t1 = new Test();
      t1.display();
      Console.ReadLine();
    }
  }
}
```

**Output**

num1: 22
num2: 33

In the above program, we have a method passParameter(). It accepts the object of the class as an argument.

```
passParameter(this);
```

Here, we have passed `this` to the passParameter() method. As `this` refers to the instance of the class, we are able to access the value of num1 and num2.

---

## this to declare a C# indexer

Indexers allow objects of a class to be indexed just like arrays. We use this keyword to declare an indexer in C#. For example,

```
using System;
namespace ThisKeyword {
      
  class Student {
      
    private string[] name = new string[3];
  
    // declaring an indexer
    public string this[int index] {

      // returns value of array element
      get {
        return name[index];
      }
      
      // sets value of array element
      set { 
        name[index] = value;
      }
    }
  }
  
  class Program {
  
    public static void Main() {
      Student s1 = new Student();
      s1[0] = "Ram";
      s1[1] = "Shyam";
      s1[2] = "Gopal";

      for (int i = 0; i < 3; i++) {

        Console.WriteLine(s1[i] + " ");
      }
    }
  }
}
```

**Output**

Ram
Shyam
Gopal

In the above program, we have created an indexer using `this` keyword.

The array name[] is private. So, we cannot access it from the Program class.

Now, to access and set the value of the array, we use an indexer.

```
Student s1 = new Student();
s1[0] = "Ram";
s1[1] = "Shyam";
s1[2] = "Gopal";
```

As we have used `this` to create an indexer, we must use the object of the Student class to access the indexer. _To know more about the indexer, visit C# indexer._