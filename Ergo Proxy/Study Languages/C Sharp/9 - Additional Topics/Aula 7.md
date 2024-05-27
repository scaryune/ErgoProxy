# Namespaces in C# Programming

Namespaces are used in C# to organize and provide a level of separation of codes. They can be considered as a container which consists of other namespaces, classes, etc.

A namespace can have following types as its members:

1. Namespaces (Nested Namespace)
2. Classes
3. Interfaces
4. Structures
5. Delegates

We will discuss about these topics in later tutorials. For now we will stick with classes and namespaces.

Namespaces are not mandatory in a C# program, but they do play an important role in writing cleaner codes and managing larger projects.

Let's understand the concept of namespace with a real life scenario. We have a large number of files and folders in our computer. Imagine how difficult it would be to manage them if they are placed in a single directory. This is why we put related files and folders in a separate directory. This helps us to manage our data properly.

The concept of namespace is similar in C#. It helps us to **organize** different members by putting related members in the same namespace.

Namespace also solves the problem of **naming conflict**. Two or more classes when put into different namespaces can have same name.

---

## Defining Namespace in C#

We can define a namespace in C# using the _namespace_ keyword as:

namespace Namespace-Name
{
    //Body of namespace
}

For example:

```
namespace MyNamespace
{
    class MyClass
    {
        public void MyMethod()
        {
            System.Console.WriteLine("Creating my namespace");
		}
	}
}
```

In the above example, a namespace `MyNamespace` is created. It consists of a class `MyClass` as its member. `MyMethod` is a method of class `MyClass`.

---

## Accessing Members of Namespace in C#

The members of a namespace can be accessed using the `dot(.)` operator. The syntax for accessing the member of namespace is,

Namespace-Name.Member-Name

For example, if we need to create an object of MyClass, it can be done as,

MyNamespace.MyClass myClass = new MyNamespace.MyClass();

We will discuss about creating objects in later tutorials. For now just focus on how the class `MyClass` is accessed.

---

## Example 1: Introducing Namespace in C# Program

```
using System;

namespace MyNamespace
{
    public class SampleClass
    {
        public static void myMethod()
        {
            Console.WriteLine("Creating my namespace");
        }
    }
}
 
namespace MyProgram
{
    public class MyClass
    {
        public static void Main()
        {
            MyNamespace.SampleClass.myMethod();
        }
    }
}
```

When we run the program, the output will be:

Creating my namespace

In the above program, we have created our own namespace `MyNamespace` and accessed its members from `Main()` method inside `MyClass`. As said earlier, the `dot (.)` operator is used to access the member of namespace.

In the `Main()` method, `myMethod()` method is called using the `dot (.)` operator.

---

## Using a Namespace in C# [The using Keyword]

A namespace can be included in a program using the using keyword. The syntax is,

using Namespace-Name;

For example,

using System;

The advantage of this approach is we don't have to specify the fully qualified name of the members of that namespace every time we are accessing it.

Once the line

using System;

is included at the top of the program. We can write

Console.WriteLine("Hello World!");

Instead of the fully qualified name i.e.

System.Console.WriteLine("Hello World!");

---

## Nested Namespace in C#

A namespace can contain another namespace. It is called nested namespace. The nested namespace and its members can also be accessed using the `dot (.)` operator.

The syntax for creating nested namespace is as follows:

namespace MyNamespace
{
    namespace NestedNamespace
    {
        // Body of nested namespace
	}
}

---

### Example 2: Nested Namespace in C#

```
using System;
 
// Nested Namespace
namespace MyNamespace
{
    namespace Nested
    {
        public class SampleClass
        {
            public static void myMethod()
            {
                Console.WriteLine("Nested Namespace Example");
            }
        }
    }
}
 
namespace MyProgram
{
    public class MyClass
    {
        public static void Main()
        {
            MyNamespace.Nested.SampleClass.myMethod();
        }
    }
}
```

When we run the program, the output will be:

Nested Namespace Example

This example illustrates how nested namespace can be implemented in C#.

Here, we now have an extra namespace inside `MyNamespace` called `Nested`. So, instead of using `MyNamespace.SampleClass.myMethod()`, we have to use `MyNamespace.Nested.SampleClass.myMethod()`.

- [](https://www.programiz.com/csharp-programming/namespaces#what-is-namespace)
- [](https://www.programiz.com/csharp-programming/namespaces#defining-namespace)
- [](https://www.programiz.com/csharp-programming/namespaces#access-members)
- [](https://www.programiz.com/csharp-programming/namespaces#introducing-namespace)
- [](https://www.programiz.com/csharp-programming/namespaces#using-keyword)
- [](https://www.programiz.com/csharp-programming/namespaces#nested-namespace)
    - [](https://www.programiz.com/csharp-programming/namespaces#example-nested)

[

  


](https://www.programiz.com/csharp-programming/preprocessor-directives "C# Preprocessor directives")