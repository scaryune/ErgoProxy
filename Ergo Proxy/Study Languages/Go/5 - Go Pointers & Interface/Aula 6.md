# Golang Type Assertions

Type assertions allow us to access the data and data type of values stored by the interface.

Before we learn about type assertions, let's see why we need type assertions in Go.

We know that an empty interface can accept any type and number of values. For example,

```
// create an empty interface
var a interface {}

//  store value of string type
a = "Hello World"

// store value of integer type
a = 10
```

Here, the a variable is of empty interface type, and it is storing both the string and integer value. To learn more about empty interfaces, visit [Go Empty Interface](https://www.programiz.com/golang/interface).

This seems like an important feature of an empty interface. However, sometimes this will create ambiguity on what data an interface is holding.

To remove this ambiguity, we use type assertions.

---

## Example: Go Type Assertions

```
package main
import "fmt"

func main() {

  // create an empty interface
  var a interface {}

  // store integer to an empty interface
  a = 10

  // type assertion
  interfaceValue := a.(int)

  fmt.Println(interfaceValue)
}
```

**Output**

10

In the above example, we have stored the integer value **10** to the empty interface denoted by a. Notice the code,

```
interfaceValue := a.(int)
```

Here, `(int)` checks if the value of a is an integer or not. If `true`, the value will be assigned to interfaceValue.

Otherwise, the program panics and terminates. For example,

```
package main
import "fmt"

func main() {

  // create an empty interface
  var a interface{}

  // store integer to an empty interface
  a = "Golang"

  // type assertion
  interfaceValue := a.(int)

  fmt.Println(interfaceValue)
}
```

**Output**

panic: interface conversion: interface {} is string, not int

Here, the value of the interface is a string. So, `a.(int)` is not true. Hence, the program panics and terminates.

To learn more about panic, visit [Go panic Statement](https://www.programiz.com/golang/defer-panic-recover#panic-statement).

---

## Avoiding panic in Type Assertions in Go

In Go, the type assertion statement actually returns a boolean value along with the interface value. For example,

```
var a interface {}

a = 12
interfaceValue := a.(int)
```

Here, the data type of value **12** matches with the specified type `(int)`, so this code assigns the value of a to interfaceValue.

Along with this, `a.(int)` also returns a boolean value which we can store in another variable. For example,

```
package main
import "fmt"

func main() {

  // create an empty interface
  var a interface{}
  a = 12

  // type assertion
  interfaceValue, booleanValue := a.(int)

  fmt.Println("Interface Value:", interfaceValue)
  fmt.Println("Boolean Value:", booleanValue)

}
```

**Output**

Interface Value: 12
Boolean Value: true

Here, you can see we get both the data and boolean value.

We can use this to avoid panic if the data type doesn't match the specified type.

This is because, when the type doesn't match, it returns `false` as the boolean value, so the panic doesn't occur. For example,

```
package main
import "fmt"

func main() {

  // create an empty interface
  var a interface{}
  a = "Golang"

  // type assertion
  interfaceValue, booleanValue := a.(int)

  fmt.Println("Interface Value:", interfaceValue)
  fmt.Println("Boolean Value:", booleanValue)

}
```

**Output**

Interface Value: 0
Boolean Value: false

Here, you can see we get **0** and `false` as output because the data type of value `(string)` doesn't match with the specified type `(int)`.