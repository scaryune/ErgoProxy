# Rust Data Types

We use data types in Rust to determine the type of data associated with the variables. For example,

```
let alphabet: char;
```

Here, `char` is the data type that specifies that the alphabet variable can only store the character data.

---

## Data Types in Rust

There are four primary data types in Rust also known as scalar types:

- Integer
- Floating-Point
- Boolean
- Character

---

## 1. Integer Type

In Rust, we use integer data types to store whole numbers. For example,

```
let number: i32 = 200;
```

Here, we have created the number variable of type `i32` (integer) and stored the value `200`.

The integer type `i32` has two parts to it:

- `i` - specifies signed integer type (can store both positive or negative value)
- `32` - size of the data type (takes 32 bits of space in memory)

---

### Signed Integer Type in Rust

```
fn main() {
    // Signed integer type 
    let x: i32 = -200;
    let y: i32 = 200;

    println!("x = {}", x);
    println!("y = {}", y);
}
```

**Output:**

x = -200
y = 200

Here, we have defined two integers x and y with values `-200` and `200` respectively and printed it to the screen.

### Unsigned Integer Type

We can also create variables that can only store positive integer values. For example,

```
fn main() {
    // Unsigned integer type
    let x: u32 = 300;

    println!("x = {}", x);
}
```

**Output:**

x = 300

Here, `u32` specifies that the x variable can only store positive values. `u` specifies unsigned integer type.

If we try to store negative numbers to `u32` type variables, we will get an error. For example,

```
fn main() {
    let x: u32 = -200;

    println!("x = {}", x);
}
```

**Error:**

error[E0600]: cannot apply unary operator `-` to type `u32`
 --> main.rs:2:18
  |
2 |   let x: u32 = -200;
  |                ^^^^ cannot apply unary operator `-`
  |
  = note: unsigned values cannot be negated

---

## Categories of Integer Data Types in Rust

Depending on the size of data, we can further classify the signed and unsigned integer type into various categories:

|Size|Signed|Unsigned|
|---|---|---|
|8-bit|i8|u8|
|16-bit|i16|u16|
|32-bit|i32|u32|
|64-bit|i64|u64|
|128-bit|i128|u128|

---

## 2. Rust Floating Point Type

Floating point types are used to store fractional numbers (numbers with decimal points). In Rust, floating-point data types can be divided into:

- `f32`
- `f64`

Here, the `f` character represents a floating point number, `32` and `64` represent the size in bits.

Let's take a look at an example,

```
let x: f32 = 3.1;
```

Here, `f32` is a type declaration for the floating point value. In this case, x is assigned to a floating point value of `3.1`.

---

### Example: Floating Point Data Type

```
fn main() {
    // f32 floating point type
    let x: f32 = 3.1;

    // f64 floating point type
    let y: f64 = 45.0000031;

    println!("x = {}", x);
    println!("y = {}", y);
}
```

**Output:**

x = 3.1
y = 45.0000031

**Note:** `f32` is a single-precision floating type whereas `f64` is double-precision type. With double-precision, `f64` can store data with a larger decimal range and is considered more precise.

---

## 3. Rust Boolean Type

In Rust, a boolean data type can have two possible values: `true` or `false`. For example,

```
// boolean value true
let flag1: bool = true;

// boolean value false
let flag2: bool = false;
```

Here, we have used the `bool` keyword to represent the boolean type in Rust.

---

### Example: Boolean Type

```
fn main() {
    // boolean type
    let flag1: bool = true;
    let flag2: bool = false;

    println!("flag1 = {}", flag1);
    println!("flag2 = {}", flag2);
}
```

**Output:**

flag1 = true
flag2 = false

**Note:** Booleans are frequently used in conditional statements like if/else expressions.

---

## 4. Rust Character Type

The character data type in Rust is used to store a character. For example,

```
fn main() {
    // char type
    let character: char = 'z';

    println!("character = {}", character);
}
```

**Output:**

character = z

Here, `char` represents the character type variable and we use single quotes to represent a character.

We can also store special characters like `$`, `@`, `&`, etc. using the character type. For example,

```
fn main() {
    // char type
    let character: char = 'z';
    let special_character: char = '$';

    println!("character = {}", character);
    println!("special_character = {}", special_character);
}
```

**Output:**

character = z
special_character = $

**Note**: We can also store numbers as characters using single quotes. For example,

```
let numeric_character: char = '5';
```

Here, `'5'` is not an integer, it's a character because we have enclosed it inside single quotes.

---

## Type Inference in Rust

So far we have mentioned the data type during the variable declaration. However, in Rust we can create variables without mentioning a data type. For example,

```
let x = 51;
```

In this case, Rust automatically identifies the data type by looking at the value of the variable x and associates it with the variable. This process is known as **Type Inference**.

Let's see an example,

```
fn main() {
    let x = 51;

    println!("x = {}", x);
}
```

**Output:**

x = 51

Here, you can see that we haven't mentioned the data type of `x` variable. It is because Rust will automatically set `i32` as the type (default type for integer variable) by looking at the value `51`.

- [](https://www.programiz.com/rust/data-types#introduction)
- [](https://www.programiz.com/rust/data-types#data-types)
- [](https://www.programiz.com/rust/data-types#integer-type)
- [](https://www.programiz.com/rust/data-types#categories)
- [](https://www.programiz.com/rust/data-types#floating-point-type)
- [](https://www.programiz.com/rust/data-types#boolean-type)
- [](https://www.programiz.com/rust/data-types#character-type)
- [](https://www.programiz.com/rust/data-types#type-inference)

[

  


](https://www.programiz.com/rust/variables-mutability "Rust Variables and Mutability")