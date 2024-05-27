# C++ switch..case Statement

The `switch` statement allows us to execute a block of code among many alternatives.

You can do the same thing with the [if...else](https://www.programiz.com/cpp-programming/if-else) statement. However, the syntax of the switch statement is much easier to read and write.

---

**Syntax**

```
switch (expression)  {
    case constant1:
        // code to be executed if 
        // expression is equal to constant1;
        break;

    case constant2:
        // code to be executed if
        // expression is equal to constant2;
        break;
        .
        .
        .
    default:
        // code to be executed if
        // expression doesn't match any constant
}
```

**How does the switch statement work?**

The `expression` is evaluated once and compared with the values of each `case` label.

- If there is a match, the corresponding code after the matching label is executed. For example, if the value of the [variable](https://www.programiz.com/cpp-programming/variables-literals) is equal to `constant2`, the code after `case constant2:` is executed until the [break statement](https://www.programiz.com/cpp-programming/break-statement) is encountered.
- If there is no match, the code after `default:` is executed.

**Note**: We can do the same thing with the if...else..if ladder. However, the syntax of the switch statement is cleaner and much easier to read and write.

---

## Flowchart of switch Statement

![C++ switch...case flowchart](https://www.programiz.com/sites/tutorial2program/files/cpp-switch-flowchart.png "C++ switch...case flowchart")

Flowchart of C++ switch...case statement

---

## Example: Create a Calculator using the switch Statement

```
// Program to build a simple calculator using switch Statement
#include <iostream>
using namespace std;

int main() {
    char oper;
    float num1, num2;
    cout << "Enter an operator (+, -, *, /): ";
    cin >> oper;
    cout << "Enter two numbers: " << endl;
    cin >> num1 >> num2;

    switch (oper) {
        case '+':
            cout << num1 << " + " << num2 << " = " << num1 + num2;
            break;
        case '-':
            cout << num1 << " - " << num2 << " = " << num1 - num2;
            break;
        case '*':
            cout << num1 << " * " << num2 << " = " << num1 * num2;
            break;
        case '/':
            cout << num1 << " / " << num2 << " = " << num1 / num2;
            break;
        default:
            // operator is doesn't match any case constant (+, -, *, /)
            cout << "Error! The operator is not correct";
            break;
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output 1**

Enter an operator (+, -, *, /): +
Enter two numbers: 
2.3
4.5
2.3 + 4.5 = 6.8

**Output 2**

Enter an operator (+, -, *, /): -
Enter two numbers: 
2.3
4.5
2.3 - 4.5 = -2.2

**Output 3**

Enter an operator (+, -, *, /): *
Enter two numbers: 
2.3
4.5
2.3 * 4.5 = 10.35

**Output 4**

Enter an operator (+, -, *, /): /
Enter two numbers: 
2.3
4.5
2.3 / 4.5 = 0.511111

**Output 5**

Enter an operator (+, -, *, /): ?
Enter two numbers: 
2.3
4.5
Error! The operator is not correct.

In the above program, we are using the `switch...case` statement to perform addition, subtraction, multiplication, and division.

**How This Program Works**

1. We first prompt the user to enter the desired [operator](https://www.programiz.com/cpp-programming/operators). This input is then stored in the `char` variable named oper.
2. We then prompt the user to enter two numbers, which are stored in the float variables num1 and num2.
3. The `switch` statement is then used to check the operator entered by the user:
    1. If the user enters `+`, addition is performed on the numbers.
    2. If the user enters `-`, subtraction is performed on the numbers.
    3. If the user enters `*`, multiplication is performed on the numbers.
    4. If the user enters `/`, division is performed on the numbers.
    5. If the user enters any other character, the default code is printed.

Notice that the [break statement](https://www.programiz.com/cpp-programming/break-statement) is used inside each `case` block. This terminates the `switch` statement.

If the `break` statement is not used, all cases after the correct `case` are executed.

You can visit the article on [C++ Program to Make a Simple Calculator](https://www.programiz.com/cpp-programming/examples/calculator-switch-case) to learn more.

- [](https://www.programiz.com/cpp-programming/switch-case#introduction)
- [](https://www.programiz.com/cpp-programming/switch-case#flowchart)
- [](https://www.programiz.com/cpp-programming/switch-case#example)

[

  


](https://www.programiz.com/cpp-programming/goto "C++ goto Statement")