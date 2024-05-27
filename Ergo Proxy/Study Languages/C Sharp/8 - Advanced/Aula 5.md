# C# Iterators

Iterators are methods that iterate collections like lists, tuples, etc. Using an iterator method, we can loop through an object and return it's elements.

---

## Create an Iterator Method

To create an iterator method, we use `yield return` keyword to return the value.

The return type of the iterator method is either `IEnumerable`, `IEnumerable<T>`, `IEnumerator`, or `IEnumerator<T>`.

We can define an iterator method as:

```
returnType methodName()
{
    yield return returnValue;
}
```

Here,

- `methodName()` - name of iterator method
- `returnType` - return type of the method
- `returnValue` - value returned by the method

**Note:** To learn more about `yield return`, visit [C# yield](https://www.programiz.com/csharp-programming/yield-keyword).

---

## Example 1: Iterator Method

```
using System;
using System.Collections;
class Program
{
    // define an iterator method
    static IEnumerable getString()
    {
        yield return "Sunday";
        yield return 2;
    }
    static void Main()
    {
        // display return values of getString()
        foreach (var items in getString())
        {
            Console.WriteLine(items);
        }
    }
}
```

**Output**

Sunday
2

Here, `getString()` is an iterator method that returns `"Sunday"` and **2** using `yield return`.

---

## Example 2: Iterator Method with List

```
using System;
using System.Collections.Generic;
class Program
{
    // define an iterator method 
    static IEnumerable<int> getList()
    {
        // create a list 
        List<int> myList = new List<int>();

        // add elements to the list 
        myList.Add(1);
        myList.Add(2);
        myList.Add(4);

        // iterate the elements of myList  
        foreach (var values in myList)
        {
            // return elements of myList which are divisible by 2
            if (values % 2 == 0)
                yield return values;
        }
    }
    static void Main()
    {
        // display return values of getList()  
        foreach (var items in getList())
        {
            Console.WriteLine(items);
        }
    }
}
```

**Output**

2
4

Here, we have defined an iterator method named `getList()` whose return type is `IEnumerable<int>`.

Inside the `getList()` method we have iterated through `myList` using `yield return`. Notice the code,

```
// iterate the elements of myList  
foreach (var values in myList)
{
    // return elements of myList which are divisible by 2
    if (values % 2 == 0)
        yield return values;
}
```

Here, `yield return` preserves the location of the current code and the control goes back to the caller(i.e. inside `foreach` of `Main()`).

Inside the `Main()` method, the `foreach` loop prints the value returned by `yield return`. Notice the code below,

```
// display return values of getList()  
foreach (var items in getList())
{
    Console.WriteLine(items);
}
```

Then `foreach` calls the `getList()` method again for the next iteration. Same process continues till every of `myList` is iterated.

In way, we can do custom iteration over a collection like `[List<T>](https://www.programiz.com/csharp-programming/list)` in C#.

- [](https://www.programiz.com/csharp-programming/iterators#introduction)
- [](https://www.programiz.com/csharp-programming/iterators#create-an-iterable-method)
- [](https://www.programiz.com/csharp-programming/iterators#example-iterator-method)
- [](https://www.programiz.com/csharp-programming/iterators#example-iterable-method)

[

  


](https://www.programiz.com/csharp-programming/generics "C# generics")