# JavaScript Comments

JavaScript comments are annotations in the code that are completely ignored by the compiler. For example,

```
// display "Programiz" to the screen
console.log("Programiz");
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Programiz

Here, `// display "Programiz" to the screen` is a comment. As a result, it is ignored by the JavaScript engine.

---

## Types of JavaScript Comments

In JavaScript, there are two ways to add comments to code:

1. `//` - Single-Line Comments
2. `/* */` - Multiline Comments

---

## Single Line Comments

In JavaScript, any line that starts with `//` is a single-line comment. For example,

```
name = "Jack";

// display name on the console
console.log("Hello " + name);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, `// display name on the console` is a single-line comment.

**Note:** You can also use single-line comments like this:

```
name = "Jack";

console.log("Hello " + name);  // display name on the console
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

However, avoid using comments this way if they are long and descriptive.

---

## Multiline Comments

In JavaScript, multiline comments allow you to add comments that can span more than one line. They start with `/*` and end with `*/`. For example,

```
/* This is a multiline comment.
It can span several lines.
*/

let numberOfStudents = 50;
console.log(numberOfStudents);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, we have used a multiline comment that can span any number of lines.

---

We can use comments to remove unwanted code that we might require later.

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/online-compiler)

---

## Make Code Easier to Understand

As a JavaScript developer, you'll write code and also need to update code written by others.

If you write comments on your code, it will be easier for you to understand the code in the future. It will also be easier for your fellow developers to understand the code.

As a general rule of thumb, use comments to explain **why** you did something rather than **how** you did something.

**Notes:**

- Comments shouldn't be used for explaining poorly written code. Your code should always be well-structured and self-explanatory.
- Remember the shortcut for using comments; it can be extremely helpful. For most code editors, it's `Ctrl + /` for Windows and `Cmd + /` for Mac.