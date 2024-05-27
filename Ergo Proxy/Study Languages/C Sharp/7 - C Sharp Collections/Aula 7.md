# C# SortedList

A `SortedList` is a non-generic collection that contains key/value pairs where keys are sorted in an order. For example,

```
using System;
using System.Collections;

class Program
{
    public static void Main()
    {
        // create a SortedList
        SortedList myList = new SortedList();
        myList.Add(2, "Python");
        myList.Add(1, "Java");
        myList.Add(3, "C");

        // iterate through myList 
        for (int i = 0; i < myList.Count; i++)
        {
            Console.WriteLine("{0} : {1} ", myList.GetKey(i),
            myList.GetByIndex(i));
        }
    }
}
```

**Output**

1 : Java 
2 : Python 
3 : C 

Here, `myList` is a `SortedList` that contains key/value pairs.

We will learn about `SortedList` in detail.

---

## Create an SortedList

To create `SortedList` in C#, we need to use the `System.Collections` namespace. Here is how we can create `SortedList`:

```
// create a sorted list 
SortedList myList = new SortedList();
```

Here, we have created a `SortedList` named `myList`.

---

## Basic Operations on SortedList

In C#, we can perform different operations on sortedlist. We will look at some commonly used `SortedList` operations in this tutorial:

- Add Elements
- Access Elements
- Change Elements
- Remove Elements

Let's see how we can perform these operations in detail!

---

## Add Elements in SortedList

C# provides a method `Add()` using which we can add elements in `SortedList`. For example,

```
using System;
using System.Collections;

class Program
{
    public static void Main()
    {
        // create a SortedList and add items 
        SortedList person = new SortedList();
 
        person.Add(2, 45);
        person.Add(1, "Jack");
        person.Add(3, "Florida");
    }
}
```

In the above example, we have created a `SortedList` named `person`.

Then we added three values, one integer type(**45**) and two string type (`"Jack"` and `"Florida"`) along with their keys(**2**, **1** and **3**).

---

## Access the SortedList

We can access the elements inside the `SortedList` using it's keys. For example,

```
using System;
using System.Collections;

class Program
{
    public static void Main()
    {
        SortedList myList = new SortedList();
        myList.Add(2, "Python");
        myList.Add(1, "Java");
        myList.Add(3, "C");

        // access the element whose key is 2
        Console.WriteLine("Element whose key is 2: " + myList[2]);

        // access the element whose key is 1
        Console.WriteLine("Element whose key is 1: " + myList[1]);
    }
}
```

**Output**

Element whose key is 2: Python
Element whose key is 1: Java

In the above example, we have accessed the elements using their keys:

- `myList[2]` - accesses the element whose key is **2**
- `myList[1]` - accesses the element whose key is **1**

**Note:** While accessing, if we pass the key which does not exist, the compiler throws an error.

---

## Iterate through SortedList

In C#, we can also loop through each element of `SortedList` using a `for` loop. For example,

```
using System;
using System.Collections;

class Program
{
    public static void Main()
    {
        SortedList myList = new SortedList();
        myList.Add(2, "BMW");
        myList.Add(1, 96);
        myList.Add(3, "Pizza");

        // iterate through myList 
        for (int i = 0; i < myList.Count; i++)
        {
            Console.WriteLine("{0} : {1} ", myList.GetKey(i),
            myList.GetByIndex(i));
        }
    }
}
```

**Output**

1 : 96 
2 : BMW 
3 : Pizza

In the above example, we have used a for loop to iterate through `myList`.

In order to get the keys and values of the `SortedList`, we use the `GetKey()` and `GetByIndex()` methods respectively.

Since the `SortedList` arranges the keys in ascending order, the output the keys are sorted.

**Note:** The Count property counts the total number of elements inside the list.

---

## Remove SortedList Elements

We can delete one or more items from `SortedList` using **2** methods:

- `Remove(key)` - removes the element according to the specified key
- `RemoveAt(index)` - removes the element according to the specified index

Let's see examples using both methods.

---

## Example: Remove() Method

```
using System;
using System.Collections;

class Program {
	public static void Main() {
	    SortedList myList = new SortedList();
	    myList.Add(2, "Evermore");
	    myList.Add(1, "Reputation");
	    myList.Add(3, "Folklore");
	    
	   // remove element whose key is 1 i.e "Reputation" 
	    myList.Remove(1);
	    
	    // iterating through the modified SortedList
	    for (int i =0; i< myList.Count; i++) {
	        Console.WriteLine("{0} : {1} ", myList.GetKey(i), 
	        myList.GetByIndex(i));
	    }
        }
}
```

**Output**

2 : Evermore 
3 : Folklore 

In the above example, we have removed the element whose **key** is **1**.

Here, `myList.Remove(1)` removes `"Reputation"` from `myList`. So when we iterate through `myList` we get a modified list as an output.

---

## Example: RemoveAt() Method

```
using System;
using System.Collections;

class Program {
	public static void Main() {
	    SortedList myList = new SortedList();
	    myList.Add(2, "Evermore");
	    myList.Add(1, "Reputation");
	    myList.Add(3, "Folklore");
	    
	   // remove element which is present in index 1 i.e "Evermore" 
	    myList.RemoveAt(1);
	    
	    // iterating through the modified SortedList
	    for (int i =0; i< myList.Count; i++) {
	        Console.WriteLine("{0} : {1}  ", myList.GetKey(i), 
	        myList.GetByIndex(i));
	    }
	}
}
```

**Output**

1 : Reputation  
3 : Folklore 

- [](https://www.programiz.com/csharp-programming/sortedlist#introduction)
- [](https://www.programiz.com/csharp-programming/sortedlist#create-a-sortedlist)
- [](https://www.programiz.com/csharp-programming/sortedlist#basic-operations-on-sortedlist)
- [](https://www.programiz.com/csharp-programming/sortedlist#add-elements-on-sortedlist)
- [](https://www.programiz.com/csharp-programming/sortedlist#access-sortedlist)
- [](https://www.programiz.com/csharp-programming/sortedlist#iterate-through-the-sortedlist)
- [](https://www.programiz.com/csharp-programming/sortedlist#remove-element-from-sortedlist)
- [](https://www.programiz.com/csharp-programming/sortedlist#remove-element-using-remove())
- [](https://www.programiz.com/csharp-programming/sortedlist#example-remove-element-using-removeAt())