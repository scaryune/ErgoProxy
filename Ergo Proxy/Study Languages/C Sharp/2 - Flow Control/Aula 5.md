# Nested Loops in C#: for, while, do-while

A loop within another loop is called nested loop. This is how a nested loop looks like:

Outer-Loop 
{
	// body of outer-loop
	Inner-Loop
	{
		// body of inner-loop
	}
... ... ...
}

As you can see, the **outer loop** encloses the **inner loop**. The inner loop is a part of the outer loop and must start and finish within the body of outer loop.

On each iteration of outer loop, the inner loop is executed completely.

---

## Nested for loop

A for loop inside another for loop is called nested for loop.

For example:

for (int i=0; i<5; i++)
{
	// body of outer for loop
	for (int j=0; j<5; j++)
	{
		// body of inner for loop
	}
	// body of outer for loop
}

### Example 1: Nested for Loop

```
using System;

namespace Loop
{
	class NestedForLoop
	{
		public static void Main(string[] args)
		{
			int outerLoop = 0, innerLoop = 0;
			for (int i=1; i<=5; i++)
			{
				outerLoop ++;
				for (int j=1; j<=5; j++)
				{
					innerLoop++;
				}
			}
			Console.WriteLine("Outer Loop runs {0} times", outerLoop);
			Console.WriteLine("Inner Loop runs {0} times", innerLoop);
		}
	}
}
```

When we run the program, the output will be:

Outer Loop runs 5 times
Inner Loop runs 25 times

In this program, the outer loop runs for 5 times. Each time the outer loop runs, the inner loop runs for 5 times making it run 25 times altogether.

### Example 2: Nested for Loop to Print Pattern

```
using System;

namespace Loop
{
	class NestedForLoop
	{
		public static void Main(string[] args)
		{
			for (int i=1; i<=5; i++)
			{
				for (int j=1; j<=i; j++)
				{
					Console.Write(j + " ");
				}
				Console.WriteLine();
			}
		}
	}
}
```

When we run the program, the output will be:

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

---

## Nested while loop

A while loop inside another while loop is called nested while loop.

For example:

while (condition-1)
{
	// body of outer while loop
	while (condition-2)
	{
		// body of inner while loop
	}
	// body of outer while loop
}

### Example 3: Nested while Loop

```
using System;

namespace Loop
{
	class NestedWhileLoop
	{
		public static void Main(string[] args)
		{
			int i=0;
			while (i<2)
			{
				int j=0;
				while (j<2)
				{
					Console.Write("({0},{1}) ", i,j);
					j++;
				}
				i++;
				Console.WriteLine();
			}
		}
	}
}
```

When we run the program, the output will be:

(0,0) (0,1)
(1,0) (1,1)

---

## Nested do-while loop

A do-while loop inside another do-while loop is called nested do-while loop.

For example:

do
{
	// body of outer while loop
	do
	{
		// body of inner while loop
	} while (condition-2);
	// body of outer while loop
} while (condition-1);

### Example 4: Nested do-while Loop

```
using System;

namespace Loop
{
	class NestedWhileLoop
	{
		public static void Main(string[] args)
		{
			int i=0;
			do
			{
				int j=0;
				do
				{
					Console.Write("({0},{1}) ", i,j);
					j++;
				} while (j<2);
				i++;
				Console.WriteLine();

			} while (i<2);
		}
	}
}
```

When we run the program, the output will be:

(0,0) (0,1)
(1,0) (1,1)

---

## Different inner and outer nested loops

It is not mandatory to nest same type of loop. We can put a for loop inside a while loop or a do-while loop inside a for loop.

### Example 5: C# Nested Loop: Different inner and outer loops

```
using System;

namespace Loop
{
	class NestedLoop
	{
		public static void Main(string[] args)
		{
			int i=1;
			while (i<=5)
			{
				for (int j=1; j<=i; j++)
				{
					Console.Write(i + " ");
				}

				Console.WriteLine();
				i++;
			}
		}
	}
}
```

When we run the program, the output will be:

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

In the above program, a for loop is placed within a while loop. We can use different types of loop inside a loop.

- [](https://www.programiz.com/csharp-programming/nested-loops#introduction)
- [](https://www.programiz.com/csharp-programming/nested-loops#nested-for)
    - [](https://www.programiz.com/csharp-programming/nested-loops#example-for)
    - [](https://www.programiz.com/csharp-programming/nested-loops#example-nested-for-print-pattern)
- [](https://www.programiz.com/csharp-programming/nested-loops#nested-while)
    - [](https://www.programiz.com/csharp-programming/nested-loops#example-while)
- [](https://www.programiz.com/csharp-programming/nested-loops#nested-do-while)
    - [](https://www.programiz.com/csharp-programming/nested-loops#example-do-while)
- [](https://www.programiz.com/csharp-programming/nested-loops#different-nested)
    - [](https://www.programiz.com/csharp-programming/nested-loops#example-different-nested)

[

  


](https://www.programiz.com/csharp-programming/do-while-loop "C# while and do...while loop")