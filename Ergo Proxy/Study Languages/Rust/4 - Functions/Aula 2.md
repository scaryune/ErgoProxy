# Rust Variable Scope

In computer programming, a variable's scope defines the region in which the variable is available for use. For example,

```
fn main() {
    // this variable has scope inside the main function block
    let age = 31;
    …
}
```

Here, the age variable has scope inside the body `{...}` of the `main()` function,

**Note:** Each variable in Rust has a scope that is valid inside a block. A block is a collection of statements enclosed by curly braces `{}`.

---

## Working of Variable Scope in Rust

Let's look at how variable scope works with an example,

```
fn main() {
    // scope of outer_var variable is inside the main function code block
    let outer_var = 100;
    
    // start of the inner code block
    {
        // scope of inner_var variable is only inside this new code block
        let inner_var = 200;
        println!("inner_var = {}", inner_var);
    }
    // end of the inner code block
    
    println!("inner_var = {}", inner_var);
    println!("outer_var = {}", outer_var);
}
```

Here, if we try to print the inner_var outside of the inner code block, the program fails to compile, and we encounter an error.

**Output**

error[E0425]: cannot find value `inner_var` in this scope
  --> src/main.rs:13:32
   |
13 |     println!("inner_var = {}", inner_var);
   |                                ^^^^^^^^^ help: a local variable with a similar name exists: `outer_var`

The Rust compiler could not find inner_var in scope as we tried to print the variable outside the inner code block.

To fix this, we can do the following,

```
fn main() {
    // scope of outer_var variable is inside the main function code block
    let outer_var = 100;
    
    // start of the inner code block
    {
        // scope of inner_var variable is only inside this new code block
        let inner_var = 200;
        println!("inner_var = {}", inner_var);
        println!("outer_var inside inner block = {}", outer_var);
    }
    // end of the inner code block
    
    println!("outer_var = {}", outer_var);
}
```

**Output**

inner_var = 200
outer_var inside inner block = 100
outer_var = 100

We removed the `println!("inner_var = {}", inner_var);` from the outer code block and the program now works as expected.

Additionally, we can access the outer_var inside the inner code block because its scope is in the `main()` function.

Here is how variable scope works in the above program,

![Working of variable scope in Rust](https://www.programiz.com/sites/tutorial2program/files/working-of-variable-scope-in-rust.png "Working of variable scope in Rust")

Working of variable scope in Rust

---

## Variable Shadowing in Rust

In Rust, when a variable declared within a particular scope has the same name as a variable declared in the outer scope, it is known as **variable shadowing**.

We can use the same variable name in different scope blocks in the same program.

Let's take a look at an example,

```
fn main() {
    let random = 100;

    // start of the inner block
    {
        println!("random variable before shadowing in inner block = {}", random);

        // this declaration shadows the outer random variable
        let random = "abc";

        println!("random after shadowing in inner block = {}", random);
    }
    // end of the inner block

    println!("random variable in outer block = {}", random);
}
```

**Output**

random variable before shadowing in inner block = 100
random after shadowing in inner block = abc
random variable in outer block = 100

Here, the random variable declared in the outer block is shadowed in the inner block. Let's look at what that means,

```
let random = "abc";
```

The random variable value inside the inner block will shadow the value of the outer block so that the inner block will have the `"abc"` value. However, the value of the random variable remains the same outside of the inner block.

---

## Variable Freezing in Rust

We can freeze a variable in Rust by using shadowing and immutability. Once a variable is frozen, we cannot change the variable value in the inner scope.

Let's see an example.

```
fn main() {
    let mut age = 1;

    // start of the inner block
    {
        // shadowing by immutable age variable
        let age = age;

        // error, age variable is frozen in this scope
        age = 2;

        println!("age variable inner block = {}", age);
        // age variable goes out of scope
    }
    // end of the inner block

    // age variable is not frozen in outer block
    age = 3;

    println!("integer variable outer block = {}", age);
}
```

**Output**

error[E0384]: cannot assign twice to immutable variable `age`
  --> src/main.rs:10:9
   |
7  |         let age = age;
   |             ---
   |             |
   |             first assignment to `age`
   |             help: consider making this binding mutable: `mut age`
...
10 |         age = 31;
   |         ^^^^^^^^ cannot assign twice to immutable variable

In the above example, we have assigned the mutable variable of the outer block named age to the same immutable variable in the inner scope.

fn main() {
    let mut age = 100;

    {

        let age = age;

        …
    }
    …
}

In doing this, we are shadowing the mutable `age` variable with an immutable variable named `age`.

Now the age variable freezes inside the inner block because the inner age variable is pointing to the same value as the age variable in the outer block.

Thus, we cannot change the value of age inside the inner block and encounter an error.

Once we get out of the inner block, the value of age can be changed.

Let's look at the working version of the variable freezing example.

```
fn main() {
    let mut age = 100;

    {
        // shadowing by immutable age variable
        let age = age;

        println!("age variable inner block = {}", age);
        // age goes out of scope
    }

    // age variable is not frozen in this scope
    age = 3;

    println!("age variable outer block = {}", age);
}
```

**Output**

age variable inner block = 100
age variable outer block = 3

- [](https://www.programiz.com/rust/variable-scope#introduction)
- [](https://www.programiz.com/rust/variable-scope#working-of-variable-scope)
- [](https://www.programiz.com/rust/variable-scope#variable-shadowing)
- [](https://www.programiz.com/rust/variable-scope#variable-freezing)

[

  


](https://www.programiz.com/rust/function "Rust Function")