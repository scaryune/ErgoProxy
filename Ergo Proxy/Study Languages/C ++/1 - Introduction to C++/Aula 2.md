# Your First C++ Program

In the previous tutorial, you learned how to [install C++](https://www.programiz.com/cpp-programming/getting-started) on your computer. Now, let's write a simple C++ program.

The following program displays `Hello, World!` on the screen.

```
#include <iostream>

using namespace std;

int main() {
    cout << "Hello, World!";
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Hello World!

**Note:** A `Hello World!` program includes the basic syntax of a programming language and helps beginners understand the structure before getting started. That's why it is a common practice to introduce a new language using a `Hello World!` program.

It's okay if you don’t understand how the program works right now. We will learn about it in upcoming tutorials. For now, just write the exact program and run it.

---

## Working of C++ Program

Congratulations on writing your first C++ program. Now, let's see how the program works.

```
#include <iostream>

using namespace std;

int main() {
    cout << "Hello, World!";
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

Notice the following line of code:

```
cout << "Hello, World!";
```

In the above code, the `cout <<` prints the text `Hello, World!` to the screen.

Remember these important things about `cout`:

- The text to be printed is enclosed within double quotes `""`.
- Each `cout <<` ends with a semicolon `;`.

Not following the above rules will result in errors and your code will not run successfully.

---

## Basic Structure of a C++ Program

As we have seen from the last example, a C++ program requires a lot of lines even for a simple program.

For now, just remember that every C++ program we will write will follow this structure:

```
#include <iostream>

using namespace std;

int main() {

    // your code

    return 0;
}
```

And, we will write out code inside curly braces `{}`.

Next, we will be learning about [C++ comments](https://www.programiz.com/cpp-programming/comments).