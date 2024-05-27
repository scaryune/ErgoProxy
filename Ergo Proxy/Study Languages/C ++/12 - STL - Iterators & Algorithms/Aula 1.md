# C++ Iterators

An iterator is a pointer-like object representing an element's position in a container. It is used to iterate over elements in a container.

Suppose we have a vector named nums of size **4**. Then, `begin()` and `end()` are member functions that return iterators pointing to the beginning and end of the vector respectively.

- `nums.begin()` points to the first element in the vector i.e **0th** index
- `nums.begin() + i` points to the element at the **ith** index.
- `nums.end()` points to one element past the final element in the vector

![begin() and end() iterators identify the beginning and the end of the container.](https://www.programiz.com/sites/tutorial2program/files/vector-iterator.png "Vector Iterators")

Vector Iterators

**Note:** C++ STL container provides iterators so that STL algorithms can be applied independently of the type of container used.

---

## Defining Iterators

We can define an iterator by using the following syntax:

```
// create a vector iterator
vector<int>::iterator vec_itr;

// create a map iterator
map<char, int>::iterator map_itr;
```

Here, we have created the iterators vec_itr and map_itr in order to traverse across elements in a vector or a map.

Always remember that we cannot use iterators with containers with mismatching data types. For example,

```
// create vector of integer type
vector<int> num {1, 2, 3};

// Error: itr can only be used with integer vectors
vector<double>::iterator itr = num.begin();
```

**Note:** We can use the `auto` keyword (C++ 11 onwards) to deduce the type of the iterator during initialization.

For example,

```
vector<string>::iterator itr = languages.begin();
```

Can be written as:

```
auto itr = languages.begin();
```

---

## Example 1: C++ Iterators

```
#include <iostream>
#include<vector>
using namespace std;

int main() {

    vector <string> languages = {"Python", "C++", "Java"};

    // create an iterator to a string vector
    vector<string>::iterator itr;

    // iterate over all elements
    for (itr = languages.begin(); itr != languages.end(); itr++) {
        cout << *itr << ", ";
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Python, C++, Java,

In the above example, we have used an iterator itr to iterate over a vector named languages.

Here,

- `itr = languages.begin()` - assigns the iterator pointing to the first vector element to itr

- `itr != languages.end()` - checks whether itr has reached the end of the vector

- `itr++` - increments itr to the next position

- `*itr` - returns the vector element at the itr position

---

## Iterator Fundamental Operations

Some fundamental operations that can be performed on iterators are shown in the table below.

|Operations|Description|
|---|---|
|`*itr`|returns the element at the current position|
|`itr->m`|returns the member value m of the object pointed by the iterator and is equivalent to `(*itr).m`|
|`++itr`|moves iterator to the next position|
|`-–itr`|moves iterator to the previous position|
|`itr + i`|moves iterator by `i` positions|
|`itr1 == itr2`|returns `true` if the positions pointed by the iterators are the same|
|`itr1 != itr2`|returns `true` if the positions pointed by the iterators are not the same|
|`itr = itr1`|assigns the position pointed by itr1 to the itr iterator|

**Note:** Not all operations listed above can be performed on all types of iterators. We shall discuss this further after we learn about different types of iterators.

---

## Iterator Types

The C++ standard template library provides five types of iterators. They are:

- Input Iterator
- Output Iterator
- Forward Iterator
- Bidirectional Iterator
- Random-access-iterator

![Input Iterators, Output Iterators, Forward Iterators, Bidirectional Iterators, and Random Access Iterators are the five types of C++ iterators.](https://www.programiz.com/sites/tutorial2program/files/cpp-iterator-types.png "C++ Iterator Types")

C++ Iterator Types

As shown by the diagram above, a random access iterator is also a bidirectional iterator with additional features.

Similarly, bidirectional iterators are also forward iterators with additional features and so on.

---

## Input Iterator

C++ Input Iterators are able to **read/process** some values while **iterating forward**.

We can iterate forward using `++` and read values using `*` or member values using `->`.

An iterator that reads values from the input stream is an example of an input iterator.

It can be created as:

```
// create an input iterator to read values from cin
istream_iterator<int> input_itr(cin);
```

Here, we have created an input iterator named input_itr of type `int` that reads input values from the standard input stream `cin`.

**Note:** Input and output iterators are part of C++ STL iterators and are defined in the `<iterator>` header file.

---

## Output Iterator

C++ Output Iterators are able to **write** some values while **iterating forward**.

We can iterate forward using `++` and write values using `*`. The `=` operator can be used to write values

An iterator that writes values to the output stream is an example of an output iterator.

```
// create an output iterator to write integers to the console
ostream_iterator<int> output_itr(cout, " ");
```

Here, we have created an output iterator named output_itr of type `int` that writes values to the standard input stream `cout`.

---

## Forward Iterator

C++ Forward Iterators are able to **read/write** some values while **iterating forward**.

The iterators of the class `forward_list` are forward iterators.

We can iterate forward using `++` and read and write values using `*` or read and write member values using `->`.

For example,

```
#include <iostream>
#include <forward_list>
using namespace std;

int main() {

    forward_list<int> nums{1, 2, 3, 4};

    // initialize an iterator to point
    // to beginning  of a forward list
    forward_list<int>::iterator itr = nums.begin();

    while (itr != nums.end()) {
        // access iterator value using indirection operator
        int original_value = *itr;

        // assign new value using indirection operator
        *itr = original_value * 2;

        // forward the iterator to next position
        itr++;
    }

    // display the contents of nums
    for (int num: nums) {
        cout << num << ", ";
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

2, 4, 6, 8, 

In the above example, we have created a forward list nums and a forward iterator itr to point to the beginning of the forward list.

We have then used itr to access and modify the contents of nums.

Finally, we have used a [ranged for loop](https://www.programiz.com/cpp-programming/ranged-for-loop) to display the elements of the modified forward list.

---

## Bidirectional Iterator

C++ Bidirectional Iterators are able to iterate both forward and backward.

We can iterate forward using `++`, backward using `--`, and read and write values using `*` or read and write member values using `->`.

The iterators of the container classes `list`, `set`, `multiset`, `map`, and `multimap` are bidirectional iterators.

```
#include <iostream>
#include <list>
using namespace std;

int main() {

    list<int> nums {1, 2, 3, 4, 5};

    // initialize iterator to point to beginning of nums
    list<int>::iterator itr = nums.begin();

    cout << "Moving forward: " << endl;

    // display the elements in forward order
    while (itr != nums.end()) {
        cout << *itr  << ", ";

        //  move iterator by 1 position forward
        itr++;
    }

    cout << endl << "Moving backward: " << endl;

    // display the elements in backward order
    while (itr != nums.begin()) {
        if (itr != nums.end()) {
            cout << *itr << ", ";
        }

        //  move iterator by 1 position backward
        itr--;
    }

    cout << *itr << endl;

    return 0;    
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Moving forward: 
1, 2, 3, 4, 5, 
Moving backward: 
5, 4, 3, 2, 1

In the above example, we have created a list nums and a bidirectional iterator itr to point to the beginning of the list.

We have then used itr to access and display the contents of nums in both forward and backward orders.

---

## Random Access Iterator

C++ Random Access Iterators have all the properties of bidirectional iterators along with random access.

Some commonly used operators for random access iterators are:

- `++` - iterate forward
- `--` - iterate backward
- `*` or `[]` - read and write values
- `->` - access member values
- `+` - iterate forward by desired numbers of steps
- `-` - iterate backward by desired numbers of steps

The iterators of the container classes `vector`, `deque`, `array`, and iterators of strings are random-access iterators.

Here's an example,

```
#include <iostream>
#include <vector>
using namespace std;

int main() {

    // create a vector
    vector<int> vec{1, 2, 3, 4};

    // create iterators to point to the first and the last elements 
    vector<int>::iterator itr_first = vec.begin();
    vector<int>::iterator itr_last = vec.end() - 1;

    // display the vector elements
    cout << "First Element: " << *itr_first << endl;
    cout << "Second Element: " << itr_first[1] << endl;


    cout << "Second Last Element: " << *(itr_last - 1) << endl;
    cout << "Last Element: " << *(itr_last) << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

First Element: 1
Second Element: 2
Second Last Element: 3
Last Element: 4

In the above example, we have created a vector vec and two random access iterators itr_first and itr_last to point to the beginning and the end of the vector, respectively.

We then used the iterators to access the contents of vec in random order and display them.

---

## Operators Supported by Iterators

As mentioned earlier, not all operators are compatible with all types of iterators. The operators that can be used for different iterators are shown in the table below.

|Iterator Type|Supported Operators|
|---|---|
|Input Iterator|`++`, `*`, `->`, `==`, `!=`|
|Output Iterator|`++`, `*`, `=`|
|Forward Iterator|`++`, `*`, `->`, `==`, `!=`|
|Bidirectional Iterator|`++`, `--`, `*`, `->`, `==`, `!=`|
|Random Access Iterator|`++`, `--`, `*`, `->`, `[]`, `+`, `-`, `<`, `<=`, `>`, `>=`, `==`, `!=`|

---

## Why Use Iterators?

Here are some reasons you might want to use iterators in C++:

- **Support for algorithms:** The C++ Standard Library provides a wide range of algorithms that can be used with iterators, such as `std::find()`, `std::sort()`, and `std::accumulate()`. These algorithms allow us to perform common operations on containers.
- **Memory efficiency:** Iterators allow us to process large datasets one element at a time without loading the entire dataset at once, resulting in memory efficiency.
- **Consistency:** Iterators provide a way to access and manipulate data of different types of containers in a consistent way. We can use the same iterator syntax for vectors, lists, sets, or any other container.
- **Simplification of code:** Iterators can simplify the code by hiding the details of iterating over the container, thus making the code more readable.

---

## Frequently Asked Questions

What are the differences between iterators and pointers?

|||
|---|---|
|||
|||
|||
|||
|||

How can we create a constant iterator?

What are the differences between begin(), rbegin(), end(), rend(), cbegin() and cend()?

|   |   |
|---|---|
|||
|||
|||
|||
|||
|||

What are advance(), next() and previous() functions?