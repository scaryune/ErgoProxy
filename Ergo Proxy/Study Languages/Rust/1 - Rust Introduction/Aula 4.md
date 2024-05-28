# Rust Print Output

In Rust, we use the `print!` macro to print strings, numbers and variables on the output screen. For example,

```
fn main() {
    print!("Hello, World!");
}
```

**Output**

Hello, World!

Here, `print!` is a macro that prints the text inside double quotes. To learn more about macros, visit [_Rust Macro_](https://programiz.com/rust/macro).

In Rust, there are two variations of the print:

- print!()
- println!()

---

## Rust print! Macro

As mentioned earlier, the `print!` macro prints the text inside double quotes. For example,

```
fn main() {
    print!("Rust is fun! ");
    print!("I love Rust programming.");
}
```

**Output**

Rust is fun! I love Rust programming.

You can see we have used two `print!` macros to print two different strings. However, both the strings are printed in the same line.

To separate the print strings in different lines, we can use the `println!` macro which will add a new line character at the end.

---

## Rust println! Macro

```
fn main() {
    println!("Rust is fun!");
    println!("I love Rust programming.");
}
```

**Output**

Rust is fun!
I love Rust programming.

Here, you can see our output is printed in two separate lines.

This is because `println!` adds a new line character (enter) at the end, so the second text is printed in the next line.

---

## Print Variables

We can use the same `print!` and `println!` macros to print variables in Rust. For example,

```
fn main() {
    let age = 31;
  
    // print the variable using println!
    println!("{}", age);

    // print the variable using print!
    print!("{}", age);
}
```

**Output**

31
31

In the above example, notice the print statements:

```
print!("{}", age);
println!("{}", age);
```

Here, `{}` is a placeholder which is replaced by the value of the variable after the comma. That's why we get **31** as output instead of `{}`.

We can also add text with the placeholder to format our output. For example,

```
fn main() {
    let age = 31;
  
    // print the variable using println!
    println!("Age = {}", age);
}
```

**Output**

Age = 31

Here, you can see the output looks much more informative.

![Placeholder {} inside of double quotes is replaced by age variable](https://www.programiz.com/sites/tutorial2program/files/rust-print-variable.png "Working of println! variable substitution")

Working of println! variable substitution

---

## Print Multiple Variables

We can use a single `println!` macro to print multiple variables together. For example,

```
fn main() {
    let age = 31;
    let name = "Jack";
  
    // print the variables using println!
    println!("Name = {}, Age = {}", name, age);
}
```

**Output**

Name = Jack, Age = 31

Here, you can see variables are printed sequentially. That is, the first variable name replaces the first placeholder and the second variable age replaces the second placeholder.

![Placeholders {} inside of double quotes are replaced by name and age variable](https://www.programiz.com/sites/tutorial2program/files/rust-print-multiple-variables.png "Working of println! multiple variable substitution")

Working of println! multiple variable substitution

However, we can also specify the numbering for placeholders to print variables in different order. For example,

```
fn main() {
    let age = 31;
    let name = "Jack";
  
    // print the variable using println!
    println!("Name = {0}, Age = {1}", name, age);
}
```

**Output**

Name = Jack, Age = 31

Here, the placeholder

- `{0}` is replaced by the first variable name
- `{1}` is replaced by the second variable age

Similarly, we can also use the variable names directly inside the placeholder. For example,

```
fn main() {
    let age = 31;
    let name = "Jack";
  
    // print the variables using println!
    println!("Name = {name}, Age = {age}");
}
```

**Output**

Name = Jack, Age = 31

Here, instead of using variables separately after comma, we have directly provided them inside the placeholder.

- `{name}` - prints the value of the name variable
- `{age}` - prints the value of the age variable

---

## Print Newline Character

In Rust, we can print newline character(s) using the `\n` escape sequence. For example,

```
fn main() {
    print!("Rust is fun!\nI love Rust programming.");
}
```

**Output:**

Rust is fun!
I love Rust programming.

Here, `\n` is an escape sequence that adds a new line character. Hence, the text after `\n` is printed in a new line.

- [](https://www.programiz.com/rust/print-output#print-macro)
- [](https://www.programiz.com/rust/print-output#println-macro)
- [](https://www.programiz.com/rust/print-output#print-variables)
- [](https://www.programiz.com/rust/print-output#print-multiple-variables)
- [](https://www.programiz.com/rust/print-output#print-newline-character)