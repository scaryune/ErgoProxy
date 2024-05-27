# C# Indexers

An indexer allows us to access instances of a class using an index just like an array.

---

## Define C# Indexer

In C#, we define an indexer just like _properties_ using `this` keyword followed by `[]` index notation. For example,

```
public int this[int index]
{
    get
    {
        return val[index];
    }

    set
    {
        val[index] = value;
    }
}
```

Here,

- `public` - access modifier
- `int` - return type of indexer
- `this` - indicates we are defining indexer in current class
- `int index` - access values using integer index position
- `get` - ,method that returns values
- `set` - method that assigns values

---

## Example: C# indexer

```
using System;
class Program
{
    // declare an array to store elements  
    private string[] studentName = new string[10];

    // define an indexer
    public string this[int index]
    {
        get
        {
            // return value of stored at studentName array  
            return studentName[index];
        }

        set
        {
            // assigns value to studentName  
            studentName[index] = value;
        }
    }

    public static void Main()
    {
        // create instance of Program class 
        Program obj = new Program();

        // insert values in obj[] using indexer i.e index position
        obj[0] = "Harry";
        obj[1] = "Ron";
        obj[2] = "Hermoine";

        Console.WriteLine("First element in obj: " + obj[0]);
        Console.WriteLine("Second element in obj: " + obj[1]);
    }
}
```

**Output**

First element in obj: Harry
Second element in obj: Ron

In the above example, notice the code

```
// declare an array to store elements  
private string[] studentName = new string[10];
```

Here, we have declared the `studentName` array of size **10**.

Then we have defined an indexer of `string` type. Notice the code below,

```
// define an indexer
public string this[int index]
{
    get
    {
        // return value stored at studentName array  
        return studentName[index];
    }

    set
    {
        // assigns value to studentName  
        studentName[index] = value;
    }
}
```

Here, the `set` method assigns values to `studentName` using `index`. And the `get` method returns values stored at `studentName`.

Notice the code,

```
// create instance of Program class 
Program obj = new Program();

// insert values in obj[] using indexer i.e index position
obj[0] = "Harry";
obj[1] = "Ron";
obj[2] = "Hermoine";
```

Here, we have used `obj` (instance of the `Program` class) like the `studentName` array.

**Note:** Without using indexer, we access the `studentName` array through `obj` as:

```
// insert value to studentName array when indexer is not used 
obj.studentName[0] = "Harry";
```

Indexer helps to simplify the syntax.

---

## Generic Indexer in C#

In C#, we can also use indexers with a generic class. For example,

```
using System;
class EmployeeInfo<T>
{
    // declare an array to store elements  
    private T[] employee = new T[50];

    // define an indexer, 
    // T indicates return type of indexer is generic 
    public T this[int index]
    {
        get
        {
            // return value of stored at studentName array  
            return employee[index];
        }

        set
        {
            // assigns value to studentName  
            employee[index] = value;
        }
    }
}
class Program
{
    public static void Main()
    {
        // create instance of EmployeeInfo class of int type  
        EmployeeInfo<int> Id = new EmployeeInfo<int>();

        // insert integer values in Id[] using indexer i.e index position
        Id[0] = 3;
        Id[1] = 23;
        Id[2] = 10;

        Console.WriteLine("First element in Id object: " + Id[0]);

        // create instance of EmployeeInfo class of string type 
        EmployeeInfo<string> Name = new EmployeeInfo<string>();

        // insert string values in Name[] using indexer i.e index position
        Name[0] = "Taylor";
        Name[1] = "Selena";
        Name[2] = "Joe";

        Console.WriteLine("First element in Name object: " + Name[0]);
    }
}
```

**Output**

First element in Id object: 3
First element in Name object: Taylor

In the above example, notice the code,

```
public T this[int index]
{
    get
    {
        // return value of stored at studentName array  
        return employee[index];
    }

    set
    {
        // assigns value to studentName  
        employee[index] = value;
    }
}
```

Here, we have defined an indexer with return type `T` which indicates it can return any generic data type.

Also, we have created an instance of the `EmployeeInfo` class of type `int` and `string`. Notice the code,

```
// create instance of EmployeeInfo class of int type  
EmployeeInfo<int> Id = new EmployeeInfo<int>();

// create instance of EmployeeInfo class of string type 
EmployeeInfo<string> Name = new EmployeeInfo<string>();
```

Here, the two instances `Id` and `Name` are used like an array using index. Notice the code,

```
// insert integer values in Id[] using indexer i.e index position
Id[0] = 3;

// insert string values in Name[] using indexer i.e index position
Name[0] = "Taylor";
```