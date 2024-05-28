# JavaScript Getter and Setter

In JavaScript, there are two kinds of object properties:

- Data properties
- Accessor properties

---

## Data Property

Here's an example of data property that we have been using in the previous tutorials.

```
const student = {

    // data property
    firstName: 'Monica';
};
```

---

## Accessor Property

In JavaScript, accessor properties are [methods](https://www.programiz.com/javascript/methods) that get or set the value of an [object](https://www.programiz.com/javascript/object). For that, we use these two [keywords](https://www.programiz.com/javascript/keywords-identifiers):

- `get` - to define a getter method to get the property value
- `set` - to define a setter method to set the property value

---

### JavaScript Getter

In JavaScript, getter methods are used to access the properties of an object. For example,

```
const student = {

    // data property
    firstName: 'Monica',
    
    // accessor property(getter)
    get getName() {
        return this.firstName;
    }
};

// accessing data property
console.log(student.firstName); // Monica

// accessing getter methods
console.log(student.getName); // Monica

// trying to access as a method
console.log(student.getName()); // error
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In the above program, a getter method `getName()` is created to access the property of an object.

```
get getName() {
    return this.firstName;
}
```

**Note:** To create a getter method, the `get` keyword is used.

And also when accessing the value, we access the value as a property.

```
student.getName;
```

When you try to access the value as a method, an error occurs.

```
console.log(student.getName()); // error
```

---

## JavaScript Setter

In JavaScript, setter methods are used to change the values of an object. For example,

```
const student = {
    firstName: 'Monica',
    
    //accessor property(setter)
    set changeName(newName) {
        this.firstName = newName;
    }
};

console.log(student.firstName); // Monica

// change(set) object property using a setter
student.changeName = 'Sarah';

console.log(student.firstName); // Sarah
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In the above example, the setter method is used to change the value of an object.

```
set changeName(newName) {
    this.firstName = newName;
}
```

**Note:** To create a setter method, the `set` keyword is used.

As shown in the above program, the value of `firstName` is `Monica`.

Then the value is changed to `Sarah`.

```
student.changeName = 'Sarah';
```

**Note**: Setter must have exactly one formal parameter.

---

## JavaScript Object.defineProperty()

In JavaScript, you can also use [Object.defineProperty()](https://www.programiz.com/javascript/library/object/defineProperty) method to add getters and setters. For example,

```
const student = {
    firstName: 'Monica'
}

// getting property
Object.defineProperty(student, "getName", {
    get : function () {
        return this.firstName;
    }
});

// setting property
Object.defineProperty(student, "changeName", {
    set : function (value) {
        this.firstName = value;
    }
});

console.log(student.firstName); // Monica

// changing the property value
student.changeName = 'Sarah';

console.log(student.firstName); // Sarah
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In the above example, `Object.defineProperty()` is used to access and change the property of an object.

The syntax for using `Object.defineProperty()` is:

```
Object.defineProperty(obj, prop, descriptor)
```

The `Object.defineProperty()` method takes three arguments.

- The first argument is the objectName.
- The second argument is the name of the property.
- The third argument is an object that describes the property.