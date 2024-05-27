# C++ Algorithm

In C++, the Standard Template Library (STL) provides a rich set of algorithms that can be utilized to perform operations like sorting, searching, and manipulating elements of containers (like arrays, vectors, etc.).

These algorithms can be accessed using the `<algorithm>` header.

```
#include <algorithm>
```

---

## Commonly Used Algorithms

The `<algorithm>` library in C++ offers many useful functions. Some of the most commonly used functions are given below.

|Functions|Description|
|---|---|
|`sort()`|Sort the elements of the container.|
|`copy()`|Copy elements within a given range.|
|`move()`|Move the given range of elements.|
|`swap()`|Exchange values of two objects.|
|`merge()`|Merge sorted ranges.|
|`replace()`|Replace the value of an element.|
|`remove()`|Remove an element.|

**Note:** We will be using vectors to understand the working of all these functions. However, these functions work on other STL containers as well.

---

## Example 1: Sort a Vector in Ascending Order

To sort a vector in ascending order, we can use the `sort()` function. Its syntax is:

```
sort( first, last);
```

Here,

- first - iterator specifying the beginning of the sorting range (inclusive)
- last - iterator specifying the end of the sorting range (exclusive)

```
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

int main() {

    vector<int> vec = {4, 2, 3, 1, 5};

    //sort the elements of the vector
    sort(vec.begin(), vec.end());

    for(int num : vec) {
        cout << num << " ";
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

1 2 3 4 5 

Here, we have set the `sort()` range from the beginning of our vector using `vec.begin()` to the end of the vector using `vec.end()`.

This sorts our vector in ascending order.

---

## Example 2: Copy Vector Elements

We use the `copy()` function to copy a given range of elements from one vector to another. Its syntax is:

```
copy(first, last, result);
```

Here,

- first - iterator specifying the beginning of the range to copy (inclusive)
- last - iterator specifying the end of the range to copy (exclusive)
- result - iterator specifying the position in the destination vector where the elements will be copied

For example,

```
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

int main() {

    vector<int> source = {1, 2, 3, 4, 5};

    // create destination vector of size 5
    vector<int> destination(5);
    
    // copy the contents of source to destination
    copy(source.begin(), source.end(), destination.begin());

    // print elements of destination vector
    for(int num : destination) {
        cout << num << " ";
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

1 2 3 4 5 

Here, we have created the source with five elements and an empty vector destination of size **5**.

We then used the `copy()` function to copy the contents of source to destination.

---

## Example 3: Move Vector Elements

We can use the `move()` function to move elements from one vector to another. Its syntax is:

```
move(first, last, result);
```

For example,

```
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

int main() {

    vector<string> source = {"apple", "banana", "cherry"};
    vector<string> destination(3);

    cout << "Before move:" << endl;
    cout << "source: ";

    for(const string& str : source) {
        cout << str << " ";
    }
    cout << endl;

    cout << "destination: ";
    for(const string& str : destination) {
        cout << str << " ";
    }
    cout << endl;

    // perform the move operation
    move(source.begin(), source.end(), destination.begin());

    cout << "After move:" << endl;
    cout << "source: ";
    for(const string& str : source) {
        cout << str << " ";
    }
    cout << endl;

    cout << "destination: ";
    for(const string& str : destination) {
        cout << str << " ";
    }
    cout << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Before move:
source: apple banana cherry 
destination:    
After move:
source:    
destination: apple banana cherry 

---

## Example 4: Swap the Contents of Two Vectors

We can swap the contents of two STL vectors using the `swap()` function. Its syntax is:

```
swap(x, y);
```

Here, x and y are containers whose contents need to be swapped.

For example,

```
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

int main() {

    vector<int> vec1 = {1, 2, 3};
    vector<int> vec2 = {4, 5, 6};

    // print vec1 and vec2 before swap
    cout << "Before swap:" << endl;
    cout << "vec1: ";
    for(int num : vec1) {
        cout << num << " ";
    }
    cout << endl;

    cout << "vec2: ";
    for(int num : vec2) {
        cout << num << " ";
    }
    cout << endl;

    // swap vec1 and vec2
    swap(vec1, vec2);

    // print vec1 and vec2 after swap
    cout << "After swap:" << endl;
    cout << "vec1: ";
    for(int num : vec1) {
        cout << num << " ";
    }
    cout << endl;

    cout << "vec2: ";
    for(int num : vec2) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Before swap:
vec1: 1 2 3 
vec2: 4 5 6 
After swap:
vec1: 4 5 6 
vec2: 1 2 3 

---

## Example 5: Merge Two Vectors

We can merge two STL containers using the `merge()` function. It's syntax is:

```
merge(first1, last1, first2,  last2, result);
```

Here,

- first1, last1 - iterators specifying the first input range.
- first2, last2 - iterators specifying the second input range.
- result - iterator specifying the beginning of the destination range.

For example,

```
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

int main() {

    vector<int> vec1 = {1, 3, 5};
    vector<int> vec2 = {2, 4, 6};
    vector<int> result(6);

    // vec1 and vec2 before merge
    cout << "Before merge:" << endl;
    cout << "vec1: ";
    for(int num : vec1) {
        cout << num << " ";
    }
    cout << endl;

    cout << "vec2: ";
    for(int num : vec2) {
        cout << num << " ";
    }
    cout << endl;

    // perform merge operation
    merge(vec1.begin(), vec1.end(), vec2.begin(), vec2.end(), result.begin());

    // output result after merge
    cout << "After merge:" << endl;
    cout << "result: ";
    for(int num : result) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Before merge:
vec1: 1 3 5 
vec2: 2 4 6 
After merge:
result: 1 2 3 4 5 6 

Notice that the merged vector is returned in sorted order.

---

## Example 6: Replace Vector Element

We can replace all occurrences of an element in an STL container with another element using `replace()` function. It's syntax is:

```
replace(first, last, old_value, new_value);
```

Here,

- first, last - iterators specifying the range to transform.
- old_value - value to be replaced.
- new_value - replacement value.

For example,

```
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

int main() {

    vector<int> vec = {4, 2, 3, 2, 5};

    // display the vector before replacement
    cout << "Before: ";
    for(int num : vec) {
        cout << num << " ";
    }
    cout << endl;

    // replace 2 with 99
    replace(vec.begin(), vec.end(), 2, 99);

    // display the vector after replacement
    cout << "After: ";
    for(int num : vec) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Before: 4 2 3 2 5 
After: 4 99 3 99 5 

Here we have replaced all the occurrences of **2** with **99**.

---

## Example 7: Delete a Value From the Given Range

We can remove the first occurrence of a value from a given range using the `remove()` function. It's syntax is:

```
remove(first, last, val);
```

Here,

- first, last - iterators specifying the range to transform
- val - value to be removed

For example,

```
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

int main() {

    vector<int> vec = {4, 2, 3, 2, 5};

    // print the vector before deletion
    cout << "Before deletion: ";
    for(int num : vec) {
        cout << num << " ";
    }
    cout << endl;

    // remove the first occurrence of 2
    remove(vec.begin(), vec.end(), 2);

    // print the vector after deletion
    cout << "After deletion: ";
    for(int num : vec) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Before deletion: 4 2 3 2 5 
After deletion: 4 3 5 2 5

- [](https://www.programiz.com/cpp-programming/algorithm#introduction)
- [](https://www.programiz.com/cpp-programming/algorithm#example1)
- [](https://www.programiz.com/cpp-programming/algorithm#example2)
- [](https://www.programiz.com/cpp-programming/algorithm#example3)
- [](https://www.programiz.com/cpp-programming/algorithm#example4)
- [](https://www.programiz.com/cpp-programming/algorithm#example5)
- [](https://www.programiz.com/cpp-programming/algorithm#example6)
- [](https://www.programiz.com/cpp-programming/algorithm#example7)

[

Previous



](https://www.programiz.com/cpp-programming/iterators "C++ Iterators")