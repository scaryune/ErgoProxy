# C++ String Class

In C++, the `string` class is used to represent a sequence of characters as an object of the class.

We can access the various `string` class functions by including the `<string>` header in our file.

```
#include <string>
```

---

## String Class Functions

The common functions that are used with the `string` class are.

|Function|Description|
|---|---|
|`find()`|Find a substring in the string.|
|`rfind()`|Find the last occurrence of a substring in the string.|
|`append()`|Append to the string.|
|`insert()`|Insert into the string.|
|`erase()`|Erase characters from the string.|
|`replace()`|Replace portions of the string.|
|`compare()`|Compare two strings.|

---

## Example 1: Find a Substring in the Given String

The `find()` function searches the string for the first occurrence of the specified substring and returns the **position of the first character of the first match**.

The `rfind()` function searches the string for the last occurrence of the specified substring and returns the **position of the first character of the last match**.

For example,

```
#include <iostream>
#include <string>
using namespace std;

int main() {

    string str = "Hello world, wonderful world!";
    cout << "String: " << str << endl;
    
    // find the first occurrence
    size_t first_occurrence = str.find("world");
    
    // find the last occurrence
    size_t last_occurrence = str.rfind("world");
    
    if (first_occurrence != string::npos) {
        cout << "First occurrence: 'world' found at position: " << first_occurrence << endl;
        cout << "Last occurrence: 'world' found at position: " << last_occurrence << endl;
    }
    else {
        cout << "'world' not found" << endl;
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

String: Hello world, wonderful world!
First occurrence: 'world' found at position: 6
Last occurrence: 'world' found at position: 23

The line `if (first_occurrence != string::npos)` checks if the variable first_occurrence contains a valid position where the substring `world` was found within the string.

- If `world` is **found** in string, first_occurrence will be set to the position of its first occurrence.
- If `world` is **not found**, it will be set to a special constant value `string::npos`, which indicates that the substring was not found in the string.

**Note**: Both functions are case-sensitive. So, if our string was `Hello World, wonderful world!`, then the `find()` function would return **23** as the first occurrence of the substring.

---

## Example 2: Append to a String

We can append a string to an existing string using the `append()` function. For example,

```
#include <iostream>
#include <string>
using namespace std;

int main() {

    string str = "Hello world,";
    cout << "Before: " << str << endl;

    //append the string
    str.append(" Have a good day!");

    cout << "After: " << str << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Before: Hello world,
After: Hello world, Have a good day!

---

## Example 3: Insert a String at a Given Position

We can insert a string at any given position using the `insert()` function. For example,

```
#include <iostream>
#include <string>
using namespace std;

int main() {

    string str = "Hello world, world!";
    cout << "Before: " << str << endl;
    
    // insert "beautiful" at the 13th index
    str.insert(13, " beautiful");

    cout << "After: " << str << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Before: Hello world, world!
After: Hello world,  beautifulworld!

Here, we have inserted the substring `beautiful` at the **13th** index of the string. Keep in mind that this doesn't add space at the end of the added string.

---

## Example 4: Erase N Characters From the Given Position

```
#include <iostream>
#include <string>
using namespace std;

int main() {

    string str = "Hello world, beautiful world!";
    cout << "Before: " << str << endl;
    
    // erase five characters starting from the seventh index
    str.erase(7, 5);

    cout << "After: " << str << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Before: Hello world, beautiful world!
After: Hello w beautiful world!

Here, we have removed five characters starting from the seventh index using the `erase()` function.

---

## Example 5: Replace N Characters Within A String

```
#include <iostream>
#include <string>
using namespace std;

int main() {

    string str = "Hello world, beautiful world!";
    cout << "Before: " << str << endl;
    
    // replace two characters with "Earth"
    // starting from the seventh index
    str.replace(6, 2, "Earth");

    cout << "After: " << str << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Before: Hello world, beautiful world!
After: Hello Earthrld, beautiful world!

Here, we have replaced the two characters (`wo`) with `Earth`. We can replace any length of string with any length of another string using the `replace()` function.

---

## Example 6: Compare Strings Alphabetically

To get the lexicographic relations between strings, we use the `compare()` function.

The `compare()` function in the C++ `string` class returns an integer that indicates the lexicographical relationship between the compared strings. It returns:

- **0** - if the compared strings are equal.
- < **0** - if the calling string is lexicographically less than the compared string.
- > **0** - if the calling string is lexicographically greater than the compared string.

For example,

```
#include <iostream>
#include <string>
using namespace std;

int main() {

    string str1 = "Hello world";
    string str2 = "Hello world";
    string str3 = "Hello";
    string str4 = "Hello world, What's Up?";
    
    cout << "String 1: " << str1 << endl;
    cout << "String 2: " << str2 << endl;
    cout << "String 3: " << str3 << endl;
    cout << "String 4: " << str4 << endl;
    
    // compare the strings
    cout <<"Comparing String 1 and String 2: "  << str1.compare(str2) << " (Equal)" <<endl;
    cout <<"Comparing String 1 and String 3: " << str1.compare(str3) << " (String 1 is Longer)" << endl;
    cout <<"Comparing String 1 and String 4: " << str1.compare(str4) <<" (String 1 is Smaller)" << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

String 1: Hello world
String 2: Hello world
String 3: Hello
String 4: Hello world, What's Up? 
Comparing String 1 and String 2: 0 (Equal)
Comparing String 1 and String 3: 6 (String 1 is Longer)
Comparing String 1 and String 4: -12 (String 1 is Smaller)

Here,

- `str1.compare(str2)` returns **0** because str1 and str2 are equal.
- `str1.compare(str3)` returns a positive number because str1 is lexicographically greater than str3 (it has more characters).
- `str1.compare(str4)` returns a negative number because str1 is lexicographically less than str4.

- [](https://www.programiz.com/cpp-programming/string-class#introduction)
- [](https://www.programiz.com/cpp-programming/string-class#example1)
- [](https://www.programiz.com/cpp-programming/string-class#example2)
- [](https://www.programiz.com/cpp-programming/string-class#example3)
- [](https://www.programiz.com/cpp-programming/string-class#example4)
- [](https://www.programiz.com/cpp-programming/string-class#example5)
- [](https://www.programiz.com/cpp-programming/string-class#example6)

[

  


](https://www.programiz.com/cpp-programming/strings "C++ String")