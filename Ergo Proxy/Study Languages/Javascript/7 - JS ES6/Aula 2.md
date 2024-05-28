# JavaScript Arrow Function

JavaScript arrow functions are a concise syntax for writing [function expressions](https://www.programiz.com/javascript/function).

Here's a quick example of the arrow function. You can read the rest of the tutorial for more.

### Example

```
// an arrow function to add two numbers
const addNumbers = (a, b) => a + b;

// call the function with two numbers
const result = addNumbers(5, 3);
console.log(result);

// Output: 8
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In this example, `addNumbers()` is an arrow function that takes two parameters, a and b, and returns their sum.

---

## Arrow Function Syntax

The syntax of the arrow function is:

```
let myFunction = (arg1, arg2, ...argN) => {
    statement(s)
}
```

Here,

- `myFunction` is the name of the function.
- `arg1, arg2, ...argN` are the function arguments.
- `statement(s)` is the function body.

If the body has single statement or expression, you can write the arrow function as:

```
let myFunction = (arg1, arg2, ...argN) => expression
```

**Note:** Arrow functions were introduced in ES6. Some browsers may not support the use of arrow functions. Visit [JavaScript Arrow Function support](https://caniuse.com/#search=arrow%20functions) to learn more.

Regular Function vs. Arrow Function

---

## Example 1: Arrow Function With No Argument

If a function doesn't take any argument, then you should use empty parentheses. For example,

```
const sayHello = () => "Hello, World!";

// call the arrow function and print its return value
console.log(sayHello());  

// Output: Hello, World!
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In this example, when `sayHello()` is called, it executes the arrow function which returns the string `Hello, World!`.

---

## Example 2: Arrow Function With One Argument

If a function has only one argument, you can omit the parentheses. For example,

```
const square = x => x * x;

// use the arrow function to square a number
console.log(square(5));  

// Output: 25
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

The arrow function `square()` takes one argument x and returns its square.

Hence, calling `square()` with the value **5** returns **25**.

---

## this Keyword With Arrow Function

Inside a regular function, [this keyword](https://www.programiz.com/javascript/this) refers to the function where it is called.

However, `this` is not associated with arrow functions. So, whenever you call `this`, it refers to its parent scope. For example,

```
// constructor function
function Person() {

    this.name = 'Jack',
    this.age = 25,
    this.sayName = function () {

        console.log(this.age);

        let innerFunc = () => {
            console.log(this.age);
        }

        innerFunc();
    }
}

const x = new Person();
x.sayName();
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

25
25

Here, the `innerFunc()` function is an arrow function.

And inside the arrow function, `this` refers to the parent's scope, i.e., the scope of the `Person()` function. Hence, `this.age` gives **25**.

this Keyword Inside a Regular Function

[](https://www.programiz.com/javascript/this)

[](https://www.programiz.com/javascript/online-compiler)

---

## More on Arrow Function

Arrow Function as an Expression

[](https://www.programiz.com/javascript/online-compiler)

Multiline Arrow Functions

[](https://www.programiz.com/javascript/online-compiler)

Things You Should Avoid With Arrow Functions

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/online-compiler)

---

**Also Read:**

- [JavaScript ES6](https://www.programiz.com/javascript/ES6)
- [JavaScript Objects](https://www.programiz.com/javascript/object)
- [JavaScript Constructor Function](https://www.programiz.com/javascript/constructor-function)

- [](https://www.programiz.com/javascript/arrow-function#introduction)
- [](https://www.programiz.com/javascript/arrow-function#syntax)
- [](https://www.programiz.com/javascript/arrow-function#example1)
- [](https://www.programiz.com/javascript/arrow-function#example2)
- [](https://www.programiz.com/javascript/arrow-function#this-arrow)

[

  


](https://www.programiz.com/javascript/ES6 "JS ES6")