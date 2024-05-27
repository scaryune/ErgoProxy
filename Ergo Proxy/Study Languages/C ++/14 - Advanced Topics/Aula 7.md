# C++ Assert

In C++, an assertion is a statement used to state or assert that the expression must be `true`.

It is used to check the conditions that cannot happen unless there is a bug. So, it is used as a debugging tool since it terminates the program when the assertion becomes `false`.

For example, if we want to calculate the average of **non-empty** vector nums, then the assertion

```
nums.size() > 0 
```

must hold true unless there is a bug in the program.

---

## Create C++ Assertion

In C++, we can use assertion using the `assert` preprocessor macro, which is defined in the `cassert` header file.

```
#include <cassert>
```

Once we import this file, we can create an assertion using the following syntax:

```
assert(expression);
```

Here, if the `expression` evaluates to

- **0 (false)** - the assert prints a message and terminates the program
- **1 (true) -** does nothing and continues normal execution of the program

---

## Example 1: C++ assert

```
#include <iostream>
#include <cassert>
using namespace std;

int main() {

  int even_num = 3;

  // asserts the value of even_num must be even
  assert((even_num % 2 == 0));

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Assertion `(even_num % 2 == 0)' failed.
Aborted

In the above example, we have used the `assert` macro to assert that the value of even_num should be even.

```
assert(even_num % 2 == 0);
```

Since the value of even_num is **3**, the assertion even `num % 2 == 0` fails. As a result, the program terminates and an error message is printed.

But if we change even_num to **2**, the program executes without any error.

**Note:** C++ `assert` macro does not provide a parameter for custom error messages. But we can add a description of the error using the comma operator.

```
assert(("The number should be even", even_num % 2  == 0));
```

This gives the error message as:

```
Assertion `("The number should be even", even_num % 2 == 0)' failed
```

---

## Disable assert in C++

Assertions are used to check conditions that should not happen unless there is a bug. So, they are used as a debugging tool.

Therefore, we should remove the assertions before the release of the application as the released build should be functional and should never trigger the assertion.

One way to disable the assertions is by searching for the assert macro in code after the debugging is completed and removing it manually.

A better approach is to disable it using the `NDEBUG` macro. This macro ignores all assertions globally. We can implement this macro by using the `#define` directive right before including the `cassert` header file.

So when we are done with debugging and don't need assertions, we can add the code below.

```
#define NDEBUG
#include <cassert> 
```

**Note:** For a larger project with multiple files, `NDEBUG` can be set with the compiler command-line options or through the IDE setting.

---

## Static Assert

The `assert` macro is used for runtime assertion. In contrast, `static_assert` is used for assertion at compile time.

The syntax for `static_assert` is

```
static_assert(const_boolean_expression, message);
```

Here,

- `const_boolean_expression` - expression that is known during compile-time
- `message` - message to show if the assertion fails

Since `static_assert` is a keyword, we don't need to include any header file.

---

### Example 2: C++ Static Assert

```
#include <iostream>
using namespace std;

int main() {

  static_assert(sizeof(int) >= 4, "Size of integer must be greater than or equal to 4 bytes");

  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

In the above example, we have used static assertions so that size of the integer is at least **4** bytes in the platform where the code is running.

Since the size of data types can differ across platforms, we can use static assertion to assert in compile time.

Unlike `assert`, which is done at runtime, the program fails to compile if the `static_assert` fails.

Here, if we run the program in an older system (**16 bit**), the assertion fails since the `sizeof(int)` is **2 bytes.**

---

## Example 3: C++ Static Assert - Generic Programming

```
#include <iostream>
using namespace std;

template <class T, int size>
class Container {

  static_assert(size > 0, "The size of container cannot be less than 1");
  T items[size];
};

int main() {
  Container<int, 0> st;
  return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

error: static assertion failed: The size of container cannot be less than 1

In the above example, we have used a static assertion to ensure that the size of the array in the [generic class](https://www.programiz.com/cpp-programming/class-templates) is greater than **0**.

Here, we have created an object of the `Container` class using:

```
Container <int, 0> st;
```

Since the value of size is **0**, the compilation fails with a static assertion failed message.

---

## When to Use Assertions

### 1. Unreachable Codes

These are the codes that do not execute when we try to run the program. Use assertions to make sure unreachable codes are actually unreachable.

Let's take an example.

```
void unreachable_code_method() {
  cout << "Reachable code";
  return;

  // Unreachable code
  cout << "Unreachable code";
  assert(false);
}
```

Let's take an example of a `switch` statement without a `default` case.

```
switch (day_of_week) {
  case 1:
    cout << "It's Sunday!";
    break;
  case 2:
    cout << "It's Monday!";
    break;
  case 3:
    cout << "It's Tuesday!";
    break;
  case 4:
    cout << "It's Wednesday!";
    break;
  case 5:
    cout << "It's Thursday!";
    break;
  case 6:
    cout << "It's Friday!";
    break;
  case 7:
    cout << "It's Saturday!";
    break;
```

The above `switch` statement indicates that the days of the week can be only from **1 to 7**. Having no `default` case means that the programmer believes that one of these cases will always be executed.

However, there might be some cases that have not yet been considered where the assumption is actually false.

This assumption should be checked using an assertion to make sure that the `default` switch case is not reached.

```
default:
  assert(("An Invalid Day", false));
```

If day_of_week has a value other than the **1 - 7**, an assertion error occurs.

---

### 2. Documenting Assumptions

To document their underlying assumptions, many programmers use comments. Let's take an example.

```
if (i % 2 == 0) {
  ...
}
else { // We know (i % 2 == 1)
  ...
}
```

Use assertions instead.

Comments can get out-of-date and out-of-sync as the program grows. However, we will be forced to update the `assert` macro; otherwise, they might fail for valid conditions too.

```
if (i % 2 == 0) {
  ...
}
else {
  assert(i % 2 == 1);
  ...
}
```

---

## When Not to Use Assertions

### 1. Argument Checking in public Functions

Arguments in public functions may be provided by the user.

So if an assertion is used to check these arguments, the conditions may fail and result in an assertion error.

Instead of using assertions, let it result in the appropriate runtime exceptions and handle these exceptions.

---

### 2. To Evaluate Expressions That Affect the Program Operation

Do not call methods or evaluate exceptions that cause side effects. For example,

```
int n = 5;

// assertion with side effects
// here assertion is decrementing 'n' and asserts if n is even
assert(--n && n % 2 == 0);
```

In the above example, the statement `--n && n % 2 == 0` has a side effect i.e it modifies the value of variable n . Also, the assert macro runs only if the assertion is enabled.

But if we have disabled the assertions using the `NDEBUG` macro, the above decrement statement is never evaluated, thus affecting the whole code if n is referenced later in the code.

So instead of evaluating expressions that have side effects inside the `assert` macro, we can write it as

```
int n = 5;

//decrement n
--n;
  
// assertion without side effects
// here assertion asserts if n is even
assert(n % 2 == 0);
```

This ensures that the value of n is the same whether **the assertion is enabled or disabled**.