# C++ Namespaces

In C++, a namespace is a collection of related names or identifiers (functions, class, variables) which helps to separate these identifiers from similar identifiers in other namespaces or the global namespace.

Let's look at the following code:

```
int main() {

    int var;

    // Error: conflicting declaration
    double var;
}
```

This code doesn't compile successfully because we have declared two variables of the same name var within the scope of the `main()` function. In C++, this is known as a **naming conflict**.

One way to compile the code without errors is to declare one var in another scope separate from the other var:

```
int main() {

    int var;

    // separate local scope
    {
        double var;
    }

    return 0;
}
```

However, we can use the same name for multiple variables (or arrays, vectors, functions, etc.) inside the same scope if we use namespaces.

In other words, namespaces in C++ are a way to prevent naming conflicts within the program, especially if it is a large project.

---

## Creating a Namespace

We can create a namespace by using the `namespace` keyword and declaring/defining our entities within its scope:

```
namespace dbl {
    double var;
}
```

Here, we have created a namespace named `dbl` and declared a `double` variable named var inside it.

We can then use the scope resolution operator `::` outside the namespace to specify that we are using the var variable belonging to `dbl`.

```
dbl::var;
```

Let's clarify this with a simple example.

```
#include <iostream>
using namespace std;

// create a namespace with a double variable
namespace dbl {
    double var;
}

int main() {
    
    // create an int variable of the same name
    int var = 5;
    
    // use the created namespace to avoid naming conflict
    dbl::var = 5.55;
    
    // display the variables
    cout << "dbl var = " << dbl::var << endl;
    cout << "main var = " << var << endl;
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

dbl var = 5.55
main var = 5

Here, we have created a namespace `dbl` where we have defined a `double` variable var.

We have then defined another var of `int` type in `main()`. By using the code `dbl::var`, we can use the variable of `dbl` namespace alongside the variable in `main()`.

Thus, we can see that using the `dbl` namespace has prevented a naming conflict from appearing in our program.

---

## Multiple and Nested Namespaces

We can use multiple namespaces in a single program. Multiple namespaces are especially useful when writing large programs with many lines of code.

Similarly, namespaces can be nested within other namespaces, allowing us to structure our code in a logical and hierarchical manner.

An example of multiple and nested namespaces is given below:

```
#include <iostream>
using namespace std;

namespace one {
    
    void display() {
        cout << "namespace one" << endl;
    }

    // create another namespace inside namespace one    
    namespace one_one {
        void display() {
            cout << "namespace one_one" << endl;
        }
    }
}

namespace two {
    void display() {
        cout << "namespace two" << endl;
    }
}

void display() {
    cout << "not a namespace" << endl;
}

int main() {

    // call the display() function of namespace one    
    one::display();

    // call the display() function of namespace one_one
    one::one_one::display();

    // call the display() function of namespace two
    two::display();

    // call the display() function outside the namespaces
    display();
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

namespace one
namespace one_one
namespace two
not a namespace

Here, we have created two namespaces `one` and `two`, each with their own `display()` functions.

We have also defined another `display()` function in the `one_one` namespace nested within the `one` namespace.

Then we have declared a `display()` function outside all the namespaces.

We then called the `display()` functions of each namespace using the `::` operator.

Notice the way we've called the `display()` function inside the nested namespace `one_one`.

```
one::one_one::display();
```

As you can see, we need to include both the outer namespace `one` and the nested namespace `one_one` in order to access members of the nested namespace.

Finally, without the `::` operator, the function not defined inside a namespace is called.

```
// call the display() function outside the namespaces
display();
```

---

## C++ Using Directive

We can bypass the use of `::` operator with the help of the `using` directive.

In fact, we have been using this directive for the majority of our programs so far with the `using namespace std;` code.

We have already mentioned that without the use of the `std` namespace, some of our most important IO objects and standard exceptions become:

```
// without using std namespace
std::cout
std::cin
std::endl
std::exception
std::bad_cast
```

By including the `using namespace std;` code in our program, we can omit the `std::` part for the identifiers defined in the `std` namespace:

```
// using std namespace
cout
cin
endl
exception
bad_cast
```

This applies to other namespaces as well.

---

### Example: C++ using Directive

We can create and use multiple namespaces in a single program.

```
#include <iostream>
using namespace std;

namespace one {

    void display() {
        cout << "namespace one" << endl;
    }
}

namespace two {

    void display() {
        cout << "namespace two" << endl;
    }
}

int main() {

    using namespace one;

    // call one::display()
    display();
    
    // call two:: display
    two::display();
    
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

namespace one
namespace two

Here, by including the code `using namespace one;` in our program, we can call its `display()` function without using the scope resolution operator `::`.

The `::` operator is required if we want to call the `display()` function of the namespace `two`.

**Note:** We have included our `using namespace one;` directive inside `main()`, while the `using namespace std;` code is outside of `main()` (and all other possible scopes).

```
#include <iostream>
using namespace std;

... .. ...
... .. ...

int main() {
  using namespace one;
  ... .. ...
}
```

This means that we have used the `one` namespace within the scope of the `main()` function, while the `std` namespace is being used in a global scope.

The use of a namespace can be global or limited to a certain scope. It depends on how we want to use the namespace.

---

### Naming Conflicts With The Using Directive

It is clear from the example program we have seen just now that the `using` directive can create a lot of naming conflicts in our program. For example,

```
using namespace one;

namespace one {
    void display() {...}
}

void display() {...}

int main() {

    // Error: more than one instance of display()
    display();

    return 0;
}
```

In the code above, we have used the `one` namespace in a global scope.

Therefore, when we call the `display()` function, the compiler cannot determine whether we are calling the function belonging to namespace `one` or whether we are calling the function outside of the namespace.

Naming conflicts can also occur when we use multiple namespaces with the same identifiers. For example,

```
namespace one {
    void display() {...}
}

namespace two {
    void display() {...}
}

using namespace one;
using namespace two;

int main() {

    // Error: more than one instance of display()
    display();

    return 0;
}
```

---

## The std Namespace

All the files in the C++ standard library declare all of its entities within the `std` namespace.

However, it is possible that many of these entities (functions, objects, etc.) of the C++ standard might share identifiers with other namespaces in other libraries.

Or they might share identifiers with the ones we have created manually in our program.

This is why it is considered a bad practice to include the `using namespace std;` code in the global scope.

For example,

```
#include <iostream>
using namespace std;

string cout() {
    return "\n";
}

int main() {

    // Error: cout is ambiguous
    cout << "Testing!" << endl;

    return 0;
}
```

Here, we have defined our own `cout()` function while also using the `std` namespace. This causes a naming conflict in our program and we get an error when we use `cout`.

- [](https://www.programiz.com/cpp-programming/namespaces#introduction)
- [](https://www.programiz.com/cpp-programming/namespaces#create)
- [](https://www.programiz.com/cpp-programming/namespaces#multiple-nested)
- [](https://www.programiz.com/cpp-programming/namespaces#using)
- [](https://www.programiz.com/cpp-programming/namespaces#example)
- [](https://www.programiz.com/cpp-programming/namespaces#using-naming-conflicts)
- [](https://www.programiz.com/cpp-programming/namespaces#std-namespace)