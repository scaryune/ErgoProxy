# C++ Pointers to Structure

A [pointer](https://www.programiz.com/cpp-programming/pointers) variable can be created not only for built-in [types](https://www.programiz.com/cpp-programming/data-types) like (`int`, `float`, `double` etc.) but they can also be created for user defined types like [structure](https://www.programiz.com/cpp-programming/structure).

If you do not know what pointers are, visit [C++ pointers](https://www.programiz.com/cpp-programming/pointers).

---

## Example: Pointers to Structure

```
#include <iostream>
using namespace std;

struct Distance {
    int feet;
    float inch;
};

int main() {
    Distance d;
    Distance* ptr = &d;
    
    cout << "Enter feet: ";
    cin >> (*ptr).feet;
    cout << "Enter inch: ";
    cin >> (*ptr).inch;
 
    cout << "Displaying information." << endl;
    cout << "Distance = " << (*ptr).feet << " feet " << (*ptr).inch << " inches";

    return 0;
}
```

**Output**

Enter feet: 4
Enter inch: 3.5
Displaying information.
Distance = 4 feet 3.5 inches

Here, the address of variable d is stored in the pointer variable ptr, which means ptr is pointing to variable d.

```
Distance* ptr = &d;
```

Then, the member function of variable d is accessed using the pointer.

```
cin >> (*ptr).feet;
```

**Notes:**

- Since pointer ptr is pointing to variable d in this program, `(*ptr).inch` and `d.inch` are equivalent. Similarly, `(*ptr).feet` and `d.feet` are equivalent.
- Since the `.` operator has a higher [precedence](https://www.programiz.com/cpp-programming/operators-precedence-associativity) than the `*` operator, we enclose `*ptr` in brackets when using `(*ptr).inch`.

---

## Arrow (->) Operator

We can use the arrow (->) operator to access member variables and member functions of a structure variable through a pointer.

---

## Accessing Member Variable Using Arrow (->) Operator Example

```
#include <iostream>
using namespace std;

struct Distance {
	int feet;
	float inch;
};

int main() {
	Distance d;

	Distance* ptr = &d;
    
	cout << "Enter feet: ";
	cin >> ptr->feet;
	cout << "Enter inch: ";
	cin >> ptr->inch;
 
	cout << "Displaying information." << endl;
	cout << "Distance = " << ptr->feet << " feet " << ptr->inch << " inches";

	return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output**

Enter feet: 4
Enter inch: 3.5
Displaying information.
Distance = 4 feet 3.5 inches

Here, the address of variable d is stored in the pointer variable ptr which means ptr is pointing to variable d.

```
Distance* ptr = &d;
```

Then, the member variable of variable d is accessed using the pointer.

```
cin >> ptr->feet;
```

**Note:** `(*ptr).inch` and `ptr->inch` are equivalent.

---

## Accessing Member Function Using Arrow (->) Operator Example

```
#include <iostream>
using namespace std;

struct Distance {
    int feet;
    float inch;
    
    void print_distance() {
    	cout << "Displaying Information." << endl;
    	cout << "Distance = " << feet << " feet " << inch << " inches";
    }
};

int main() {
    Distance d;

    Distance* ptr = &d;
    
    cout << "Enter feet: ";
    cin >> ptr->feet;
    cout << "Enter inch: ";
    cin >> ptr->inch;
    
    ptr->print_distance();

    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

**Output:**

Enter feet: 4
Enter inch: 3.5
Displaying Information.
Distance = 4 feet 3.5 inches

Here, the member function of variable d is accessed using the pointer.

```
ptr->print_distance();
```