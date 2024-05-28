# Rust Thread

A thread is the smallest executable unit of a process.

Threads allow us to split the computation in our program into multiple threads. Running multiple tasks at the same time can improve performance of the code. However, it can add complexity.

---

## Creating a New Thread in Rust

In Rust, we can create a native operating system thread using the `thread::spawn()` function from the `std` module. The spawn method takes a closure as an argument.

Here is the syntax of `thread::spawn()`,

```
thread::spawn(|| {
    // code to execute in the thread 
})
```

Now, let's see an example.

```
use std::thread;
use std::time::Duration;

fn main() {
    // create a thread
    thread::spawn(|| {
        // everything in here runs in a separate thread
        for i in 0..10 {
            println!("{} from the spawned thread!", i);
            thread::sleep(Duration::from_millis(2));
        }
    });

    // main thread
    for i in 0..5 {
        println!("{} from the main thread!", i);
        thread::sleep(Duration::from_millis(1));
    }
}
```

**Output**

0 from the main thread!
0 from the spawned thread!
1 from the main thread!
1 from the spawned thread!
2 from the main thread!
3 from the main thread!
2 from the spawned thread!
4 from the main thread!

In the example above, we create a thread using the `thread::spawn()` function. The thread loops over `0..5` and prints the current value.

Similarly, we have a main thread where we loop over `0..5` and print the current value.

We also call `thread::sleep` to force a thread to stop its execution for a short duration, allowing a different thread to run.

Notice that we sleep **2** milliseconds in the spawned thread and 1 millisecond in the main thread.

The output from this program might be a little different every time. The important thing to remember here is that if the main thread completes, all other threads are shut down whether or not they have finished running.

So, even though the spawned thread should print until `i` is 9, it only reaches to **2** because the main thread shut down.

---

## Join Handles in Rust

A spawned thread always returns a join handle. If we want the spawned thread to complete execution, we can save the return value of `thread::spawn` in a variable and then call the `join()` method on it.

The `join()` method on `JoinHandle` (return type of `thread::spawn`) waits for the spawned thread to finish.

Let's look at an example.

```
use std::thread;
use std::time::Duration;

fn main() {
    // create a thread and save the handle to a variable
    let handle = thread::spawn(|| {
        // everything in here runs in a separate thread
        for i in 0..10 {
            println!("{} from the spawned thread!", i);
            thread::sleep(Duration::from_millis(2));
        }
    });

    // main thread
    for i in 0..5 {
        println!("{} from the main thread!", i);
        thread::sleep(Duration::from_millis(1));
    }
    
    // wait for the separate thread to complete
    handle.join().unwrap();
}
```

**Output**

0 from the main thread!
0 from the spawned thread!
1 from the main thread!
2 from the main thread!
1 from the spawned thread!
3 from the main thread!
2 from the spawned thread!
4 from the main thread!
3 from the spawned thread!
4 from the spawned thread!
5 from the spawned thread!
6 from the spawned thread!
7 from the spawned thread!
8 from the spawned thread!
9 from the spawned thread!

Here, we save the return of the `thread::spawn()` function and bind it to a variable called `handle`.

In the final line of the code, we call the `join()` method of the `handle`. Calling `join()` on the `handle` blocks the thread until the thread terminates.

The two threads (main and spawned thread) continue alternating for some time, but the main thread waits because of `handle.join()` and does not end until the spawned thread is finished.

If we move the `handle.join()` before the final loop, the output will change and the print statements won't be interleaved.

```
use std::thread;
use std::time::Duration;

fn main() {
    // create a thread and save the handle to a variable
    let handle = thread::spawn(|| {
        // everything in here runs in a separate thread
        for i in 0..10 {
            println!("{} from the spawned thread!", i);
            thread::sleep(Duration::from_millis(2));
        }
    });
    
    // wait for the separate thread to complete
    handle.join().unwrap();

    // main thread
    for i in 0..5 {
        println!("{} from the main thread!", i);
        thread::sleep(Duration::from_millis(1));
    }
}
```

**Output**

0 from the spawned thread!
1 from the spawned thread!
2 from the spawned thread!
3 from the spawned thread!
4 from the spawned thread!
5 from the spawned thread!
6 from the spawned thread!
7 from the spawned thread!
8 from the spawned thread!
9 from the spawned thread!
0 from the main thread!
1 from the main thread!
2 from the main thread!
3 from the main thread!
4 from the main thread!

Thus, it is important to know where `join()` is called. I will dictate whether threads run at the same time or not.

---

## Using move Closures with Threads in Rust

A value can be moved into a separate thread by passing it as an argument to the `thread::spawn()` function.

Let's look at an example.

```
use std::thread;

fn main() {
    // main thread starts here
    let message = String::from("Hello, World!");

    // move the message value to a separate thread
    let handle = thread::spawn(move || {
        println!("{}", message);
    });

    // wait for the thread to finish
    handle.join().unwrap();
}
```

**Output**

Hello, World!

Here, the closure `||` passed to the `thread::spawn()` function uses the `move` keyword to indicate that it takes ownership of the `message` variable.

When a value is moved into a thread, ownership of the value is transferred to the thread, and the main thread can no longer access the value.

This means that the closure can use the `message` variable even after the main thread has completed.

Let's look at what happens if we don't use the `move` keyword in front of the closure.

```
use std::thread;

fn main() {
    let message = String::from("Hello, World!");

    // using the message variable without a move
    let handle = thread::spawn(|| {
        println!("{}", message);
    });

    handle.join().unwrap();
}
```

**Output**

error[E0373]: closure may outlive the current function, but it borrows `message`, which is owned by the current function
 --> src/main.rs:7:32
  |
7 |     let handle = thread::spawn(|| {
  |                                ^^ may outlive borrowed value `message`
8 |         println!("{}", message);
  |                        ------- `message` is borrowed here
  |

The program in this case fails to compile. Here, Rust will try to borrow the `message` variable into the separate thread.

```
7 |     let handle = thread::spawn(|| {
  |                                ^^ may outlive borrowed value `message`
```

However, Rust doesn't know how long the spawned thread will run. Thus it can't tell if the reference to the `message` variable will always be valid.

By adding the `move` keyword before the closure, we force the closure to take ownership of the `message` variable or any variable used inside closure.

We are telling Rust that the main thread won't use the `message` variable anymore. This is a classic example of Rust ownership and how it saves us from mishaps. To learn more about ownership in Rust, visit [_Rust Ownership_](https://www.programiz.com/rust/ownership).

Note that moving a value into a thread can be useful for parallelism, but it can also be a source of bugs if not used carefully.

---

## Sending Messages between Threads in Rust

In Rust, threads can communicate with each other by sending messages through channels. A channel is a way to send values between threads, and it can be used to synchronize communication and avoid data races.

We use the `channel()` function in the `std::sync::mspsc` module to create a channel in Rust.

Let's take a look at how we can use channels to communicate between threads.

```
use std::sync::mpsc;
use std::thread;

fn main() {
    // main thread starts here
    // create a new channel
    let (sender, receiver) = mpsc::channel();

    // spawn a new thread
    let handle = thread::spawn(move || {
        // receive message from channel
        let message = receiver.recv().unwrap();

        println!("Received message: {}", message);
    });

    let message = String::from("Hello, World!");
    // send message to channel
    sender.send(message).unwrap();

    // wait for spawned thread to finish
    handle.join().unwrap();
}
```

**Output**

Received message: Hello, World!

Here, we create a channel using the `channel()` function. The `std::sync::mpsc` module provides **multiple-producer, single-consumer** (mspc) channels that can be used to send values between threads.

```
// create a new channel
let (sender, receiver) = mpsc::channel();
```

The `sender` and `receiver` variables represent the two endpoints of the channel. The sender endpoint is used to send messages, while the receiver endpoint is used to receive messages.

```
// spawn a new thread
let handle = thread::spawn(move || {
    // receive message from channel
    let message = receiver.recv().unwrap();

    println!("Received message: {}", message);
});
```

We also create a spawned thread using the `thread::spawn()` function. The closure passed to the function receives a message using the `receiver.recv()` method.

The `recv()` method blocks until a message is received on the channel, and it returns a `Result` indicating whether a message was received or an error occurred.

```
let message = String::from("Hello, World!");
// send message to channel
sender.send(message).unwrap();
```

In the main thread, a `message` is created and sent using the `sender.send()` method. The `send(`) method returns a `Result` indicating whether the message was successfully sent or an error occurred.

```
// wait for spawned thread to finish
handle.join().unwrap();
```

Finally, the `join()` method is called on the handle to wait for the spawned thread to finish before the program exits.