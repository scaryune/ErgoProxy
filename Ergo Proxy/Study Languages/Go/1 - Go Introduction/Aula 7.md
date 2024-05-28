# Go Operators

In Computer Programming, an operator is a symbol that performs operations on a value or a variable.

For example, `+` is an operator that is used to add two numbers.

Go programming provides wide range of operators that are categorized into following major categories:

- Arithmetic operators
- Assignment operator
- Relational operators
- Logical operators

---

## Arithmetic Operator

We use arithmetic operators to perform arithmetic operations like addition, subtraction, multiplication, and division.

Here's a list of various arithmetic operators available in Go.

|Operators|Example|
|---|---|
|`+` (Addition)|`a + b`|
|`-` (Subtraction)|`a - b`|
|`*` (Multiplication)|`a * b`|
|`/` (Division)|`a / b`|
|`%` (Modulo Division)|`a % b`|

---

### Example 1: Addition, Subtraction and Multiplication Operators

```
package main
import "fmt"

func main() {

  num1 := 6
  num2 := 2

  // + adds two variables
  sum := num1 + num2
  fmt.Printf("%d + %d = %d\n", num1, num2, sum)

  // - subtract two variables
  difference := num1 - num2
  fmt.Printf("%d - %d = %d\n",num1, num2,  difference)

  // * multiply two variables
  product := num1 * num2
  fmt.Printf("%d * %d is %d\n",num1, num2,  product)

}
```

**Output**

6 + 2 = 8
6 - 2 = 4
6 * 2 = 12

---

### Example 2: Golang Division Operator

```
package main
import "fmt"

func main() {

  num1 := 11
  num2 := 4

  // / divide two integer variables
  quotient := num1 / num2
  fmt.Printf(" %d / %d = %d\n", num1, num2, quotient)

}
```

**Output**

11 / 4 = 2

In the above example, we have used the `/` operator to divide two numbers: `11` and `4`. Here, we get the output `2`.

However, in normal calculation, `11 / 4` gives `2.75`. This is because when we use the `/` operator with integer values, we get the quotients instead of the actual result.

![The division operator with integer values returns the quotient.](https://www.programiz.com/sites/tutorial2program/files/go-integer-division.png "Division with integer in Go")

Division with integer

If we want the actual result we should always use the `/` operator with floating point numbers. For example,

```
package main
import "fmt"

func main() {

  num1 := 11.0
  num2 := 4.0

  // / divide two floating point variables
  result := num1 / num2
  fmt.Printf(" %g / %g = %g\n", num1, num2, result)

}
```

**Output**

11 / 4 = 2.75  

Here, we get the actual result after division.

---

### Example 3: Modulus Operator in Go

```
package main
import "fmt"

func main() {

  num1 := 11
  num2 := 4

  // % modulo-divides two variables
  remainder := num1 % num2
  fmt.Println(remainder )

}
```

In the above example, we have used the modulo operator with numbers: `11` and `4`. Here, we get the result `3`.

This is because in programming, the modulo operator always returns the remainder after division.

![The modulo operator in golang returns the remainder after division.](https://www.programiz.com/sites/tutorial2program/files/go-modulo-division.png "Modulo Division in Go")

Modulo Division in Go

**Note:** The modulo operator is always used with integer values.

---

## Increment and Decrement Operator in Go

In Golang, we use `++` (increment) and `--` (decrement) operators to increase and decrease the value of a variable by 1 respectively. For example,

```
package main
import "fmt"

func main() {

  num := 5

  // increment of num by 1
  num++
  fmt.Println(num)  // 6

  // decrement of num by 1
  num--
  fmt.Println(num)  // 4

}
```

In the above example,

- num++ - increases the value of num by `1`, from `5` to `6`
- num-- - decreases the value of num by `1`, from `5` to `4`

**Note:** We have used `++` and `--` as prefixes (before variable). However, we can also use them as postfixes (num++ and num--).

There is a slight difference between using increment and decrement operators as prefixes and postfixes. To learn the difference, visit [Increment and Decrement Operator as Prefix and Postfix](https://www.programiz.com/article/increment-decrement-operator-difference-prefix-postfix).

---

## Go Assignment Operators

We use the assignment operator to assign values to a variable. For example,

```
var number = 34
```

Here, the `=` operator assigns the value on right (**34**) to the variable on left (number).

---

### Example: Assignment Operator in Go

```
package main
import "fmt"

func main() {

  num := 6
  var result int

  // = operator to assign the value of num to result
  result = num
  fmt.Println(result)    // 6
}
```

In the above example, we have used the assignment operator to assign the value of the num variable to the result variable.

---

### Compound Assignment Operators

In Go, we can also use an assignment operator together with an arithmetic operator. For example,

```
number := 2
number += 6
```

Here, `+=` is additional assignment operator. It first adds **6** to the value of number (**2**) and assigns the final result (**8**) to `number`.

Here's a list of various compound assignment operators available in Golang.

|Operator|Example|Same as|
|---|---|---|
|`+=` (addition assignment)|`a += b`|`a = a + b`|
|`-=` (subtraction assignment)|`a -= b`|`a = a - b`|
|`*=` (multiplication assignment)|`a *= b`|`a = a * b`|
|`/=` (division assignment)|`a /= b`|`a = a / b`|
|`%=` (modulo assignment)|`a %= b`|`a = a % b`|

---

## Relational Operators in Golang

We use the relational operators to compare two values or variables. For example,

```
5 == 6
```

Here, `==` is a relational operator that checks if `5` is equal to `6`.

A relational operator returns

- `true` if the comparison between two values is correct
- `false` if the comparison is wrong

Here's a list of various relational operators available in Go:

|Operator|Example|Descriptions|
|---|---|---|
|`==` (equal to)|`a == b`|returns `true` if `a` and `b` are equal|
|`!=` (not equal to)|`a != b`|returns `true` if `a` and `b` are not equal|
|`>` (greater than)|`a > b`|returns `true` if `a` is greater than `b`|
|`<` (less than)|`a < b`|returns `true` if `a` is less than `b`|
|`>=` (greater than or equal to)|`a >= b`|returns `true` if `a` is either greater than or equal to `b`|
|`<=` (less than or equal to)|`a <= b`|returns `true` is `a` is either less than or equal to `b`|

To learn more, visit [_Go relational operators_](https://www.programiz.com/golang/boolean-expression).

---

## Logical Operators in Go

We use the logical operators to perform logical operations. A logical operator returns either `true` or `false` depending upon the conditions.

|Operator|Description|Example|
|---|---|---|
|`&&` (Logical AND)|`exp1 && exp2`|returns `true` if both expressions `exp1` and `exp2` are `true`|
|`\|` (Logical OR)|`exp1 \| exp2`|returns `true` if any one of the expressions is `true`.|
|`!` (Logical NOT)|`!exp`|returns `true` if `exp` is `false` and returns `false` if `exp` is `true`.|

To learn more, visit [_Go logical operators_](https://www.programiz.com/golang/boolean-expression).

---

## More on Go Operators

Go Binary Right Shift Operator >>

Go Binary Left Shift Operator <<

What is the use of the & operator in Go?

[](https://www.programiz.com/golang/pointers)

What is the use of the`*`operator in Go?

If we use multiple operators together in a single statement, which operator is executed first?

- [](https://www.programiz.com/golang/operators#introduction)
- [](https://www.programiz.com/golang/operators#arithmetic-operators)
- [](https://www.programiz.com/golang/operators#basic-arithmetic)
- [](https://www.programiz.com/golang/operators#Example2)
- [](https://www.programiz.com/golang/operators#increment-decrement)
- [](https://www.programiz.com/golang/operators#assignment-operator)
- [](https://www.programiz.com/golang/operators#compound-assignment)
- [](https://www.programiz.com/golang/operators#relational-operator)
- [](https://www.programiz.com/golang/operators#logical-operator)