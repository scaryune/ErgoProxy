# Rust Type Casting

Type casting allows us to convert variables of one data type to another. In Rust, we use the `as` keyword to perform type casting. For example,

```
// create a floating-point variable
let decimal: f64 = 54.321;

// convert floating point type to integer type
let integer = decimal as u16;
```

Here, `decimal as u16;` expression converts `f64` floating-point type to `u16` integer type.

---

### Example: Rust Type Casting
 
```
fn main() {
    // assign a floating point f64 value to decimal variable
    let decimal: f32 = 64.31;

    // convert decimal variable to u16 integer type using as keyword
    let integer = decimal as u16;

    println!("decimal = {}", decimal);
    println!("integer = {}", integer);
}
```

**Output:**

decimal = 64.31
integer = 64

Here, the variable decimal with floating point value `64.31` is converted to an integer value `64` of type `u16` with the help of `as` Rust keyword.

We are converting data from one type to another type manually using the `as` keyword. This type of type casting is also known as **Explicit Type Casting**.

---

## Type Conversion: Character to Integer in Rust

```
fn main() {
    let character: char = 'A';

    // convert char type to u8 integer type
    let integer = char as u8;

    println!("character = {}", character);
    println!("integer = {}", integer);
}
```

**Output:**

character = A
integer = 65

In Rust, the `char` data type is internally stored as a Unicode Scalar Value. Unicode Scalar Value is simply the numeric representation of a character in [Unicode](https://en.wikipedia.org/wiki/Unicode) standard also known as a code point.

The Unicode value of character `A` is `65`. So, we get the output of `65` when converting the character `A` to an integer.

---

## Type Conversion: Integer to Character in Rust

We can also convert integer type to a character type. For example,

```
fn main() {
    // only u8 integer data type can be converted into char
    let integer: u8 = 65;
  
    // convert integer to char using the as keyword
    let character = integer as char;

    println!("integer = {}" , integer);
    println!("character = {}", character);
}
```

**Output:**

integer = 65
character = A

In the example above, the integer value `65` is the Unicode code for character `A`. Thus after type casting, we get character `A` as the output. Every character has an Unicode code associated with it.

### Error while Converting Integer to Character

We are only allowed to use `u8` integers while performing type casting between integer and character. If we use any other integer type and convert it to a character, we will get an error. For example,

```
fn main() {
    let integer: i32 = 65;
  
    // convert integer to char using the as keyword
    let character = integer as char;

    println!("integer = {}" , integer);
    println!("character = {}", character);
}
```

**Error:**

error[E0604]: only `u8` can be cast as `char`, not `i32`
 --> main.rs:5:19
  |
5 |   let character = integer as char;
  |                   ^^^^^^^^^^^^^^^ invalid cast

Here, we have used `i32` data type instead of `u8`. Hence we get an error.

It's because Unicode Scalar Values are small integer numbers and fit in the range of `u8` data type.

---

## Type Casting: Boolean to Integer in Rust

```
fn main() {
    let boolean1: bool = false;
    let boolean2: bool = true;
  
    // convert boolean type to integer
    let integer1 = boolean1 as i32;
    let integer2 = boolean2 as i32;

    println!("boolean1 = {}", boolean1);
    println!("boolean1 = {}", boolean2);
    println!("integer1 = {}", integer1);
    println!("integer2 = {}", integer2);
}
```

**Output:**

boolean1 = false
boolean1 = false
integer1 = 0
integer2 = 1

Here, boolean data type `false` and `true` are converted to integer `0` and `1` respectively.

---

## Limitations of Type Casting

There are limitations while performing type casting in Rust. Not all data types are converted to one another.

For example, we cannot convert a floating type to a character.

```
fn main() {
    let decimal: f32 = 65.321;
  
    // convert float to char data type
    let character = decimal as char;

    println!("decimal = {}", decimal);
    println!("character = {}", character);
}
```

**Error:**

error[E0604]: only `u8` can be cast as `char`, not `f32`
 --> main.rs:5:19
  |
5 |   let character = decimal as char;
  |                   ^^^^^^^^^^^^^^^ invalid cast

Here, we have tried to convert the `float` type to `char`, hence we get an error. The error says that Rust is expecting a `u8` data type for conversion not `f32`.