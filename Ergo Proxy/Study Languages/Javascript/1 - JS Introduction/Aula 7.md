# JavaScript Type Conversion

In programming, type conversion is the process of converting data of one [type](https://www.programiz.com/javascript/data-types) to another. For example, converting [string](https://www.programiz.com/javascript/string) data to [number](https://www.programiz.com/javascript/numbers).

There are two types of type conversion in JavaScript:

- **Implicit Conversion** - Automatic type conversion.
- **Explicit Conversion** - Manual type conversion.

---

## JavaScript Implicit Conversion

In certain situations, JavaScript automatically converts data of one type to another (to the right type). This is known as implicit conversion. For example,

```
// numeric string used with + gives string type
let result;

// convert number to string
result = "3" + 2; 
console.log(result, "-", typeof(result));

result = "3" + true; 
console.log(result, "-", typeof(result));

result = "3" + null; 
console.log(result, "-", typeof(result));
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

32 - string
3true - string
3null - string

In this example, we performed implicit type conversion using the `+` [operator](https://www.programiz.com/javascript/operators) with a string and another data type.

Here,

- `"3" + 2` - Converts the number **2** to string and joins it to `"3"`, resulting in the string `"32"`.
- `"3" + true` - Converts the [boolean](https://www.programiz.com/javascript/booleans) `true` to string and joins it to `"3"`, resulting in the string `"3true"`.
- `"3" + null` - Converts [null](https://www.programiz.com/javascript/null-undefined) to string and joins it to `"3"`, resulting in the string `"3null"`.

**Note**: The [typeof](https://www.programiz.com/javascript/typeof) operator gives the data type of the variable.

---

## JavaScript Explicit Conversion

In explicit type conversion, you manually convert one type of data into another using [built-in functions](https://www.programiz.com/javascript/library). For example,

```
let result;

// convert string to number
result = Number("5");
console.log(result, "-", typeof(result));

// convert boolean to string
result = String(true);
console.log(result, "-", typeof(result));

// convert number to boolean
result = Boolean(0);
console.log(result, "-", typeof(result));
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

5 - number
true - string
false - boolean

Here,

- [Number("5")](https://www.programiz.com/javascript/numbers#function) changes the string `"5"` into the number **5**.
- [String(true)](https://www.programiz.com/javascript/string#function) turns the boolean `true` into the string `"true"`.
- [Boolean(0)](https://www.programiz.com/javascript/booleans#function) converts the number **0** to the boolean `false` because **0** is considered a **falsy** value in JavaScript.

---

## More on JavaScript Type Conversion

Implicit Conversion to Number

[](https://www.programiz.com/javascript/online-compiler)

JavaScript Type Conversion Table

|||||
|---|---|---|---|
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||

[](https://www.programiz.com/javascript/object)[](https://www.programiz.com/javascript/array)

Rules for Type Conversion

---

**Also Read:**

- [JavaScript Dates to Numbers](https://www.programiz.com/javascript/examples/convert-date-number)
- [JavaScript Dates to Strings](https://www.programiz.com/javascript/examples/display-current-date)