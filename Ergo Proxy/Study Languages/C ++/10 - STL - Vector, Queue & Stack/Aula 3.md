## C++ std::array Declaration

`std::array` is defined in the `<array>` header so we must include this header before we can use `std::array`.

**Syntax**

```
#include <array>

// declaration of std::array 
std::array<T, N> array_name;
```

where,

- T - Type of element to be stored
- N - Number of elements in the array

Here is how we declare a `std::array` of size 5 that stores a list of numbers:

```
std::array<int, 5> numbers;
```

---

## Initialization of std::array

We can initialize `std::array` in two ways:

**Method 1:**

```
// initializer list
std::array<int, 5> numbers = {1, 2, 3, 4, 5};
```

**Method 2:**

```
// uniform initialization
std::array<int, 5> marks {10, 20, 30, 40, 50};
```

Here, we initialized two arrays named numbers and marks both of size **5** that stores element of type `int`.

---

## Example: C++ std::array

```
// C++ program to demonstrate the usage of std::arrays

#include <iostream>
#include <array>

using namespace std;

int main(){
    // uniform initialization
    array <int , 5> numbers {1, 2, 3, 4, 5};

    cout << "The elements are: " << endl;

    // use a ranged for loop print the elements
    for(const int num: numbers){
        cout << num << " ";
    }
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

The elements are: 
1 2 3 4 5

In the above example, we have declared and initialized a `std::array` named numbers using uniform initialization.

```
array <int , 5> numbers {1, 2, 3, 4, 5};
```

We then displayed the content of the array using a [ranged for loop](https://www.programiz.com/cpp-programming/ranged-for-loop).

---

## Accessing the Elements of std::array

We can access the element of the array using the `[]` operator and index of the array element.

```
// array of 5 integers
std::array<int, 5> n = {1, 2, 3, 4, 5};

// access first array element
std::cout << n[0] // returns 1

// access second array element
std::cout << n[1] // returns 2 
```

Since the indexing starts from 0, `n[0]` returns the first element of the array, `n[1]` returns the second element and so on.

**Note**: Accessing elements using `[]` operator doesn't check for out of bound error.

An out of bounds error occurs when a program tries to access data outside the allowed range. For example, we have an array of **5** elements and we try accessing the **10th** element, that's an out of bound error.

Another way to access the element of the array is to use the `at` method which checks for out of bound error.

```
// array of 5 integers
std::array<int, 5> n = {1, 2, 3, 4, 5}; 
std::cout << n.at(0) // returns 1
std::cout << n.at(1) // returns 2
std::cout << n.at(10) // throws std::out_of_range exception
```

---

## Modifying the Elements of std::array

To modify an element at a particular index, we can again use `[]` and `at`.

```
std::array<int, 5> marks = {50, 67, 88, 98, 34};

// modify the 3rd element using []
marks[2] = 76; 

// modify the first element using at
n.at(0)= 1;
```

---

## Example: Modify and Access the Array Elements

```
#include <iostream>
#include <array>

using namespace std;

int main(){
    array <int, 5> numbers = {1, 2, 3, 4, 5};

    // accessing using the [] operator
    cout << "First element: " << numbers[0] << '\n';

    // accessing using the at method
    cout << "Second element: " << numbers.at(1) << '\n';

    // modify the element at index 0
    numbers[0] = 8;

    cout << "Modifying first element: " << numbers[0] << '\n';

    // modify the element at index 1
    numbers.at(1) = 90;

    cout << "Modifying second element: " << numbers[1] << '\n';
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

First element: 1
Second element: 2
Modifying first element: 8
Modifying second element: 90

The above example demonstrates the use of `[]` operator and the `at` method to access and modify the elements of `std::array`.

---

## Check if the Array is Empty

To check if the array is empty or not, we can use the `empty()` method as:

```
// let n be a std::array
n.empty()
```

The `empty` method returns true when the array is empty and false otherwise.

---

## Get the Number of Elements in the Array

We can use the `size` method to get the number of elements in the array.

```
// let n be a std::array
n.size() // returns the size of array
```

---

## Example: Using the empty and size method with std::array

```
#include <iostream>
#include <array>
using namespace std;

int main(){
    array <int, 5> numbers = {1, 2, 3, 4, 5};

    cout << "The size of array is: " << numbers.size() << '\n';

    if(numbers.empty()){
        cout << "The array is empty";
    }
    else{
        cout << "The array is not empty";
    }
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

The size of array is: 5
The array is not empty

In the above example, we used the `empty` method to check if the array is empty and the `size` method to get the number of elements in the array.

---

## Fill std::array With Same Value

We can use the fill method to `fill` the entire array with the same value.

Let's look at an example.

```
#include <iostream>
#include <array>

using namespace std;

int main(){
    array<int, 5> a;

    // fill the array with zeros
    a.fill(0);
  
    cout << "The elements are: ";
    for(const int& elt: a){
        cout << elt << " ";
    }
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

The elements are: 0 0 0 0 0

Here, we used `a.fill(0)` to fill the entire array with 0.

---

## Example: Using std::array with STL Algorithms

In C++, we can use the [Standard Template Library](https://www.programiz.com/cpp-programming/standard-template-library) to implement some of the commonly used algorithms. These algorithm supports `std::array` very well. For example,

```
#include <iostream>
#include <algorithm>
#include <numeric>
#include <array>

using namespace std;

int main(){
    array<int, 5> age = {45, 23, 66, 87, 21};

    // sorting
    sort(age.begin(), age.end());

    // print the sorted array
    cout << "The sorted array is: ";
    for(const int elt: age){
        cout << elt << " ";
    }
    cout << endl;

    // searching
   // checking whether the number 5  exists or not
    auto found = find(age.begin(), age.end(), 5);

    if (found != age.end()) cout << "5 was Found" << endl;
    else cout << "5 was Not Found" << endl;

    // summing
    int sum = accumulate(age.begin(), age.end(), 0);

    cout << "The sum of the element of array is : " << sum;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

The sorted array is: 21 23 45 66 87 
5 was Not Found
The sum of the element of array is : 242

Here, we performed 3 different operations in the array: sorting, searching and summing.

To **sort** the array, we used the `sort()` function.

```
sort(age.begin(), age.end());
```

This sorts the array from the first element to last.

To **search** an element in the array, we used the `find()` function.

```
// check if the number 5 is present or not
auto found = find(age.begin(), age.end(), 5);
```

Here, the find function searches if the number **5** is in the array age . The result is stored in the variable found. If found equals to `age.end()`, the number isn't there; otherwise, it is.

To find the **sum** of the elements of the array, we use the `std::accumulate` function.

```
int sum = std::accumulate(age.begin(), age.end(), 0);
```

This returns the sum of the numbers of an entire array.

What are the differences between`std::array`and C-style-array?