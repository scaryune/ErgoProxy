# C# Tuples

A tuple in C# allows us to store elements of different data types. For example,

```
var student = ("Taylor", 27, "Orlando");
```

Here, `student` is a tuple that consists of two string elements (`"Taylor"` and `"Orlando"`) and an integer element (**27**).

---

## Create Tuple in C#

C# provides various ways for creating tuples. We will learn about the following methods:

1. Using Parentheses
2. Using the Create() Function

Let's understand both of these processes in detail.

---

## 1. C# Tuple Using Parentheses

We can create a tuple by directly assigning different values using parentheses `()`. For example,

```
using System;

class Program {
    public static void Main() {
        // create a tuple containing 3 elements
        var student= ("Taylor", 5, "Orlando");
        Console.WriteLine(student);
    }
}
```

**Output**

("Taylor", 5, "Orlando")

In the above example, we have created a tuple without mentioning the datatypes of the elements.

In this way, we can store data elements of different data types inside a tuple without mentioning the datatype.

**Note:** However, we can also mention the data type of the tuple as:

```
using System;

class Program {
	public static void Main() {
	    
                (string,int,string) student = ("Taylor", 5, "Orlando"); 
                 Console.WriteLine(student);
	}
}
// Output: (Taylor, 5, Orlando)
```

---

## 2. C# Tuple using Create() Method

In C# we can also use the `Create()` method to create a tuple without having to mention the datatypes of the tuple elements.

The syntax for creating tuple using `Create()` is:

```
var t1 = Tuple.Create(value);
```

To understand it clearly, let's see an example:

```
using System;
					
class Program {
    public static void Main() {
        // create a tuple containing 3 elements 
         var programming = Tuple.Create("programiz", "java", 12);
        Console.WriteLine(programming);
    }
}
```

**Output**

(programiz, java, 12)

In the above example, we have used the `Create()` method to create a tuple named `programming` that contains **3** elements.

**Note:** While creating a tuple using the `Create()` method it can only include a maximum of eight elements.

---

## Access Tuple Elements

In the previous example, we have directly displayed the whole tuple. However, it is possible to access each element of the tuple.

In C# each element of the tuple is associated with a default name.

- first element - `Item1`
- second element - `Item2`
- and so on

We can access elements of tuple using the default name. For example,

```
using System;
					
class Program {
	public static void Main() {
	    
	    var subjects = Tuple.Create("Science", "Maths", "English");
        // access the first element 
        Console.WriteLine("The first element is " + subjects.Item1);
        // access the second element
        Console.WriteLine("The second element is " +subjects.Item2);
	}
}
```

**Output**

The first element is Science
The second element is Maths

In the above example:

- `subjects.Item1` - accesses the first element
- `subjects.Item2` - accesses the second element

---

## Change Value of the Tuple Element

We can change the value of data inside a tuple. To change the elements of the tuple, we can reassign a new value to the default name. For example,

```
using System;
					
class Program {
    public static void Main() {
        var roll_num = (5, 7, 8, 3);
	    
         // original tuple
         Console.WriteLine("Original Tuple: " + roll_num);
	    
        // replacing the value 7 with 6
        roll_num.Item2 = 6; 
         Console.WriteLine("Changing value of 2nd element to " + roll_num.Item2);
         Console.WriteLine("Modified Tuple: " + roll_num);
    }
}
```

**Output**

Original Tuple: (5, 7, 8, 3)
Changing value of 2nd element to 6
Modified Tuple: (5, 6, 8, 3)

In the above example, we have replaced the value of the 2nd element with **6**.

**Note:** If we have used `Create()` to create a tuple, then we cannot change the value of the elements. That means the elements of the tuple are read-only.

For example,

```
using System;

class Program {
	public static void Main() {
	    var t1= Tuple.Create("Taylor", "Jack");
	    t1.Item2 = "Monica";
	    Console.WriteLine(t1.Item2);
	}
}
```

**Output**

Property or indexer 'Tuple<string, string>.Item2' cannot be assigned to -- it is read only

---

## Nested Tuple

We can create a tuple inside another tuple. A tuple within a tuple is called a nested tuple. For example,

```
using System;
					
class Program {
    public static void Main() {
	    
         var myTuple= Tuple.Create("Taylor", "Jack", Tuple.Create(7, 8, 9));
        Console.WriteLine("The elements inside myTuple: " + myTuple); 
    }
}
```

**Output**

The elements inside myTuple: (Taylor, Jack, (7, 8, 9))   

Here, we have a tuple `(7, 8, 9)` inside the `myTuple` tuple. This is called a nested tuple.

---

## Other Topics in C# Tuples

C# Tuple as a Method Parameter

C# Tuple as a Return Type

Named Properties in Tuples

Why use Tuples?