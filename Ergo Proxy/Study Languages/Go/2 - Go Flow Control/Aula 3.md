# Go switch

In Go, the switch statement allows us to execute one code block among many alternatives.

**Syntax**

```
switch expression {
  case 1:
    // code block 1

  case 2:
    // code block 2

  case 3:
    // code block 3
  ...
  ...
   	 
  default:
    // default code block
}
```

The expression after the `switch` keyword is evaluated. If the result of the `expression` is equal to

- `case 1` - **code block 1** is executed
- `case 2` - **code block 2** is executed
- `case 3` - **code block 3** is executed

In case there is no match, the **default code block** is executed.

**Note**: We can also use `if...else` statements in place of `switch`. However, the syntax of the switch is much cleaner and easier to write.

---

## Flowchart of Switch Statement

![Flowchart of Switch Statement in Go](https://www.programiz.com/sites/tutorial2program/files/golang-switch-flowchart.png "Flowchart of Switch Statement in Go")

Flowchart of Switch Statement in Go

---

## Example: switch case in Golang

```
// Program to print the day of the week using  switch case

package main
import "fmt"

func main() {
  dayOfWeek := 3

  switch dayOfWeek {

    case 1:
      fmt.Println("Sunday")
   	 
    case 2:
      fmt.Println("Monday")
   	 
    case 3:
      fmt.Println("Tuesday")
   	 
    case 4:
      fmt.Println("Wednesday")
   	 
    case 5:
      fmt.Println("Thursday")
   	 
    case 6:
      fmt.Println("Friday")
   	 
    case 7:
      fmt.Println("Saturday")
   	 
    default:
      fmt.Println("Invalid day")
  }
}
```

**Output**

Tuesday

In the above example, we have assigned `3` to the `dayOfWeek` variable. Now, the variable is compared with the value of each case statement.

Since the value matches with `case 3`, the statement `fmt.Println("Tuesday")` inside the case is executed.

**Note**: Unlike other programming languages like C and Java, we don't need to use `break` after every case. This is because in Go, the switch statement terminates after the first matching case.

---

## Go switch case with fallthrough

If we need to execute other cases after the matching case, we can use `fallthrough` inside the case statement. For example,

```
// Program to print the day of the week using fallthrough in switch

package main
import "fmt"

func main() {
  dayOfWeek := 3

  switch dayOfWeek {
    case 1:
      fmt.Println("Sunday")
   	 
    case 2:
      fmt.Println("Monday")
   	 
    case 3:
      fmt.Println("Tuesday")
      fallthrough
   	 
    case 4:
      fmt.Println("Wednesday")
      	 
    case 5:
      fmt.Println("Thursday")
   	 
    case 6:
      fmt.Println("Friday")
   	 
    case 7:
      fmt.Println("Saturday")
   	 
    default:
      fmt.Println("Invalid day")
  }
}
```

**Output**

Tuesday
Wednesday

In the above example, the expression in switch matches `case 3` so, `Tuesday` is printed. However, `Wednesday` is also printed even if the case doesn't match.

This is because we have used `fallthrough` inside `case 3`.

---

## Go switch with multiple cases

We can also use multiple values inside a single case block. In such case, the case block is executed if the expression matches with one of the case values.

Let's see an example,

```
// Program to check if the day is a weekend or a weekday

package main
import "fmt"

func main() {
  dayOfWeek := "Sunday"

  switch dayOfWeek {
    case "Saturday", "Sunday":
      fmt.Println("Weekend")

    case "Monday","Tuesday","Wednesday","Thursday","Friday":
      fmt.Println("Weekday")

    default:
      fmt.Println("Invalid day")
  }
}
```

**Output**

Weekend

In the above example, we have used multiple values for each case:

- **case "Saturday", "Sunday"** - executes if dayOfWeek is either Saturday or Sunday
- **case "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"** - executes if dayOfWeek is either one of the value

---

## Golang switch without expression

In Go, the expression in switch is optional. If we don't use the expression, the switch statement is `true` by default. For example,

```
// Program to check if it's February or not using switch without expression

package main
import "fmt"

func main() {
  numberOfDays := 28

  // switch without any expression
  switch {

    case 28 == numberOfDays:
      fmt.Println("It's February")
        	 
    default:
      fmt.Println("Not February")
  }
}
```

**Output**

It's February

In the above example, switch doesn't have an expression. Hence, the statement is `true`.

---

## Go switch optional statement

In Golang, we can also use an optional statement along with the expression. The statement and expression are separated by semicolons. For example,

```
// Program to check the day of a week using optional statement

package main
import "fmt"

func main() {

  // switch with statement
  switch day := 4; day {

    case 1:
      fmt.Println("Sunday")

    case 2:
      fmt.Println("Monday")

    case 3:
      fmt.Println("Tuesday")

    case 4:
      fmt.Println("Wednesday")

    case 5:
      fmt.Println("Thursday")

    case 6:
      fmt.Println("Friday") 
   
    case 7:
      fmt.Println("Saturday")

    default:
      fmt.Println("Invalid Day!")
  }
}
```

**Output**

Wednesday

In the above example, we have used the optional statement `day := 4` along with the expression `day`. It matches **case 4** and hence, **Wednesday** is printed.

- [](https://www.programiz.com/golang/switch#flowchart)
- [](https://www.programiz.com/golang/switch#switch-example)
- [](https://www.programiz.com/golang/switch#switch-fallthrough)
- [](https://www.programiz.com/golang/switch#multiple-cases)
- [](https://www.programiz.com/golang/switch#without-expression)
- [](https://www.programiz.com/golang/switch#optional)

[

  


](https://www.programiz.com/golang/if-else "Go if...else")