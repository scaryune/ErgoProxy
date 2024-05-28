# Rust loop

In programming, a loop is used to execute a code block multiple times. For example, to print a number 100 times, we use a loop instead of writing the print statement repeatedly.

In Rust, you can use three different keywords to execute a code block multiple times:

- loop
- while
- for

---

## Loop Expression

In Rust, we use the `loop` expression to indefinitely execute a block of code. If we use a `loop`, the code execution inside of the loop code block doesn't stop and runs forever.

The syntax of the `loop` expression is:

```
loop {
    // code to execute
}
```

Let's see an example.

```
fn main() {
    //  loop expression
    loop {
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

This example code will print **"Loop forever!"** indefinitely unless the user terminates the program. Since the loop runs forever, it is also known as an **infinite loop**.

---

## Terminating Loop in Rust

We use the `break` keyword to terminate a `loop`. For example,

```
fn main() {
    // initiate an infinite loop
    loop {
        println!("Loop forever!");
        
        // stop infinite loop
        break;
    }
}
```

**Output**

Loop forever!

Here, the `break` keyword terminates the loop. That is why the `println!` macro is executed only once.

**Note**: In Rust, we often use a `loop` and `break` together.

---

### Example: Print First 10 Natural Numbers using Loop

```
fn main() {
    let mut number = 0;
    
    // infinite loop starts here
    loop {
        number += 1;
        println!("{}", number);
        
        if number >= 10 {
            // exit the loop
            break;
        }
    }
}
```

**Output**

1
2
3
4
5
6
7
8
9
10

In the above example, we have used a `loop` expression to print the natural numbers. Here, the initial value of the number variable is `0`.

**Working of Loop**

The below table shows the working of the `loop` in each iteration.

|number|Inside loop|number >= 10|
|---|---|---|
|0|`number` is increased to **1**  <br>**1** is printed|`false`|
|1|`number` is increased to **2**  <br>**2** is printed|`false`|
|2|`number` is increased to **3**  <br>**3** is printed|`false`|
|3|`number` is increased to **4**  <br>**4** is printed|`false`|
|4|`number` is increased to **5**  <br>**5** is printed|`false`|
|5|`number` is increased to **6**  <br>**6** is printed|`false`|
|6|`number` is increased to **7**  <br>**7** is printed|`false`|
|7|`number` is increased to **8**  <br>**8** is printed|`false`|
|8|`number` is increased to **9**  <br>**9** is printed|`false`|
|9|`number` is increased to **10**  <br>**10** is printed|`true` (loop terminates)|

Hence, we see numbers **1** to **10** printed on the screen.

---

## Working of loop and break in Rust

![Working of loop and break in Rust](https://www.programiz.com/sites/tutorial2program/files/working-of-loop-in-rust.png "Working of loop and break in Rust")

Working of loop and break in Rust

To learn more about the `break` keyword, visit [_Rust break and continue_](https://programiz.com/rust/break-continue).