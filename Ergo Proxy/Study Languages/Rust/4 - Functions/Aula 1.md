# Rust Functions

Functions are reusable blocks of code that perform a specific task. For example, if we want to create a program to add two numbers, then we can create a Rust function to add numbers. Now, we can reuse this same function whenever we add two numbers.

Creating a function in Rust helps divide our code into smaller blocks and makes our code look cleaner and easier to understand.

Not only in Rust, but functions are also one of the core building blocks of any programming language.

---

## Define a Function in Rust

In Rust, we use the `fn` keyword to define a function. The syntax of a function is,

```
fn function_name(arguments) {
    // code
}
```

Let's see an example.

```
fn greet() {
    // code
}
```

Here,

- `fn` - keyword used to create a function in Rust
- `greet()` - name of the function
- `// code` - function body
- `{ }` - start and end of the function body

Now let's complete the `greet()` function to print "Hello, World!".

```
// define a function
fn greet() {
    println!("Hello, World!");
}

fn main() {

}
```

When we run this code, we will not get any output. This is because here we are just defining a function. To execute a function, we need to call it.

---

## Calling a Function in Rust

We use the name of the function and parentheses `()` to call a function.

```
// call a function
greet();
```

Let's complete the above example now.

```
// define a function
fn greet() {
    println!("Hello, World!");
}

fn main() {
    // function call
    greet();
}
```

**Output**

Hello, World!

Here, we have created a `greet()` function that prints "Hello, World!" on the screen. Notice that we are calling the function from inside `main()`.

**main() Function in Rust**

If you look carefully, you can see the syntax of `main()` looks similar to a function.

```
fn main() {
    // function call
    greet();
}
```

In Rust, `main()` is also a function known as a built-in function that has a special meaning. It is the entry point (start) of every Rust program.

**Note:** Rust code uses a small case as the convention for defining a function name. An extended function name with multiple words will have underscores in between words.

---

### Example: Function to Add Two Numbers in Rust

```
// function to add two numbers
fn add() {
    let a = 5;
    let b = 10;

    let sum = a + b;

    println!("Sum of a and b = {}", sum);
}

fn main() {
    // function call
    add();
}
```

**Output**

Sum of a and b = 15

In the above example, we have created a function named `add()`. The function adds two numbers and prints the sum.

Here's how the program works,

![Working of function in Rust](https://www.programiz.com/sites/tutorial2program/files/working-of-function-in-rust.png "Working of function in Rust")

Working of function in Rust

---

## Function Parameters in Rust

From the definition, we know that a function should be reusable. However, the `add()` function in our previous example can only be used to perform the addition of **5** and **10**.

```
// function to add two numbers
fn add() {
    let a = 5;
    let b = 10;

    let sum = a + b;

    println!("Sum of a and b = {}", sum);
}
```

This function is not dynamic to be reused.

To deal with this and make our functions more dynamic, we can create functions that accept external values. These external values are called function parameters.

Here's how we can create a function with parameters.

```
// function with parameters
fn add(a: i32, b: i32) {
    let sum = a + b;

    println!("Sum of a and b = {}", sum);
}
```

Here,

- `a` and `b` are function parameters
- `i32` is the data type of parameters

To call this function, we should provide some value during the function call.

```
add(2, 11);
```

Here, **2** and **11** are known as function arguments that are passed to the `add` function.

---

### Example: Function Parameters

```
// define an add function that takes in two parameters
fn add(a: i32, b: i32) {
    let sum = a + b;
    
    println!("Sum of a and b = {}", sum);
}

fn main() {
    // call add function with arguments
    add(2, 11);
}
```

**Output**

Sum of a and b = 13

Here's how the program works,

![Working of function with parameters in Rust](https://www.programiz.com/sites/tutorial2program/files/working-of-function-with-parameters-in-rust.png "Working of function with parameters in Rust")

Working of function with parameters in Rust

The arguments are assigned to the function parameters when we call the function.

- **2** is assigned to `a`
- **11** is assigned to `b`

As a result, we see the sum of **2** and **11** equal to **13** printed on the screen.

---

## Function with Return Value in Rust

In the last example, we computed the sum of two numbers and printed the result inside the function. However, we can also return the result from the function and use it anywhere in our program.

Here's how we can create a function in Rust that returns a value.

```
// define an add function that takes in two parameters with a return type
fn add(a: i32, b: i32) -> i32 {
    let sum = a + b;

    // return a value from the function
    return sum;
}
```

Here, `-> i32` before the opening curly bracket `{` indicates the function's return type. In this case, the function will return an `i32` value.

We have then used the `return` keyword to return the sum variable from the function.

The function returns the value to the place from where it is called, so the returned value needs to be stored somewhere.

```
// store the returned value in a variable
let sum = add(3, 5);
```

---

## Example: Function with Return Value

```
// define an add function that takes in two parameters with a return type
fn add(a: i32, b: i32) -> i32 {
    let sum = a + b;

    // return a value from the function
    return sum;
}

fn main() {
    // function call
    let sum = add(3, 5);

    println!("Sum of a and b = {}", sum);
}
```

**Output**

Sum of a and b = 8

Here's how the program works,

![Working of function with return value in Rust](https://www.programiz.com/sites/tutorial2program/files/working-of-function-with-return-value-in-rust.png "Working of function with return value in Rust")

Working of function with return value in Rust

In the above example, when we reach the `return` statement in the add function, it returns the sum variable. The returned value is stored in the sum variable inside `main()`.

---

## Frequently Asked Questions

How can we return a value from a function with a Rust expression?

How can we return multiple values from a function in Rust?

How to pass by reference in Rust?

	What are the advantages of functions in Rust?