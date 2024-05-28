# JavaScript Classes

In [JavaScript ES6](https://www.programiz.com/javascript/ES6), classes provide a way to create blueprints for objects, similar to traditional object-oriented programming languages like C++ or Java.

Let's explore a simple example by creating a `Person` class:

```
// define a class named 'Person'
class Person {
    // class constructor to initialize the 'name' and 'age' properties
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    
    // method to display a message
    greet() {
        console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
    }
}

// create two instances of the Person class
let person1 = new Person("Jack", 30);
let person2 = new Person("Tina", 33);

// call greet() method on two instances 
person1.greet();
person2.greet();
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Hello, my name is Jack and I am 30 years old.
Hello, my name is Tina and I am 33 years old.

In the above example, we have defined a `Person` class using the `class` keyword.

Inside `Person`, we have defined:

- a class constructor that initializes the `name` and `age` properties
- a `greet()` method that displays a greeting message using the `name` and `age` properties.

Using the `new` keyword, we have created two objects of the `Person` class- `person1` and `person2`.

We have then called the `greet()` method on `person1` and `person2` using the `.` operator:

- `person1.greet()` - calls `greet()` on `person1`
- `person2.greet()` - calls `greet()` on `person2`

---

## Create Objects Without Classes

In JavaScript, you have the flexibility to create objects directly without the use of formal class definitions. This can be achieved by using object literals.

Let's look at the example below,

```
// create an object 'person' without a formal class definition
let person = {
    name: "Jack",
    age: 30,
    greet: function() {
        console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`)
    }
};

// call the greet() method on the person object
person.greet(); 
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Hello, my name is Jack and I am 30 years old.

In the above example, we have created an object named `person` directly using an object literal.

The `person` object has:

- properties - `name` and `age` with values `"Jack"` and **30** respectively.
- method - `greet()` that displays a greeting message.

We have called the `greet()` method on `person` using the `.` operator as `person.greet()`.

To learn more about object literals, visit [JavaScript Objects](https://www.programiz.com/javascript/object).

---

## Features of a JavaScript Class

Let's revisit the code from the beginning of the tutorial and explore each part in detail to gain a deeper understanding of how classes work in JavaScript.

```
// define a class named 'Person'
class Person {
    // class constructor to initialize the 'name' and 'age' properties
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    
    // method to display a message
    greet() {
        console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
    }
}

// create two objects of the Person class
let person1 = new Person("Jack", 30);
let person2 = new Person("Tina", 33);

// call greet() method on two instances 
person1.greet();
person2.greet();
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Hello, my name is Jack and I am 30 years old.
Hello, my name is Tina and I am 33 years old.

**Create a class**

In JavaScript, we create a class using the `class` keyword. For example,

```
// create a class
class Person {
    // body of class
};
```

**Class Constructor**

A class constructor is a special method within a class that is automatically executed when a new object of that class is created.

![Constructor of the Person Class](https://www.programiz.com/sites/tutorial2program/files/class-constructor.png "Constructor of the Person Class")

Constructor of the Person Class

The `Person` class constructor initializes the `name` and `age` properties when a new object is created.

Here,

- the `person1` object is initialized with `"Jack"` and **30**
- the `person2` object is initialized with `"Tina"` and **33**

**Class Method**

A class method is a function inside a class that defines behaviors for the class's objects.

![Method of the Person Class](https://www.programiz.com/sites/tutorial2program/files/class-method.png "Method of the Person Class")

Method of the Person Class

Here, `greet()` is a method of the `Person` class that displays a greeting message when called on objects of the class.

- [](https://www.programiz.com/javascript/classes#introduction)
- [](https://www.programiz.com/javascript/classes#create-objects)
- [](https://www.programiz.com/javascript/classes#features)