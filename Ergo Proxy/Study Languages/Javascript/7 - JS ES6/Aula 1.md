# JavaScript ES6

**JavaScript ES6** (also known as **ECMAScript2015** or **ECMAScript6**) is the sixth edition of JavaScript introduced in June 2015.

[ECMAScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Language_Resources) (European Computer Manufacturers Association Script) is the standard specification of JavaScript to ensure compatibility in all browsers and environments.

This tutorial provides a summary of commonly used features and syntax improvements of ES6.

---

## JavaScript Declarations

Previously, JavaScript only allowed variable declarations using the `var` keyword.

ES6 now allows you to declare variables using two more keywords: `let` and `const`.

### Declaration With let Keyword

The `let` keyword creates [block-scoped](https://www.programiz.com/javascript/variable-scope) variables, which means they are only accessible within a particular block of code. For example,

```
{
    // block of code

    // declare variable with let
    let name = "Peter";

    // can be accessed here
    console.log(name); // Peter
}

// can't be accessed here
console.log(name);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Peter
ERROR!
...
ReferenceError: name is not defined

However, the above program works without any error if we swap `let` with `var`. For example,

```
{
    // block of code

    // declare variable with var
    var name = "Peter";

    // can be accessed here
    console.log(name);
}

// can be accessed here
console.log(name);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Peter
Peter

This simply means that we have more control over variables declared with `let`.

To learn more about the difference between `let` and `var`, visit [JavaScript let vs var](https://www.programiz.com/javascript/let-vs-var).

---

### Declaration With const Keyword

The `const` keyword creates constant variables that cannot be changed after declaration. For example,

```
// declare variable with const
const fruit = "Apple";

console.log(fruit);

// reassign fruit
// this code causes an error
fruit = "Banana";

console.log(fruit);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Apple
Error: Assignment to constant variable

Here, we used `const` to declare the variable fruit with the value of `Apple`.

Thus, changing its value to `Banana` causes an error.

---

## JavaScript Template Literals

The template literal makes it easier to include variables inside a string.

For example, this was how we concatenated strings and variables before:

```
const firstName = "Jack";
const lastName = "Sparrow";

console.log("Hello " + firstName + " " + lastName);

// Output: Hello Jack Sparrow
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Now, you can simply do this:

```
const firstName = "Jack";
const lastName = "Sparrow";

console.log(`Hello ${firstName} ${lastName}`);

// Output: Hello Jack Sparrow
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

To learn more about template literals, visit [JavaScript Template Literal](https://www.programiz.com/javascript/template-literal).

---

## Default Parameter Values

In ES6, you can pass default values for function parameters. For example,

```
// function to find sum of two numbers
function sum(numA, numB = 5) {

    // default value of numB is 5
    console.log(numA + numB);
};

// pass 10 to numA but
// don't pass value to numB
// numB takes default value 5
sum(10);  // 15

// pass 5 to numA and 15 to numB 
sum(5, 15);  // 20
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In the above example, we included the default parameter value `numB = 5` in the function declaration.

This means, even if you don't pass the parameter for numB, it will take **5** by default.

To learn more about default parameters, visit [JavaScript Default Parameters](https://www.programiz.com/javascript/default-parameters).

---

## JavaScript Arrow Function

ES6 introduces a new way to write [function and function expressions](https://www.programiz.com/javascript/function) using `=>` called the arrow function.

Previously, the only way to write a function expression was:

```
// function expression
let product = function(x, y) {
   return x * y;
};

result = product(5, 10);

console.log(result);  // 50
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Now, you can simply write it as:

```
// function expression using arrow function
let product = (x, y) => x * y;

result = product(5, 10);

console.log(result);  // 50
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

To learn more about arrow functions, visit [JavaScript Arrow Function](https://www.programiz.com/javascript/arrow-function).

---

## JavaScript Classes

ES6 also introduces the concept of classes, a fundamental aspect of object-oriented programming (OOP).

We can use the `class` keyword to create classes and objects. Previously, we used [constructor functions](https://www.programiz.com/javascript/constructor-function) to create objects. For example,

```
// constructor function
function Person(name) {
    this.name = name;
};

// create objects
var p1 = new Person("John");
var p2 = new Person("Rachel");

// print object properties
console.log(p1.name);  // John
console.log(p2.name);  // Rachel
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Now, we can do the same thing using the `class` keyword. And, we can initialize the class using the `constructor()` function. For example,

```
// declare a class
class Person {

    // constructor function
    constructor(name) {
        this.name = name;
    };
};

// create objects
let p1 = new Person("John");
let p2 = new Person("Rachel");

// print object properties
console.log(p1.name);  // John
console.log(p2.name);  // Rachel
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

To learn more about classes, visit [JavaScript Classes](https://www.programiz.com/javascript/classes).

---

## JavaScript Destructuring

The destructuring syntax makes it easier to extract values from arrays or objects into individual variables.

For example, previously we extracted object values into variables in the following way:

```
// object of hospital
const hospital = {
    doctors: 23,
    patients: 44,
};

// assign individual values
let doctors = hospital.doctors;
let patients = hospital.patients;

console.log(doctors);  // 23
console.log(patients);  // 44
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Now, we can simply use the ES6 destructuring syntax:

```
const hospital = {
    doctors: 23,
    patients: 44,
};

// use ES6 destructuring syntax
let { doctors, patients } = hospital;

console.log(doctors);  // 23
console.log(patients);  // 44
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

To learn more about destructuring, visit [JavaScript Destructuring](https://www.programiz.com/javascript/destructuring-assignment).

---

## JavaScript import and export

Before ES6, there was no standard way for developers to manage their code in separate files as modules.

With ES6, we can finally manage modules with the `import` and `export` syntax.

For example, suppose you have two JavaScript files named **person.js** and **action.js**.

In **action.js**, you can export anything. For this tutorial, let's just export a function named `greet()`:

```
// export
export default function greet(name) {
    console.log(`Hi ${name}!`);
};
```

Then in **person.js**, you can import the `greet()` function and use it:

```
import greet from './action.js';

greet("Sara");

// Output: Hi Sara!
```

---

## JavaScript Promise

The ES6 `Promise` provides a clean way to handle [asynchronous tasks](https://www.programiz.com/javascript/async-await). For example,

```
// define a promise
let countValue = new Promise(function (resolve, reject) {
    setTimeout(function () {
        resolve("Promise resolved!");
    }, 5000);
});

// executes when promise resolves
countValue.then(function successValue(result) {
    console.log(result);
});

// Output: Promise resolved!
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, we first created a promise on the variable countValue.

We then used the `setTimeout()` function to resolve the promise after a delay of **5** seconds.

Likewise, the `.then()` method executes when the promise resolves and displays the output `Promise resolved!`.

To learn more about promises, visit [JavaScript Promises](https://www.programiz.com/javascript/promise).

---

## JavaScript Rest Parameter

You can use the **rest** **parameter** `...` to represent an infinite number of arguments as an array. For example,

```
// function with ...args rest parameter
function show(a, b, ...args) {
    console.log("a:", a);
    console.log("b:", b);
    console.log("args:", args);
}

// call function with extra parameters
show(1, 2, 3, 4, 5);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

a: 1
b: 2
args: [ 3, 4, 5 ]

You can use any name for the rest parameter. However, args is a common convention.

---

## Spread Operator

You can use the **spread operator** `...` to unpack an array or object. For example,

```
let numArr = [1, 2, 3];

// without spread operator
console.log([numArr, 4, 5]);  // [[1, 2, 3], 4, 5]

// with spread operator
console.log([...numArr, 4, 5]);  // [1, 2, 3, 4, 5]
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

To learn more about the spread operator, visit [JavaScript Spread Operator.](https://www.programiz.com/javascript/spread-operator)

**Note:** Both the rest parameter and the spread operator use the same syntax. However, we only use the rest operator in the function definition as arguments.