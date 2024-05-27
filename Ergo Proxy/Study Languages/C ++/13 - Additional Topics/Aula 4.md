# C++ Ranged for Loop

C++11 introduced the ranged `for` loop. This `for` loop is specifically used with collections such as **arrays** and **vectors**.

For example,

```
// initialize an int array
int num[3] = {1, 2, 3};

// use of ranged for loop
for (int var : num) {
    // code
}
```

Here, the ranged `for` loop iterates the array num from beginning to end. The `int` variable var stores the value of the array element in each iteration.

Its syntax is,

```
for (rangeDeclaration : rangeExpression) {
    // code
}
```

In the above example,

- **rangeDeclaration** - `int var`
- **rangeExpression** - num

![Working of Ranged for Loop in C++](https://cdn.programiz.com/sites/tutorial2program/files/cpp-ranged-for-loop.png "C++ Working of Ranged for Loop")

Working of ranged for loop in C++

---

### Example 1: Ranged for Loop Using Array

```
#include <iostream>
using namespace std;

int main() {

    // initialize array  
    int numArray[] = {1, 2, 3, 4, 5};

    // use of ranged for loop to print array elements  
    for (int n : numArray) {
        cout << n << " ";
    }
  
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

1 2 3 4 5

In this example, we declared and initialized an `int` array named numArray. Here, we used the ranged `for` loop to print out the elements of numArray.

- **first iteration** - n takes the value of the first member of the array, which is `1`
- **second iteration** - n takes the value of `2` and is then printed
- ...and so on.

**Note:** The ranged for loop automatically iterates the array from its beginning to its end. We do not need to specify the number of iterations in the loop.

---

### Example 2: C++ Ranged for Loop Using Vector

```
#include <iostream>
#include <vector>
using namespace std;

int main() {

    // declare and initialize vector  
    vector<int> num_vector = {1, 2, 3, 4, 5};

    // print vector elements  
    for (int n : num_vector) {
        cout << n << " ";
    }
  
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

1 2 3 4 5

---

### Example 3: Declare Collection inside the Loop

```
#include <iostream>

using namespace std;

int main() {

    // define the collection in the loop itself
    for (int n : {1, 2, 3, 4, 5}) {
        cout << n << " ";
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

1 2 3 4 5

Here, we have declared the collection within the loop itself i.e.

```
rangeExpression = {1, 2, 3, 4, 5}
```

This is also a valid way of using the ranged `for` loop, and it works in the same way as when we use an actual array or vector.

---

## C++ Ranged for Loop Best Practices

In the above examples, we have declared a variable in the `for` loop to store each element of the collection in each iteration.

```
int num[3] = {1, 2, 3};

// copy elements of num to var
for (int var : num) {
    // code
}
```

However, it's better to write the **ranged based for loop** like this:

```
// access memory location of elements of num
for (int &var : num) {
    // code
}
```

Notice the use of `&` before var. Here,

- `int var : num` - Copies each element of num to the var variable in each iteration. This is not good for computer memory.
- `int &var : num` - Does not copy each element of num to var. Instead, accesses the elements of num directly from num itself. This is more efficient.

**Note:** The `&` operator is known as the reference operator. We will learn more about it in [C++ pointers](https://www.programiz.com/cpp-programming/pointers).

![Working of Address Pointing in Ranged for Loop in C++](https://cdn.programiz.com/sites/tutorial2program/files/cpp-ranged-for-loop-point-address.png "C++ Working of Address Pointing in Ranged for Loop")

Working of address pointing in C++ ranged for loop

**Note:** If we are not modifying the array/vector/collection within the loop, it is better to use the `const` keyword in range declaration.

```
// collection is not modified in the loop
for (const int &var : num) {
    // code
}
```

- [](https://www.programiz.com/cpp-programming/ranged-for-loop#introduction)
- [](https://www.programiz.com/cpp-programming/ranged-for-loop#example1)
- [](https://www.programiz.com/cpp-programming/ranged-for-loop#example2)
- [](https://www.programiz.com/cpp-programming/ranged-for-loop#example3)
- [](https://www.programiz.com/cpp-programming/ranged-for-loop#best-practices)

[

  


](https://www.programiz.com/cpp-programming/file-handling "C++ File Handling")