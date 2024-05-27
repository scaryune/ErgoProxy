# C++ Class Templates

Templates are powerful features of C++ that allows us to write generic programs. There are two ways we can implement templates:

- [Function Templates](https://programiz.com/cpp-programming/function-template)
- Class Templates

Similar to function templates, we can use class templates to create a single [class](https://www.programiz.com/cpp-programming/object-class#class) to work with different [data types](https://www.programiz.com/cpp-programming/data-types).

Class templates come in handy as they can make our code shorter and more manageable.

---

## Class Template Declaration

A class template starts with the keyword `template` followed by template parameter(s) inside `<>` which is followed by the class declaration.

```
template <class T>
class className {
  private:
    T var;
    ... .. ...
  public:
    T functionName(T arg);
    ... .. ...
};
```

In the above declaration, `T` is the template argument which is a placeholder for the data type used, and `class` is a [keyword](https://www.programiz.com/cpp-programming/keywords-identifiers#keywords).

Inside the class body, a member variable var and a member function `functionName()` are both of type `T`.

---

## Creating a Class Template Object

Once we've declared and defined a class template, we can create its [objects](https://www.programiz.com/cpp-programming/object-class#object) in other classes or [functions](https://www.programiz.com/cpp-programming/function) (such as the `main()` function) with the following syntax:

```
className<dataType> classObject;
```

For example,

```
className<int> classObject;
className<float> classObject;
className<string> classObject;
```

---

## Example 1: C++ Class Templates

```
// C++ program to demonstrate the use of class templates

#include <iostream>
using namespace std;

// Class template
template <class T>
class Number {
   private:
    // Variable of type T
    T num;

   public:
    Number(T n) : num(n) {}   // constructor

    T getNum() {
        return num;
    }
};

int main() {

    // create object with int type
    Number<int> numberInt(7);

    // create object with double type
    Number<double> numberDouble(7.7);

    cout << "int Number = " << numberInt.getNum() << endl;
    cout << "double Number = " << numberDouble.getNum() << endl;

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

int Number = 7
double Number = 7.7

In this program. we have created a class template `Number` with the code;

```
template <class T>
class Number {
   private:
    T num;

   public:
    Number(T n) : num(n) {}
    T getNum() { return num; }
};
```

Notice that the variable num, the constructor argument n, and the function `getNum()` are of type `T`, or have a return type `T`. That means that they can be of any type.

In `main()`, we have implemented the class template by creating its objects;

```
Number<int> numberInt(7);
Number<double> numberDouble(7.7);
```

Notice the codes `Number<int>` and `Number<double>` in the code above.

This creates a class definition each for `int` and `float`, which are then used accordingly.

It is a good practice to specify the type when declaring objects of class templates. Otherwise, some compilers might throw an error.

```
//Error
Number numberInt(7);
Number numberDouble(7.7);
```

---

## Defining a Class Member Outside the Class Template

Suppose we need to define a function outside of the class template. We can do this with the following code:

```
template <class T>
class ClassName {
    ... .. ...
    // Function prototype
    returnType functionName();
};

// Function definition
template <class T>
returnType ClassName<T>::functionName() {
    // code
}
```

Notice that the code `template <class T>` is repeated while defining the function outside of the class. This is necessary and is part of the syntax.

If we look at the code in **Example 1**, we have a function `getNum()` that is defined inside the class template `Number`.

We can define `getNum()` outside of `Number` with the following code:

```
template <class T>
class Number {
    ... .. ...
    // Function prototype
    T getnum();
};

// Function definition
template <class T>
T Number<T>::getNum() {
    return num;
}
```

---

## Example 2: Simple Calculator Using Class Templates

This program uses a class template to perform addition, subtraction, multiplication and division of two [variables](https://www.programiz.com/cpp-programming/variables-literals) num1 and num2.

The variables can be of any type, though we have only used `int` and `float` types in this example.

```
#include <iostream>
using namespace std;

template <class T>
class Calculator {
   private:
    T num1, num2;

   public:
    Calculator(T n1, T n2) {
        num1 = n1;
        num2 = n2;
    }

    void displayResult() {
        cout << "Numbers: " << num1 << " and " << num2 << "." << endl;
        cout << num1 << " + " << num2 << " = " << add() << endl;
        cout << num1 << " - " << num2 << " = " << subtract() << endl;
        cout << num1 << " * " << num2 << " = " << multiply() << endl;
        cout << num1 << " / " << num2 << " = " << divide() << endl;
    }

    T add() { return num1 + num2; }
    T subtract() { return num1 - num2; }
    T multiply() { return num1 * num2; }
    T divide() { return num1 / num2; }
};

int main() {
    Calculator<int> intCalc(2, 1);
    Calculator<float> floatCalc(2.4, 1.2);

    cout << "Int results:" << endl;
    intCalc.displayResult();

    cout << endl
         << "Float results:" << endl;
    floatCalc.displayResult();

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Int results:
Numbers: 2 and 1.
2 + 1 = 3
2 - 1 = 1
2 * 1 = 2
2 / 1 = 2

Float results:
Numbers: 2.4 and 1.2.
2.4 + 1.2 = 3.6
2.4 - 1.2 = 1.2
2.4 * 1.2 = 2.88
2.4 / 1.2 = 2

In the above program, we have declared a class template `Calculator`.

The class contains two private members of type `T`: num1 & num2, and a constructor to initialize the members.

We also have `add()`, `subtract()`, `multiply()`, and `divide()` functions that have the return type `T`. We also have a `void` function `displayResult()` that prints out the results of the other functions.

In `main()`, we have created two objects of `Calculator`: one for `int` data type and another for `float` data type.

```
Calculator<int> intCalc(2, 1);
Calculator<float> floatCalc(2.4, 1.2);
```

This prompts the compiler to create two class definitions for the respective data types during compilation.

---

## C++ Class Templates With Multiple Parameters

In C++, we can use multiple template parameters and even use default arguments for those parameters. For example,

```
template <class T, class U, class V = int>
class ClassName {
  private:
    T member1;
    U member2;
    V member3;
    ... .. ...
  public:
    ... .. ...
};
```

---

### Example 3: C++ Templates With Multiple Parameters

```
#include <iostream>
using namespace std;

// Class template with multiple and default parameters
template <class T, class U, class V = char>
class ClassTemplate {
   private:
    T var1;
    U var2;
    V var3;

   public:
    ClassTemplate(T v1, U v2, V v3) : var1(v1), var2(v2), var3(v3) {}  // constructor

    void printVar() {
        cout << "var1 = " << var1 << endl;
        cout << "var2 = " << var2 << endl;
        cout << "var3 = " << var3 << endl;
    }
};

int main() {
    // create object with int, double and char types
    ClassTemplate<int, double> obj1(7, 7.7, 'c');
    cout << "obj1 values: " << endl;
    obj1.printVar();

    // create object with int, double and bool types
    ClassTemplate<double, char, bool> obj2(8.8, 'a', false);
    cout << "\nobj2 values: " << endl;
    obj2.printVar();

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

obj1 values: 
var1 = 7
var2 = 7.7
var3 = c

obj2 values: 
var1 = 8.8
var2 = a
var3 = 0

In this program, we have created a class template, named `ClassTemplate`, with three parameters, with one of them being a default parameter.

```
template <class T, class U, class V = char>
class ClassTemplate {
  // code  
};
```

Notice the code `class V = char`. This means that `V` is a default parameter whose default type is `char`.

Inside `ClassTemplate`, we declare 3 variables var1, var2, and var3, each corresponding to one of the template parameters.

```
class ClassTemplate {
   private:
    T var1;
    U var2;
    V var3;
    ... .. ...
    ... .. ...
};
```

In `main()`, we create two objects of `ClassTemplate` with the code

```
// create object with int, double and char types
ClassTemplate<int, double> obj1(7, 7.7, 'c');

// create object with double, char and bool types
ClassTemplate<double, char, bool> obj2(8, 8.8, false);
```

Here,

|Object|T|U|V|
|---|---|---|---|
|obj1|`int`|`double`|`char`|
|obj2|`double`|`char`|`bool`|

For obj1, `T = int`, `U = double` and `V = char`.

For obj2, `T = double`, `U = char` and `V = bool`.

---

**Also Read**

- [C++ Standard Template Library](https://www.programiz.com/cpp-programming/standard-template-library)