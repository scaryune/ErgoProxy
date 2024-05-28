# JavaScript Variables and Constants

## JavaScript Variables

A JavaScript variable is a container for storing data. For example,

```
let num = 5;
```

Here, num is a variable that stores the number **5**.

---

### Declare Variables in JavaScript

In JavaScript, we use the `var` or `let` [keywords](https://www.programiz.com/javascript/keywords-identifiers) to declare variables. For example,

```
var age;
let name;
```

Here, age and name are variables.

What is the difference between var and let?

|||
|---|---|
|||
|[](https://www.programiz.com/javascript/variable-scope#local)||
|||

[](https://www.programiz.com/javascript/let-vs-var)

[](https://caniuse.com/#feat=let)

---

### Initialize Variables in JavaScript

We use the assignment operator `=` to assign a value to a variable.

```
// declare variable num
let num;

// assign 5 to num
num = 5;
```

Here, **5** is assigned to the variable num.

You can also initialize variables during its declaration.

```
// declare variable num1 and assign 5 to it
let num1 = 5;

// declare variable num2 and assign 6 to it
let num2 = 6;
```

Declare multiple variables in a single statement.

Use a variable without initializing it.

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/null-undefined)

---

### Change the Value of Variables

The value of a variable may **vary**. Hence, the name **variable**.

Let's look at the example below to learn how to change the value of a variable:

```
// assign 5 to variable score
let score = 5; 
console.log(score); // 5

// change the value of score to 3
score = 3; 
console.log(score); // 3
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, the value of the score variable is changed from **5** to **3** when we assign a new value to it.

---

### Rules for Naming JavaScript Variables

- Variable names must start with a letter, an underscore `_`, or the dollar sign `$`. For example,

```
// valid
let message = "hello";
let _message = "hello";
let $message = "hello";
```

- Variables cannot start with numbers. For example,

```
// invalid
let 1message = "hello"; // this gives an error
```

- Variable names are case-sensitive. So age and Age are different variables. For example,

```
let age = 23;
let Age = 20;

console.log(age); // 23
console.log(Age); // 20
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

- Variable names cannot be keywords (special words reserved for specific purposes in JavaScript such as `if`, `else`, `let`, `var`, etc.). For example,

```
//invalid
let new = 5; // Error! new is a keyword
```

Recommended ways to name a variable in JavaScript.

-   
      
    

-   
      
    

---

## JavaScript Constants

A constant is a type of variable whose value cannot be changed.

In JavaScript, we use the `const` keyword to create constants. For example,

```
// assign 5 to num 
const num = 5;
```

Once a constant is initialized, we cannot change its value.

```
// assign 5 to num
const num = 5;

// assign 10 to num
num = 10;  
console.log(num) // Error! constant cannot be changed
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

### Always Initialize a Constant During Declaration

If you do not initialize a constant at the time of declaration, it throws an error. For example,

```
// Error! Missing initializer in const declaration
const x;

// attempt to initialize constant after declaration
x = 5;

console.log(x)
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Note:** If you are sure that the value of a variable won't change throughout the program, we recommend you use `const`.

However, there are a few browsers that do not support `const`. Visit [JavaScript const browser support](https://caniuse.com/#feat=const) to learn more.

---

## Also Read

- [JavaScript Data Types](https://www.programiz.com/javascript/data-types)