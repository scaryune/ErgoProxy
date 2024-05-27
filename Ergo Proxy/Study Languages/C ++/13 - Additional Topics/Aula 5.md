# C++ Nested Loop

A loop within another loop is called a nested loop. Let's take an example,

Suppose we want to loop through each day of a week for 3 weeks.

To achieve this, we can create a loop to iterate three times (3 weeks). And inside the loop, we can create another loop to iterate 7 times (7 days). This is how we can use nested loops.

---

## Example: Nested for Loop

```
// C++ program to display 7 days of 3 weeks

#include <iostream>
using namespace std;

int main() {
    int weeks = 3, days_in_week = 7;

    for (int i = 1; i <= weeks; ++i) {
        cout << "Week: " << i << endl;

        for (int j = 1; j <= days_in_week; ++j) {
            cout << "    Day:" << j << endl;
        }
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Week: 1
    Day:1
    Day:2
    Day:3
    ... .. ...
Week: 2
    Day:1
    Day:2
    Day:3
    ... ... ..

We can create nested loops with [while and do...while](https://www.programiz.com/cpp-programming/do-while-loop) in a similar way.

---

## Example: Displaying a Pattern

```
// C++ program to display a pattern
// with 5 rows and 3 columns

#include <iostream>
using namespace std;

int main() {

   int rows = 5;
   int columns = 3;

   for (int i = 1; i <= rows; ++i) {
      for (int j = 1; j <= columns; ++j) {
         cout << "*  ";
      }
      cout << endl;
   }

   return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

*  *  *  
*  *  *  
*  *  *  
*  *  *  
*  *  *  

In this program, the outer loop iterates from `1` to rows.

The inner loop iterates from `1` to columns. Inside the inner loop, we print the character `'*'`.

---

## break and continue Inside Nested Loops

When we use a [break statement](https://www.programiz.com/cpp-programming/break-statement) inside the inner loop, it terminates the inner loop but not the outer loop. For example,

### Example: break Inside Nested Loops

```
#include <iostream>
using namespace std;

int main() {
    int weeks = 3, days_in_week = 7;

    for (int i = 1; i <= weeks; ++i) {
        cout << "Week: " << i << endl;

        for (int j = 1; j <= days_in_week; ++j) {
            // break during the 2nd week
            if (i == 2) {
                break;
            }
            cout << "    Day:" << j << endl;
        }
    }
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Week: 1
    Day:1
    Day:2
    ... .. ...
Week: 2
Week: 3
    Day:1
    Day:2
    ... .. ...

This program does not run the inner loop when the value of i is `2` i.e. it does not print the days of the 2nd week. The outer loop that prints the weeks is unaffected.

---

Similarly, when we use a [continue statement](https://www.programiz.com/cpp-programming/continue-statement) inside the inner loop, it skips the current iteration of the inner loop only. The outer loop is unaffected. For example,

### Example: continue Inside Nested Loops

```
#include <iostream>
using namespace std;

int main() {
    int weeks = 3, days_in_week = 7;

    for (int i = 1; i <= weeks; ++i) {
        cout << "Week: " << i << endl;

        for (int j = 1; j <= days_in_week; ++j) {
            // continue if the day is an odd number
            if (j % 2 != 0) {
                continue;
            }
            cout << "    Day:" << j << endl;
        }
    }
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Week: 1
    Day:2
    Day:4
    Day:6
Week: 2
    Day:2
    Day:4
    Day:6
Week: 3
    Day:2
    Day:4
    Day:6

This program prints only those days that are even.

Whenever the days_in_week is odd, the `continue` statement skips that iteration of the inner loop.

- [](https://www.programiz.com/cpp-programming/nested-loops#introduction)
- [](https://www.programiz.com/cpp-programming/nested-loops#nested-for)
- [](https://www.programiz.com/cpp-programming/nested-loops#example-pattern)
- [](https://www.programiz.com/cpp-programming/nested-loops#break)
- [](https://www.programiz.com/cpp-programming/nested-loops#continue)

[

  


](https://www.programiz.com/cpp-programming/ranged-for-loop "C++ Ranged for Loop")