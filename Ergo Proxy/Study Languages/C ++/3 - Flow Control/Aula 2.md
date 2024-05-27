# C++ Relational and Logical Operators

In C++, relational and logical operators compare two or more operands and return either `true` or `false` values.

We use these operators in decision making.

---

## C++ Relational Operators

A relational operator is used to check the relationship between two operands. For example,

```
// checks if a is greater than b
a > b;
```

Here, `>` is a relational operator. It checks if a is greater than b or not.

If the relation is **true**, it returns **1** whereas if the relation is **false**, it returns **0**.

The following table summarizes the relational operators used in C++.

|Operator|Meaning|Example|
|---|---|---|
|`==`|Is Equal To|`3 == 5` gives us **false**|
|`!=`|Not Equal To|`3 != 5` gives us **true**|
|`>`|Greater Than|`3 > 5` gives us **false**|
|`<`|Less Than|`3 < 5` gives us **true**|
|`>=`|Greater Than or Equal To|`3 >= 5` give us **false**|
|`<=`|Less Than or Equal To|`3 <= 5` gives us **true**|

---

### == Operator

The equal to `==` operator returns

- `true` - if both the operands are equal or the same
- `false` - if the operands are unequal

For example,

```
int x = 10;
int y = 15;
int z = 10;

x == y   // false
x == z   // true
```

**Note:** The relational operator `==` is not the same as the assignment operator `=`. The assignment operator `=` assigns a value to a variable, constant, array, or vector. It does not compare two operands.

---

### != Operator

The not equal to `!=` operator returns

- `true` - if both operands are unequal
- `false` - if both operands are equal.

For example,

```
int x = 10;
int y = 15;
int z = 10;

x != y   // true
x != z   // false
```

---

### > Operator

The greater than `>` operator returns

- `true` - if the left operand is greater than the right
- `false` - if the left operand is less than the right

For example,

```
int x = 10;
int y = 15;

x > y   // false
y > x   // true
```

---

### < Operator

The less than operator `<` returns

- `true` - if the left operand is less than the right
- `false` - if the left operand is greater than right

For example,

```
int x = 10;
int y = 15;

x < y   // true
y < x   // false
```

---

### >= Operator

The greater than or equal to `>=` operator returns

- `true` - if the left operand is either greater than or equal to the right
- `false` - if the left operand is less than the right

For example,

```
int x = 10;
int y = 15;
int z = 10;

x >= y   // false
y >= x   // true
z >= x   // true
```

---

### <= Operator

The less than or equal to operator `<=` returns

- `true` - if the left operand is either less than or equal to the right
- `false` - if the left operand is greater than right

For example,

```
int x = 10;
int y = 15;

x > y   // false
y > x   // true
```

---

In order to learn how relational operators can be used with strings, refer to our tutorial here.

## C++ Logical Operators

We use logical operators to check whether an expression is **true** or **false**. If the expression is **true**, it returns **1** whereas if the expression is **false**, it returns **0**.

|Operator|Example|Meaning|
|---|---|---|
|`&&`|expression1 **&&** expression 2|Logical AND.  <br>true only if all the operands are true.|
|`\|`|expression1 **\|** expression 2|Logical OR.  <br>true if at least one of the operands is true.|
|`!`|**!**expression|Logical NOT.  <br>true only if the operand is false.|

---

### C++ Logical AND Operator

The logical AND operator `&&` returns

- `true` - if and only if **all the operands are** `true`.
- `false` - if **one or more operands** are `false`.

**Truth Table of && Operator**

Let **a** and **b** be two operands. **0** represents **false** while **1** represents **true**. Then,

|a|b|a && b|
|---|---|---|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|1|

As we can see from the truth table above, the `&&` operator returns true only if both `a` and `b` are true.

Note: The Logical AND operator `&&` should not be confused with the Bitwise AND operator `&`.

---

### Example 1: C++ OR Operator

```
// C++ program demonstrating && operator truth table

#include <iostream>
using namespace std;

int main() {
    int a = 5;
    int b = 9;
  
    // false && false = false
    cout << ((a == 0) && (a > b)) << endl;
  
    // false && true = false
    cout << ((a == 0) && (a < b)) << endl;

    // true && false = false
    cout << ((a == 5) && (a > b)) << endl;

    // true && true = true
    cout << ((a == 5) && (a < b)) << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

0
0
0
1

In this program, we declare and initialize two `int` variables a and b with the values `5` and `9` respectively. We then print a logical expression

```
((a == 0) && (a > b))
```

Here, `a == 0` evaluates to `false` as the value of a is `5`. `a > b` is also `false` since the value of a is less than that of b. We then use the AND operator `&&` to combine these two expressions.

From the truth table of `&&` operator, we know that `false && false` (i.e. `0 && 0`) results in an evaluation of `false` (`0`). This is the result we get in the output.

Similarly, we evaluate three other expressions that fully demonstrate the truth table of the `&&` operator.

---

### C++ Logical OR Operator

The logical OR operator `||` returns

- `true` - if **one or more of the operands are** `true`.
- `false` - if and only if **all the operands** are `false`.

**Truth Table of || Operator**

Let **a** and **b** be two operands. Then,

|a|b|a \| b|
|---|---|---|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|1|

As we can see from the truth table above, the `||` operator returns false only if both `a` and `b` are false.

---

### Example 2: C++ OR Operator

```
// C++ program demonstrating || operator truth table

#include <iostream>
using namespace std;

int main() {
    int a = 5;
    int b = 9;
  
    // false && false = false
    cout << ((a == 0) || (a > b)) << endl;
  
    // false && true = true
    cout << ((a == 0) || (a < b)) << endl;

    // true && false = true
    cout << ((a == 5) || (a > b)) << endl;

    // true && true = true
    cout << ((a == 5) || (a < b)) << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

0
1
1
1

In this program, we declare and initialize two `int` variables a and b with the values `5` and `9` respectively. We then print a logical expression

```
((a == 0) || (a > b))
```

Here, `a == 0` evaluates to `false` as the value of a is `5`. `a > b` is also `false` since the value of a is less than that of b. We then use the OR operator `||` to combine these two expressions.

From the truth table of `||` operator, we know that `false || false` (i.e. `0 || 0`) results in an evaluation of `false` (`0`). This is the result we get in the output.

Similarly, we evaluate three other expressions that fully demonstrate the truth table of `||` operator.

---

### C++ Logical NOT Operator !

The logical NOT operator `!` is a unary operator i.e. it takes only one operand.

It returns **true** when the operand is **false**, and **false** when the operand is **true**.

**Truth Table of the ! Operator**

Let **a** be an operand. Then,

---

### Example 3: C++ ! Operator

```
// C++ program demonstrating ! operator truth table
#include <iostream>
using namespace std;

int main() {
    int a = 5;
  
    // !false = true
    cout << !(a == 0) << endl;

    // !true = false
    cout << !(a == 5) << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

1
0

In this program, we declare and initialize an `int` variable a with the value `5`. We then print a logical expression

```
!(a == 0) 
```

Here, `a == 0` evaluates to `false` as the value of a is `5`. However, we use the NOT operator `!` on `a == 0`. Since `a == 0` evaluates to `false`, the `!` operator inverts the results of `a == 0` and the final result is `true`.

Similarly, the expression `!(a == 5)` ultimately returns `false` because `a == 5` is `true`.

- [](https://www.programiz.com/cpp-programming/relational-logical-operators#relational)
- [](https://www.programiz.com/cpp-programming/relational-logical-operators#equal-to)
- [](https://www.programiz.com/cpp-programming/relational-logical-operators#greater-than)
- [](https://www.programiz.com/cpp-programming/relational-logical-operators#less-than)
- [](https://www.programiz.com/cpp-programming/relational-logical-operators#logical)
- [](https://www.programiz.com/cpp-programming/relational-logical-operators#logical-and)
- [](https://www.programiz.com/cpp-programming/relational-logical-operators#logical-or)
- [](https://www.programiz.com/cpp-programming/relational-logical-operators#logical-not)