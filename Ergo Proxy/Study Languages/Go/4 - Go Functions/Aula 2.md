# Go Variable Scope

In Go, we can declare variables in two different scopes: local scope and global scope.

A variable scope specifies the region where we can access a variable. For example,

```
func addNumbers() {
  sum := 5 + 4
}
```

Here, the sum variable is created inside the function, so it can only be accessed within it (local scope). This type of variable is called a local variable.

Based on the scope, we can classify Go variables into two types:

- Local Variables
- Global Variables

---

## Go Local Variables

When we declare variables inside a function, these variables will have a local scope (within the function). We cannot access them outside the function.

These types of variables are called **local variables**. For example,

```
// Program to illustrate local variables

package main
import "fmt"

func addNumbers() {

  // local variables
  var sum int
  
  sum = 5 + 9

}


func main() {

  addNumbers()

  // cannot access sum out of its local scope
  fmt.Println("Sum is", sum)


}
```

**Output**

undefined: sum

Here, the sum variable is local to the `addNumbers()` function, so it can only be accessed within the function.

That's why we get an error when we try to access the function from `main()`.

To fix this issue, we can either return the value of the local variable and assign it to another variable inside the main function. Or we can make the variable sum global.

---

## Global Variables in Golang

When we declare variables before the `main()` function, these variables will have global scope. We can access them from any part of the program.

These types of variables are called global variables. For example,

```
// Program to illustrate global variable

package main
import "fmt"

// declare global variable before main function
var sum int

func addNumbers () {

  // local variable
  sum = 9 + 5
}


func main() {

  addNumbers()

  // can access sum
  fmt.Println("Sum is", sum)

}
```

**Output**

Sum is 14

This time we can access the sum variable from inside the `main()` function. This is because we have created the sum variable as the global variable.

```
// outside the function
var sum int
```

Now, the sum will be accessible from any scope (region) of the program.

---

## Frequently Asked Questions

What are the default values of local variables and global variables?

What happens if both local and global variables have the same name?

Why is local variables preferred over global variables?

- [](https://www.programiz.com/golang/variable-scope#introduction)
- [](https://www.programiz.com/golang/variable-scope#local-variables)
- [](https://www.programiz.com/golang/variable-scope#global-variables)