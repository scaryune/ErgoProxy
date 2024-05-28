# JavaScript Multidimensional Array

In JavaScript, multidimensional arrays contain another [array](https://www.programiz.com/javascript/array) inside them.

Here is a simple example of a multidimensional array. Read the rest of the tutorial to learn more.

### Example

```
// multidimensional array
// contains 3 separate arrays as elements
const data = [[1, 2, 3], [1, 3, 4], [4, 5, 6]];

console.log(data);

// Output : [ [ 1, 2, 3 ], [ 1, 3, 4 ], [ 4, 5, 6 ] ]
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, we created a multidimensional array named data with the following arrays as its elements: `[ 1, 2, 3 ]`, `[ 1, 3, 4 ]`, `[ 4, 5, 6 ]`.

---

## Use Existing Arrays as Elements

We can also create multidimensional arrays by nesting existing arrays within them. For example,

```
// declare three arrays
let student1 = ['Jack', 24];
let student2 = ['Sara', 23];
let student3 = ['Peter', 24];

// create multidimensional array
// using student1, student2, and student3
let studentsData = [student1, student2, student3];

// print the multidimensional array
console.log(studentsData);

// Output: [ [ 'Jack', 24 ], [ 'Sara', 23 ], [ 'Peter', 24 ] ]
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, we first created three arrays named student1, student2, and student3.

We then nested these three arrays within the studentsData array to create our multidimensional array:

```
let studentsData = [student1, student2, student3];
```

---

## Access Elements of an Array

You can access the elements of a multidimensional array using array indexes. For example,

```
let x = [
['Jack', 24],
['Sara', 23], 
['Peter', 24]
];

// access the first item 
console.log(x[0]);  // [ 'Jack', 24 ]

// access the first item of the first inner array
console.log(x[0][0]);  // Jack

// access the second item of the third inner array
console.log(x[2][1]);  // 24
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

[ 'Jack', 24 ]
Jack
24

You can think of a multidimensional array (in this case, x), as a table with **3** rows and **2** columns.

![Accessing multidimensional array elements](https://www.programiz.com/sites/tutorial2program/files/javascript-multidimensional-array.png "Accessing multidimensional array elements")

Accessing multidimensional array elements

---

## Add Elements to a Multidimensional Array

You can use an index notation or the [push()](https://www.programiz.com/javascript/library/array/push) method to add elements to a multidimensional array.

**1. Using Index Notation**

```
let studentsData = [["Jack", 24], ["Sara", 23]];

// add "hello" as the 3rd element
// of the 2nd inner array
studentsData[1][2] = "hello";

console.log(studentsData);

// Output: [ [ 'Jack', 24 ], [ 'Sara', 23, 'hello' ] ]
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**2. Using the push() Method**

The `push()` method inserts an element at the end of the array. For example,

```
let studentsData = [["Jack", 24], ["Sara", 23]];

// add element to the end of the outer array
studentsData.push(["Peter", 24]);

console.log(studentsData);

// add "hello" as the final element
// of the 2nd inner array
studentsData[1].push("hello");

console.log(studentsData);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

[ [ 'Jack', 24 ], [ 'Sara', 23 ], [ 'Peter', 24 ] ]
[ [ 'Jack', 24 ], [ 'Sara', 23, 'hello' ], [ 'Peter', 24 ] ]

Add elements using the splice() method.

[](https://www.programiz.com/javascript/library/array/splice)

[](https://www.programiz.com/javascript/online-compiler)

---

## Remove Elements From a Multidimensional Array

You can use the [splice()](https://www.programiz.com/javascript/library/array/splice) method to remove an element from any position in the multidimensional array. For example,

```
let studentsData = [['Jack', 24], ['Sara', 23],];

// remove one element
// starting from index 0
studentsData.splice(0,1);

console.log(studentsData);

// Output: [ [ 'Sara', 23 ] ]
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In the above program, `studentsData.splice(0,1)` removes the first element of the multidimensional array. Here,

- **0** - The start index from where to modify the array.
- **1** - The number of elements to delete.

If you want to delete both arrays, you can use the code `studentsData.splice(0,2)`.

Remove the last element using the pop() method.

[](https://www.programiz.com/javascript/library/array/pop)

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/online-compiler)

---

## Iterate Over Multidimensional Array

In JavaScript, you can use nested loops to go through a multidimensional array: one loop for the outer array and another loop inside it for the inner arrays. For example,

```
let studentsData = [["Jack", 24], ["Sara", 23]];

// loop over outer array
for(let i = 0; i < studentsData.length; i++) {

    // loop over inner array elements
    for(let j = 0; j < studentsData[i].length; j++) {
        console.log(studentsData[i][j]);
    }
}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Jack
24
Sara
23

Use forEach() to Iterate Over Multidimensional Array

[](https://www.programiz.com/javascript/library/array/foreach)

[](https://www.programiz.com/javascript/online-compiler)

Use for...of to Iterate Over Multidimensional Array