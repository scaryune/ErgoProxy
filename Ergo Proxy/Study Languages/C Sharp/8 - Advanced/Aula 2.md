# C# Lambda Expression

C# Lambda Expression is a short block of code that accepts parameters and returns a value. It is defined as an anonymous function (function without a name). For example,

```
num => num * 7
```

Here, `num` is an input parameter and `num * 7` is a return value. The lambda expression does not execute on its own. Instead, we use it inside other methods or variables.

Let's learn about lambda expressions in detail below.

---

## How to Define a Lambda Expression

We can define lambda expression in C# as,

```
(parameterList) => lambda body
```

Here,

- `parameterList` - list of input parameters
- `=>` - a lambda operator
- `lambda body` - can be an expression or statement

Based on lambda body, the C# lambda expression is divided into two types.

---

## Types of Lambda Expression

The two types of lambda expressions are:

1. Expression Lambda
2. Statement Lambda

**1. Expression Lambda:** Expression lambda contains a single expression in the lambda body. For example,

```
(int num) => num * 5;
```

The above expression lambda contains a single expression `num * 5` in the lambda body. It takes an `int` input, multiplies it by **5**, and returns the output.

**2. Statement Lambda:** Statement lambda encloses one or more statements in the lambda body. We use curly braces `{}` to wrap the statements. For example,

```
(int a, int b) =>
{
    var sum = a + b;
    return sum;
};
```

The above expression is a statement lambda which contains two statements in the lambda body. This takes two `int` inputs and returns its sum.

Let's see examples to get a clear understanding of C# lambda.

---

## Example: C# Expression Lambda

```
using System;
class Program
{
    static void Main()
    {
        // expression lambda that returns the square of a number 
        var square = (int num) => num * num;

        // passing input to the expression lambda 
        Console.WriteLine("Square of number: " + square(5));
    }
}
```

**Output**

Square of number: 25

In the above example, the expression lambda is

```
(int num) => num * num;
```

Here, the expression lambda returns the square of `num`. We have then assigned the expression lambda to the `square` variable.

So, when we pass **5** as an input in `square`, we get **25** as an output.

---

## Example: C# Statement Lambda

```
using System;
class Program
{
    static void Main()
    {
        // statement lambda that takes two int inputs and returns the sum 
        var resultingSum = (int a, int b) =>
        {
            int calculatedSum = a + b;
            return calculatedSum;
        };

        // find the sum of 5 and 6
        Console.WriteLine("Total sum: " + resultingSum(5, 6));
    }
}
```

**Output**

Total sum: 11

In the above example, we have used the statement lambda as,

```
(int a, int b) =>
{
    int calculatedSum = a + b;
    return calculatedSum;
}
```

Here, the statement lambda takes two integer parameters - `a` and `b`. On the right side of the lambda operator `=>` we have enclosed two statements that:

- calculate the sum of `a` and `b`
- return the sum

---

## Lambda Expression with Delegate

In C#, we can assign lambda expressions to the delegate types like `Func`. For example,

```
using System;
class Program
{
    static void Main()
    {
        // using lambda expression with delegate type 
        // take an int input, multiply it with 3 and return the result 
        Func<int, int> multiply = num => num * 3;

        // calls multiply() by passing 5 as an input
        Console.WriteLine(multiply(5));
    }
}
```

**Output**

15

In the above example, we have assigned lambda expression `num => num * 3;` to the `Func` delegate `multiply`.

Here, the lambda expression takes an `int` type input `num`, multiplies it with **3** and returns the result to `multiply()`.

Hence, when we pass **5** in `multiply()`, it returns **15**.

**Note:** The `Func<>` delegate type takes **0** or more input values and returns an output value. For example, `Func<int,int,string>` takes two `int` inputs and returns a `string` output. To learn more about delegates, visit [C# delegates](https://www.programiz.com/csharp-programming/delegates).

---

## Use of Lambda Expression

Some of the uses of the lambda expression are:

### 1. Writing Easy and Simple Delegate Code

Using lambda expressions, we can write much easier and simpler code. Let's see programs with and without using a lambda expression in a delegate.

**Program Without Using Lambda Expression**

```
using System;
class Program
{
    static void Main()
    {
        // method that returns square of a number
        int Square(int num)
        {
            return num * num;
        }

        // delegate that points the Square() method 
        Func<int, int> square = Square;

        // calling square() delegate 
        Console.WriteLine(square(7));
    }
}
```

**Output**

49

In the above program, we have defined a delegate `square` of `Func` type that points to the `Square()` method.

**Program With Using Lambda Expression**

```
using System;
class Program
{
    static void Main()
    {
        // delegate using lambda expression 
        Func<int, int> square = num => num * num;

        // calling square() delegate 
        Console.WriteLine(square(7));
    }
}
```

**Output**

49

Here, we don't need to define a separate method. We have replaced the pointer to the `square()` method with the lambda expression.

### 2. Passing Parameter in Method

We can pass a lambda expression as a parameter in a method call.

Let's take a built-in `Count()` method of C# array and pass a lambda expression as its parameter.

```
using System;
class Program
{
    static void Main()
    {
        // array containing integer values 
        int[] numbers = { 2, 13, 1, 4, 13, 5 };

        // lambda expression as method parameter
        // returns the total count of 13 in the numbers array
        int totalCount = numbers.Count(x => x == 13);

        Console.WriteLine("Total number of 13: " + totalCount);
    }
}
```

**Output**

Total number of 13: 2

In the above example, we have passed the lambda expression `x => x == 13` as a method parameter.

The `Count()` method checks each element of the numbers array and counts the total number of **13** in the array.

- [](https://www.programiz.com/csharp-programming/lambda-expression#introduction)
- [](https://www.programiz.com/csharp-programming/lambda-expression#define-a-lambda-expression)
- [](https://www.programiz.com/csharp-programming/lambda-expression#types-of-lambda-expression)
- [](https://www.programiz.com/csharp-programming/lambda-expression#expression-lambda)
- [](https://www.programiz.com/csharp-programming/lambda-expression#statement-lambda)
- [](https://www.programiz.com/csharp-programming/lambda-expression#lambda-expression-with-delegate)
- [](https://www.programiz.com/csharp-programming/lambda-expression#use-of-lambda-expression)