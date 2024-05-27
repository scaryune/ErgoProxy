# C++ Deque

In C++, the STL `deque` is a sequential container that provides the functionality of a double-ended queue data structure.

In a regular queue, elements are added from the rear and removed from the front. However, in a deque, we can insert and remove elements from both the **front** and **rear**.

![In a deque, we can insert and remove elements from both the front and rear.](https://www.programiz.com/sites/tutorial2program/files/cpp-deque.png "Deque Data Structure")

Deque Data Structure

To learn more about deques, visit [Deque Data Structure.](https://www.programiz.com/dsa/deque)

---

## Create C++ STL Deque

In order to create a deque in C++, we first need to include the `deque` header file.

```
#include <deque>
```

Once we import this file, we can create a `deque` using the following syntax:

```
deque<type> dq;
```

Here, `type` indicates the data type we want to store in the deque. For example,

```
// create a deque of integer data type
deque<int> dq_integer;

// create a deque of string data type
deque<string> dq_string;
```

---

## Initialize a Deque

We can initialize a C++ deque in the following ways:

```
// method 1: initializer list
deque<int> deque1 = {1, 2, 3, 4, 5};

// method 2: uniform initialization
deque<int> deque2 {1, 2, 3, 4, 5};
```

Here, both deque1 and deque2 are initialized with values **1**, **2**, **3**, **4**, **5**.

---

### Example: C++ Deque

```
#include <iostream>
#include <deque>
using namespace std;

// function prototype
void display_deque(deque<int>);

int main() {
 
  // uniform initialization 
  deque<int> deque1 {1, 2, 3, 4, 5};

  cout << "deque1 = ";

  // display elements of deque1
  for (int num : deque1) {
    cout << num << ", ";
  }

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

deque1 = 1, 2, 3, 4, 5, 

In the above example, we have declared and initialized a deque named deque1 using uniform initialization.

```
deque<int> deque1 {1, 2, 3, 4, 5};
```

Then, we have displayed the deque contents using a [ranged for loop](https://www.programiz.com/cpp-programming/ranged-for-loop).

```
for (int num : deque1) {
  cout << num << ", ";
}
```

---

## Other Ways to Create a C++ Deque

Create a deque using fill constructor.

Create a deque from another deque.

---

## C++ Deque Methods

In C++, the `deque` class provides various methods to perform different operations on a deque.

|Methods|Description|
|---|---|
|`push_back()`|inserts element at the back|
|`push_front()`|inserts element at the front|
|`pop_back()`|removes element from the back|
|`pop_front()`|removes element from the front|
|`front()`|returns the element at the front|
|`back()`|returns the element at the back|
|`at()`|sets/returns the element at specified index|
|`size()`|returns the number of elements|
|`empty()`|returns `true` if the deque is empty|

---

## Insert Elements to a Deque

We can use the following methods to insert elements:

- `push_back()` - insert elements at the end
- `push_front()` - insert elements at the beginning

For example,

```
#include <iostream>
#include <deque>
using namespace std;

int main() {

  deque<int> nums {2, 3};

  cout << "Initial Deque: ";
  for (const int& num : nums) {
    cout << num << ", ";
  }
  
  // add integer 4 at the back
  nums.push_back(4);
   
  // add integer 1 at the front
  nums.push_front(1);
  
  cout << "\nFinal Deque: ";
  for (const int& num : nums) {
    cout << num << ", ";
  }
  
  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Initial Deque: 2, 3, 
Final Deque: 1, 2, 3, 4,

In the above example, we have initialized a `deque` of integers named nums with the elements **2** and **3**.

Then, we inserted the integer **4** to the back of the nums.

```
// nums = {2, 3, 4}
nums.push_back(4);
```

Finally, we inserted **1** at the front of the deque.

```
// nums = {1, 2, 3, 4}
nums.push_front(1);
```

**Note**: We can also use the `insert()` and `emplace()` methods to add elements to the deque.

---

## Access Elements from a Deque

We can use the following methods to access elements of the `deque`:

- `front()` - returns element at the front
- `back()` - returns element at the back
- `at()` - returns element at the specified index

For example,

```
#include <iostream>
#include <deque>
using namespace std;

int main() {

  deque<int> nums {1, 2, 3};
  
  cout << "Front element: " << nums.front() << endl;
  cout << "Back element: " << nums.back() << endl;
  cout << "Element at index 1: " << nums.at(1) << endl;
  cout << "Element at index 0: " << nums[0];
  
  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Front element: 1
Back element: 3
Element at index 1: 2
Element at index 0: 1

In the above example,

- `nums.front()` - returns the element at the front of the deque i.e. **1**
- `nums.back()` - returns the element at the back of the deque i.e. **3**
- `nums.at(1)` - returns the element at **index 1** i.e. **2**
- `nums[0]` - returns the element at **index 0** i.e. **1**

**Note**: While we can use the `[]` operator to access deque elements, it is preferable to use the `at()` method.

This is because `at()` throws an exception whenever the deque is out of bounds, while `[]` gives a garbage value.

---

## Change Elements of a Deque

We can use the `at()` method to change the element of the `deque`. For example,

```
#include <iostream>
#include <deque>
using namespace std;

int main() {

  deque<int> nums = {1, 2};
  
  cout << "Initial Deque: ";

  for (const int& num : nums) {
    cout << num << ", ";
  }
  
  // change elements at the index
  nums.at(0) = 3;
  nums.at(1) = 4;
  
  cout << "\nUpdated Deque: ";

  for (const int& num : nums) {
    cout << num << ", ";
  }
  
  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Initial Deque: 1, 2,    
Updated Deque: 3, 4,  

In the above example, the initial contents of the nums deque are `{1, 2}`.

Then, we have used the `at()` method to change the elements at the specified indexes:

- `nums.at(0) = 2;` - changes the value at **index 0** changes to **3**
- `nums.at(1) = 4;` - changes the value at **index 1** to **4**

---

## Remove Elements from a Deque

We can remove the elements of a deque using the following methods:

- `pop_back()` - removes the element from the back
- `pop_front()` - removes the element from the front

For example,

```
#include <iostream>
#include <deque>
using namespace std;

// function prototype for display_deque()
void display_deque(deque<int>);

int main() {

  deque<int> nums {1, 2, 3};
  
  cout << "Initial Deque: ";
  display_deque(nums);

  // remove element from the back
  nums.pop_back();
  
  cout << "\nDeque after pop_back(): ";
  display_deque(nums);
  
  // remove element from the front
  nums.pop_front();
  
  cout << "\nDeque after pop_front(): ";
  display_deque(nums);
  
  return 0;
}

// utility function to print deque elements
void display_deque(deque<int> dq){
  for (const int& num : dq) {
    cout << num << ", ";
  }
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Initial Deque: 1,  2,  3,  
Deque after pop_back(): 1, 2, 
Deque after pop_front(): 2, 

In the above example, we have initialized an integer `deque` named nums with the elements `{1, 2, 3}`.

Then, we used `pop_back()` and `pop_front()` to remove elements from nums.

```
nums.pop_back(); // removes 3
names.pop_front(); // removes 1
```

So the final deque becomes `{2}`.

---

## C++ Deque Iterators

Iterators can be used to point to the memory address of a `deque` element.

We can create a `deque` iterator using the following syntax:

```
deque<type>::iterator itertaor_name;
```

For example,

```
// iterator for int deque
deque<int>::iterator iter_int;

// iterator for double deque
deque<double>::iterator iter_double;
```

---

### Access Elements Using Deque Iterators

We can access the elements in `deque` using iterators. For example,

```
#include <iostream>
#include <deque>
using namespace std;

int main() {

  deque<int> nums {1, 2, 3};
  
  // declare an iterator to deque
 deque<int>::iterator dq_iter;
  
  // make iterator point to first element
  dq_iter = nums.begin();
  
  // print value pointed by itertor using *
  int first_element = *dq_iter; 

  cout << "nums[0] = " << first_element << endl;
  
  // make iterator point to element at index 1
  dq_iter = nums.begin() + 1; 
  int element_index1 = *dq_iter; 

  cout << "nums[1] = " << element_index1 << endl;

  // make iterator point to last element
  dq_iter = nums.end() - 1; 
  int last_element = *dq_iter; 

  cout << "nums[2] = " << last_element;
  
  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

nums[0] = 1
nums[1] = 2
nums[2] = 3

In the above example, we have used iterators to access elements in the `deque`. Initially, we created an iterator that can point to a `deque` of integers:

```
deque<int>::iterator dq_iter;
```

Then, we have used the dq_iter iterator to point to the following elements:

**1. The First Element**

```
dq_iter = nums.begin();
```

Here, the `begin()` method returns an iterator that points to the first element.

**2. Element at Index 1**

```
dq_iter = nums.begin() + 1;
```

The code `begin() + 1` returns an iterator that points to the element at **index 1**.

**Note:** To generalize, `nums.begin() + i` points to the element at index `i`.

**3. The Last Element**

```
dq_iter = nums.end() - 1;
```

Notice that we are using `nums.end() - 1` instead of `nums.end()`.

This is because the `end()` method iterator points to the iterator past the last element. So, in order to get the final element, we are subtracting **1**.

**4. Get the Element Value**

After using dq_iter to point to a certain element, we use the **indirection operator** `*` to get the value of that element:

```
// point to the first element
dq_iter = nums.begin();

// returns 1
int first_element = *dq_iter;
```

Here, *dq_iter gives the value of the element pointed to by the dq_iter iterator.

---

## Frequently Asked Questions

How to remove elements at the specified index?

How to remove elements in a certain index range?

[](https://www.programiz.com/cpp-programming/online-compiler)

How to remove all elements of the deque?

How to determine the size of the deque?

Can we use auto to initialize a deque iterator?

- [](https://www.programiz.com/cpp-programming/deque#introduction)
- [](https://www.programiz.com/cpp-programming/deque#initialize)
- [](https://www.programiz.com/cpp-programming/deque#deque-methods)
- [](https://www.programiz.com/cpp-programming/deque#insert)
- [](https://www.programiz.com/cpp-programming/deque#access)
- [](https://www.programiz.com/cpp-programming/deque#change)
- [](https://www.programiz.com/cpp-programming/deque#remove)
- [](https://www.programiz.com/cpp-programming/deque#iterators)