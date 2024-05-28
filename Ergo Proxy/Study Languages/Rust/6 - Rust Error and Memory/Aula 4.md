# Rust References and Borrowing

**References** in Rust allow us to point to a resource (value) without owning it. This means that the original owner of the resource remains the same.

References are helpful when passing values to a function that we do not want to change the ownership of. Creating a reference is known as **borrowing in Rust**.

---

## Understanding References in Rust

Let's look at an example to learn about references in Rust.

```
fn main() {
    let str = String::from("Hello, World!");
    
    // Call function with reference String value
    let len = calculate_length(&str);

    println!("The length of '{}' is {}.", str, len);
}

// Function to calculate length of a string
// It takes a reference of a String as an argument
fn calculate_length(s: &String) -> usize {
    s.len()
}
```

**Output**

The length of 'Hello, World!' is 13.

In the above example, we define a function called `calculate_length()` which takes a `&String` type as an argument.

The important part here is that `s` is a reference to a `String` and it doesn't take ownership of the actual value of `String`.

```
fn calculate_length(s: &String) -> usize { // s is a reference to a String
    s.len()
}
```

When, `s` goes out of scope, at the end of the function, it is not dropped because it does not have ownership of what it refers to.

The function call looks like:

```
let str = String::from("Hello, World!");

let len = calculate_length(&str);
```

The `&str` syntax while calling the function lets us create a **reference** that refers to the value of `str` but does not own it.

The action of creating a reference is known as **borrowing**. Borrowing is when we borrow something, and we are done with it, we give it back. It doesn't make us the owner of the data.

**Note:** Ampersand (&) represents references, and they allow us to refer to some value without taking ownership of it.

---

## Modifying a Reference in Rust

By default a reference is always immutable. However, we can use the `&mut` keyword to make a reference mutable.

For example,

```
fn main() {
    let mut str = String::from("Hello");
    
    // before modifying the string
    println!("Before: str = {}", str);

    // pass a mutable string when calling the function
    change(&mut str);
    
    // after modifying the string
    println!("After: str = {}", str);
}

fn change(s: &mut String) {
    // push a string to the mutable reference variable
    s.push_str(", World!");
}
```

**Output**

Before: str = Hello
After: str = Hello, World!

Here, we set the variable `str` to be mutable. Then we create a mutable reference with `&mut str`, and call the `change()` function with a mutable reference `s: &mut String`.

This allows the `change()` function to modify the value it borrows. Inside the `change()` function, we push a string with `s.push_str(", World!")` to the reference string.

**Note:** If you have a mutable reference to a value, you can have no other references to that value.

```
fn main() {
    let mut str = String::from("hello");

    // mutable reference 1
    let ref1 = &mut str;

    // mutable reference 2
    let ref2 = &mut str;

    println!("{}, {}", ref1, ref2);
}
```

**Output**

error[E0499]: cannot borrow `str` as mutable more than once at a time
  --> src/main.rs:8:16
   |
5  |     let ref1 = &mut str;
   |                -------- first mutable borrow occurs here
...
8  |     let ref2 = &mut str;
   |                ^^^^^^^^ second mutable borrow occurs here
9  |
10 |     println!("{}, {}", ref1, ref2);
   |                        ---- first borrow later used here

---

## Rules of References

Rust primarily follows these rules of references at any given time:

1. At any given time, you can have either one mutable reference or any number of immutable references.
2. References must always be valid.

- [](https://www.programiz.com/rust/references-and-borrowing#introduction)
- [](https://www.programiz.com/rust/references-and-borrowing#understanding-references)
- [](https://www.programiz.com/rust/references-and-borrowing#modifying-a-reference)
- [](https://www.programiz.com/rust/references-and-borrowing#rules)

[

  


](https://www.programiz.com/rust/ownership "Rust Ownership")