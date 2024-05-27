# C# Stack<T>

A `Stack<T>` is a generic class that arranges the elements of a specified data type using **Last In First Out(LIFO)** principles. For example,

```
using System;
using System.Collections.Generic;

class Program
{
    public static void Main()
    {
        // create a stack 
        Stack<string> country = new Stack<string>();

        // push "USA" and "India" to the country stack
        country.Push("USA");
        country.Push("India");

        // print elements inside the country Stack 
        foreach (string item in country)
        {
            Console.WriteLine(item);
        }
    }
}
```

**Output**

India
USA

Here, `country` is a stack that contains string elements (`"USA"` and `"India"`).

We will learn about `Stack<T>` in detail.

**Note:** In C#, there are two types of stack collection classes:

- `Stack<T>` - generic
- `Stack` - non-generic

It is recommended to use generic `Stack<T>` class.

---

## Stack Implementation

In stack, elements are stored and accessed in **Last In First Out** (LIFO) manner. That is, elements are added to the top of the stack and removed from the top of the stack.

![Working of stack data structure](https://www.programiz.com/sites/tutorial2program/files/csharp-stack-implementation.png "Working of stack data structure")

Working of stack data structure

---

## Create a Stack

To create `Stack<T>` in C#, we need to use the `System.Collection.Generic` namespace. Here is how we can create `Stack<T>` in C#,

```
Stack<dataType> stackName = new Stack<dataType>();
```

Here, `dataType` indicates the stack's type. For example,

```
// create Integer type stack
Stack<int> stack1 = new Stack<int>();

// create String type stack
Stack<string> stack2 = new Stack<string>();
```

---

## C# Stack Methods

C# provides **3** major `Stack<T>` methods. These methods are:

1. `Push()` - adds element to the top of the stack
2. `Pop()` - removes and returns an element from the top of the stack
3. `Peek()` - returns an element from the top of the stack without removing

Let's learn each method in detail.

---

## Stack Push() Method

To add an element to the top of the stack, we use the `Push()` method. For example,

```
using System;
using System.Collections.Generic;

class Program
{
    public static void Main()
    {
        // create a stack and push two elements 
        Stack<int> numbers = new Stack<int>();

        // add two elements to the stack
        numbers.Push(1);
        numbers.Push(5);

        // print elements inside the numbers Stack 
        foreach (int item in numbers)
        {
            Console.WriteLine(item);
        }
    }
}
```

**Output**

5
1

In the above example, we have created `Stack<T>` class named `numbers`.

Then we added **1** and **5** to the stack using the `Push()` method. We then printed those elements using a `foreach` loop.

Since the stack follows LIFO principle the element pushed at the last (**5**) is displayed at the first in the output.

---

## Stack Pop() Method

To remove an element from the top of the stack, we use the `Pop()` method. For example,

```
using System;
using System.Collections.Generic;

class Program
{
    public static void Main()
    {
        // create a stack  
        Stack<string> subject = new Stack<string>();
        subject.Push("Math");
        subject.Push("English");

        // pop the element from top of the stack 
        Console.WriteLine("Popped element: " + subject.Pop());
    }
}
```

**Output**

Popped element: English

In the above example, we have popped the element from the top of the `subject` stack using the `Pop()` method.

---

## Stack Peek() Method

The `Peek()` method returns the object at the top of the stack without removing it. For example,

```
using System;
using System.Collections.Generic;

class Program
{
    public static void Main()
    {
        // create a stack  
        Stack<string> cars = new Stack<string>();
        cars.Push("Toyota");
        cars.Push("BMW");

        // return the element at top of the Stack 
        Console.WriteLine("Element at top of stack: " + cars.Peek());
    }
}
```

**Output**

Element at top of stack: BMW

Here, we have displayed the element present at the top of the `cars` stack.

---

## Frequently Asked Questions

How to check whether an element is present inside a stack?

How to remove all the elements from Stack?

- [](https://www.programiz.com/csharp-programming/stack#stack-implementation)
- [](https://www.programiz.com/csharp-programming/stack#create-a-stack)
- [](https://www.programiz.com/csharp-programming/stack#stack-methods)
- [](https://www.programiz.com/csharp-programming/stack#push()-method)
- [](https://www.programiz.com/csharp-programming/stack#pop()-method)
- [](https://www.programiz.com/csharp-programming/stack#peek()-method)

[

  


](https://www.programiz.com/csharp-programming/arraylist "C# ArrayList")