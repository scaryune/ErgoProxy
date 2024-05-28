# JavaScript Spread Operator

The JavaScript spread operator `...` is used to expand or spread out elements of an iterable, such as an [array](https://www.programiz.com/javascript/array), [string](https://www.programiz.com/javascript/string), or [object](https://www.programiz.com/javascript/object).

This makes it incredibly useful for tasks like combining arrays, passing elements to [functions](https://www.programiz.com/javascript/function) as separate arguments, or even copying arrays.

Here's a quick example of the spread statement. You can read the rest of the tutorial for more.

### Example

```
let numbers = [1, 2, 3];

// equivalent to
// console.log(numbers[0], numbers[1], numbers[2])
console.log(...numbers);

// Output: 1 2 3
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, we used the spread operator `...` inside `console.log()` to expand the numbers array into individual elements.

---

## JavaScript Spread Operator Inside Arrays

We can also use the spread operator inside arrays to expand the elements of another array. For example,

```
let fruits = ["Apple", "Banana", "Cherry"];

// add fruits array to moreFruits1
// without using the ... operator
let moreFruits1 = ["Dragonfruit", fruits, "Elderberry"];

// spread fruits array within moreFruits2 array
let moreFruits2 = ["Dragonfruit", ...fruits, "Elderberry"];

console.log(moreFruits1);
console.log(moreFruits2);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

[ 'Dragonfruit', [ 'Apple', 'Banana', 'Cherry' ], 'Elderberry' ]
[ 'Dragonfruit', 'Apple', 'Banana', 'Cherry', 'Elderberry' ]

Here, `...fruits` expands the fruits array inside the moreFruits2 array, which results in moreFruits2 consisting only of individual string elements and no inner arrays.

On the other hand, the moreFruits1 array consists of an inner array because we didn't expand the fruits array inside it.

**Note:** Since the spread operator was introduced in [ES6](https://www.programiz.com/javascript/ES6), some browsers may not support its use. To learn more, visit [JavaScript Spread Operator support](https://caniuse.com/#search=spread%20operator).

Clone Array Using Spread Operator

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/online-compiler)

---

## Spread Operator With Object

You can also use the spread operator with object literals. For example,

```
let obj1 = { x : 1, y : 2 };
let obj2 = { z : 3 };

// use the spread operator to add
// members of obj1 and obj2 to obj3
let obj3 = {...obj1, ...obj2};

// add obj1 and obj2 without spread operator
let obj4 = {obj1, obj2};

console.log("obj3 =", obj3);
console.log("obj4 =", obj4);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

obj3 = { x: 1, y: 2, z: 3 }
obj4 = { obj1: { x: 1, y: 2 }, obj2: { z: 3 } }

Here, the properties of obj1 and obj2 are added to obj3 using the spread operator.

However, when we add those two objects to obj4 without using the spread operator, we get `obj1` and `obj2` as keys for obj4.

---

## JavaScript Rest Parameter

When the spread operator is used as a parameter, it is known as the **rest parameter**.

You can accept multiple arguments in a function call using the rest parameter. For example,

```
let printArray = function(...args) {
    console.log(args);
}

// pass a single argument
printArray(3);

// pass multiple arguments
printArray(4, 5, 6);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

[ 3 ]
[ 4, 5, 6 ]

Here,

- When a single argument is passed to `printArray()`, the rest parameter takes only one parameter.
- When three arguments are passed, the rest parameter takes all three parameters.

**Note**: Using the rest parameter will pass the arguments as array elements.

---

## Spread Operator as Part of Function Argument

You can also use the spread operator as part of a function argument. For example,

```
// function that takes three arguments
function sum(num1, num2 , num3) {
    console.log(num1 + num2 + num3);
}

let num1 = [1, 3, 4, 5];

// pass the first three array elements
sum(...num1); 

// Output: 8
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

If you pass multiple arguments using the spread operator, the function takes the required number of arguments and ignores the rest.

---

**Also Read:**

- [JavaScript Program to Append an Object to an Array](https://www.programiz.com/javascript/examples/append-object-array)

- [](https://www.programiz.com/javascript/spread-operator#introduction)
- [](https://www.programiz.com/javascript/spread-operator#array)
- [](https://www.programiz.com/javascript/spread-operator#object)
- [](https://www.programiz.com/javascript/spread-operator#rest-parameter)
- [](https://www.programiz.com/javascript/spread-operator#function-argument)