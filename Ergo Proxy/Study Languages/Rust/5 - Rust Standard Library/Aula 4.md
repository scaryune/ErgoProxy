# Rust HashMap

The Rust HashMap data structure allows us to store data in **key-value pairs**. Here are some of the features of hashmap:

- Each value is associated with a corresponding key.
- Keys are unique, whereas values can duplicate.
- Values can be accessed using their corresponding keys.

---

## Creating a HashMap in Rust

HashMap is part of the Rust standard collections library, so we must include the `HashMap` module in our program to use it.

```
use std::collections::HashMap;
```

We can import the `HashMap` module using the `use` declaration. It should be at the top of the program.

Now, we can create a hashmap using the `new()` method in the `HashMap` module. For example,

```
let mut info: HashMap<i32, String> = HashMap::new();
```

Here,

- `let mut info` - declares a mutable variable `info`
- `HashMap<i32, String>` - type of the HashMap where the key is a Integer and the value is a String
- `HashMap::new()` - creates a new HashMap

---

### Example: Creating a HashMap

```
// import HashMap from Rust standard collections library
use std::collections::HashMap;

fn main() {
    // create a new HashMap
    let mut info: HashMap<i32, String> = HashMap::new();
    
    println!("HashMap = {:?}", info);
}
```

**Output**

HashMap = {}

Here, we create an empty HashMap and print it to the screen.

**Note:** We use `:?` in the `println!` macro to print a HashMap.

---

## HashMap Operations in Rust

The `HashMap` module provides various methods to perform basic operations in a hashmap.

- Add Elements
- Access Values
- Remove Elements
- Change Elements

---

## 1. Add Elements to a HashMap in Rust

We can use the `insert()` to add an element (key-value pairs) to a hashmap. For example,

```
let mut fruits: HashMap<i32, String> = HashMap::new();

// insert elements to hashmap
fruits.insert(1, String::from("Apple"));
fruits.insert(2, String::from("Banana"));
```

Here, we insert two key-value pairs in the `HashMap` bound to the variable `fruits`. The `String::from()` method here creates a value of `String` type.

**Note:** Adding a new key-value to the HashMap is only possible because of the `mut` variable declaration.

---

### Example: Add Elements to a HashMap

```
use std::collections::HashMap;

fn main() {
    let mut fruits: HashMap<i32, String> = HashMap::new();
    
    // add key-value in a hashmap
    fruits.insert(1, String::from("Apple"));
    fruits.insert(2, String::from("Banana"));
    
    println!("fruits = {:?}", fruits);
}
```

**Output**

fruits = {1: "Apple", 2: "Banana"}

---

## 2. Access Values in a HashMap in Rust

We can use the `get()` to access a value from the given hashmap. For example,

```
let mut fruits: HashMap<i32, String> = HashMap::new();

fruits.insert(1, String::from("Apple"));
fruits.insert(2, String::from("Banana"));

let first_fruit = fruits.get(&1);
```

Here, we get a value out of the hashmap using the key `&1` and the `get()` method.

We use the ampersand(`&`) and the key (`&1`) as the argument because `get()` returns us a reference of the value. It is not the actual value in the HashMap.

---

### Example: Access Values in a HashMap

```
use std::collections::HashMap;

fn main() {
    let mut fruits: HashMap<i32, String> = HashMap::new();
    
    // insert elements in a hashmap
    fruits.insert(1, String::from("Apple"));
    fruits.insert(2, String::from("Banana"));
    
    // access values in a hashmap
    let first_fruit = fruits.get(&1);
    let second_fruit = fruits.get(&2);
    let third_fruit = fruits.get(&3);
    
    println!("first fruit = {:?}", first_fruit);
    println!("second fruit = {:?}", second_fruit);
    println!("third fruit = {:?}", third_fruit);
}
```

**Output**

first fruit = Some("Apple")
second fruit = Some("Banana")
third fruit = None

Notice that we use the ampersand(`&`) and the key (`&1`, `&2`) as an argument to the `get()` method.

```
let first_fruit = fruits.get(&1);
let second_fruit = fruits.get(&2); 
```

The output of the `get()` method is an `Option` enum which means that if the key passed as an argument matches, it returns `Some` value, and if it doesn't, it returns `None`.

In the above example, `let third_fruit = fruits.get(&3)` returns `None` because the key `&3` doesn't match anything that's in the hashmap.

---

## 3. Remove Elements from a HashMap in Rust

We can remove elements from a hashmap by providing a key to the `remove()` method. For example,

```
let mut fruits: HashMap<i32, String> = HashMap::new();

fruits.insert(1, String::from("Apple"));
fruits.insert(2, String::from("Banana"));

fruits.remove(&1);
```

Here, we remove a value from the hashmap using the key and the `remove()` method.

---

### Example: Remove Elements in a HashMap

```
use std::collections::HashMap;

fn main() {
    let mut fruits: HashMap<i32, String> = HashMap::new();
    
    // insert values in a hashmap
    fruits.insert(1, String::from("Apple"));
    fruits.insert(2, String::from("Banana"));
    
    println!("fruits before remove operation = {:?}", fruits);

    // remove value in a hashmap
    fruits.remove(&1);
    
    println!("fruits after remove operation = {:?}", fruits);
}
```

**Output**

fruits before remove operation = {1: "Apple", 2: "Banana"}
fruits after remove operation = {2: "Banana"}

Here, we remove an element in the hashmap with key `&1` using the `remove()` method.

---

## 4. Change Elements of a HashMap in Rust

We can change/update elements of a hashmap by using the `insert()` method. For example,

```
let mut fruits: HashMap<i32, String> = HashMap::new();

// insert values in the hashmap
fruits.insert(1, String::from("Apple"));
fruits.insert(2, String::from("Banana"));

// update the value of the element with key 1
fruits.insert(1, String::from("Mango"));
```

Here, the final insert expression updates the initial value of the element with the key of **1**.

---

### Example: Change Elements of a HashMap

```
use std::collections::HashMap;

fn main() {
    let mut fruits: HashMap<i32, String> = HashMap::new();
    
    // insert values in a hashmap
    fruits.insert(1, String::from("Apple"));
    fruits.insert(2, String::from("Banana"));
    
    println!("Before update = {:?}", fruits);
    
    // change value of hashmap with key of 1
    fruits.insert(1, String::from("Mango"));
    
    println!("After update = {:?}", fruits);
}
```

**Output**

Before update = {1: "Apple", 2: "Banana"}
After update = {1: "Mango", 2: "Banana"}

---

## Other Methods of Rust HashMap

Besides the basic methods, here are some more commonly used HashMap methods.

|Method|Description|
|---|---|
|`len()`|Returns the length of the HashMap.|
|`contains_key()`|Checks if a value exists for the specified key.|
|`iter()`|Returns an iterator over the entries of a HashMap.|
|`values()`|Returns an iterator over the values of a HashMap.|
|`keys()`|Returns an iterator over the keys of a HashMap.|
|`clone()`|Creates and returns a copy of the HashMap.|

---

### Example: Rust HashMap Methods

```
use std::collections::HashMap;

fn main() {
    let mut fruits: HashMap<i32, String> = HashMap::new();
    
    fruits.insert(1, String::from("Apple"));
    fruits.insert(2, String::from("Banana"));
    
    // loop and print values of hashmap using values() method
    for fruit in fruits.values() {
        println!("{}", fruit)
    }
    
    // print the length of hashmap using len() method
    println!("Length of fruits = {}", fruits.len());
}
```

**Output**

Apple
Banana
Length of fruits = 2

Here, we use the `values()` method of the HashMap to loop through its values and `len()` method of the hashmap to find its length.

- [](https://www.programiz.com/rust/hashmap#introduction)
- [](https://www.programiz.com/rust/hashmap#create-hashmap)
- [](https://www.programiz.com/rust/hashmap#operations)
- [](https://www.programiz.com/rust/hashmap#add-elements)
- [](https://www.programiz.com/rust/hashmap#access-values)
- [](https://www.programiz.com/rust/hashmap#remove-elements)
- [](https://www.programiz.com/rust/hashmap#change-elements)
- [](https://www.programiz.com/rust/hashmap#methods)