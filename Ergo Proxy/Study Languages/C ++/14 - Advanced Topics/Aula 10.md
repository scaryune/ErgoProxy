# C++ ostream

The C++ `ostream` class provides a set of functions and operators for writing data as output.

Before using `ostream`, we need to include the `<iostream>` header in our program.

```
#include <iostream>
```

---

## C++ Insertion Operator <<

To write data to the console using `ostream`, we can use the `cout` object with the insertion operator `<<` operator.

```
#include <iostream>
using namespace std;

int main() {

    int entered_number;

    // write the text "Hello World!" to the screen
    cout << "Hello World!";
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Hello World!

---

## C++ put() Function

The `put()` function of `ostream` is primarily used to write characters to the console. For example,

```
#include <iostream>
using namespace std;

int main() {

    char ch = 'A';

    // print a character to the console
    cout.put(ch);
    
    cout<< endl ;

    // print another character to the console
    cout.put('C'); 

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

A
C

---

## C++ write() Function

The `write()` function of `ostream` is generally used to write blocks of data into the console. For example,

```
#include <iostream>
#include <cstring>

using namespace std;

int main() {

    // create a C-string
    const char* str = "Hello, World!";

    // print the C-string
    cout.write(str, strlen(str));
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Hello, World!

Here, we have written a C-string `Hello, World` to the output stream using the `write()` function.

**Note:** We have used a C-string with the `write()` function because it doesn't work with `std::string` objects of C++.