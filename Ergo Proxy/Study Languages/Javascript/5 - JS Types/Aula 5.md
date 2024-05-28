# JavaScript Number

In JavaScript, numbers are used to represent numerical values. They can be whole numbers (like **5**, **10**, **100**) or decimal numbers (like **3.13**, **0.5**, **10.75**). For example,

```
let num1 = 5;
let num2 = 3.13;

console.log(num1); // 5
console.log(num2); // 3.13
```

---

## JavaScript NaN

`NaN` (Not a Number) is a special value that is returned when a mathematical operation cannot produce a meaningful numeric result.

Performing arithmetic operations (except addition) on numeric values and strings results in `NaN`. For example,

```
let num = 4 - "hello";
console.log(num); // NaN
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

NaN is a Number

[](https://www.programiz.com/javascript/online-compiler)

JavaScript isNaN() Method

[](https://www.programiz.com/javascript/online-compiler)

---

## JavaScript Infinity

`Infinity` is a special value that signifies an amount larger than any finite number. For example,

```
let num1 = 2 / 0;
console.log(num1); // Infinity

let num2 = -2 / 0;
console.log(num2); // -Infinity
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, dividing a positive number by **0** yields `Infinity`, while dividing a negative number by **0** results in `-Infinity`.

Exponential Numbers

[](https://www.programiz.com/javascript/online-compiler)

Hexadecimal Numbers

[](https://www.programiz.com/javascript/online-compiler)

---

## JavaScript Number Methods

Here is a list of built-in number methods in JavaScript.

|Method|Description|
|---|---|
|[isNaN()](https://www.programiz.com/javascript/library/built-in/isNaN)|Determines whether the passed value is `NaN`.|
|[isFinite()](https://www.programiz.com/javascript/library/built-in/isfinite)|Determines whether the passed value is a finite number.|
|[isInteger()](https://www.programiz.com/javascript/library/number/isinteger)|Determines whether the passed value is an integer.|
|[isSafeInteger()](https://www.programiz.com/javascript/library/number/isSafeInteger)|Determines whether the passed value is a safe integer.|
|[parseFloat()](https://www.programiz.com/javascript/library/built-in/parseFloat)|Converts the numeric floating string to a floating-point number.|
|[parseInt()](https://www.programiz.com/javascript/library/built-in/parseInt)|Converts the numeric string to an integer.|
|[toExponential()](https://www.programiz.com/javascript/library/number/toexponential)|Returns a string value for a number in exponential notation.|
|[toFixed()](https://www.programiz.com/javascript/library/number/tofixed)|Returns a string value for a number in fixed-point notation.|
|[toPrecision()](https://www.programiz.com/javascript/library/number/toprecision)|Returns a string value for a number to a specified precision.|
|[toString()](https://www.programiz.com/javascript/library/number/toString)|Returns a string value in a specified radix (base).|
|[valueOf()](https://www.programiz.com/javascript/library/object/valueOf)|Returns the number's value.|
|[toLocaleString()](https://www.programiz.com/javascript/library/number/tolocalestring)|Returns a string with a language-sensitive representation of a number.|

---

### Example: JavaScript Number Methods

```
// check if num1 is integer
let num1 = 12;
console.log(Number.isInteger(num1)); // true

// check if num2 is NaN
let num2 = NaN;
console.log(Number.isNaN(num2)); // true

// display up to two decimal points
let num3 = 5.1234;
console.log(num3.toFixed(2)); // 5.12
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## More on JavaScript Numbers

+ Operator With Numbers

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/online-compiler)

Numeric Operations on Numeric Strings

[](https://www.programiz.com/javascript/online-compiler)

JavaScript Precision Problems

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/online-compiler)

JavaScript BigInt

[](https://www.programiz.com/javascript/online-compiler)

[](https://caniuse.com/#feat=bigint)

JavaScript Number() Function

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/type-conversion)

Number Objects

[](https://www.programiz.com/javascript/online-compiler)

---

**Also Read:**

- [JavaScript String](https://www.programiz.com/javascript/string)
- [JavaScript Symbol](https://www.programiz.com/javascript/symbol)

- [](https://www.programiz.com/javascript/numbers#introduction)
- [](https://www.programiz.com/javascript/numbers#nan)
- [](https://www.programiz.com/javascript/numbers#infinity)
- [](https://www.programiz.com/javascript/numbers#methods)