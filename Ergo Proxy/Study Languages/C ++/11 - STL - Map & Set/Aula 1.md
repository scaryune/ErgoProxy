# C++ Map

In C++, maps are associated containers that hold pairs of data.

These pairs, known as **key-value** pairs, have a unique key, while the associated values don't have to be unique.

![A map named student with integer-type keys and string-type values](https://www.programiz.com/sites/tutorial2program/files/cpp-map.png "A map named student")

A map named student

The elements in a map are internally sorted by their **keys**.

In order to use maps in C++, we must include the `map` header file in our program:

```
#include <map>
```

---

## Create a Map

We can declare a map using the following syntax:

```
std::map<key_type, value_type> map_name = {{key1, value1},{key2, value2}, ...};
```

Here,

- `std::map` - declares an [STL container](https://www.programiz.com/cpp-programming/stl-containers) of type `map`
- `<key_type>` - the data type of the keys to be stored in the map
- `<value_type>` - the data type of the values to be stored in the map
- `map_name` - a unique name given to the map
- `key1, key2, ...` - keys to be stored in the map
- `value1, value2, ...` - values to be stored in the map

Let's see an example,

```
// create a map with integer keys and string values
std::map<int, string> student = {{1,"Jacqueline"}, {2,"Blake"}, {3,"Denise"}};
```

**Note:** We can also initialize map elements without using the assignment operator `=`. For example,

```
std::map<int, string> student {{1,"Jacqueline"}, {2,"Blake"}, {3,"Denise"}};
```

---

## Map Methods

In C++, the `map` [class](https://www.programiz.com/cpp-programming/object-class) provides various methods to perform different operations on a map.

|Operation|Description|
|---|---|
|`insert()`|adds an element (key-value pair) to the map|
|`erase()`|removes an element or range of elements from the map|
|`clear()`|removes all the elements from the map|
|`find()`|searches the map for the given key|
|`size()`|returns the number of elements in the map|
|`empty()`|returns `true` if the map is empty|

---

## Add Values in a Map

We can use the `[]` operator to add key-value pairs to a map. For example,

```
// create a map with integer keys and string values
std::map<int, string> student;

// add element with key 1 and value "Jacqueline"
student[1] = "Jacqueline";

// add element with key 2 and value "Blake"
student[2] = "Blake";
```

We can also use the `insert()` function alongside the `make_pair()` function to insert elements into the map. For example,

```
student.insert(std::make_pair(3, "Denise"));
```

We can generalize the above two methods into the following syntaxes:

```
// using the [] operator
map_name[key] = value;

// using the insert() and make_pair() functions
map_name.insert(std::make_pair(key, value));
```

---

### Example 1: C++ Maps

```
#include <iostream>
#include <map>
using namespace std;

int main() {
    
    map<int, string> student;
  
    // use [] operator to add elements
    student[1] = "Jacqueline";
    student[2] = "Blake";

    // use insert() method to add elements
    student.insert(make_pair(3, "Denise"));
    student.insert(make_pair(4, "Blake"));

    // add elements with duplicate keys
    student[5] = "Timothy";
    student[5] = "Aaron";

    for (int i = 1; i <= student.size(); ++i) {
        cout << "Student[" << i << "]: " << student[i] << endl;
    }

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Student[1]: Jacqueline
Student[2]: Blake
Student[3]: Denise
Student[4]: Blake
Student[5]: Aaron

In this program, we have created a map named student that stores `int` keys and `string` values.

Notice that we have two duplicate **values** (`"Blake"`) in our program, which is **valid.**

However, we also have two duplicate **keys** (**5**) in our program, which is **invalid.**

Here, since both `"Timothy"` and `"Aaron"` share the same **key**, only one of the values is allowed to be stored.

First, `"Timothy"` is paired with the key **5** in student. Then, when `"Aaron"` is paired with **5**, `"Timothy"` is overwritten.

We then use a [for](https://www.programiz.com/cpp-programming/for-loop) [loop](https://www.programiz.com/cpp-programming/for-loop) to print all the map elements.

**Note:** When we use `cout` to print a map element directly, we only print the corresponding map **value**, not its **key**.

```
// Output: Jacqueline
cout << student[1];
```

---

## Access Keys and Values

We can access the keys and values of our map with the help of map [iterators](https://www.programiz.com/cpp-programming/iterators). For example,

```
#include <iostream>
#include <map>
using namespace std;

int main() {

    map<int, string> student;

    student[1] = "Jacqueline";
    student[2] = "Blake";
    student[3] = "Denise";
    student[4] = "Aaron";

    // declare map iterator
    map<int, string>::iterator iter;

    // use iterator to display map elements
    for (iter = student.begin(); iter != student.end(); ++iter) {
        cout << iter->first << " - " << iter->second << endl;
    }

    return 0;  
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

1 - Jacqueline
2 - Blake
3 - Denise
4 - Aaron

In the above example, we have used a custom iterator iter to access the keys and values of the student map. The **key** is given by the `first` object, and the **value** by the `second` object.

Notice that we have used a `for` loop with the iter iterator to display all the elements of student.

```
for (iter = student.begin(); iter != student.end(); ++iter) {
    cout << iter->first << " - " << iter->second << endl;
}
```

Here,

- `begin()` - returns an iterator that points to the first element of the map
- `end()` - returns an iterator that points to the theoretical element following the last element of the map

We have used the `->` operator with iter to access the `first` and `second` objects.

Alternatively, we can also **dereference** iter and use the `.` operator to access `first` and `second` objects.

```
// Output: 1
cout << (*iter).first << " - ";

// Output: Jacqueline
cout << (*iter).second;
```

**Note**: The `*` operator dereferences iterators for direct access to map elements.To learn more, visit [C++ Pointers](https://www.programiz.com/cpp-programming/pointers).

---

## C++ find() Function for Maps

We can search for keys in a map using the `find()` function. Its syntax is

```
map_name.find(key);
```

For example,

```
map<int, string> student;
map<int, string>::iterator iter;

student[1] = "Jacqueline";
student[2] = "Blake";

// find the key 2 in the student map
// store the return value in iter
iter = student.find(2);
```

In the example above, we have used the `find()` function to search for the element of student that contains the key **2.**

Now, the `find()` function returns:

- an iterator pointing to the element if the element exists
- an iterator pointing to the end of the map, i.e., `student.end()` if the element doesn't exist.

**Note**: To learn more, visit [C++ functions](https://www.programiz.com/cpp-programming/function).

---

## Delete Elements from C++ Maps

We can delete map elements with the `erase()` and `clear()` functions.

Let's talk about the `clear()` function first.

---

### C++ clear() Function for Maps

The `clear()` function deletes all the elements of the map. For example,

```
map<int, string> student;
student[1] = "Jacqueline";
student[2] = "Blake";

cout << student.size();    // Output: 2

student.clear();

cout << student.size();    // Output: 0
```

---

### C++ erase() Function for Maps

We can use the `erase()` function to delete individual elements either with the help of iterators or with keys.

Suppose we have a map named student_rank as follows:

```
map <string, int> student_rank {{"Josh", 2}, {"Rachel", 4}, {"Betty", 6}};
```

Now, we can delete elements of this map in the following ways:

**1. erase() Using a Key**

```
// delete element with key "Rachel" from the map
student_rank.erase("Rachel");
```

**2. erase() Using an Iterator**

```
// initialize an iterator pointing to the beginning of the map
map <string, int>::iterator itr = student_rank.begin();

// increment the iterator to point to the second element
itr++;
    
// delete the second element
student_rank.erase(itr);
```

---

### Example 2: erase() to Remove Individual Elements

```
#include <iostream>
#include <map>
using namespace std;

int main() {
    
    // create a map named student
    map <int, string> student {{1, "Denise"}, {2, "Blake"}, {3, "Courtney"}, {4, "John"}, {5, "Jennifer"}};
    
    // create map iterator
    map <int, string>::iterator itr;

    // display initial map values
    cout << "Initial Values:" << endl;

    for(itr = student.begin(); itr != student.end(); ++itr) {
        cout << itr->second << ", ";
    }
    
    cout << endl;
    
    // use itr iterator to point to the first map element
    itr = student.begin();

    // remove the first element
    student.erase(itr);

    // remove the element having key 4
    student.erase(4);

    // display final map values
    cout << "\nFinal Values:" << endl;

    for(itr = student.begin(); itr != student.end(); ++itr) {
        cout << itr->second << ", ";
    }
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Initial Values:
Denise, Blake, Courtney, John, Jennifer, 

Final Values:
Blake, Courtney, Jennifer, 

In the above program, we have used the `erase()` function to delete individual map elements.

First, we deleted the first map element by supplying the itr iterator to `erase()`.

```
itr = student.begin();
student.erase(itr);
```

**Note:** We have also used the itr iterator to loop through the map.

Then, we deleted the map element possessing the key **4** by supplying the key to `erase()`.

```
student.erase(4);
```

![The erase() function can remove individual elements with an iterator or a key](https://www.programiz.com/sites/tutorial2program/files/cpp-map-remove-individual-element.png "Remove Individual Map Elements")

Remove Individual Map Elements

---

### Delete a Range of Elements

The `erase()` function can also be used to remove a range of elements from the map. For this, we need to pass two iterators to the `erase()` function:

```
my_map.erase(itr_first, itr_last);
```

Here,

- itr_first - iterator to the first element to remove
- itr_last - iterator to the element succeeding the last element to remove

Here, itr_first is inclusive, meaning it is removed, while itr_last is not inclusive, meaning it is not removed. Obviously, all the elements in between are removed as well.

Note that the elements in a map are internally sorted by their **key**.

---

### Example 3: erase() to Remove a Range of Elements

```
#include <iostream>
#include <map>
using namespace std;

int main() {
    
    // create a map named student
    map <int, string> student {{1, "Denise"}, {2, "Blake"}, {3, "Courtney"}, {4, "John"}, {5, "Jennifer"}};

    // create a map iterator
    map <int, string>::iterator iter;
    
    // display initial map values
    cout << "Initial Values:" << endl;
    for(iter = student.begin(); iter != student.end(); ++iter) {
        cout << iter->second << ", ";
    }
    
    cout << endl;
    
    // remove a range of elements
    student.erase(student.find(2),student.find(5));

    // display final map values
    cout << "\nFinal Values:" << endl;

    for(iter = student.begin(); iter != student.end(); ++iter) {
        cout << iter->second << ", ";
    }
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Initial Values:
Denise, Blake, Courtney, John, Jennifer, 

Final Values:
Denise, Jennifer, 

In the above program, we have removed the map elements between the keys **2** and **5**.

However, notice that the element with the key **5** is not removed, while the element with the key **2** is removed.

This is because `erase()` removes the starting element of the given range but doesn't remove the end element.

![The erase() function can remove a range of map elements with an iterator or a key](https://www.programiz.com/sites/tutorial2program/files/cpp-map-remove-elements-range.png "Remove a Range of Map Elements")

Remove a Range of Map Elements

---

**Also Read:**

- [C++ Unordered Map](https://www.programiz.com/cpp-programming/unordered-map)
- [C++ Multimap](https://www.programiz.com/cpp-programming/multimap)
- [C++ Unordered Multimap](https://www.programiz.com/cpp-programming/unordered-multimap)

- [](https://www.programiz.com/cpp-programming/map#introduction)
- [](https://www.programiz.com/cpp-programming/map#map-methods)
- [](https://www.programiz.com/cpp-programming/map#store-values)
- [](https://www.programiz.com/cpp-programming/map#key-value-access)
- [](https://www.programiz.com/cpp-programming/map#find)
- [](https://www.programiz.com/cpp-programming/map#delete-elements)
- [](https://www.programiz.com/cpp-programming/map#example2)
- [](https://www.programiz.com/cpp-programming/map#delete-range)

[

  


](https://www.programiz.com/cpp-programming/stack "C++ Stack")