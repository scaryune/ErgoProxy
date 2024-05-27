# C++ Unordered Multimap

C++ unordered multimaps are STL [multimaps](http://programiz.com/cpp-programming/multimap), where the elements aren't stored in any sorted order.

Elements in an unordered multimap are not sorted based on their keys or values. Instead, they are organized into **buckets** using **hash** values for quick direct access by key, resulting in constant average time complexity.

The data type of key and value may differ.

---

## Create an Unordered Multimap

In order to create an unordered multimap in C++, we first need to include the `<unordered_map>` header file.

```
#include <unordered_map>  
```

The syntax for initializing an unordered multimap is

```
std::unordered_multimap<int, std::string> my_unordered_multimap;
```

This will create an unordered multimap named my_unordered_multimap to store **key-value** pairs, where the key type is `int` and the value type is `std::string`.

**Note:** We will be using the `std` namespace throughout the tutorial. So, the syntax will not contain `std`.

```
unordered_multimap<int, string> my_unordered_multimap;
```

---

### Example: C++ Unordered Multimap

```
#include <iostream>
#include <unordered_map>  
using namespace std;

int main() {

    // create an unordered_multimap
    // with integer keys and string values
    unordered_multimap<int, string> my_unordered_multimap {
        {1, "Apple"},
        {22, "Banana"},
        {1, "Apricot"},
        {3, "Avocado"}
    };

    // print the elements
    cout << "Unordered Multimap Elements:" << endl;
    for (const auto& pair : my_unordered_multimap) {
        cout << pair.first << ": " << pair.second << endl;
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Unordered Multimap Elements:
3: Avocado
22: Banana
1: Apricot
1: Apple

Here, we have created an **unordered multimap** named my_unordered_multimap which has two elements sharing the same key **1**.

As you can see, the elements aren't stored in a sorted order.

Notice the code,

```
for (const auto& pair : my_unordered_multimap) {
    cout << pair.first << ": " << pair.second << endl;
}
```

Here, the loop variable pair stores the **key-value** pairs present in my_unordered_multimap. We can then access the **key** using `pair.first` and the **value** using `pair.second`.

---

## C++ Unordered Multimap Methods

Some of the most commonly used methods for unordered multimaps are listed below:

|Methods|Description|
|---|---|
|`insert()`|Inserts elements into the multimap.|
|`find()`|Finds the value of the given key.|
|`count()`|Counts the number of elements with a specific key.|
|`empty()`|Checks if the multimap is empty.|
|`size()`|Check the size of the multimap.|
|`erase()`|Deletes an element from the multimap.|
|`clear()`|Deletes all values from the multimap.|

---

## Add elements to an Unordered Multimap

We can add elements to an unordered multimap using the `insert()` function. For example,

```
#include <iostream>
#include <unordered_map>
using namespace std;

int main() {

    unordered_multimap<string, int> my_unordered_multimap;

    // insert single key-value pairs
    my_unordered_multimap.insert({"apple", 5});
    my_unordered_multimap.insert({"banana", 3});

    // insert multiple key-value pairs
    my_unordered_multimap.insert({{"apple", 2}, {"cherry", 4}});


    // print the unordered multimap
    cout << "Elements inserted into unordered multimap:" << endl;
    for (const auto& pair : my_unordered_multimap) {
        cout << pair.first << " -> " << pair.second << endl;
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Elements inserted into unordered multimap:
cherry -> 4
banana -> 3
apple -> 5
apple -> 2

---

## Find a Key in an Unordered Multimap

We can use the `find()` function to find elements with a particular key.

The `find()` function returns

- iterator to the element if the **key is found**
- iterator to the end of the container if the **key is not found**

For example,

```
#include <iostream>
#include <unordered_map>
using namespace std;

int main() {

    unordered_multimap<string, int> my_unordered_multimap;

    my_unordered_multimap.insert({"apple", 5});
    my_unordered_multimap.insert({"banana", 3});
    my_unordered_multimap.insert({"apple", 2});
    my_unordered_multimap.insert({"cherry", 4});

    // find elements with the key "apple"
    string key_to_find = "apple";
    auto found = my_unordered_multimap.find(key_to_find);

    // print the found key
    if (found != my_unordered_multimap.end()) {
        cout << "Found key " << key_to_find << ": " << endl;
        cout << found->first << " - " << found->second << endl;
    }
    else {
        cout << "Key " << key_to_find << " not found." << endl;
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Found key apple: 
apple - 5

As can be seen from the example, the `find()` function returns only the first instance of the key from the multimap.

---

## Count the Occurrences of a Key

We can count the number of occurrences of a specific key using the `count()` function. For example,

```
#include <iostream>
#include <unordered_map>

using namespace std;

int main() {

    unordered_multimap<string, int> my_unordered_multimap;

    my_unordered_multimap.insert({"apple", 5});
    my_unordered_multimap.insert({"banana", 3});
    my_unordered_multimap.insert({"apple", 2});
    my_unordered_multimap.insert({"cherry", 4});

    // count the number of elements with a specific key
    string key_to_count = "apple";
    int count = my_unordered_multimap.count(key_to_count);
    cout << "Count of key " << key_to_count << ": " << count << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Count of key apple: 2

Here, we have used the `count()` function to count the number of values with the key `apple`. The function returns the value **2**, which means that there are two values with this key.

---

## Check the Size of an Unordered Multimap

We can check if a multimap is empty using the `empty()` function and calculate its size using `size()` function.

The `empty()` function returns

- **true** - if the multimap is empty.
- **false** - if the multimap isn't empty.

And, the `size()` function returns the number of elements in the multimap. For example,

```
#include <iostream>
#include <unordered_map>
using namespace std;

int main() {

    unordered_multimap<string, int> my_unordered_multimap;
    
    // check capacity before insertion
    string result = my_unordered_multimap.empty()? "Yes" : "No";
    int multimap_size =  my_unordered_multimap.size();

    cout << "Before Insertion";
    cout << "\nIs unordered_multimap empty? " << result << endl;
    cout << "unordered_multimap size: " << multimap_size << endl;
        
    // insert element
    my_unordered_multimap.insert({"apple",2});
    
    // check capacity after insertion
    result = my_unordered_multimap.empty()? "Yes" : "No";
    multimap_size = my_unordered_multimap.size();

    cout << "\nAfter Insertion" << endl;
    cout << "\Is unordered_multimap empty? " << result << endl;
    cout << "unordered_multimap size: " << multimap_size << endl;
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Before Insertion
Is unordered_multimap empty? Yes
unordered_multimap size: 0

After Insertion
Is unordered_multimap empty? No
unordered_multimap size: 1

Here, using the [ternary operator](https://www.programiz.com/cpp-programming/ternary-operator), the result variable stores the string

- `Yes` if the multimap is empty (i.e., when `empty()` returns `true`)
- `Yes` if the multimap is not empty (i.e., when `empty()` returns `false`)

---

## Delete Elements From an Unordered Multimap

We can use the following functions to delete elements from an unordered multimap:

- `erase()` - deletes all instances of a key from the multimap
- `clear()` - deletes every element from the multimap

```
#include <iostream>
#include <unordered_map>
using namespace std;

int main() {

    unordered_multimap<string, int> my_unordered_multimap;

    my_unordered_multimap.insert({"apple", 5});
    my_unordered_multimap.insert({"banana", 3});
    my_unordered_multimap.insert({"apple", 2});
    my_unordered_multimap.insert({"cherry", 4});

    // erase elements with the key "apple"
    string key_to_erase = "apple";
    my_unordered_multimap.erase(key_to_erase);

    cout << "Elements after erasing key " << key_to_erase << ":" << endl;
    for (const auto& pair : my_unordered_multimap) {
        cout << pair.first << " -> " << pair.second << endl;
    }

    // clear the entire unordered_multimap
    my_unordered_multimap.clear();

    cout << "Elements after clearing:" << endl;
    for (const auto& pair : my_unordered_multimap) {
        cout << pair.first << " -> " << pair.second << endl;
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Elements after erasing key apple:
cherry -> 4
banana -> 3
Elements after clearing: