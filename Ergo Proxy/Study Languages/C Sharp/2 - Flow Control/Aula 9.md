# C# goto

In C#, the `goto` statement transfers control to some other part of the program. For example,

```
goto label;
... 
...
label:
  ...
  ...
```

Here, `label` is an identifier. When `goto label;` is encountered, the control of the program is transferred to `label:`. Then the code below `label:` is executed.

![Working of goto in C#](https://www.programiz.com/sites/tutorial2program/files/csharp-goto.png "Working of goto in C#")

Working of goto in C#

---

### Example: C# goto

```
using System;

namespace CSharpGoto {

  class Program {
    public static void Main(string[] args) {
      
      // label
      repeat: 
        Console.WriteLine("Enter a number less than 10");
        int num = Convert.ToInt32(Console.ReadLine());  

        if(num >= 10) {
          // transfers control to repeat
          goto repeat;
        }

        Console.WriteLine(num + " is less than 10");
        Console.ReadLine();
    }
  }
}
```

**Output**

Enter a number less than 10
99
Enter a number less than 10
9
9 is less than 10

In the above program, we have a `goto` statement inside the `if` statement.

If the entered number is not less than **10**, `goto repeat:` transfers the control of the code to `repeat:`. Then, the code below `repeat:` is executed.

The control of code will be transferred to the `repeat:` label unless the entered number is less than 10.

---

## C# goto with switch statement

In C#, we can use `goto` with a [switch](https://www.programiz.com/csharp-programming/switch-statement) statement to transfer control of a program to a specific case. For example,

```
using System;

namespace CSharpGoto {

  class Program {

    public static void Main(string[] args) {

      Console.Write("Choose your coffee? milk or black: ");
      string coffeeType = Console.ReadLine();

      switch (coffeeType) {
        case "milk":
          Console.WriteLine("Can I have a milk coffee?");
          break;

        case "black":
          Console.WriteLine("Can I have a black coffee?");
          // transfer code to case "milk" 
          goto case "milk";
     
        default:
          Console.WriteLine("Not available.");
            break;
        }
      Console.ReadLine();
    }
  }
}
```

**Output**

Can I have a black coffee?
Can I have a milk coffee?

In the above program, we have used the `goto` statement with a `switch` statement.

We have entered `"black"` as the coffeeType. Now the `case "black"` is executed.

Inside the case, we have used `goto case "milk";` which will transfer the control of the program to the `case "milk"`.

Hence, both cases are executed.

---

## goto with for Loop

In C#, we can use `goto` to break out of a `for` loop. For example,

```
using System;

namespace CSharpGoto {

  class Program {

    static void Main() {
    for(int i = 0; i <= 10; i++) {

      if(i == 5) {
        // transfers control to End label
        goto End;
      }

      Console.WriteLine(i);
    }

    // End label
    End:
      Console.WriteLine("Loop End");
      Console.ReadLine();
    }
  }
}
```

**Output**

0
1
2
3
4
Loop End

In the above program, we have created a `for` loop. It iterates from **0** to **100**.

Whenever the value of i equals **5**, the `goto` statement transfers the control of code to the `End` label. Hence, the program breaks out of the `for` loop.