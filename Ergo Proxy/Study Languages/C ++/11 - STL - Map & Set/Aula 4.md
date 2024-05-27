# C++ Multiset

C++ multisets are STL containers that store elements of the **same type** in **sorted** order, where multiple elements can have **equivalent** **values**. In other words, duplicate values are allowed.

Like C++ sets, the **value** of each element acts as its own **key**.

---

## Multiset Properties

C++ multisets have the following properties:

**Associative:** Elements are referenced by their key and not by their absolute position in the container.

**Sorted:** Elements are stored in a sorted manner.

**Equivalent keys**: Multiple elements in the container can have equivalent keys.

**Immutable:** The value of elements can't be modified after they have been stored in the multiset.

---

## Create a Multiset

To implement a multiset in C++, we must include the `<set>` header file in our program.

```
#include <set>
```

We can create a multiset in C++ using the following syntax:

```
// declare a multiset
std::multiset<data_type> multiset_name = {key1, key2, key3, ...};
```

Here,

- `std::multiset` - declares an STL container of type `multiset`.
- `<data_type>` - the data type of the values to be stored in the multiset.
- `multiset_name` - a unique name given to the multiset.
- `key1, key2, key3, ...` - key/value to be stored in the multiset.

For example,

```
// initialize multiset with elements
std::multiset<int> my_multiset1 = {5, 3, 8, 1, 3};

// create an empty multiset
std::multiset<int> my_multiset2;
```

**Note:** Moving forward, we will be using the `std` namespace so we can omit `std::` from our syntax.

---

### Example 1: Create a Multiset

```
#include <iostream>
#include <set>
using namespace std;

int main() {

    multiset<int> my_multiset = {5, 3, 8, 1, 3};
    
    for(int val : my_multiset) {
        cout << val << " ";
    }
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

1 3 3 5 8

Here, we have created a **multiset** of type `int`.

As you can see, the multiset returned the values in a sorted manner and included the duplicate instances of **3**.

---

## Sort the Multiset in Descending Order

To get the elements of the multiset in descending order, we can modify our syntax as:

```
multiset<int, greater<int>> my_multiset ;
```

For example,

```
#include <iostream>
#include <set>
using namespace std;

int main() {

    multiset<int, greater<int>> my_multiset = {5, 3, 8, 1, 3};
    
    for(int val : my_multiset) {
        cout << val << " ";
    }
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

8 5 3 3 1 

As is evident by the output, the multiset now returns the elements in descending order.

---

## C++ Multiset Methods

In C++, we have various methods to perform various operations in a multiset.

|Operation|Description|
|---|---|
|`insert()`|Insert elements into a multiset.|
|`erase()`|Erase all instances of an element.|
|`clear()`|Remove all the elements from a multiset.|
|`empty()`|Check if the multiset is empty.|
|`size()`|Returns the size of the multiset.|

---

## Example 2: Add Elements to a Multiset

```
#include <iostream>     
#include <set>          
using namespace std;
   
int main () {

    multiset<int> my_multiset;
    
    // add values to the multiset
    my_multiset.insert(10);
    my_multiset.insert(30);
    my_multiset.insert(20);
    my_multiset.insert(50);
    my_multiset.insert(40);
    my_multiset.insert(50);

    // print multiset after insertion
    for (int i : my_multiset) {
        cout << i << "  ";
    }
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

10  20  30  40  50  50  

As you can see, `insert()` in multiset is the same as in [sets](https://programiz.com/cpp-programming/set).

---

## Example 3: Remove Elements From a Multiset

```
#include <iostream>     
#include <set>          
using namespace std;
   
int main () {

    multiset<int> my_multiset = {10, 30, 20, 50, 40, 50};

    // delete all occurences of 50 from the multiset
    my_multiset.erase(50);
    
    // print multiset after erase
    cout << "\nThe multiset after erase: ";
    for (int i : my_multiset) {
        cout << i << "  ";
    }
    
    // delete all values from the multiset
    my_multiset.clear();
    
    // print multiset after clear
    cout << "\nThe multiset after clear: ";
    for (int i : my_multiset) {
        cout << i << "  ";
    }
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

The multiset after erase: 10  20  30  40  
The multiset after clear: 

As you can see, `clear()` operates the same way in multiset as it does in set and deletes all values.

On the other hand, the `erase()` method deletes every instance of the given value from the multiset.

```
// delete all values from the multiset
my_multiset.erase(50);
```

In our case, both instances of **50** were deleted from my_multiset.

---

## Example 4: C++ Multiset empty() and size() Methods

We can use the **capacity methods** `empty()` and `size()` with multisets to check if it is empty and get its size, respectively.

The `empty()` method returns

- **1** (**true**) - if the multiset is empty
- **0** (**false**) - if the multiset is not empty

For example,

```
#include <iostream>     
#include <set>          
using namespace std;
   
int main () {

    multiset<int> my_multiset = {10, 20, 20, 20 ,30 , 40};

    // print multiset before clearing all values
    cout << "The multiset before clear: ";
    for (int i : my_multiset) {
        cout << i << "  ";
    }
    
    // check if the multiset is empty
    cout << "\nEmpty: " << my_multiset.empty() << endl;

    // check the size of the multiset
    cout << "Size: " << my_multiset.size() << endl;
    
    // delete all values from the multiset
    my_multiset.clear();
    
    // multiset after clear
    cout << "\nThe multiset after clear: ";
    for (int i : my_multiset) {
        cout << i << "  ";
    }
    
    // use the capacity methods again
    cout << "\nEmpty: " << my_multiset.empty() << endl;
    cout << "Size: " << my_multiset.size() << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

The multiset before clear: 10  20  20  20  30  40  
Empty: 0
Size: 6

The multiset after clear: 
Empty: 1
Size: 0

Here, we have used the `empty()` and `size()` methods before and after clearing the contents of the multiset.

**Before clearing the contents:**

- `empty()` returns **0**, indicating that the multiset isn't empty.
- `size()` returns **6**, indicating that there are six elements in the multiset.

**After clearing the contents:**

- `empty()` returns **1**, indicating that the multiset is empty.
- `size()` returns **0**, indicating that there are no elements in the multiset.