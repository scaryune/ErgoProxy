# Go defer, panic, and recover

In Go, we use defer, panic and recover statements to handle errors.

We use `defer` to delay the execution of functions that might cause an error. The `panic` statement terminates the program immediately and `recover` is used to recover the message during panic.

Before we learn about error handling statements, make sure to know about [Go errors](https://www.programiz.com/golang/errors).

---

## defer in Go

We use the `defer` statement to prevent the execution of a function until all other functions execute. For example,

```
package main
import "fmt"

func main() {

  // defer the execution of Println() function
  defer fmt.Println("Three")

  fmt.Println("One")
  fmt.Println("Two")

}
```

**Output**

One
Two
Three

In the above example, we have used the defer before the first print statement.

That's why the `Println()` function is executed last after all other functions are executed.

---

## Multiple defer Statements in Go

When we use multiple defer in a program, the order of execution of the defer statements will be **LIFO (Last In First Out)**.

This means the last defer statement will be executed first. For example,

```
package main
import "fmt"

func main() {

  defer fmt.Println("One")
  defer fmt.Println("Two")
  defer fmt.Println("Three")

}
```

**Output**

Three
Two
One

In the above example, we are calling the `Println()` function using 3 `defer` statements.

As you can see, the order of execution is **LIFO**. That is, the last `defer` statement is executed first, and the first `defer` statement is executed last

---

## Golang panic

We use the panic statement to immediately end the execution of the program. If our program reaches a point where it cannot be recovered due to some major errors, it's best to use panic.

The lines of code after the panic statement are not executed. For example,

```
package main
import "fmt"

func main() {

  fmt.Println("Help! Something bad is happening.")
  panic ("Ending the program")
  fmt.Println("Waiting to execute")

}
```

**Output**

Help! Something bad is happening.
panic: Ending the program

Here, the program is terminated when it reaches the panic statement. That's why the print statement after the panic is not executed.

**Note:** `panic:` in the output specifies that the program is terminated due to panic and it's the panic message.

---

### Example: Panic in Golang

```
package main

import "fmt"

func division(num1, num2 int) {

  // if num2 is 0, program is terminated due to panic
  if num2 == 0 {
    panic("Cannot divide a number by zero")
  } else {	
    result := num1 / num2
    fmt.Println("Result: ", result)
  }
}

func main() {

  division(4, 2)
  division(8, 0)
  division(2, 8)

}
```

**Output**

Result:  2
panic: Cannot divide a number by zero

In the above example, we have created a function that performs the division of two numbers: `num1` and `num2`.

Inside the function, we have used an [if...else statement](https://www.programiz.com/golang/if-else) that checks if `num2` (denominator) is **0** or not. If it is **0**, the execution of the program stops because of the **panic statement**.

```
panic("Cannot divide a number by zero")
```

Here, when we run the program, we first get result **2** (division of **4** and **2**). However, during the second function call, the value of `num2` is **0** (division of **8** and **0**).

Hence, the execution of the program is terminated.

---

## recover in Go Programming

The panic statement immediately terminates the program. However, sometimes it might be important for a program to complete its execution and get some required results.

In such cases, we use the recover statement to handle panic in Go. The **recover statement** prevents the termination of the program and recovers the program from panic.

Let's see an example.

```
package main
import "fmt"

// recover function to handle panic
func handlePanic() {

  // detect if panic occurs or not
  a := recover()

  if a != nil {
    fmt.Println("RECOVER", a)
  }

}

func division(num1, num2 int) {

  // execute the handlePanic even after panic occurs
  defer handlePanic()

  // if num2 is 0, program is terminated due to panic
  if num2 == 0 {
    panic("Cannot divide a number by zero")
  } else {
    result := num1 / num2
    fmt.Println("Result: ", result)
  }
}

func main() {

  division(4, 2)
  division(8, 0)
  division(2, 8)

}
```

**Output**

Result:  2
RECOVER Cannot divide a number by zero
Result:  0

In the above example, we have created a `handlePanic()` function to recover from the panicking state.

```
func handlePanic() {

  // detect if panic occurs or not
  a := recover()

  if a != nil {
    fmt.Println("RECOVER", a)
  }
}
```

Here, we have used `a := recover()` to detect any occurrence of panic in our program and assign the panic message to a.

In our example, a panic occurs, so there will be some value in a. Hence, the **if statement** is executed, which prints the panic message.

Inside the `division()` function, we are calling the `handlePanic()` function

```
defer handlePanic()
```

Here, notice two things:

- **We are calling the handlePanic() before the occurrence of panic.** It's because the program will be terminated if it encounters panic and we want to execute `handlePanic()` before the termination.
- **We are using defer to call handlePanic().** It's because we only want to handle the panic after it occurs, so we are deferring its execution.

- [](https://www.programiz.com/golang/defer-panic-recover#introduction)
- [](https://www.programiz.com/golang/defer-panic-recover#defer-statement)
- [](https://www.programiz.com/golang/defer-panic-recover#multiple-defer)
- [](https://www.programiz.com/golang/defer-panic-recover#panic-statement)
- [](https://www.programiz.com/golang/defer-panic-recover#example-panic)
- [](https://www.programiz.com/golang/defer-panic-recover#recover-statement)