# Go Booleans (Relational and Logical Operators)

## Go Boolean Data Types

A boolean data type represents logical entities. It can have two possible values: `true` or `false`.

We use the `bool` keyword to create boolean-type variables. For example,

```
package main
import "fmt"

func main() {

  var boolTrue bool = true
  var boolFalse bool = false

  fmt.Println("The boolean values are", boolTrue, "and", boolFalse)
}
```

**Output:**

The boolean values are true and false

---

## Relational Operators in Golang

We use the relational operators to compare two values or variables. For example,

```
number1 := 9
number2 := 3

result := number1 > number2
```

Here, `>` is a relational (comparison) operator. It compares whether number1 is greater than number2.

Relational Operators use boolean values (`true` and `false`) to return the validity of a relation. It returns:

- `true` if the comparison between operators is correct.
- `false` if the comparison between operators is incorrect.

---

### Different Types of Relational Operators in Golang

Here's a list of various relational operators available in Go:

|Operator|Example|Descriptions|
|---|---|---|
|`==` (equal to)|`a == b`|returns `true` if `a` and `b` are equal|
|`!=` (not equal to)|`a != b`|returns `true` if `a` and `b` are not equal|
|`>` (greater than)|`a > b`|returns `true` if `a` is greater than `b`|
|`<` (less than)|`a < b`|returns `true` if `a` is less than `b`|
|`>=` (greater than or equal to)|`a >= b`|returns `true` if `a` is either greater than or equal to `b`|
|`<=` (less than or equal to)|`a <= b`|returns `true` is `a` is either less than or equal to `b`|

---

### Example: Relational Operator in Go

```
// Program to illustrate the working of Relational Operators

package main
import "fmt"

func main() {

  number1 := 12
  number2 := 20
  var result bool

  // equal to operator
  result = (number1 == number2)

  fmt.Printf("%d == %d returns %t \n", number1, number2, result)

  // not equal to operator
  result = (number1 != number2)

  fmt.Printf("%d != %d returns %t \n", number1, number2, result)

  // greater than operator
  result = (number1 > number2)

  fmt.Printf("%d > %d returns %t \n", number1, number2, result)

  // less than operator
  result = (number1 < number2)

  fmt.Printf("%d < %d returns %t \n", number1, number2, result)

}
```

**Output**

12 == 20 returns false 
12 != 20 returns true 
12 > 20 returns false 
12 < 20 returns true 

---

## Logical Operators in Go

Logical operators return either `true` or `false` depending upon the conditions.

|Operator|Description|Example|
|---|---|---|
|`&&` (Logical AND)|`exp1 && exp2`|returns `true` if both expressions `exp1` and `exp2` are `true`|
|`\|` (Logical OR)|`exp1 \| exp2`|returns `true` if any one of the expressions is `true`.|
|`!` (Logical NOT)|`!exp`|returns `true` if `exp` is `false` and returns `false` if `exp` is `true`.|

---

### Example: Logical Operator in Go

```
// Program to illustrate the working of Logical Operator

package main
import "fmt"

func main() {

  number1 := 6
  number2 := 12
  number3 := 6
  var result bool

  // returns false because number1 > number2 is false
  result = (number1 > number2) && (number1 == number3)

  fmt.Printf("Result of AND operator is %t \n", result)

  // returns true because number1 == number3 is true
  result = (number1 > number2) || (number1 == number3)

  fmt.Printf("Result of OR operator is %t \n", result)
  
  // returns false because number1 == number3 is true
  result = !(number1 == number3);

  fmt.Printf("Result of NOT operator is %t \n", result)

}
```

**Output**

Result of AND operator is false 
Result of OR operator is true 
Result of NOT operator is false 

---

## Go Boolean Expression

In programming, expressions that return boolean values: `true` or `false` are known as boolean expressions. For example,

```
number1 := 5
number2 := 8

result := number1 > number2
```

Here, `number1 > number2` is a boolean expression that returns `false`.

**Why boolean expression?**

Boolean expressions are used to create decision-making programs. Suppose we want to create a program that determines whether a person can vote or not.

We can use a boolean expression to check if the age of that person is greater than **18**. If true, the person can vote. If false, cannot vote.

We will learn more about these decision-making programs in [_Go if...else_](https://www.programiz.com/golang/if-else).