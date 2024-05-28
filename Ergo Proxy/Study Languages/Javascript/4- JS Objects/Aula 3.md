# JavaScript Constructor Function

In JavaScript, a constructor function is used to create and initialize [objects](https://www.programiz.com/javascript/object).

Here is a simple example of a constructor function. Read the rest of the tutorial for more.

### Example

```
// constructor function
function Person () {
    this.name = "John",
    this.age = 23
}

// create an object
const person = new Person();

// print object attributes
console.log(person.name);
console.log(person.age);

// Output:
// John
// 23
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, `Person()` is an object constructor function. And, we use the `new` keyword to create an object from a constructor function.

---

## Create Multiple Objects With Constructor Function

In JavaScript, you can create multiple objects from a constructor function. For example,

```
// constructor function
function Person () {
    this.name = "John",
    this.age = 23,

     this.greet = function () {
        console.log("hello");
    }
}

// create objects
const person1 = new Person();
const person2 = new Person();

// access properties
console.log(person1.name);  // John
console.log(person2.name);  // John
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In the above program, we created two objects (person1 and person2) using the same constructor function.

JavaScript this Keyword

[](https://www.programiz.com/javascript/this)

[](https://www.programiz.com/javascript/online-compiler)

---

## JavaScript Constructor Function Parameters

You can also create a constructor function with parameters. For example,

```
// constructor function with parameters
function Person (person_name, person_age, person_gender) {

   // assign parameter values to the calling object
    this.name = person_name,
    this.age = person_age,
    this.gender = person_gender,

    this.greet = function () {
        return (`Hi ${this.name}`);
    }
}

// create objects and pass arguments
const person1 = new Person("John", 23, "male");
const person2 = new Person("Sam", 25, "female");

// access properties
console.log(person1.name); // John
console.log(person2.name); // Sam
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In the above example, we have passed arguments to the constructor function during the creation of the object.

```
const person1 = new Person("John", 23, "male");
const person2 = new Person("Sam", 25, "female");
```

This allows each object to have different properties:

|person1|person2|
|---|---|
|name holds the value `John`.|name holds the value `Sam`.|
|age holds the value **23**.|age holds the value **25**.|
|gender holds the value `male`.|gender holds the value `female`.|

---

## Constructor Function vs. Object Literal

Constructor functions can create multiple objects.

Each object created from a constructor function is unique.

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/online-compiler)

---

## JavaScript Built-In Constructors

JavaScript also has built-in constructors to create objects of various types. Some of them are:

|Constructor|Description|
|---|---|
|`Object()`|Creates a new object with properties and methods.|
|`String()`|Constructs a string object for manipulating and representing textual data.|
|`Number()`|Constructs a number object for handling data and operations.|
|`Boolean()`|Constructs a boolean object representing `true` or `false` values for logical operations.|

---

### Example: JavaScript Built-In Constructors

```
// use Object() constructor to create object
const person = new Object({ name: "John", age: 30 });

// use String() constructor to create string object
const name = new String ("John");

// use Number() constructor to create number object
const number = new Number (57);

// use Boolean() constructor to create boolean object
const count = new Boolean(true);

console.log(person);
console.log(name);
console.log(number);
console.log(count);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

{ name: 'John', age: 30 }
[String: 'John']
[Number: 57]
[Boolean: true]

**Note**: You should not declare [strings](https://www.programiz.com/javascript/string), [numbers](https://www.programiz.com/javascript/number), and [boolean](https://www.programiz.com/javascript/booleans) values as objects because they slow down the program. Instead, declare them as primitive types using code such as `let name = "John"`, `let number = 57`, etc.

---

## More on Constructor Functions

JavaScript Object Prototype

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/prototype)

JavaScript Classes

[](https://www.programiz.com/javascript/ES6)

[](https://www.programiz.com/javascript/ES6#class)

---

**Also Read:**

- [JavaScript Function and Function Expressions](https://www.programiz.com/javascript/function)