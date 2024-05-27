# C++ Structure and Function

We can pass [structure](https://www.programiz.com/cpp-programming/structure) variables to a [function](https://www.programiz.com/cpp-programming/function) and return it from a function in the same way as normal data types.

---

## Passing Structure to Function in C++

A structure variable can be passed to a function just like any other variable.

Consider this example:

```
#include <iostream>
#include <string>
using namespace std;

struct Person {
    string first_name;
    string last_name;
    int age;
    float salary;
};

// declare function with
// structure variable type as an argument
void display_data(const Person&);

int main() {
    // initialize the structure variable
    Person p {"John", "Doe", 22, 145000};

    // function call with 
    // structure variable as an argument
    display_data(p);

    return 0;
}

void display_data(const Person& p) {
    cout << "First Name: " << p.first_name << endl;
    cout << "Last Name: " << p.last_name << endl;
    cout << "Age: " << p.age << endl;
    cout << "Salary: " << p.salary;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

First Name: John
Last Name: Doe
Age: 22
Salary: 145000

In this program, we passed the structure variable p by reference to the function `display_data()` to display the members of `p`.

---

## Return Structure From Function in C++

We can also return a structure variable from a function.

Let's look at an example.

```
#include <iostream>
#include <string>
using namespace std;

// define structure
struct Person {
    string first_name;
    string last_name;
    int age;
    float salary;
};

// declare functions
Person get_data();
void display_data(const Person&);

int main() {

    Person p = get_data();
    display_data(p);

    return 0;
}

// define function to return structure variable
Person get_data() {

    Person p;
    
    string first_name;
    string last_name;
    int age;
    float salary;
    
    cout << "Enter first name: ";
    cin >> first_name;
    cout << "Enter last name: ";
    cin >> last_name;
    cout << "Enter age: ";
    cin >> age;

    cout << "Enter salary: ";
    cin >> salary;
    
    // return structure variable
    return Person{first_name, last_name, age, salary};
}

// define function to take
// structure variable as an argument
void display_data(const Person& p) {
    cout << "\nDisplaying Information." << endl;
    cout << "First Name: " << p.first_name << endl;
    cout << "Last Name: " << p.last_name << endl;
    cout << "Age: " << p.age << endl;
    cout << "Salary: " << p.salary;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Enter first name: John
Enter last name: Doe
Enter age: 22
Enter salary: 145000

Displaying Information.
First Name: John
Last Name: Doe
Age: 22
Salary: 145000

In this program, we took user input for the structure variable in the `get_data()` function and returned it from the function

Then we passed the structure variable p to `display_data()` function by reference, which displays the information.

---

**Also Read:**

- [C++ Program to Add Complex Numbers by Passing Structure to a Function](https://www.programiz.com/cpp-programming/examples/complex-number-add)