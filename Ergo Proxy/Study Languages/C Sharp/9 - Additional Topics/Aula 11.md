# C# yield keyword

The `yield` keyword performs custom iteration over a collection like list, array, etc.

---

## Two Forms of yield Keyword

The `yield` keyword is used in two forms:

- `yield return` - returns an expression at each iteration
- `yield break` - terminates the iteration

---

## yield return in an Iterator

The `yield` keyword is used in an iterator as:

```
yield return <expression>; 
```

We use `yield return` inside an iterator as:

```
using System;
using System.Collections.Generic;
class Program
{
    // define an iterator method
    static IEnumerable<int> getNumber()
    {
        // create a list of integers 
        List<int> myList = new List<int> { -1, -4, 3, 5 };

        foreach (var num in myList)
        {
            // returns positive number from myList 
            if (num >= 0)
            {
                yield return num;

                // location of the code is preserved 
                // so on the next iteration getNumber() is executed from here 
                Console.WriteLine("....");
            }
        }
    }
    static void Main()
    {
        // display return values of getNumber() 
        foreach (var items in getNumber())
        {
            Console.WriteLine(items);
        }
    }
}
```

**Output**

3
....
5
....

In the above example, we have created an iterator method `getNumber()` inside which we have used `yield return`.

Here, when `getNumber()` is called from `foreach` of `Main()`, the code inside `getNumber()` is executed until it reaches `yield return`.

When it reaches `yield return`, the current location of the code is preserved and the control goes back to the caller(i.e. `foreach` loop) and **3** is printed.

In the next iteration of `foreach`, the `getNumber()` method is called again. This time, `getNumber()` is executed from the preserved location of the code. This means,

```
Console.WriteLine("....");
```

gets executed and `getNumber()` resumes until it encounters another `yield return` and the same process continues till iterating over `myList` is completed.

Let's discuss the working of the above program with the help of an image.

---

## Working of yield return

![yield return is returning values to the iterator method](https://www.programiz.com/sites/tutorial2program/files/csharp-yield-keyword.png "Working of yield return")

Working of yield return

1. `foreach` calls `getNumber()` - At first, the code inside the `Main()` function gets executed. Inside `Main()`, we have created a `foreach` loop that calls `getNumber()` method.

2. Inside `getNumber()`, `myList` is created.

3. Then, the `foreach` loop inside `getNumber()` starts iterating over `myList`. Notice the code,

```
if (num >= 0)
{
    yield return num;

    // location of the code is preserved 
    // so on the next iteration getNumber() is executed from here 
    Console.WriteLine("....");
}
```

When `num` = **3**, `num >= 0` returns `True` and `yield return` is encountered. Two operations occur:

- pauses `getNumber()` and preserves the current location of the code
- control goes back to the `foreach` loop (caller)

4. Control goes back to the caller - Here, the returned value **3** is printed and the next iteration of `foreach` begins.

In the next iteration, the `getNumber()` method is called again. In this call, `getNumber()` is resumed from the preserved location.

This means `Console.WriteLine("....");` gets executed.

Now, in `if` block, `num = 5` so `num >= 0` is `True`. And again we encounter `yield return`.

5. Again, control goes back to the caller (inside `foreach`). Here, **5** is printed and `foreach` calls `getNumber()` in the next iteration.

The method resumes from the preserved location and prints `....`. Since there are no other elements left in `myList`, iteration is stopped.

---

## Frequently Asked Question

Why use yield keyword?

---

## yield break

The `yield break` ends an iterator ( list, array, etc) block. Let's take an example to understand it clearly.

```
using System;
using System.Collections.Generic;
class Program
{
    // define an iterator method
    static IEnumerable<string> getString()
    {
        // create a list of strings 
        List<string> myList = new List<string> { "Sun", "Mon", "Tue" };

        foreach (var day in myList)
        {
            if (day == "Mon")
            {
                // terminates the iterator block after encountering "Mon"
                yield break;
            }

            yield return day;
        }
    }
    static void Main()
    {
        // display return values of getString() 
        foreach (var items in getString())
        {
            Console.WriteLine(items);
        }
    }
}
```

**Output**

Sun

Here inside the getString() method, notice

```
foreach (var day in myList)
{
    if (day == "Mon")
    {
        // terminates the iterator block after encountering "Mon"
        yield break;
    }
    yield return day;
}
```

Here,

- `"Sun"=="Mon"` is `False` so `if` block is not executed. Hence, the program executes `yield return day` and returns `"Sun"` to `getString()`.
- `"Mon" == "Mon` is `True` so `if` block is executed. Here, `yield break` is encountered and it ends the iterator block returning nothing.

Basically, if `yield break` is encountered, it indicates there are no more elements left in the collection.

**Note:** The `yield break` is different from `break` statement because `break` statement terminates the closest loop in normal method and `yield break` terminates the iterator method and transfers the control of the program to the caller.

`yield break` works just like `return` statement that returns nothing.

- [](https://www.programiz.com/csharp-programming/yield-keyword#introduction)
- [](https://www.programiz.com/csharp-programming/yield-keyword#two-forms-of-yield-keyword)
- [](https://www.programiz.com/csharp-programming/yield-keyword#yield-return)
- [](https://www.programiz.com/csharp-programming/yield-keyword#working-of-yield-return)
- [](https://www.programiz.com/csharp-programming/yield-keyword#yield-break)

[

  


](https://www.programiz.com/csharp-programming/nullable-types "C# Nullable Types")