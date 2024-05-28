# JavaScript Function and Function Expressions

A function is an independent block of code that performs a specific task, while a function expression is a way to store functions in variables.

Here's a quick example of function and function expression. You can read the rest of the tutorial for more.

### Example

```
// create a function named greet()
function greet() {
    console.log("Hello World!");
}

// store a function in the displayPI variable
// this is a function expression
let displayPI = function() {
    console.log("PI = 3.14");
}

// call the greet() function
greet();

// call the reply() function
displayPI();

// Output:
// Hello World!
// PI = 3.14
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, we created the `greet()` function and used the displayPI variable to create a function expression. Then, we called the functions by using their names followed by parentheses `()` i.e. `greet()` and `displayPI()`.

---

## Create a JavaScript Function

We can create a function in JavaScript using the `function` keyword:

```
function greet() {
    console.log("Hello World!");
}
```

![Create a JavaScript Function](https://www.programiz.com/sites/tutorial2program/files/javascript-create-function.png "Create a JavaScript Function")

Create a JavaScript Function

Here, we have created a simple function named `greet()` that prints `Hello World!` on the screen.

Our function contains the following parts:

- **Function Keyword** - The `function` keyword is used to create the function.
- **Function Name** - The name of the function is `greet`, followed by parentheses `()`.
- **Function Body** - The code that is executed when we call the function. In our case, it is `console.log("Hello World!");`

## Frequently Asked Questions

Benefits of Using a Function

---

## Call a Function

Previously, we declared a function named `greet()`:

```
function greet() {
   console.log("Hello World!");
}
```

If we run the above code, we won't get any output. But why?

It's because creating a function doesn't mean we are executing the code inside it. In other words, the function is ready and available for us to execute whenever we choose.

And if we want to use the function, we need to call it.

**Function Call**

```
greet();
```

As you can see, we call a function by writing the function name (`greet`) followed by parentheses `()`.

---

## Example 1: JavaScript Function Call

```
// create a function
function greet() {
    console.log("Hello World!");
}

// call the function
greet();

console.log("Outside function");
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Hello World!
Outside function

In the above example, we created a function named `greet()`. Here's how the control of the program flows:

![Working of a Function in JavaScript](https://www.programiz.com/sites/tutorial2program/files/javascript-working-of-function.png "Working of a Function in JavaScript")

Working of a Function in JavaScript

Here,

1. When the `greet()` function is called, the program's control transfers to the function definition.
2. All the code inside the function is executed (`Hello World!` is printed).
3. The program control then jumps to the next statement after the function call (`Outside function` is printed).

---

## JavaScript Function Arguments

Arguments are values you pass to the function when you call it.

```
// function with a parameter called 'name'
function greet(name) {
    console.log(`Hello ${name}`);
}

// pass argument to the function
greet("John");

// Output: Hello John
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In the above example, we passed `"John"` as an argument to the `greet()` function.

![Pass Argument to the Function](https://www.programiz.com/sites/tutorial2program/files/javascript-function-argument.png "Pass Argument to the Function")

Pass Argument to the Function

Notice the name variable declared inside parentheses:

```
function greet(name) {
    // code
}
```

Here, name is a **function parameter**, which acts as a placeholder to store the function argument.

In other words, the argument `"John"` is stored in the name parameter.

**Remember:** A function argument is the value we pass to the function, while a function parameter is a placeholder that stores the argument passed to the function.

**Pass Different Arguments to the Function**

We can pass different arguments in each call, making the function re-usable and dynamic.

```
function greet(name) {
    console.log(`Hello ${name}`);
}

// pass "John" as argument
greet("John");

// pass "David" as argument
greet("David");
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Hello John
Hello David

---

## Example 2: JavaScript Function to Add Two Numbers

We can also pass multiple arguments to a single function. For example,

```
// function with two arguments
function addNumbers(num1, num2) {
    let sum = num1 + num2;
   console.log(`Sum: ${sum}`);
}

// call function by passing two arguments
addNumbers(5, 4);

// Output:
// Sum: 9
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In the above example, we have created a function named `addNumbers()` with two parameters: num1 and num2. Here,

- num1 takes the value of the first argument, **5**.
- num2 takes the value of the second argument, **4**.

The function then adds the values of num1 and num2 and the result is printed as output.

![JavaScript Function Argument](https://www.programiz.com/sites/tutorial2program/files/javascript-function-multiple-arguments.png "JavaScript Function Argument")

JavaScript Function Argument

---

## The return Statement

We can return a value from a JavaScript function using the `return` statement.

```
// function to find square of a number
function findSquare(num) {

    // return square
    return num * num; 
}

// call the function and store the result
let square = findSquare(3);

console.log(`Square: ${square}`);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Square: 9

In the above example, we have created a function named `findSquare()`. The function accepts a number and returns the square of the number.

In our case, we passed **3** as an argument to the function. So, the function returns the square of **3**, which is **9**, to the function call.

We then stored this return value in the square variable and printed it.

![Working of JavaScript Functions](https://www.programiz.com/sites/tutorial2program/files/javascript-function-return-value.png "Working of JavaScript Functions")

Working of JavaScript Functions

---

## The return Statement Terminates the Function

Any code written in the function after the `return` statement is not executed. For example,

```
function display() {

    console.log("This will be executed.");

    return "Returning from function.";

    console.log("This will not be executed.");
}

let message = display();
console.log(message);  
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

This will be executed.
Returning from function.

In this example, the `display()` function doesn't execute the second `console.log()` statement inside it.

This is because the function execution stops at the `return` statement. So, the following code is never reached:

```
console.log("This will not be executed.");
```

This is what actually happens:

1. First, the function prints `This will be executed.` to the screen.
2. Then, it returns the string `Returning from function.` to the function call.
3. Finally, the function terminates its execution.
4. The return value is then stored in the message variable and printed.

![Function Terminates After return](https://www.programiz.com/sites/tutorial2program/files/javascript-function-return-terminate.png "Function Terminates After return")

Function Terminates After return

---

## JavaScript Library Functions

JavaScript provides some built-in functions that can be directly used in our program. We don't need to create these functions; we just need to call them.

Some common JavaScript library functions are:

|Library Function|Description|
|---|---|
|[console.log()](https://www.programiz.com/javascript/console)|Prints the string inside the quotation marks.|
|[Math.sqrt()](https://www.programiz.com/javascript/library/math/sqrt)|Returns the square root of a number.|
|[Math.pow()](https://www.programiz.com/javascript/library/math/pow)|Returns the power of a number.|
|[toUpperCase()](https://www.programiz.com/javascript/library/string/touppercase)|Returns the [string](https://www.programiz.com/javascript/string) converted to uppercase.|
|[toLowerCase()](https://www.programiz.com/javascript/library/string/tolowercase)|Returns the string converted to lowercase.|

To learn more about library functions, visit [JavaScript Library Functions](https://www.programiz.com/javascript/library).

---

### Example 3: JavaScript Library Function

```
// Math.sqrt() computes the square root
let squareRoot = Math.sqrt(4);
console.log("Square Root of 4 is", squareRoot);

// Math.pow() computes the power
let power = Math.pow(2, 3);
console.log("2 to the power of 3 is", power);

// toUpperCase() converts text to uppercase
let band = "Iron Maiden";
let bandUpper = band.toUpperCase();
console.log(`Favorite Band: ${bandUpper}`);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Square Root of 4 is 2
2 to the power 3 is 8
Favorite Band: IRON MAIDEN

Here,

- `Math.sqrt(4)` calculates the square root of **4**, resulting in **2**.
- `Math.pow(2, 3)` computes `2 ^ 3` (**2** raised to the power of **3**), which is **8**.
- `band.toUpperCase()` converts the string in the band variable to uppercase, resulting in `IRON MAIDEN`.

---

## Function Expressions

In JavaScript, a function expression is a way to store functions in variables. For example,

```
// store a function in the square variable
let square = function(num) {
    return num * num;
};

console.log(square(5));  

// Output: 25
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In this example, the function that calculates the square of a number is assigned to the square variable.

We then used this variable to call the function expression using the code `square(5)`, where **5** is the function argument.

**Note:** Like with functions, we need to use parentheses `()` with the variable name to call a function expression.

---

**Also Read:**

- [JavaScript Default Parameters](https://www.programiz.com/javascript/default-parameters)
- [JavaScript Arrow Function](https://www.programiz.com/javascript/arrow-function)
- [JavaScript CallBack Function](https://www.programiz.com/javascript/callback)

- [](https://www.programiz.com/javascript/function#introduction)
- [](https://www.programiz.com/javascript/function#create)
- [](https://www.programiz.com/javascript/function#call)
- [](https://www.programiz.com/javascript/function#example1)
- [](https://www.programiz.com/javascript/function#arguments)
- [](https://www.programiz.com/javascript/function#example2)
- [](https://www.programiz.com/javascript/function#return)
- [](https://www.programiz.com/javascript/function#terminate-function)
- [](https://www.programiz.com/javascript/function#library)
- [](https://www.programiz.com/javascript/function#function-expression)