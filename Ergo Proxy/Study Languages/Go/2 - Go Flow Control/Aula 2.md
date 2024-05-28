# Go if else

In computer programming, we use the if statement to run a block code only when a certain condition is met.

For example, assigning grades **(A, B, C)** based on marks obtained by a student.

- if the percentage is above **90**, assign grade **A**
- if the percentage is above **75**, assign grade **B**
- if the percentage is above **65**, assign grade **C**

---

## Go if statement

The syntax of the `if` statement in Go programming is:

```
if test_condition {
   // code
}
```

If **test_condition** evaluates to

- `true` - statements inside the body of `if` are executed.
- `false` - statements inside the body of `if` are not executed.

![Working of if statement in Go programming](https://www.programiz.com/sites/tutorial2program/files/golang-if-statement.png "Working of if statement in Go")

Working of if statement in Go programming

---

### Example: Simple if statement in Golang

```
// Program to display a number if it is positive

package main
import "fmt"

func main() {
  number := 15

  // true if number is less than 0
  if number > 0 {
    fmt.Printf("%d is a positive number\n", number)
  }

  fmt.Println("Out of the loop")
}
```

**Output**

The positive number is 15
Out of the loop

In the above example, we have created a variable named number. Notice the **test_condition**,

```
number > 0
```

Here, since the variable number is greater than **0**, the **test_condition** evaluates `true`.

If we change the variable to a negative integer. Let's say **-5**.

```
number := -5
```

Now, when we run the program, the output will be:

Keep Learning

This is because the value of number is less than **0**. Hence, the **test_condition** evaluates to `false`. And, the body of the `if` block is skipped.

---

## Go if...else statement

The `if` statement may have an optional `else` block. The syntax of the `if..else` statement is:

```
if test_condition {
    // run code if test_condition is true
} else {
    // run code if test_condition is false
}
```

If **test_condition** evaluates to `true`,

- the code inside `if` is executed
- the code inside `else` is skipped

If **test_condition** evaluates to `false`,

- the code inside `else` is executed
- the code inside `if` is skipped

![Working of if...else in Go programming](https://www.programiz.com/sites/tutorial2program/files/if-else-golang.png "Working of if..else in Go")

Working of if...else in Go programming

---

### Example: if...else statement in Golang

```
package main
import "fmt"

func main() {
  number := 10

  // checks if number is greater than 0
  if number > 0 {
    fmt.Printf("%d is a positive number\n", number)
  } else {
    fmt.Printf("%d is a negative number\n", number)
  }
}
```

**Output**

10 is a positive number

The number is **10**, so the test condition `number > 0` is evaluated to be `true`. Hence, the statement inside the body of `if` is executed.

If we change the variable to a negative integer. Let's say **-5**.

```
number := -5
```

Now if we run the program, the output will be:

```
-5 is a negative number
```

Here, the test condition evaluates to `false`. Hence code inside the body of `else` is executed.

**Note**: The `else` statement must start in the same line where the `if` statement ends.

---

## Go if...else if ladder

The `if...else` statement is used to execute a block of code among two alternatives.

However, if you need to make a choice between more than two alternatives, then we use the `else if` statement.

```
if test_condition1 {
   // code block 1
} else if test_condition2 {
   // code block 2
}.
.
.
} else {
   // code block 3
}
```

Here,

**if test_condition1 evaluates to true**

- `code block 1` is executed
- `code block 2` and `code block 3` are skipped

**if test_condition2 evaluates to true**

- `code block 2` is executed
- `code block 1` and `code block 3` are skipped

**if both test conditions evaluates to false**

- `code block 3` is executed
- `code block 1` and `code block 2` are skipped

![Working of if.. else if..else in Go programming.](https://www.programiz.com/sites/tutorial2program/files/golang-if-else-ladder.png "Working of if..else if ladder in Go")

Working of if.. else if..else in Go programming.

---

### Example: if...if else ladder statement in Golang

```
// Program to relate two integers using =, > or < symbol

package main
import "fmt"

func main() {

  number1 := 12
  number2 := 20

  if number1 == number2 {
    fmt.Printf("Result: %d == %d", number1, number2)
  } else if number1 > number2 {
    fmt.Printf("Result: %d > %d", number1, number2)
  } else {
    fmt.Printf("Result: %d < %d", number1, number2)     
  }
}
```

**Output**

Result: 12 < 20

Here, both the test conditions `number1 == number2` and `number1 > number2` are `false`. Hence the code inside the `else` block is executed.

---

## Go nested if statement

You can also use an `if` statement inside of an `if` statement. This is known as a **nested if** statement.

```
// outer if statement
if test_condition1 {
  // statements

  // inner if...else statement
  if test_condition2 {
    // statements
  }else {
    // statements
  }
}
```

---

### Example: Nested if statement in Golang

```
package main
import "fmt"

func main() {

  number1 := 12
  number2 := 20

  // outer if statement
  if number1 >= number2 {

  // inner if statement
  if number1 == number2 {
    fmt.Printf("Result: %d == %d", number1, number2)
    // inner else statement
  } else {
    fmt.Printf("Result: %d > %d", number1, number2)
  } 

  // outer else statement
  } else {
    fmt.Printf("Result: %d < %d", number1, number2)
  }
}
```

**Output**

Result: 12 < 20

If the outer condition `number1 >= number2` is `true`

- inner `if` condition `number1 == number2` is checked
- if condition is `true`, code inside the inner `if` is executed
- if condition is `false`, code inside the inner `else` is executed

If the outer condition is `false`, the outer `else` statement is executed.

- [](https://www.programiz.com/golang/if-else#introduction)
- [](https://www.programiz.com/golang/if-else#if)
- [](https://www.programiz.com/golang/if-else#if-else)
- [](https://www.programiz.com/golang/if-else#if-else-ladder)
- [](https://www.programiz.com/golang/if-else#nested-if)