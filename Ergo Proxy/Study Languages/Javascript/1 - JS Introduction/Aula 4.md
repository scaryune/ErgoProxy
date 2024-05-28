# JavaScript Data Types

Data types represent the different kinds of values we can use in JavaScript.

There are altogether **8** basic data types in JavaScript.

|Data Type|Description|Example|
|---|---|---|
|`String`|Textual data.|`'hello'`, `"hello world!"`, etc.|
|`Number`|An integer or a floating-point number.|`3`, `3.234`, `3e-2`, etc.|
|`BigInt`|An integer with arbitrary precision.|`900719925124740999n`, `1n`, etc.|
|`Boolean`|Any of two values: `true` or `false`.|`true` and `false`|
|`undefined`|A data type whose variable is not initialized.|`let a;`|
|`null`|Denotes a `null` value.|`let a = null;`|
|`Symbol`|A data type whose instances are unique and immutable.|`let value = Symbol('hello');`|
|`Object`|Key-value pairs of collection of data.|`let student = {name: "John"};`|

**Note:** JavaScript data types are divided into primitive and non-primitive types.

- **Primitive Data Types:** They can hold a single simple value. `String`, `Number`, `BigInt`, `Boolean`, `undefined`, `null`, and `Symbol` are primitive data types.

- **Non-Primitive Data Types:** They can hold multiple values. `Objects` are non-primitive data types.

---

## JavaScript String

A string represents textual data. It contains a sequence of characters. For example, `"hello"`, `"JavaScript"`, etc.

In JavaScript, strings are surrounded by quotes:

- **Single quotes:** `'Hello'`
- **Double quotes:** `"Hello"`
- **Backticks:** `` `Hello` ``

For example,

```
// string enclosed within single quotes
let fruit = 'apple';
console.log(fruit)

// string enclosed within double quotes
let country = "USA";
console.log(country);

// string enclosed within backticks
let result = `fail`;
console.log(result);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

apple
USA
fail

In a string, we can either use single quotes or double quotes. However, it is recommended to use double quotes.

**Note:** It is illegal to mismatch quotes in strings. For example, the strings `'hello"` and `"world'` are enclosed inside one single quote and one double quote, which results in an error.

To learn more about strings, visit [JavaScript String](https://www.programiz.com/javascript/string).

---

## JavaScript Number

In JavaScript, the **number** type represents numeric values (both integers and floating-point numbers).

- **Integers** - Numeric values without any decimal parts. Example: **3**, **-74**, etc.
- **Floating-Point** - Numeric values with decimal parts. Example: **3.15**, **-1.3**, etc.

```
// integer value
let integer_number = -3;
console.log(integer_number);

// floating-point value
let float_number = 3.15;
console.log(float_number);
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

-3
3.15

To learn more about numbers, visit [JavaScript Number](https://www.programiz.com/javascript/numbers).

## Special Numeric Values

JavaScript can also represent special numeric values.

[](https://www.programiz.com/javascript/online-compiler)

---

## JavaScript BigInt

**BigInt** is a type of number that can represent very large or very small integers beyond the range of the regular **number** data type.

**Note:** The regular number data type can handle values less than **(2^53 - 1)** and greater than **-(2^53 - 1)**.

A `BigInt` number is created by appending `n` to the end of an integer. For example,

```
// BigInt value
let value1 = 900719925124740998n;

// add two big integers
let result1 = value1 + 1n;
console.log(result1);  // "900719925124740999n"

let value2 = 900719925124740998n;
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

900719925124740999n
TypeError: Cannot mix BigInt and other types, use explicit conversions

**Note:** `BigInt` was introduced in a newer version of JavaScript (ES11) and is not supported by many browsers, including Safari. To learn more, visit [JavaScript BigInt support](https://caniuse.com/#feat=bigint).

## You can't mix BigInt and number

You can't mix BigInt and number values.

[](https://www.programiz.com/javascript/online-compiler)

---

## JavaScript Boolean

A `Boolean` data can only have one of two values: `true` or `false`. For example,

```
let dataChecked = true;
console.log(dataChecked);  // true

let valueCounted = false;
console.log(valueCounted);  // false
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

If you want to learn more about booleans, visit [JavaScript Booleans](https://www.programiz.com/javascript/booleans).

---

## JavaScript undefined

In JavaScript, `undefined` represents the absence of a value.

If a variable is declared but the value is not assigned, then the value of that variable will be `undefined`. For example,

```
let name;
console.log(name);  // undefined
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

It is also possible to explicitly assign `undefined` as a variable value. For example,

```
let name = undefined;
console.log(name);  // undefined
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Note:** You should avoid explicitly assigning `undefined` to a variable. Usually, we assign `null` to variables to indicate "unknown" or "empty" values.

---

## JavaScript null

In JavaScript, `null` represents **"no value"** or **"nothing."** For example,

```
let number = null;
console.log(number);  // null
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, `let number = null;` indicates that the number variable is set to have no value.

Visit [JavaScript null and undefined](https://www.programiz.com/javascript/null-undefined) to learn more.

---

## JavaScript Symbol

A `Symbol` is a unique and primitive value. This data type was introduced in **ES6**.

When you create a `Symbol`, JavaScript guarantees that it is distinct from all other symbols, even if they have the same descriptions. For example,

```
// two symbols with the same description
let value1 = Symbol("programiz");
let value2 = Symbol("programiz");

console.log(value1 === value2);  // false
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, we have used `===` to compare value1 and value2. It returns `true` if the two values are exactly the same. Otherwise, it returns `false`.

Though both value1 and value2 contain `"programiz"`, JavaScript treats them as different since they are of the `Symbol` type. Hence, `value1 === value2` returns `false`.

To learn more, visit [JavaScript Symbol](https://www.programiz.com/javascript/symbol).

---

## JavaScript Object

An `Object` holds data in the form of key-value pairs. For example,

```
let student = {
    firstName: "John",
    lastName: null,
    class: 10
};
```

Here, we have created an object named student that contains key-value pairs:

|Key|Value|
|---|---|
|`firstName`|`"John"`|
|`lastName`|`null`|
|`class`|`10`|

To learn more, visit [JavaScript Objects](https://www.programiz.com/javascript/object).

---

## More on JavaScript Data Types

How can you check the data type of a variable?

[](https://www.programiz.com/javascript/typeof)

[](https://www.programiz.com/javascript/online-compiler)

JavaScript automatically determines the variable's data type.