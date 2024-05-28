# Rust Tuple

A tuple in Rust allows us to store values of different data types. For example,

```
let tuple = ('Hello', 5, 3.14);
```

Here, we have used the small bracket `( )` to create a tuple and it is able to store a string value, `Hello`, an integer value, `5`, and a floating-point value `3.14` together.

**Note**: In Rust, tuples have a fixed size and cannot grow or shrink after they have been created.

---

## Creating a Tuple in Rust

In Rust, we can create a tuple in two different ways:

1. Tuple with data type
2. Tuple without data type

Let's understand each of them in detail.

---

## Rust Tuple with Data Type

While creating a tuple, we can mention the type of data it is storing. For example,

```
// create a tuple with data type
let student_info: (&str, u8, f32) = ("Ricky", 21, 3.56);
```

Here,

- `let student_info: (&str, u8, f32)` - specifies the variable name and the data types of the tuple elements
- `("Ricky", 21, 3.56)` - specifies the elements of the tuple

### Example: Tuple with Data Type

```
fn main() {
    // initialization of tuple with data type
    let tuple: (&str, f32, u8) = ("Rust", 3.14, 100);
    
    println!("Tuple contents = {:?}", tuple);
}
```

**Output**

Tuple contents = ("Rust", 3.14, 100)

**Note:** We use the `:?` in the `println!` function to print an entire tuple.

---

## Tuple without Data Type in Rust

We can create a tuple without mentioning the type of data it is storing. The Rust compiler can automatically detect and set the data type. For example,

```
// create a tuple without data type
let student_info = ("Ricky", 21, 3.56);
```

Here,

- `let student_info` - specifies the variable name of the tuple
- `("Ricky", 21, 3.56)` - specifies the elements of the tuple

### Example: Tuple without Data Types

```
fn main() {
    // initialization of tuple without data type
    let tuple = ("Rust", "fun", 100);

    println!("Tuple contents = {:?}", tuple);
}
```

**Output**

Tuple contents = ("Rust", "fun", 100)

---

## Accessing Elements in a Tuple

Each element in a tuple is associated with a unique sequence of numbers. This number is known as the **tuple index** or just **index**.

Suppose we have a tuple,

```
let random_tuple = ("Hello", 200, 3.14);
```

The tuple indexes of the random_tuple look like,

![Tuple index Visualization in Rust](https://www.programiz.com/sites/tutorial2program/files/tuple-index-visualization-in-rust.png "Tuple index Visualization in Rust")

Tuple index Visualization in Rust

In Rust, we can access individual tuple elements using their corresponding tuple indexes and the dot `.` notation. For example,

- `random_tuple.0` - access the element at index 0 (first element)
- `random_tuple.1` - access the element at index 1 (second element)
- `random_tuple.2` - access the element at index 2 (third element)

### Example: Access Tuple Elements

```
fn main() {
    let random_tuple = ("Hello", 200, 3.14);

    // accessing tuple element at index 0
    println!("Value at Index 0 = {}", random_tuple.0);
    
    // accessing tuple element at index 1
    println!("Value at Index 1 = {}", random_tuple.1);
    
    // accessing tuple element at index 2
    println!("Value at Index 2 = {}", random_tuple.2);
}
```

**Output**

Value at Index 0 = Hello
Value at Index 1 = 200
Value at Index 2 = 3.14

**  
Note:** The tuple index always starts at 0; hence the first element of the tuple is at position 0, not 1.

---

## Mutable Tuple

In Rust, a tuple is immutable, which means we cannot change its elements once it is created.

However, we can create a mutable array by using the `mut` keyword before assigning it to a variable. For example,

```
// create a mutable tuple 
let mut mountains = ("Everest", 8848, "Fishtail", 6993);
```

Now, we can make changes to this tuple.

Let's take a look at an example,

```
fn main() {
    // initialize a mutable tuple
    let mut mountain_heights = ("Everest", 8848, "Fishtail", 6993);
    
    println!("Original tuple = {:?}", mountain_heights);
    
    // change 3rd and 4th element of a mutable tuple
    mountain_heights.2 = "Lhotse";
    mountain_heights.3 = 8516;
    
    println!("Changed tuple = {:?}", mountain_heights);
}
```

**Output**

Original tuple = ("Everest", 8848, "Fishtail", 6993)
Changed tuple = ("Everest", 8848, "Lhotse", 8516)

Here, we create a mutable tuple named mountain_heights. We then change its 3rd and 4th element, the 2nd and 3rd tuple index.

```
mountain_heights.2 = "Lhotse";
mountain_heights.3 = 8516;
```

**Note:** You can only change the element of a tuple to the same type as when it was created. Changing data types is not allowed after tuple creation.

---

## Destructuring a Tuple

We can break down tuples into smaller variables in Rust, known as **destructuring**.

Suppose we have a tuple,

```
let tuple = ("John Doe", 18, 178);
```

Now, we can perform destructuring using,

```
let (name, age, height) = tuple;
```

Now, we access the `name`, `age` and `height` variables directly without using tuple indexes.

- `name` instead of `tuple.0`
- `age` instead of `tuple.1`
- `height` instead of `tuple.2`

You can name the variables as you like while destructuring a tuple.

**Note**: Destructuring a tuple is also known as **tuple unpacking**.

---

### Example: Destructuring a Tuple

```
fn main() {
    let mixture = ("Hello, World!", 16, 2.71828);
    
    // destructuring a tuple
    let (message, number, float) = mixture;
    
    println!("message = {}", message);
    println!("number = {}", number);
    println!("float = {}", float);
}
```

**Output**

message = Hello, World!
number = 16
float = 2.71828

Here, we destructure the tuple `mixture` to variables message, number and float.

```
let (message, number, float) = mixture;
```

Finally, we print these variables to the screen.

- [](https://www.programiz.com/rust/tuple#introduction)
- [](https://www.programiz.com/rust/tuple#creating)
- [](https://www.programiz.com/rust/tuple#tuple-with-data-type)
- [](https://www.programiz.com/rust/tuple#tuple-without-data-type)
- [](https://www.programiz.com/rust/tuple#accessing-elements)
- [](https://www.programiz.com/rust/tuple#mutable-tuple)
- [](https://www.programiz.com/rust/tuple#destructuring-a-tuple)