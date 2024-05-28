# Go Closure

Go closure is a nested function that allows us to access variables of the outer function even after the outer function is closed.

Before we learn about closure, let's first revise the following concepts:

- Nested Functions
- Returning a function

---

## Nested function in Golang

In Go, we can create a function inside another function. This is known as a nested function. For example,

```
package main
import "fmt"

// outer function
func greet(name string) {

  // inner function
  var displayName = func() {
    fmt.Println("Hi", name)
  }

  // call inner function
  displayName()

}

func main() {

  // call outer function
  greet("John")  // Hi John

}
```

In the above example, we have created an [anonymous function](https://www.programiz.com/golang/anonymous-function) inside the `greet()` function.

Here, `var displayName = func() {...}` is a nested function. The nested function works similar to the normal function. It executes when `displayName()` is called inside the function `greet()`.

---

## Returning a function in Go

We can create a function that returns an anonymous function. For example,

```
package main
import "fmt"

func greet() func() {

  return func() {
    fmt.Println("Hi John")
  }

}

func main() {

  g1 := greet()
  g1()
}
```

**Output**

Hi John

In the above example, we have created the `greet()` function.

```
func greet() func() {...}
```

Here, `func()` before the curly braces indicates that the function returns another function.

Also, if you look into the return statement of this function, we can see the function is returning a function.

From `main()`, we call the `greet()` function.

```
g1 := greet()
```

Here, the returned function is now assigned to the `g1` variable. Hence, `g1()` executes the nested anonymous function.

---

## Go Closures

As we have already discussed, closure is a nested function that helps us access the outer function's variables even after the outer function is closed. Let's see an example.

```
package main
import "fmt"

// outer function
func greet() func() string {

  // variable defined outside the inner function
  name := "John"
  
  // return a nested anonymous function
  return func() string {
    name = "Hi " + name
    return name
  }
}

func main() {

  // call the outer function
  message := greet()

  // call the inner function
  fmt.Println(message())

}
```

**Output**

Hi John

In the above example, we have created a function named `greet()` that returns a nested anonymous function.

Here, when we call the function from `main()`.

```
message := greet()
```

The returned function is now assigned to the message variable.

At this point, the execution of the outer function is completed, so the name variable should be destroyed. However, when we call the anonymous function using

```
fmt.Println(message())
```

we are able to access the name variable of the outer function.

It's possible because the nested function now acts as a closure that closes the outer scope variable within its scope even after the outer function is executed.

Let's see one more example to make this concept clear for you.

---

## Example: Print Odd Numbers using Golang Closure

```
package main
import "fmt"

func calculate() func() int {
  num := 1

  // returns inner function
  return func() int {
    num = num + 2
    return num
  }

}

func main() {

  // call the outer function
  odd := calculate()

  // call the inner function
  fmt.Println(odd())
  fmt.Println(odd())
  fmt.Println(odd())

  // call the outer function again
  odd2 := calculate()
  fmt.Println(odd2())

}
```

**Output**

3
5
7
3

In the above example,

```
odd := calculate()
```

This code executes the outer function `calculate()` and returns a closure to the odd number. That's why we can access the num variable of `calculate()` even after completing the outer function.

Again, when we call the outer function using

```
odd2 := calculate()
```

a new closure is returned. Hence, we get **3** again when we call `odd2()`.

---

## Closure helps in Data Isolation

As we see in the previous example, a new closure is returned every time we call the outer function. Here, each returned closure is independent of one another, and the change in one won't affect the other.

This helps us to work with multiple data in isolation from one another. Let's see an example.

```
package main
import "fmt"

func displayNumbers() func() int {
  number := 0

  // inner function
  return func() int {
  number++
  return number
  }

}

func main() {

  // returns a closure 
  num1 := displayNumbers()

  fmt.Println(num1())
  fmt.Println(num1())
  fmt.Println(num1())

  // returns a new closure
  num2 := displayNumbers()
  fmt.Println(num2())
  fmt.Println(num2())

}
```

**Output**

1
2
3
1
2

In the above example, the `displayNumbers()` function returns an anonymous function that increases the number by **1**.

```
return func() int {
  number++
  return number
}
```

Inside the `main()` function, we assign the function call to num1 and num2 variables.

Here, we first call the closure function using `num1()`. In this case, we get outputs **1**, **2**, and **3**.

Again, we call it using `num2()`. In this case, the value of the number variable doesn't start from **3**; instead, it starts from **1** again.

This shows that the closure returned from `displayNumbers()` is isolated from one another.