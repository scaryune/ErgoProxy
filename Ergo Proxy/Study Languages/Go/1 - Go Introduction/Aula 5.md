# Go Take Input

In Go, we use the `scan()` function to take input from the user. For example,

```
package main
import "fmt"

func main() {
  var name string

  // takes input value for name
  fmt.Print("Enter your name: ")
  fmt.Scan(&name)

  fmt.Printf("Name: %s", name)

}
```

**Output**

Enter your name: Rosie
Name: Rosie

In the above example, the line

```
fmt.Scan(&name)
```

takes input value from the user and assigns it to the `name` variable.

Go programming provides three different variations of the `Scan()` method:

- `fmt.Scan()`
- `fmt.Scanln()`
- `fmt.Scanf()`

**Note:** All these functions are defined under the `fmt` package. So, we must import the `fmt` package before we can use these functions.

---

## Go fmt.Scan()

As mentioned earlier, the `Scan()` function takes input from the user. However, it can only take input values up to a space.

When it encounters a space, the value before space is assigned to the specified variable. For example,

```
package main
import "fmt"

func main() {
  var language string

  // takes input value for name
  fmt.Print("Enter your favorite language: ")
  fmt.Scan(&language)

  fmt.Printf("Favorite Language: %s", language)

}
```

**Output**

Enter your favorite language: Go Programming
Favorite Language: Go

In the above example, we have provided the input value `Go Programming`. However, we are only getting `Go` as the output.

This is because the `Scan()` function only takes input value up to the space.

---

## Take Multiple Inputs Using Scan()

In Go, we can use the `Scan()` function to take multiple inputs from the user. For example,

```
package main
import "fmt"

func main() {
    
  // create variables
  var name string
  var age int
    
  // take name and age input
  fmt.Println("Enter your name and age:")
  fmt.Scan(&name, &age)
    
  // print input values
  fmt.Printf("Name: %s\nAge: %d", name, age)

} 
```

**Output**

Enter your name and age:
Maria
27
Name: Maria
Age: 27

In the above example, we have created two variables, name and age. Notice that we have used a single `Scan()` function to take input values for both variables.

```
fmt.Scan(&name, &age)
```

Here, we have provided two input values, `Maria` and **27** in two different lines (input values are separated by newline). In this case, the value in the first line is assigned to the name variable and the value in the second line is assigned to age.

We can also provide two values in a single line by separating them with space.

**Output**

Enter your name and age:
Maria 27
Name: Maria
Age: 27

In this case, the value before space is assigned to the first variable, name, and the value after space is assigned to the second variable, age.

---

## Go fmt.Scanln()

We use the `Scanln()` function to get input values up to the new line. When it encounters a new line, it stops taking input values. For example,

```
package main
import "fmt"

func main() {
  var name string
  var age int
    
  // take name and age input
  fmt.Println("Enter your name and age:")
  fmt.Scanln(&name, &age)
    
  fmt.Printf("Name: %s\nAge: %d", name, age)

}
```

**Output**

Enter your name and age:
Maria
Name: Maria
Age: 0

In the above example, we have used the `Scanln()` function to take two input values for name and age.

```
fmt.Scanln(&name, &age)
```

However, when we press enter after providing the first value, `Maria`, the program exits. This is because `Scanln()` only takes input value up to the new line, so when it encounters the enter after `Maria`, it stops taking input.

If we want to take input values for age, we must provide values separated by space.

**Output**

Enter your name and age:
Maria 27
Name: Maria
Age: 27

Here, we have separated two inputs by space, so `Scanln()` can take both input values.

---

## Go fmt.Scanf()

The `fmt.Scanf()` function is similar to `Scanln()` function. The only difference is that `Scanf()` takes inputs using format specifiers. For example,

```
// Program to take input from user using Scanf()

package main
import "fmt"

func main() {
  var name string
  var age int

  // take name and age input using format specifier
  fmt.Println("Enter your name and age:")
  fmt.Scanf("%s %d", &name, &age) 

  fmt.Printf("Name: %s\nAge: %d", name, age)
}
```

**Output**

Enter your name and age:
Maria 27
Name: Maria
Age: 27

In the above example, we have used the `Scanln()` function to take two input values for name and age using their respective format specifiers.

```
fmt.Scanf("%s %d", &name, &age) 
```

Here,

- `%s` - specifies the string input which is assigned to the name variable
- `%d` - specifies the integer input which is assigned to the age variable

Just like `Scanln()`, the `Scanf()` function takes values separated by space. When it encounters a new line, the `Scanf()` stops taking input values. That's why we have given inputs in the same line, separated by a space.

In Go, every data type has a unique format specifier and we can use them to take input values of each type using `Scanf()`.

|Data Type|Format Specifier|
|---|---|
|integer|`%d`|
|float|`%g`|
|string|`%s`|
|bool|`%t`|

---

### Take Input of Float and Boolean Type

```
package main
import "fmt"

func main() {
  var temperature float32
  var sunny bool

  // take float input
  fmt.Println("Enter the current temperature:")
  fmt.Scanf("%g", &temperature)

  // take boolean input
  fmt.Println("Is the day sunny?")
  fmt.Scanf("%t", &sunny)

  fmt.Printf("Current temperature: %g\nIs the day Sunny? %t", temperature, sunny)

}
```

**Output**

Enter the current temperature:
31.2
Is the day sunny?
true
Current temperature: 31.2
Is the day Sunny? true

In the above example, we have used `%g` to take the input of `float32` type and `%t` to take the input of `bool` type.

The input value **31.2** is assigned to the variable temperature and `true` is assigned to sunny.

- [](https://www.programiz.com/golang/take-input#go-scan)
- [](https://www.programiz.com/golang/take-input#take-multiple-inputs)
- [](https://www.programiz.com/golang/take-input#go-scanln)
- [](https://www.programiz.com/golang/take-input#go-scanf)
- [](https://www.programiz.com/golang/take-input#example-format)