# C++ Unordered Multiset

In C++, unordered multisets store elements like a multiset but without any specific order, allowing quick retrieval by value.

Like in a multiset, each element acts as its own key.

---

## Create an Unordered Multiset

To implement a multiset in C++, we must include the `<unordered_set>` header file in our program.

```
#include <unordered_set>
```

We can create an unordered multiset in C++ using the following syntax:

```
// declare an unordered multiset
std::unordered_multiset<data_type> multiset_name = {key1, key2, key3, ...};
```

Here,

- `std::unordered_multiset` - declares an STL container of type `unordered_multiset`.
- `<data_type>` - the data type of the values to be stored in the multiset.
- `multiset_name` - a unique name given to the multiset.
- `key1, key2, key3, ...` - key/value to be stored in the multiset.

For example,

```
// initialize unordered multiset with elements
std::multiset<int> unordered_multiset1 = {5, 3, 8, 1, 3};

// create an empty unordered multiset
std::multiset<int> unordered_multiset2;
```

**Note:** Moving forward, we will be using the `std` namespace so we can omit `std::` from our syntax.

---

### Example 1: Create an Unordered Multiset

```
#include <iostream>
#include <unordered_set>
using namespace std;

int main() {

    unordered_multiset<int> new_multiset = {5, 3, 8, 1, 3};
    
    for(int val : new_multiset) {
        cout << val << " ";
    }
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

1 8 3 3 5 

Here, we have created an unordered multiset of type `int` and we can see that the elements are stored in no particular order.

---

## C++ Unordered Multiset Methods

Here are some commonly used methods that we can use with multisets in C++.

|Function|Description|
|---|---|
|`insert()`|Insert elements into an unordered multiset.|
|`erase()`|Erase all instances of an element.|
|`clear()`|Remove all the elements from a multiset.|
|`empty()`|Check if the multiset is empty.|
|`size()`|Returns the size of the multiset.|
|`found()`|Find the occurrence of a value.|
|`count()`|Count the frequency of a value.|

---

## Example 2: Insert Elements into an Unordered Multiset

We can add values to an unordered multiset using the `insert()` function. For example,

```
#include <iostream>
#include <unordered_set> 
using namespace std;

int main () {

    unordered_multiset<int> my_unordered_multiset; 

    // add values to the unordered_multiset
    my_unordered_multiset.insert(10);
    my_unordered_multiset.insert(30);
    my_unordered_multiset.insert(20);
    my_unordered_multiset.insert(50);
    my_unordered_multiset.insert(40);
    my_unordered_multiset.insert(50);

    // print unordered_multiset after insertion
    for (int i : my_unordered_multiset) {
        cout << i << "  ";
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

40  50  50  20  30  10  

---

## Example 3: Delete Values from an Unordered Multiset

We can use the `erase()` and `clear()` functions to delete from an unordered multiset:

- `erase()` - deletes all instances...
- `clear()` - deletes all elements from the multiset

For example,

```
#include <iostream>
#include <unordered_set> 
using namespace std;

int main () {

    unordered_multiset<int> my_unordered_multiset = {10, 30, 20, 50, 40, 50};

    // delete all occurrences of 50
    my_unordered_multiset.erase(50);
    
    // print unordered_multiset after erase
    cout << "\nThe unordered_multiset after erase: ";
    for (int i : my_unordered_multiset) {
        cout << i << "  ";
    }
    
    // delete all values from the unordered_multiset
    my_unordered_multiset.clear();
    
    // print unordered_multiset after clear
    cout << "\nThe unordered_multiset after clear: ";
    for (int i : my_unordered_multiset) {
        cout << i << "  ";
    }
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

The unordered_multiset after erase: 40  20  30  10  
The unordered_multiset after clear: 

---

## Example 4: C++ empty() and size() Methods

We can use the **capacity methods** `empty()` and `size()` with multisets to check if it is empty and get its size, respectively.

The `empty()` method returns

- **1** (**true**) - if the multiset is empty
- **0** (**false**) - if the multiset is not empty

For example,

```
#include <iostream>
#include <unordered_set>
using namespace std;

int main () {

    unordered_multiset<int> my_unordered_multiset = {10, 20, 20, 20 ,30 , 40};

    // print unordered_multiset before clearing all values
    cout << "The unordered_multiset before clear: ";
    for (int i : my_unordered_multiset) {
        cout << i << "  ";
    }
    
    // check if the unordered_multiset is empty
    cout << "\nEmpty: " << my_unordered_multiset.empty() << endl;

    // check the size of the unordered_multiset
    cout << "Size: " << my_unordered_multiset.size() << endl;
    
    // delete all values from the unordered_multiset
    my_unordered_multiset.clear();
    
    // unordered_multiset after clear
    cout << "\nThe unordered_multiset after clear: ";
    for (int i : my_unordered_multiset) {
        cout << i << "  ";
    }
    
    // use the capacity methods again
    cout << "\nEmpty: " << my_unordered_multiset.empty() << endl;
    cout << "Size: " << my_unordered_multiset.size() << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

The unordered_multiset before clear: 40  30  20  20  20  10  
Empty: 0
Size: 6

The unordered_multiset after clear: 
Empty: 1
Size: 0

---

## Example 4: C++ find() and count() Methods

We use `find()` to check if a given value exists in the multiset and `count()` to check its frequency.

For example,

```
#include <iostream>
#include <unordered_set>
using namespace std;

int main () {

    unordered_multiset<int> my_unordered_multiset = {10, 20, 20, 20 ,30 , 40};

    // print unordered_multiset before searching
    cout << "The unordered_multiset: ";
    for (int i : my_unordered_multiset) {
        cout << i << "  ";
    }

    // find an element in the unordered_multiset
    int target = 20;
    unordered_multiset<int>::iterator it = my_unordered_multiset.find(target);

    if (it != my_unordered_multiset.end()) {
        cout << "\nFound " << target << " in the unordered_multiset." << endl;
    }
    else {
        cout << "\n" << target << " not found in the unordered_multiset." << endl;
    }

    // count occurrences of an element in the unordered_multiset
    int count_value = 20;
    int count_result = my_unordered_multiset.count(count_value);

    cout << count_value << " appears " << count_result << " times in the unordered_multiset." << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

The unordered_multiset: 40  30  20  20  20  10  
Found 20 in the unordered_multiset.
20 appears 3 times in the unordered_multiset.

Notice this code in the above program:

```
if (it != my_unordered_multiset.end()) {
```

The above condition checks whether the value has been found by the `find()` function or not.

If the value is found, the it iterator will point to the element in the multiset that matches the value.

If the value is not found in the multiset, the it iterator will be equal to `my_unordered_multiset.end()`, which indicates that it reached the **end** of the multiset without finding a match.

**Note:** `end()` does not point to an actual element but represents the position after the last element in the multiset.

- [](https://www.programiz.com/cpp-programming/unordered-multiset#introduction)
- [](https://www.programiz.com/cpp-programming/unordered-multiset#example1)
- [](https://www.programiz.com/cpp-programming/unordered-multiset#unordered-multiset-methods)
- [](https://www.programiz.com/cpp-programming/unordered-multiset#example2)
- [](https://www.programiz.com/cpp-programming/unordered-multiset#example3)
- [](https://www.programiz.com/cpp-programming/unordered-multiset#example4)
- [](https://www.programiz.com/cpp-programming/unordered-multiset#example4)

[

  


](https://www.programiz.com/cpp-programming/multiset "C++ Unordered Set")