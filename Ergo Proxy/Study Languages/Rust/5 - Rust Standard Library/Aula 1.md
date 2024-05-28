# Rust Stack and Heap

Stack and Heap are parts of memory available to our Rust code to use at runtime.

Rust is a memory-safe programming language. To ensure that Rust is memory-safe, it introduces concepts like ownership, references and borrowing.

To understand these concepts, we must first understand how to allocate and deallocate memory into the Stack and Heap.

---

## The Stack

The Stack can be thought of as a stack of books. When we add more books, we add them on the top of the pile. When we need a book, we take one from the top.

The stack inserts values in order. It gets them and removes the values in the opposite order.

- Adding data is called **pushing onto the stack**
- Removing data is called **popping off the stack**

This phenomenon is called **Last In, First Out (LIFO)** in programming.

Data stored on the stack must have a fixed size during compile time. Rust, by default, allocates memory on the stack for primitive types.

Let's visualize how memory is allocated and deallocated on the stack with an example.

```
fn foo() {
    let y = 999;
    let z = 333;
}

fn main() {
    let x = 111;
    
    foo();
}
```

In the above example, we first call the function `main()`. The `main()` function has one variable binding `x`.

When `main()` executes, we allocate a single 32-bit integer (`x`) to the stack frame.

|Address|Name|Value|
|---|---|---|
|0|x|111|

In the table, the **"Address"** column refers to the memory address of the RAM.

It starts from **0** and goes to how much RAM (number of bytes) your computer has. The **"Name"** column refers to the variable, and the **"Value"** column refers to the variable's value.

When `foo()` is called a new stack frame is allocated. The `foo()` function has two variable bindings, `y` and `z`.

|Address|Name|Value|
|---|---|---|
|2|z|333|
|1|y|999|
|0|x|111|

The numbers **0**, **1**, and **2** do not use address values the computer will use in reality. In reality, the addresses are separated by some number of bytes based on the value.

After `foo()` is completed, its stack frame is deallocated.

|Address|Name|Value|
|---|---|---|
|0|x|111|

Finally, `main()` is completed, and everything goes away.

Rust automatically does allocation and deallocation of memory in and out of the stack.

---

## The Heap

As opposed to the stack, most of the time, we will need to pass variables (memory) to different functions and keep them alive for longer than a single function's execution. This is when we can use the heap.

We can allocate memory on the heap using the `Box<T>` type. For example,

```
fn main() {
    let x = Box::new(100);
    let y = 222;
    
    println!("x = {}, y = {}", x, y);
}
```

**Output**

x = 100, y = 222

Let's visualize the memory when `main()` is called in the above example.

|Address|Name|Value|
|---|---|---|
|1|y|222|
|0|x|???|

Like before, we allocate two variables, `x` and `y`, on the stack.

However, the value of `x` is allocated on the heap when `Box::new()` is called. Thus, the actual value of `x` is a pointer to the heap.

The memory now looks like this:

|Address|Name|Value|
|---|---|---|
|5678||100|
|…|…|…|
|1|y|222|
|0|x|→ 5678|

Here, the variable `x` holds a pointer to the address **→ 5678**, an arbitrary address used for demonstration. Heap can be allocated and freed in any order. Thus it can end up with different addresses and create holes between addresses.

So when `x` goes away, it first frees the memory allocated on the heap.

|Address|Name|Value|
|---|---|---|
|1|y|222|
|0|x|???|

Once the `main()` is completed, we free the stack frame, and everything goes away, freeing all the memory.

We can make the memory live longer by transferring ownership where the heap can stay alive longer than the function which allocates the `Box`. To learn more about ownership, visit [_Rust Ownership_](https://www.programiz.com/rust/ownership).

---

## Differences between Stack and Heap

|Stack|Heap|
|---|---|
|Accessing data in the stack is faster.|Accessing data in a heap is slower.|
|Managing memory in the stack is predictable and trivial.|Managing memory for the heap (arbitrary size) is non-trivial.|
|Rust stack allocates by default.|`Box` is used to allocate to the heap.|
|Primitive types and local variables of a function are allocated on the stack.|Data types that are dynamic in size, such as `String`, `Vector`, `Box`, etc., are allocated on the heap.|