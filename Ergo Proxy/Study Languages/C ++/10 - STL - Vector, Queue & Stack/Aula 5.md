# C++ List

C++ List is a [STL](https://www.programiz.com/cpp-programming/standard-template-library) [container](https://www.programiz.com/cpp-programming/stl-containers) that stores elements randomly in unrelated locations. To maintain sequential ordering, every list element includes two links:

- one that points to the previous element
- another that points to the next element

![C++ STL  list implementation showing its doubly linked nature](https://www.programiz.com/sites/tutorial2program/files/cpp-list-implementation.png "C++ STL list")

C++ STL list implementation

In C++, the STL list implements the [doubly-linked list data structure](https://www.programiz.com/dsa/doubly-linked-list). As a result, we can iterate both forward and backward.

---

## Create C++ STL List

To create a list, we need to include the `list` header file in our program.

```
#include<list>
```

Once we import the header file, we can now declare a list using the following syntax:

```
std::list<Type> list_name = {value1, value2, ...};
```

Here,

- `std::list` - declares an STL container of type `list`
- `<Type>` - the [data type](https://www.programiz.com/cpp-programming/data-types) of the values to be stored in the list
- `list_name` - a unique name given to the list
- `value1, value2, ...` - values to be stored in the list

Let's see an example,

```
// create a list of integer type
std::list<int> numbers = {1, 2, 3, 4, 5};

// create a list of character type
std::list<char> vowels = {'a', 'e', 'i', 'o', 'u'};
```

**Note:** We can also include list elements without mentioning the [assignment operator](https://www.programiz.com/cpp-programming/operators#assignment). For example,

```
std::list<int> numbers {1, 2, 3, 4, 5};
```

---

## Example: C++ STL List

```
#include <iostream>
#include <list>

using namespace std;

int main() {

    // create the list
    list<int> numbers {1, 2, 3, 4};
  
    // display the elements of the list
    cout << "List Elements: ";
    for(int number : numbers) {
        cout << number <<", ";
    }
    
    return 0;

}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

List Elements: 1, 2, 3, 4,

In the above example, we have created a list named numbers with elements: **1**, **2**, **3**, **4**. We then used a [ranged for loop](https://www.programiz.com/cpp-programming/ranged-for-loop) to print the list elements.

**Note:** We have used `list` instead of `std::list` because we have already defined [std namespace](https://www.programiz.com/cpp-programming/std-namespace) using `using namespace std;`.

---

## Basic operations on List

C++ STL provides various [functions](https://www.programiz.com/cpp-programming/function) that we can use to perform different operations on lists. Let's look at some commonly used list functions to perform the following operations:

1. Add elements
2. Access elements
3. Remove elements

---

## 1. Add Elements to a List in C++

We can add values in a list using the following functions:

- `push_front()` - inserts an element to the beginning of the list
- `push_back()` - adds an element to the end of the list

Let's see an example,

```
#include <iostream>
#include <list>

using namespace std;

int main() {
    
    // create a list
    list<int> numbers = {1, 2, 3};
  
    // display the original list 
    cout << "Initial List: ";
    for(int number: numbers) {
        cout << number << ", ";
    }
  
    // add element at the beginning
    numbers.push_front(0);

    // add element at the end
    numbers.push_back(4);

    // display the modified list
    cout << endl << "Final List: ";
    for(int number : numbers) {
        cout << number << ", ";
    }

  return 0;

}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Initial List: 1, 2, 3, 
Final List: 0, 1, 2, 3, 4,

---

## 2. Access List Elements

We can access list elements using the following functions:

- `front()` - returns the first element of the list
- `back()` - returns the last element of the list

Let's see an example,

```
#include <iostream>
#include <list>

using namespace std;

int main() {

    // create a list
    list<int> numbers = {1, 2, 3, 4, 5};
  
    // display the first element
    cout << "First Element: " << numbers.front() << endl;
  
    // display the last element
    cout << "Last Element: " << numbers.back();
  
    return 0;
    
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

First Element: 1
Last Element: 5

---

## 3. Delete List Elements

We can delete list elements using the following functions:

- `pop_front()` - removes the element at the beginning of the list
- `pop_back()` - removes the element at the end of the list

Here's an example,

```
#include <iostream>
#include <list>

using namespace std;

int main() {
    // create a list
    list<int> numbers = {1, 2, 3, 4, 5};
 
    // display the original list 
    cout << "Inital List: ";
    for(int number : numbers) {
        cout << number << ",  ";
    }

    // remove the first element of the list
    numbers.pop_front();

    // remove the last element of the list
    numbers.pop_back();

    // display the modified list 
    cout << endl << "Final List: ";
    for(int number : numbers) {
        cout << number << ", ";
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Inital List: 1,  2,  3,  4,  5,  
Final List: 2, 3, 4, 

---

## Other List Functions in C++

While there are many functions that can be used with lists, we will only look at some of the functions in the table below:

|Function|Description|
|---|---|
|`reverse()`|Reverses the order of the elements.|
|`sort()`|Sorts the list elements in a particular order.|
|`unique()`|Removes consecutive duplicate elements.|
|`empty()`|Checks whether the list is empty.|
|`size()`|Returns the number of elements in the list.|
|`clear()`|Clears all the values from the list|
|`merge()`|Merges two sorted lists.|

---

## Access elements using an iterator

We can use [iterators](https://www.programiz.com/cpp-programming/iterators) to access a list element at a specified position. For example,

```
#include <iostream>
#include <list>

using namespace std;

int main() {

     // create a list
    list<int> numbers = {1, 2, 3, 4, 5};

    // create an iterator to point to the first element of the list
    list<int>::iterator itr = numbers.begin();
  
    // increment itr to point to the 2nd element
    ++itr;
    
    //display the 2nd element
    cout << "Second Element: " << *itr << endl;
  
    // increment itr to point to the 4th element
    ++itr;
    ++itr;

    // display the 4th element
    cout << "Fourth Element: " << *itr;
  
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Second Element: 2
Fourth Element: 4

In the above example,

- `list<int>::iterator` - defines an iterator for a list of `int` type
- `numbers.begin()` - sets the iterator to point to the beginning of the list

Notice that we have used `++itr;` repeatedly instead of adding an integer to itr like `itr+3;`.

This is because iterators are not simple numeric values like regular integers. They point to specific memory locations in the container.  
  
Incrementing an iterator with the `++` operator makes it point to the next element in the container.

To learn more about iterators, visit [C++ STL Iterators](https://www.programiz.com/cpp-programming/iterators).

---

## Frequently Asked Questions

How to add an element to a list at a specified location?

[](https://www.programiz.com/cpp-programming/online-compiler)

How to remove a list element from a specified location?

[](https://www.programiz.com/cpp-programming/online-compiler)

[](https://www.programiz.com/cpp-programming/online-compiler)

---

**Also Read**

- [C++ Forward List](https://www.google.com/url?q=/cpp-programming/forward-list&sa=D&source=docs&ust=1706675883798730&usg=AOvVaw1kBwY2q5L0r1GNx5-UmMp5)
- [C++ Array](https://www.programiz.com/cpp-programming/arrays)