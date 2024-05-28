# Rust while Loop

We use the `while` loop to execute a code block till the condition is `true`. The syntax for the `while` expression is:

```
while condition {
    // code block
}

// code block outside while loop
```

Here, the `while` loop evaluates the **condition** before proceeding further.

If the **condition** evaluates to:

- `true` - the code block inside the while loop is executed and the condition is evaluated again

- `false` - the loop terminates and the code block outside the while loop is executed

---

### Example: Rust while Loop

```
fn main() {
    let mut counter = 1;

    // usage of while loop
    while counter < 6 {
        println!("{}", counter);
        
        counter += 1;
    }
}
```

**Output**

1
2
3
4
5

In the example above, we have a **condition**:

```
while counter < 6 {
    // code block
}
```

Here, the loop keeps running till the counter variable is less than `6`. Inside the loop, we are increasing the value of the counter by `1`.

After 5th iteration, the value of counter will be `6`, so the **condition**, `counter < 6` becomes `false` and the loop is terminated.

**Note**: `while` expressions are generally used in conjunction with counter variables that help exit the loop after certain conditions.

---

## Working of while Expression in Rust

![Working of while Expression in Rust](https://www.programiz.com/sites/tutorial2program/files/working-of-while-expression-in-rust.png "Working of while Expression in Rust")

Working of while Expression in Rust

---

## Infinite while Loop

You can write a loop that never ends using the `while` expression. Let's look at an example,

```
fn main() {
    let counter = 1;

    // while loop with a condition that always evaluates to true
    while counter < 6 {
        println!("Loop forever!");
   }
}
```

**Output**

Loop forever!
Loop forever!
Loop forever!
.
.
.

This example code will print "**Loop forever!**" indefinitely because the **condition** `counter < 6` always evaluates to `true`. It is because we never increase the value of the counter variable inside the loop. Thus, this program will run until the user terminates the program.

**Note:** You can use the `break` keyword to terminate any kind of loop in Rust.

---

### Example: Multiplication Table Using while Loop

```
fn main() {
    // variable to print multiplication table for
    let i = 2;
    
    // counter variable that starts at 1
    let mut j = 1;
    
    // while loop that runs for 10 iterations
    while j <= 10 {
        // multiply i and j
        let mult = i * j;
        
        // print multiplication result on each iteration
        println!("{} * {} = {}", i, j, mult);

        // increase value of counter variable j
        j += 1;
    }
}
```

**Output**

2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20

---

## Nested while Loop

We can use a `while` loop inside the body of another `while` loop. This is known as a nested `while` loop. A nested `while` loop looks like:

```
while outer_condition {
    // outer code block 1

    while inner_condition {
        // inner code block
    }

    // outer code block 2
}
```

Let's print a pattern using a nested `while` loop,

```
fn main() {
    // outer loop counter
    let mut i = 1;
    
    // outer loop
    while i <= 5 {
        // inner loop counter
        let mut j = 1;
        
        // inner loop
        while j <= 5 {
            print!("*");
            
            // increase inner loop counter
            j += 1;
        }
        
        println!("");
        
        // increase outer loop counter
        i += 1;
    }
}
```

**Output**

*****
*****
*****
*****
*****

In the above example,

- The outer `while` loop iterates `5` times
- The inner `while` loop inside of the outer `while` loop also iterates `5` times
- The inner `while` loop prints an asterisk(`*`) → `print!(*)` on every iteration
- The inner `while` loop stops when the counter variable j reaches to `6` as the **inner condition** evaluates to `false`
- The outer `while` loop prints a new line → `println!("")` on every iteration and goes to the next iteration which will initiate the inner `while` loop again
- The outer `while` loop stops when the counter variable i reaches to `6` as the **outer condition** evaluates to `false`

- [](https://www.programiz.com/rust/while-loop#introduction)
- [](https://www.programiz.com/rust/while-loop#example-while-loop)
- [](https://www.programiz.com/rust/while-loop#working-of-while-expression)
- [](https://www.programiz.com/rust/while-loop#infinite-while-loop)
- [](https://www.programiz.com/rust/while-loop#example-multiplication-table)
- [](https://www.programiz.com/rust/while-loop#nested-while-loops)