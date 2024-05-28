# Rust Macro

A macro in Rust is a piece of code that generates another piece of code.

Macros generate code based on input, simplify repetitive patterns, and make code more concise.

Rust macro simply allows us to write code that writes more code which is also known as meta programming. Macros are used extensively in Rust.

Some of the popular Rust macros are `println!`, `vec!` and `panic!`.

---

## Creating a Macro in Rust

We can create a macro using the `macro_rules!` macro. It might be surprising but yes we use a macro to create a macro.

The `macro_rules!` macro has a special syntax.

```
macro_rules! macro_name {
    (...) => {...}
    // more match rules
}
```

Here, `() => {}` is the entry for a macro rule. We can have many rules to match for in a single macro.

Let's look at an example of a simple macro that defines a new function to print "Hello, World!".

```
// A simple macro named `hello_world`
macro_rules! hello_world {
    // `()` indicates that the macro takes no argument
    () => {
        // The macro will expand into the contents of this block
        println!("Hello, World!")
    };
}

fn main() {
    // Call the hello_world macro
    // This call will expand into `println!("Hello, World!");`
    hello_world!()
}
```

**Output**

Hello, World!

In this example, we create a macro named `hello_world`. The macro definition has one rule to match which is:

```
() => {
    println!("Hello, World!");
};
```

To call the macro we use the `hello_world!()` call in the `main()` function.

The macro will replace the `hello_world!()` call with the code defined in the macro definition i.e. `println!("Hello, World!)`.

---

## Creating a Macro with Arguments in Rust

Macros can also take arguments, which allows us to customize the code that it generates based on different inputs.

For example, here's a macro that defines a function to print a custom message:

```
// A macro named `print_message`
macro_rules! print_message {
    // Match rule that takes an argument expression
    ($message:expr) => {
        println!("{}", $message)
    };
}

fn main() {
    // Call the macro with an argument
    print_message!("I am learning Rust!");
}
```

**Output**

I am learning Rust!

Here, we create a macro called `print_message` which takes an argument `$message`. The argument(s) of a macro are prefixed by a dollar sign `$` and type annotated with a **designator**.

Rust will try to match the patterns defined within the match rules. In the above example our rule is:

```
($message:expr) => {
    println!("{}", $message)
};
```

The first part after the dollar sign `$` is the name of the variable. We capture it as a `$message`.

The part after the semicolon `:` is called a designator, which are types that we can choose to match for. We are using the expression designator (`expr`) in the example.

Now, when we call the macro `print_message!("I am learning Rust!")` it matches our input expression and captures the `$message` variable.

Here, `$message` is assigned to `"I am learning Rust!"` which is then passed into `println!("{}", $message)`.

It will generate code that is equivalent to writing `println!("{}", "I am learning Rust!")`. The `$message` argument allows us to specify the message to print.

**Note**: There are many designators that we can use inside a macro rule body:

- `stmt`: a statement
- `pat`: a pattern
- `expr`: an expression
- `ty`: a type
- `ident`: an identifier
- …

---

## Macro Repetitions in Rust

Rust macro is also useful when we need to generate repetitive code. We can define a macro to accept arguments and repeat the generated code based on those arguments.

The `macro_rules!` macro supports repetition using the `$(...)*` syntax. The `...` inside the parentheses can be any valid Rust expression or a pattern.

Here's an example that demonstrates macro repetition:

```
// A macro which uses repetitions
macro_rules! repeat_print {
    // match rule which matches multiple expressions in an argument
    ($($x:expr),*) => {
        $(
            println!("{}", $x);
        )*
    };
}

fn main() {
    // Call the macro with multiple arguments
    repeat_print!(1, 2, 3);
}
```

**Output**

1
2
3

Here, the macro `repeat_print` takes a single argument, `($($x:expr),*)`, which is a repeating pattern.

The pattern consists of zero or more expressions, separated by commas, that are matched by the macro. The star (`*`) symbol at the end will repeatedly match against the pattern inside `$()`.

![Breakdown of macro match rule in Rust](https://www.programiz.com/sites/tutorial2program/files/breakdown-of-macro-match-rule-in-rust.png "Breakdown of macro match rule in Rust")

Breakdown of macro match rule in Rust

The code inside the curly braces `println!("{}", $x);`, is repeated zero or more times, once for each expression in the list of arguments as it is wrapped around `$(...)*` in the body of the macro definition. The `$x` in the code refers to the matched expressions.

Each iteration of the generated code will print a different expression. Now, when we call `repeat_print!(1, 2, 3);` the macro will generate this code:

```
println!("{}", 1); // matches argument 1,
println!("{}", 2); // matches argument 2,
println!("{}", 3); // matches argument 3
```

Thus, this macro `repeat_print!` can print multiple expressions in a concise and convenient manner, without having to write out the `println!` macro every time.