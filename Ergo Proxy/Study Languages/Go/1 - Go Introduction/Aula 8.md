# Go Type Casting

Type casting is the process of converting the value of one data type (integer, float, string) to another data type. For example,

```
// variable of float type
var floatValue float = 9.8

// convert float to int
var intValue int = int(floatValue)
```

Here, `int(floatValue)` specifies that we are converting the float value **9.8** to **9**.

Since we are manually performing the type conversion, this is called **explicit type casting in Go**.

---

## Go Explicit Type Casting

Golang provides various predefined functions like `int()`, `float32()`, `string()`, etc to perform explicit type casting.

Let's see some of the examples of explicit type casting:

### Example: Go float to int conversion

```
package main
import "fmt"

func main() {
  
  var floatValue float32 = 5.45

  // type conversion from float to int
  var intValue int = int(floatValue)
 
  fmt.Printf("Float Value is %g\n", floatValue)
  fmt.Printf("Integer Value is %d", intValue)
}
```

**Output**

Float Value is 5.45
Integer Value is 5

Here, we have used the function `int()` to convert the value from **5.45** to **5**.

In this case, we are manually converting the type of one type to another. **Hence, it is called explicit type casting.**

---

### Example: Go int to float conversion

```
package main
import "fmt"

func main() {
  
  var intValue int = 2

  // type conversion from int to float
  var floatValue float32 = float32(intValue)
 
  
  fmt.Printf("Integer Value is %d\n", intValue)
  fmt.Printf("Float Value is %f", floatValue)

}
```

**Output:**

Integer Value is 2
Float Value is 2.000000

Here, we have used the function `float32()` to convert an integer value to float. The integer value **2** changed to **2.000000** after the type casting.

---

## Implicit Type Casting in Go

In implicit type casting, one data type is automatically converted to another data type. However, Go doesn't support implicit type casting. For example,

```
package main
import "fmt"

func main() {
  
  // initialize integer variable to a floating-point number
  var number int = 4.34

  fmt.Printf("Number is %g", number)
}
```

In the above example, we have created an `int` type variable named number. Here, we are trying to assign a floating point value **4.34** to the `int` variable.

When we run this program, we will get an error:

```
./prog.go:8:7: constant 4.34 truncated to integer
```

This is because Golang doesn't support implicit type conversion.

---

## Example: Add int and float number using Go type casting

```
package main
import "fmt"

func main() {
  
  var number1 int = 20
  var number2 float32 = 5.7
  var sum float32
 
  // addition of different data types
  sum = float32(number1) + number2

  fmt.Printf("Sum is %g",sum)
}
```

**Output:**

Sum is 25.7

In the above example, we have created an integer variable named number1 and a float variable named number2. Notice the line,

```
sum = float32(number1) + number2
```

Here, we are adding values of two different types (`float` and `int`). Since Go doesn't support implicit type casting, we need to change the value of one type to another.

This is why we have used `float32(number1)` to convert the `int` type variable number to `float` type.

- [](https://www.programiz.com/golang/type-casting#introduction)
- [](https://www.programiz.com/golang/type-casting#explicit-casting)
- [](https://www.programiz.com/golang/type-casting#int-to-float)
- [](https://www.programiz.com/golang/type-casting#implicit-casting)
- [](https://www.programiz.com/golang/type-casting#add-int-and-float)