# JavaScript break Statement

The `break` statement terminates the loop immediately when it's encountered.

Here's a quick example of the `break` statement. You can read the rest of the tutorial for more.

### Example

```
// infinite loop because condition is always true
while (true) {

    // get number input from user
    let num = Number(prompt("Enter a number: "));

    // break condition
    if (num == 0) {
        break;
    }

    console.log(num);
}

// Output:
// Enter a number: 5
// 5
// Enter a number: 0
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In this example, the `break` statement terminates the infinite loop when the user input num is **0.** If it isn't **0**, the loop keeps taking input and printing it to the screen.

---

## Working of JavaScript break Statement

The image below shows the working of the `break` statement in [for](https://www.programiz.com/javascript/for-loop) and [while](https://www.programiz.com/javascript/while-loop) loops.

![Working of break statement in JavaScript](https://www.programiz.com/sites/tutorial2program/files/javascript-break-statement_1.png "Working of break statement in JavaScript")

Working of JavaScript break Statement

**Note**: The `break` statement is usually used inside decision-making statements such as [if...else](https://www.programiz.com/javascript/if-else).

---

## Example 1: JavaScript break With for Loop

```
// Program to print the value of i

for (let i = 1; i <= 5; i++) {

    // break condition     
    if (i == 3) {
        break;
    }

    console.log(i);
}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

1
2

In the above program, we have used a [for](https://www.programiz.com/javascript/for-loop) [loop](https://www.programiz.com/javascript/for-loop) to print numbers from **1** to **5**. Notice the use of `break` inside the `if` statement:

```
if(i == 3) {
    break;
}
```

Here, when the value of i becomes **3**, the `break` statement is executed, which terminates the loop.

Hence, the output doesn't include values greater than or equal to **3**.

---

## Example 2: JavaScript break With while Loop

We can terminate a `while` loop using the `break` statement. For example,

```
// Program to find the sum of positive numbers
// the while loop runs infinitely
// loop terminates only when user enters a negative number

let sum = 0;

// infinite loop
while (true) {

    // get number input
    let num = Number(prompt("Enter a number: "));

    // terminate the loop if num is negative
    if (num < 0)
        break;
    }

    // otherwise, add num to sum
    else {
        sum += num;
    }
}

// print the sum
console.log(`Sum: ${sum}`);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Enter a number: 3
Enter a number: 5
Enter a number: 0
Enter a number: 8
Enter a number: -3
Sum: 16

In the above example, we have used a `while` loop whose condition is always `true`.

```
while (true) {
    // code
}
```

Inside the loop, we ask for user input.

- If the input value is negative, `num < 0` becomes `true`, and the `break` statement terminates the loop.
- Otherwise, the input value is added to the sum variable.

```
if (num < 0) {
    break;
}
else {
    sum += num;
}
```

---

## More on JavaScript break

JavaScript break With Nested Loop.

[](https://www.programiz.com/javascript/online-compiler)

![Using break inside a nested loop](https://www.programiz.com/sites/tutorial2program/files/javascript-break-nested-loop_0.png "Using break inside a nested loop")

Using break with labels.

![Working of labeled break statement in JavaScript](https://www.programiz.com/sites/tutorial2program/files/javascript-labeled-break-statement_0.png "Working of labeled break statement in JavaScript")

[](https://www.programiz.com/javascript/online-compiler)

Using break in a switch statement.

[](https://www.programiz.com/javascript/switch-statement)

[](https://www.programiz.com/javascript/online-compiler)

---

**Also Read:**

- [JavaScript continue Statement](https://www.programiz.com/javascript/continue-statement)