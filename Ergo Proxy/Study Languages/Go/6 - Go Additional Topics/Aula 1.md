# Go Errors

In programming, there will be situations where our program won't run properly and generate an error. For example,

```
package main
import "fmt"

func main() {

  for i := 0; i < 5; i++ {
    result := 20 / i
    fmt.Println(result)
  }
}
```

When we run this code, we will get an error called **integer divide by zero**.

During the first iteration, the value of i is **0**, so the code `result := 20 / i` is trying to divide a number by **0**.

In this state, the program stops its execution known as a Go error. Here, **"integer divide by zero"** is an error message returned by the compiler.

**Note:** The error we get in our previous example is a built-in error. In Go, we can also create our own errors for efficient programming.

---

### Golang Error Handling

When an error occurs, the execution of a program stops completely with a built-in error message. In Go, we . Hence, it is important to handle those exceptions in our program.

Unlike other programming languages, we don't use **try/catch** to handle errors in Go. We can handle errors using:

- `New()` Function
- `Errof()` Function

---

## 1. Go Error using New() Function

In Go, we can use the `New()` function to handle an error. This function is defined inside the `errors` package and allows us to create our own error message.

Let's see an example,

```
package main

// import the errors package
import (
  "errors"
  "fmt"
)

func main() {

  message := "Hello"

  // create error using New() function
  myError := errors.New("WRONG MESSAGE")

if message != "Programiz" {
  fmt.Println(myError)
}
  
}
```

**Output**

WRONG MESSAGE

In the above example, we have created an error using the `errors.New()` function.

```
myError := errors.New("WRONG MESSAGE") 
```

Here, the **"WRONG MESSAGE"** inside the `New()` function is the custom error message. It prints when the message variable does not match with the given string **"PROGRAMIZ"**.

---

### Example: Error using New()

```
package main

// import the errors package
import (
  "errors"
  "fmt"
)

// function that checks if name is Programiz
func checkName(name string) error {

  // create a new error
  newError := errors.New("Invalid Name")

  // return the error if name is not Programiz
  if name != "Programiz" {
    return newError
  }

  // return nil if there is no error
  return nil
}

func main() {

  name := "Hello"

  // call the function
  err := checkName(name)

  // check if the err is nil or not
  if err != nil {
    fmt.Println(err)
  } else {
    fmt.Println("Valid Name")
  }

}
```

**Output**

Invalid Name

In the above example, we have created a function named `checkName()`

```
checkName(name string) error {...}
```

The return of this function is an `error`, which means this function will return a value of error type

Inside the function, we have created an error using the `New()` function. Here, if the name is not **Programiz**, we are returning the newly created error message.

However, if the name is **Programiz**, we are returning `nil` (represents no error).

Inside the `main()` function, we have called the `checkName()` function using

`err := checkName(name)`

Here, the returned error will be assigned to `err`. We then checked if the value in `err` is nil or not.

---

## 2. Error using Errorf() in Golang

We can also handle Go errors using the `Errorf()` function. Unlike, `New()`, we can format the error message using `Errorf()`.

This function is present inside the `fmt` package, so we can directly use this if we have imported the `fmt` package.

Let's see an example.

```
package main
import "fmt"

func main() {

  age := -14

  // create an error using Efforf()
  error := fmt.Errorf("%d is negative\nAge can't be negative", age)

  if age < 0 {
    fmt.Println(error)
  } else {
  fmt.Println("Age: %d", age);
  }
}
```

**Output**

-14 is negative
Age can't be negative

In the above example, we have used the `Errorf()` function to create a new formatted error.

```
error := fmt.Errorf("%d is negative\nAge can't be negative", age)
```

Here, you can see we have used the format specifier `%d` to use the value of age inside our error.

---

### Example: Error using Errorf()

```
package main
import "fmt"

func divide(num1, num2 int) error {

  // returns error
  if num2 == 0 {
    return fmt.Errorf("%d / %d\nCannot Divide a Number by zero", num1, num2)
  }

  // returns the result of division
  return nil
}

func main() {

  err := divide(4,0)

  // error found
  if err != nil {
    fmt.Printf("error: %s", err)

  // error not found
  } else {
    fmt.Println("Valid Division")
  }
}
```

**Output**

error: 4 / 0
Cannot Divide a Number by zero

In the above example, we have created a function named `divide()`.

```
func divide(num1, num2 int) error {...}
```

The return of this function is an `error,` which means this function will return an error value.

Inside the function, we have created a formatted error using the `Errorf()`. If the condition `num2==0` is true, the function divide returns the error message inside the `Errorf()`.

However, if num2 is not **0**, we are returning `nil`, which represents that there is no error.

---

## Custom Errors in Golang

In Go, we can create custom errors by implementing an `error` interface in a struct.

**error Interface**

```
type error interface {
  Error() string
}
```

Here, the `Error()` method returns an error message in string form if there is an error. Otherwise, it returns `nil`.

Now, to create a custom error, we have to implement the `Error()` method on a [Go struct](http://programiz.com/golang/struct).

Let's see an example,

```
package main

import "fmt"

type DivisionByZero struct {
  message string
}

// define Error() method on the struct
func (z DivisionByZero) Error() string {
  return "Number Cannot Be Divided by Zero"
}

func divide(n1 int, n2 int) (int, error) {

  if n2 == 0 {
    return 0, &DivisionByZero{}
  } else {
    return n1 / n2, nil
  }
}

func main() {

  number1 := 15
  // change the value of number2 to get different result
  number2 := 0

  result, err := divide(number1, number2)

  // check if error occur or not
  if err != nil {
    fmt.Println(err)
  } else {
    fmt.Printf("Result: %d", result)
  }
}
```

**Output**

Number Cannot Be Divided by Zero

In the above example, we are implementing the `Error()` method of the `error` interface on the `DivisionByZero` struct.

```
func (z DivisionByZero) Error() string {
  return "Number Cannot Be Divided by Zero"
}
```

Here,

- `z DivisionByZero` - an instance of the `DivisionByZero` struct
- `string` - return type of the method
- `"Number Cannot Be Divided by Zero"` - error message

We have then created a `divide()` method that takes two parameters and returns the result and an `error`.

```
func divide(n1 int, n2 int) (int, error) {...}
```

The function returns **0** and `&DivisionByZero{}`, if the value of n2 is **0**. Here, `&DivisionByZero{}` is an instance of the struct. To learn more, visit [Go Pointers to Struct](https://www.programiz.com/golang/pointers-struct).

Inside the `main()` function, if the returned error type is not `nil`, we print the error message.

Note that we are not calling the `Error()` method from anywhere in the program, but we can access its return value using the struct instance.

- [](https://www.programiz.com/golang/errors#introduction)
- [](https://www.programiz.com/golang/errors#new-error)
- [](https://www.programiz.com/golang/errors#errorf-function)
- [](https://www.programiz.com/golang/errors#custom-error)

[

  


](https://www.programiz.com/golang/type-assertions "Go Type Assertions")