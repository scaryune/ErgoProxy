# o Data Types

We use data types in Golang to determine the type of data associated with variables. For example,

```
var age int
```

Here, `int` is a data type that specifies that the `age` variable can store integer data.

The basic data types in Golang are

|Data Types|Description|Examples|
|---|---|---|
|`int`|Integer numbers.|`7123`, `0`, `-5`, `7023`|
|`float`|Numbers with decimal points.|`20.2`, `500.123456`, `-34.23`|
|`complex`|Complex numbers.|`2+4i`, `-9.5+18.3i`|
|`string`|Sequence of characters.|`"Hello World!"`, `"1 is less than 2"`|
|`bool`|Either true or false.|`true`, `false`|
|`byte`|A byte (8 bits) of non-negative integers.|`2`, `115`, `97`|
|`rune`|Used for characters. Internally used as 32-bit integers.|`'a'`, `'7'`, `'<'`|

Now, let's discuss the commonly used data types in detail.

---

## 1. Integer Data Type

Integers are whole numbers that can have both zero, positive and negative values but no decimal values. For example, `0`, `5`, `-1340`.

We commonly use the `int` keyword to declare integer numbers.

```
var id int
```

Here, id is a variable of type integer.

You can declare multiple variables at once in the same line.

```
var id, age int
```

In Go programming, there are two types of integers:

- signed integer `int` - can hold both positive and negative integers
- unsigned integer `uint` - can only hold positive integers

There are different variations of integers in Go programming.

|Data type|Size|
|---|---|
|int/uint|either 32 bits (4 bytes) or 64 bits (8 bytes)|
|int8/uint8|8 bits (1 byte)|
|int16/uint16|16 bits (2 bytes)|
|int32/uint32|32 bits (4 bytes)|
|int64/uint64|64 bits ( 8 bytes)|

**Note**: Unless we have a specific requirement, we usually use the int keyword to create integers.

---

### Example 1: Understanding Integer Type

```
package main
import "fmt"

func main() {
  var integer1 int
  var integer2 int

  integer1 = 5
  integer2 = 10

  fmt.Println(integer1)
  fmt.Print(integer1)
}
```

**Output**

5
10

If you want to learn more about creating variables, visit [Go Variables](https://www.programiz.com/golang/variables-constants).

---

## 2. Float Data Type

The float type is used to hold values with decimal points. For example, `6.7`, `-34.2`  
  
**Keywords used:** `float32`, `float64`

Here's an example,

```
var salary float64
```

There are two sizes of floating-point data in Go programming.

|Data Type|Size|
|---|---|
|float32|32 bits (4 bytes)|
|float64|64 bits (8 bytes)|

**Note**: If we define float variables without specifying size explicitly, the size of the variable will be 64 bits. For example,

```
// the size of the variable is 64
salary := 5676.3
```

---

### Example 2: Understanding Float Type

```
// Program to illustrate float32 and float64 with example

package main
import "fmt"

func main() {
  var salary1 float32
  var salary2 float64

  salary1 = 50000.503882901

  // can store decimals with greater precision
  salary2 = 50000.503882901

  fmt.Println(salary1) 
  fmt.Println(salary2)

}
```

**Output**

50000.504
50000.503882901

---

## 3. String Data Type

A string is a sequence of characters. For example, `"Hello"`, `"Hey there"`

**Keyword:** `string`

Here's an example,

```
var message string
```

In Go, we use either double quotes or backticks to create strings.

```
var message string = "Hello World "
var message string =  `Hello World`
```

---

### Example 3: Understanding String Type

```
// Program to create string variables

package main
import "fmt"

func main() {
  var message string
  message = "Welcome to Programiz"

  fmt.Println(message)

}
```

**Output**

Welcome to Programiz

## 4. Boolean Data Type

The boolean data type has one of two possible values either `true` or `false`.

**Keyword**: `bool`

```
var isValid bool
```

---

### Example 4: Understanding bool Type

```
// Program to create boolean variables

package main
import "fmt"

func main() {
  var boolValue bool
  boolValue = false

  fmt.Println(boolValue)
}
```

**Output**

false

We will learn about booleans in detail in the [_Go Comparison and Logical Operators_](https://www.programiz.com/golang/boolean-expression) tutorial.