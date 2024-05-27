# C++ Multimap

C++ multimap is an associative container in the Standard Template Library (STL) that provides the functionality of a [map](https://www.programiz.com/cpp-programming/map) but allows multiple elements to have equivalent keys.

---

## Create C++ Multimap

In order to create a multimap in C++, we first need to include the `<map>` header file.

```
#include <map>
```

Once we import this file, we can create a multimap using the following syntax:

```
std::multimap<key_type, value_type> multimap_name = {
    {key1, value1},
    {key2, value2},
    ...
};
```

Here,

- `key_type` - the data type for the key
- `value_type` - the data type for the value
- `{key1, value1}, {key2, value2}, ...` - the key-value pairs to be assigned to the multimap

**Note:** We'll be using the `std` namespace in our tutorial. So, we can simply write `multimap` instead of `std::multimap`.

For example,

```
// create a multimap with int key and string value
multimap<int, string> my_multimap = {
    {1, "One"},
    {1, "Uno"},
    {2, "Two"},
};
```

This creates a multimap named my_multimap where the keys are of type `int` and the values are of type `string`.

---

### Example: C++ Multimap

```
#include <iostream>
#include <map>
using namespace std;

int main() {

    // create a multimap
    multimap<int, string> my_multimap = {
        {1, "Un"},
        {1, "One"},
        {2, "Two"},
        {2, "Dos"},
        {1, "Uno"},
        {2, "Deux"}
    };

    cout << "Key - Value" << endl;

    // loop across the multimap
    // display the key-value pairs
    for(const auto& key_value: my_multimap) {
        int key = key_value.first;
        string value = key_value.second;

        cout << key << " - " << value << endl;
  }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Key - Value
1 - Un
1 - One
1 - Uno
2 - Two
2 - Dos
2 - Deux

In the above example, we have declared and initialized a multimap named my_multimap.

Notice that the multimap has been sorted by its keys and not by the order of insertion.

**Note**: Insertion order is only maintained for elements with identical keys.

Then, we displayed the contents of the multimap using a [ranged for loop](https://www.programiz.com/cpp-programming/ranged-for-loop).

```
for(const auto& key_value: my_multimap) {
    int key = key_value.first;
    string value = key_value.second;    
    cout << key << " - " << value << endl;
}
```

In the above code, each element (key-value pair) of the multimap is stored in the variable key_value.

Then, we get the key and value using:

- `key_value.first` - gives the key
- `key_value.second` - gives the value

---

## C++ Multimap Methods

In C++, the `multimap` class provides various methods to perform different operations on a multimap.

|Methods|Description|
|---|---|
|`insert()`|inserts one or more key-value pairs|
|`count()`|returns total number of occurrences of the specified key|
|`find()`|returns the iterator to the element with the specified key|
|`size()`|returns the number of elements|
|`empty()`|returns true if the multimap is empty|
|`erase()`|removes elements with specified key|
|`clear()`|removes all elements|

---

## Insert Into a Multimap

We can insert a **key-value** pair in a multimap using the `insert()` method. For example,

```
#include <iostream>
#include <map>
using namespace std;

int main() {

    multimap<string, int> numbers;

    // insert a pair {"Odd", 1}
    numbers.insert({"Odd", 1});

    // insert multiple pairs
    numbers.insert({{"Even", 2}, {"Even", 6}, {"Odd", 5}, {"Even", 4}});

    cout << "Key - Value" << endl;

    // display numbers   
    for(const auto& key_value: numbers) {
        string key = key_value.first;
        int value = key_value.second;
        cout << key << " - " << value << endl;
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Key - Value
Even - 2
Even - 6
Even - 4
Odd - 1
Odd - 5

---

## Remove Elements From a Multimap

We can use the following methods to remove elements from a multimap:

- `erase()` - remove the element with the specified key
- `clear()` - remove all multimap elements

For example,

```
#include <iostream>
#include <map>
using namespace std;

// function prototype for display_multimap()
void display_multimap(const multimap<int, string> &);

int main() {

    multimap<int, string> student {
        {111, "John"},
        {132, "Mark"},
        {143, "Chris"},
        {143, "Christopher"}
    };
  
    cout << "Initial Multimap:" << endl;
    display_multimap(student);

    // remove element with key: 143  
    student.erase(143);
  
    cout << "\nMultimap After Erasing Key 143: " << endl;
    display_multimap(student);

    // remove all multimap elements
    student.clear();

    cout << "\nMultimap After Clearing: " << endl;
    display_multimap(student);

    return 0;
}

// function to print multimap elements
void display_multimap(const multimap<int, string> &umap){

    for(const auto& key_value: umap) {
        int key = key_value.first;
        string value = key_value.second;
    
        cout << key << " - " << value << endl;
    }
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Initial Multimap:
111 - John
132 - Mark
143 - Chris
143 - Christopher

Multimap After Erasing Key 143: 
111 - John
132 - Mark

Multimap After Clearing: 

In the above example, we have used the `erase()` method to remove the elements with the key **143** from the multimap.

Then, we used the `clear()` method to remove all the elements of the multimap.

---

## Check the Size of a Multimap

We can check if a multimap is empty using the `empty()` method and calculate its size using `size()` method.

The `empty()` method returns

- **true** - if the multimap is empty.
- **false** - if the multimap isn't empty.

And, the `size()` method returns the number of elements in the multimap. For example,

```
#include <iostream>
#include <map>
using namespace std;

int main() {

    multimap<string, int> my_multimap;
    
    // check capacity before insertion
    string result = my_multimap.empty()? "Yes" : "No";
    int multimap_size =  my_multimap.size();

    cout << "Before Insertion";
    cout << "\nIs multimap empty? " << result << endl;
    cout << "multimap size: " << multimap_size << endl;
        
    // insert element
    my_multimap.insert({"apple",2});
    
    // check capacity after insertion
    result = my_multimap.empty()? "Yes" : "No";
    multimap_size = my_multimap.size();

    cout << "\nAfter Insertion" << endl;
    cout << "\Is multimap empty? " << result << endl;
    cout << "multimap size: " << multimap_size << endl;
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Before Insertion
Is multimap empty? Yes
multimap size: 0

After Insertion
Is multimap empty? No
multimap size: 1

Here, using the [ternary operator](https://www.programiz.com/cpp-programming/ternary-operator), the result variable stores the string

- `Yes` if the multimap is empty (i.e., when `empty()` returns `true`)
- `Yes` if the multimap is not empty (i.e., when `empty()` returns `false`)

---

## Find a Key in a Multimap

We can use the `find()` function to find elements with a particular key.

The `find()` function returns

- iterator to the element if the **key is found**
- iterator to the end of the container (the `end()` iterator) if the **key is not found**

For example,

```
#include <iostream>
#include <map>
using namespace std;

int main() {

    multimap<string, int> my_multimap;

    my_multimap.insert({"apple", 5});
    my_multimap.insert({"banana", 3});
    my_multimap.insert({"apple", 2});
    my_multimap.insert({"cherry", 4});

    // find elements with the key "apple"
    string key_to_find = "apple";
    auto found = my_multimap.find(key_to_find);

    // print the found key
    if (found != my_multimap.end()) {
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

As can be seen from the example, the `find()` method returns only the first instance of the key from the multimap.

---

## Check if a Key Exists in the Multimap

We can use the following methods to check if the specified key exists in the multimap.

- `find()` - returns an iterator to the element if the key is found, else returns the `end()` iterator
- `count()` - returns total number of occurrences of specified key

For example,

```
#include <iostream>
#include <map>
using namespace std;

int main() {

    multimap<int, string> students {
        {20, "Chris"},
        {28, "Joseph"},
        {20, "Blake"}
    };

    cout << "Using count():" << endl;
    cout << "Does age " << 20 << " exist? ";

    // count() returns the number of occurences of the specified key
    int count_20 = students.count(20);

    if (count_20) {
        cout << "Yes";
        cout << "\nTotal Students with age 20 = " << count_20 << endl;
    }
    else {
        cout << "No";
    }

    cout << "\nUsing find():" << endl;
    cout << "Does age " << 27 << " exist? ";

    // find() returns students.end()
    // if the key is not found 
    if (students.find(27) != students.end()) {
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

Using count():
Does age 20 exist? Yes
Total Students with age 20 = 2

Using find():
Does age 27 exist? No

In the above example, we have used the `find()` and `count()` methods to check if a given key exists in the multimap.

Initially, we have used the `count()` method to find the total number of times the key **20** appears.

```
int count_20 = students.count(20);
```

Then, we have used the `find()` method to check if the key **27** exists.

```
if (students.find(27) != students.end()) {
    cout << "Yes";
}
else {
    cout << "No";
}
```