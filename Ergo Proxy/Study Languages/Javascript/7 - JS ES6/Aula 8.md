# JavaScript Destructuring Assignment

## JavaScript Destructuring

The destructuring assignment introduced in [ES6](https://www.programiz.com/javascript/ES6) makes it easy to assign [array](https://www.programiz.com/javascript/array) values and [object properties](https://www.programiz.com/javascript/object#properties) to distinct [variables](https://www.programiz.com/javascript/variables-constants). For example,  
  
**Before ES6:**

```
// assigning object attributes to variables
const person = {
    name: 'Sara',
    age: 25,
    gender: 'female'    
}

let name = person.name;
let age = person.age;
let gender = person.gender;

console.log(name); // Sara
console.log(age); // 25
console.log(gender); // female
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**From ES6:**

```
// assigning object attributes to variables
const person = {
    name: 'Sara',
    age: 25,
    gender: 'female'    
}

// destructuring assignment
let { name, age, gender } = person;

console.log(name); // Sara
console.log(age); // 25
console.log(gender); // female
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Note**: The order of the name does not matter in object destructuring.

For example, you could write the above program as:

```
let { age, gender, name } = person;
console.log(name); // Sara
```

**Note**: When destructuring objects, you should use the same name for the variable as the corresponding object key.

For example,

```
let {name1, age, gender} = person;
console.log(name1); // undefined
```

If you want to assign different variable names for the object key, you can use:

```
const person = {
    name: 'Sara',
    age: 25,
    gender: 'female'    
}

// destructuring assignment
// using different variable names
let { name: name1, age: age1, gender:gender1 } = person;

console.log(name1); // Sara
console.log(age1); // 25
console.log(gender1); // female
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## Array Destructuring

You can also perform array destructuring in a similar way. For example,

```
const arrValue = ['one', 'two', 'three'];

// destructuring assignment in arrays
const [x, y, z] = arrValue;

console.log(x); // one
console.log(y); // two
console.log(z); // three
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## Assign Default Values

You can assign the default values for variables while using destructuring. For example,

```
let arrValue = [10];

// assigning default value 5 and 7
let [x = 5,  y = 7] = arrValue;

console.log(x); // 10
console.log(y); // 7
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In the above program, arrValue has only one element. Hence,

- the x variable will be **10**
- the y variable takes the default value **7**

In object destructuring, you can pass default values in a similar way. For example,

```
const person = {
    name: 'Jack',
}

// assign default value 26 to age if undefined
const { name, age = 26} = person;

console.log(name); // Jack
console.log(age); // 26
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## Swapping Variables

In this example, two variables are swapped using the destructuring assignment syntax.

```
// program to swap variables

let x = 4;
let y = 7;

// swapping variables
[x, y] = [y, x];

console.log(x); // 7
console.log(y); // 4
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## Skip Items

You can skip unwanted items in an array without assigning them to local variables. For example,

```
const arrValue = ['one', 'two', 'three'];

// destructuring assignment in arrays
const [x, , z] = arrValue;

console.log(x); // one
console.log(z); // three
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In the above program, the second element is omitted by using the comma separator `,`.

---

## Assign Remaining Elements to a Single Variable

You can assign the remaining elements of an array to a variable using the spread syntax `...`. For example,

```
const arrValue = ['one', 'two', 'three', 'four'];

// destructuring assignment in arrays
// assigning remaining elements to y
const [x, ...y] = arrValue;

console.log(x); // one
console.log(y); // ["two", "three", "four"]
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, `one` is assigned to the x variable. And the rest of the array elements are assigned to y variable.

You can also assign the rest of the object properties to a single variable. For example,

```
const person = {
    name: 'Sara',
    age: 25,
    gender: 'female'    
}

// destructuring assignment
// assigning remaining properties to rest
let { name, ...rest } = person;

console.log(name); // Sara
console.log(rest); // {age: 25, gender: "female"}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Note**: The variable with the spread syntax cannot have a trailing comma `,`. You should use this rest element (variable with spread syntax) as the last variable.

For example,

```
const arrValue = ['one', 'two', 'three', 'four'];

// throws an error
const [ ...x, y] = arrValue;

console.log(x); // eror
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## Nested Destructuring Assignment

You can perform nested destructuring for array elements. For example,

```
// nested array elements
const arrValue = ['one', ['two', 'three']];

// nested destructuring assignment in arrays
const [x, [y, z]] = arrValue;

console.log(x); // one
console.log(y); // two
console.log(z); // three
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, the variable y and z are assigned nested elements `two` and `three`.

In order to execute the nested destructuring assignment, you have to enclose the variables in an array structure (by enclosing inside `[]`).

You can also perform nested destructuring for object properties. For example,

```
const person = {
    name: 'Jack',
    age: 26,
    hobbies: {
        read: true,
        playGame: true
    }
}
// nested destructuring 
const {name, hobbies: {read, playGame}} = person;

console.log(name); // Jack
console.log(read); // true
console.log(playGame); // true
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In order to execute the nested destructuring assignment for objects, you have to enclose the variables in an object structure (by enclosing inside `{}`).

---

**Note**: Destructuring assignment feature was introduced in **ES6**. Some browsers may not support the use of the destructuring assignment. Visit [Javascript Destructuring support](https://caniuse.com/#search=destructuring) to learn more.