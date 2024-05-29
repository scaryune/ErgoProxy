# Rust Operators

An operator is a symbol that performs operations on values or variables. For example, `-` is an operator that performs subtraction between two values.

Rust programming provides various operators that can be categorized into the following major categories:

- Arithmetic Operators
- Compound Assignment Operators
- Logical Operators
- Comparison Operators

---

## 1. Arithmetic Operators in Rust

We use arithmetic operators to perform addition, subtraction, multiplication, and division.

Here's a list of various arithmetic operators available in Rust. We have used the variable names `a` and `b` in the example.

| Operator             | Example |
| -------------------- | ------- |
| `+` (Addition)       | `a + b` |
| `-` (Subtraction)    | `a - b` |
| `*` (Multiplication) | `a * b` |
| `/` (Division)       | `a / b` |
| `%` (Remainder)      | `a % b` |

### Example 1: Addition, Subtraction and Multiplication Operators

```
fn main() {
    let a = 20;
    let b = 2;

    // add two variables using + operator
    let x = a + b;
    println!("{} + {} = {}", a, b, x);

    // subtract two variables using - operator
    let y = a - b;
    println!("{} - {} = {}", a, b, y);

    // multiply two variables using * operator
    let z = a * b;
    println!("{} * {} = {}", a, b, z);
}
```

**Output:**

20 + 2 = 22
20 - 2 = 18
20 * 2 = 40

---

### Example 2: Rust Division Operator

```
fn main() {
    let dividend = 21;
    let divisor = 8;

    // arithmetic division using / operator with integers
    let division = dividend / divisor;

    println!("{} / {} = {}", dividend, divisor, division);
}
```

**Output:**

21 / 8 = 2

In the above example, we use the `/` operator to divide two integers `21` and `8`. The output of the operation is `2`.

In standard calculation, `21 / 8` gives `2.625`. However, in Rust, when the `/` operator is used with integer values, we get the quotient (integer) as the output.

![Integer division operation in Rust](https://www.programiz.com/sites/tutorial2program/files/rust-division-operation.png "Working of integer division operation in Rust")

Working of integer division operation in Rust

If we want the actual result, we should use the `/` operator with floating-point values. For example,

```
fn main() {
    let dividend = 21.0;
    let divisor = 8.0;

    // arithmetic division using / operator with floating point values
    let division = dividend / divisor;

    println!("{} / {} = {}", dividend, divisor, division);
}
```

**Output:**

21 / 8 = 2.625

Here, both dividend and divisor variables are assigned floating point values. Thus, the division operation returns a floating point result of `2.625`.

---

### Example 3: Remainder Operator

```
fn main() {
    let dividend = 21;
    let divisor = 8;

    // arithmetic remainder using % operator
    let remainder = dividend % divisor;
  
    println!("{} % {} = {}", dividend, divisor, remainder);
}
```

**Output:**

21 % 8 = 5

Here, we use the remainder operator `%` with two integers: `21` and `8`. The output of the operation is `5`.

The remainder operator `%`, as the name suggests, always returns the remainder after division.

![Remainder operation in Rust](https://www.programiz.com/sites/tutorial2program/files/rust-remainder-operation.png "Working of remainder operation in Rust")

Working of remainder operation in Rust

---

## Assignment Operator

We use an assignment operator to assign a value to a variable. For example,

```
let x = 5;
```

Here, `=` is an assignment operator that assigns the value on the right `5` to the variable `x` on the left. The assignment operator is the most common operator in Rust.

---

## Assignment Operators

In Rust, we use the assignment operator to assign a value to a variable. For example,

```
let mut x = 1;
```

Here, the `=` operator assigns the value on the right to the variable on the left.

### Compound Assignment Operators

We can also use an assignment operator and an arithmetic operator, known as a compound assignment operator. For example,

```
let mut x = 1;

// compound assignment operators
x += 3;
```

Here, `+=` is a compound assignment operator known as an addition assignment. It first adds **3** to the value of x (**1**) and assigns the final result (**4**) to `x`.

Here's a list of various compound assignment operators in Rust.

|Operator|Example|Equivalent To|
|---|---|---|
|`+=` (addition assignment)|`a += b`|`a = a + b`|
|`-=` (subtraction assignment)|`a -= b`|`a = a - b`|
|`*=` (multiplication assignment)|`a *= b`|`a = a * b`|
|`/=` (division assignment)|`a /= b`|`a = a / b`|
|`%=` (remainder assignment)|`a %= b`|`a = a % b`|

---

### Example: Compound Assignment Operator

```
fn main() {
    let mut a = 2;
  
    // arithmetic addition and assignment
    a += 3;

    println!("a = {}", a);
}
```

**Output:**

a = 5

---

## Comparison Operators

We use comparison operators to compare two values or variables. For example,

```
6 > 5
```

Here, the relational operator `>` (greater than) checks if `6` is greater than `5`.

A relational operator returns:

- `true` if the relation between two values is correct
- `false` if the relation is incorrect

**Note:** Comparison operators are also known as **relational operators**.

Here's a list of comparison operators available in Rust.

|Operator|Example|Description|
|---|---|---|
|`>` (Greater than)|`a > b`|`true` if `a` is greater than `b`|
|`<` (Less than)|`a < b`|`true` if `a` is less than `b`|
|`>=` (Greater than or equal to)|`a >= b`|`true` if `a` is greater than or equal to `b`|
|`<=` (Less than or equal to)|`a <= b`|`true` if `a` is less than or equal to `b`|
|`==` (Equal to)|`a == b`|`true` if `a` is equal to `b`|
|`!=` (Not equal to)|`a != b`|`true` if `a` is not equal to `b`|

### Example: Comparison Operators

```
fn main() {
    let a = 7;
    let b = 3;
    
    // use of comparison operators
    let c = a > b;
    let d = a < b;
    let e = a == b;
    
    println!("{} >= {} is {}", a, b, c);
    println!("{} <= {} is {}", a, b, d);
    println!("{} == {} is {}", a, b, e);
}
```

**Output:**

7 > 3 is true
7 < 3 is false
7 == 3 is false

---

## Logical Operators

We use logical operators to perform logical decisions or operations. A logical operation returns either `true` or `false` depending on the conditions. For example,

```
(5 < 6) && (7 > 4)
```

Here, `&&` is the **logical AND operator** that returns `true` if both conditions are `true`. In our example, both conditions are `true`. Hence the expression is `true`.

There are mainly 3 logical operators in Rust.

|Operator|Example|Description|
|---|---|---|
|`&&` (Logical AND)|`exp1 && exp2`|returns `true` if both `exp1` and `exp2` are `true`|
|`\|` (Logical OR)|`exp1 \| exp2`|returns `true` if any one of the expressions is `true`|
|`!` (Logical NOT)|`!exp`|returns `true` if the expression is `false` and returns `false`, if it is `true`|

### Example: Logical Operators

```
fn main() {
    let a = true;
    let b = false;
    
    // logical AND operation
    let c = a && b;

    // logical OR operation
    let d = a || b;

    // logical NOT operation
    let e = !a;
    
    println!("{} && {} = {}", a, b, c);
    println!("{} || {} = {}", a, b, d);
    println!("!{} = {}", a, e);
}
```

**Output:**

true && false = false
true || false = true
!true = false

**Note:** The logical `AND` and `OR` operators are also called **short-circuiting logical operators** because these operators don't evaluate the whole expression in cases they don't need to. For example, in this expression

```
false || true || false
```

The `||` operator evaluates to `true` because once the compiler sees a single `true` expression, it skips the evaluation and returns `true` directly.