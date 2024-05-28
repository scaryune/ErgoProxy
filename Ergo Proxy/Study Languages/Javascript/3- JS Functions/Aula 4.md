# JavaScript Recursion

Recursion is a programming technique where a function calls itself repeatedly to solve a problem. For example,

```
// Program to countdown till 1

// recursive function
function counter(count) {

    // display count
    console.log(count);

    // condition for stopping
    if(count > 1) {

        // decrease count
        count = count - 1;

        // call counter with new value of count
        counter(count);
    } else {

        // terminate execution
        return;
    };
};

// access function
counter(5);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

5
4
3
2
1

In the above example, we have a function `counter()` that accepts the argument `count`, which is the starting point for our countdown till **1**.

The `counter()` function first displays count then checks if the value of count is greater than **1** with `count > 1`.

If `count > 1` evaluates to `true`, the program decreases the value of count and calls `counter()` with the new value of count (recursion).

Otherwise, if `count > 1` evaluates to `false`, the program executes the `return` statement, stopping the recursion.

Here,

- The `counter()` function is a **recursive function**, a function that calls itself recursively.
- The `count > 1` condition is called a **base case**, a condition that specifies when the recursion must stop.

**Note:** Without base cases, a recursive function won't know when to stop, resulting in an **infinite recursion** (error).

![Working of recursive function to countdown till 1](https://www.programiz.com/sites/tutorial2program/files/javascript-recursion-countdown.png "Working of JavaScript recursion in Countdown")

Counting Down Till 1 Using Recursion

---

## Example: Find Factorial of a Number

Now, let's see an example of how we can use recursion to find the factorial of a number.

```
// recursive function
function factorial(num) {

    // base case
    // recurse only if num is greater than 0
    if (num > 1) {
        return num * factorial(num - 1);
    }
    else {
        return 1;
    };
};

let x = 3;

// store result of factorial() in variable
let y = factorial(x);

console.log(`The factorial of ${x} is ${y}`);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

The factorial of 3 is 6

Here, the `factorial()` function calls itself recursively as long as the num variable is greater than **1**.

We can divide the overall recursion process into two halves.

The iterations in the first half includes:

|Variable|Base case: num > 1|Action|
|---|---|---|
|`num = 3`|`true`|`factorial(3)` returns `3 * factorial(2)`|
|`num = 2`|`true`|`factorial(2)` returns `2 * factorial(1)`|
|`num = 1`|`false`|`factorial(1)` returns `1`|

1. `factorial(3)` returns `3 * factorial(2)` and waits for `factorial(2)` to compute.
2. `factorial(2)` returns `2 * factorial(1)` and waits for `factorial(1)` to compute.
3. `factorial(1)` doesn't pass the base case, so it directly returns **1**.

After that, the second half takes place in reverse:

1. `factorial(1)` returns **1.**
2. `factorial(2)` returns `2 * factorial(1)`. Since `factorial(1)` returned 1, `factorial(2)` returns `2 * 1 = 2`.
3. `factorial(3)` returns `3 * factorial(2)`. Since `factorial(2)` returned 2, `factorial(3)` returns `3 * 2 = 6`.

Finally, the returned value from `factorial(3)` is stored in the result variable.

![Working of recursive function to calculate factorial](https://www.programiz.com/sites/tutorial2program/files/javascript-recursion-factorial.png "Working of JavaScript recursion in Factorial")

Computing Factorial Using Recursion

---

## More on JavaScript Recursion

Does JavaScript have a recursion limit?

What is an infinite recursion?

[](https://www.programiz.com/javascript/online-compiler)