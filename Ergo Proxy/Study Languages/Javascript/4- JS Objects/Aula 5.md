# JavaScript Prototype

Before continuing this tutorial, make sure you are familiar with:

- [JavaScript Objects](https://www.programiz.com/javascript/object)
- [JavaScript Constructor Function](https://www.programiz.com/javascript/constructor-function)

---

In JavaScript, prototypes allow properties and methods to be shared among instances of the function or object. For example,

```
function Car() {
    console.log("Car instance created!");
};

// add a property to prototype
Car.prototype.color = "Red";

// add a method to the prototype
Car.prototype.drive = function () {
    console.log(`Driving the car painted in ${this.color}...`);
};

// display the added property
console.log(`The car's color is: ${Car.prototype.color}`);

// call the added method
Car.prototype.drive();
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

The car's color is: Red
Driving the car painted in Red...

In the above example, we have defined a constructor function named `Car()`.

**Add a Property to the Prototype**

We then added a property named color and set its value to `Red`.

```
Car.prototype.color = "Red";
```

We can access this property using the code `Car.prototype.color`.

**Add a Method to the Prototype**

We also added a method called `drive()` to the `Car` prototype:

```
Car.prototype.drive = function () {
    console.log(`Driving the car painted in ${this.color}...`);
};
```

We can access this method using the code `Car.prototype.drive()`.

**Note:** The usage of the prototype has decreased significantly since the introduction of [classes](https://www.programiz.com/javascript/classes) in [ES6](https://www.programiz.com/javascript/ES6). However, you can still learn it to improve your understanding of JavaScript.

---

## Prototype Inheritance

Properties or methods added to the prototype of a constructor function are accessible to all objects derived from it. For example,

```
function Car(model, year) {
    this.model = model;
    this.year = year;
};

// create multiple objects
let c1 = new Car("Mustang", 1964);
let c2 = new Car("Corolla", 1966);

// add property
Car.prototype.color = "Red";

// add method
Car.prototype.drive = function() {
    console.log(`Driving ${this.model}`);
};

// display added property using c1 and c2 objects
console.log(`${c1.model} color: ${c1.color}`);  
console.log(`${c2.model} color: ${c2.color}`);  

// display added method using c1 and c2 objects
c1.drive();
c2.drive();
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Mustang color: Red
Corolla color: Red
Driving Mustang
Driving Corolla

In the above example, we created the objects c1 and c2 using the `Car()` constructor.

We then added the following to the prototype of `Car()`:

**1. The color Property**

- It has a value of `Red`.
- Both c1 and c2 can access it using `c1.color` and `c2.color`, respectively.

**2. The drive() Method**

- It is a method that displays a message.
- Both c1 and c2 can access it using `c1.drive()` and `c2.drive()`, respectively.

---

## JavaScript Prototype Chaining

JavaScript always searches for properties in the objects of the constructor function first. Then, it searches in the prototype.

This process is known as prototype chaining. For example,

```
function Car() {
    this.color = "Red";
};

// add property that already exists
Car.prototype.color = "Blue";

// add a new property
Car.prototype.wheels = 4;

const c1 = new Car();

console.log(`The car's color is ${c1.color}.`); 
console.log(`The car has ${c1.wheels} wheels.`);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

The car's color is Red.
The car has 4 wheels.

Here, we declared the name property in the `Car()` constructor. Then, we added the same property with a different value to its prototype.

When we display `c1.color`, JavaScript searches for color in c1 and then displays it without checking the prototype.

However, JavaScript can't find wheels in c1. So, when we display `c1.wheels`, it displays the prototype property.

---

## More on JavaScript Prototypes

Access the prototype of a constructor function from its object.

[](https://www.programiz.com/javascript/online-compiler)

Change the property value of a prototype.

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/string)[](https://www.programiz.com/javascript/array)

---

**Also Read:**

- [JavaScript this Keyword](https://www.programiz.com/javascript/this)