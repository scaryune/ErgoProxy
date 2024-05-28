# Rust Closure

In Rust, closures are functions without names. They are also known as anonymous functions or lambdas.

### Defining a Closure in Rust

Here's how we create a closure in Rust,

```
// define a closure to print a text
let print_text = || println!("Defining Closure");
```

In the above example, we have created a closure that prints the text "**Defining Closure**". Here,

- `print_text` - variable to store the closure
- `||` - start of a closure
- `println!("Defining Closure")` - body of the closure

### Calling Closure

Once a closure is defined, we need to call it just like calling a function. To call a closure, we use the variable name to which the closure is assigned. For example,

```
// define a closure to print a text
let print_text = || println!("Defining Closure");

// call the closure
print_text();
```

Here, `print_text()` calls the closure.

---

## Example: Closure in Rust

```
fn main() {
    // closure that prints a text
    let print_text = || println!("Hello, World!");
    
    print_text(); 
}
```

**Output**

Hello, World!

In the above example, we have defined a closure and stored it in the print_text variable. We then call the closure using `print_text()`.

---

## Rust Closure with Parameters

In Rust, we can also pass parameters to a closure. For example,

```
// define closure to add 1 to an integer
let add_one = |x: i32| x + 1;
```

Here,

- `let add_one` - is the name of the variable to store the the closure
- `|x: i32|` - is the parameter and its type that we pass to the closure
- `x + 1;` - is the body of the closure which returns `x + 1`

If we create a closure with parameters, we need to also pass the value while calling the closure.

```
// call the closure with value 2
add_one(2);
```

---

### Example: Rust Closure with Parameter

```
fn main() {
    // define a closure and store it in a variable
    let add_one = |x: i32| x + 1;
    
    // call closure and store the result in a variable
    let result = add_one(2);
    
    println!("Result = {}", result);
}
```

**Output**

Result = 3

In the above example, we have defined a closure and binded it to the add_one variable. We then call the closure with `add_one(2)` and bind the return value to the result variable.

Here's how the program works,

![Working of closure with parameter in Rust](https://www.programiz.com/sites/tutorial2program/files/working-of-closure-with-parameter-in-rust.png "Working of closure with parameter in Rust")

Working of closure with parameter in Rust

---

## Multi-line Closure in Rust

We can also include multiple statements inside a closure. In this case, we enclose those statements using curly braces `{}`.

Let's look at an example.

```
fn main() {
    // define a multi-line closure
    let squared_sum = |x: i32, y: i32| {
    
        // find the sum of two parameters
        let mut sum: i32 = x + y;
        
        // find the squared value of the sum
        let mut result: i32 = sum * sum;
        
        return result;
    };
    
    // call the closure
    let result = squared_sum(5, 3);
    
    println!("Result = {}", result);
}
```

**Output**

Result = 64

In the above example, we have created a closure that takes two parameters: `x` and `y`. Inside the closure, we add `x` and `y` and assign the result to the sum variable.

Finally, we have computed the square of sum and returned the `result`.

Here, code inside the opening and closing curly braces, `{}` denotes the body of the closure.

---

## Closure Environment Capturing in Rust

Closure has a unique feature that allows it to capture the environment. This means the closure can use the values in its scope. For example,

```
fn main() {
    let num = 100;
    
    // A closure that captures the num variable
    let print_num = || println!("Number = {}", num);
    
    print_num(); 
}
```

**Output**

Number = 100

Here, the closure bound to print_num uses the variable num which was not defined in it. This is known as closure environment capturing.

---

## Closure Environment Capturing Modes in Rust

Environment capturing of closures can be of 3 different modes based on the variable and the closure definition.

1. Variable is not modified inside closure
2. Variable is modified inside closure
3. Variable is moved inside closure

Let's look at each of these modes of environment capturing.

**1. Variable is not modified inside closure**

```
fn main() {
    let word = String::from("Hello");
    
    // immutable closure
    let print_str = || {
        println!("word = {}", word);
    };

    // immutable borrow is possible outside the closure
    println!("length of word = {}", word.len());
    
    print_str();
}
```

**Output**

word = Hello
length of word = 5

Here, the variable word is not modified inside the closure print_str. As the variable is immutable by default, we can make any number of immutable references of word inside the closure. Notice that the closure variable print_str is also immutable.

This mode of capture is also known as **Capture by Immutable Borrow**.

**2. Variable is modified inside closure**

```
fn main() {
    let mut word = String::from("Hello");
    
    // mutable closure
    let mut print_str = || {
        // value of word is changed here
        word.push_str(" World!");
        println!("word = {}", word);
    };
     
     // cannot immutable borrow because the variable is borrowed as mutable inside the closure
     // println!("length of word = {}", word.len());
    
    print_str();

    // can immutable borrow because the closure has been already used
    println!("length of word = {}", word.len());
}
```

**Output**

word = Hello World!
length of word = 12

Here, the variable word is modified inside the closure print_str with `word.push_str("World!");`. Thus, we have to make the variable word mutable as well as the closure variable print_str. This means no other references of the word variable can exist unless the closure is used.

This mode of capture is also known as **Capture by Mutable Borrow**.

**3. Variable is moved inside closure**

```
fn main() {
    let word = String::from("Hello");

    // immutable closure
    let print_str = || {
        // word variable is moved to a new variable
        let new_word = word;
        println!("word = {}", new_word);
    };

    print_str();

    // cannot immutable borrow because word variable has moved inside closure
    // println!("length of word = {}", word.len());
}
```

**Output**

word = Hello

Here, we move the variable word to a new variable new_word inside the closure. As the variable is moved, we cannot use it anywhere else except for inside the closure.

This mode of capture is also known as **Capture by Move**.

---

## Frequently Asked Questions

What is the difference between functions and closures in Rust?

How to use closure as a function argument in Rust?