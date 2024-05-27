# C++ STL Containers

A container is an object that stores a collection of objects of a specific type. For example, if we need to store a list of names, we can use a `vector`.

C++ STL provides different types of containers based on our requirements.

---

## Types of STL Container in C++

In C++, there are generally 3 kinds of STL containers:

- Sequential Containers
- Associative Containers
- Unordered Associative Containers

---

## 1. Sequential Containers in C++

In C++, sequential containers allow us to store elements that can be accessed in sequential order.

Internally, sequential containers are implemented as **arrays** or **linked lists** data structures**.**

**Types of Sequential Containers**

- _Array_
- _Vector_
- _Deque_
- _List_
- _Forward List_

---

### Example: C++ Sequential Container (vector)

In this example, we will be using the `vector` class to demonstrate the working of a sequential container.

```
#include <iostream>
#include <vector>
using namespace std;

int main() {

  // initialize a vector of int type
  vector<int> numbers = {1, 100, 10, 70, 100};

  // print the vector
  cout << "Numbers are: ";
  for(auto &num: numbers) {
    cout << num << ", ";
  }

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Numbers are: 1, 100, 10, 70, 100,

In the above example, we have created sequential container numbers using the `vector` class.

```
vector<int> numbers = {1, 100, 10, 70, 100};
```

Here, we have used a [ranged for loop](https://www.programiz.com/cpp-programming/ranged-for-loop) to print each element of the container.

In the output, we can see the numbers are shown in sequential order as they were initialized.

```
// output numbers
1, 100, 10, 70, 100,
```

---

## 2. Associative Containers in C++

In C++, associative containers allow us to store elements in sorted order. The order doesn't depend upon when the element is inserted.

Internally, they are implemented as **binary tree** data structures.

**Types of Associative Containers**

- _Set_
- _Map_
- _Multiset_
- _Multimap_

---

### Example: C++ Associative Container (set)

In this example, we will be using the `set` class to demonstrate the working of an associative container.

```
#include <iostream>
#include <set>
using namespace std;

int main() {

  // initialize a set of int type
  set<int> numbers = {1, 100, 10, 70, 100};

  // print the set
  cout << "Numbers are: ";
  for(auto &num: numbers) {
    cout << num << ", ";
  }

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Numbers are: 1, 10, 70, 100,

In the above example, we have created an associative container using the `set` class.

We have initialized a set named numbers with unordered integers, along with a duplicate value **100**:

```
set<int> numbers = {1, 100, 10, 70, 100};
```

Then we print the content of the set using a ranged `for` loop.

In the output, we see that the numbers are sorted in ascending order with duplicate numbers removed. Initially, **100** was repeated twice but the set removes the duplicate number **100**.

```
// output numbers
1, 10, 70, 100
```

---

## 3. Unordered Associative Containers in C++

In C++, STL Unordered Associative Containers provide the unsorted versions of the associative container.

Internally, unordered associative containers are implemented as **hash table** data structures**.**

**Types of Unordered Associative Containers**

- _Unordered Set_
- _Unordered Map_
- _Unordered Multiset_
- _Unordered Multimap_

---

### Example: C++ Unordered Associative Container (unordered_set)

In this example, we will be using the `unordered_set` class to demonstrate the working of an unordered associative container.

```
#include <iostream>
#include <unordered_set>
using namespace std;

int main() {

  // initialize an unordered_set of int type
  unordered_set<int> numbers = {1, 100, 10, 70, 100};

  // print the set
  cout << "Numbers are: ";
  for(auto &num: numbers) {
    cout << num << ", ";
  }

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Numbers are: 70, 10, 100, 1,

In the above example, we have created an associative container using the `unordered_set` class.

We have initialized the unordered set numbers with unordered integers, along with a duplicate value **100**:

```
unordered_set<int> numbers = {1, 100, 10, 70, 100};
```

Then we print the content of the set using a range-based `for` loop.

In the output, we see that the duplicate number **100** is removed but it is not sorted in ascending order.

```
// output numbers
70, 10, 100, 1,
```

---

## Container Adapters in C++

In C++, Container Adapters take an existing STL container and provide a restricted interface to make them behave differently. For example,

A stack is a container adapter that uses the sequential container `deque` and provides a restricted interface to support `push()` and `pop()` operations only.

**Types of Container Adapters**

- _Stack_
- _Queue_
- _Priority Queue_

---

### Example: C++ Container Adapter (stack)

In this example, we will be using the `stack` class to demonstrate the working of a container adapter.

```
#include <iostream>
#include <stack>
using namespace std;

int main() {

  // create a stack of ints
  stack<int> numbers;

  // push into stack
  numbers.push(1);
  numbers.push(100);
  numbers.push(10);

  cout << "Numbers are: ";

  // we can access the element by getting the top and popping
  // until the stack is empty
  while(!numbers.empty()) {
    // print top element
    cout << numbers.top() << ", ";

    // pop top element from stack
    numbers.pop();
  }

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Numbers are: 10, 100, 1,

In the above example, we have created a container adaptor using the `stack` class.

```
stack <int> numbers;
```

Unlike other containers, we are not directly initializing values to this container. This is because the container adaptor restricts assigning values directly to the container.

That's why we have used the `push()` operation to insert elements to the stack.

Similarly, we are not allowed to directly iterate through this container. So, we have used a loop that iterates until the stack is empty.

```
while (!numbers.empty()) {
  cout << numbers.top() << ", ";
  numbers.pop();
}
```

Here,

- `numbers.empty()` - checks if the `stack` is empty
- `numbers.top()` - returns the element at the top of the `stack`
- `numbers.pop()` - removes the top element of the `stack`