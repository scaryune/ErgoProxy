# C++ Keywords and Identifiers

## C++ Keywords

Keywords are **predefined** words that have special meanings to the compiler. For example,

```
int money;
```

Here, `int` is a keyword that indicates money is a variable of type integer.

Here is a list of all C++ keywords. (as of C++17)

|   |   |   |   |
|---|---|---|---|
|`alignas`|`decltype`|`namespace`|`struct`|
|`alignof`|`default`|`new`|`switch`|
|`and`|`delete`|`noexcept`|`template`|
|`and_eq`|`do`|`not`|`this`|
|`asm`|`double`|`not_eq`|`thread_local`|
|`auto`|`dynamic_cast`|`nullptr`|`throw`|
|`bitand`|`else`|`operator`|`true`|
|`bitor`|`enum`|`or`|`try`|
|`bool`|`explicit`|`or_eq`|`typedef`|
|`break`|`export`|`private`|`typeid`|
|`case`|`extern`|`protected`|`typename`|
|`catch`|`false`|`public`|`union`|
|`char`|`float`|`register`|`unsigned`|
|`char16_t`|`for`|`reinterpret_cast`|`using`|
|`char32_t`|`friend`|`return`|`virtual`|
|`class`|`goto`|`short`|`void`|
|`compl`|`if`|`signed`|`volatile`|
|`const`|`inline`|`sizeof`|`wchar_t`|
|`constexpr`|`int`|`static`|`while`|
|`const_cast`|`long`|`static_assert`|`xor`|
|`continue`|`mutable`|`static_cast`|`xor_eq`|

**Note:** As C++ is a case sensitive language, all keywords must be written in lowercase.

---

## C++ Identifiers

Identifiers are the unique names given to variables, classes, functions, or other entities by the programmer. For example,

```
int money;
double accountBalance;
```

Here, money and accountBalance are identifiers.

---

### Rules for naming identifiers

- Identifiers can be composed of letters, digits, and the underscore character.
- It has no limit on name length.
- It must begin with either a letter or an underscore.
- It is case-sensitive.
- We cannot use keywords as identifiers.

We can choose any name as an identifier if we follow the above rules. However, we should give meaningful names to the identifier that makes sense.

---

### Examples of good and bad identifiers

| Invalid Identifier | Bad Identifier | Good Identifier |
| ------------------ | -------------- | --------------- |
| Total points       | T_points       | totalPoint      |
| 1list              | list_1         | list1           |
| float              | n_float        | floatNumber     |