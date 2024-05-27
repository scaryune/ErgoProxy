# C# String

In C#, a string is a sequence of characters. For example, `"hello"` is a string containing a sequence of characters `'h'`, `'e'`, `'l'`, `'l'`, and `'o'`.

We use the `string` keyword to create a string. For example,

```
// create a string
string str = "C# Programming";
```

Here, we have created a `string` named str and assigned the text `"C# Programming"`. We use double quotes to represent strings in C#.

---

### Example: Create string in C#

```
using System;  
namespace CsharpString {  
  class Test {
    public static void Main(string [] args) {
      
      // create string
      string str1 = "C# Programming";
      string str2 = "Programiz";
      
      // print string
      Console.WriteLine(str1);
      Console.WriteLine(str2);

      Console.ReadLine();
    }
  } 
}
```

**Output**

C# Programming
Programiz

In the above example, we have created two strings named str1 and str2 and printed them.

**Note**: A string variable in C# is not of primitive types like `int`, `char`, etc. Instead, it is an object of the `String` class.

---

## String Operations

C# string provides various methods to perform different operations on strings. We will look into some of the commonly used string operations.

### 1. Get the Length of a string

To find the length of a string, we use the `Length` property. For example,

```
using System;  
namespace CsharpString {  
  class Test {
    public static void Main(string [] args) {

      // create string
      string str = "C# Programming";
      Console.WriteLine("string: " + str);
      
      // get length of str
      int length = str.Length;     
      Console.WriteLine("Length: "+ length);

      Console.ReadLine();
    }
  } 
}
```

**Output**

string: C# Programming
Length: 14

In the above example, the `Length` property calculates the total number of characters in the string and returns it.

---

### 2. Join two strings in C#

We can join two strings in C# using the `Concat()` method. For example,

```
using System;  
namespace CsharpString {  
  class Test {
    public static void Main(string [] args) {

      // create string
      string str1 = "C# ";
      Console.WriteLine("string str1: " + str1);

      // create string
      string str2 = "Programming";
      Console.WriteLine("string str2: " + str2);
      
      // join two strings
      string joinedString = string.Concat(str1, str2);
      Console.WriteLine("Joined string: " + joinedString);

      Console.ReadLine();
    }
  } 
}
```

**Output**

string str1: C#
string str2: Programming
Joined string: C# Programming

In the above example, we have created two strings named str1 and str2. Notice the statement,

```
string joinedString = string.Concat(str1, str2);
```

Here, the `Concat()` method joins str1 and str2 and assigns it to the joinedString variable.

We can also join two strings using the `+` operator in C#. To learn more, visit _C# string Concat_.

---

### 3. C# compare two strings

In C#, we can make comparisons between two strings using the `Equals()` method. The `Equals()` method checks if two strings are equal or not. For example,

```
using System;  
namespace CsharpString {  
  class Test {
    public static void Main(string [] args) {

      // create string
      string str1 = "C# Programming";
      string str2 = "C# Programming";
      string str3 = "Programiz";
      
      // compare str1 and str2
      Boolean result1 = str1.Equals(str2);
      Console.WriteLine("string str1 and str2 are equal: " + result1);

      //compare str1 and str3
      Boolean result2 = str1.Equals(str3);
      Console.WriteLine("string str1 and str3 are equal: " + result2);     

      Console.ReadLine();
    }
  } 
}
```

**Output**

string str1 and str2 are equal: True
string str1 and str3 are equal: False

In the above example, we have created 3 strings named str1, str2, and str3. Here, we are using the `Equals()` method to check if one string is equal to another.

---

## Immutability of String Objects

In C#, strings are immutable. This means, once we create a string, we cannot change that string.

To understand it, consider an example:

```
// create string
string str = "Hello ";
```

Here, we have created a string variable named str. The variable holds the string `"Hello "`.

Now suppose we want to change the string str.

```
// add another string "World"
// to the previous string example
str = string.Concat(str, "World");
```

Here, we are using the `Concat()` method to add the string "World" to the previous string str.

But how are we able to modify the string when they are immutable?

Let's see what has happened here,

1. C# takes the value of the string `"Hello "`.
2. Creates a new string by adding `"World"` to the string `"Hello "`.
3. Creates a new string object, gives it a value `"Hello World"`, and stores it in str.
4. The original string, `"Hello "`, that was assigned to str is released for garbage collection because no other variable holds a reference to it.

---

## String Escape Sequences

The escape character is used to escape some of the characters present inside a string. In other words, we use escape sequences to insert special characters inside the string.

Suppose we need to include double quotes inside a string.

```
// include double quote
string str = "This is the "String" class";
```

Since strings are represented by double quotes, the compiler will treat `"This is the "` as the string. And the above code will cause an error.

To solve this issue, we use the escape character `\"` in C#. For example,

```
// use the escape character
string str = "This is the \"String\" class.";
```

Now by using `\` before double quote `"`, we can include it in the string.

Some of the escape sequences in C# are as follows:

|Escape Sequence|Character Name|
|---|---|
|`\'`|single quote|
|`\"`|double quote|
|`\\`|backslash|
|`\0`|null|
|`\n`|new line|
|`\t`|horizontal tab|

---

## String interpolation

In C#, we can use string interpolation to insert variables inside a string. For string interpolation, the string literal must begin with the `$` character. For example,

```
using System;  
namespace CsharpString {  
  class Test {
    public static void Main(string [] args) {

      // create string
      string name = "Programiz";

      // string interpolation
      string message = $"Welcome to {name}";
      Console.WriteLine(message);

      Console.ReadLine();
    }
  } 
}
```

**Output**

Welcome to Programiz

In the above example, we are using the name variable inside the message string.

```
string message = $"Welcome to {name}";
```

Notice that,

- the string literal starts with `$`
- the name variable is placed inside the curly braces `{}`

---

## Methods of C# string

There are various string methods in C#. Some of them are as follows:

|Methods|Description|
|---|---|
|`Format()`|returns a formatted string|
|`Split()`|splits the string into substring|
|`Substring()`|returns substring of a string|
|`Compare()`|compares string objects|
|`Replace()`|replaces the specified old character with the specified new character|
|`Contains()`|checks whether the string contains a substring|
|`Join()`|joins the given strings using the specified separator|
|`Trim()`|removes any leading and trailing whitespaces|
|`EndsWith()`|checks if the string ends with the given string|
|`IndexOf()`|returns the position of the specified character in the string|
|`Remove()`|returns characters from a string|
|`ToUpper()`|converts the string to uppercase|
|`ToLower()`|converts the string to lowercase|
|`PadLeft()`|returns string padded with spaces or with a specified Unicode character on the left|
|`PadRight()`|returns string padded with spaces or with a specified Unicode character on the right|
|`StartsWith()`|checks if the string begins with the given string|
|`ToCharArray()`|converts the string to a `char` array|
|||
|`LastIndexOf()`|returns index of the last occurrence of a specified string|

## Frequently Asked Questions

1. How to create an array of strings in C#?

2. Difference between string and String in C#

- [](https://www.programiz.com/csharp-programming/string#introduction)
- [](https://www.programiz.com/csharp-programming/string#string-example)
- [](https://www.programiz.com/csharp-programming/string#operation)
- [](https://www.programiz.com/csharp-programming/string#immutable)
- [](https://www.programiz.com/csharp-programming/string#escape)
- [](https://www.programiz.com/csharp-programming/string#interpolation)
- [](https://www.programiz.com/csharp-programming/string#methods)

[

  


](https://www.programiz.com/csharp-programming/expressions-statements-blocks "C# Expressions, Statements and Blocks")