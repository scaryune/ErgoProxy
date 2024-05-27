# C++ Unordered Map

In C++, the STL `unordered_map` is an [unordered associative container](https://www.programiz.com/cpp-programming/stl-containers#unordered-associative-container) that provides the functionality of an unordered map or dictionary data structure.

In contrast to a regular map, the order of keys in an unordered map is undefined.

Also, the unordered map is implemented as a [hash table](https://www.programiz.com/dsa/hash-table) data structure whereas the regular map is a [binary search tree](https://www.programiz.com/dsa/binary-search-tree) data structure.

---

## Create C++ STL unordered_map

In order to create an unordered map in C++, we first need to include the `unordered_map` header file.

```
#include <unordered_map>
```

Once we import this file, we can create an unordered map using the following syntax:

```
unordered_map<key_type, value_type> ump;
```

Here,

- `key_type` indicates the data type for the **key**
- `value_type` indicates the data type for the **value**

For example,

```
// create an unordered_map with integer key and value
unordered_map<int, int> ump_integer;

// create an unordered_map with string key and int value
unordered_map<string, int> ump_string;
```

---

## Initialize an Unordered Map

We can initialize a C++ unordered map in the following ways:

```
// Initializer List 
unordered_map<string, int> unordered_map1 = {
  {"One", 1},
  {"Two", 2},
  {"Three", 3}
};

// Uniform Initialization
unordered_map<string, int> unordered_map2 {
  {"One", 1},
  {"Two", 2},
  {"Three", 3}
};
```

Here, we have initialized the unordered map by providing values directly to them.

Now, both unordered_map1 and unordered_map2 are initialized with `{{"One", 1}, {"Two", 2}, {"Three", 3}}`.

---

### Example: C++ unordered_map

```
#include <iostream>
#include <unordered_map>
using namespace std;

int main() {

  // uniform initialization
  unordered_map<string, int> unordered_map1  {
  {"One", 1},
  {"Two", 2},
  {"Three", 3}
 };

  cout << "Key - Value" << endl;

  // loop across the unordered map
  // display the key-value pairs
  for(const auto& key_value: unordered_map1) {
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
Three - 3
Two - 2
One - 1

In the above example, we have declared and initialized an unordered map named unordered_map1 using uniform initialization.

```
unordered_map<string, int> unordered_map1 {
  {"One", 1},
  {"Two", 2},
  {"Three", 3}
};
```

Then, we have displayed the unordered map content using a [ranged for loop](https://www.programiz.com/cpp-programming/ranged-for-loop).

```
for(const auto& key_value: unordered_map1) {
  string key = key_value.first;
  int value = key_value.second;    
  cout << key << " - " << value << endl;
}
```

In the above code, each element (key-value pair) of the unordered map is stored in variable key_value.

Then, we get the key and value using:

- `key_value.first` - gives the key
- `key_value.second` - gives the value

Notice that we have created the unordered map in order of the keys: `"One"`, `"Two"`, `"Three"`. However, the output is in undefined order.

This is because the elements are not stored in any particular order based on key, or the values.

**Note:** Starting from C++17, you can use **structure bindings** to simplify this code further:

```
for(const auto& [key, value]: unordered_map1) {
  cout << key << " -  " << value << endl; 
}
```

---

## Other Ways to Initialize a C++ Unordered Map

Copy one unordered map to another.

---

## C++ Unordered Map Methods

In C++, the `unordered_map` class provides various methods to perform different operations on an unordered map.

|Methods|Description|
|---|---|
|`insert()`|insert one or more key-value pairs|
|`count()`|returns **1** if key exists and **0** if not|
|`find()`|returns the iterator to the element with the specified key|
|`at()`|returns the element at the specified key|
|`size()`|returns the number of elements|
|`empty()`|returns true if the unordered map is empty|
|`erase()`|removes elements with specified key|
|`clear()`|removes all elements|

---

## Insert Key-Value Pairs to an Unordered Map

We can insert a **key-value** pair in an unordered map using :

- `insert()` - insert key-value pairs
- `[]` - insert a key and value

For example,

```
#include <iostream>
#include <unordered_map>
using namespace std;

int main() {

  unordered_map<string, int> unordered_map1;
  
  // insert key-value pair {"One", 1}
  unordered_map1["One"] = 1;

  // insert a pair {"Two", 2}
  unordered_map1.insert({"Two", 2});

  // insert two pairs {"Three", 3}, {"Four", 4}	
  unordered_map1.insert({{"Three", 3}, {"Four", 4}});
  
  cout << "Key - Value" << endl;

  // display elements of unordered_map1   
  for(const auto& key_value: unordered_map1) {
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
Four - 4
Two - 2
Three - 3
One - 1

In the above example, we have initialized an empty unordered map to store the key-value pairs of a string and an integer.

Then, we have inserted the pair `{"One", 1}` using `[]`.

```
unordered_map1["One"] = 1;
```

We have then inserted another pair using the `insert()` method.

```
unordered_map1.insert({"Two", 2});
```

Finally, we inserted two pairs using `insert()`.

```
unordered_map1.insert({{"Three", 3}, {"Four", 4}});
```

---

## Access Values of Unordered Maps

We can use the following methods to access the values of the specified key of an unordered map:

- `at()` - returns value for the specified key
- `[]` - returns value for the specified key

For example,

```
#include <iostream>
#include <unordered_map>
using namespace std;

int main() {

  unordered_map<string, string> capital_city {
    {"Nepal", "Kathmandu"},
    {"India", "New Delhi"},
    {"Australia", "Canberra"}
  };
  
  cout << "Capital of Nepal is " << capital_city["Nepal"] << endl;
  cout << "Capital of Australia is " << capital_city.at("Australia");
  
  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Capital of Nepal is Kathmandu
Capital of Australia is Canberra

In the above example,

- `capital_city["Nepal"]` - returns the element with key `"Nepal"`
- `capital_city.at("Australia")` - returns the element with key `"Australia"`

**Note:** While we can use the `[]` operator to access the elements, it is preferable to use the `at()` method.

This is because `at()` throws an exception whenever the specified key doesn't exist, while `[]` pairs the key with a garbage value.

For example,

```
// key "Japan" doesn't exist
// so the key "Japan" is paired with a garbage value
cout << "Capital of Japan is: " << capital_city["Japan"];
```

---

## Change Values of an Unordered Map

We can use the `at()` method or the `[]` operator to change the value of the unordered map. For example,

```
#include <iostream>
#include <unordered_map>
using namespace std;

int main() {

  unordered_map<string, string> capital_city {
    {"India", "Calcutta"},
    {"Pakistan", "Karachi"},
  };
  
  cout << "Old Capitals:" << endl;
  cout << "India : " << capital_city["India"] << endl;
  cout << "Pakistan : " << capital_city["Pakistan"];
 
  // change value for "India" using []
  capital_city["India"] = "New Delhi";

  // change value for "Pakistan" using at()
  capital_city.at("Pakistan") = "Islamabad";
  
  cout << "\n\nNew Capitals:" << endl;
  cout << "India : " << capital_city["India"] << endl;
  cout << "Pakistan : " << capital_city["Pakistan"];
  
  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Old Capitals: 
India : Calcutta
Pakistan : Karachi

New Capitals: 
India : New Delhi
Pakistan : Islamabad

In the above example, the initial key-value pairs for capital_city are `{"India", "Calcutta"}` and `{"Pakistan", "Karachi"}`.

Then, we have used the `[]` operator to change the value for key `"India"` using:

```
capital_city["India"] = "New Delhi";
```

Similarly, we have used the `at()` method to change the value for the key `"Pakistan"` using:

```
capital_city.at("Pakistan") = "Islamabad";
```

---

## Remove Elements From an Unordered Map

We can remove the element with the specified key of an unordered map using the `erase()` method. For example,

```
#include <iostream>
#include <unordered_map>
using namespace std;

// function prototype for display_unordered_map()
void display_unordered_map(const unordered_map<int, string> &);

int main() {

  unordered_map<int, string> student {
    {111, "John"},
    {132, "Mark"},
    {143, "Chris"}
  };
  
  cout << "Initial Unordered Map:\n";
  display_unordered_map(student);

  // remove element with key: 143  
  student.erase(143);
  
  cout << "\nFinal Unordered Map: \n";
  display_unordered_map(student);

  return 0;
}

// utility function to print unordered_map elements
void display_unordered_map(const unordered_map<int, string> &umap){

  for(const auto& key_value: umap) {
    int key = key_value.first;
    string value = key_value.second;
    
    cout << key << " - " << value << endl;
  }
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Initial Unordered Map:
143 - Chris
132 - Mark
111 - John

Final Unordered Map: 
132 - Mark
111 - John

In the above example, we have used the `erase()` method to remove an element from the unordered map.

Initially, the content of unordered map named student is `{{"143": Chris}, {"132": Mark}, {"111": John}}`.

Then we have used the `erase()` method to remove the element with key **143**.

```
// removes element with the key 143
student.erase(143);
```

So the final content becomes `{{"132": Mark}, {"111": John}}`.

**Note:** We can use the `clear()` method to remove all the elements of the unordered map.

---

## Check if a Key Exists in the Unordered Map

We can use the following methods to check if the specified key exists in the unordered map.

- `find()` - returns the iterator to the element if the key is found, else returns the `end()` iterator
- `count()` - returns **1** if the key exists and **0** if not

For example,

```
#include <iostream>
#include <unordered_map>
using namespace std;

int main() {

  unordered_map<int, string> student{
      {111, "John"},
      {132, "Mark"},
      {143, "Chris"}
  };

  cout << "Using find():" << endl;
  cout << "Does id " << 143 << " exist? ";

  // find() returns student.end() if the key is not found 
  if (student.find(143) != student.end()) {
    cout << "Yes";
  }
  else {
    cout << "No";
  }

  cout << "\n\nUsing count():" << endl;
  cout << "Does id " << 1433 << " exist? ";

  // count() returns 0 if the key doesn't exist
  if (student.count(1433)) {
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

Using find():
Does id 143 exist? Yes

Using count():
Does id 1433 exist? No

In the above example, we have used `find()` and `count()` to check if a given key exists in the unordered map.

Initially, we have used the `find()` method to check if the key **143** exists.

```
// checks if key 143 exists
if (student.find(143) != student.end()) {
  cout << "Yes";
}
else {
  cout << "No";
}
```

The `find()` method returns an iterator pointing to the element if it exists. If the key doesn't exist, it points to the `end()` iterator.

Then, we have used the `count()` method to check if the key **1433** exists.

```
// checks if key 1433 exists
if (student.count(1433)) {
  cout << "Yes";
}
else {
  cout << "No";
}
```