# Go Packages

A package is a container that contains various functions to perform specific tasks. For example, the `math` package includes the `Sqrt()` function to perform the square root of a number.

While working on big projects, we have to deal with a large amount of code, and writing everything together in the same file will make our code look messy. Instead, we can separate our code into multiple files by keeping the related code together in packages.

Now, we can use the package whenever we need it in our projects. This way we can also reuse our code.

---

## Golang main() package

Remember this `Hello World` program, you wrote while starting with Go programming.

```
package main
import "fmt"

func main() {
    fmt.Println("Hello World!")
}
```

Here, we have started our program with the `package main`.

Every Go program starts with the main package. Whenever the compiler sees the main package, it treats the program as the executable code.

---

## Import package in Golang

In our previous example, we have used the code

```
import "fmt"
```

Here, we have used the `import` keyword to import the `fmt` package.

Once we import the package, we can use all of its functions in our program. For example,

```
package main

// import the fmt package
import "fmt"

func main() {

  // use the Println() function of fmt
  fmt.Println("Hello World!")
}
```

In the above program, we have imported the `fmt` package in our program. Notice the code

```
fmt.Println("Hello World!")
```

Here, we are using the `Println()` function of the `fmt` package to print the text.

---

### Commonly used packages in Go

Now that we know how to import packages, let's learn about some of the popular packages:

- `fmt` Package
- `math` Package
- `string` Package

---

## Golang fmt Package

In Go, the `fmt` package provides functions to format our input/output data. For example, the `fmt.Println()` function prints the data to the output screen.

Some of the commonly used `fmt` functions:

|Functions|Descriptions|
|---|---|
|`Print()`|prints the text to output screen|
|`Println()`|prints the text to output with a new line character at the end|
|`Printf()`|prints the formatted string to the output screen|
|`Scan()`|get input values from the user|
|`Scanf()`|get input values using the format specifier|
|`Scanln()`|get input values until the new line is detected|

To use these functions, we must import the `fmt` package.

---

### Example 1: Golang fmt package

```
package main
import "fmt"

func main() {

  var number int

  // take input value
  fmt.Scan(&number)

  // print using Println
  fmt.Println("Number is", number)

  fmt.Print("Using Print")
  fmt.Println("Using Println")

}
```

**Output**

Number is 10
Using PrintUsing Println

In the above example, we have used the `fmt.Scan()` function to take input value and assign it to the number variable. We then print the value of number using the `fmt.Println()`.

The `Println()` function adds a newline character at the end by default. That's why the next statement, `fmt.Print()` prints the text, `Using Print` in the new line.

However, `Print()` doesn't add the newline character by default, the next print statement prints the text `Using Println` in the same line

---

### Example 2: fmt Scanf() and Printf() functions

```
package main
import "fmt"

func main() {

  var number int
  
  fmt.Scanf("%d", &number)  // Input: 10
  fmt.Printf("%d", number)  // Output: 10

}
```

In the above example, functions

- `fmt.Scanf("%d", &number)` - takes integer input value and assign it to the `number` variable
- `fmt.Printf("%d", number)` - replaces the `%d` format specifier by the value of `number` and prints it

---

## math package in Go

The `math` package provides various functions to perform mathematical operations. For example, `math.Sqrt()` finds the square root of a number.

Some of the commonly used `math` functions:

|Functions|Descriptions|
|---|---|
|`Sqrt()`|returns the square root of the number|
|`Cbrt()`|returns the cube root of the number|
|`Max()`|returns the larger number between two|
|`Min()`|returns the smaller number between two|
|`Mod()`|computes the remainder after division|

To use these functions, we must import the `math` package.

---

### Example: math Package

```
package main
import "fmt"

// import the math package
import "math"

func main() {

  // find the square root
  fmt.Println(math.Sqrt(25))    // 5

  // find the cube root
  fmt.Println(math.Cbrt(27))    // 3

  // find the maximum number
  fmt.Println(math.Max(21, 18))    // 21

  // find the minimum number
  fmt.Println(math.Min(21, 18))    // 18

  // find the remainder
  fmt.Println(math.Mod(5, 2))    // 1

}
```

Here, we have imported the `math` package in our program. This is why we are able to use math-based functions like `Sqrt()`, `Max()`, etc in our program.

**Note:** In our example, you might have noticed that we have used two `import` statements to import the `fmt` and `math` packages. In such cases, we can import both packages together using a single `import` statement. For example,

```
// use two import statements
import "fmt"
import "math"

// use single import statement
import (
  "fmt"
  "math"
)
```

---

## Go strings package

The `strings` package provides functions to perform operations on UTF-8 encoded strings. For example, `strings.Contains()` checks if the string contains a substring.

Some of the commonly used `strings` functions:

|Functions|Descriptions|
|---|---|
|`Compare()`|checks if two strings are equal|
|`Contains()`|checks if the string contains a substring|
|`Count()`|counts the number of times a substring present in the string|
|`Join()`|creates a new string by concatenating elements of a string array|
|`ToLower()`|converts the string to lowercase|
|`ToUpper()`|converts the string to uppercase|

To use these functions, we must import the `strings` package.

---

### Example: string Package

```
package main

// import multiple packages
import (
  "fmt"
  "strings"
  )

func main() {

  // convert the string to lowercase
  lower := strings.ToLower("GOLANG STRINGS")
  fmt.Println(lower)

  // convert the string to uppercase
  upper := strings.ToUpper("golang strings")
  fmt.Println(upper)

  // create a string array
  stringArray := []string{"I love", "Go Programming"}

  // join elements of array with space in between
  joinedString := strings.Join(stringArray, " ");
  fmt.Println(joinedString)

}
```

**Output**

golang strings
GOLANG STRINGS
I love Go Programming

In the above example, we have used functions of the `strings` package to perform various operations on the strings.

---

## Go Custom Package

So far, we have been using packages that are already defined inside the Go library. However, Go programming allows us to create our own custom packages and use them just like the predefined packages.

**1. Create Custom Package**

To create a custom package, we first need to create a new file and declare the package. For example,

```
// declare package
package calculator
```

Now, we can create functions inside the file. For example,

```
package calculator

// create add function
func Add(n1, n2 int) int {
  return n1 + n2
}

// create subtract function
func Subtract(n1, n2 int) int {
  return n1 - n2
}
```

In the above example, we have created a custom package named `calculator`. Inside the package, we have defined two functions: `Add()` and `Subtract()`.

**Note:** This file doesn't contain the main package. Hence, the Go compiler doesn't consider this as an executable program and it is created for the sole purpose of sharing and reusing.

**2. Importing Custom Package**

Now, we can import the custom package in our main file.

```
package main 

// import the custom package calculator
import (
  "fmt"
  "Packages/calculator"
)

func main() {

  number1 := 9
  number2 := 5

  // use the add function of calculator package
  fmt.Println(calculator.Add(number1, number2))

  // use the subtract function of calculator package
  fmt.Println(calculator.Subtract(number1, number2))

}
```

Here, we have successfully imported the calculator package in our program and used its functions.

**Note:** We have used `Packages/calculator` as the name of the package. This is because the calculator package is present inside the `Packages` folder and we are providing the path to that package from the location of the `main` file.

---

## Frequently Asked Questions

How to use name aliasing with Go packages?

What happens if we import a package but didn't use it in our program?