# C++ Queue

In C++, the STL `queue` provides the functionality of a queue data structure.

The queue data structure follows the **FIFO (First In First Out)** principle where elements that are added first will be removed first.

![In a queue, elements are added from the rear and removed from the front.](https://www.programiz.com/sites/tutorial2program/files/cpp-queue.png "Queue Data Structure")

Queue Data Structure

**Recommended Readings**

- [Queue Data Structure](https://www.programiz.com/dsa/queue "Queue Data Structure")
- [C++ STL](https://www.programiz.com/cpp-programming/standard-template-library "C++ STL")

---

## Create C++ STL Queue

In order to create a queue in C++, we first need to include the `queue` header file.

```
#include <queue>
```

Once we import this file, we can create a `queue` using the following syntax:

```
queue<type> q;
```

Here, `type` indicates the [data type](https://www.programiz.com/cpp-programming/data-types "C++ Data Types") we want to store in the queue. For example,

```
// create a queue of integer data type
queue<int> integer_queue;

// create a queue of string data type
queue<string> string_queue;
```

---

## C++ Queue Methods

In C++, `queue` is a [class](https://www.programiz.com/cpp-programming/object-class#class "C++ Class") that provides various methods to perform different operations on a queue.

|Methods|Description|
|---|---|
|`push()`|Inserts an element at the back of the queue.|
|`pop()`|Removes an element from the front of the queue.|
|`front()`|Returns the first element of the queue.|
|`back()`|Returns the last element of the queue.|
|`size()`|Returns the number of elements in the queue.|
|`empty()`|Returns `true` if the queue is empty.|

---

## Insert Element to a Queue

We use the `push()` method to insert an element to the back of a queue. For example,

```
#include <iostream>
#include <queue>

using namespace std;

int main() {

  // create a queue of string
  queue<string> animals;

  // push elements into the queue
  animals.push("Cat");
  animals.push("Dog");
  
  cout << "Queue: ";

  // print elements of queue
  // loop until queue is empty
  while(!animals.empty()) {

    // print the element
    cout << animals.front() << ", ";

    // pop element from the queue
    animals.pop();
  }

  cout << endl;
 
  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Queue: Cat, Dog,

In the above example, we have created a `queue` of [strings](https://www.programiz.com/cpp-programming/strings "C++ Strings") called animals. Here, we have used the `push()` method to add elements to the end of the queue.

```
animals.push("Cat");
animals.push("Dog");
```

Instead of directly printing the contents of the queue, we have used a `while` loop and various queue methods.

```
while(!animals.empty()) {
  cout << animals.front() << ", ";
  animals.pop();
}
```

This is because the STL queue is an [STL Container Adapter](https://www.programiz.com/cpp-programming/stl-containers#container-adapter) that provides restrictive access to make it behave like a standard queue data structure.

As a result, we cannot iterate through the queue like iterating through [vectors](https://www.programiz.com/cpp-programming/vectors "C++ Vectors") or other [containers](https://www.programiz.com/cpp-programming/stl-containers "STL Containers").

Instead, we print its **front** and then **pop** the element repeatedly inside a loop until the queue is empty.

We will learn about `pop()`, `front()` and `empty()` in the coming sections.

---

## Remove Element from a Queue

We can use the `pop()` method to remove an element from the front of a queue. For example,

```
#include <iostream>
#include <queue>
using namespace std;

// function prototype for display_queue utility
void display_queue(queue<string> q);

int main() {

  // create a queue of string
  queue<string> animals;

  // push element into the queue
  animals.push("Cat");
  animals.push("Dog");
  animals.push("Fox");
  
  cout << "Initial Queue: ";
  display_queue(animals);
  
  // remove element from queue
  animals.pop();
  
  cout << "Final Queue: ";
  display_queue(animals);
  
  return 0;
}

// utility function to display queue
void display_queue(queue<string> q) {
  while(!q.empty()) {
    cout << q.front() << ", ";
    q.pop();
  }

  cout << endl;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Initial Queue: Cat, Dog, Fox, 
Final Queue: Dog, Fox, 

In the above example, we have used the `pop()` method to remove an element from the queue.

Initially, the contents of the queue are `"Cat"`, `"Dog"` and `"Fox"`.

```
// removes front element
animals.pop();
```

Here `animals.pop()` removes the element at the front of the queue i.e. the element inserted at the very beginning which is `"Cat"`.

Hence, the final queue contains the elements `"Dog"` and `"Fox"`.

---

## Access Element from a Queue

We can access the elements of a `queue` using the following methods:

- `front()` - returns the element from the front of the queue
- `back()` - returns the element from the back of the queue

For example,

```
#include <iostream>
#include <queue>
using namespace std;

int main() {

  // create a queue of int
  queue<int> nums;

  // push element into the queue
  nums.push(1);
  nums.push(2);
  nums.push(3);
  
  // get the element at the front
  int front = nums.front();
  cout << "First element: " << front << endl;
  
  // get the element at the back
  int back = nums.back();
  cout << "Last element: " << back << endl;
  
  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

First element: 1
Last element: 3

In the above example, we have used the `front()` and `back()` methods to get the first and last elements from a queue of integers called nums.

We can get the first element i.e. the element at the front using:

```
// returns 1
nums.front()
```

Here, **1** was inserted first so it is at the front.

Similarly, we find the last element i.e. the rear (back) element using:

```
// returns 3
nums.back()
```

Here, **3** was inserted last, so it is at the back.

---

## Get the size of a Queue

We use the `size()` method to get the number of elements in the `queue`. For example,

```
#include <iostream>
#include <queue>
using namespace std;

int main() {

  // create a queue of string
  queue<string> languages;

  // push element into the queue
  languages.push("Python");
  languages.push("C++");
  languages.push("Java");
  
  // get the size of the queue
  int size = languages.size();
  cout << "Size of the queue: " << size;

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Size of the queue: 3

In the above example, we have created a queue of strings called languages and added three elements to it.

Then, we used the `size()` method to find the number of elements in the queue:

```
// returns 3
languages.size();
```

Since we have added three elements to the queue, `languages.size()` returns **3**.

---

## Check if the Queue is Empty

We use the `empty()` method to check if the `queue` is empty. This method returns:

- **1 (true)** - if the queue is empty
- **0 (false)** - if the queue is not empty

For example,

```
#include <iostream>
#include <queue>
using namespace std;

int main() {

  // create a queue of string
  queue<string> languages;
  
  cout << "Is the queue empty? ";

  // check if the queue is empty  
  if (languages.empty()) {
    cout << "Yes" << endl;
  }
  else {
    cout << "No" << endl;
  }

  cout << "Pushing elements..." << endl;

  // push element into the queue
  languages.push("Python");
  languages.push("C++");
 
  cout << "Is the queue empty? ";

  // check if the queue is empty  
  if (languages.empty()) {
    cout << "Yes";
  }
  else {
    cout << "No";
  }

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Is the queue empty? Yes
Pushing elements...
Is the queue empty? No

In the above example, we have used the `empty()` method to determine if the `queue` is empty,

```
if (languages.empty()) {
  cout << "Yes" << endl;
}
else{
  cout << "No" << endl; 
}
```

Initially, the queue has no elements in it. So `languages.empty()` returns `true`.

We then add elements to the queue.

Then we again use `languages.empty()` again to determine if the queue is empty. This time, it returns `false`.

---

**Also Read**

- ﻿[C++ Priority Queue](https://www.programiz.com/cpp-programming/priority-queue "C++ Priority Queue")
- [C++ Deque](https://www.programiz.com/cpp-programming/deque "C++ Deque")
- [C++ Stack](https://www.programiz.com/cpp-programming/stack "C++ Stack")