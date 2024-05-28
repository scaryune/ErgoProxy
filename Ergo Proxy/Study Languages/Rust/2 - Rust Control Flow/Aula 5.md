# Rust break and continue

A loop executes a block of code multiple times. However, sometimes we might need to alter the flow of a loop by terminating its execution or skipping an iteration.

In such cases, we use the Rust `break` and `continue` to alter the normal execution of loops. For example,

- `break` - terminates the loop
- `continue` - skips the current iteration of the loop and moves on to the next

---

## Rust break

In Rust, we use the `break` keyword to terminate the execution of any loop. For example,

```
while n < 10 {
    break;
}
```

Here, the `while` loop will end whenever it encounters the `break` keyword, irrespective of the loop condition (`n < 10`).

---

## Example: Rust break

```
fn main() {
    let mut number = 0;
    
    // loop starts here
    loop {
        number += 1;

        // condition to exit the loop
        if number > 5 {
            break;
        }

        println!("{}", number);        
    }
}
```

**Output**

1
2
3
4
5

This program prints the first five natural numbers using a `loop` expression and a `break` keyword. Notice the use of the `break` keyword,

```
if number > 5 {
    break;
}
```

When the number variable, which is incremented by `1` in each iteration, reaches `6`, the `if` condition evaluates to `false`, and we exit the `loop` using the `break` keyword.

**Note:** It is upto the user to define the **condition** when the loop exits, or else the loop might run forever. You can use the `break` keyword with `while` or `for` loops in a similar pattern.

---

## Working of break Keyword in Rust

![Working of continue in Rust](https://www.programiz.com/sites/tutorial2program/files/working-of-continue-in-rust.png "Working of continue in Rust")

Working of continue in Rust

---

## Rust break with Nested Loops

```
fn main() {
    let mut i = 1;
    
    // start of outer loop
    while i <= 5 {
        let mut j = 1;
     
        // start of inner loop
        while j <= 5 {
            print!("*");
            
            // condition to exit the inner loop
            if j == 3 {
                // terminate the inner loop
                break;
            }
            
            j += 1;
        }
        
        println!("");
        
        i += 1;
    }
}
```

**Output**

***
***
***
***
***

In the above example, we have used the `break` keyword in the body of the inner `while` loop.

```
if j == 3 {
    // terminate the inner loop
    break;
}
```

When the value of the counter variable j reaches `3`, the inner `while` loop terminates. As a result, we only see three asterisks (`***`) printed on every line of the screen.

---

## Rust continue

In Rust, we use the `continue` statement to skip the current iteration of any loop and move to the next iteration. For example,

```
while n < 10 {
    if n == 5 {
        continue;
    }
}
```

Here, the `while` loop will skip the current iteration when it encounters the `continue` keyword irrespective of the loop **condition** (`n<10`).

---

## Example: Rust continue

```
fn main() {
    let mut number = 0;

    while number < 5 {
        number += 1;

        // condition to skip the iteration
        if number == 3 {
            continue;
        }

        println!("{}", number);
    }
}
```

**Output**

1
2
4
5

In this example, we use the `while` expression to print natural numbers. Notice the use of the `continue` keyword,

```
if number == 3 {
    continue;
}
```

Here, we skip the iteration when the number variable is equals `3`. As a result, we don't see `3` in the output.

---

## Working of continue Keyword in Rust

---

## Rust continue with Nested Loops

```
fn main() {
    let mut i = 1;
    
    // start of outer loop
    while i <= 5 {
        let mut j = 1;
            
        // start of inner loop
        while j <= 5 {
            j += 1;
            
            // condition to skip iteration of the inner loop
            if j == 3 {
                // move to the next iteration of the inner loop
                continue;
            }
            
            print!("*");
        }
        
        println!("");
        
        i += 1;
    }
}
```

**Output**

****
****
****
****
****

Here, we have used the `continue` keyword to skip an iteration of the inner while loop.

```
if j == 3 {
    // move to the next iteration of the inner loop
    continue;
}
```

When the value of the counter variable j reaches `3`, we skip the current inner `while` iteration and the `print!("*")` statement is skipped. As a result, we only see four asterisks (`****`) printed on every line of the screen.

---

## break and continue with loop

We can also use `break` and `continue` together to control the flow of a program. For example,

```
fn main() {
    let mut number = 0;

    loop {
        number += 1;

        // condition to skip the iteration
        if number == 3 {
            continue;
        }
        
        // condition to exit the loop
        if number > 5 {
            break;
        }
        
        println!("{}", number);
    }
}
```

**Output**

1
2
4
5

Here, the `continue` keyword,

```
if number == 3 {
    continue;
}
```

skips the iteration when the value of the number variable is `3`.

Similarly, the `break` keyword,

```
if number > 5 {
    break;
}
```

terminates the loop if the value of the number variable is greater than `5`.

- [](https://www.programiz.com/rust/break-continue#introduction)
- [](https://www.programiz.com/rust/break-continue#break)
- [](https://www.programiz.com/rust/break-continue#example-break)
- [](https://www.programiz.com/rust/break-continue#working-of-break)
- [](https://www.programiz.com/rust/break-continue#break-nested-loops)
- [](https://www.programiz.com/rust/break-continue#continue)
- [](https://www.programiz.com/rust/break-continue#example-continue)
- [](https://www.programiz.com/rust/break-continue#working-of-continue)
- [](https://www.programiz.com/rust/break-continue#continue-nested-loops)
- [](https://www.programiz.com/rust/break-continue#break-and-continue-with-loop)