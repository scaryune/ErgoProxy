# JavaScript Methods and this Keyword

Before continuing this tutorial, make sure you are familiar with:

- [JavaScript Objects](https://www.programiz.com/javascript/object)
- [JavaScript Function](https://www.programiz.com/javascript/function)

---

## JavaScript Method

A JavaScript method is a function defined within an object. For example,

```
// dog object
const dog = {
    name: "Rocky",

    // bark method
    bark: function () {
        console.log("Woof!");
    }
};

// access method
dog.bark();

// Output: Woof!
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In the above example, the dog object has two keys: name and bark.

Since the bark key holds a function, we refer to it as a **method**.

Notice that we accessed the `bark()` method using `dog.bark()`. Thus, the syntax to access an object method is:

```
objectName.methodKey()
```

---

## JavaScript this Keyword

We use `this` keyword in an object method to access a property of the same object. For example,

```
// person object
const person = {
    name: "John",
    age: 30,

    // method
    introduce: function () {
        console.log(`My name is ${this.name} and I'm ${this.age} years old.`);
    }
};

// access the introduce() method
person.introduce();

// Output: My name is John and I'm 30 years old.
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In the above example, we created the person object with two properties (name and age) and a method `introduce()`.

Inside the `introduce()` method, we used `this.name` and `this.age` to refer to the name and age keys of the person object.

To learn more, visit [JavaScript this](https://www.programiz.com/javascript/this).

---

## Add Methods to an Object

You can add more methods to a JavaScript object even after we've defined it. For example,

```
// student object
let student = {
    name: "John"
};

// add new method
student.greet = function () {
    console.log("Hello");
};

// access greet() method
student.greet();

// Output: Hello
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In the above example, we created the student object with the property `name: "John"`.

Initially, student did not have any method. So, we used the dot notation to add a new method to the object:

```
student.greet = function() {
    console.log("Hello");
};
```

---

## JavaScript Built-In Methods

JavaScript provides a wide array of useful methods known as built-in methods. Some commonly used built-in methods (and the respective objects they belong to) are given in the table below:

|Method|Object|Description|
|---|---|---|
|[console.log()](https://programiz.com/javascript/console)|Console|Displays messages or variables in the browser's console.|
|`prompt()`|Window|Displays a dialog box that prompts the user for input.|
|[concat()](https://www.programiz.com/javascript/library/string/concat)|[String](https://www.programiz.com/javascript/library/string)|Concatenates the arguments to the calling string.|
|[toFixed()](https://www.programiz.com/javascript/library/number/tofixed)|[Number](https://www.programiz.com/javascript/library/number)|Rounds off a number into a fixed number of digits.|
|[sort()](https://www.programiz.com/javascript/library/array/sort)|[Array](https://www.programiz.com/javascript/library/array)|Sorts the elements of an array in specific order.|
|[random()](https://www.programiz.com/javascript/library/math/random)|[Math](https://www.programiz.com/javascript/library/math)|Returns a pseudo-random float number between **0** and **1**.|

To learn more about JavaScript built-in methods, visit [JavaScript Built-In Methods](https://www.programiz.com/javascript/library).

---

## Examples: JavaScript Build-In Methods

JavaScript concat() Method

[](https://www.programiz.com/javascript/online-compiler)

JavaScript toFixed() Method

[](https://www.programiz.com/javascript/online-compiler)

---

**Also Read:**

- [JavaScript Getter and Setter](https://www.programiz.com/javascript/getter-setter)