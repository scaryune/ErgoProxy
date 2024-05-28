# Go Pointers to Structs

The struct types store the variables of different data types and we use the struct variable to access the members of the struct.

In Go, we can also create a pointer variable of struct type.

Before you learn about pointers to struct, make sure to know about:

- [Go Pointers](http://programiz.com/golang/pointers)
- [Go Struct](https://www.programiz.com/golang/struct)

---

## Go Pointer to Struct

Suppose we have a struct like this

```
type Person struct {
  name string
  age int
}
```

Now, let's create a struct variable of Person type.

```
person1 := Person{"John", 25}
```

Similar to this, we can also create a pointer variable of struct type.

```
var ptr *Person
```

We can now assign the address of the struct variable to this pointer variable. Let's see an example.

```
package main
import "fmt"

func main() {

  // declare a struct Person
  type Person struct {
    name string
    age int
  }

  // instance of the struct Person
  person1 := Person{"John", 25}

  // create a struct type pointer that
  // stores the address of person1
  var ptr *Person
  ptr = &person1

  // print struct instance
  fmt.Println(person1)

  // print the struct type pointer
  fmt.Println(ptr)

}
```

**Output**

{John 25}
&{John 25}

In the above example, we have created a struct variable person1 that initialized the struct members; `name` to `John` and age to **25**.

We have also created a pointer variable of the struct type that stores the address of person1.

```
var ptr *Person
ptr = &person1
```

Since the ptr now stores the address of person1, we get `&{John 25}` as the output while printing ptr.

**Note**: We can also create struct-type pointers and assign variable addresses in the same line. For example,

```
var ptr = &person1
```

---

## Access struct using pointer in Golang

We can also access the individual member of a struct using the pointer. For example,

```
// Program to access the field of a struct using pointer

package main
import "fmt"

func main() {

  // declare a struct Person
  type Person struct {
    name string
    age int
  }

  person := Person{"John", 25}

  // create a struct type pointer that
  // stores the address of person
  var ptr *Person
  ptr = &person

  // access the name member
  fmt.Println("Name:", ptr.name)

  // access the age member
  fmt.Println("Age:", ptr.age)

}
```

**Output**

Name: John
Age: 25

In the above example, we have used the struct type pointer to access struct members:

- `ptr.name` - gives the value of the name member
- `ptr.age` - gives the value of the age member

Here, we have used the dot operator to access the struct members using the pointer.

**Note:** We can also use the dereference operator, `*` to access the members of struct. For example,

```
fmt.Println(ptr.name) // John
fmt.Println((*ptr).name)  // John
```

---

## Change the Struct member in Go

Similarly, we can also use the pointer variable and the dot operator to change the value of a struct member. For example,

```
// Program to change the struct member using pointer

package main
import "fmt"

// create struct
type Weather struct{
  city string
  temperature int
}   
    
func main() {

  // create struct variable
  weather := Weather{"California", 20}
  fmt.Println("Initial Weather:", weather)

  // create struct type pointer
  ptr := &weather

  // change value of temperature to 25
  ptr.temperature = 25  

  fmt.Println("Updated Weather:", weather)

}
```

**Output**

Initial Weather: {California 20}
Updated Weather: {California 25}

In the above example, notice the line

```
ptr.temperature = 25
```

Here, we have changed the value of the struct member temperature to **25** using the pointer variable ptr.

- [](https://www.programiz.com/golang/pointers-struct#introduction)
- [](https://www.programiz.com/golang/pointers-struct#pointer-struct)
- [](https://www.programiz.com/golang/pointers-struct#access-struct)
- [](https://www.programiz.com/golang/pointers-struct#change-struct)

[

  


](https://www.programiz.com/golang/pointers-functions "Go Pointers and Functions")