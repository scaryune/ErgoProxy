# C# Comments

Comments are used in a program to help us understand a piece of code. They are human readable words intended to make the code readable. Comments are completely ignored by the compiler.

In C#, there are 3 types of comments:

1. Single Line Comments ( `//` )
2. Multi Line Comments (`/* */`)
3. XML Comments ( `///` )

---

## Single Line Comments

Single line comments start with a double slash `//`. The compiler ignores everything after `//` to the end of the line. For example,

int a = 5 + 7; // Adding 5 and 7

Here, `Adding 5 and 7` is the comment.

### Example 1: Using single line comment

```
// Hello World Program
using System;

namespace HelloWorld
{
	class Program
	{
		public static void Main(string[] args)  // Execution Starts from Main method
		{
			// Prints Hello World
			Console.WriteLine("Hello World!");
		}
	}
}
```

The above program contains 3 single line comments:

// Hello World Program
// Execution Starts from Main method

and

// Prints Hello World

Single line comments can be written in a separate line or along with the codes in same line. However, it is recommended to use comments in a separate line.

---

## Multi Line Comments

Multi line comments start with `/*` and ends with `*/`. Multi line comments can span over multiple lines.

### Example 2: Using multi line comment

```
/*
	This is a Hello World Program in C#.
	This program prints Hello World.
*/
using System;

namespace HelloWorld
{
	class Program
	{
		public static void Main(string[] args)
		{
			/* Prints Hello World     */
			Console.WriteLine("Hello World!");
		}
	}
}
```

The above program contains 2 multi line comments:

/*
This is a Hello World Program in C#.
This program prints Hello World.
*/

and

/* Prints Hello World */

Here, we may have noticed that it is not compulsory for a multi line comment to span over multiple lines.`/* … */` can be used instead of single line comments.

---

## XML Documentation Comments

XML documentation comment is a special feature in C#. It starts with a triple slash `///` and is used to categorically describe a piece of code.. This is done using XML tags within a comment. These comments are then, used to create a separate XML documentation file.

If you are not familiar with XML, see [What is XML?](https://www.w3schools.com/xml/xml_whatis.asp "What is XML?")

### Example 3: Using XML documentation comment

```
/// <summary>
///  This is a hello world program.
/// </summary>

using System;

namespace HelloWorld
{
	class Program
	{
		public static void Main(string[] args)
		{
			Console.WriteLine("Hello World!");
		}
	}
}
```

The XML comment used in the above program is

/// <summary>
/// This is a hello world program.
/// </summary>

The XML documentation (.xml file) generated will contain:

<?xml version="1.0"?>
<doc>
	<assembly>
		<name>HelloWorld</name>
	</assembly>
	<members>
	</members>
</doc>

Visit [XML Documentation Comments](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/xmldoc/xml-documentation-comments) if you are interested in learning more.

---

## Use Comments the Right Way

Comments are used to explain parts of code but they should not be overused .

For example:

// Prints Hello World
Console.WriteLine("Hello World");

Using comment in the above example is not necessary. It is obvious that the line will print Hello World. Comments should be avoided in such cases.

- Instead comments should be used in the program to explain complex algorithms and techniques.
- Comments should be short and to the point instead of a long description.
- As a rule of thumb, it is better to explain **why** instead of **how**, using comments.