# C# Hashtable

A Hashtable is a non-generic collection that stores key/value pairs that are arranged based on the hashcode of each key.

The `Hashtable` Class implements `ICollection`.

![C# Hashtable implements ICollection](https://www.programiz.com/sites/tutorial2program/files/csharp-hashtable.png "C# Hashtable implements ICollection")

C# Hashtable implements ICollection

---

## Create a Hashtable

To create `Hashtable` in C#, we need to use the `System.Collections` namespace. Here is how we can create a `Hashtable` in C#.

```
// create a hashtable
Hashtable myTable = new Hashtable();
```

---

## Example: Create a Hashtable

```
using System;
using System.Collections;
class Program
{
    public static void Main()
    {
        // create a hashtable
        Hashtable myTable = new Hashtable();

        // add items to hashtable
        myTable.Add("Name", "Ginny");
        myTable.Add("RollNumber", 12);
        myTable.Add("Address", "Miami");

        // print value of the element whose key is "RollNumber"
        Console.WriteLine(myTable["RollNumber"]);
    }
}
```

**Output**

12

---

## Basic Operations on Hashtable

In C#, we can perform different operations on a hashtable. We will look at some commonly used `Hashtable` operations in this tutorial:

- Add Elements
- Access Elements
- Change Elements
- Remove Elements

Let's see how we can perform these operations in detail!

---

## Add Elements in Hashtable

C# provides the `Add()` method using which we can add elements in `Hashtable`. For example,

```
using System;
using System.Collections;
class Program
{
    public static void Main()
    {
        // create a hashtable
        Hashtable myTable = new Hashtable();

        // add items to hashtable
        myTable.Add("Subject", "Math");
        myTable.Add("Code", 139);
    }
}
```

In the above example, we have created a `Hashtable` named `myTable`.

Here we have added key/value pairs using the `Add()` method:

- keys - `"Subject"` and `"Code"`
- values - `"Math"` and **139**

**Note:** In `Hashtable`, keys must be unique and cannot be `null`. However, values can be `null` or duplicate.

---

## Another way to add Elements to Hashtable

Add Elements in a`Hashtable`without using`Add()`method

---

## Access Hashtable Elements

We can access the elements inside the `Hashtable` using it's keys. For example,

```
using System;
using System.Collections;
class Program
{
    public static void Main()
    {
        // create a hashtable and add elements 
        Hashtable myTable = new Hashtable();

        // add items to hashtable
        myTable.Add("Employee", "James");
        myTable.Add("Id", 13);

        // access the value whose key is "Employee"
        Console.WriteLine(myTable["Employee"]);
```

```
       // access the value whose key is "Id"
        Console.WriteLine(myTable["Id"]);
    }
}
```

**Output**

James
13

In the above example, we have accessed the values of `Hashtable` using their keys:

- `myTable["Employee"]` - accesses the value whose key is `"Employee"`
- `myTable["Id"]` - accesses the value whose key is `"Id"`

---

## Iterate Hashtable

In C#, we can also loop through each element of `Hashtable` using a `foreach` loop. For example,

```
using System;
using System.Collections;
class Program
{
    public static void Main()
    {
        // create a hashtable and add elements 
        Hashtable myTable = new Hashtable();

        // add items to hashtable
        myTable.Add("Employee", "Jake");
        myTable.Add("Id", 23);
        myTable.Add("Address", "Cornelia Street");

        // print keys of hashtable
        foreach (var item in myTable.Keys)
        {
            Console.WriteLine("Key = {0}", item);
        }

        // print values of hashtable   
        foreach (var item in myTable.Values)
        {
            Console.WriteLine("Value = {0}", item);
        }
    }
}
```

**Output**

Key = Address
Key = Employee
Key = Id
Value = Cornelia Street
Value = Jake
Value = 23

In the above example, we have looped through `myTable` using a `foreach` loop.

---

## Another way to iterate through Hashtable

Iterate using DictionaryEntry

---

## Change Hashtable Elements

We can change the value of elements in `Hashtable` as:

```
using System;
using System.Collections;
class Program
{
    public static void Main()
    {
        // create a hashtable and add elements 
        Hashtable myTable = new Hashtable();

        // add items to hashtable
        myTable.Add("Employee", "Jake");
        myTable.Add("Id", 23);
        myTable.Add("Address", "Cornelia Street");

        // print original value 
        Console.WriteLine("Value of Address before changing: " + myTable["Address"]);

        // change the value of "Address" key to "Ontario"
        myTable["Address"] = "Ontario";

        // print new updated value of "Address"
        Console.WriteLine("Value of Address after changing: " + myTable["Address"]);
    }
}
```

**Output**

Value of Address before changing: Cornelia Street
Value of Address after changing: Ontario

Here, we have changed the value of the `"Address"` key in `myTable`.

---

## Remove Hashtable Elements

To remove the elements of `Hashtable` we use:

- `Remove(key)` - removes the element according to the specified key

For example,

```
using System;
using System.Collections;
class Program
{
    public static void Main()
    {
        // create a hashtable and add elements 
        Hashtable myTable = new Hashtable();

        // add items to hashtable
        myTable.Add("Employee", "Tom");
        myTable.Add("Id", 5);
        myTable.Add("Address", "London");

        Console.WriteLine("Original Hashtable :");

        foreach (DictionaryEntry item in myTable)
        {
            Console.WriteLine("{0} : {1} ", item.Key, item.Value);
        }

        // remove value with key "Id"
        myTable.Remove("Id");

        Console.WriteLine("\nModified Hashtable :");

        // iterate through the modified hashtable
        foreach (DictionaryEntry item in myTable)
        {
            Console.WriteLine("{0} : {1} ", item.Key, item.Value);
        }
    }
}
```

**Output**

Original Hashtable :
Employee : Tom 
Address : London
Id : 5

Modified Hashtable :
Employee : Tom
Address : London

In the above example, we have removed the element whose key is `"Id"`.

Here, `myTable.Remove("Id")` removes **5** from `myTable`. So when we iterate through `myTable` we get a modified `Hashtable` that does not contain `"Id"`.

- [](https://www.programiz.com/csharp-programming/hashtable#introduction)
- [](https://www.programiz.com/csharp-programming/hashtable#create-a-hashtable)
- [](https://www.programiz.com/csharp-programming/hashtable#example-create-a-hashtable)
- [](https://www.programiz.com/csharp-programming/hashtable#basic-operations-on-hashtable)
- [](https://www.programiz.com/csharp-programming/hashtable#add-elements-on-hashtable)
- [](https://www.programiz.com/csharp-programming/hashtable#access-a-hashtable)
- [](https://www.programiz.com/csharp-programming/hashtable#iterate-hashtable)
- [](https://www.programiz.com/csharp-programming/hashtable#change-elements-of-Hashtable)

[

  


](https://www.programiz.com/csharp-programming/sortedlist "C# SortedList")