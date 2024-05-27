# C++ Operator Overloading

In C++, we can define how operators behave for user-defined types like [class](https://www.programiz.com/cpp-programming/object-class) and [structures](https://www.programiz.com/cpp-programming/structure) For example,

The `+` operator, when used with values of type `int`, returns their sum. However, when used with objects of a user-defined type, it is an error.

In this case, we can define the behavior of the `+` operator to work with objects as well.

This concept of defining operators to work with objects and structure variables is known as **operator overloading**.

---

## Syntax for C++ Operator Overloading

The syntax for overloading an operator is similar to that of [function](https://www.programiz.com/cpp-programming/function) with the addition of the `operator` keyword followed by the operator symbol.

```
returnType operator symbol (arguments) {
    ... .. ...
} 
```

Here,

- `returnType` - the return type of the function
- `operator` - a special [keyword](https://www.programiz.com/cpp-programming/keywords-identifiers)
- `symbol` - the operator we want to overload (`+`, `<`, `-`, `++`, etc.)
- `arguments` - the arguments passed to the function

---

## Overloading the Binary + Operator

Following is a program to demonstrate the overloading of the `+` operator for the class `Complex`.

```
// C++ program to overload the binary operator +
// This program adds two complex numbers

#include <iostream>
using namespace std;

class Complex {
    private:
        float real;
        float img;

    public:
         // constructor to initialize real and img to 0
         Complex() : real(0), img(0) {}
         Complex(float real, float img) : real(real), img(img){}

       // overload the + operator
         friend Complex operator + (const Complex& obj1, const Complex& obj2) {
             Complex temp;
              temp.real = obj1.real + obj2.real;
              temp.img = obj1.img + obj2.img;
              return temp;
    }

    void display() {
        if (img < 0)
            cout << "Output Complex number: " << real << img << "i";
      else
           cout << "Output Complex number: " << real << "+" << img << "i";
    }
};

int main() {
    Complex c1(1.0f, 2.0f);
    Complex c2(1.0f, 3.0f);

    // calls the overloaded + operator
    Complex result = c1 + c2;
    result.display();

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Output Complex number: 2+5i

Here, we first created a friend function with a return type `Complex`.

```
friend Complex operator + () {
    ...
}
```

The operator keyword followed by `+` indicates that we are overloading the `+` operator.

The function takes two arguments:

```
friend Complex operator + (const Complex& obj1, const Complex& obj2) {...}
```

Here,

- `Complex&` indicates that we are passing objects by reference and obj1 and obj2 are references to `Complex` objects. This is an efficient approach because it avoids unnecessary copying, especially for large objects. To learn more, visit [C++ References](https://www.programiz.com/cpp-programming/pointers-function).

- `const` indicates that referenced objects are constant, meaning we cannot modify obj1 and obj2 within the function.

Inside the function, we created another `Complex` object, temp to store the result of addition.

```
Complex temp;
```

We then add the real parts of two objects and store it into the `real` attribute of the temp object.

```
temp.real = obj1.real + obj2.real;
```

Similarly, we add the imaginary parts of the two objects and store them into the `img` attribute of the temp object.

```
temp.img = obj1.img + obj2.img;
```

At last, we return the temp object from the function.

```
return temp;
```

Reason to Overload Operators Using Friend Function

---

## Overloading ++ as a Prefix Operator

Following is a program to demonstrate the overloading of the `++` operator for the class `Count` .

```
// Overload ++ when used as a prefix operator

#include <iostream>
using namespace std;

class Count {
    private:
        int value;

   public:

    // constructor to initialize count to 5
    Count() : value(5) {}

    // overload ++ when used as prefix
    void operator ++ () {
        ++value;
    }

    void display() {
        cout << "Count: " << value << endl;
    }
};

int main() {
    Count count1;

    // call the "void operator ++ ()" function
    ++count1;

    count1.display();
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Count: 6

Here, when we use `++count1;`, the `void operator ++ ()` is called. This increases the value attribute for the object count1 by 1.

**Note**: When we overload operators, we can use it to work in any way we like. For example, we could have used ++ to increase value by 100.

However, this makes our code confusing and difficult to understand. It's our job as a programmer to use operator overloading properly and in a consistent and intuitive way.

Overloading`++`as a Postfix Operator

[](https://www.programiz.com/cpp-programming/online-compiler)

---

## Things to Remember in C++ Operator Overloading

1. By default, operators `=` and `&` are already overloaded in C++. For example,

we can directly use the `=` operator to copy objects of the same class. Here, we do not need to create an operator function.

2. We cannot change the precedence and associativity of operators using operator overloading.

3. We cannot overload following operators in C++:

- `::` (scope resolution)
- `.` (member selection)
- `.*` (member selection through pointer to function)
- `?:` (ternary operator)
- `sizeof` operator
- `typeid` Operator

4. We cannot overload operators for fundamental data types like `int`, `float`, etc

---

**Also Read:**

- [How to overload increment operator in right way?](https://www.programiz.com/cpp-programming/increment-decrement-operator-overloading)
- [How to overload binary operator - to subtract complex numbers?](https://www.programiz.com/cpp-programming/operator-overloading/binary-operator-overloading)
- [Increment ++ and Decrement -- Operators](https://www.programiz.com/article/increment-decrement-operator-difference-prefix-postfix)