# Rust for Loop

The `for` loop in Rust is used to iterate a range of numbers. The syntax of `for` loop is:

```
for variable in lower_bound_number..upper_bound_number {
    // code block
}
```

Let's take a look at an example,

### Example: Rust for Loop

```
fn main() {
    // usage of for loop
    for i in 1..6 {
        println!("{}", i);
    }
}
```

**Output**

1
2
3
4
5

In this example, we print numbers `1` to `5` using the `for` syntax. If we look at the example closely, we see

```
for i in 1..6 {
    println!("{}", i);
}
```

Here,

- `for` - is the keyword to start any `for` loop
- `i` - is known as the loop variable and should be a valid variable name
- `in` - is the keyword used to iterate over a series of values with `for`
- `1..6` - is known as an **Iterator** where `1` is the lower bound and `6` is the upper bound. This yields values from 1 (inclusive) to 6 (exclusive) in steps of one.

**Note:** The for loop is also known as a for-in loop because of its syntax.

---

## Working of for Loop

![Working of Rust for Loop](https://www.programiz.com/sites/tutorial2program/files/working-rust-for-loop.png "Working of Rust for Loop")

Working of Rust for Loop

---

### Example: Sum of First 10 Natural Numbers using for Loop

```
fn main() {
    let mut sum = 0;
    
    // for loop to iterate over first 10 natural numbers
    for i in 1..11 {
        sum += i;
    }
    
    println!("Sum: {}", sum);
}
```

**Output**

Sum: 55

Here, we loop over the iterator `1..11`, which yields values from `1` to `10`. A sum variable is created to sum all the values in each iteration. Finally, we print the sum of all the values.

**Note**: The `1..11` syntax is also known as a **range notation** or **range operator** used to create **Iterators** in Rust.

To learn more about iterators, visit [_Rust Iterator_](https://www.programiz.com/rust/iterator).

---

## Frequently Asked Questions

Does Rust have a "C-style" for loop?

How to use range notation that is inclusive on both ends?

How to use for to loop over an array or a list?