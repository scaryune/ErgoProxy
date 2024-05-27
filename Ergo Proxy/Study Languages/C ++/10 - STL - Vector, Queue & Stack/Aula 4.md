# C++ Vectors

In C++, vectors are used to store elements of similar data types. However, unlike [arrays](https://www.programiz.com/cpp-programming/arrays), the size of a vector can grow dynamically.

That is, we can change the size of the vector during the execution of a program as per our requirements.

Vectors are part of the [C++ Standard Template Library](https://www.programiz.com/cpp-programming/standard-template-library). To use vectors, we need to include the `vector` header file in our program.

```
#include <vector>
```

---

## C++ Vector Declaration

Once we include the header file, here's how we can declare a vector in C++:

```
std::vector<T> vector_name;
```

The type parameter `<T>` specifies the type of the vector. It can be any primitive data type such as `int`, `char`, `float`, etc. For example,

```
vector<int> num;
```

Here, num is the name of the vector.

Notice that we have not specified the **size** of the vector during the declaration. This is because the size of a vector can grow dynamically, so it is not necessary to define it.

---

## C++ Vector Initialization

There are different ways to initialize a vector in C++.

**Method 1:**

```
// Initializer list
vector<int> vector1 = {1, 2, 3, 4, 5};
```

```
// Uniform initialization
vector<int> vector2 {1, 2, 3, 4, 5};
```

Here, we are initializing the vector by providing values directly to the vector. Now, both `vector1` and `vector2` are initialized with values **1**, **2**, **3**, **4**, **5**.

**Method 2:**

```
vector<int> vector3(5, 12);
```

Here, **5** is the size of the vector and **12** is the value.

This code creates an `int` vector with size **5** and initializes the vector with the value of **12**. So, the vector is equivalent to

```
vector<int> vector3 = {12, 12, 12, 12, 12};
```

---

### Example: C++ Vector Initialization

```
#include <iostream>
#include <vector>
using namespace std;

int main() {

  // initializer list
  vector<int> vector1 = {1, 2, 3, 4, 5};

  // uniform initialization
  vector<int> vector2{6, 7, 8, 9, 10};

  // method 3
  vector<int> vector3(5, 12);

  cout << "vector1 = ";

  // ranged loop
  for (const int& i : vector1) {
    cout << i << "  ";
  }

  cout << "\nvector2 = ";

  // ranged loop
  for (const int& i : vector2) {
    cout << i << "  ";
  }

  cout << "\nvector3 = ";

  // ranged loop
  for (int i : vector3) {
    cout << i << "  ";
  }

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

vector1 = 1  2  3  4  5  
vector2 = 6  7  8  9  10  
vector3 = 12  12  12  12  12 

Here, we have declared and initialized three different vectors using three different initialization methods and displayed their contents.

---

## Basic Vector Operations

The `vector` class provides various methods to perform different operations on vectors. We will look at some commonly used vector operations in this tutorial:

- Add elements
- Access elements
- Change elements
- Remove elements

---

## 1. Add Elements to a Vector

To add a single element into a vector, we use the `push_back()` function. It inserts an element into the end of the vector. For example,

```
#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> num {1, 2, 3, 4, 5};

  cout << "Initial Vector: ";

  for (const int& i : num) {
    cout << i << "  ";
  }
  
  // add the integers 6 and 7 to the vector
  num.push_back(6);
  num.push_back(7);

  cout << "\nUpdated Vector: ";

  for (const int& i : num) {
    cout << i << "  ";
  }

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Initial Vector: 1  2  3  4  5  
Updated Vector: 1  2  3  4  5  6  7

Here, we have initialized an `int` vector num with the elements `{1, 2, 3, 4, 5}`. Notice the statements

```
num.push_back(6);
num.push_back(7);
```

Here, the `push_back()` function adds elements `6` and `7` to the vector.

**Note**: We can also use the `insert()` and `emplace()` functions to add elements to a vector.

---

## 2. Access Elements of a Vector

In C++, we use the index number to access the vector elements. Here, we use the `at()` function to access the element from the specified index. For example,

```
#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> num {1, 2, 3, 4, 5};

  cout << "Element at Index 0: " << num.at(0) << endl;
  cout << "Element at Index 2: " << num.at(2) << endl;
  cout << "Element at Index 4: " << num.at(4);

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

 
Element at Index 0: 1
Element at Index 2: 3
Element at Index 4: 5

Here,

- `num.at(0)` - access element at index **0**
- `num.at(2)` - access element at index **2**
- `num.at(4)` - access element at index **4**

**Note:** Like an array, we can also use the square brackets `[]` to access vector elements. For example,

```
vector<int> num {1, 2, 3};
cout << num[1];  // Output: 2
```

However, the `at()` function is preferred over `[]` because `at()` throws an exception whenever the vector is out of bound, while `[]` gives a garbage value.

```
vector<int> num {1, 2, 3};

// gives garbage value
cout << num[4];

// throws an exception
cout << num.at(4);
```

---

## 3. Change Vector Element

We can change an element of the vector using the same `at()` function. For example,

```
#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> num {1, 2, 3, 4, 5};

  cout << "Initial Vector: ";

  for (const int& i : num) {
    cout << i << "  ";
  }

  // change elements at indexes 1 and 4
  num.at(1) = 9;
  num.at(4) = 7;

  cout << "\nUpdated Vector: ";

  for (const int& i : num) {
    cout << i << "  ";
  }

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Initial Vector: 1  2  3  4  5  
Updated Vector: 1  9  3  4  7

In the above example, notice the statements,

```
num.at(1) = 9;
num.at(4) = 7;
```

Here, we have assigned new values to indexes **1** and **4**. So the value at **index 1** is changed to **9** and the value at **index 4** is changed to **7**.

---

## 4. Delete Elements from C++ Vectors

To delete a single element from a vector, we use the `pop_back()` function. For example,

```
#include <iostream>
#include <vector>

using namespace std;

int main() {
  vector<int> prime_numbers{2, 3, 5, 7};
  
  // initial vector
  cout << "Initial Vector: ";
  for (int i : prime_numbers) {
    cout << i << " ";
  }

  // remove the last element
  prime_numbers.pop_back();

  // final vector
  cout << "\nUpdated Vector: ";
  for (int i : prime_numbers) {
    cout << i << " ";
  }
  
  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Initial Vector: 2 3 5 7 
Updated Vector: 2 3 5 

In the above example, notice the statement,

```
prime_numbers.pop_back();
```

Here, we have removed the last element (**7**) from the vector.

---

## C++ Vector Functions

In C++, the vector header file provides various functions that can be used to perform different operations on a vector.

|Function|Description|
|---|---|
|`size()`|returns the number of elements present in the vector|
|`clear()`|removes all the elements of the vector|
|`front()`|returns the first element of the vector|
|`back()`|returns the last element of the vector|
|`empty()`|returns **1** (true) if the vector is empty|
|`capacity()`|check the overall size of a vector|

---

## C++ Vector Iterators

Vector [iterators](https://www.programiz.com/cpp-programming/iterators) are used to point to the memory address of a vector element. In some ways, they act like [pointers](https://www.programiz.com/cpp-programming/pointers) in C++.

We can create vector iterators with the syntax

```
vector<T>::iterator iteratorName;
```

For example, if we have **2** vectors of `int` and `double` types, then we will need **2** different iterators corresponding to their types:

```
// iterator for int vector
vector<int>::iterator iter1;

// iterator for double vector
vector<double>::iterator iter2;
```

---

### Initialize Vector Iterators

We can initialize vector iterators using the `begin()` and `end()` functions.

**1. begin() function**

The `begin()` function returns an iterator that points to the first element of the vector. For example,

```
vector<int> num = {1, 2, 3};
vector<int>::iterator iter;

// iter points to num[0]
iter = num.begin();
```

**2. end() function**

The `end()` function points to the **theoretical element** that comes **after** the final element of the vector. For example,

```
// iter points to the last element of num
iter = num.end() - 1;
```

Here, due to the nature of the `end()` function, we have used the code `num.end() - 1` to point to the last element of the num vector i.e. num[2].

---

### Example: C++ Vector Iterators

```
#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> num {1, 2, 3, 4, 5};

  // declare iterator
  vector<int>::iterator iter;

  // initialize the iterator with the first element
  iter = num.begin();

  // print the vector element
  cout << "num[0] = " << *iter << endl;

  // iterator points to the 3rd element
  iter = num.begin() + 2;
  cout << "num[2] = " << *iter;

  // iterator points to the last element
  iter = num.end() - 1;
  cout << "num[4] = " << *iter;

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

num[0] = 1
num[2] = 3
num[4] = 5

In this program, we have declared an `int` vector iterator iter to use it with the vector num.

```
// declare iterator
vector<int>::iterator iter;
```

Then, we initialized the iterator to the first element of the vector using the `begin()` function.

```
// initialize the iterator with the first element
iter = num.begin();
```

Then, we printed the vector element by **dereferencing** the iterator:

```
// print the vector element
cout << "num[0] = " << *iter << endl;
```

Then, we printed the 3rd element of the vector by changing the value of iter to `num.begin() + 2`.

Finally, we printed the last element of the vector using the `end()` function.

---

### Example: Iterate Through Vector Using Iterators

```
#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> num {1, 2, 3, 4, 5};

  // declare iterator
  vector<int>::iterator iter;

  // use iterator with for loop
  for (iter = num.begin(); iter != num.end(); ++iter) {
    cout << *iter << "  ";
  }

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

1  2  3  4  5 

Here, we have used a [for loop](https://www.programiz.com/cpp-programming/for-loop) to initialize and iterate the iterator iter from the beginning of the vector to the end of the vector using the `begin()` and `end()` functions.

```
// use iterator with for loop
for (iter = num.begin(); iter != num.end(); ++iter) {
  cout << *iter << "  ";
}
```

---

**Also Read**:

- [C++ Arrays](https://www.programiz.com/cpp-programming/arrays)
- [C++ Standard Template Library](https://www.programiz.com/cpp-programming/standard-template-library)

- [](https://www.programiz.com/cpp-programming/vectors#introduction)
- [](https://www.programiz.com/cpp-programming/vectors#declare)
- [](https://www.programiz.com/cpp-programming/vectors#initialization)
- [](https://www.programiz.com/cpp-programming/vectors#example1)
- [](https://www.programiz.com/cpp-programming/vectors#add-element)
- [](https://www.programiz.com/cpp-programming/vectors#access-element)
- [](https://www.programiz.com/cpp-programming/vectors#change-element)
- [](https://www.programiz.com/cpp-programming/vectors#delete-element)
- [](https://www.programiz.com/cpp-programming/vectors#vector-functions)
- [](https://www.programiz.com/cpp-programming/vectors#iterators)
- [](https://www.programiz.com/cpp-programming/vectors#example4)