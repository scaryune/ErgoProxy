# Go struct

A struct is used to store variables of different data types. For example,

Suppose we want to store the name and age of a person. We can create two variables: name and age and store value.

However, suppose we want to store the same information of multiple people.

In this case, creating variables for a person might be a tedious task. We can create a struct that stores the name and age to overcome this.

And, we can use this same struct for every person.

---

## Declare Go Struct

The syntax to declare a struct in Go is:

```
type StructureName struct {
  // structure definition 
}
```

Here,

1. `struct` - keyword used to define a structure
2. `StructName` - the name of the structure

Let's see an example,

```
type Person struct {
  name string
  age  int
}
```

Here, we have declared a struct named Person. Inside the curly braces `{}`, the struct contains two variables name and age.

---

## Struct instances

A struct definition is just a blueprint. To use a struct, we need to create an instance of it. For example,

```
type Person struct {
  name string
  age  int
}

// create an instance of struct
var person1 Person
```

Here, we have created an instance `person1` followed by the name of the struct `Person`.

Now, we can use the person1 instance to access and define the struct properties.

```
// define the value of name and age
person1 = Person("John", 25)
```

We can also directly define a struct while creating an instance of the struct. For example,

```
person1 := Person("John", 25)
```

Here, **John** will be assigned to the name variable and **25** will be assigned to the age variable of the Person struct.

---

## Example: Golang struct

```
package main
import "fmt"

func main() {

  // declare a struct
  type Person struct {
    name string
    age  int
  }

  // assign value to struct while creating an instance
  person1 := Person{ "John", 25}
  fmt.Println(person1)

  // define an instance
  var person2 Person

  // assign value to struct variables
  person2 = Person {
    name: "Sara",
    age: 29,
  }

  fmt.Println(person2)
}
```

**Output**

{John 25}
{Sara 29}

---

## Access a struct in Golang

We can access individual elements of a struct using the struct instances. For example,

```
// Program to access the individual elements of struct

package main
import "fmt"

func main() {

  // declare a struct
  type Rectangle struct {
    length  int
    breadth int
}

  // declare instance rect1 and defining the struct
  rect := Rectangle{22, 12}

  // access the length of the struct
  fmt.Println("Length:", rect.length)

  // access the breadth of the struct
  fmt.Println("Breadth:", rect.breadth)
  
  area := rect.length * rect.breadth
  fmt.Println("Area:", area)

}
```

**Output**

Length: 22
Breadth: 12
Area: 264

Here, we have used the `.` (dot) symbol to access the property of a struct.

- `rect.length` - access the value of the length variable from the struct
- `rect.breadth` - access the value of the breadth variable from the struct

---

## Function inside a Struct in Go

Go also allows us to create a function inside a struct. It treats function as a field of struct. For example,

```
// Program to use function as a field  of struct

package main
import "fmt"

// initialize the function Rectangle
type Rectangle func(int, int) int

// create structure
type rectanglePara struct {
  length  int
  breadth int
  color   string

  // function as a field of struct
  rect Rectangle
}

func main() {

  // assign values to struct variables
  result := rectanglePara{
    length:  10,
    breadth: 20,
    color:   "Red",
    rect: func(length int, breadth int) int {
      return length * breadth
    },
  }

  fmt.Println("Color of Rectangle: ", result.color)
  fmt.Println("Area of Rectangle: ", result.rect(result.length, result.breadth))
}
```

**Output**

Color of Rectangle:  Red
Area of Rectangle:  200

In the above example, we have defined a function Rectangle as a field of struct rectanglePara and used the function to find the area of a rectangle.

---

- [](https://www.programiz.com/golang/struct#introduction)
- [](https://www.programiz.com/golang/struct#define-structure)
- [](https://www.programiz.com/golang/struct#instance)
- [](https://www.programiz.com/golang/struct#example)
- [](https://www.programiz.com/golang/struct#access-struct)