# Rust Pattern Matching

Pattern matching is a way to match the structure of a value and bind variables to its parts. It is a powerful way to handle data and control flow of a Rust program.

We generally use the `match` expressions when it comes to pattern matching.

The syntax of the `match` expressions is:

```
match VALUE {
    PATTERN => EXPRESSION,
    PATTERN => EXPRESSION,
    PATTERN => EXPRESSION,
}
```

Here, `PATTERN => EXPRESSION` are called patterns, a special syntax in Rust which usually works together with the `match` keyword.

---

## Matching a Variable in Rust

We can pattern match against the value of a variable. This is useful if our code wants to take some action based on a particular value. For example,

```
fn main() {
    let x = 2;

    // use of match expression to pattern match against variable x
    match x {
        1 => println!("x is 1"),
        2 => println!("x is 2"),
        _ => println!("x is something else"),
    }
}
```

**Output**

x is 2

Here, we have used the `match` expression to match against x. In the `match` body, we pattern matched with values `1`, `2` and `_`.

```
1 => println!("x is 1"),
2 => println!("x is 2"),
_ => println!("x is something else"),
```

Because the value of x is `2`, the pattern that matches is:

```
2 => println!("x is 2")
```

Thus, x is 2 is printed on the screen.

Notice that we also match against underscore `_`. The `_` has a special meaning in pattern matching, if all the other patterns do not match, it defaults to `_`.

**Note**: `match` body (also known as match arms) should always ensure that all possible cases are being handled. If all possible cases are not handled, the Rust program fails to compile.

---

## Matching an Enum In Rust

Pattern matching is extensively used to match enum variants. For example,

```
fn main() {
    enum Color {
        Red,
        Green,
        Blue,
    }

    let my_color = Color::Green;

    // use of match expression to match against an enum variant
    match my_color {
        Color::Red => println!("The color is red"),
        Color::Green => println!("The color is green"),
        Color::Blue => println!("The color is blue"),
    }
}
```

**Output**

The color is green

Here, we created a pattern in the `match` expression to match against all enum variants.

```
Color::Red => println!("The color is red"),
Color::Green => println!("The color is green"),
Color::Blue => println!("The color is blue"),
```

Because the value of `my_color` is `Color::Green`, the pattern that it matches is:

```
Color::Green => println!("The color is green"),
```

Thus, `The color is green` is printed on the screen.

---

## Matching Option and Result Type in Rust

The most common case for pattern matching is with `Option` and `Result` enum types. Both the `Option` and `Result` type have two variants.

`Option` type has:

- `None` → to indicate failure with no value
- `Some(T)` → a value with type T

`Result` type has:

- `Ok(T)` → operation succeeded with value T
- `Err(E)` → operation failed with an error E

Let's look at examples of how we can use pattern matching on these types.

---

### Example: Matching Option Type in Rust

```
fn main() {
    let my_option: Option<i32> = Some(222);
    
    // use of match expression to match Option type
    match my_option {
        Some(value) => println!("The option has a value of {}", value),
        None => println!("The option has no value"),
    }
}
```

**Output**

The option has a value of 222

In this example, `my_option` is an `Option` type that contains either a `Some` variant with an `i32` value or a `None` variant.

The `match` expression compares the value of `my_option` to the `Some` and `None` variants, and binds the value of `Some` variant to the `value` variable.

When a match is found, the corresponding code block is executed.

```
Some(value) => println!("The option has a value of {}", value),
```

Thus, `The option has a value of 222` is printed on the screen.

---

### Example: Matching Result Type in Rust

```
fn main() {
    let my_result: Result<i32, &str> = Ok(100);

    // use of match expression to match Result type
    match my_result {
        Ok(value) => println!("The result is {}", value),
        Err(error) => println!("The error message is {}", error),
    }
}
```

**Output**

The result is 100

In this example, `my_result` is a `Result` type that contains either an `Ok` variant with an `i32` value, or an `Err` variant with an error message of type `&str`.

The match expression compares the value of `my_result` to the `Ok` and `Err` variants, and binds the value of `Ok` variant to the `value` variable or the `Err` variant to the `error` variable.

```
Ok(value) => println!("The result is {}", value),
Err(error) => println!("The error message is {}", error),
```

When a match is found, the corresponding code block is executed.

```
Ok(value) => println!("The result is {}", value),
```

Thus, `The result is 100` is printed on the screen.

---

## if let Expression in Rust

The `if let` expression in Rust is a shorthand for a `match` expression with only one pattern/arm to match.

It allows us to match on a value and then execute code only if the match is successful.

```
fn main() {
    let my_option: Option<i32> = Some(222);

    // use of if let expression on the Option type
    if let Some(value) = my_option {
        println!("The option has a value of {}", value);
    } else {
        println!("The option has no value");
    }
}
```

**Output**

The option has a value of 111

Here, the `if let` expression is matching on the `my_option` variable and binding the value of `Some` variant to the `value` variable.

If the match is successful, the code inside the `if` block is executed. If the match is not successful, the code inside the `else` block is executed.

---

## Common Use Cases of Pattern Matching in Rust

As you have seen, pattern matching is useful in numerous situations. Some common use cases for pattern matching include:

- Matching against any value like integers
- Matching against enum, struct or tuples
- Expressing conditional logic
- Destructuring data structure or destructuring elements of an iterator in a for loop
- Error handling with Result and Option types

- [](https://www.programiz.com/rust/pattern-matching#introduction)
- [](https://www.programiz.com/rust/pattern-matching#matching-a-variable)
- [](https://www.programiz.com/rust/pattern-matching#matching-an-enum)
- [](https://www.programiz.com/rust/pattern-matching#matching-option-and-result-type)
- [](https://www.programiz.com/rust/pattern-matching#if-let)
- [](https://www.programiz.com/rust/pattern-matching#common-use-cases)