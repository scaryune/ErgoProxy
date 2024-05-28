# Rust HashSet

HashSet implements the set data structure in Rust. Just like a set, it allows us to store values without duplicates.

### Creating a HashSet in Rust

Hashset is part of the Rust standard collections library, so we must include the `HashSet` module in our program.

```
use std::collections::HashSet;
```

We have imported the `HashSet` module using the `use` declaration. It should be at the top of the program.

Now, we can create a hashset using the `new()` method of the `HashSet` module. For example,

```
let mut color: HashSet<String> = HashSet::new();
```

Here,

- `let mut color` - declares a mutable variable `color`
- `HashSet<String>` - type of the hashset where the values are of type `String`
- `HashSet::new()` - creates a new hashset

---

### Example: Creating a HashSet

```
// import HashSet from Rust standard collections library
use std::collections::HashSet;

fn main() {
    // create a new HashSet
    let mut color: HashSet<String> = HashSet::new();
    
    println!("HashSet = {:?}", color);
}
```

**Output**

HashSet = {}

Here, we create an empty `HashSet` and print it to the screen.

**Note:** We use `:?` in the `println!` macro to print a hashset.

---

## HashSet Operations in Rust

The `HashSet` module provides various methods to perform basic operations in a hashset.

- Add Values
- Check Values
- Remove Values
- Iterate over Values

---

## 1. Add Values to a HashSet in Rust

We can use the `insert()` method to add an element to the hashset. For example,

```
let mut colors: HashSet<&str> = HashSet::new();

// insert elements to hashset
colors.insert("Red");
colors.insert("Yellow");
```

Here, we insert two values in the `HashSet` bound to the variable `colors`.

**Note:** Adding a new value to the hashset is only possible because of the `mut` variable declaration.

---

### Example: Add Values to a HashSet

```
use std::collections::HashSet;

fn main() {
    let mut colors: HashSet<&str> = HashSet::new();
    
    // insert values in a HashSet
    colors.insert("Red");
    colors.insert("Yellow");
    colors.insert("Green");

    println!("colors = {:?}", colors);
}
```

**Output**

colors = {"Green", "Yellow", "Red"}

Here, the output has the elements in a different order. It's because a hashset doesn't preserve the insertion order of values.

---

## 2. Check Value is Present in a HashSet in Rust

We use the `contains()` method to check if a value is present in a hashset. The method returns true if the specified element is present in the hashset, otherwise returns false.

Let's see an example,

```
use std::collections::HashSet;

fn main() {
    let mut colors: HashSet<&str> = HashSet::new();

    colors.insert("Red");
    colors.insert("Yellow");

    println!("colors = {:?}", colors);

    // check for a value in a HashSet
    if colors.contains("Red") {
        println!("We have the color \"Red\" in the HashSet.")
    }
}
```

**Output**

colors = {"Red", "Yellow"}
We have the color "Red" in the HashSet.

In the above example, we have used the `colors.contains("Red")` as a condition to the `if` statement.

Here, the element `Red` is present inside the hashset, so the condition is true. Hence, we get the desired output.

---

## 3. Remove Values from a HashSet in Rust

We can use the `remove()` method to remove the specified element from the hashset. For example,

```
use std::collections::HashSet;

fn main() {
    let mut colors: HashSet<&str> = HashSet::new();

    colors.insert("Red");
    colors.insert("Yellow");
    colors.insert("Green");

    println!("colors before remove operation = {:?}", colors);

    // remove value from a HashSet
    colors.remove("Yellow");
    
    println!("colors after remove operation = {:?}", colors);
}
```

**Output**

colors before remove operation = {"Yellow", "Green", "Red"}
colors after remove operation = {"Green", "Red"}

In the above example, we have used

```
colors.remove("Yellow");
```

to remove the element `Yellow` from the hashset.

---

## 4. Iterate over Values of a HashSet in Rust

We can use the [Rust for Loop](https://www.programiz.com/rust/for-loop) to iterate over values of a hashset. For example,

```
use std::collections::HashSet;

fn main() {
    let mut colors: HashSet<&str> = HashSet::new();
    
    colors.insert("Red");
    colors.insert("Yellow");
    colors.insert("Green");

    // iterate over a hashset
    for color in colors {
        // print each value in the hashset
        println!("{}", color);
    }
}
```

**Output**

Red
Green
Yellow

Here, we iterate over the hashset named colors and print each element.

---

## HashSet with Default Values in Rust

We can also create a hashset with default values using the `from()` method when creating it. For example,

```
use std::collections::HashSet;

fn main() {
    // Create HashSet with default set of values using from() method
    let numbers = HashSet::from([2, 7, 8, 10]);
    
    println!("numbers = {:?}", numbers);
}
```

**Output**

numbers = {8, 2, 7, 10}

Here, we create a hashset using the `HashSet::from()` method with default values and print it to the screen.

---

## Other Methods of Rust HashSet

Besides the basic methods, here are some more commonly used HashSet methods.

|Method|Description|
|---|---|
|`len()`|returns the length of a hashset|
|`is_empty()`|checks if the hashset is empty|
|`clear()`|removes all elements from the hashset|
|`drain()`|returns all the elements as an iterator and clears the hashset|

---

## Set Operations

The HashSet module also provides various methods used to perform different set operations.

## 1. Union of two Sets

We can use the `union()` method to find the union of two sets. For example,

```
use std::collections::HashSet;

fn main() {
    let hashset1 = HashSet::from([2, 7, 8]);
    let hashset2 = HashSet::from([1, 2, 7]);
    
    // Union of hashsets
    let result: HashSet<_> = hashset1.union(&hashset2).collect();
    
    println!("hashset1 = {:?}", hashset1);
    println!("hashset2 = {:?}", hashset2);
    println!("union = {:?}", result);
}
```

**Output**

hashset1 = {7, 8, 2}
hashset2 = {2, 7, 1}
union = {2, 7, 8, 1}

Here, we have used the `union()` method to find the union between two sets: hashset1 and hashset2.

```
hashset1.union(&hashset2).collect();
```

The `union()` method returns an iterator, so we have used the `collect()` method to get the actual result.

**Note:** We have passed `&hashset2` as an argument to the `union()` method because it takes a reference as an argument.

---

## 2. Intersection of two Sets

We can use the `intersection()` method to find the intersection between two sets. For example,

```
use std::collections::HashSet;

fn main() {
    let hashset1 = HashSet::from([2, 7, 8]);
    let hashset2 = HashSet::from([1, 2, 7]);
    
    // Intersection of hashsets
    let result: HashSet<_> = hashset1.intersection(&hashset2).collect();
    
    println!("hashset1 = {:?}", hashset1);
    println!("hashset2 = {:?}", hashset2);
    println!("intersection = {:?}", result);
}
```

**Output**

hashset1 = {2, 7, 8}
hashset2 = {2, 1, 7}
intersection = {7, 2}

---

## 3. Difference between two Sets

We can use the `difference()` method to find the difference between two sets. For example,

```
use std::collections::HashSet;

fn main() {
    let hashset1 = HashSet::from([1, 2, 3, 4]);
    let hashset2 = HashSet::from([4, 3, 2]);
    
    // Difference between hashsets
    let result: HashSet<_> = hashset1.difference(&hashset2).collect();
    
    println!("hashset1 = {:?}", hashset1);
    println!("hashset2 = {:?}", hashset2);
    println!("difference = {:?}", result);
}
```

**Output**

hashset1 = {3, 4, 1, 2}
hashset2 = {2, 4, 3}
difference = {1}

---

## 4. Symmetric Difference between two Sets

We can use the `symmetric_difference()` method to find the symmetric difference between two sets. The symmetric difference returns values from both sets except the ones in both.

```
use std::collections::HashSet;

fn main() {
    let hashset1 = HashSet::from([2, 7, 8]);
    let hashset2 = HashSet::from([1, 2, 7, 9]);
    
    // Symmetric difference of hashsets
    let result: HashSet<_> = hashset1.symmetric_difference(&hashset2).collect();
    
    println!("hashset1 = {:?}", hashset1);
    println!("hashset2 = {:?}", hashset2);
    println!("symmetric difference = {:?}", result);
}
```

**Output**

hashset1 = {8, 7, 2}
hashset2 = {2, 9, 1, 7}
symmetric difference = {8, 9, 1}

- [](https://www.programiz.com/rust/hashset#introduction)
- [](https://www.programiz.com/rust/hashset#operations)
- [](https://www.programiz.com/rust/hashset#add-values)
- [](https://www.programiz.com/rust/hashset#check-values)
- [](https://www.programiz.com/rust/hashset#remove-values)
- [](https://www.programiz.com/rust/hashset#iterate-over-values)
- [](https://www.programiz.com/rust/hashset#default-values)
- [](https://www.programiz.com/rust/hashset#other-methods)