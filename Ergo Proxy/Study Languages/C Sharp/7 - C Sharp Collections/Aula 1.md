# C# Collections

In C# Collections are classes that provide an easy way to work with a group of objects.

For example,

`System.Collections.Generic`

classes provide the implementation of strongly typed entities like lists, stacks etc.

---

## Types of C# Collection Classes

In C# collections are divided into **3** classes. They are:

1. System.Collections.Generic
2. System.Collections
3. System.Collections.Concurrent

Let's learn about each class in more detail!

---

## System.Collections.Generic Classes

The `System.Collections.Generic` classes help us to create a generic collection. In this, we store type compatible data elements. This collection does not allow us to store different types of elements.

Let's take an example of a generic class: `List<T>`.

```
using System;
using System.Collections.Generic;

class Program
{
    public static void Main()
    {
        // create a list named number that contains integer data items
        List<int> number = new List<int>();
        number.Add(1);
        number.Add(2);
        number.Add("Programiz");

        Console.WriteLine(number[1]); //
    }
}
```

The above code throws the following error:

```
Argument 1: cannot convert from 'string' to 'int'
```

Here, we have defined the type of the `number` list, which is `int`.

Since `List<T>` comes under generic collection, we cannot add an element of a different data type(i.e. `string`).

---

## Some System.Collections.Generic Classes

In C#, following are the classes that come under `System.Collections.Generic` namespace:

### 1. List Class

The `List<T>` class is used to store multiple elements of the **same data type** that can be accessed using the indexes. We can add, insert and remove elements inside the list. Moreover, we can dynamically change the size of the list.

### 2. Stack Class

The `Stack<T>` class is also generic, which means we store data elements of the same data type.

In stack, the elements are stored in LIFO(Last In First Out) manner. With the help of methods, we can perform operations in stack:

- `Push()`- insert elements
- `Pop()`- remove elements

### 3. Queue Class

In `Queue<T>` class, the objects are stored in FIFO(First In First Out) manner. Here, the elements are inserted at one end and removed from the other. It is implemented using a circular queue. We can perform operations using methods like:

- `Enqueue()`- add elements
- `Dequeue()` - remove elements

### 4. SortedList Class

The `SortedList<TKey,TValue>` is an array that consists of key/value pairs that are sorted in an order. Every key inside `SortedList<TKey,TValue>` must be unique, and using those keys we can access the elements inside it. `null` value is not accepted as a key.

---

## System.Collections Classes

In C#, the `System.Collections` classes help us to create a **non-generic** collection.

For this we use `System.Collections` namespace. Using this we can create classes where we can add data elements of multiple data types.

Following are some of the classes that are in `System.Collections` namespace:

### 1. ArrayList Class

`ArrayList` is non-generic which means we can store elements of multiple data types. We use the `ArrayList` class to implement the functionality of resizable arrays. Duplicate elements are allowed inside `ArrayList`.

We can use the sort method to sort the elements inside it.

### 2. Hashtable Class

`Hashtable` is also non-generic which consists of key/value pairs that are managed using the hash code of the particular key. The key cannot be `null` however a value can be null. We can perform dynamic allocation of the memory inside `Hashtable`.

---

## System.Collections.Concurrent Classes

The `System.Collections.Concurrent` provides some collection classes that help to achieve thread-safe code.

### What is Thread Safety?

There can be situations when multiple threads are trying to execute the same piece of code. The code is said to be "thread-safe" if it can be executed correctly irrespective of multiple threads accessing concurrently.

It is recommended to use `System.Collections.Concurrent` classes rather than `System.Collections` and `System.Collections.Generic` classes when multiple threads are accessing the collection.

Some of the thread-safe collection classes are:

- `ConcurrentStack<T>`
- `ConcurrentQueue<T>`
- `ConcurrentDictionary<TKey,TValue>`