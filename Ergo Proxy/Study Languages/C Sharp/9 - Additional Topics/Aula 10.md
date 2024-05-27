# C# Nullable Types

In C#, the nullable type allows us to assign `null` to the variable. For example,

```
Nullable<int> x = null;
```

Here, we have assigned `null` value to the integer type variable `x`.

---

## Declare Nullable Type

In C#, we can declare the nullable type as:

```
Nullable<dataType> variableName = null;
```

Here, `dataType` is **Value Data Types** like floating point type, integer type, boolean type etc.

## Another way to declare Nullable Type

**Declaring Nullable Type using ? operator**

---

## Why Nullable Type?

In C#, we cannot directly assign null value to a variable type. For example,

```
using System;
class Program
{
    public static void Main()
    {
        // assigning 'null' to x 
        int x = null;

        Console.WriteLine(x);
    }
}
```

This code throws a compiler error:

```
Cannot convert null to 'int' because it is a non-nullable value type
```

So in place of that, we use the `Nullable` type to assign `null` to the variable as:

```
using System;
class Program
{
    public static void Main()
    {
        // assigning 'null' to x 
        Nullable<int> x = null;

        Console.WriteLine(x);
    }
}
```

The above program does not throw an error.

---

## Access the Nullable Type

To access the value of the `Nullable` Type, we use the `GetValueOrDefault()` method. For example,

```
using System;
class Program
{
    public static void Main()
    {
        // assigning 'null' to integer type variable x 
        Nullable<int> x = null;

        // access Nullable type 
        Console.WriteLine("Value of x: " + x.GetValueOrDefault());
    }
}
```

**Output**

Value of x: 0

In the above example, we have assigned `null` to the integer type variable `x`.

---

## Nullable with Different Data Types

In C#, the `Nullable` types work only with the value data types like integer types, floating point types, boolean types, etc. For example,

```
using System;
class Program
{
    public static void Main()
    {
        // assigning 'null' to integer type variable x 
        Nullable<int> x = null;

        // assigning 'null' to boolean type variable y
        Nullable<bool> y = null;

        // assigning 'null' to floating point type variable z 
        Nullable<float> z = null;


        // access Nullable types
        Console.WriteLine("Value of x: " + x.GetValueOrDefault());
        Console.WriteLine("Value of y: " + y.GetValueOrDefault());
        Console.WriteLine("Value of z: " + z.GetValueOrDefault());
    }
}
```

**Output**

Value of x: 0
Value of y: False
Value of z: 0

Here, we have assigned `null` to different types of variables.

---

## Frequently Asked Questions

Assignment rule for Nullable Type

How to check whether a value to a variable is assigned or not?

- [](https://www.programiz.com/csharp-programming/nullable-types#introduction)
- [](https://www.programiz.com/csharp-programming/nullable-types#declare-nullable-type)
- [](https://www.programiz.com/csharp-programming/nullable-types#why-nullable-type)
- [](https://www.programiz.com/csharp-programming/nullable-types#access-nullable-type)
- [](https://www.programiz.com/csharp-programming/nullable-types#Nullable-types-with-different-data-type)

[

  


](https://www.programiz.com/csharp-programming/tuple "C# Tuples")