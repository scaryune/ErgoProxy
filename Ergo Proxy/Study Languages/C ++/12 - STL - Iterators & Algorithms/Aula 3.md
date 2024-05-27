# C++ Functors

A C++ functor (function object) is a class or struct object that can be called like a function.

It overloads the **function-call operator** `()` and allows us to use an object like a function.

---

## Create a Functor in C++

We can create a functor in C++ as:

```
class Greet {
  public:
    void operator()() {
      // function body
    }
};
```

Here, we are overloading the function call operator `()`. This allows us to call the class object as if it were a function as shown below:

```
// create an instance of Greet
Greet greet;

// call the object as a function
greet(); 
```

**Note**: Remember to set `public` access specifier while overloading the `()` operator for the class, since by default the members of a class are `private`.

---

## Example 1: C++ Functor

```
#include <iostream>
using namespace std;

class Greet {

  public:    
    // overload function call/parentheses operator
    void operator()() {
      cout << "Hello World!";
    }
};

int main() {

  // create an object of Greet class
  Greet greet;

  // call the object as a function
  greet();

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Hello World!

In the above example, we have created a simple program that prints `Hello World!` using C++ functors.

In order to create a functor, we first have to create a class whose object we can call like a function. So, we have created a class named `Greet`.

**Inside the Greet class**

Here, we have overloaded the function call operator `()` using:

```
class Greet {

public:
  // overload function call operator
  void operator()() {
    cout << "Hello World!";
  }
};
```

Here, our overloaded function simply prints `Hello World!`.

**Inside the main() Function**

Here, we have created an object called greet from the `Greet` class.

```
Greet greet;
```

Now, we call the greet object using the `()` operator:

```
// displays "Hello World!"
greet() 
```

Alternatively, we can call greet using the following code:

```
// displays "Hello World!"
greet.operator()();
```

---

## C++ Functor With Return Type and Parameters

We can also define a functor that accepts parameters and returns a value. For example,

```
#include <iostream>
using namespace std;

class Add {

  public:
    // overload function call operator
    // accept two integer arguments
    // return their sum
    int operator() (int a, int b) {
      return a + b;
    }
};

int main() {

  // create an object of Add class
  Add add;

  // call the add  object
  int sum = add(100, 78);

  cout << "100 + 78 = " << sum;

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

100 + 78 = 178

In the above example, we have used a functor with an integer return type and two integer parameters to find their sum.

```
class Add {
  public:
    int operator()(int a, int b) {
      return a + b;
    }
};
```

Inside `main()`, we have created the add object from the `Add` class.

Then, we have called the add object with parameters **100** and **78**. The return value from the functor is assigned to the sum variable.

```
// returns 178
int sum = add(100, 78);
```

---

## Example 2: C++ Functor With a Member Variable

```
#include<iostream>
using namespace std;

class Add_To_Sum {

  private:
    int initial_sum;

  public:

    // constructor to initialize member variable  
    Add_To_Sum(int sum) {
      initial_sum = sum;
    }

    // overload function call operator
    int operator()(int num) {
      return initial_sum + num;
    }

};

int main() {

  // create object of Add_To_Sum class
  // initialize member variable of object with value 100
  Add_To_Sum add = Add_To_Sum(100);

  // call the add object with 78 as argument
  int final_sum = add(78);

  cout << "100 + 78 = " << final_sum;

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

100 + 78 = 178

In the above example, the `Add_To_Sum` class has a member variable initial_sum. We have initialized this variable using a constructor:

```
// constructor to initialize member variable
Add_To_Sum(int sum) {
  initial_sum = sum;
}
```

Then, we have overloaded the function call operator that:

- adds its parameter num to the initial_sum variable
- then returns the result.

```
int operator()(int num) {
  return initial_sum + num;
}
```

In `main()`, we have initialized the initial_sum variable of the add object to **100** using the parameterized constructor:

```
// initialize initial_sum variable to 100
Add_To_Sum add = Add_To_Sum(100);
```

Finally, we have called the functor and passed **78** as an argument.

```
// returns sum of 100 and 78 i.e 178
int final_sum = add_to_100(78); 
```

---

## C++ Predefined Functors

We can use predefined functors provided by the standard library by including the `functional` header file:

```
#include <functional>
```

C++ provides the following library functors for arithmetic, relational, and logical operations.

### 1. Arithmetic Functors

|Functors|Description|
|---|---|
|`plus`|returns the sum of two parameters|
|`minus`|returns the difference of two parameters|
|`multiplies`|returns the product of two parameters|
|`divides`|returns the result after dividing two parameters|
|`modulus`|returns the remainder after dividing two parameters|
|`negate`|returns the negated value of a parameter|

---

### 2. Relational Functors

|Functors|Description|
|---|---|
|`equal_to`|returns `true` if the two parameters are equal|
|`not_equal_to`|returns `true` if the two parameters are not equal|
|`greater`|returns `true` if the first parameter is greater than the second|
|`greater_equal`|returns `true` if the first parameter is greater than or equal to the second|
|`less`|returns `true` if the first parameter is less than the second|
|`less_equal`|returns `true` if the first parameter is less than or equal to the second|

---

### 3. Logical Functors

|Functors|Description|
|---|---|
|`logical_and`|returns the result of **Logical AND** operation of two booleans|
|`logical_or`|returns the result of **Logical OR** operation of two booleans|
|`logical_not`|returns the result of **Logical NOT** operation of a boolean|

---

### 4. Bitwise Functors

|Functors|Description|
|---|---|
|`bit_and`|returns the result of **Bitwise AND** operation of two parameters|
|`bit_or`|returns the result of **Bitwise OR** operation of two parameters|
|`bit_xor`|returns the result of **Bitwise XOR** operation of two parameters|

---

## Example 3: C++ Predefined Functor with STL

Usually, functors are used with C++ STL as arguments to STL algorithms like `sort`, `count_if`, `all_of`, etc.

In this example, we will look at a predefined C++ functor `greater<T>()`, where `T` is the type of the functor parameter with the STL algorithm `sort`.

```
#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>

using namespace std;

int main() {

  // initialize vector of int
  vector<int> nums = {1, 20, 3, 89, 2};

  // sort the vector in descending order
  sort(nums.begin(), nums.end(), greater<int>());

  for(auto num: nums) {
    cout << num << ", ";
  }

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

89, 20, 3, 2, 1

In the above example, we have used a predefined functor to sort a vector of integers (called nums) in descending order.

By default, the `sort()` function sorts the elements in ascending order.

In order ro make it sort in descending order, we have used the predefined functor `greater<T>`.

```
sort(nums.begin(), nums.end(), greater<int>());
```

Notice that we have used the code `greater<int>()`. This is because nums is an integer vector, so we use `int` in place of `T`.

Finally, we print the sorted vector using a ranged `for` loop.

---

## Frequently Asked Questions

How to create a functor using C++ struct?

[](https://www.programiz.com/cpp-programming/online-compiler)

How to use custom functors with STL algorithms?

[](https://www.programiz.com/cpp-programming/online-compiler)

How can we create generic functors?

[](https://www.programiz.com/cpp-programming/class-templates)

[](https://www.programiz.com/cpp-programming/online-compiler)

- [](https://www.programiz.com/cpp-programming/functors#introduction)
- [](https://www.programiz.com/cpp-programming/functors#syntax)
- [](https://www.programiz.com/cpp-programming/functors#example-1)
- [](https://www.programiz.com/cpp-programming/functors#return-type-parameters)
- [](https://www.programiz.com/cpp-programming/functors#example-2)
- [](https://www.programiz.com/cpp-programming/functors#predefined-functors-cpp)
- [](https://www.programiz.com/cpp-programming/functors#example-3)

[

  


](https://www.programiz.com/cpp-programming/algorithm "C++ Algorithm")