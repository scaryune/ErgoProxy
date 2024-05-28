# JavaScript Proxies

In JavaScript, proxies (proxy object) are used to wrap an object and redefine various operations into the object such as reading, insertion, validation, etc. Proxy allows you to add custom behavior to an [object](https://www.programiz.com/javascript/object) or a [function](https://www.programiz.com/javascript/function).

---

## Creating a Proxy Object

The syntax of proxy is:

```
new Proxy(target, handler);
```

Here,

- `new Proxy()` - the [constructor](https://www.programiz.com/javascript/constructor-function).
- `target` - the object/function which you want to proxy
- `handler` - can redefine the custom behavior of the object

For example,

```
let student1 = {
    age: 24,
    name: "Felix"
}

const handler = {
    get: function(obj, prop) {
        return obj[prop] ? obj[prop] : 'property does not exist';
    }
}

const proxy = new Proxy(student1, handler);
console.log(proxy.name); // Felix
console.log(proxy.age); // 24
console.log(proxy.class); // property does not exist
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, the `get()` method is used to access the object's property value. And if the property is not available in the object, it returns property does not exist.

As you can see, you can use a proxy to create new operations for the object. A case may arise when you want to check if an object has a particular key and perform an action based on that key. In such cases, proxies can be used.

You can also pass an empty handler. When an empty handler is passed, the proxy behaves as an original object. For example,

```
let student = {
    name: 'Jack',
    age: 24
}

const handler = { };

// passing empty handler
const proxy1 = new Proxy(student, {});

console.log(proxy1); // Proxy {name: "Jack", age: 24}
console.log(proxy1.name); // Jack
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## Proxy handlers

Proxy provides two handler methods `get()` and `set()`.

### get() handler

The `get()` method is used to access the properties of a target object. For example,

```
let student = {
    name: 'Jack',
    age: 24
}

const handler = {

    // get the object key and value
    get(obj, prop) {

        return obj[prop];
  }
}

const proxy = new Proxy(student, handler);
console.log(proxy.name); // Jack
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, the `get()` method takes the object and the property as its parameters.

---

### set() handler

The `set()` method is used to set the value of an object. For example,

```
let student = {
    name: 'John'
}

let setNewValue = {
  set: function(obj, prop, value) {

    obj[prop] = value;
    return;
  }
};

// setting new proxy
let person = new Proxy(student, setNewValue);

// setting new key/value
person.age = 25;
console.log(person); // Proxy {name: "John", age: 25}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, a new property `age` is added to the student object.

---

## Uses of Proxy

### 1. For Validation

You can use a proxy for validation. You can check the value of a key and perform an action based on that value.

For example,

```
let student = {
    name: 'Jack',
    age: 24
}

const handler = {

    // get the object key and value
    get(obj, prop) {

    // check condition
    if (prop == 'name') {
      return obj[prop];
    } else {
      return 'Not allowed';
    }
  }
}

const proxy = new Proxy(student, handler);
console.log(proxy.name); // Jack
console.log(proxy.age); // Not allowed
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, only the name property of the student object is accessible. Else, it returns Not allowed.

---

### 2. Read Only View of an Object

There may be times when you do not want to let others make changes in an object. In such cases, you can use a proxy to make an object readable only. For example,

```
let student = {
    name: 'Jack',
    age: 23
}

const handler = {
    set: function (obj, prop, value) {
        if (obj[prop]) {
            
            // cannot change the student value
            console.log('Read only')
        }
    }
};

const proxy = new Proxy(student, handler);

proxy.name = 'John'; // Read only
proxy.age = 33; // Read only
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In the above program, one cannot mutate the object in any way.

If one tries to mutate the object in any way, you'll only receive a string saying Read Only.

---

### 3. Side Effects

You can use a proxy to call another function when a condition is met. For example,

```
const myFunction = () => {
    console.log("execute this function")
};

const handler = {
    set: function (target, prop, value) {
        if (prop === 'name' && value === 'Jack') {
            // calling another function
            myFunction();
        }
        else {
            console.log('Can only access name property');
        }
    }
};

const proxy = new Proxy({}, handler);

proxy.name = 'Jack'; // execute this function
proxy.age = 33; // Can only access name property
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

JavaScript proxy was introduced from the version of **JavaScript ES6**. Some browsers may not fully support its use. To learn more, visit [JavaScript proxy](https://caniuse.com/?search=javascript%20proxy).

---

**Also Read:**

- [JavaScript Getter and Setter](https://www.programiz.com/javascript/getter-setter)