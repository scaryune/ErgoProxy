# JavaScript Objects

JavaScript object is a variable that can store multiple data in **key-value** pairs.

Here's a quick example of the JavaScript object. Read the rest of the tutorial for more.

### Example

```
// student object
const student = {
    firstName: "Jack",
    rollNo: 32 
};

console.log(student);

// Output: { firstName: 'Jack', rollNo: 32 }
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, `student` is an object that stores the first name and the roll number of students as key-value pairs.

---

## Create JavaScript Objects

The syntax of JavaScript object is:

```
const objectName = {
    key1: value1,
    key2: value2,
    ...,
    keyN: valueN
};
```

Here,

- `objectName` - Name of the object.
- `key1: value1` - The first key-value pair.
- `key2: value2` - The second key-value pair.
- `keyN: valueN` - The `Nth` key-value pair.

Each key-value pair has a colon `:` between them and is separated by a comma `,`.

---

### Example 1: JavaScript Objects

```
// create person object
const person = {
    name: "John",
    age: 20
};

console.log(person);

// Output: { name: "John", age: 20 }
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In the above example, `name: "John"` and `age: 30` are key-value pairs.

**Note:** You can also create objects in a single line. For example,

```
const person = { name: "John", age: 20 };
```

However, it's preferable to break down objects into multiple lines for better readability.

---

## JavaScript Object Properties

In JavaScript, the key-value pairs of an object are referred to as **properties**. For example,

```
const person = {
    name: "John",
    age: 20,
};
```

Here, `name: "John"` and `age: 30` are the properties of the object person.

![Key-Value Pairs are Object Properties in JavaScript](https://www.programiz.com/sites/tutorial2program/files/javascript-object-properties_1.png "JavaScript Object Properties")

JavaScript Object Properties

---

## Access Object Properties

You can access the **value** of a property by using its **key**.

**1. Using Dot Notation**

```
const dog = {
    name: "Rocky",
};

// access property
console.log(dog.name);

// Output: Rocky
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**2. Using Bracket Notation**

```
const cat = {
    name: "Luna",
};

// access property
console.log(cat["name"]);

// Output: Luna
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## JavaScript Object Operations

In JavaScript, we can perform various operations on object properties like modifying, adding, deleting, and so on. Let's discuss some of them.

### 1. Modify Object Properties

We can modify object properties by assigning a new value to an existing key. For example,

```
const person = {
    name: "Bobby",
    hobby: "Dancing",
};

// modify property
person.hobby = "Singing";

// display the object
console.log(person);

// Output: { name: 'Bobby', hobby: 'Singing' }
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In the above example, we used the dot notation to change the value of the hobby key from `Dancing` to `Singing`.

---

### 2. Add Object Properties

```
const student = {
    name: "John",
    age: 20,
};

// add properties
student.rollNo = 14;
student.faculty = "Science";

// display the object
console.log(student);

// Output: { name: 'John', age: 20, rollNo: 14, faculty: 'Science' }
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In the above example, the keys rollNo and faculty do not exist within the object. Hence, when we assign values to these keys, new properties are added to the object.

---

### 3. Delete Object Properties

We can remove properties from an object using the `delete` operator. For example,

```
const employee = {
    name: "Tony",
    position: "Officer",
    salary: 30000,
};

// delete object property
delete employee.salary

// display the object
console.log(employee);

// Output: { name: 'Tony', position: 'Officer' }
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## JavaScript Object Methods

We can also include functions inside an object. For example,

```
const person = {
    name: "Bob",
    age: 30,

    // use function as value
    greet: function () {
        console.log("Bob says Hi!");
    }
};

// call object method
person.greet();  // Bob says Hi!
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, we have assigned a function as a value for the greet key.

These functions that are defined inside objects are called **methods**.

**Note:** Just like we use `()` to call a function, we must use `()` to call methods.

You will learn more about [JavaScript Methods](https://www.programiz.com/javascript/methods) in the next tutorial.

---

## JavaScript Nested Objects

What is a nested object?

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/online-compiler)

---

**Also Read:**

- [Different Ways to Create Objects](https://www.programiz.com/javascript/examples/create-object)
- [JavaScript Constructor Function](https://www.programiz.com/javascript/constructor-function)
- [JavaScript Prototype](https://www.programiz.com/javascript/prototype)