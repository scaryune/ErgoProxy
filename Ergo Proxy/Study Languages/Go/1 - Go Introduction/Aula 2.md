# Go Variables and Constants

## Go Variables

In programming, a variable is a container that is used to store data. Here's how we can declare a variable in Go programming.

```
var number int
```

Here,

- number - name of the variable
- `var` - keyword used to declare variable
- `int` - data type associated with the variable

**Note:** In Go, every variable has a fixed data type associated with it. The data type determines the type of data that the variable can store.

For example, the number variable can only store integer data. It's because its type is `int`.

We will learn about different types of [data types](https://www.programiz.com/golang/data-types "Go Data Types") in detail in the next tutorial.

---

## Assign Values to Go Variables

There are 3 ways to assign values to a variable.

**Method 1**

```
var number int = 10 
```

Here, we have assigned an integer value **10** to the number variable.

**Method 2**

```
var number = 10
```

Here, we are not explicitly specifying the data type of the variable. In this case, the compiler automatically detects the type by looking at the value of the variable.

Since the value **10** is an integer, the data type of number is `int`.

**Method 3**

```
number := 10
```

Here, we are using the `:=` operator to assign the value **10** to the variable number. This is the shorthand notation to assign values to variables.

---

### Important Notes on Go Variables

1. If a variable is not assigned any value, a default value is assigned to it. For example,

```
var count int
fmt.Println(count)
```

Here, the count variable prints **0** (default value for `int`) because we haven't assigned any value to it.

2. In Go, every variable must have a data type associated with it. If not, the program throws an error.

```
// Error: count variable doesn't have a data type
var count

// count1 is of the int type
var count1 int

// count2 is of the int type
var count2 = 10
```

---

## Example: Go Variables

```
package main
import "fmt"

func main() {
 
  // explicitly declare the data type
  var number1 int = 10
  fmt.Println(number1)

 // assign a value without declaring the data type
  var number2 = 20
  fmt.Println(number2)

  // shorthand notation to define variable
  number3 := 30
  fmt.Println(number3)  
}
```

**Output**

10
20
30

---

## Changing Value of a Variable

As suggested by the name **variable**, we can change the value stored in a variable. For example,

```
// initial value
number := 10
fmt.println("Initial number value", number) // prints 10

// change variable value
number = 100
fmt.Println("The changed value", number)  // prints 100
```

Initially, **10** was stored in the variable. Then, its value is changed to **100**.

**Note**: In Go, we cannot change the type of variables after it is declared.

In the above example, the number variable can only store integer values. It cannot be used to store other types of data. For example,

```
number := 10

// Error code
// assign string data
number = "Hello" 
```

---

## Creating Multiple Variables at Once

In Go, it's also possible to declare multiple variables at once by separating them with commas. For example,

```
var name, age = "Palistha", 22
```

Here, "Palistha" is assigned to the name variable. Similarly, **22** is assigned to the age variable.

The same code above can also be written as:

```
name, age := "Palistha", 22
```

---

### Rules of naming Variables

- A variable name consists of alphabets, digits, and an underscore.
- Variables cannot have other symbols ( $, @, #, etc).
- Variable names cannot begin with a number.
- A variable name cannot be a reserved word as they are part of the Go syntax like `int`, `type`, `for`, etc.

By the way, we should always try to give meaningful variable names. This makes your code easier to read and understand.

|Illegal Variable|Bad Variable|Good Variable|
|---|---|---|
|1a|a|age|
|s@lary|sal|salary|
|first name|fn|firstName|
|annual-income|annInc|annualIncome|

---

## Constant in Go

Constants are the fixed values that cannot be changed once declared. In Go, we use the `const` keyword to create **constant variables**. For example,

```
const lightSpeed = 299792458 // initial value

// Error! Constants cannot be changed
lightSpeed = 299792460
```

By the way, we cannot use the shorthand notation `:=` to create constants. For example,

```
// Error code
const lightSpeed := 299792458
```

- [](https://www.programiz.com/golang/variables-constants#variable)
- [](https://www.programiz.com/golang/variables-constants#assign-values)
- [](https://www.programiz.com/golang/variables-constants#example)
- [](https://www.programiz.com/golang/variables-constants#changing-value)
- [](https://www.programiz.com/golang/variables-constants#multiple-variables)
- [](https://www.programiz.com/golang/variables-constants#constant)