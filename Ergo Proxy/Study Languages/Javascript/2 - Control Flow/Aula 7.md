# JavaScript switch...case Statement

The JavaScript `switch...case` statement executes different blocks of code based on the value of a given expression.

Here's a simple example of the `switch...case` statement. You can read the rest of the tutorial for more.

### Example

```
let trafficLight = "green";
let message = ""
 
switch (trafficLight) {
    case "red":
        message = "Stop immediately.";
        break;
    case "yellow":
        message = "Prepare to stop.";
        break;
    case "green":
        message = "Proceed or continue driving.";
        break;
    default:
        message = "Invalid traffic light color.";
}
 
console.log(message)
 
// Output: Proceed or continue driving.
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

The above program checks the value of trafficLight and prints the corresponding meaning of the traffic light. If the value doesn't match any of the specified cases, it prints `Invalid traffic light color.`

---

## Syntax of the switch...case Statement

```
switch (expression) {

    case value1:
        // code block to be executed
        // if expression matches value1
        break;

    case value2:
        // code block to be executed
        // if expression matches value2
        break;

    ...

    default:
        // code block to be executed
        // if expression doesn't match any case
}
```

Here,

1. The `switch` statement first evaluates the `expression`.
2. After that, it compares the result against value1. If a matching is found, the corresponding code block is executed. Then, the `break` statement immediately stops further checking of other cases.
3. If there is no match for value1, the program compares the result with the next specified case value (value2). This process continues until a matching case is found.
4. If none of the case values match, the code block in the `default` block is executed.

Let's try to understand this process with a flowchart below.

---

## Flowchart of switch Statement

![Flowchart of JavaScript switch statement](https://www.programiz.com/sites/tutorial2program/files/javascript-switch-statement_0.png "Flowchart of JavaScript switch statement")

Flowchart of JavaScript switch statement

---

## Example 1: Simple Program Using switch...case

Suppose we want to display a message based on the current day of the week. Let's look at the example below to see how we can achieve this using `switch...case`.

```
let day = 3; 
let activity;

switch (day) {

    case 1:
        console.log("Sunday");
        break;

    case 2:
        console.log("Monday");
        break;

    case 3:
        console.log("Tuesday");
        break;

    case 4:
        console.log("Wednesday");
        break;

    case 5:
        console.log("Thursday");
        break;

    case 6:
        console.log("Friday");
        break;

    case 7:
        console.log("Saturday");
        break;

    default:
        console.log("Invalid Day");
}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Tuesday

This program prints the day based on the number stored in the day variable (**1** for `Sunday`, **2** for `Monday`, and so on).

Here, the `switch` statement checks the value of day against a series of cases:

1. First, it checks day against `case 1`. Since it doesn't match, this case is skipped.
2. Next, it checks day against `case 2`. Since it doesn't match, this case is skipped.
3. Then, it checks day against `case 3`. Since there is a match, its code block is executed (`Tuesday` is printed).
4. After printing `Tuesday`, a `break` statement is encountered, which terminates the `switch` statement.

---

## Example 2: Simple Calculator Using switch...case

```
// take user input for two numbers
let number1 = Number(prompt("Enter the value of number1: "));
let number2 = Number(prompt("Enter the value of number2: "));

// take user input to select an operator 
const operator = prompt("Enter a operator ( either +, -, * or / ): ");

switch(operator) {

    case "+":
        result = number1 + number2;
        console.log(`${number1} + ${number2} = ${result}`);
        break;

    case "-":
        result = number1 - number2;
        console.log(`${number1} - ${number2} = ${result}`);
        break;

    case "*":
        result = number1 * number2;
        console.log(`${number1} * ${number2} = ${result}`);
        break;

    case "/":
        result = number1 / number2;
        console.log(`${number1} / ${number2} = ${result}`);
        break;

    default:
        console.log("Invalid operator");
}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Sample Output 1**

Enter the value of number1: 6
Enter the value of number2: 3
Enter a operator ( either +, -, * or / ): *
6 * 3 = 18

**Sample Output 2**

Enter the value of number1: 6
Enter the value of number2: 3
Enter a operator ( either +, -, * or / ): +
6 + 3 = 9

In the above program, we prompted the user to:

- Enter two numbers: number1 and number2.
- Select an operator: `+`, `-`, `*`, or `/`.

Based on the user input, the `switch` statement performs the corresponding calculation.

**Note:** Here, we have used template literal `` `${number1} + ${number2} = ${result}` `` that combines text and variable into one string.

It shows the values of number1, number2, and result directly in the message, like `5 + 3 = 8`. To learn more about template literals, visit [JavaScript Template Literals](https://www.programiz.com/javascript/template-literal).

---

## More on JavaScript switch Statement

The default case is optional.

[](https://www.programiz.com/javascript/online-compiler)

What happens when we use a switch statement without break?

[](https://www.programiz.com/javascript/online-compiler)

How can we use a single block of code for multiple case values?

[](https://www.programiz.com/javascript/online-compiler)

JavaScript switch statement performs strict type checking.

[](https://www.programiz.com/javascript/online-compiler)

Comparison between switch statement and if...else statement.

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/online-compiler)

---

**Also Read:**

- [JavaScript if...else Statement](https://www.programiz.com/javascript/if-else)
- [JavaScript continue Statement](https://www.programiz.com/javascript/continue-statement)