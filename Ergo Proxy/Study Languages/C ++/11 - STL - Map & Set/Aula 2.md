# C++ Set

Sets are [STL](https://www.programiz.com/cpp-programming/standard-template-library) [containers](https://www.programiz.com/cpp-programming/stl-containers) that store unique elements of the same type in a sorted manner.

As the value of every element in a set is unique, the value itself acts as the key for identifying the element.

---

## Set Properties

C++ set has the following properties.

**1. Unique Elements**

No two elements in a set can be equal.

**2. Immutable**

We can add or remove elements from a set, but we can't change the values of existing elements.

**3. Sorted Order**

Elements in a set are sorted following a specific strict weak ordering.

By default, C++ sets are sorted in ascending order, but we have the option to change that.

**4. Associative**

Elements of a set are referenced using their **key**, not by their position in the container.

This is unlike [arrays](https://www.programiz.com/cpp-programming/arrays), where elements are accessed using indexes.

---

## Create a Set

To implement a set in C++, we must include the `<set>` header file in our program.

```
#include <set>
```

We can create a set in C++ using the following syntax:

```
// declare a set
std::set<data_type> set_name = {key1, key2, key3, ...};
```

Here,

- `std::set` - declares an STL container of type `set`.
- `<data_type>` - the [data type](https://www.programiz.com/cpp-programming/data-types) of the values to be stored in the set.
- `set_name` - a unique name given to the set.
- `key1, key2, key3, ...` - key/value to be stored in the set.

For example,

```
// initialize set with elements
std::set<int> my_set1 = {5, 3, 8, 1, 3};

// create an empty set
std::set<int> my_set2;
```

**Note:** Moving forward, we will be using the `std` [namespace](https://www.programiz.com/cpp-programming/namespaces) so we can omit `std::` from our syntax.

---

### Example 1: Create a Set

```
#include <iostream>
#include <set>
using namespace std;

int main() {

    set<int> my_set = {5, 3, 8, 1, 3};
    
    for(int val : my_set) {
        cout << val << " ";
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

1 3 5 8 

Here, we have created a set of type `int`.

As you can see, the set returned the values in a sorted manner and ignored the repeated instance of **3**.

**Note:** We cannot use the `[]` [operator](https://www.programiz.com/cpp-programming/operators) to add elements to a set. Doing so will result in an error.

```
// this is not allowed in a set
my_set[4] = 4
```

---

## Sort a Set in Descending Order

To get the elements of a set sorted in descending order, we can modify our syntax as follows:

```
set<int, greater<int>> my_set;
```

For example,

```
#include <iostream>
#include <set>
using namespace std;

int main() {

    set<int, greater<int>> my_set = {5, 3, 8, 1, 3};
    
    for(int val : my_set) {
        cout << val << " ";
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

8 5 3 1 

As can be seen from the output, the set now returns the elements sorted in descending order.

---

## C++ Set Methods

In C++, the `set` class provides various methods to perform various operations in a set.

|Operation|Description|
|---|---|
|`insert()`|Insert elements into a set.|
|`erase()`|Delete elements from a set.|
|`clear()`|Remove all the elements from a set.|
|`empty()`|Check if the set is empty.|
|`size()`|Returns the size of the set.|

---

## Example 2: Add Values to a Set

```
#include <iostream>     
#include <set>          
using namespace std;
   
int main () {

    set<int> my_set;

    // add values to the set
    my_set.insert(10);
    my_set.insert(30);
    my_set.insert(20);
    my_set.insert(50);
    my_set.insert(40);
    my_set.insert(50);
    
    // print the set elements
    for (int i : my_set) {
        cout << i << "  ";
    }
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

10  20  30  40  50  

Here, we have created an empty set my_set of type `int` and added values to it using the `insert()` method.

Notice that the duplicate insertions are removed, and the set is sorted in ascending order despite the order of insertion being different.

---

## Example 3: Check if an Element Exists in a Set

```
#include <iostream>     
#include <set>          
using namespace std;
   
int main () {

    set<int> my_set;

    // add values to the set
    my_set.insert(10);
    my_set.insert(30);
    my_set.insert(20);
    my_set.insert(50);
    my_set.insert(40);
    my_set.insert(50);
    
    // check if 40 exists
    int num = 40;
    if(my_set.count(num) == 1) {
        cout << num << " exists." << endl;
    } else {
        cout << num << " doesn't exist." << endl;
    }
    
    // check if 60 exists
    num = 60;
    if(my_set.count(num) == 1) {
        cout << num << " exists." << endl;
    } else {
        cout << num << " doesn't exist." << endl;
    }
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

40 exists.
60 doesn't exist.

Here, we have created an empty set my_set of type `int` and added values to it using the `insert()` method.

We checked if **40** and **60** exist in the set my_set by `my_set.count(num)` when num is **40** and **60**.

`my_set.count(num)` returns **1** if `num` exists in `my_set`, otherwise it returns **0**.

---

## Example 4: Delete Elements From a Set

```
#include <iostream>     
#include <set>          
using namespace std;
   
int main () {

    set<int> my_set = {10, 20, 30, 40};
    
    // set before deletion
    cout << "The set before deletion: ";
    for (int i : my_set) {
        cout << i << "  ";
    }

    // delete values from the set
    my_set.erase(10);
    my_set.erase(20);
    
    // set after deletion
    cout << "\nThe set after deletion: ";
    for (int i : my_set) {
        cout << i << "  ";
    }

    // delete all elements from the set
    my_set.clear();

    // set after clearing all elements
    cout << "\nThe set after clearing all elements: ";
    for (int i : my_set) {
        cout << i << "  ";
    }
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

The set before deletion: 10  20  30  40  
The set after deletion: 30  40
The set after clearing all elements:   

Here, we have used the `erase()` method to delete individual set elements.

Then, we used the `clear()` method to delete all elements of the set.

---

## Example 5: C++ Set empty() and size() Methods

In C++, the `empty()` and `size()` methods are called **capacity** methods.

The `empty()` method returns

- **1** (**true**) - if the set is empty
- **0** (**false**) - if the set is not empty

For example,

```
#include <iostream>     
#include <set>          
using namespace std;
   
int main () {

    set<int> my_set = {10, 20, 30};

    // set before clear
    cout << "The set before clear: ";
    for (int i : my_set) {
        cout << i << "  ";
    }
    
    // check if the set is empty
    cout << "\nEmpty: " << my_set.empty() << endl;

    // check the size of the set
    cout << "Size: " << my_set.size() << endl;
    
    // clear values from the set
    my_set.clear();
    
    // set after clear
    cout << "\nThe set after clear: ";
    for (int i : my_set) {
        cout << i << "  ";
    }
    
    // use the capacity methods again
    cout << "\nEmpty: " << my_set.empty() << endl;
    cout << "Size: " << my_set.size() << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

The set before clear: 10  20  30  
Empty: 0
Size: 3

The set after clear: 
Empty: 1
Size: 0

Here, we have used the `empty()` and `size()` methods before and after clearing the contents of the set.

**Before clearing the contents:**

- `empty()` returns **0**, indicating that the set isn't empty
- `size()` returns **3**, indicating that there are three elements in the set

**After clearing the contents:**

- `empty()` returns **1**, indicating that the set is empty
- `size()` returns **0**, indicating that there are no elements in the set

---

**Also Read**

- [C++ Standard Template Library](https://www.programiz.com/cpp-programming/standard-template-library)
- [C++ Unordered Set](https://www.google.com/url?q=/cpp-programming/unordered-set&sa=D&source=docs&ust=1706675737241131&usg=AOvVaw0EqSAA3D7wUVZOUbUeTE6b)
- [C++ Multiset](https://www.google.com/url?q=/cpp-programming/multiset&sa=D&source=docs&ust=1706675737241214&usg=AOvVaw3eA1Lt5sYoHJbWt7lOmPeX)
- [C++ Unordered Multiset](https://www.google.com/url?q=/cpp-programming/unordered-multiset&sa=D&source=docs&ust=1706675737241283&usg=AOvVaw3bk9Ba5s4LeY6_WOkOCa_x)
- [C++ Vector](https://www.programiz.com/cpp-programming/vectors)
- [C++ List](https://www.programiz.com/cpp-programming/list)

- [](https://www.programiz.com/cpp-programming/set#introduction)
- [](https://www.programiz.com/cpp-programming/set#set-properties)
- [](https://www.programiz.com/cpp-programming/set#create-set)
- [](https://www.programiz.com/cpp-programming/set#sort-order)
- [](https://www.programiz.com/cpp-programming/set#set-methods)
- [](https://www.programiz.com/cpp-programming/set#example2)
- [](https://www.programiz.com/cpp-programming/set#example3)
- [](https://www.programiz.com/cpp-programming/set#example4)
- [](https://www.programiz.com/cpp-programming/set#example5)

[

  


](https://www.programiz.com/cpp-programming/map "C++ Map")