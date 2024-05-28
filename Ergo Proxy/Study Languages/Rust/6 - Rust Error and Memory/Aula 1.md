# Rust Error Handling

An error is an unexpected behavior or event in a program that will produce an unwanted output.

In Rust, errors are of two categories:

- Unrecoverable Errors
- Recoverable Errors

---

## Unrecoverable Errors in Rust

Unrecoverable errors are errors from which a program stops its execution. As the name suggests, we cannot recover from unrecoverable errors.

These errors are known as **panic** and can be triggered explicitly by calling the `panic!` macro.

Let's look at an example that uses the `panic!` macro.

### Example 1: Rust Unrecoverable Errors with panic! Macro

```
fn main() {
    println!("Hello, World!");

    // Explicitly exit the program with an unrecoverable error
    panic!("Crash");
}
```

**Output**

Hello, World!
thread 'main' panicked at 'Crash', src/main.rs:5:5

Here, the call to the `panic!` macro causes an unrecoverable error.

`thread 'main' panicked at 'Crash', src/main.rs:5:5`

Notice that the program still runs the expressions above `panic!` macro. We can still see `Hello, World!` printed to the screen before the error message.

The `panic!` macro takes in an error message as an argument.

---

### Example 2: Rust Unrecoverable Errors

Unrecoverable errors are also triggered by taking an action that might cause our code to panic. For example, accessing an array past its index will cause a panic.

```
fn main() {
    let numbers = [1, 2 ,3];

    println!("unknown index value = {}", numbers[3]);
}
```

**Error**

error: this operation will panic at runtime
 --> src/main.rs:4:42
  |
4 |     println!("unknown index value = {}", numbers[3]);
  |                                          ^^^^^^^^^^ index out of bounds: the length is 3 but the index is 3
  |

Here, Rust stops us from compiling the program because it knows the operation will panic at runtime.

The array numbers does not have a value at index **3** i.e. `numbers[3]`.

---

## Recoverable Errors

Recoverable errors are errors that won't stop a program from executing. Most errors are recoverable, and we can easily take action based on the type of error.

For example, if you try to open a file that doesn't exist, you can create the file instead of stopping the execution of the program or exiting the program with a panic.

Let's look at an example.

```
use std::fs::File;

fn main() {
    let data_result = File::open("data.txt");

    // using match for Result type
    let data_file = match data_result {
        Ok(file) => file,
        Err(error) => panic!("Problem opening the data file: {:?}", error),
    };

    println!("Data file", data_file);
}
```

If the `data.txt` file exists, the **output** is:

Data file: File { fd: 3, path: "/playground/data.txt", read: true, write: false }

If the `data.txt` file doesn't exist, the **output** is:

thread 'main' panicked at 'Problem opening the data file: Os { code: 2, kind: NotFound, message: "No such file or directory" }', src/main.rs:8:23

---

## The Result Enum

In the above example, the return type of the `File::open('data.txt')` is a `Result<T, E>`.

The `Result<T, E>` type returns either a value or an error in Rust. It is an `enum` type with two possible variants.

- `Ok(T)` → operation succeeded with value `T`
- `Err(E)` → operation failed with an error `E`

Here, `T` and `E` are generic types. To know more about generics or generic types, visit [_Rust Generics_](https://www.programiz.com/rust/generics).

The most basic way to see whether a `Result` enum has a value or error is to use pattern matching with a `match` expression.

```
// data_file is a Result<T, E>
match data_result {
    Ok(file) => file,
    Err(error) => panic!("Problem opening the data file: {:?}", error),
 };
```

When the result is `Ok`, this code will return the `file`, and when the result is `Err`, it will return a `panic!`.

To learn more about pattern matching, visit [_Rust Pattern Matching_](https://www.programiz.com/rust/pattern-matching).

---

## The Option Enum

The `Option` type or `Option<T>` type is an `enum` type just like `Result` with two possible variants.

- `None` → to indicate failure with no value
- `Some(T)` → a value with type `T`

Let's look at an example,

```
fn main() {
    let text = "Hello, World!";
    
    let character_option = text.chars().nth(15);
    
    // using match for Option type
    let character = match character_option {
        None => "empty".to_string(),
        Some(c) => c.to_string()
    };
    
    println!("Character at index 15 is {}", character);
}
```

**Output**

Character at index 15 is empty

Here, the method `text.chars().nth(15)` returns an `Option<String>`. So, to get the value out of the `Option`, we use a `match` expression.

In the example above, the 15th index of the string text doesn't exist. Thus, the `Option` type returns a `None` which matches the `"empty"` string.

None => "empty".to_string() 

If we were to get the 11th index of the string text, the `Option` enum would return `Some(c)`, where `c` is the character in the 11th index.

Let's update the above example to find out the 11th index in the string.

```
fn main() {
    let text = "Hello, World!";
    
    let character_option = text.chars().nth(11);
    
    // using match for Option type
    let character = match character_option {
        None => "empty".to_string(),
        Some(c) => c.to_string()
    };
    
    println!("Character at index 11 is {}", character);
}
```

**Output**

Character at index 11 is d

---

## Difference between Result and Option enum in Rust

`Option` enum can return `None`, which can indicate failure.

However, sometimes it is essential to express why an operation failed. Thus, we have the `Result` enum, which gives us the `Err` with the reason behind the failure of the operation.

In short,

- `Option` is about `Some` or `None` (value or no value)
- `Result` is about `Ok` or `Err` (result or error result)