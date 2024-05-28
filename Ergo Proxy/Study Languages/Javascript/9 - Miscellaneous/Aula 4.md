# JavaScript this

In JavaScript, `this` keyword refers to the [object](https://www.programiz.com/javascript/object) where it is called.

## 1. this Inside Global Scope

When `this` is used alone, `this` refers to the global object (`window` object in browsers). For example,

```
let a = this;
console.log(a);  // Window {}

this.name = 'Sarah';
console.log(window.name); // Sarah
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, `this.name` is the same as `window.name`.

---

## 2. this Inside Function

When `this` is used in a function, `this` refers to the global object (`window` object in browsers). For example,

```
function greet() {

    // this inside function
    // this refers to the global object
    console.log(this);
}

greet(); // Window {}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## 3. this Inside Constructor Function

In JavaScript, [constructor functions](https://www.programiz.com/javascript/constructor-function) are used to create objects. When a function is used as a constructor function, `this` refers to the object inside which it is used. For example,

```
function Person() {

    this.name = 'Jack';
    console.log(this);

}

let person1 = new Person();
console.log(person1.name);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Person {name: "Jack"}
Jack

Here, `this` refers to the person1 object. That's why, `person1.name` gives us Jack.

**Note**: When `this` is used with [ES6 classes](https://www.programiz.com/javascript/classes), it refers to the object inside which it is used (similar to constructor functions).

---

## 4. this Inside Object Method

When `this` is used inside an object's method, `this` refers to the object it lies within. For example,

```
const person = {
    name : 'Jack',
    age: 25,

    // this inside method
    // this refers to the object itself
    greet() {
        console.log(this);
        console.log(this.name);
    }
}

person.greet();
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

{name: "Jack", age: 25, greet: ƒ}
Jack

In the above example, `this` refers to the `person` object.

---

## 5. this Inside Inner Function

When you access `this` inside an inner function (inside a method), `this` refers to the global object. For example,

```
const person = {
    name : 'Jack',
    age: 25,

    // this inside method
    // this refers to the object itself
    greet() {
        console.log(this);        // {name: "Jack", age ...}
        console.log(this.age);  // 25

        // inner function
        function innerFunc() {
        
            // this refers to the global object
            console.log(this);       // Window { ... }
            console.log(this.age);    // undefined
            
        }

        innerFunc();

    }
}

person.greet();
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

{name: "Jack", age: 25, greet: ƒ}
25
Window { …}
undefined

Here, `this` inside `innerFunc()` refers to the **global object** because `innerFunc()` is inside a method.

However, `this.age` outside `innerFunc()` refers to the `person` object.

---

## 6. this Inside Arrow Function

Inside the arrow function, `this` refers to the parent scope. For example,

```
const greet = () => {
    console.log(this);
}
greet(); // Window {...}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

[Arrow functions](https://www.programiz.com/javascript/arrow-function) do not have their own `this`. When you use `this` inside an arrow function, `this` refers to its parent scope object. For example,

```
const greet = {
    name: 'Jack',

    // method
    sayHi () {
        let hi = () => console.log(this.name);
        hi();
    }
}

greet.sayHi(); // Jack
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, `this.name` inside the `hi()` function refers to the `greet` object.

You can also use the arrow function to solve the issue of having `undefined` when using a function inside a method (as seen in Example 5). For example,

```
const person = {
    name : 'Jack',
    age: 25,

    // this inside method
    // this refers to the object itself
    greet() {
        console.log(this);
        console.log(this.age);

        // inner function
        let innerFunc = () => {
        
            // this refers to the global object
            console.log(this);
            console.log(this.age);
            
        }

        innerFunc();

    }
}

person.greet();
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

{name: "Jack", age: 25, greet: ƒ}
25
{name: "Jack", age: 25, greet: ƒ}
25

Here, `innerFunc()` is defined using the arrow function. It takes `this` from its parent scope. Hence, `this.age` gives **25**.

When the arrow function is used with `this`, it refers to the outer scope.

---

## 7. this Inside Function with Strict Mode

When `this` is used in [a function with strict mode](https://www.programiz.com/javascript/use-strict#function), `this` is [undefined](https://www.programiz.com/javascript/null-undefined#undefined). For example,

```
'use strict';
this.name = 'Jack';
function greet() {

    // this refers to undefined
    console.log(this);
}
greet(); // undefined
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Note**: When using `this` inside a function with strict mode, you can use [JavaScript Function call()](https://www.programiz.com/javascript/library/function/call).

For example,

```
'use strict';
this.name = 'Jack';

function greet() {
    console.log(this.name);
}

greet.call(this); // Jack
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

When you pass `this` with the `call()` function, `greet()` is treated as the method of the `this` object (global object in this case).

- [](https://www.programiz.com/javascript/this#global)
- [](https://www.programiz.com/javascript/this#function)
- [](https://www.programiz.com/javascript/this#constructor)
- [](https://www.programiz.com/javascript/this#method)
- [](https://www.programiz.com/javascript/this#inner-function)
- [](https://www.programiz.com/javascript/this#arrow)
- [](https://www.programiz.com/javascript/this#strict)

[

  


](https://www.programiz.com/javascript/closure "JS Closure")