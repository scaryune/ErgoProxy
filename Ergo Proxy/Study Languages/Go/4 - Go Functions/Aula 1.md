# Go Functions

We use functions to divide our code into smaller chunks to make our code looks clean and easier to understand.

Basically, a function is a block of code that performs a specific task. For example, suppose we want to write code to create a circle and rectangle and color them.

In this case, we can organize our code by creating three different functions:

- function to create a circle
- function to create a rectangle
- function to color

This way, our code will look more organized. Also, we can reuse the same function to color the circle and rectangle. Hence, providing the benefits of code reusability.

---

## Create a Go Function

In Golang, we use the `func` keyword to create a function.

```
func greet(){
  // code
}
```

Here, `greet()` is the name of the function (denoted by `()`) and code inside `{....}` indicates the function body.

Let's now create a function that prints **Good Morning**.

```
// Program to define a function

package main
import "fmt"

// define a function
func greet() {
  fmt.Println("Good Morning")
}

func main() {

}
```

When we run this program, we will not get the output.

This is because we are just defining a function. To execute a function, we need to call it first.

**Function Call**

We use the function's name followed by parenthesis to call a function.

```
greet()
```

Now, let's add a function call inside `main()`.

```
// Program to define a function

package main
import "fmt"

// define a function
func greet() {
  fmt.Println("Good Morning")
}

func main() {
 
  // function call
  greet()

}
```

**Output**

Good Morning

This time the function runs, and we get **Good Morning** as output.

---

### Example: Golang Function

```
package main 
import "fmt"

// function to add two numbers
func addNumbers() {
  n1 := 12
  n2 := 8

  sum := n1 + n2
  fmt.Println("Sum:", sum)
}

func main() {
  // function call
  addNumbers()
}
```

**Output**

Sum: 20

In the above example, we have created a function named `addNumbers()`. The function adds two numbers and prints the sum.

Here's how the program works:

![To run a function, we need to call the function.](https://www.programiz.com/sites/tutorial2program/files/go-function-working.png "Working of function in Go")

Working of function in Go

---

## Function Parameters in Golang

In our last example, we have created a function that does a single task, adds two numbers, **12** and **8**.

```
func addNumbers() {
  n1 := 12
  n2 := 8
  sum := n1 + n2
  fmt.Println("Sum:", sum)
}
```

However, in real projects, we want our functions to work dynamically. That is, instead of adding **12** and **8**, the `addNumbers()` function should be able to add any two numbers.

In this case, we can create functions that accept external values and perform operations on them. These additional parameters are known as function parameters.

**Define Function with Parameters**

Here's how we can create a function with parameters:

```
func addNumbers(n1 int, n2 int) {
  // code
}
```

Now, the `addNumbers()` function accepts two parameters: `n1` and `n2`. Here, `int` denotes that both parameters are of integer type.

To call this function, we need to pass some values (known as function arguments).

```
// function call
addNumbers(21, 13)
```

Here, **21** and **13** are the function arguments that are passed to the `addNumbers()` function.

---

### Example: Function Parameters

```
// Program to illustrate function parameters

package main
import "fmt"

// define a function with 2 parameters
func addNumbers(n1 int, n2 int) {
  sum := n1 + n2
  fmt.Println("Sum:", sum)
}

func main() {

  // pass parameters in function call
  addNumbers(21, 13)

}
```

**Output**

Sum: 34

Here's how the program works:

![To pass values in the function, we use parameters.](https://www.programiz.com/sites/tutorial2program/files/go-function-parameter.png "Working of Function with Parameters")

Working of Function with Parameters

The arguments are assigned to the function parameters when we call the function. `21` is assigned to `n1` and `13` is assigned to `n2`.

That's why when we add `n1` and `n2` inside the function, we get **34 (21 + 13)**.

**Note:** The function parameter data type should always match the data passed during the function call. Here, the data type of n1 and n2 is `int`, so we have passed integer values **21** and **13** during a function call.

---

## Return Value from Go Function

In our last example, we have printed the value of the sum inside the function itself. However, we can also return value from a function and use it anywhere in our program.

Here's how we can create a Go function that returns a value:

```
func addNumbers(n1 int, n2 int) int {
  // code
  return sum
}
```

Here, `int` before the opening curly bracket `{` indicates the return type of the function. In this case, `int` means the function will return an integer value.

And `return sum` is the return statement that returns the value of the `sum` variable.

The function returns value to the place from where it is called, so we need to store the returned value to a variable.

```
// function call
result := addNumbers(21, 13)
```

Here, we are storing the returned value to the `result` variable.

---

### Example: Function Return Value

```
package main
import "fmt"

// function definition
func addNumbers(n1 int, n2 int) int {
  sum := n1 + n2
  return sum
}

func main() {

  // function call
  result := addNumbers(21, 13)

  fmt.Println("Sum:",result)
}
```

**Output**

Sum: 34

In the above example, when the `return` statement is encountered, it returns the value of sum. The returned value is assigned to the result variable inside `main()`.

Here's how the program works.

![Return statement returns the value when encountered.](https://www.programiz.com/sites/tutorial2program/files/go-function-return.png "Working of Go function with return values")

Working of Go function with return values

The `return` statement should be the last statement of the function. When a return statement is encountered, the function terminates.

Let's see an example,

```
package main
import "fmt"

// function definition
func addNumbers(n1 int, n2 int) int {
  sum := n1 + n2
  return sum

  // code after return statement
  fmt.Println("After return statement")
}

func main() {

  // function call
  result := addNumbers(21, 13)
  fmt.Println("Sum:",result)

}
```

We get a **"missing return at the end of function"** error as we have added a line after the return statement.

---

## Return Multiple Values from Go Function

In Go, we can also return multiple values from a function. For example,

```
// Program to return multiple values from function

package main
import "fmt"

// function definition
func calculate(n1 int, n2 int) (int, int) {
  sum := n1 + n2
  difference := n1 - n2

  // return two values
  return sum, difference
}

func main() {

  // function call
  sum, difference := calculate(21, 13)

  fmt.Println("Sum:", sum, "Difference:", difference)
}
```

**Output**

Sum: 34 Difference: 8

In the above example, we have created a function named `calculate()`.

```
func calculate(n1 int, n2 int) (int, int) {
  ...
}
```

Here, `(int, int)` indicates that we are returning two integer values: sum and difference from the function.

Since the function returns two values, we have used two variables while calling the function.

```
sum, difference = calculate(21, 13);
```

---

## Benefits of Using Functions

Here are the benefits of using a function in programming:

**1. Code Reusability**

We can reuse the same function multiple times in our program. For example,

```
// Program to illustrate code reusability in function

package main
import "fmt"

// function definition
func getSquare(num int) {
  square := num * num
  fmt.Printf("Square of %d is %d\n", num, square)  
}

// main function
func main() {

  // call function 3 times
  getSquare(3)
  getSquare(5)
  getSquare(10)

}
```

**Output**

Square of 3 is 9
Square of 5 is 25
Square of 10 is 100

In the above program, we have created the function named `getSquare()` to calculate the square of a number.

Here, we are reusing the same function multiple times to calculate the square of different numbers.

**2. Code Readability**

Functions help us break our code into chunks to make our program readable and easy to understand. It also makes the code easier to maintain and debug.

- [](https://www.programiz.com/golang/function#introduction)
- [](https://www.programiz.com/golang/function#define-function)
- [](https://www.programiz.com/golang/function#function-example)
- [](https://www.programiz.com/golang/function#function-parameter)
- [](https://www.programiz.com/golang/function#return-function)
- [](https://www.programiz.com/golang/function#return-multiple)
- [](https://www.programiz.com/golang/function#function-benefits)