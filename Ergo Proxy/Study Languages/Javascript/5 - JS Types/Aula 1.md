# JavaScript Array

An array is an [object](https://www.programiz.com/javascript/object) that can store multiple values at once.

```
const age = [17, 18, 15, 19, 14];
```

In the above example, we created an array to record the age of five students.

![Array of Five Elements](https://www.programiz.com/sites/tutorial2program/files/javascript-array_1.png "Array of Five Elements")

Array of Five Elements

### Why Use Arrays?

Arrays allow us to organize related data by grouping them within a single variable.

Suppose you want to store a list of fruits. Using only variables, this process might look like this:

```
let fruit1 = "Apple";
let fruit2 = "Banana";
let fruit3 = "Orange";
```

Here, we've only listed a few fruits. But what if we need to store **100** fruits?

For such a case, the easiest solution is to store them in an array.

```
let fruits = ["Apple", "Banana", "Orange", ...];
```

An array can store many values in a single variable, making it easy to access them by referring to the corresponding index number.

---

## Create an Array

We can create an array by placing elements inside an array literal `[]`, separated by commas. For example,

```
const numbers = [10, 30, 40, 60, 80];
```

Here,

- `numbers` - Name of the array.
- `[10, 30, 40, 60, 80]` - Elements of the array.

Examples of JavaScript Arrays

---

## Access Elements of an Array

Each element of an array is associated with a number called an **index**, which specifies its position inside the array.

Consider the following array:

```
let numbers = [10, 30, 40, 60, 80];
```

Here is the indexing of each element:

![Index of Array Elements](https://www.programiz.com/sites/tutorial2program/files/javascript-array-index_1.png "Index of Array Elements")

Index of Array Elements

We can use an array index to access the elements of the array.

|Code|Description|
|---|---|
|`numbers[0]`|Accesses the first element **10**.|
|`numbers[1]`|Accesses the second element **30**.|
|`numbers[2]`|Accesses the third element **40**.|
|`numbers[3]`|Accesses the fourth element **60**.|
|`numbers[4]`|Accesses the fifth element **80**.|

Let's look at an example.

```
let numbers = [10, 30, 40, 60, 80]

// access first element
console.log(numbers[0]);  // 10

// access third element
console.log(numbers[2]);  // 40
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Remember:** Array indexes always start with **0**, not **1.**

---

## Add Element to an Array

We can add elements to an array using built-in methods like `push()` and `unshift()`.

**1. Using the push() Method**

The `push()` method adds an element at the end of the array.

```
let dailyActivities = ["eat", "sleep"];

// add an element at the end
dailyActivities.push("exercise");

console.log(dailyActivities);

// Output: [ 'eat', 'sleep', 'exercise' ]
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**2. Using the unshift() Method**

The `unshift()` method adds an element at the beginning of the array.

```
let dailyActivities = ["eat", "sleep"];

// add an element at the beginning
dailyActivities.unshift("work"); 

console.log(dailyActivities);

// Output: [ 'work', 'eat', 'sleep' ]
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

To learn more, visit [Array push()](https://www.programiz.com/javascript/library/array/push) and [Array unshift()](https://www.programiz.com/javascript/library/array/unshift).

---

## Change the Elements of an Array

We can add or change elements by accessing the index value. For example,

```
let dailyActivities = [ "eat", "work", "sleep"];

// change the second element
// use array index 1
dailyActivities[1] = "exercise";

console.log(dailyActivities);

// Output: [ 'eat', 'exercise', 'sleep' ]
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, we changed the array element in index **1** (second element) from `work` to `exercise`.

---

## Remove Elements From an Array

We can remove an element from any specified index of an array using the `splice()` method.

```
let numbers = [1, 2, 3, 4, 5];

// remove one element
// starting from index 2
numbers.splice(2, 1);

console.log(numbers);

// Output: [ 1, 2, 4, 5 ]
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In this example, we removed the element at index **2** (the third element) using the `splice()` method.

Notice the following code:

```
numbers.splice(2, 1);
```

Here, `(2, 1)` means that the `splice()` method deletes one element starting from index **2**.

**Note:** Suppose you want to remove the second, third, and fourth elements. You can use the following code to do so:

```
numbers.splice(1, 3);
```

To learn more, visit [JavaScript Array splice()](https://www.programiz.com/javascript/library/array/splice).

---

## Array Methods

JavaScript has various array methods to perform useful operations. Some commonly used array methods in JavaScript are:

|Method|Description|
|---|---|
|[concat()](https://www.programiz.com/javascript/library/array/concat)|Joins two or more arrays and returns a result.|
|[toString()](https://www.programiz.com/javascript/library/array/tostring)|Converts an array to a string of (comma-separated) array values.|
|[indexOf()](https://www.programiz.com/javascript/library/array/indexof)|Searches an element of an array and returns its position (index).|
|[find()](https://www.programiz.com/javascript/library/array/find)|Returns the first value of the array element that passes a given test.|
|[findIndex()](https://www.programiz.com/javascript/library/array/findindex)|Returns the first index of the array element that passes a given test.|
|[forEach()](https://www.programiz.com/javascript/library/array/foreach)|Calls a function for each element.|
|[includes()](https://www.programiz.com/javascript/library/array/includes)|Checks if an array contains a specified element.|
|[sort()](https://www.programiz.com/javascript/library/array/sort)|Sorts the elements alphabetically in strings and ascending order in numbers.|
|[slice()](https://www.programiz.com/javascript/library/array/slice)|Selects part of an array and returns it as a new array.|
|[splice()](https://www.programiz.com/javascript/library/array/splice)|Removes or replaces existing elements and/or adds new elements.|

To learn more, visit [JavaScript Array Methods](https://www.programiz.com/javascript/library/array).

---

## More on Javascript Array

Create an array using the new keyword.

[](https://www.programiz.com/javascript/online-compiler)

Remove elements from an array using pop() and shift() methods.

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/library/array/pop)[](https://www.programiz.com/javascript/library/array/shift)

Length of an Array.

[](https://www.programiz.com/javascript/online-compiler)

Relationship between arrays and objects in JavaScript.

[](https://www.programiz.com/javascript/online-compiler)

---

**Also Read:**

- [JavaScript forEach](https://www.programiz.com/javascript/forEach)
- [JavaScript for...of](https://www.programiz.com/javascript/for-of)
- [JavaScript Multidimensional Array](https://www.programiz.com/javascript/multidimensional-array)