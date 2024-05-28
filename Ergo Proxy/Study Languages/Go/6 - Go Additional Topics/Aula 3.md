# Goroutines

In Go, we use goroutines to create concurrent programs. Concurrent programs are able to run multiple processes at the same time.

Suppose we have a program that has two independent functions. In normal programs, two functions will be executed synchronously. That is, the second function is executed only after the execution of the first function.

However, since both functions are independent, it would be efficient if we could execute both functions together asynchronously.

For this, we use goroutines that help us to achieve concurrency in programming.

---

## Create Goroutine

We can convert a regular function to a goroutine by calling the function using the `go` keyword. For example,

```
func display() {
  // code inside the function
}

// start goroutine
go display()
```

Here, `display()` is a goroutine.

---

## Example: Goroutine

Let's now see a working example of concurrent programming using goroutine.

```
package main
import (
  "fmt"
  "time"
)

// create a function
func display(message string) {

  fmt.Println(message)
}

func main() {

  // call goroutine
  go display("Process 1")

  display("Process 2")
}
```

**Output**

Process 2

In the above example, we have called the `display()` function two times:

- `go display("Process 1")` - as a goroutine
- `display("Process 2")` - regular function call

During the normal execution, the control of the program moves to the function during the first function call and once the execution is completed, it returns back to the next statement.

In our example, the next statement is the second call to the function. So, first **Process 1** should be printed and then **Process 2**.

However, we are only getting **Process 2** as output.

This is because we have used `go` with the first function call, so it is treated as a goroutine. And the function runs independently and the `main()` function now runs concurrently.

Hence, the second call is executed immediately and the program terminates without completing the first function call.

![In a program that uses Goroutine, the execution of processes is concurrent.](https://www.programiz.com/sites/tutorial2program/files/working-of-goroutine.png "Working of Goroutine")

Working of Goroutine

---

## Run two functions concurrently using Goroutine

In a concurrent program, the `main()` is always a default goroutine. Other goroutines can not execute if the `main()` is not executing.

So, in order to make sure that all the goroutines are executed before the main function ends, we sleep the process so that the other processes get a chance to execute.

```
// Program to run two goroutines concurrently

package main
import (
  "fmt"
  "time"
)

// create a function
func display(message string) {

  // infinite for loop
  for {
    fmt.Println(message)

    // to sleep the process for 1 second
    time.Sleep(time.Second * 1)
  }
}

func main() {

  // call function with goroutine
  go display("Process 1")

  display("Process 2")

}
```

**Output**

Process 3
Process 2
Process 1

In the above example, we have added a line in the function definition.

```
time.Sleep(time.Second * 1)
```

Here, when the `display("Process 2")` is executing, the `time.Sleep()` function stops the process for **1** second. In that **1** second, the goroutine `go display("Process 1")` is executed.

This way, the functions run concurrently before the `main()` functions stops.

---

## Multiple Goroutines

While running multiple Goroutines together, they interact with each other concurrently. The order of execution of goroutine is random, so we might not get the output as expected. For example,

```
// Program to illustrate multiple goroutines

package main

import (
  "fmt"
  "time"
)

func display(message string) {

  fmt.Println(message)

}

func main() {

  // run two different goroutine
  go display("Process 1")
  go display("Process 2")
  go display("Process 3")

  // to sleep main goroutine for 1 sec
  time.Sleep(time.Second * 1)
}
```

**Output**

Process 1
Process 1
.
.
Process 3
Process 2
Process 2
.
.

Here, all the goroutines run concurrently with the sleep time of 1 second. The order of execution is random, so everytime we run the program, we get a different output.

---

## Benefits of Goroutines

Here are some of the major benefits of goroutines.

- With Goroutines, concurrency is achieved in Go programming. It helps two or more independent functions to run together.
- Goroutines can be used to run background operations in a program.
- It communicates through private channels so the communication between them is safer.
- With goroutines, we can split one task into different segments to perform better.