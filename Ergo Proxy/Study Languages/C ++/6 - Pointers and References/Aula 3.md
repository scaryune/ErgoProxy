# C++ References

In C++, we use a reference to create an alias for a variable. We can use the reference variable to access or modify the variable.

---

## Create a C++ Reference

We use the ampersand sign to create a reference. For example,

```
string& ref_city = city;
```

Here,

- `string` - datatype of the variable
- `&` - denotes we are creating a reference
- ref_city - name of the reference variable
- city - the variable for which reference is created

---

### Example: C++ Reference

```
#include <iostream>

using namespace std;

int main() {

    string city = "Paris";

    // create a reference to the variable
    string& ref_city = city;
    
    // display the variable
    cout << "Variable Value: " << city << endl;
    cout << "Reference Value: " << ref_city << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Variable Value: Paris
Reference Value: Paris

In the above example, we have used the reference variable `ref_city` to display the value of the variable `city`.

---

## Modify Variables Using References

We can modify a variable by simply assigning a new value to the reference variable. For example,

```
#include <iostream>

using namespace std;

int main() {

    string city = "Paris";

    // create a reference to the variable
    string& ref_city = city;
    
    // display the variable
    cout << "Variable Value = " << city << endl;
    cout << "Reference Value = " << ref_city << endl;

    // modify the variable using reference
    ref_city = "New York";

    // display the variable
    cout << endl << "After Modification: " << endl;
    cout  << "Variable Value = " << city << endl;
    cout << "Reference Value = " << ref_city << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Variable Value: Paris
Reference Value: Paris

After Modification:
Variable Value: = New York
Reference Value: New York

---

## Important Points

**1. Placement of the `&` sign**

We can place the `&` sign with data type or with a variable while creating a reference. However, the standard practice is to use the sign along with the data type. For example,

```
// create a variable
string city = "Paris";

// valid but not a standard practice
string &ref_city = city;

// valid and a standard practice
sring& ref_city = city;
```

**2. References Initialization**

We must initialize references at the time of declaration.

```
// create a variable
string city = "Paris";

// incorrect code [reference not initialized]
string& ref_city;
ref_city = city;

// correct code
string& ref_city = city;
```

**3. Reference With a New Variable**

Once we create a reference to a variable, it cannot be changed to refer to another variable. For example,

```
#include <iostream>

using namespace std;

int main() {

    string city1 = "Paris";

    // create a reference to the variable
    string& ref_city = city1;
    
    // display the variable
    cout << "city1 = " << city1 << endl;
    cout << "ref_city = " << ref_city << endl;
    
    string city2 = "New York";
    
    // trying to modify the ref_city reference variable to refer to city2
    // but it assigns the value of city2 to the variable city1
    ref_city = city2;

    // display the variables
    cout << endl << "city1 = " << city1 << endl;
    cout << "city2 = " << city2 << endl;
    cout << "ref_city = " << ref_city << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

city1 = Paris
ref_city = Paris

city1 = New York
city2 = New York
ref_city = New York

Here, when we try to modify the reference variable ref_city to refer to the variable city2 in the line `my_city = city2;`, the reference variable my_city is not modified to refer to city2.

Rather, the value of city2 is assigned to the variable city1, as the reference variable ref_city refers to the variable city1.

---

## Frequently Asked Questions

What are the types of references?

What are the differences between references and pointers?

---

**Also Read:**

- [C++ Pass by Reference](https://www.programiz.com/cpp-programming/pointers-function)
- [C++ Return by Reference (programiz.com)](https://www.programiz.com/cpp-programming/return-reference)

- [](https://www.programiz.com/cpp-programming/references#create-a-reference)
- [](https://www.programiz.com/cpp-programming/references#example)
- [](https://www.programiz.com/cpp-programming/references#modify-using-reference)
- [](https://www.programiz.com/cpp-programming/references#important-points)

[

  


](https://www.programiz.com/cpp-programming/pointers-arrays "C++ Pointers and Arrays")