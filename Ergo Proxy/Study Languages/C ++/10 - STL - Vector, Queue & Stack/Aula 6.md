# C++ Forward List

C++ forward lists are sequence containers ordered in a strict linear sequence, where you can add or remove elements anywhere in the sequence with constant time efficiency.

Elements in a forward list store information about their next element's location. Thus, they are more efficient in insertion, moving, and extracting elements compared to containers like array, vectors, etc.

However, direct random access is not supported in forward lists.

---

## Create a Forward List

To create a forward list, we must include the `<forward_list>` header in our code.

```
#include <forward_list>
```

We can initialize a forward list as

```
std::forward_list<data_type> forward_list_name = {value1, value2, value3, ...};
```

Here,

- `data_type` - type of data in the forward list.
- `forward_list_name` - name of the forward list.
- `value1, value2, value3, ...` - values to be inserted.

For example,

```
// create an integer forward list
std::forward_list<int> integer_fwd_list = {1, 3, 2, 4, 5};

// create a string forward list
std::forward_list<string> string_fwd_list = {"Eeny", "Meeny", "Miny", "Moe"};
```

---

### Example 1: C++ Forward List

```
#include <forward_list>
#include <iostream>
using namespace std;

int main() {

    forward_list<int> fwd_list = {1, 3, 2, 4, 5};

    // print the elements in the forward list
    for (const int& element : fwd_list) {
        cout << element << " ";
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

1 3 2 4 5 

Notice that the elements appear in the order they were inserted.

**Note**: We will be using the `std` namespace throughout the tutorial. Hence, we have omitted `std::` from our examples.

---

## Forward Lists Methods

Some of the most common methods used with forward lists are listed below:

|Functions|Description|
|---|---|
|`front()`|Access the front element.|
|`push_front()`|Add an element to the start of the list.|
|`insert_after()`|Add an element at the position right after the given position.|
|`assign()`|Assign new contents to the list by replacing the current contents.|
|`pop_front()`|Remove the element at the front.|
|`remove()`|Remove elements with specific values.|
|`clear()`|Delete all the contents of the list.|

---

## Example 2: Find the First Element of the Forward List

We can access the first element of the forward list using the `front()` function. For example,

```
#include <forward_list>
#include <iostream>

using namespace std;

int main() {

    forward_list<int> fwd_list = {1, 2, 3, 4, 5};

    // access the first element
    int first_element = fwd_list.front();

    cout << "The first element is: " << first_element;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

The first element is: 1

---

## Example 3: Add Elements to a Forward List

There are two ways we can add elements to a forward list:

- `push_front()` - adds an element to the front of the list.
- `insert_after()` - adds an element to the specified position.

For example,

```
#include <forward_list>
#include <iostream>

using namespace std;

int main() {

    forward_list<int> fwd_list = {1, 2, 5};

    // add an element to the front
    fwd_list.push_front(2);

    cout << "Forward List after push_front(): ";
    for (const int& element : fwd_list) {
        cout << element << " ";
    }
    cout << endl;

    // point iterator to the 2nd position of the forward list
    auto itr = fwd_list.begin();
    advance(itr, 1);

    // insert element 7 at the 3rd position
    fwd_list.insert_after(itr, 7);

    cout << "Forward List after insert_after(): ";
    for (const int& element : fwd_list) {
        cout << element << " ";
    }
    cout << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Forward List after push_front(): 2 1 2 5 
Forward List after insert_after(): 2 1 7 2 5  

Here, `fwd_list.push_front();` adds **2** to the **front** of fwd_list.

However, to insert **7** at the third position, we must first bring the itr iterator to the **second** position of the forward list:

```
// point itr to the second position
auto itr = fwd_list.begin();
advance(itr, 1);
```

Then, we insert the element to the position that comes **after** the one pointed by itr:

```
// insert 7 one position after itr
fwd_list.insert_after(itr, 7); 
```

---

## Example 4: Update the Contents of the Forward List

We can update the entire contents of a forward list with new elements using the `assign()` function. For example,

```
#include <forward_list>
#include <iostream>

using namespace std;

int main() {

    forward_list<int> fwd_list = {1, 2, 5};
    
    cout << "Forward List before assign(): ";
    for (const int& element : fwd_list) {
        cout << element << " ";
    }
    
    // replace the entire content of the forward list
    // with new elements 3 and 4
    fwd_list.assign({3, 4});

    cout << "\nForward List after assign(): ";
    for (const int& element : fwd_list) {
        cout << element << " ";
    }
    cout << endl;
    
    return 0;    
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Forward List before assign(): 1 2 5 
Forward List after assign(): 3 4 

As you can see, the `assign()` function replaces the original contents of the forward list with new ones.

---

## Example 5: Delete Elements From a Forward List

There are three ways of deleting elements from a forward list:

- pop_front() - deletes the first element of the list.
- remove() - deletes all occurrences of the specified element from the list.
- clear() - deletes all the elements from the list.

For example,

```
#include <forward_list>
#include <iostream>

using namespace std;

int main() {

    forward_list<int> fwd_list = {1, 2, 3, 4, 3, 5};

    cout << "Original Forward List: ";
    for (const int& element : fwd_list) {
        cout << element << " ";
    }
    cout << endl;

    // remove the first element
    fwd_list.pop_front();

    cout << "Forward List after pop_front(): ";
    for (const int& element : fwd_list) {
        cout << element << " ";
    }
    cout << endl;

    // remove all occurrences of 3
    fwd_list.remove(3);

    cout << "Forward List after remove(3): ";
    for (const int& element : fwd_list) {
        cout << element << " ";
    }
    cout << endl;

    // remove all elements of the list
    fwd_list.clear();

    cout << "Forward List after clear(): ";
    for (const int& element : fwd_list) {
        cout << element << " ";
    }
    cout << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Original Forward List: 1 2 3 4 3 5 
Forward List after pop_front(): 2 3 4 3 5 
Forward List after remove(3): 2 4 5 
Forward List after clear():