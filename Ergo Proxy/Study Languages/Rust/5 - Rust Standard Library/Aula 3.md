# Rust String

A string in Rust is a sequence of Unicode characters encoded in UTF-8. For example, `"Rust Programming"` is a string in which each character is a valid Unicode character. i.e. `"R"`, `"u"`, `"s"`, `"t"`, `" "`, and so on.

### Creating a String in Rust

We can create a string with a default value using the `String::from()` method. For example,

```
// create a string with a default value
let word = String::from("Hello, World!");
```

Here, we create a new string and assign it to the word variable. We also provide a default value of `"Hello, World!"`.

**Note:** A string is allocated in heap memory and is dynamic (resizable) in size. Hence, the size of string is unknown at compile time.

---

## Example: Creating a String in Rust

```
fn main() {
    // string creation using String::from() method
    let word = String::from("Hello, World!");

    println!("word = {}", word);
}
```

**Output**

word = Hello, World!

---

## Mutable String in Rust

We can create a mutable string in Rust by using the `mut` keyword before assigning a string to a variable. For example,

```
// mutable string
let mut word = String::from("cat");
```

We can make changes to this string.

Let's look at an example,

```
fn main() {
    let mut word = String::from("cat");
    
    println!("original string = {}", word);
    
    // push a new string at the end of the initial string 
    word.push_str(" dog");
    
    println!("changed string = {}", word);
}
```

**Output**

original string = cat
changed string = cat dog

Here, we create a mutable variable `word` that holds the string `"cat"`. We then push a new string to the end of the original string using `word.push_str(" dog");`.

---

## String Slicing in Rust

We can slice a string in Rust to reference a part of the string. String slicing allows us to reference a part (portion) of a string. For example,

```
fn main() {
    let word = String::from("Hello, World!");

    // slicing a string
    let slice = &word[0..5];

    println!("string = {}", word);
    println!("slice = {}", slice);
}
```

**Output**

string = Hello, World!
slice = Hello

Here, `&word[0..5]` is a notation for slicing the string stored in variable `word` from start index **0** (inclusive) to end index **5** (exclusive).

The `&` (ampersand) in the slicing syntax signifies that it is a string reference. It is not actual data.

Slicing is also used to access portions of data stored in arrays and vectors. To learn about Slice in Rust, visit [Rust Slice](https://www.programiz.com/rust/slice).

---

## Iterating over Strings

We can use the `chars()` method of the string type to iterate over a string. For example,

```
fn main() {
    let str = String::from("Hello");
    
    // Loop through each character in a string using chars() method
    for char in str.chars() {
        println!("{}", char);
    }
}
```

**Output**

H
e
l
l
o

Here, we iterate through all the characters using the `chars()` method and print each of them.

---

## Creating an Empty String with String::new()

We can create an empty string, using the `String::new()` method. For example,

```
// create an empty string
let mut word = String::new();
```

We can then append a string to the word variable using the `push_str()` method.

```
word.push_str("Hello, World!");
```

Here, we push the string `"Hello, World!"` to the empty string variable word.

---

### Example: Creating an Empty String with String::new()

```
fn main() {
    // create an empty string
    let mut word = String::new();
    
    println!("original string = {}", word);
    
    // append a string to the word variable
    word.push_str("Hello, World!");

    println!("changed string = {}", word);
}
```

**Output**

original string = 
changed string = Hello, World!

Here, we create an empty string with `String::new()` and append a string `"Hello, World!"` using `the push_str()` method to the original string.

---

## Frequently Asked Questions

What is the difference between String and str in Rust?

- [](https://www.programiz.com/rust/slice)

Does Rust support string indexing?