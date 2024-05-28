# Rust Slice

A Rust slice is a data type used to access portions of data stored in collections like arrays, vectors and strings.

Suppose we have an array,

```
let numbers = [1, 2, 3, 4, 5];
```

Now, if we want to extract the **2nd** and **3rd** elements of this array. We can slice the array like this,

```
let slice = &array[1..3];
```

Here, let's look at the right-hand side of the expression,

- `&numbers` - specifies a reference to the variable `numbers` (not the actual value)
- `[1..3]` - is a notation for slicing the array from **start_index** `1` (inclusive) to **end_index** `3` (exclusive)

---

## Example: Rust Slice

```
fn main() {
    // an array of numbers
    let numbers = [1, 2, 3, 4, 5];
    
    // create a slice of 2nd and 3rd element
    let slice = &numbers[1..3];
    
    println!("array = {:?}", numbers);
    println!("slice = {:?}", slice);
}
```

**Output**

array = [1, 2, 3, 4, 5]
slice = [2, 3]

**Note:** A slice is not the actual data like integers or floats but a reference/pointer to the data block. That's why we have used the `&` symbol before the variable name.

---

## Omit Indexes of a Rust Slice

While slicing a data collection, Rust allows us to omit either the start index or the end index or both from its syntax.

```
&variable[start_index..end_index];
```

For example,

**1. Omitting the Start Index of a Slice**

```
fn main() {
    let numbers = [1, 2, 3, 4, 5];

    // omit the start index
    let slice = &numbers[..3];

    println!("array = {:?}", numbers);
    println!("slice = {:?}", slice);
}
```

**Output**

array = [1, 2, 3, 4, 5]
slice = [1, 2, 3]

Here, `&numbers[..3]` includes `..3` without the start index. This means the slice starts from index `0` and goes up to index `3` (exclusive). It is equivalent to `&numbers[0..3]`.

**2. Omitting the End Index of a Slice**

```
fn main() {
    let numbers = [1, 2, 3, 4, 5];

    // omit the end index
    let slice = &numbers[2..];

    println!("array = {:?}", numbers);
    println!("slice = {:?}", slice);
}
```

**Output**

array = [1, 2, 3, 4, 5]
slice = [3, 4, 5]

Here, `&numbers[2..]` includes `2..` without the end index. This means the slice starts from index `2` and goes up to index `5` (exclusive). It is equivalent to `&numbers[2..5]`.

**3. Omitting both Start and End Index of a Slice**

```
fn main() {
    let numbers = [1, 2, 3, 4, 5];
    
    // omit the start index and the end index
    // reference the whole array
    let slice = &numbers[..];

    println!("array = {:?}", numbers);
    println!("slice = {:?}", slice);
}
```

**Output**

array = [1, 2, 3, 4, 5]
slice = [1, 2, 3, 4, 5]

Here, `&numbers[..]` includes `..` without the start and end index. This means the slice starts from index `0` and goes up to index `5` (exclusive).

It is equivalent to `&numbers[0..5]` which will produce the same slice and will reference the whole array.

---

## Mutable Slice in Rust

We can create a mutable slice by using the `&mut` keyword.

```
let numbers = [1, 2, 3, 4, 5];
let slice = &mut numbers[1..4];
```

Once the slice is marked as mutable, we can change values inside the slice. Let's see an example,

```
fn main() {
    // mutable array
    let mut colors = ["red", "green", "yellow", "white"];
    
    println!("array = {:?}", colors);

    // mutable slice
    let sliced_colors = &mut colors[1..3];
    
    println!("original slice = {:?}", sliced_colors);

    // change the value of the original slice at the first index
    sliced_colors[1] = "purple";

    println!("changed slice = {:?}", sliced_colors);
}
```

**Output**

array = ["red", "green", "yellow", "white"]
original slice = ["green", "yellow"]
changed slice = ["green", "purple"]

Here, we have created a mutable array colors. Then, we have created a mutable slice sliced_colors with `&mut array[1..3]`.

Now, we can change the content of the mutable slice,

```
sliced_colors[1] = "purple"
```

We change the value of original slice sliced_colors at the 1st index from `"yellow"` to `"purple"`.

---

## Frequently Asked Questions

How to slice a string in Rust?

[](https://www.programiz.com/rust/string)

How to slice a vector in Rust?

[](https://www.programiz.com/rust/vector)

- [](https://www.programiz.com/rust/slice#introduction)
- [](https://www.programiz.com/rust/slice#example-slice)
- [](https://www.programiz.com/rust/slice#omit-indexes)
- [](https://www.programiz.com/rust/slice#mutable-slice)

[

  


](https://www.programiz.com/rust/array "Rust Array")