# C++ Standard Template Library

In C++, the Standard Template Library (STL) provides a set of programming tools to implement algorithms and data structures like vectors, lists, queues, etc.

STL implements these data structures and algorithms using general-purpose classes and functions that have been tested rigorously.

C++ STL has 3 major components:

- Containers
- Iterators
- Algorithms

In addition to these, STL also provides several other features, including function objects, smart pointers, and exception handling mechanisms.

---

## C++ STL Containers

STL containers store data and organize them in a specific manner as required.

For example, **vectors** store data of the same type in a sequential order. Whereas, **maps** store data in key-value pairs.

We can classify STL containers into 3 types:

**1.** **Sequence containers:**

- Array
- [Vector](https://www.programiz.com/cpp-programming/vectors)
- [Queue](https://www.programiz.com/cpp-programming/queue)
- [Deque](https://www.programiz.com/cpp-programming/deque)
- Forward_list
- [List](https://www.programiz.com/cpp-programming/list)

**2.** **Associative containers:**

- Set
- Multiset
- Map
- Multimap

**3.** **Unordered associative containers:**

- [Unordered_set](https://www.programiz.com/cpp-programming/unordered-set)
- Unordered_multiset
- [Unordered_map](https://www.programiz.com/cpp-programming/unordered-map)
- Unordered_multimap

To learn more about containers, visit our [C++ STL Containers](https://www.programiz.com/cpp-programming/stl-containers) tutorial.

**Note:** STL array is different from the common arrays we've been using so far. STL array is defined in the `std::array` class, which contains many useful functions and algorithms in addition to the array data structure. These features are not present in ordinary arrays.

---

### Example 1: C++ STL Containers: Vector

In C++, vectors are like resizable arrays; they store data of the same type in a sequence and their size can be changed during runtime as needed.

We need to import the `<vector>` header file to use a vector.

```
#include <iostream>
#include <vector>

using namespace std;

int main() {
    
    // create vector of int type
    vector<int> numbers {1, 2, 3, 4, 5};

    // print vector elements using ranged loop
    for (int number : numbers) {
        cout << number << "  ";
    }
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

1  2  3  4  5

Here, we have created a vector of `int` type named numbers with 5 elements.

We then used the [ranged for loop](https://www.programiz.com/cpp-programming/ranged-for-loop) to print all elements of the vector.

To learn more about vectors in C++, visit our [C++ Vectors](https://www.programiz.com/cpp-programming/vectors) tutorial.

---

## C++ STL Iterators

Iterators are objects that are used to access elements of a container.

We can declare an iterator for each container in the C++ Standard Template Library. For example,

```
vector<int>::iterator it;
```

We often use iterator member functions like `begin()`, `end()`, etc. to return iterators that point to container elements. For example,

```
vector<int> numbers = {3, 2, 5, 1, 4};
vector<int>::iterator itr1 = numbers.begin();
vector<int>::iterator itr2 = numbers.end();
```

Here,

- `numbers.begin()` - returns an iterator that points to the beginning of the numbers vector i.e. the element **3**
- `numbers.end()` - returns an iterator that points to the end of the numbers vector.

**Note:** `numbers.end()` doesn't return an iterator to the final vector element **4**. Instead, it returns an iterator to the theoretical element that comes after the final element. The same applies to all other container types.

To learn more about iterators in STL, visit our tutorial on _C++ STL Iterators_.

---

### Example 2: C++ STL Iterators

```
#include <iostream>
#include <vector>
using namespace std;

int main() {
    
    // initialize vector of int type
    vector<int> numbers {1, 2, 3, 4, 5};

    // initialize vector iterator to point to the first element
    vector<int>::iterator itr = numbers.begin();
    cout << "First Element: " << *itr << "  "<<endl;

    // change iterator to point to the last element
    itr = numbers.end() - 1;
    cout << "Last Element: " << *itr;

    return 0;  
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

First Element: 1  
Last Element: 5

Here, we have used `numbers.end()- 1` instead of `numbers.end()`.

This is because the `end()` function points to the **theoretical element** that comes after the final element of the container.

So, we need to subtract **1** from `numbers.end()` in order to point to the final element. Similarly, using the code `numbers.end()- 2` points to the second-last element, and so on.

**Note:** The asterisk `*` before itr indicates that the value of the element that the iterator points to is being accessed. This is similar to [dereferencing pointers](https://www.programiz.com/cpp-programming/pointers/#get-value).

Also, when we try to print the iterators, we get an error.

```
// error
cout << itr << "  ";
```

This is because, unlike pointers, we cannot print an iterator.

---

## C++ STL Algorithms

An algorithm is a series of instructions to solve a particular problem.

In C++, we can use the Standard Template Library to implement some of the commonly used algorithms. These STL components are simply known as the "algorithms library".

Some of the most commonly used algorithms in the C++ Standard Template Library are:

- Sorting algorithms
- Searching algorithms
- Copying algorithms
- Counting algorithms

To learn more about the algorithms library, visit our _C++ STL Algorithms_ tutorial.

---

### Example 3: C++ STL Sorting Algorithm

```
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    
    // initialize vector of int type
    vector<int> numbers = {3, 2, 5, 1, 4};

    // sort vector elements in ascending order
    sort(numbers.begin(), numbers.end());

    // print the sorted  vector 
    for (int number : numbers) {
        cout << number << "  ";
    }
    
    return 0;    
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

1  2  3  4  5

In this example, we have used the `sort()` function to sort the elements of the `numbers` vector in ascending order.

Notice that we have imported the `<algorithm>` header file to use the `sort()` function.