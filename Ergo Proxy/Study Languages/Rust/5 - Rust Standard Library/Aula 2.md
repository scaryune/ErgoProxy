# Rust Vector

Vector is a dynamic (resizable) data structure that can store a list of elements of the same type. Being a resizable data structure, vectors can grow and shrink at runtime.

### Create a Vector in Rust

In Rust, we can create a vector using the `vec!` macro. For example,

```
let v = vec![1, 2, 3];
```

Here, we are creating a vector using the `vec!` macro with some initial values.

- `let v` - the name of the variable
- `vec![1, 2, 3]` - initialize a vector with integer values **1**, **2**, **3**

By looking at the type of the values provided to the macro, Rust will automatically set the vector type. For example, the vector type of the above vector is `Vec<i32>`.

We can also define the vector type ourselves using the `vec!` macro.

```
let v: Vec<u8> = vec![1, 2, 3];
```

Here, we are creating a vector with type `u8`, which has elements **1**, **2** and **3**.

---

### Example: Creating a Vector in Rust

```
fn main() {    
    // vector creation with vec! macro
    let v = vec![1, 2, 3];
    
    println!("v2= {:?}", v);
}
```

**Output**

v = [1, 2, 3]

**Note:** Since Rust Vectors implement the Debug trait, We can use `:?` in the `println!` macro to print a vector.

---

## Accessing Elements of a Vector in Rust

Each element in a vector is associated with a unique sequence of numbers. This number is known as the **vector index**.

We can access elements of a vector using the vector index. Suppose we have a vector of colors.

```
let colors = vec!["blue", "red", "green"];
```

Here's what the indexes for this vector look like,

![Vector index visualization in Rust](https://www.programiz.com/sites/tutorial2program/files/vector-index-visualization-in-rust.png "Vector index visualization in Rust")

Vector index visualization in Rust

We can access individual vector elements using their corresponding vector indexes. For example,

- `colors[0]` - access the element at **index 0** (first element)
- `colors[1]` - access the element at **index 1** (second element)
- `colors[2]` - access the element at **index 2** (third element)

**  
Note:** The vector index always starts at **0**; hence the first element of the array is at position **0**, not **1**.

---

### Example: Accessing Elements of a Vector using Vector Index

```
fn main() {
    let colors = vec!["blue", "red", "green"];
    
    // method 1: access vector elements using vector index
    println!("first color = {}", colors[0]);
    println!("second color = {}", colors[1]);
    println!("third color = {}", colors[2]);
}
```

**Output**

first color = blue
second color = red
third color = green

---

## Accessing Elements of a Vector using the get() method in Rust

We can also access the element of the vector with the `get()` method and the index of the element.

Suppose we have a vector of colors:

```
let colors = vec!["blue", "red", "green"];
```

We can access the elements of this vector using `get()`. The `get()` method does not directly return the vector element but an enum with type `Option<T>`. The result is either a `Some(T)` or `None`.

- `colors.get(0)` - returns `Some` value at **index 0**
- `colors.get(1)` - returns `Some` value at **index 1**
- `colors.get(2)` - returns `Some` value at **index 2**

The advantage of using the `get()` method over just using the vector index to access the element directly is that it will not error if the vector index is out of range.

Suppose we go out of the vector index range; then `get()` will return `None`. For example,

`colors.get(3)` will return `None`

---

### Example: Accessing Elements of a Vector using `get()`

```
fn main() {
    let colors = vec!["blue", "red", "green"];
    
    // method 2: access vector elements using get() method and vector index
    println!("first color = {:?}", colors.get(0));
    println!("second color = {:?}", colors.get(1));
    println!("third color = {:?}", colors.get(2));
}
```

**Output**

first color = Some("blue")
second color = Some("red")
third color = Some("green")

As we can see, the output returns a value `Some("blue")`, `Some("red")` and `Some("green")` of the `Option<T>` type.

To get the exact value from the `Option<T>` type, we need to unwrap the value. To learn about unwrap, visit [_Rust unwrap() and expect()_](https://www.programiz.com/rust/unwrap-and-expect).

---

## Adding Values to a Vector in Rust

We can add values to a Vector by creating a mutable vector in Rust. We can use the `mut` keyword before assigning a vector to a variable to make it mutable. For example,

```
// mutable vector
let mut v = vec![2, 4, 6, 8, 10];
```

We can add values to this vector using the `push()` method.

Let's look at an example.

```
fn main() {
    let mut even_numbers = vec![2, 4, 6, 8, 10];
    
    println!("original vector = {:?}", v);
    
    // push values at the end of the vector
    even_numbers.push(12);
    even_numbers.push(14);
    
    println!("changed vector = {:?}", v);
}
```

**Output**

original vector = [2, 4, 6, 8, 10]
changed vector = [2, 4, 6, 8, 10, 12, 14]

Here, we push values to the vector with the `push()` method. It is only possible because the variable holding the vector even_numbers is mutable.

```
even_numbers.push(12);
even_numbers.push(14);
```

As a result, the final vector includes **12** and **14** with the default elements.

---

## Removing Values from a Vector in Rust

We can remove values from a vector by making it mutable and with the `remove()` method. For example,

```
fn main() {
    let mut even_numbers = vec![2, 4, 6, 8, 10];
    
    println!("original vector = {:?}", even_numbers);
    
    // remove value from the vector in its second index
    even_numbers.remove(2);
    
    println!("changed vector = {:?}", even_numbers);
}
```

**Output**

original vector = [2, 4, 6, 8, 10]
changed vector = [2, 4, 8, 10]

Here, we remove the value in the second index with the `even_numbers.remove(2)` method. Thus, the final result does not include the value **6** in the vector.

**Note:** Removing an element will shift all other values beyond that element by one (**-1** index).

---

## Looping Through a Vector in Rust

We can use the `for` loop to iterate through a vector. For example,

```
fn main() {
    let colors = vec!["blue", "red", "green"];
    
    let mut index = 0;
    
    // loop through a vector to print its index and value
    for color in colors {
        println!("Index: {} -- Value: {}", index, color);
        index = index + 1;
    }
}
```

**Output**

Index: 0 -- Value: blue
Index: 1 -- Value: red
Index: 2 -- Value: green

In the above example, we have used the for loop.

```
for color in colors {
    ...
}
```

Here, the loop runs **3** times (total number of vector elements).

In each iteration of the loop, the value of `color` will be set to **blue**, **red**, and **green,** respectively. Similarly, we have used an index variable to represent the index of each vector element.

**Note**: A for loop should preferred over the `[]` operator to access vector elements because access by `[]` incurs run-time cost due to out of bounds checks.

---

## Creating a Vector using `Vec::new()` Method

Alternatively, we can create an empty vector using the `Vec::new()` method. For example,

```
let v: Vec<i32> = Vec::new();
```

Here, we are creating an empty vector to hold values of type `i32`.

- `let v` - the name of the variable
- `Vec<i32>` - type of the vector, where `i32` is the data type of all elements in the vector
- `Vec::new()` - initialize an empty vector with the `new()` method

---

### Example: Creating a Vector using Vec::new()

```
fn main() {
    // vector creation with Vec::new() method
    let mut v: Vec<i32> = Vec::new();

    // push values to a mutable vector
    v.push(10);
    v.push(20);

    println!("v = {:?}", v);
}
```

**Output**

v = [10, 20]

Here, we create a mutable vector with `Vec::new()` and push values to it using the `push()` method of the vector.