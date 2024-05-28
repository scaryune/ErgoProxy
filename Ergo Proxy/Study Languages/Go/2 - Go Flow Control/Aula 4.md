# Go for Loop

In programming, a loop is used to repeat a block of code. For example,

If we want to print a statement 100 times, instead of writing the same print statement 100 times, we can use a loop to execute the same code 100 times.

This is just a simple example; we use `for` loops to clean and simplify complex programs.

---

## Golang for loop

In Golang, we use the `for` loop to repeat a block of code until the specified condition is met.

Here's the syntax of the `for` loop in Golang.

```
for initialization; condition; update {
  statement(s)
}
```

Here,

1. The **initialization** initializes and/or declares variables and is executed only once.
2. Then, the **condition** is evaluated. If the condition is `true`, the body of the for loop is executed.
3. The **update** updates the value of **initialization**.
4. The **condition** is evaluated again. The process continues until the condition is `false`.
5. If the **condition** is `false`, the for loop ends.

---

## Working of for loop

![Working of for loop in Golang programming](https://www.programiz.com/sites/tutorial2program/files/golang-for-loop-flowcontrol.png "Flow Diagram of for loop in Go")

Flow Diagram of for loop in Go

---

## Example 1: Golang for loop

```
// Program to print the first 5 natural numbers

package main
import "fmt"

func main() {

  // for loop terminates when i becomes 6
  for i := 1; i <= 5; i++ {
    fmt.Println(i)
  }

}
```

**Output**

1
2
3
4
5

Here is how this program works.

|Iteration|Variable|Condition: i|Action|
|---|---|---|---|
|1st|`i = 1`|`true`|`1` is printed.  <br>i is increased to **2**.|
|2nd|`i = 2`|`true`|`2` is printed.  <br>i is increased to **3**.|
|3rd|`i = 3`|`true`|`3` is printed.  <br>i is increased to **4**.|
|4th|`i = 4`|`true`|`4` is printed.  <br>i is increased to **5**.|
|5th|`i = 5`|`true`|`5` is printed.  <br>i is increased to **6**.|
|6th|`i = 6`|`false`|The loop is terminated.|

---

## Example 2: Golang for loop

```
// Program to print numbers for natural numbers 1 + 2 + 3 + ... +n

package main
import "fmt"

func main() {
  var n, sum = 10, 0
  
  for i := 1 ; i <= n; i++ {
    sum += i    // sum = sum + i  
  }

  fmt.Println("sum =", sum)
}
```

**Output**

sum = 55

Here, we have used a `for` loop to iterate from i equal to 1 to 10.

In each iteration of the loop, we have added the value of i to the `sum` variable.

---

## Related Golang for Loop Topics

Range form of the Golang for loop

  
  
  
  
[](https://www.programiz.com/golang/arrays)

Using Golang for loop as a while loop

What is an infinite loop?

  
  

Golang Blank Identifier in for loop.