# Go Anonymous Function

In Go, we can create a function without the function name, known as an anonymous function. For example,

```
func () {
  fmt.Println("Function without name")
}
```

The above function is a valid function that prints **"Function without name"**. It works just like a regular [function in Go](http://programiz.com/golang/function).

---

## Working of Go Anonymous Function

Since an anonymous function doesn't have any name, you might be wondering how we can call the function.

Usually, what we do is assign the anonymous function to a variable and then use the variable name to call the function. For example,

```
//anonymous function
var greet = func (){
  // code
}

// function call
greet()
```

Here, you can see that we have used the variable name greet to call the function.

### Example: Go Anonymous Function

```
package main
import "fmt"

func main() {

  // anonymous function
  var greet = func() {
    fmt.Println("Hello, how are you")
  }

  // function call
  greet()

}
```

**Output**

Hello, how are you

Here, we have assigned the anonymous function to the variable greet and used `greet()` to call the function.

---

## Anonymous Function with Parameters

Like a regular function, an anonymous function can also accept function parameters. For example,

```
// Program to pass arguments in an anonymous function

package main
import "fmt"

func main() {

  // anonymous function with arguments
  var sum = func(n1, n2 int) {
    sum := n1 + n2
    fmt.Println("Sum is:", sum)
  } 

  // function call
  sum(5, 3)

}
```

**Output**

Sum is: 8

Here, the anonymous function takes two integer arguments n1 and n2.

```
func(n1, n2 int) {
  ...
}
```

Since we have assigned the anonymous function to the sum variable, we are calling the function using the variable name.

```
sum(5, 3)
```

Here, **5** and **3** are values passed to the function.

---

## Return Value From Anonymous Function

Like in regular functions, we can also return a value from an anonymous function. For example,

```
// Program to return value from an anonymous function

package main
import "fmt"

func main() {

  // anonymous function
  var sum = func(n1, n2 int) int {
    sum := n1 + n2
  
    return sum
  } 

  // function call
  result := sum(5, 3)

  fmt.Println("Sum is:", result)

}
```

**Output**

Sum is: 8

Here, we have assigned the anonymous function `func(n1,n2 int) int` to the sum variable. The function calculates the sum of n1 and n2 and returns it.

---

## Example: Return Value From Anonymous Function

```
// Program to return the area of a rectangle

package main
import "fmt"

func main() {

  // anonymous function
  area := func(length, breadth int) int {
    return length * breadth
  } 

  // function call using variable name
  fmt.Println("The area of rectangle is", area(3,4))

}
```

**Output**

The area of rectangle is 12

In the above program, we have defined an anonymous function and assigned it to the variable area. The area of the rectangle, `length * breadth` (**3** * **4**), is returned to the area.

---

## Anonymous Function as Arguments to Other Functions

In Go, we can also pass anonymous functions as arguments to other functions. In that case, we pass the variable that contains the anonymous function. For example,

```
package main
import "fmt"

var sum = 0

// regular function to calculate square of numbers
func findSquare(num int) int {
  square := num * num
  return square
}

func main() {

  // anonymous function that returns sum of numbers
  sum := func(number1 int, number2 int) int {
    return number1 + number2
}

  // function call
  result := findSquare(sum(6, 9))
  fmt.Println("Result is:", result)

}
```

**Output**

Result is: 225

In the above example, we have created two functions:

- an anonymous function to find the sum of two numbers
- a regular function, `findSquare()`, to find the square of a number.

Notice the function call inside `main()`

```
result := findSquare(sum(6, 9))
```

Here, we have passed the anonymous function as the function parameter to the `findSquare()` function.

The anonymous function returns the sum of two parameters. This sum is then passed to the `findSquare()` function, which returns the square of the sum.

So, in our program, the anonymous function first returns the sum of **6** and **9**, which is **15**.

This value is then passed to the `findSquare()` function, which returns the square of **15**, which is **225**.

---

## Return an Anonymous Function in Go

We can also return an anonymous function in Go. For that, we need to create an anonymous function inside a regular function and return it. For example,

```
// Program to return an anonymous function 

package main
import "fmt"

// function that returns an anonymous function
func displayNumber() func() int {

  number := 10
  return func() int {
    number++
    return number
  }
}

func main() {

  a := displayNumber()

  fmt.Println(a())

}
```

**Output**

11

In the above program, notice this line in the `displayNumber()` function,

```
func displayNumber() func() int {
```

Here, the `func()` denotes that `displayNumber()` returns a function, whereas the `int` denotes that the anonymous function returns an integer. Notice that `displayNumber()` is a regular function.

Inside the `displayNumber()` function, we have created an anonymous function.

```
return func() int {
  …
}
```

Here, we are returning the anonymous function. So, when the `displayNumber()` function is called, the anonymous function is also called and the incremented number is returned.

- [](https://www.programiz.com/golang/anonymous-function#introduction)
- [](https://www.programiz.com/golang/anonymous-function#create-anonymous)
- [](https://www.programiz.com/golang/anonymous-function#function-argument)
- [](https://www.programiz.com/golang/anonymous-function#function-return-value)
- [](https://www.programiz.com/golang/anonymous-function#anonymous-argument)
- [](https://www.programiz.com/golang/anonymous-function#return-anonymous)