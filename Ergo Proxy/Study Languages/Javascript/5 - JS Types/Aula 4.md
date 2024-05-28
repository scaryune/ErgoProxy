# JavaScript for...in loop

Before reading this tutorial, make sure you first learn about [JavaScript objects](https://www.programiz.com/javascript/object).

---

The JavaScript `for...in` loop iterates over the keys of an object.

Here's a simple example of the `for...in` loop in JavaScript. Read the rest of the tutorial to learn more.

### Example

```
const student = {
    name: "Monica",
    class: 7
};

// loop through the keys of student object
for (let key in student) {

    // display the key-value pairs
    console.log(`${key} => ${student[key]}`);
};

// Output:
// name => Monica
// class => 7
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, the `for...in` loop iterates over the keys of the student object. In each iteration of the loop, the key variable stores a single key belonging to student.

---

## Syntax of JavaScript for...in Loop

```
for (key in object) {
    // body of for...in
};
```

Here,

- object - The object whose keys we want to iterate over.
- key - A variable that stores a single key belonging to object.

**Working of for...in Loop**

1. In the first iteration, the key variable is assigned the first key of object. The body of the loop is then executed.
2. In the second iteration, the key variable is assigned the next key of object. The body of the loop is then executed.
3. This process continues until there are no more keys over which to iterate.

**Note**: Once you get the keys of an object, you can easily find their corresponding values.

---

## Example: JavaScript for...in Loop

```
const salaries = {
    Jack: 24000,
    Paul: 34000,
    Monica: 55000
};

// use for...in to loop through
// properties of salaries
for (let i in salaries) {

    // access object key using [ ]
    // add a $ symbol before the key
    let salary = "$" + salaries[i];

    // display the values
    console.log(`${i}: ${salary}`);
};
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

Jack: $24000,
Paul: $34000,
Monica: $55000

In the above example, we used the `for...in` loop to iterate over the properties of the salaries object. Then, we added the string `$` to each value of the object.

**Note:** We have used the variable i instead of key because we can use any valid variable name.

---

## More on JavaScript for...in Loop

JavaScript for...in With Strings

[](https://www.programiz.com/javascript/string)

[](https://www.programiz.com/javascript/online-compiler)

JavaScript for...in With Arrays

[](https://www.programiz.com/javascript/array)

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/for-of)

---

**Also Read:**

- [JavaScript while and do...while loop](https://www.programiz.com/javascript/while-loop)
- [JavaScript for loop](https://www.programiz.com/javascript/for-loop)
- [JavaScript forEach()](https://www.programiz.com/javascript/forEach)

- [](https://www.programiz.com/javascript/for-in#introduction)
- [](https://www.programiz.com/javascript/for-in#syntax)
- [](https://www.programiz.com/javascript/for-in#example)