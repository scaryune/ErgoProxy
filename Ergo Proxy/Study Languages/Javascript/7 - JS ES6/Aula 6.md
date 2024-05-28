# JavaScript Map

The JavaScript **ES6** has introduced two new data structures, i.e `Map` and `WeakMap`.

Map is similar to objects in JavaScript that allows us to store elements in a **key/value** pair.

The elements in a Map are inserted in an insertion order. However, unlike an object, a map can contain [objects](https://www.programiz.com/javascript/object), [functions](https://www.programiz.com/javascript/function) and other [data types](https://www.programiz.com/javascript/data-types) as key.

---

## Create JavaScript Map

To create a `Map`, we use the `new Map()` constructor. For example,

```
// create a Map
const map1 = new Map(); // an empty map
console.log(map1); // Map {}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## Insert Item to Map

After you create a map, you can use the `set()` method to insert elements to it. For example,

```
// create a set
let map1 = new Map();

// insert key-value pair
map1.set('info', {name: 'Jack', age: 26});
console.log(map1); // Map {"info" => {name: "Jack", age: 26}}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

You can also use objects or functions as keys. For example,

```
// Map with object key
let map2 = new Map();

let obj = {};
map2.set(obj, {name: 'Jack', age: "26"});

console.log(map2); // Map {{} => {name: "Jack", age: "26"}}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## Access Map Elements

You can access `Map` elements using the `get()` method. For example,

```
let map1 = new Map();
map1.set('info', {name: 'Jack', age: "26"});

// access the elements of a Map
console.log(map1.get('info')); // {name: "Jack", age: "26"}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## Check Map Elements

You can use the `has()` method to check if the element is in a Map. For example,

```
const set1 = new Set([1, 2, 3]);

let map1 = new Map();
map1.set('info', {name: 'Jack', age: "26"});

// check if an element is in Set
console.log(map1.has('info')); // true
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## Removing Elements

You can use the `clear()` and the `delete()` method to remove elements from a Map.

The `delete()` method returns `true` if a specified key/value pair exists and has been removed or else returns `false`. For example,

```
let map1 = new Map();
map1.set('info', {name: 'Jack', age: "26"});

// removing a particular element
map1.delete('address'); // false
console.log(map1); // Map {"info" => {name: "Jack", age: "26"}} 

map1.delete('info'); // true
console.log(map1); // Map {}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

The `clear()` method removes all key/value pairs from a Map object. For example,

```
let map1 = new Map();
map1.set('info', {name: 'Jack', age: "26"});

// removing all element
map1.clear();
console.log(map1); // Map {}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## JavaScript Map Size

You can get the number of elements in a Map using the `size` property. For example,

```
let map1 = new Map();
map1.set('info', {name: 'Jack', age: "26"});

console.log(map1.size); // 1
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## Iterate Through a Map

You can iterate through the Map elements using the [for...of](https://www.programiz.com/javascript/for-of) loop or [forEach()](https://www.programiz.com/javascript/forEach) method. The elements are accessed in the insertion order. For example,

```
let map1 = new Map();
map1.set('name', 'Jack');
map1.set('age', '27');

// looping through Map
for (let [key, value] of map1) {
    console.log(key + '- ' + value);
}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

name- Jack
age- 27

You could also get the same results as the above program using the `forEach()` method. For example,

```
// using forEach method()
let map1 = new Map();
map1.set('name', 'Jack');
map1.set('age', '27');

// looping through Map
map1.forEach(function(value, key) {
  console.log(key + '- ' + value)
})
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## Iterate Over Map Keys

You can iterate over the Map and get the key using the [key()](https://www.programiz.com/javascript/library/object/keys) method. For example,

```
let map1 = new Map();
map1.set('name', 'Jack');
map1.set('age', '27');

// looping through the Map
for (let key of map1.keys()) {
  console.log(key)
}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

name
age

---

## Iterate Over Map Values

You can iterate over the Map and get the values using the [values()](https://www.programiz.com/javascript/library/object/values) method. For example,

```
let map1 = new Map();
map1.set('name', 'Jack');
map1.set('age', '27');

// looping through the Map
for (let values of map1.values()) {
    console.log(values);
}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Jack
27

---

## Get Key/Values of Map

You can iterate over the Map and get the key/value of a Map using the [entries()](https://www.programiz.com/javascript/library/object/entries) method. For example,

```
let map1 = new Map();
map1.set('name', 'Jack');
map1.set('age', '27');

// looping through the Map
for (let elem of map1.entries()) {
    console.log(`${elem[0]}: ${elem[1]}`);
}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

name: Jack
age: 27

---

## JavaScript Map vs Object

|Map|Object|
|---|---|
|Maps can contain objects and other data types as keys.|Objects can only contain strings and symbols as keys.|
|Maps can be directly iterated and their value can be accessed.|Objects can be iterated by accessing its keys.|
|The number of elements of a Map can be determined by `size` property.|The number of elements of an object needs to be determined manually.|
|Map performs better for programs that require the addition or removal of elements frequently.|Object does not perform well if the program requires the addition or removal of elements frequently.|

---

## JavaScript WeakMap

The WeakMap is similar to a Map. However, WeakMap can only contain objects as keys. For example,

```
const weakMap = new WeakMap();
console.log(weakMap); // WeakMap {} 

let obj = {};

// adding object (element) to WeakMap
weakMap.set(obj, 'hello');

console.log(weakMap); // WeakMap {{} => "hello"}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

When you try to add other data types besides objects, WeakMap throws an error. For example,

```
const weakMap = new WeakMap();

// adding string as a key to WeakMap
weakMap.set('obj', 'hello');
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

// throws error
// TypeError: Attempted to set a non-object key in a WeakMap

---

## WeakMap Methods

WeakMaps have methods `get()`, `set()`, `delete()`, and `has()`. For example,

```
const weakMap = new WeakMap();
console.log(weakMap); // WeakMap {} 

let obj = {};

// adding object (element) to WeakMap
weakMap.set(obj, 'hello');

console.log(weakMap); // WeakMap {{} => "hello"}

// get the element of a WeakMap
console.log(weakMap.get(obj)); // hello

// check if an element is present in WeakMap
console.log(weakMap.has(obj)); // true

// delete the element of WeakMap
console.log(weakMap.delete(obj)); // true

console.log(weakMap); // WeakMap {} 
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## WeakMaps Are Not iterable

Unlike Maps, WeakMaps are not iterable. For example,

```
const weakMap = new WeakMap();
console.log(weakMap); // WeakMap {} 

let obj = {};

// adding object (element) to WeakMap
weakMap.set(obj, 'hello');


// looping through WeakMap
for (let i of weakMap) {

    console.log(i);  // TypeError
}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

JavaScript `Map` and `WeakMap` were introduced in **ES6**. Some browsers may not support their use. To learn more, visit [JavaScript Map support](https://caniuse.com/?search=JavaScript%20Map) and [JavaScript WeakMap support](https://caniuse.com/?search=JavaScript%20WeakMap).

---

**Also Read:**

- [JavaScript ES6](https://www.programiz.com/javascript/ES6)
- [JavaScript Set and WeakSet](https://www.programiz.com/javascript/set-weakset)