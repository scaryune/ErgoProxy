# Go Pointers and Functions

Go pointers store the memory addresses of variables. And just like regular variables, we can also pass pointers to functions.

Before you learn how to use pointers with functions, make sure to know about

- [Go Pointers](http://programiz.com/golang/pointers)
- [Functions in Golang](http://programiz.com/golang/function)

---

## Pointer as Function Argument in Golang

In Go, we can pass pointers as arguments to a function. For example,

```
// Program to pass pointer as a function argument

package main
import "fmt"

// function definition with a pointer argument
func update(num *int) {

  // dereference the pointer
  *num = 30

} 

func main() {
 
  var number = 55

  // function call
  update(&number)
  
  fmt.Println("The number is", number)

}
```

**Output**

The number is 30

In the above example, we have passed the address of number to the `update()` function. The pointer num accepts this argument in the function definition.

```
func update(num *int) {
  ...
}
```

When we change `*num` to **30** inside the `update()` function, the value of number inside the `main()` function is also changed.

This is because num and number are referring to the same address in the memory. So, updating one updates the other as well.

---

## Return Pointers From Function

Just like regular variables, we can also return pointers from a function. For example,

```
// Program to return a pointer from a function

package main
import "fmt"
 
func main() {

  // function call
  result := display() 
  fmt.Println("Welcome to", *result)

} 

func display() *string {

  message := "Programiz"

  // returns the address of message
  return &message

}
```

**Output**

Welcome to Programiz

In the above example, we have created a function named `display()` that returns a pointer.

```
func display() *string
```

Here, `*string` indicates that the function returns a pointer of `string` type.

Notice the `return &message` statement in the `display()` function:

```
func display() *string {
  ...
  return &message
} 
```

This indicates that the function returns the address of the message variable to the `main()` function.

The returned address is assigned to the result pointer. To get the value stored in the memory address, we have used the code `*result`.

---

## Call By Reference

While passing pointers to a function, we are actually passing a reference (address) of the variable. Instead of working with the actual value, we are working with references like

- accessing value using reference
- changing value using reference

That's why this process of calling a function with pointers is called **call by reference** in Go.

Let's see an example.

```
// Program to illustrate call by reference

package main
import "fmt"

// call by value
func callByValue(num int) {

  num = 30
  fmt.Println( num) // 30

} 

// call by reference
func callByReference(num *int) {
    
  *num = 10
  fmt.Println(*num) // 10

} 

func main() {
 
  var number int

  // passing value
  callByValue(number)

  // passing a reference (address)
  callByReference(&number)

}
```

Here, we have created two functions: `callByValue()` and `callByReference()`.

	In the `callByValue()` function, we are directly passing the number variable. Whereas in `callByReference()`, we are passing the memory address of number.