# C# Preprocessor directives

As the name justifies, preprocessor directives are a block of statements that gets processed before the actual compilation starts. C# preprocessor directives are the commands for the compiler that affects the compilation process.

These commands specifies which sections of the code to compile or how to handle specific errors and warnings.

C# preprocessor directive begins with a `# (hash)` symbol and all preprocessor directives last for one line. Preprocessor directives are terminated by `new line` rather than `semicolon`.

The preprocessor directives available in C# are:

Preprocessor directives in C#
|Preprocessor Directive|Description|Syntax|
|---|---|---|
|`#if`|Checks if a preprocessor expression is true or not|#if preprocessor-expression<br>	code to compile<br>#endif|
|`#elif`|Used along with `#if` to check multiple preprocessor expressions|#if preprocessor-expression-1<br>	code to compile<br>#elif preprocessor-expression-2<br>	code to compile<br>#endif|
|`#else`|Used along with `#if` to create compound conditional directive.|#if preprocessor-expression<br>	code to compile<br>#elif<br>	code to compile<br>#endif|
|`#endif`|Used along with `#if` to indicate the end of a conditional directive|#if preprocessor-expression<br>	code to compile<br>#endif|
|`#define`|Used to define a symbol|#define SYMBOL|
|`#undef`|Used to undefine a symbol|#undef SYMBOL|
|`#warning`|Allows us to generate level 1 warning from our code|#warning warning-message|
|`#error`|Allows us to generate error from our code|#error error-message|
|`#line`|Allows us to modify the compiler's line number and filename to display errors and warnings|#line line-number file-name|
|`#region`|Allows us to create a region that can be expanded or collapsed when using a Visual Studio Code Editor|#region region-description<br>	codes<br>#endregion|
|`#endregion`|Indicates the end of a region|#region region-description<br>	codes<br>#endregion|
|`#pragma`|Gives the compiler special instructions for the compilation of the file in which it appears.|#pragma pragma-name pragma-arguments|

---

## #define directive

- The `#define` directive allows us to define a symbol.
- Symbols that are defined when used along with `#if` directive will evaluate to true.
- These symbols can be used to specify conditions for compilation.
- **Syntax:**
    
    #define SYMBOL
    
- **For example:**
    
    #define TESTING
    
    Here, TESTING is a symbol.

---

## #undef directive

- The `#undef` directive allows us to undefine a symbol.
- Undefined symbols when used along with `#if` directive will evaluate to false.
- **Syntax:**
    
    #undef SYMBOL
    
- For example:
    
    #undef TESTING
    
    Here, TESTING is a symbol.

---

## #if directive

- The `#if` directive are used to test the preprocessor expression.
- A preprocessor expression may consists of a symbol only or combination of symbols along with operators like `&&` (AND), `||` (OR), `!` (NOT).
- `#if` directive is followed by an `#endif` directive.
- The codes inside the `#if` directive is compiled only if the expression tested with `#if` evaluates to true.
- **Syntax:**
    
    #if preprocessor-expression
    	code to compile<
    #endif
    
- **For example:**
    
    #if TESTING
    	Console.WriteLine("Currently Testing");
    #endif
    

### Example 1: How to use #if directive?

```
#define CSHARP

using System;
 
namespace Directive
{
	class ConditionalDirective
	{
		public static void Main(string[] args)
		{
			#if (CSHARP)
				Console.WriteLine("CSHARP is defined");
			#endif
		}
	}
}
```

When we run the program, the output will be:

CSHARP is defined

In the above program, `CSHARP` symbol is defined using the `#define` directive at the beginning of program. Inside the `Main()` method, `#if` directive is used to test whether `CSHARP` is true or not. The block of code inside `#if` directive is compiled only if `CSHARP` is defined.

---

## #elif directive

- The `#elif` directive is used along with #if directive that lets us create a compound conditional directive.
- It is used when testing multiple preprocessor expression.
- The codes inside the `#elif` directive is compiled only if the expression tested with that `#elif` evaluates to true.
- **Syntax:**
    
    #if preprocessor-expression-1
    	code to compile
    #elif preprocessor-expression-2
    	code-to-compile
    #endif
    
- **For example:**
    
    #if TESTING
    	Console.WriteLine("Currently Testing");
    #elif TRAINING
    	Console.WriteLine("Currently Training");
    #endif
    

---

## #else directive

- The `#else` directive is used along with `#if` directive.
- If none of the expression in the preceding `#if` and `#elif` (if present) directives are true, the codes inside the `#else` directive will be compiled.
- **Syntax:**
    
    #if preprocessor-expression-1
    	code to compile
    #elif preprocessor-expression-2
    	code-to-compile
    #else
    	code-to-compile
    #endif
    
- **For example:**
    
    #if TESTING
    	Console.WriteLine("Currently Testing");
    #elif TRAINING
    	Console.WriteLine("Currently Training");
    #else
    	Console.WriteLine("Neither Testing nor Training");
    #endif
    

---

## #endif directive

- The `#endif` directive is used along with `#if` directive to indicate the end of `#if` directive.
- **Syntax:**
    
    #if preprocessor-expression-1
    	code to compile
    #endif
    
- **For example:**
    
    #if TESTING
    	Console.WriteLine("Currently Testing");
    #endif
    

### Example 2: How to use conditional directive (if, elif, else, endif) ?

```
#define CSHARP
#undef PYTHON
 
using System;
 
namespace Directive
{
	class ConditionalDirective
	{
		static void Main(string[] args)
		{
			#if (CSHARP && PYTHON)
				Console.WriteLine("CSHARP and PYTHON are defined");
			#elif (CSHARP && !PYTHON)
				Console.WriteLine("CSHARP is defined, PYTHON is undefined");
			#elif (!CSHARP && PYTHON)
				Console.WriteLine("PYTHON is defined, CSHARP is undefined");
			#else
				Console.WriteLine("CSHARP and PYTHON are undefined");
			#endif
		}
	}
}
```

When we run the program, the output will be:

CSHARP is defined, PYTHON is undefined

In this example, we can see the use of `#elif` and `#else` directive. These directive are used when there are multiple conditions to be tested. Also, symbols can be combined using logical operators to form a preprocessor expression.

---

## #warning directive

- The `#warning` directive allows us to generate a user-defined level one warning from our code.
- **Syntax:**
    
    #warning warning-message
    
- **For example:**
    
    #warning This is a warning message
    

---

### Example 3: How to use #warning directive?

```
using System;
 
namespace Directives
{
	class WarningDirective
	{
		public static void Main(string[] args)
		{
			#if (!CSHARP)
				#warning CSHARP is undefined
			#endif
			Console.WriteLine("#warning directive example");
		}
	}
}
```

When we run the program, the output will be:

Program.cs(10,26): warning CS1030: #warning: 'CSHARP is undefined' [/home/myuser/csharp/directives-project/directives-project.csproj]
#warning directive example

After running the above program, we will see the output as above. The text represents a warning message. Here, we are generating a user-defined warning message using the `#warning` directive.

Note that the statements after the `#warning` directive are also executed. It means that the `#warning` directive does not terminate the program but just throws a warning.

---

## #error directive

- The `#error` directive allows us to generate a user-defined error from our code.
- **Syntax:**
    
    #error error-message
    
- **For example:**
    
    #error This is an error message
    

### Example 4: How to use #error directive?

```
using System;
 
namespace Directive
{
	class Error
	{
		public static void Main(string[] args)
		{
			#if (!CSHARP)
				#error CSHARP is undefined
			#endif
			Console.WriteLine("#error directive example");
		}
	}
}
```

When we run the program, the output will be:

Program.cs(10,24): error CS1029: #error: 'CSHARP is undefined' [/home/myuser/csharp/directives-project/directives-project.csproj]
The build failed. Please fix the build errors and run again.

We will see some errors, probably like above. Here we are generating a user-defined error.

Another thing to note here is the program will be terminated and the line `#error directive example` won't be printed as it was in the `#warning` directive.

---

## #line directive

- The `#line` directive allows us to modify the line number and the filename for errors and warnings.
- **Syntax:**
    
    #line line-number file-name
    
- **For example:**
    
    #line 50 "fakeprogram.cs"
    

### Example 5: How to use #line directive?

```
using System;
 
namespace Directive
{
	class Error
	{
		public static void Main(string[] args)
		{
			#line 200 "AnotherProgram.cs"
			#warning Actual Warning generated by Program.cs on line 10
		}
	}
}
```

When we run the program, the output will be:

AnotherProgram.cs(200,22): warning CS1030: #warning: 'Actual Warning generated by Program.cs on line 10' [/home/myuser/csh
arp/directive-project/directive-project.csproj]

We have saved the above example as `Program.cs`. The warning was actually generated at `line 10` by `Program.cs`. Using the `#line` directive, we have changed the line number to `200` and the filename to `AnotherProgram.cs` that generated the error.

---

## #region and #endregion directive

- The `#region` directive allows us to create a region that can be expanded or collapsed when using a Visual Studio Code Editor.
- This directive is simply used to organize the code.
- The #region block can not overlap with a `#if` block. However, a `#region` block can be included within a `#if` block and a `#if` block can overlap with a `#region` block.
- `#endregion` directive indicates the end of a `#region` block.
- **Syntax:**
    
    #region region-description
    	codes
    #endregion
    

### Example 6: How to use #region directive?

```
using System;
 
namespace Directive
{
	class Region
	{
		public static void Main(string[] args)
		{
			#region Hello
			Console.WriteLine("Hello");
			Console.WriteLine("Hello");
			Console.WriteLine("Hello");
			Console.WriteLine("Hello");
			Console.WriteLine("Hello");
			#endregion
		}
	}
}
```

When we run the program, the output will be:

Hello
Hello
Hello
Hello
Hello

---

## #pragma directive

- The `#pragma` directive is used to give the compiler some special instructions for the compilation of the file in which it appears.
- The instruction may include disabling or enabling some warnings.
- C# supports two `#pragma` instructions:
    - `#pragma warning`: Used for disabling or enabling warnings
    - `#pragma checksum`: It generates checksums for source files which will be used for debugging.
- **Syntax:**
    
    #pragma pragma-name pragma-arguments
    
- **For example:**
    
    #pragma warning disable
    

### Example 7: How to use #pragma directive?

```
using System;
 
namespace Directive
{
	class Error
	{
		public static void Main(string[] args)
		{
			#pragma warning disable
			#warning This is a warning 1
			#pragma warning restore
			#warning This is a warning 2
		}
	}
}
```

When we run the program, the output will be:

Program.cs(12,22): warning CS1030: #warning: 'This is a warning 2' [/home/myuser/csharp/directive-project/directive-project.csproj]

We can see that only the **second warning** is displayed on the output screen.

This is because, we initially disabled all warnings before the first warning and restored them only before the second warning. This is the reason why the first warning was hidden.

We can also disable specific warning instead of all warning.

To learn more about `#pragma`, visit [#pragma (C# reference)](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/preprocessor-directives/preprocessor-pragma "#pragma reference C#").