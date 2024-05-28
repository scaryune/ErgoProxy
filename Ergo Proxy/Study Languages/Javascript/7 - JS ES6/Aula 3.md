# JavaScript Default Parameters

Starting from **JavaScript ES6**, we can provide default values for function parameters.

These default values are used when the function is called without passing the corresponding arguments.

Here's a quick example of JavaScript default parameters. You can read the rest of the tutorial for more details.

### Example

```
function greet(name = "Guest") {
    console.log(`Hello, ${name}!`);
}

greet(); 

// Output: Hello, Guest!
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In this example, the `greet()` function has a default parameter name with the string value `Guest`. Since we have not passed any argument to the function, it uses the default value.

---

## Example: JavaScript Default Parameters

```
function sum(x = 3, y = 5) {
    // return sum
    return x + y;
}

// pass arguments to x and y
var result = sum(5, 15);
console.log(`Sum of 5 and 15: ${result}`);

// pass argument to x but not to y
result = sum(7);
console.log(`Sum of 7 and default value (5): ${result}`);

// pass no arguments
// use default values for x and y
result = sum();
console.log(`Sum of default values (3 and 5): ${result}`);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Sum of 5 and 15: 20
Sum of 7 and default value (5): 12
Sum of default values (3 and 5): 8

In the above example, the default value of x is **3** and the default value of y is **5**.

- `sum(5, 15)` - When both arguments are passed, x takes **5** and y takes **15**.
- `sum(7)` - When **7** is passed, x takes **7** and y takes the default value **5**.
- `sum()` - When no argument is passed, x and y take the default values **3** and **5**, respectively.

![How default arguments work in JavaScript](https://www.programiz.com/sites/tutorial2program/files/javascript-default-arguments.png "How default arguments work in JavaScript")

How default arguments work in JavaScript

---

## More on Default Parameters

Pass One Parameter as the Default Value of Another

[](https://www.programiz.com/javascript/online-compiler)

Pass Function Value as Default Value

[](https://www.programiz.com/javascript/online-compiler)

Pass undefined Value

[](https://www.programiz.com/javascript/null-undefined#undefined)

[](https://www.programiz.com/javascript/online-compiler)

---

**Also Read:**

- [JavaScript Function and Function Expressions](https://www.programiz.com/javascript/function)
- [JavaScript ES6](https://www.programiz.com/javascript/ES6)