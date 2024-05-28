# JavaScript Variable Scope

In JavaScript, the scope of a variable determines where it can be accessed within the code.

Variables can be declared in different scopes:

- Global Scope
- Local (Function) Scope
- Block-Level Scope

For example,

```
function addNumbers() {
    var sum = 5 + 4;
}
```

Here, the sum variable is created inside the `addNumbers()` function.

So, it's accessible only within that function (local or function scope). This kind of variable is known as a **local variable**.

**Note:** Based on the scope they're declared in, variables can be classified as:

- Global Variables
- Local Variables
- Block-Level Variables

---

## JavaScript Local Variables

When variables are declared inside a function, they have a local scope and are accessible only within that function.

These types of variables are called local variables. For example,

```
function greet() {

    // local variable
    var message = "Hello";
    
    console.log(`Local: ${message}`);
}

greet();

// try to access message variable
// outside the greet() function
console.log(`Global: ${message}`);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Local: Hello
ERROR!
... ... ...
ReferenceError: message is not defined

Here, the message variable is local to the `greet()` function. So, it can only be accessed within that function.

That's why we get an error when we try to access it outside the `greet()` function.

To fix this issue, we can make the message variable global.

---

## JavaScript Global Variables

In JavaScript, a variable declared outside any function or in the global scope is known as a global variable.

A global variable can be accessed both inside and outside of functions. For example,

```
// declare global variable
var message = "Hello";

function greet() {
    console.log(`Local: ${message}`);
}

greet();

console.log(`Global: ${message}`);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Local: Hello
Global: Hello

Here, we can access the message variable from outside of the `greet()` function.

This is possible because we have created the message variable in the global scope (outside the function).

Thus, message will be accessible from any scope (region) of the program.

Change the Value of a Global Variable Inside a Function

[](https://www.programiz.com/javascript/online-compiler)

Use Variables Without Declaration

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/use-strict)

---

## JavaScript Block-Level Variables

JavaScript [ES6](https://www.programiz.com/javascript/ES6) introduced block-level scoping with the `let` and `const` keywords.

Block-level variables are accessible only within the block `{}` they are defined in, which can be smaller than a function's scope. For example,

```
function display_scopes() {
    // declare variable in local scope
    let message = "local";

    if (true) {

        // declare block-level variable
        let message = "block-level";

        console.log(`inner scope: ${message}`);
    }

    console.log(`outer scope: ${message}`);
}

display_scopes();
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

inner: block-level
outer: local

In this example, we have created two separate message variables:

- **Block-Level:** The variable inside the [if block](https://www.programiz.com/javascript/if-else) (visible only there).
- **Local-Level:** The variable inside the `display_scopes()` function.

let is Block-Scoped

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/console)

---

**Also Read:**

- [JavaScript Variables and Constants](https://www.programiz.com/javascript/variables-constants)
- [JavaScript Function and Function Expressions](https://www.programiz.com/javascript/function)

- [](https://www.programiz.com/javascript/variable-scope#introduction)
- [](https://www.programiz.com/javascript/variable-scope#local)
- [](https://www.programiz.com/javascript/variable-scope#global)
- [](https://www.programiz.com/javascript/variable-scope#block)