# JavaScript for... of Loop

In JavaScript, there are three ways we can use a `for` loop.

- [JavaScript for loop](https://www.programiz.com/javascript/for-loop)
- [JavaScript for...in loop](https://www.programiz.com/javascript/for-in)
- [JavaScript for...of loop](https://www.programiz.com/javascript/for-of)

The `for...of` loop was introduced in the later versions of [JavaScript ES6](https://www.programiz.com/javascript/ES6).

The `for..of` loop in JavaScript allows you to iterate over iterable objects (arrays, sets, maps, strings etc).

---

## JavaScript for...of loop

The syntax of the `for...of` loop is:

```
for (element of iterable) {
    // body of for...of
}
```

Here,

- **iterable** - an iterable object (array, set, strings, etc).
- **element** - items in the iterable

In plain English, you can read the above code as: for every element in the iterable, run the body of the loop.

---

## for...of with Arrays

The `for..of` loop can be used to iterate over an [array](https://www.programiz.com/javascript/array). For example,

```
// array
const students = ['John', 'Sara', 'Jack'];

// using for...of
for ( let element of students ) {

    // display the values
    console.log(element);
}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

John
Sara
Jack

In the above program, the `for...of` loop is used to iterate over the students array object and display all its values.

---

## for...of with Strings

You can use `for...of` loop to iterate over [string](https://www.programiz.com/javascript/string) values. For example,

```
// string
const string = 'code';

// using for...of loop
for (let i of string) {
    console.log(i);
}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

c
o
d
e

---

## for...of with Sets

You can iterate through [Set](https://www.programiz.com/javascript/set-weakset) elements using the `for...of` loop. For example,

```
// define Set
const set = new Set([1, 2, 3]);

// looping through Set
for (let i of set) {
    console.log(i);
}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

1
2
3

---

## for...of with Maps

You can iterate through [Map](https://www.programiz.com/javascript/map-weakmap) elements using the `for...of` loop. For example,

```
// define Map
let map = new Map();

// inserting elements
map.set('name', 'Jack');
map.set('age', '27');

// looping through Map
for (let [key, value] of map) {
    console.log(key + '- ' + value);
}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

name- Jack
age- 27

---

## User Defined Iterators

You can create an iterator manually and use the `for...of` loop to iterate through the [iterators](https://www.programiz.com/javascript/iterators-iterables). For example,

```
// creating iterable object
const iterableObj = {

    // iterator method
    [Symbol.iterator]() {
        let step = 0;
        return {
            next() {
                step++;
                if (step === 1) {
                    return { value: '1', done: false};
                 }
                else if (step === 2) {
                    return { value: '2', done: false};
                }
                else if (step === 3) {
                    return { value: '3', done: false};
                }
                return { value: '', done: true };
            }
        }
    }
}

// iterating using for...of
for (const i of iterableObj) {
 console.log(i);
}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

1
2
3

---

## for...of with Generators

Since generators are iterables, you can implement an iterator in an easier way. Then you can iterate through the [generators](https://www.programiz.com/javascript/generators) using the `for...of` loop. For example,

```
// generator function
function* generatorFunc() {
  
    yield 10;
    yield 20;
    yield 30;
}

const obj = generatorFunc();

// iteration through generator
for (let value of obj) {
    console.log(value);
}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

10
20
30

---

## for...of Vs for...in

|for...of|for...in|
|---|---|
|The `for...of` loop is used to iterate through the values of an iterable.|The `for...in` loop is used to iterate through the keys of an object.|
|The `for...of` loop cannot be used to iterate over an object.|You can use `for...in` to iterate over an iterable such arrays and strings but you should avoid using `for...in` for iterables.|

---

The `for...of` loop was introduced in **ES6**. Some browsers may not support its use. To learn more, visit [JavaScript for...of Support](https://caniuse.com/?search=javascript%20for...of).