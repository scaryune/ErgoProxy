
# C# Hello World - Your First C# Program

Let's write our first C# program.

We will write a simple program C# that displays `Hello, World!` on the screen.

```
public class Program
{
    public static void Main(string[] args)
    {
        System.Console.WriteLine("Hello, World!");
    }
}
```

**Output**

Hello World!

---

## Basic Structure of a C# Program

As you can see from the example above, even a simple C# program requires several lines of code.

For future reference, remember that every C# program you write will generally follow this structure:

```
class Program
{
    public static void Main(string[] args)
    {
        // Your code goes here
    }
}
```

You will write your code inside the curly braces { } in place of // Your code goes here.

---

## Working of C# Program

Here's the first C# program we wrote:

```
public class Program
{
    public static void Main(string[] args)
    {
        System.Console.WriteLine("Hello, World!");
    }
}
```

Notice the following line of code:

```
System.Console.WriteLine("Hello, World!");
```

Keep these important things in mind about `System.Console.WriteLine()`:

- Everything you want to print should be placed inside the parentheses `()`.
- The text to be printed is enclosed within double quotes `""`.
- Each `System.Console.WriteLine()` statement ends with a semicolon `;`.
- Not adhering to these rules will lead to errors, and your code will not execute successfully.

Next, we will learn about [C# comments](https://dev.programiz.com/csharp-programming/comments).