# C++ istream

The C++ `istream` class provides a set of functions and operators for reading data from various input sources.

Before using the `istream` class, we need to include the `<iostream>` header in our program.

```
#include <iostream>
```

---

## Example 1: Reading Data From the Console

To read data from the console using `istream`, you can use the `cin` object with the extraction operator `>>`. Here's an example:

```
#include <iostream>
using namespace std;

int main() {

    int entered_number;

    cout << "Enter an integer: ";

    // read data from the console
    cin >> entered_number;
    
    cout << "You entered: " << entered_number << endl;
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Enter an integer: 3
You entered: 3

In this example, `cin` represents the standard input stream that reads data from the keyboard. We use the `>>` operator to extract the user's input and store it in the number variable.

---

## The get() Function

The `get()` function of the `istream` class is primarily used for reading individual characters from the input stream.

**Key Characteristics**

- **Reading Characters**: It reads the next character from the input stream and advances the stream's internal position indicator.

- **Single Character**: Unlike the `>>` operator, `get()` reads characters as they are, including spaces, tabs, and newline characters.

- **Character Extraction**: You can use it to extract characters into variables of type `char` or to store them in character arrays (C-strings).

- **Delimiter Control**: It allows you to specify a delimiter character as an optional parameter. When you specify a delimiter, `get()` stops reading characters when it encounters that delimiter. This is useful for reading words or lines.

---

### Example 2: C++ get() Function

```
#include <iostream>
using namespace std; 

int main() {

    char ch;
    
    cout << "Enter a sentence: ";

    // read the character one by one
    // until a new line is encountered
    while (cin.get(ch) && ch != '\n') {
        cout << ch;
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Enter a sentence: Hello World
Hello World

Here, we have used `cin.get()` to read a single character from the user.

Notice this part of the code:

```
while (cin.get(ch) && ch != '\n') {
    cout << ch;
}
```

The loop reads characters one by one from standard input until a newline character is encountered. In each iteration, it prints the character immediately as it is read.

---

## C++ getline() Function

The `getline()` function in `istream` is used to read a line of text from the specified input stream (such as `cin` for standard input).

**Key Characteristics**

- **Reading Lines**: Unlike the`get()` function, `getline()` reads entire lines of text, up to a specified delimiter or the end of the line.

- **Delimiter Control**: You can specify a delimiter character like one that indicates the end of a line. This allows you to read multiple lines of text sequentially.

- **Buffer Size**: It accepts an optional parameter to specify the maximum number of characters to read, preventing buffer overflows and handling long lines gracefully.

---

### Example 3: C++ getline() Function

```
#include <iostream>
using namespace std; 

int main() {

    string line;
    
    cout << "Enter a line of text: ";

    // read a line of input from user
    getline(cin, line);
    
    cout << "You entered: " << line << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Enter a line of text: Hello
You entered: Hello

---

## C++ ignore() Function

The `ignore()` function is used to skip a given length of characters in the input stream.

```
#include <iostream>
using namespace std;

int main() {

    cout << "Enter a line of text: ";

    char ch;

    // ignore the next 5 characters from standard input
    cin.ignore(5);

    // read the sixth character and print the value
    if (cin.get(ch)) {
        cout << "Next character after ignoring 5 characters: " << ch << endl;
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Enter a line of text: 12345678
Next character after ignoring 5 characters: 6

Here, `cin.ignore(5);` is instructing the input stream to ignore the next five characters that are entered by the user.

After this, the `if` condition `cin.get(ch)` attempts to read the next character from the input stream after the previous five have been ignored. If successful, it stores them in the ch variable.

- [](https://www.programiz.com/cpp-programming/istream#introduction)
- [](https://www.programiz.com/cpp-programming/istream#example1)
- [](https://www.programiz.com/cpp-programming/istream#get-function)
- [](https://www.programiz.com/cpp-programming/istream#getline-function)
- [](https://www.programiz.com/cpp-programming/istream#ignore-function)