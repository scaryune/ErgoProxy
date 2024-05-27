# C# Polymorphism

Polymorphism is one of the features provided by Object Oriented Programming. Polymorphism simply means occurring in more than one form.

That is, the same entity (method or operator or object) can perform different operations in different scenarios.

---

## Example of Polymorphism

```
using System;
class Program
{
    // method does not take any parameter 
    public void greet()
    {
        Console.WriteLine("Hello");
    }

    // method takes one string parameter
    public void greet(string name)
    {
        Console.WriteLine("Hello " + name);
    }

    static void Main(string[] args)
    {
        Program p1 = new Program();

        // calls method without any argument
        p1.greet();

        //calls method with an argument
        p1.greet("Tim");

    }
}
```

**Output**

Hello
Hello Tim

In the above example, we have created a class `Program` inside which we have two methods of the same name `greet()`.

Here, one of the `greet()` methods takes no parameters and displays `"Hello"`. While the other `greet()` method takes a parameter and displays `"Hello Tim"`.

Hence, the `greet()` method behaves differently in different scenarios. Or, we can say `greet()` is polymorphic.

---

## Types of Polymorphism

After getting the basic idea of polymorphism, let's learn the types of polymorphism in C#.

There are two types of polymorphism:

1. Compile Time Polymorphism / Static Polymorphism
2. Run-Time Polymorphism / Dynamic Polymorphism

---

## 1. Compile Time Polymorphism

In compile time polymorphism, the compiler identifies which method is being called at the compile time.

In C#, we achieve compile time polymorphism through 2 ways:

- Method overloading
- Operator overloading

Let's discuss each of them in detail.

---

## C# Method Overloading

In a C# class, we can create methods with the same name in a class if they have:

- different numbers of parameter
- types of parameter

For example,

```
void totalSum() {...}
void totalSum(int a) {...}
void totalSum(int a, int b) {...}
void totalSum(float a, float b) {...}
```

Here we have different types and numbers of parameters in `totalSum()`. This is known as method overloading in C#. The same method will perform different operations based on the parameter.

Look at the example below,

```
using System;
class Program
{

    // method adds two integer numbers
    void totalSum(int a, int b)
    {
        Console.WriteLine("The sum of numbers is " + (a + b));
    }

    // method adds two double-type numbers
    // totalSum() method is overloaded
    void totalSum(double a, double b)
    {
        Console.WriteLine("The sum of numbers is " + (a + b));
    }
    static void Main(string[] args)
    {

        Program sum1 = new Program();
        sum1.totalSum(5, 7);
        sum1.totalSum(53.5, 8.7);
    }
}
```

**Output**

The sum of numbers is 12
The sum of numbers is 62.2

In the above example, the class `Program` contains a method named `totalSum()` that is overloaded. The `totalSum()` method prints:

- sum of integers if two integers are passed as an argument
- sum of doubles if two doubles are passed as an argument

---

## C# Operator Overloading

Some operators in C# behave differently with different operands. For example,

- `+` operator is overloaded to perform numeric addition as well as string concatenation and

Now let's see how we can achieve polymorphism using operator overloading.

The `+` operator is used to add two entities. However, in C#, the `+` operator performs two operations:

1. Adding two numbers,

```
int x = 7;
int y = 5;
int sum = x + y;
Console.WriteLine(sum);
// Output: 12
```

2. Concatenating two strings,

```
string firstString = "Harry";
string secondString = "Styles";

string concatenatedString = firstString + secondString;
Console.WriteLine(concatenatedString);
// Output: HarryStyles
```

Here, we can see that the `+` operator is overloaded in C# to perform two operations: addition and concatenation.

---

## 2. Runtime Polymorphism

In runtime polymorphism, the method that is called is determined at the runtime not at compile time.

The runtime polymorphism is achieved by:

- Method Overriding

Let's discuss method overriding in detail.

---

### Method Overriding in C#

During [inheritance in C#](https://www.programiz.com/csharp-programming/inheritance#:~:text=In%20C%23%2C%20inheritance%20allows%20us,derived%20class%20(child%20or%20subclass)), if the same method is present in both the superclass and the subclass. Then, the method in the subclass overrides the same method in the superclass. This is called method overriding.

In this case, the same method will perform one operation in the superclass and another operation in the subclass.

We can use `virtual` and `override` keywords to achieve method overriding.

Let's see the example below,

```
using System;
class Polygon
{
    // method to render a shape
    public virtual void render()
    {
        Console.WriteLine("Rendering Polygon...");
    }
}

class Square : Polygon
{
    // overriding render() method 
    public override void render()
    {
        Console.WriteLine("Rendering Square...");
    }
}
class myProgram
{
    public static void Main()
    {
        // obj1 is the object of Polygon class
        Polygon obj1 = new Polygon();

        // calls render() method of Polygon Superclass 
        obj1.render();

        // here, obj1 is the object of derived class Square 
        obj1 = new Square();

        // calls render() method of derived class Square
        obj1.render();
    }
}
```

**Output**

Rendering Polygon...
Rendering Square…

In the above example, we have created a superclass: `Polygon` and a subclass: `Square`.

Notice, we have used `virtual` and `override` with methods of the base class and derived class respectively. Here,

- `virtual` - allows the method to be overridden by the derived class
- `override` - indicates the method is overriding the method from the base class

In this way, we achieve method overriding in C#.

**Note:** A method in derived class overrides the method in base class if the method in derived class has the **same name**, **same return type** and **same parameters** as that of the base class.

---

## Why Polymorphism?

Polymorphism allows us to create consistent code. In the previous example, we can also create a different method: `renderSquare()` to render Square.

This will work perfectly. However, for every shape, we need to create different methods. It will make our code inconsistent.

To solve this, polymorphism in C# allows us to create a single method `render()` that will behave differently for different shapes.