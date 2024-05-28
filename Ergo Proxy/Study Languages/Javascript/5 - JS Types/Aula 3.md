# JavaScript String

The JavaScript string is a primitive [data type](https://www.programiz.com/javascript/data-types) that represents textual data. For example,

```
let name = "John";
```

### Create JavaScript Strings

In JavaScript, we create strings by surrounding them with quotes or backticks.

|   |   |
|---|---|
|Single Quotes|`'Hello'`|
|Double Quotes|`"Hello"`|
|Backticks|`` `Hello` ``|

Single quotes and double quotes are practically the same, and you can use either of the two.

Backticks are generally used when you need to insert variables or expressions into a string. This is done by wrapping variables or expressions with `${variable or expression}`. For example,

```
// strings example
let name1 = 'Peter';
let name2 = "Jack";
let result = `The names are ${name1} and ${name2}`;

console.log(result);

// Output: The names are Peter and Jack
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Note:** In JavaScript, strings enclosed by backticks `` ` ` `` are called [template literals](https://www.programiz.com/javascript/template-literal).

---

## Access String Characters

You can access the characters in a string in two ways:

**1. Using Indexes**

One way is to treat strings as an array and access the character at the specified index. For example,

```
let message = "hello";

// use index 1 to access
// 2nd character of message
console.log(message[1]);  // e
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, the code `message[1]` gives us the character at index **1** of the message string, i.e., its second character.

**2. Using the charAt() Method**

Another way is to supply the position of the character to the `charAt()` method. For example,

```
let message = "hello";

// use charAt(1) to get the
// 2nd character of message
console.log(message.charAt(1));  // e
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

Here, the code `message.charAt(1)` gives us the character at index **1** of the message string.

---

## Features of JavaScript Strings

JavaScript strings have some interesting features. The most important of these features are:

**1. JavaScript Strings are Immutable**

In JavaScript, the characters of a string cannot be changed. For example,

```
let message = "hello";
message[0] = "H";
console.log(message);  // hello
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

In the above example, we tried changing the first character of message using the code:

```
message[0] = "H";
```

However, this operation failed due to the immutable nature of JavaScript strings.

That being said, you can successfully assign a new value to the string variable. For example,

```
let message = "hello";
message = "Hello";
console.log(message);  // Hello
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**2. JavaScript Strings are Case-Sensitive**

In JavaScript., the lowercase and uppercase letters are treated as different values. For example,

```
let value1 = "a";
let value2 = "A"
console.log(value1 == value2);  // false
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

As you can see, `a` and `A` are treated as different values.

---

## JavaScript String Methods

|Method|Description|
|---|---|
|[charAt()](https://www.programiz.com/javascript/library/string/charat)|Returns the character at the specified index.|
|[concat()](https://www.programiz.com/javascript/library/string/concat)|Joins two or more strings.|
|[replace()](https://www.programiz.com/javascript/library/string/replace)|Replace a string with another string.|
|[split()](https://www.programiz.com/javascript/library/string/split)|Converts the string to an array of strings.|
|substr()|Returns a part of a string by taking the starting position and length of the substring.|
|[substring()](https://www.programiz.com/javascript/library/string/substring)|Returns a part of the string from the specified start index (inclusive) to the end index (exclusive).|
|[slice()](https://www.programiz.com/javascript/library/string/slice)|Returns a part of the string from the specified start index (inclusive) to the end index (exclusive).|
|[toLowerCase()](https://www.programiz.com/javascript/library/string/tolowercase)|Returns the passed string in lowercase.|
|[toUpperCase()](https://www.programiz.com/javascript/library/string/touppercase)|Returns the passed string in uppercase.|
|[trim()](https://www.programiz.com/javascript/library/string/trim)|Removes whitespace from the strings.|
|[includes()](https://www.programiz.com/javascript/library/string/includes)|Searches for a string and returns a boolean value.|
|[search()](https://www.programiz.com/javascript/library/string/search)|Searches for a string and returns the position of a match.|

To learn more, visit [JavaScript String methods](https://www.programiz.com/javascript/library/string).

---

### Example: JavaScript String Methods

```
let text1 = "hello";
let text2 = "world";
let text3 = "     JavaScript    ";

// concatenate two strings
let result1 = text1.concat(' ', text2);
console.log(result1);  // hello world

// convert the text to uppercase
let result2 = text1.toUpperCase();
console.log(result2);  // HELLO

// remove whitespace from the string
let result3 = text3.trim();
console.log(result3);  // JavaScript

// convert the string to an array
let result4 = text1.split();
console.log(result4);  // [ 'hello' ]

// slice the string
let result5= text1.slice(1, 3);
console.log(result5);  // el
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

hello world
HELLO
JavaScript
[ 'hello' ]
el

---

## More on JavaScript Strings

Get String Length

[](https://www.programiz.com/javascript/library/string/length)

[](https://www.programiz.com/javascript/online-compiler)

Insert a quote inside another quote.

JavaScript String Objects

[](https://www.programiz.com/javascript/object)

[](https://www.programiz.com/javascript/online-compiler)

Convert to String

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/type-conversion)

JavaScript Escape Characters

[](https://www.programiz.com/javascript/online-compiler)

|||
|---|---|
|||
|||
|||
|||
|||
|||
|||
|||

JavaScript Multiline Strings

[](https://www.programiz.com/javascript/online-compiler)

[](https://www.programiz.com/javascript/online-compiler)

---

**Also Read:**

- [JavaScript Number](https://www.programiz.com/javascript/numbers)