# Go Empty Interface

We know that interfaces are used to store a set of methods without implementation. In Go, we can also create interfaces without any methods, known as empty interfaces. For example,

```
interface {}
```

Here, we have created an empty interface without any methods.

---

## Variable of Empty Interface in Golang

In Go, we can create variables of the empty interface type. For example,

```
package main
import "fmt"

func main() {

  // variable of empty interface type
  var a interface {}
  fmt.Println("Value:", a)

}
```

**Output**

Value: <nil>

Here, we have created a variable of type empty interface. When we print the variable, we get `nil` as output.

---

## Empty Interface to Pass Function Argument of Any Type

Normally in functions, when we pass values to the function parameters, we need to specify the data type of parameters in a function definition.

However, with an empty interface, we can pass parameters of any data type. For example,

```
package main
import "fmt"

// empty interface as function parameter
func displayValue(i interface {}) {
  fmt.Println(i)
}

func main() {

  a := "Welcome to Programiz"
  b := 20
  c := false

  // pass string to the function 
  displayValue(a)

  // pass integer number to the function
  displayValue(b)

  // pass boolean value to the function
  displayValue(c)

}
```

**Output**

Welcome to Programiz
20
false

In the above example, we have used an empty interface `i` as the parameter to the `displayValue()` function.

Now the same function works for any type of parameters (string,numeric, boolean).

---

## Go Empty Interface to Pass Any Numbers of Arguments

We can also use an empty interface to pass any number of arguments to the function definition. For example,

```
package main
import "fmt"

// function with an empty interface as its parameter
func displayValue(i... interface {}) {
  fmt.Println(i)
}

func main() {

  a := "Welcome to Programiz"
  b := 20
  c := false

  // function call with a single parameter
  displayValue(a)

  // function call with 2 parameters
  displayValue(a, b)

  // function call with 3 parameters
  displayValue(a, b, c)

}
```

**Output**

[Welcome to Programiz 20 false 20 40 Hi again]

In the above example, we have used an empty interface i as the parameter to the `displayValue()` function.

```
func displayValue(i... interface{})
```

Now the same function works for any number of parameters.