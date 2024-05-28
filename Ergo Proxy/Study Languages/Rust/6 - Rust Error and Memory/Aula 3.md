# Rust Ownership

Ownership is a set of rules that ensure memory safety in Rust programs.

Rust has an ownership model for memory management instead of garbage collector and manual memory management.

This ownership makes Rust different from other languages and allows programs to run without memory leaks and slowness.

---

## Variable Scope in Rust

A scope is a code block within the program for which a variable is valid. The scope of a variable defines its ownership.

For example,

```
// `name` is invalid and cannot be used here because it's not yet declared
{ // code block starts here
    let name = String::from("Ram Nepali");   // `name` is valid from this point forward
    
    // do stuff with `name`
} // code block ends
// this scope ends, `name` is no longer valid and cannot be used
```

Here the variable name is only available inside the code block, i.e., between the curly braces `{}`. We cannot use the name variable outside the closing curly brace.

Whenever a variable goes out of scope, its memory is freed.

To learn more about variable scope in Rust, visit [_Rust Variable Scope_](https://www.programiz.com/rust/variable-scope).

---

## Ownership Rules in Rust

Rust has some ownership rules. Keep these rules in mind as we work through some examples:

1. Each value in Rust has an owner.
2. There can only be one owner at a time.
3. When the owner goes out of scope, the value will be dropped.

---

## Data Move in Rust

Sometimes, we might not want a variable to be dropped at the end of the scope. Instead, we want to transfer ownership of an item from one binding (variable) to another.

Here's an example to understand data movement and ownership rules in Rust.

```
fn main() {
    // owner of the String value
    // rule no. 1 
    let fruit1 = String::from("Banana");
    
    // ownership moves to another variable
    // only one owner at a time
    // rule no. 2
    let fruit2 = fruit1;
    
    // cannot print variable fruit1 because ownership has moved
    // error, out of scope, value is dropped
    // rule no. 3
    // println!("fruit1 = {}", fruit1);
    
    // print value of fruit2 on the screen
    println!("fruit2 = {}", fruit2);
}
```

**Output**

fruit2 = Banana

Let's look into this example in detail, especially these two lines of code:

```
let fruit1 = String::from("Banana");
let fruit2 = fruit1;
```

Here, `fruit1` is the owner of the `String`.

A `String` stores data both on the stack and the heap. This means that when we bind a `String` to a variable `fruit1`, the memory representation looks like this:

![Memory representation of a String holding the value](https://www.programiz.com/sites/tutorial2program/files/rust-memory-representation-of-string.png "Memory representation of a String holding the value")

Memory representation of a String holding the value "Banana" bound to fruit1

A `String` holds a pointer to the memory that holds the content of the string, a length, and a capacity in the stack. The heap on the right hand side of the diagram holds the contents of the `String`.

Now, when we assign `fruit1` to `fruit2`, this is how the memory representation looks like:

![Memory representation when String value](https://www.programiz.com/sites/tutorial2program/files/rust-memory-representation-of-a-move.png "Memory representation when String value")

Memory representation when String value "Banana" moves from fruit to fruit2

Rust will invalidate (drop) the first variable `fruit1`, and move the value to another variable `fruit2`. This way two variables cannot point to the same content. At any point, there is only one owner of the value.

**Note:** The above concept is applicable for data types that don't have fixed sizes in memory and use the heap memory to store the contents.

Create a copy instead of the move using clone()

---

## Data Copy in Rust

Primitive types (Integers, Floats, and Booleans) have a known size at compile time and are stored entirely on the stack. Due to this, primitive types are cheap to copy, and they implement the copy trait instead of the move.

Let's see an example.

```
fn main() {
    let x = 11;
    
    // copies data from x to y 
    let y = x;

    println!("x = {}, y = {}", x, y);
}
```

**Output**

x = 11, y = 11

Here x is copied instead of a move, because primitive types like integers, floats implement the `Copy` trait by default and hence are copied.

Here, x variable can be used afterward, because x is copied and not moved even though `y` is assigned to `x`.

A **trait** is a way to define shared behavior in Rust. To learn more about traits, visit [_Rust Trait_](https://www.programiz.com/rust/trait).

---

## Ownership in Functions

Passing a variable to a function will move or copy, just as an assignment. Stack-only types will copy the data when passed into a function. Heap data types will move the ownership of the variable to the function.

Let's take a look at some examples.

**1. Passing String to a function**

```
fn main() {
    let fruit = String::from("Apple");  // fruit comes into scope
    
    // ownership of fruit moves into the function
    print_fruit(fruit);
    
    // fruit is moved to the function so is no longer available here
    // error
    // println!("fruit = {}", fruit);
}

fn print_fruit(str: String) {   // str comes into scope
    println!("str = {}", str);
}   // str goes out of scope and is dropped, plus memory is freed
```

**Output**

str = Apple

Here, the value of the fruit variable is moved into the function `print_fruit()` because `String` type uses heap memory.

**2. Passing Integer to a function**

```
fn main() {
    // number comes into scope
    let number = 10;
    
    // value of the number is copied into the function
    print_number(number);
    
    // number variable can be used here
    println!("number = {}", number);
}

fn print_number(value: i32) { // value comes into scope
    println!("value = {}", value);
}   // value goes out of scope
```

**Output**

value = 10

number = 10

Here, the value of the number variable is copied into the function `print_number()` because the `i32` (integer) type uses stack memory.

- [](https://www.programiz.com/rust/ownership#variable-scope)
- [](https://www.programiz.com/rust/ownership#rules)
- [](https://www.programiz.com/rust/ownership#data-move)
- [](https://www.programiz.com/rust/ownership#data-copy)
- [](https://www.programiz.com/rust/ownership#ownership-in-functions)