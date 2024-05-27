# C# Anonymous Types

Anonymous type in C# allows us to create a type without specifying the name. For example,

```
var subject = new {Name = "Math", Code = 123};
```

Here, `subject` is an anonymous type variable containing two properties: `Name` and `Code`.

You can see we have used a `new` operator to create an anonymous type.

---

## Example: C# Anonymous Type

```
using System;
class Program
{
    static void Main()
    {
        // create an anonymous type containing 3 properties 
        var person = new { Age = 34, Name = "John", Address = "Miami" };

        // display the anonymous type
        Console.WriteLine(person);
    }
}
```

**Output**

{ Age = 34, Name = John, Address = Miami }

In the above example, `person` is an anonymous type variable with properties: `Age`, `Name`, and `Address` with values **32**, `"John"`, and `"Miami"`, respectively.

---

## C# Nested Anonymous Type

In C#, we can also create an anonymous type inside the property of another anonymous type. This is called nested anonymous type. For example,

```
using System;
class Program
{
    static void Main()
    {
        // create another anonymous type inside Employee property 
        var school = new
        {
            Address = "Orlando",
            Contact = 1200,
            Employee = new { Id = 3, Name = "Tina" }
        };

        // access Address property
        Console.WriteLine(school.Address);

        // access Id property of Employee property 
        Console.WriteLine(school.Employee.Id);
    }
}
```

**Output**

Orlando
3

In the above example, notice the code

```
var school = new
{
    Address = "Orlando",
    Contact = 1200,
    Employee = new { Id = 3, Name = "Tina" }
};
```

Here, we have created an anonymous type variable `school` with properties: `Address`, `Contact`, and `Employee`. You can see that the `Employee` property itself is also an anonymous type.

This is an example of a nested anonymous type.

Also, we are using the dot operator to access properties of the nested anonymous type.

- `school.Address` - accesses the `Address` property of school
- `school.Employee.Id` - accesses the `Id` property which is present inside the `Employee` property

---

## Features of Anonymous Type in C#

Some of the features of anonymous type in C# are:

- It encapsulates a set of read-only properties.
- It cannot contain method or events of a class.
- It has local scope. This means, the anonymous type is accessible only from the class in which it is defined.
- We can create an array of anonymous types.
- We can retrieve specific properties of anonymous type using LINQ.

---

## Frequently Asked Questions

Can anonymous types contain methods?

Can we change properties inside the anonymous type?

How to create an array of anonymous types?

How to retrieve specific properties of an anonymous type in LINQ?