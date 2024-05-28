# JavaScript Template Literals (Template Strings)

JavaScript template literals are [strings](https://www.programiz.com/javascript/string) that allow us to embed variables or expressions directly within them. They are enclosed in backticks ` `` `.

Here is a simple example of template literals. Read the rest of the tutorial to learn more.

### Example

```
let name = "Alice";
let greeting = `Hello ${name}`;

console.log(greeting); 

// Output: Hello Alice
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, `` `Hello ${name}` `` is a template literal and we have embedded the name variable directly within it.

---

## Example: JavaScript Template Literals

We can use template literals to embed JavaScript expressions or variables with the help of the `${...}` syntax. For example,

```
let number1 = 8;
let number2 = 3;

// embed expression within template literal 
let result = `The sum of ${number1} and ${number2} is ${number1 + number2}.`;

console.log(result);

// Output: The sum of 8 and 3 is 11.
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In the above example, the following code is the template literal:

```
`The sum of ${number1} and ${number2} is ${number1 + number2}.`
```

In this template literal,

- `${number1 + number2}` is the embedded expression.
- `${number1}` and `${number2}` are the embedded variables.

**Notes:**

- Before template literals were introduced in [JavaScript ES6](https://www.programiz.com/javascript/ES6), we would use the `+` operator to concatenate variables and expressions in a string.
- Some browsers may not support the use of template literals. To learn more, visit [JavaScript Template Literal](https://caniuse.com/#search=template%20literal) support.

---

Template literals allow any type of quotes to be included directly.

[](https://www.programiz.com/javascript/online-compiler)

Create multiline strings using template literals.

[](https://www.programiz.com/javascript/online-compiler)

---

## Tagged Templates

Tagged templates are an advanced form of template literals in JavaScript. They allow you to parse template literals with a function.

Furthermore, you don't need to use parentheses `()` when passing the template literal to the function. For example,

```
function displayMessage(message) {
    return message;
}

// create a tagged template
let result = displayMessage`Hello Jack`;

console.log(result);  // [ 'Hello Jack' ]
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, unlike regular function arguments, the template literal is split into an array.

In our example, the function received an array with a single element (the string from the template literal). So, we obtained `[ 'Hello Jack' ]` as an output.

**Tip:** Try passing normal strings as arguments to the `displayMessage()` function and notice the difference in syntax and output.