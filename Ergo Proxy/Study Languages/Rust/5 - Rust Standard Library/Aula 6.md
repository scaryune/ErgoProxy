# Rust Iterators

An iterator in Rust is responsible for creating a sequence of values and allows us to iterate over each item of the sequence. It is primarily used for looping and we can only loop over iterators in Rust.

Let's look at a simple example on how we can loop through an array.

```
let numbers = [2, 1, 17, 99, 34, 56];
```

Now, let's change the array to an iterable array by calling the `iter()` method. If a data structure has the `iter()` method, it is called iterable.

```
let numbers_iterator = numbers.iter();
```

Finally, we can loop through the values and print them out.

```
for number in numbers_iterator {
    println!("{}", number);
}
```

**Note:** Collections like Array, Vector, HashMap and HashSet are not iterable by default. We can use the `iter()` method to tell Rust that it can be used to loop over the values.

---

### Example: Iterator in Rust

```
fn main() {
    let numbers = [2, 1, 17, 99, 34, 56];
    
    // iterator
    let numbers_iterator = numbers.iter();
    
    for number in numbers_iterator {
        println!("{}", number);
    }
}
```

**Output**

2
1
17
99
34
56

Here, `for..in` loop is called using the iterator in numbers_iterator, each value in the iterator is used in one iteration and then printed to the screen.

---

## next() Method of an Iterator in Rust

Another important method of iterator is the `next()` method. The `next()` method of an iterator can be used to traverse through the values in the iterator.

Every iterator in Rust by definition will have the `next()` method. The `next()` method is used to fetch individual values from the iterator.

Let's take a look at an example.

```
fn main() {
    let colors = vec!["Red", "Yellow", "Green"];
    
    // iterator
    let mut colors_iterator = colors.iter();
    println!("colors iterator = {:?}", colors_iterator);
    
    // fetch values from iterator one by one using next() method
    println!("{:?}", colors_iterator.next());
    println!("{:?}", colors_iterator.next());
    println!("{:?}", colors_iterator.next());
    println!("{:?}", colors_iterator.next());
}
```

**Output**

colors iterator = Iter(["Red", "Yellow", "Green"])
Some("Red")
Some("Yellow")
Some("Green")
None

Here, we fetch values from the iterator in colors_iterator using the `next()` method. The `next()` method either returns `Some` value or `None`.

Notice that we need to make the colors_iterator a mutable variable because calling `next()` will change the internal state of the iterator. Each call to `next()` will consume an item from the iterator.

The `next()` method returns `None` when the iterator reaches the end of the sequence.

---

## Ways to Create Iterator in Rust

We can create an iterator by converting a collection into an iterator. There are three ways to create an iterator.

1. Using `iter()` method
2. Using `into_iter()` method
3. Using `iter_mut()` method

All these methods provide different views of the data within the iterator.

### 1. Using iter() method

Using the `iter()` method on a collection will borrow (reference) each element of the collection in each iteration. Thus, the collection will be available for use after we have looped through it.

For example,

```
fn main() {
    let colors = vec!["Red", "Yellow", "Green"];
    
    // using iter() to iterate through a collection
    for color in colors.iter() {
        // reference to the items in the iterator
        println!("{}", color);
    }
    
    // the collection is untouched and still available here
    println!("colors = {:?}", colors);
}
```

**Output**

Red
Yellow
Green
colors = ["Red", "Yellow", "Green"]

Notice here that the colors variable is still available after the `iter()` method is used on it.

### 2. Using into_iter() method

Using the `into_iter()` method on a collection will iterate on the same element of the collection in each iteration. Thus, the collection will no longer be available for reuse as the value moves within the loop.

For example,

```
fn main() {
    let colors = vec!["Red", "Yellow", "Green"];
    
    // using into_iter() to iterate through a collection
    for color in colors.into_iter() {
        // the items in the collection move into this scope
        println!("{}", color);
    }
    // end of scope of for loop
    
    // error
    // the collection is not available here as the for loop scope ends above
    println!("colors = {:?}", colors);
}
```

**Output**

error[E0382]: borrow of moved value: `colors`
  --> src/main.rs:11:31
   |
2  |     let colors = vec!["Red", "Yellow", "Green"];
   |         ------ move occurs because `colors` has type `Vec<&str>`, which does not implement the `Copy` trait
...
5  |     for color in colors.into_iter() {
   |                         ----------- `colors` moved due to this method call
...
11 |     println!("colors = {:?}", colors);
   |                               ^^^^^^ value borrowed here after move
   |

Notice here that the `colors` variable is unavailable because the `into_iter()` method moves the actual data into the `for` loop and is not available outside of its scope.

**Note:** By default the for loop will apply the `into_iter()` function to the collection. We don't have to use the `into_iter()` function to convert the collection to an iterator when using the for loop.

For example, these two ways to loop through an iterator are the same.

```
for color in colors.into_iter() {
    // code
}

for color in colors {
    // code
}
```

### 3. Using iter_mut() method

Using the `iter_mut()` method on a collection will mutably borrow each element of the collection in each iteration. It means we can modify the collection in place.

For example,

```
fn main() {
    let mut colors = vec!["Red", "Yellow", "Green"];
    
    // using iter_mut() to iterate through a collection
    for color in colors.iter_mut() {
        // modify the item in the collection
        *color = "Black";
        println!("{}", color);
    }
    
    // the modified collection is available here
    println!("colors = {:?}", colors);
}
```

**Output**

Black
Black
Black
colors = ["Black", "Black", "Black"]

Notice here that we use `iter_mut()` method to change the original items in the collection with `*color = "Black"`. Thus, every item in the collection after the for loop is modified.

**Note:** All of the ways to construct an iterator follow the concept of **Borrowing**. To learn more about Borrowing, visit [_Rust References and Borrowing_](https://www.programiz.com/rust/references-and-borrowing).

---

## Iterator Adapters in Rust

Iterator adapters are used to transform it into another kind of iterator by altering its behavior. For example, let's take a look at the `map()` adapter.

```
let numbers = vec![1, 2, 3];

numbers.iter().map(|i| i + 1);
```

Here, the `map()` method takes a closure to call on each item on the vector numbers.

However, we will have to use the `collect()` method on the `map()` adapter to collect the result. This is because iterator adapters do not produce the result directly (lazy) without calling the `collect()` method.

```
numbers.iter().map(|i| i + 1).collect();
```

This will return a vector containing each item from the original vector incremented by **1**.

---

### Example: Iterator Adapters

```
fn main() {
   let numbers: Vec<i32> = vec![1, 2, 3];
   
   // using the map iterator adapter
   let even_numbers: Vec<i32> = numbers.iter().map(|i| i * 2).collect();
   
   println!("numbers = {:?}", numbers);
   println!("even_numbers = {:?}", even_numbers);
}
```

**Output**

numbers = [1, 2, 3]
even_numbers = [2, 4, 6]

In the above example, we use the `map()` method on the numbers iterator to loop through each item. The resulting vector contains each item from the original vector multiplied by **2**.

---

## Range in Rust

One of the other ways to create an iterator is to use the range notation. An example of a range is `1..6` which is an iterator. For example,

```
fn main() {
    // looping through a range
    for i in 1..6 {
        println!("{}", i);
    }
}
```

**Output**

1
2
3
4
5

Here, we loop through a range `1..6` which is inclusive on the left (starts at 1) and exclusive on the right (ends at 5). Range is usually used together with the `for` loop.

To learn more about range and for loop, visit [_Rust for Loop_](https://www.programiz.com/rust/for-loop).