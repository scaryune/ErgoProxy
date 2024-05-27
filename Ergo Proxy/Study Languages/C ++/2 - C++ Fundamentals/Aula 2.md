# C++ Variables, Literals and Constants

In the previous tutorial you learnt about [C++ comments](https://www.programiz.com/cpp-programming/comments). Now, let's learn about variables, constants and literals in C++.

## C++ Variables

In programming, a variable is a container (storage area) to hold data.

To indicate the storage area, each variable should be given a unique name (identifier). For example,

```
int age = 14;
```

Here, age is a variable of the `int` data type, and we have assigned an integer value `14` to it.

The value of a variable can be changed, hence the name **variable**.

```
int age = 14;   // age is 14
age = 17;       // age is 17
```

Visit this page to learn more about [different types of data a variable can store](https://www.programiz.com/cpp-programming/data-types).

Rules for naming a variable

4. [](https://www.programiz.com/cpp-programming/keywords-identifiers)

---

## C++ Constants

In C++, we can create variables whose value cannot be changed. For that, we use the `const` keyword. Here's an example:

```
const int LIGHT_SPEED = 299792458;
LIGHT_SPEED = 2500 // Error! LIGHT_SPEED is a constant.
```

Here, we have used the keyword `const` to declare a constant named `LIGHT_SPEED`. If we try to change the value of `LIGHT_SPEED`, we will get an error.

A constant can also be created using the `#define` preprocessor directive. We will learn about it in detail in the [C++ Macros tutorial](https://www.programiz.com/cpp-programming/preprocessor-macros).

---

## C++ Literals

Literals are data used for representing fixed values. They can be used directly in the code. For example: `1`, `2.5`, `'c'` etc.

Here, `1`, `2.5` and `'c'` are literals. Why? You cannot assign different values to these terms.

---

### 1. Integers

An integer is a numeric literal(associated with numbers) without any fractional or exponential part. There are three types of integer literals in C++ programming:

- decimal (base 10)
- octal (base 8)
- hexadecimal (base 16)

For example:

Decimal: 0, -9, 22 etc

Octal: 021, 077, 033 etc

Hexadecimal: 0x7f, 0x2a, 0x521 etc

In C++ programming, octal starts with a `0,` and hexadecimal starts with a `0x`.

---

### 2. Floating-point Literals

A floating-point literal is a numeric literal that has either a fractional form or an exponent form. For example:

`-2.0`

`0.0000234`

`-0.22E-5`

**Note**: E-5 = 10-5

---

### 3. Characters

A character literal is created by enclosing a single character inside single quotation marks. For example: 'a', 'm', 'F', '2', '}' etc.

---

### 4. String Literals

A string literal is a sequence of characters enclosed in double-quote marks. For example:

|   |   |
|---|---|
|`"good"`|string constant|
|`""`|null string constant|
|`" "`|string constant of six white space|
|`"x"`|string constant having a single character|
|`"Earth is round\n"`|prints string with a newline|

We will learn about strings in detail in the [C++ string tutorial](https://www.programiz.com/cpp-programming/strings).

- [](https://www.programiz.com/cpp-programming/variables-literals#variables)
- [](https://www.programiz.com/cpp-programming/variables-literals#constants)
- [](https://www.programiz.com/cpp-programming/variables-literals#literals)
- [](https://www.programiz.com/cpp-programming/variables-literals#integers)
- [](https://www.programiz.com/cpp-programming/variables-literals#floats)
- [](https://www.programiz.com/cpp-programming/variables-literals#characters)
- [](https://www.programiz.com/cpp-programming/variables-literals#string)

[

  


](https://www.programiz.com/cpp-programming/keywords-identifiers "C++ Keywords and Identifiers")