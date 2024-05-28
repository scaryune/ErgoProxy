# Rust Variables and Mutability

In computer programming, we use variables to store data. For example,

```
let x = 1;
```

Here, x is the name of the variable which stores the value `1`.

We can think of variables as containers that hold information.

---

## Rust Variable Declaration

We use the `let` keyword to declare a variable in Rust.

```
let age = 31;
```

Here, we have created a variable named age with value `31`.

### Example: Rust Variables

```
fn main() {
    // variable to store integer value
    let age = 31;
    println!("Age: {}", age);

    // variable to store floating-point value
    let salary = 342523.23;
    println!("Salary: {}", salary);

    // variable to store string
    let name = "Jackie";
    println!("Name: {}", name);
}
```

**Output**

Age: 31
Salary: 342523.23
Name: Jackie

In the above example, we have created three different variables:

- age - to store an integer value
- salary - to store a floating-point data
- name - to store a string

Notice that we have used the `println!` macro to print the variables.

```
println!("Age: {}", age);
```

To learn more about `println!`, visit [_Rust Print Output_](https://www.programiz.com/rust/print-output).

---

## Change Value of a Variable

By default, Rust variables are immutable, which means we cannot change the value of a variable once it is defined. Let's see an example,

```
fn main() {
    // declare a variable with value 1
    let x = 1;
    println!("x = {}", x);

    // change the value of variable x
    x = 2;
    println!("x = {}", x);
}
```

When we run this code, we will get an error. This is because we are trying to change the value of the x variable from `1` to `2`.

```
error[E0384]: cannot assign twice to immutable variable `x`
 --> main.rs:7:5
  |
3 |     let x = 1;
  |         -
  |         |
  |         first assignment to `x`
  |         help: consider making this binding mutable: `mut x`
...
7 |     x = 2;
  |     ^^^^^ cannot assign twice to immutable variable
```

To solve this problem, Rust allows us to create mutable variables.

---

## Mutability in Rust

We use the `mut` keyword before the variable name to create a mutable variable. For example,

```
let mut x = 1;
```

Here, x is a mutable variable. Now we can change the value of x.

### Example: Mutable Variables

```
fn main() {
    // declare a mutable variable with value 1
    let mut x = 1;
    println!("Value of x = {}", x);

    // change the value of variable x
    x = 2;
    println!("Updated value of x = {}", x);
}
```

**Output**

Value of x = 1
Updated value of x = 2

Here, you can see we have successfully changed the value of the x variable. This is because we have defined the x variable using the `mut` keyword.

---

## Rules for Naming Variables in Rust

We can use any names as variable names, however, there are some rules we should follow:

1. Rust is a case sensitive language. Hence, lowercase variables and uppercase variables are different. For example,

age is different from AGE

name is different from Name

2. Variables must start with either a letter or an underscore. For example,

```
let age = 31;     	// valid and good practice
let _age = 31;    	// valid variable 
let 1age = 31;    // inavlid variable
```

3. Variable names can only contain letters, digits and an underscore character. For example,

```
let age1 = 31;        // valid variable
let age_num = 31;     // valid variable
let s@lary = 52352;   // invalid variable
```

4. Use underscore if we need to use two words as variable names. For example,

```
let first name = "Jack";    // invalid variable
let first_name = "Jack";    // valid variable
let first-name = "Jack";    // invalid variable
```

**Note:** Always try to give meaningful names to your variables. For example, `name`, `age`, `number` are better names than `n`, `ag`, `nm`.

---

## Rust Constants

A constant is a special type of variable whose value cannot be changed. We use the const keyword to create constants in Rust. For example,

```
fn main() {
    // declare a float constant
    const PI: f32 = 3.14;

    println!("Value of PI = {}", PI);
}
```

**Output:**

Value of PI = 3.14

In the above example, we have declared a constant PI with value `3.14`. Now, the value of PI cannot be changed throughout the program.

Let's see what happens if we try to change the value of a constant.

```
fn main() {
    // declare a constant
    const PI:f32 = 3.14;
    println!("Initial Value of PI: {}", PI);

    // change value of PI
    PI = 535.23;
    println!("Update Value of PI: {}", PI);
}
```

When we run this code, we will get an error because PI is a constant.

```
error[E0070]: invalid left-hand side of assignment
 --> main.rs:7:8
  |
7 |     PI = 535.23;
  |     -- ^
  |     |
  |     cannot assign to this expression
```

**Note:** As per Rust's naming convention, we use uppercase for the name of constants.