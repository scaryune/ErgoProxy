# Go Pointers

Pointers in Go programming allows us to directly work with memory addresses. For example, we can access and modify the values of variables in the memory using pointers.

Before we learn about pointers, let's first understand memory addresses in Golang.

---

## Memory Address

When we create a variable, a memory address is allocated for the variable to store the value.

In Go, we can access the memory address using the `&` operator. For example,

```
// Program to illustrate how memory address works

package main
import "fmt"

func main() {
  
  var num int = 5
  // prints the value stored in variable
  fmt.Println("Variable Value:", num)

  // prints the address of the variable
  fmt.Println("Memory Address:", &num)

}
```

**Output**

Variable Value: 5
Memory Address: 0xc000018030

In the above example, we have created the num variable with the value **5**. Notice the print statement

```
fmt.Println("Memory Address:", &num)
```

Here, `&num` accesses the memory address where the num variable is stored.

---

## Go Pointer Variables

In Go, we use the pointer variables to store the memory address. For example,

```
var num int = 5

// create the pointer variable
var ptr *int = &num
```

Here, we have created the pointer variable named ptr that stores the memory address of the num variable.

`*int` represents that the pointer variable is of `int` type (stores the memory address of `int` variable).

We can also create pointer variables of other types. For example,

```
// pointer variable of string type
var ptr1 *string

// pointer variable of double type
var ptr2 * float32
```

Let's now see a working example of pointers.

---

## Example: Pointer Variables

We can assign the memory address of a variable to a pointer variable. For example,

```
// Program to assign memory address to pointer

package main
import "fmt"

func main() {

  var name = "John"
  var ptr *string

  // assign the memory address of name to the pointer
  ptr = &name

  fmt.Println("Value of pointer is", ptr)
  fmt.Println("Address of the variable", &name)

}
```

**Output**

Value of pointer is 0xc00007c1c0
Address of the variable 0xc00007c1c0

In the above example, we have created a pointer variable named ptr of type `string`. Here, both the pointer variable and the address of the name variables are the same.

This is because the pointer ptr stores the memory address of the `name` variable.

```
ptr = &name
```

---

## Get Value Pointed by Pointers in Golang

We use the `*` operator to access the value present in the memory address pointed by the pointer. For example,

```
// Program to get the value pointed by a pointer

package main
import "fmt"

func main() {

  var name = "John"
  var ptr *string

  ptr = &name

  // * to get the value pointed by ptr
  fmt.Println(*ptr) // John

}
```

Here, we have used the `*ptr` to access the value stored in the memory address pointed by the pointer.

Since the pointer stores the memory address of the name variable, we get the value **"John"** as output.

**Note:** In the above example, ptr is a pointer, not `*ptr`. You cannot and should not do something like `*ptr = &name`

The `*` is called the dereference operator (when working with pointers). It operates on a pointer and gives the value stored in that pointer.

---

## Example: Working of Pointers in Golang

```
package main
import "fmt"

func main() {
  var num  int
  var ptr *int
    
  num = 22
  fmt.Println("Address of num:",&num)
  fmt.Println("Value of num:",num)

  ptr = &num
  fmt.Println("\nAddress of pointer ptr:",ptr)
  fmt.Println("Content of pointer ptr:",*ptr)
    
  num = 11
  fmt.Println("\nAddress of pointer ptr:",ptr)
  fmt.Println("Content of pointer ptr:",*ptr)
    
  *ptr = 2
  fmt.Println("\nAddress of num:",&num)
  fmt.Println("Value of num:",num)
}
```

**Output**

Address of num: 0xc000090020
Value of num: 22

Address of pointer ptr: 0xc000090020
Content of pointer ptr: 22

Address of pointer ptr: 0xc000090020
Content of pointer ptr: 11

Address of num: 0xc000090020
Value of num: 2

---

### Explanation: Working of Go Pointers

**1. Declare Variables**

```
var num int
var ptr *int
```

![The pointer variable and normal variable are declared](https://www.programiz.com/sites/tutorial2program/files/declare-pointer-variable.png "Declare Variables")

The pointer variable and normal variable are declared

Here, we have created an integer type pointer variable ptr and a normal variable num. The two variables are not initialized initially, so the pointer ptr doesn't point to any address.

**2. Assign a value to a regular variable**

```
num = 22
```

![A value is assigned to the regular variable.](https://www.programiz.com/sites/tutorial2program/files/assign-value-to-variable.png "Assign a value to a regular variable")

Assign a value to a regular variable

This assigns **22** to the variable num. That is, **22** is stored in the memory location of the variable num.

**3. Assign an address to the pointer**

```
ptr = &num
```

![The address of a regular variable is assigned to the pointer variable](https://www.programiz.com/sites/tutorial2program/files/assign-memory-address-to-pointer.png "Assign address of a variable to the pointer")

Assign address of a variable to the pointer

This assigns the address of variable num to the pointer ptr.

**4. Change the value of a variable**

```
num = 11
```

![The value of the variable is changed.](https://www.programiz.com/sites/tutorial2program/files/change-variable-value.png "Change the value of a variable")

Change the value of the variable

This assigns **11** to the variable num.

**5. Change the value using pointer**

```
*ptr = 2
```

![The value of the variable is changed using the pointer dereference operator.](https://www.programiz.com/sites/tutorial2program/files/change-value-using-pointer.png "Change the value of the variable using pointer")

Change the value of the variable using pointer

This changes the value at the memory location pointed by the pointer ptr to **2**.

---

## Frequently Asked Questions

Nil Pointers in Golang

Create Pointers using Golang new()

Create pointers without using the * operator