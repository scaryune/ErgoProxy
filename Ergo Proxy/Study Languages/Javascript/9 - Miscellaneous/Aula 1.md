# JavaScript and JSON

JSON stands for Javascript Object Notation. JSON is a text-based data format that is used to store and transfer data. For example,

```
// JSON syntax
{
    "name": "John",
    "age": 22,
    "gender": "male",

}
```

In JSON, the data are in **key/value** pairs separated by a comma `,`.

JSON was derived from JavaScript. So, the JSON syntax resembles JavaScript object literal syntax. However, the JSON format can be accessed and be created by other programming languages too.

**Note**: [JavaScript Objects](https://www.programiz.com/javascript/object) and JSON are not the same. You will learn about their differences later in this tutorial.

---

## JSON Data

JSON data consists of **key/value** pairs similar to JavaScript object properties. The key and values are written in double quotes separated by a colon `:`. For example,

```
// JSON data
"name": "John"
```

**Note**: JSON data requires double quotes for the key.

---

## JSON Object

The JSON object is written inside curly braces `{ }`. JSON objects can contain multiple **key/value** pairs. For example,

```
// JSON object
{ "name": "John", "age": 22 }
```

---

## JSON Array

JSON array is written inside square brackets `[ ]`. For example,

```
// JSON array
[ "apple", "mango", "banana"]

// JSON array containing objects
[
    { "name": "John", "age": 22 },
    { "name": "Peter", "age": 20 }.
    { "name": "Mark", "age": 23 }
]
```

**Note**: JSON data can contain objects and [arrays](https://www.programiz.com/javascript/array). However, unlike JavaScript objects, JSON data cannot contain [functions](https://www.programiz.com/javascript/function) as values.

---

## Accessing JSON Data

You can access JSON data using the dot notation. For example,

```
// JSON object
const data = {
    "name": "John",
    "age": 22,
    "hobby": {
	"reading" : true,
	"gaming" : false,
	"sport" : "football"
    },
    "class" : ["JavaScript", "HTML", "CSS"]
}

// accessing JSON object
console.log(data.name); // John
console.log(data.hobby); // { gaming: false, reading: true, sport: "football"}

console.log(data.hobby.sport); // football
console.log(data.class[1]); // HTML
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

We use the `.` notation to access JSON data. Its syntax is: `variableName.key`

You can also use square bracket syntax `[]` to access JSON data. For example,

```
// JSON object
const data = {
    "name": "John",
    "age": 22
}

// accessing JSON object
console.log(data["name"]); // John
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## JavaScript Objects VS JSON

Though the syntax of JSON is similar to the JavaScript object, JSON is different from JavaScript objects.

|JSON|JavaScript Object|
|---|---|
|The key in key/value pair should be in double quotes.|The key in key/value pair can be without double quotes.|
|JSON cannot contain functions.|JavaScript objects can contain functions.|
|JSON can be created and used by other programming languages.|JavaScript objects can only be used in JavaScript.|

---

## Converting JSON to JavaScript Object

You can convert JSON data to a JavaScript object using the built-in `JSON.parse()` function. For example,

```
// json object
const jsonData = '{ "name": "John", "age": 22 }';

// converting to JavaScript object
const obj = JSON.parse(jsonData);

// accessing the data
console.log(obj.name); // John
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## Converting JavaScript Object to JSON

You can also convert JavaScript objects to JSON format using the JavaScript built-in `JSON.stringify()` function. For example,

```
// JavaScript object
const jsonData = { "name": "John", "age": 22 };

// converting to JSON
const obj = JSON.stringify(jsonData);

// accessing the data
console.log(obj); // "{"name":"John","age":22}"
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

---

## Use of JSON

JSON is the most commonly used format for transmitting data (data interchange) from a server to a client and vice-versa. JSON data are very easy to parse and use. It is fast to access and manipulate JSON data as they only contain texts.

JSON is language independent. You can create and use JSON in other programming languages too.

---

**Also Read:**

- [JavaScript Program to Convert Objects to Strings](https://www.programiz.com/javascript/examples/convert-object-string)