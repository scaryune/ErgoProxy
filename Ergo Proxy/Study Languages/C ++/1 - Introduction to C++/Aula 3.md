# C++ Comments

In the previous tutorial you learned how to [](https://www.programiz.com/r/getting-started)write your first [C++ program](http://cpp-programming/first-program). Now, let's learn about C++ comments.

**Tip**: We are introducing comments early in this tutorial series because, from now on, we will be using them to explain our code.

Comments are hints that we add to our code, making it easier to read and understand. In C++, comments start with `//`.

For example,

```
#include <iostream>
using namespace std;

int main() {
    // print Hello World to the screen
    cout << "Hello World";

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Hello World

Here, `// print Hello World to the screen` is a comment.

The C++ compiler ignores everything after the `//` symbol.

**Note**: The purpose of this tutorial is to help you understand comments, so you can ignore other concepts used in the program. We will learn about them in later tutorials.

---

## Single Line Comments

In C++, a single line comment starts with a **double slash** **(**`//`**)** symbol. For example,

```
#include <iostream>

int main() {
    // declaring a variable
    int a;

    // initializing the variable 'a' with the value 2
    a = 2;
    
    // print the value of 'a'
    std::cout << "Value of a is: "<< a;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Value of a is: 2

Here, we have used three single-line comments:

- `// declaring a variable`
- `// initializing the variable 'a' with the value 2`
- `// print the value of 'a'`

Single-line comments start with `//` and extend up to the end of the line. We can also use single line comment along with the code like this:

```
int a;    // declaring a variable
```

Here, code before `//` are executed and code after `//` are ignored by the compiler.

---

## Multi-line comments

In C++, any line between `/*` and `*/` is also a comment. For example,

```
#include <iostream>

int main() {
    /* declaring a variable
    to store salary to employees
    */
    int salary = 2000;
    
    // print the salary
    std::cout << "Salary: "<< salary;

    return 0;
}
```

Here, everything between `/*` and `*/` is ignored by the compiler.This syntax can be used to write both single-line and multi-line comments.

**Note**: Remember the keyboard shortcut to use comments:

- Single Line comment: ctrl + / (windows) and cmd + / (mac)
- Multi line comment: ctrl + shift + / (windows) and cmd + shift + / (mac)

---

## Using Comments for Debugging

Comments are useful for debugging a code. For example,

```
#include <iostream>
using namespace std;
int main() {
   cout << "some code";
   cout << ''error code;
   cout << "some other code";

   return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

When you encounter an error in your program, you can use comments to temporarily stop that part of the code from running. This can help you figure out what's wrong without removing the code. For example;

```
#include <iostream>
using namespace std;
int main() {
   cout << "some code";
   // cout << ''error code;
   cout << "some other code";

   return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

---

## Why use Comments?

We should use comments for the following reasons:

- Comments make our code readable for future reference.
- Comments are used for debugging purposes.
- We can use comments for code collaboration as it helps peer developers to understand our code.

**Note**: Comments are not and should not be used as a substitute to explain poorly written code. Always try to write clean, understandable code, and then use comments as an addition.

In most cases, always use comments to explain 'why' rather than 'how' and you are good to go.

Next, we will learn about [C++ variables, constants and literals](https://www.programiz.com/cpp-programming/variables-literals).

- [](https://www.programiz.com/cpp-programming/comments#introduction)
- [](https://www.programiz.com/cpp-programming/comments#single-line)
- [](https://www.programiz.com/cpp-programming/comments#multi-line)
- [](https://www.programiz.com/cpp-programming/comments#debugging)
- [](https://www.programiz.com/cpp-programming/comments#why)

[

  


](https://www.programiz.com/cpp-programming/first-program "Your First C++ Program")