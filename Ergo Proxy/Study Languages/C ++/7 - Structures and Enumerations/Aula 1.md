# C++ Structures

A structure is a collection of [variables](https://www.programiz.com/cpp-programming/variables-literals#variables) of different [data types](https://www.programiz.com/cpp-programming/data-types) and member functions under a single name.

It is similar to a [class](https://www.programiz.com/cpp-programming/object-class) as both hold a collection of data of different data types.

Suppose you want to store some information about a person: their first_name, last_name, age, and salary.

You can easily create different variables—first_name, last_name, age, salary—to store this information separately.

However, in the future, you might want to store information about multiple people.

Now, you'd need to create different variables for each information per person: first_name1, last_name1, age1, salary1, first_name2, last_name2, age2, salary2, …

You can visualize how big and messy the code would look. Additionally, as there is no relation between the variables (information), it would be a daunting task to manage.

A better approach is to have a collection of all related information under a single name, such as Person and use it for every individual.

Now, the code looks much cleaner, more readable, and efficient as well.

This collection of all related information under a single name Person is a structure.

---

## How to Declare a Structure in C++ Programming?

The `struct` [keyword](https://www.programiz.com/cpp-programming/keywords-identifiers#keywords) defines a structure type followed by an [identifier](https://www.programiz.com/cpp-programming/keywords-identifiers#identifiers) (name of the structure).

Then, inside the curly braces, you can declare one or more members (declare variables inside curly braces) of that structure. For example:

```
struct Person
{
    string first_name;
    string last_name;
    int age;
    float salary;
};
```

Here, the structure Person is defined which has four members: first_name, last_name, age, and salary.

When a structure is defined, no memory is allocated.

The structure definition is only the blueprint for the creation of variables. You can imagine it as a data type.

When you define an integer as below:

```
int foo;
```

The `int` specifies that variable foo can hold integer elements only. Similarly, structure definition only specifies what property a structure variable holds when it is defined.

**Note:** Remember to end the declaration with a semicolon **(;)**.

---

## How to Define a Structure Variable?

Once you declare a structure Person as above, you can define a structure variable as:

```
Person bill;
```

Here, a structure variable bill is defined, which is of type structure Person.

Only when the structure variable is declared is the required memory allocated by the compiler.

---

## How to Access Members of a Structure?

The members of a structure variable are accessed using a **dot (.)** [operator](https://www.programiz.com/cpp-programming/operators).

Suppose you want to access the age of the structure variable bill and assign **50** to it. You can perform this task by using the following code:

```
bill.age = 50;
```

---

## Example: C++ Structure

```
// Program to assign data to members of a structure variable

#include <iostream>
using namespace std;

struct Person
{
    string first_name;
    string last_name;
    int age;
    float salary;
};

int main()
{
    Person p1;
    
    cout << "Enter first name: ";
    cin >> p1.first_name;
    cout << "Enter last name: ";
    cin >> p1.last_name;
    cout << "Enter age: ";
    cin >> p1.age;
    cout << "Enter salary: ";
    cin >> p1.salary;

    cout << "\nDisplaying Information." << endl;
    cout << "First Name: " << p1.first_name << endl;
    cout << "Last Name: " << p1.last_name << endl;
    cout << "Age: " << p1.age << endl;
    cout << "Salary: " << p1.salary;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Enter first name: Jane
Enter last name: Smith
Enter age: 27
Enter salary: 10000

Displaying Information.
First Name: Jane
Last Name: Smith
Age: 27
Salary: 10000

Here the structure Person is declared which has four members: first_name, last_name, age and salary.

Inside the `main()` [function](https://www.programiz.com/cpp-programming/function), a structure variable p1 is defined. Then, the user is asked to enter information, and data entered by the user is displayed.

---

## Member Functions in C++ Structures

In C++, structures can also have member functions.

These member functions are similar to regular functions but are defined within the scope of a structure. They can access and manipulate the data members of the structure directly.

We can declare a member function by defining the function within the structure definition.

```
struct Person {
    string first_name;
    string last_name;
    int age;
    float salary;

    // member function to display information about the person
    void displayInfo() {
        cout << "First Name: " << first_name << endl;
        cout << "Last Name: " << last_name << endl;
        cout << "Age: " << age << endl;
        cout << "Salary: " << salary << endl;
    }
};
```

In this example, the `Person` structure includes a member function, `displayInfo()` which displays the information about the person.

Let's look at an example.  

```
#include <iostream>
using namespace std;

struct Person {
    string first_name;
    string last_name;
    int age;
    float salary;

    // member function to display information about the person
    void display_info() {
        cout << "First Name: " << first_name << endl;
        cout << "Last Name: " << last_name << endl;
        cout << "Age: " << age << endl;
        cout << "Salary: " << salary << endl;
    }
};

int main() {
    Person p1;
    
    cout << "Enter first name: ";
    cin >> p1.first_name;
    cout << "Enter last name: ";
    cin >> p1.last_name;
    cout << "Enter age: ";
    cin >> p1.age;
    cout << "Enter salary: ";
    cin >> p1.salary;

    // display information using member function
    cout << "\nDisplaying Information." << endl;
    p1.display_info();

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Enter first name: Jane
Enter last name: Smith
Enter age: 27
Enter salary: 10000

Displaying Information.
First Name: Jane
Last Name: Smith
Age: 27
Salary: 10000

---

**Also Read**

- [How to pass structures to functions?](https://www.programiz.com/cpp-programming/structure-function)
- [How to use pointers with structures?](https://www.programiz.com/cpp-programming/structure-pointer)