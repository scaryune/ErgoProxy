# C++ Stack

The STL `stack` provides the functionality of a stack data structure in C++.

The stack data structure follows the **LIFO (Last In First Out)** principle. That is, the element added last will be removed first.

![In stack, the element added last is removed first.](https://www.programiz.com/sites/tutorial2program/files/cpp-stack.png "Stack Data Structure")

Stack Data Structure

To learn more about stacks, visit our tutorial on [Stack Data Structure.](https://www.programiz.com/dsa/stack)

---

## Create a Stack

In order to create a stack in C++, we first need to include the `stack` header file.

```
#include <stack>
```

Once we import this file, we can create a `stack` using the following syntax:

```
stack<type> st;
```

Here, `type` indicates the data type we want to store in the stack. For instance,

```
// create a stack of integers
stack<int> integer_stack;

// create a stack of strings
stack<string> string_stack;
```

---

## Example: C++ STL Stack

```
#include <iostream>
#include <stack>
using namespace std;

int main() {
    // create a stack of strings
    stack<string> languages;
    
    // add element to the Stack
    languages.push("C++");
    languages.push("Java");
    languages.push("Python");
    
    // print top element
    cout << languages.top();

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Python

In the above example, we have created a `stack` of strings named languages.

Here, we have used the `push()` method to add elements to the stack. We have then used the `top()` method to display the top element.

We will learn more about `push()` and `top()` method later in the tutorial.

---

## Stack Methods

In C++, the `stack` class provides various methods to perform different operations on a stack.

|Operation|Description|
|---|---|
|`push()`|adds an element into the stack|
|`pop()`|removes an element from the stack|
|`top()`|returns the element at the top of the stack|
|`size()`|returns the number of elements in the stack|
|`empty()`|returns `true` if the stack is empty|

---

## Add Element Into the Stack

We use the `push()` method to add an element into a stack. For example,

```
#include <iostream>
#include <stack>
using namespace std;

int main() {

  // create a stack of strings
  stack<string> colors;

  // push elements into the stack
  colors.push("Red");
  colors.push("Orange");
  
  cout << "Stack: ";

  // print elements of stack
   while(!colors.empty()) {
    cout << colors.top() << ", ";
    colors.pop();
  }
 
  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Stack: Orange, Red, 

In the above example, we have created a stack of strings called colors. Then, we have used the `push()` method to add elements to the stack.

```
colors.push("Red");
colors.push("Orange");
```

Instead of directly printing the contents of the stack, we have used a `while` loop and various stack methods.

```
while(!colors.empty()) {
  cout << colors.top() << ", ";
  colors.pop();
}
```

To print all elements of the stack, we print its **top element** and then **pop** (remove) it inside the loop. This process continues repeatedly until the stack is empty.

We will learn about the `pop()`, `top()` and `empty()` methods in the coming sections.

Also notice that we have inserted the elements in this order: `{"Red", "Orange"}`.

But when printing the elements, we get `{"Orange", "Red"}` instead.

This is because the stack is a LIFO data structure, which means that the **element inserted last is retrieved first**.

**Note**: Unlike vectors or other containers, we cannot use a ranged `for` loop to iterate through a stack. This is because the STL stack is an [STL Container Adapter](https://www.programiz.com/cpp-programming/stl-containers#container-adapter), which provides restrictive access to make it behave like a standard stack data structure.

---

## Remove Elements From the Stack

We can remove an element from the stack using the `pop()` method. For example,

```
#include <iostream>
#include <stack>
using namespace std;

// function prototype for display_stack utility
void display_stack(stack<string> st);

int main() {

  // create a stack of strings
  stack<string> colors;

  // push elements into the stack
  colors.push("Red");
  colors.push("Orange");
  colors.push("Blue");
  
  cout << "Initial Stack: ";
  // print elements of stack
  display_stack(colors);
  
  // removes "Blue" as it was inserted last
  colors.pop();
  
  cout << "Final Stack: ";

  // print elements of stack
  display_stack(colors);
  
  return 0;
}

// utility function to display stack elements
void display_stack(stack<string> st) {

  while(!st.empty()) {
    cout << st.top() << ", ";
    st.pop();
  }

  cout << endl;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Initial Stack: Blue, Orange, Red, 
Final Stack: Orange, Red,

In the above example, we have used the `pop()` method to remove an element from the stack.

Initially, the contents of the stack are `{"Blue", "Orange", "Red"}`.

Then we have used the `pop()` method to remove the element.

```
// removes top element
colors.pop() 
```

This removes the element at the top of the `stack` i.e. the element inserted last, which is `"Blue"`.

Hence, the final stack becomes `{"Orange", "Red"}`.

---

## Access Elements From the Stack

We access the element at the top of the stack using the `top()` method. For example,

```
#include <iostream>
#include <stack>
using namespace std;

int main() {

  // create a stack of strings
  stack<string> colors;

  // push element into the stack
  colors.push("Red");
  colors.push("Orange");
  colors.push("Blue");
  
  // get top element
  string top = colors.top();

  cout << "Top Element: " << top;
  
  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Top Element: Blue

In the above example, we have created a stack of strings called colors and added the following elements: `"Red"`, `"Orange"` and `"Blue"`.

We have then used the `top()` method to access the top element:

```
string top = colors.top(); 
```

Here, `"Blue"` was inserted last, so it is the **top element.**

---

## Get the Size of the Stack

We use the `size()` method to get the number of elements in the `stack`. For example,

```
#include <iostream>
#include <stack>
using namespace std;

int main() {

  // create a stack of int
  stack<int> prime_nums;

  // push elements into the stack
  prime_nums.push(2);
  prime_nums.push(3);
  prime_nums.push(5);
  
  // get the size of the stack
  int size = prime_nums.size();
  cout << "Size of the stack: " << size;

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Size of the stack: 3

In the above example, we have created a stack of integers called prime_nums and added three elements to it.

Then we have used the `size()` method to find the number of elements in the stack:

```
prime_nums.size();
```

Since we have added 3 elements to the stack, `prime_nums.size()` returns **3**.

---

## Check if the Stack Is Empty

We use the `empty()` method to check if the stack is empty. This method returns:

- **1** **(true)** - if the stack is empty
- **0** **(false)** - if the stack is not empty

For example,

```
#include <iostream>
#include <stack>
using namespace std;

int main() {

  // create a stack of double
  stack<double> nums;
  
  cout << "Is the stack empty? ";

  // check if the stack is empty  
  if (nums.empty()) {
    cout << "Yes" << endl;
  }
  else {
    cout << "No" << endl;
  }

  cout << "Pushing elements..." << endl;

  // push element into the stack
  nums.push(2.3);
  nums.push(9.7);
 
  cout << "Is the stack empty? ";

  // check if the stack is empty  
  if (nums.empty()) {
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

Is the stack empty? Yes
Pushing elements...
Is the stack empty? No

In the above example, we have used the `empty()` method to determine if the `stack` is empty,

```
if(nums.empty()) { // returns false
  cout << "Yes" << end;;
}
else {
  cout << "No" << endl; 
}
```

Initially, the stack has no elements in it. So `nums.empty()` returns `true`.

We have then added elements to the stack.

Again, we use `nums.empty()` to determine if the stack is empty. This time, it returns `false`.

- [](https://www.programiz.com/cpp-programming/stack#introduction)
- [](https://www.programiz.com/cpp-programming/stack#create)
- [](https://www.programiz.com/cpp-programming/stack#example)
- [](https://www.programiz.com/cpp-programming/stack#stack-methods)
- [](https://www.programiz.com/cpp-programming/stack#push)
- [](https://www.programiz.com/cpp-programming/stack#pop)
- [](https://www.programiz.com/cpp-programming/stack#top)
- [](https://www.programiz.com/cpp-programming/stack#size-empty)
- [](https://www.programiz.com/cpp-programming/stack#empty)

[

  


](https://www.programiz.com/dsa/priority-queue "C++ Priority Queue")