# Go Interface

In Go programming, we use interfaces to store a set of methods without implementation. That is, methods of interface won't have a method body. For example,

```
type Shape interface {
  area() float32
  perimeter() float32
}
```

Here, `Shape` is an interface with methods: `area()` and `perimeter()`. You can see both methods only have method signatures without any implementation.

---

## Implementation of a Go Interface

You might be wondering what is the use of interface if the methods inside it don't have any implementations.

Well, to use an interface, we first need to implement it by a type (struct). To implement an interface, a struct should provide implementations for all methods of an interface. For example,

```
package main 
import "fmt"

// interface
type Shape interface {
  area() float32
}

 // struct to implement interface
type Rectangle struct {
  length, breadth float32
}

// use struct to implement area() of interface
func (r Rectangle) area() float32 {
  return r.length * r.breadth
}

// access method of the interface
func calculate(s Shape) {
  fmt.Println("Area:", s.area())
}

// main function
func main() {
 
  // assigns value to struct members
  rect := Rectangle{7, 4}

  // call calculate() with struct variable rect
  calculate(rect)
    
}
```

**Output**

Area: 28

Let's see how this program works:

**Working on Interface Implementation**

In the above example, we have created an interface named `Shape` with a method `area()`. Here, we are trying to implement this interface by the `Rectangle` struct.

```
type Rectangle struct {
  length, breadth float32
}
```

Now, to implement the interface, we have provided the implementation for `getArea()` of the interface.

```
func (r Rectangle) area() float32 {
  return r.length * r.breadth
}
```

To access this method, we have created a `calculate()` method

```
// access method of the interface
func calculate(s Shape) {
  fmt.Println("Area: ", s.area())
}
```

Here, the method takes a variable of `Shape` named `s` and uses it to call the `area()` method.

Since the structure implements the interface, we have called `calculate()` using the variable of structure

```
rect := Rectangle{7, 4}
calculate(rect)
```

---

## Implement Go Interface by Multiple Structs

In Go, more than 1 struct can also implement a single interface. For example,

```
package main 
import "fmt"

// interface
type Shape interface {
  area() float32
}

 // Rectangle struct implements the interface
type Rectangle struct {
  length, breadth float32
}

// Rectangle provides implementation for area()
func (r Rectangle) area() float32 {
  return r.length * r.breadth
}

// Triangle struct implements the interface
type Triangle struct {
  base, height float32       
}

// Triangle provides implementation for area()
func (t Triangle) area() float32 {
    return 0.5 * t.base * t.height
}

// access method of the interface
func calculate(s Shape) float32 {
  return s.area()
}

// main function
func main() {
 
  // assigns value to struct members
  r := Rectangle{7, 4}
  t := Triangle{8, 12}
 
  // call calculate() with struct variable rect 
  rectangleArea := calculate(r)
  fmt.Println("Area of Rectangle:", rectangleArea)
  
  triangleArea := calculate(t)
  fmt.Println("Area of Triangle:", triangleArea)

}
```

**Output**

Area of Rectangle: 28
Area of Rectangle: 48

In the above example, we have used two structs: `Rectangle` and `Triangle` to implement the interface `Shape`.

Just like before, both structs provide implementation for the `area()` method.

Here, this time `calculate()` calls the `area()` using interface `Shape` and returns it.

So, for the first call, `calculate(r)`, the method will call the `area()` method implementation of `Rectangle`. Similarly, for `calculate(t)`, the method will call the `area()` method implementation of `Triangle`.

---

### What happens if the struct doesn't implement all methods of interface?

When a struct implements an interface, it should provide an implementation for all the methods of the interface. If it fails to implement any method, we will get an error. For example,

```
package main 
import "fmt"

// interface
type Shape interface {
  area() float32
  perimeter() float32
}

 // Rectangle struct implements the interface
type Rectangle struct {
  length, breadth float32
}

// Rectangle provides implementation for area()
func (r Rectangle) area() float32 {
  return r.length * r.breadth
}

// access method of the interface
func calculate(s Shape) float32 {
  return s.area()
}

// main function
func main() {
 
  // assigns value to struct members
  r := Rectangle{7, 4}

  // call calculate() with struct variable rect 
  rectangleArea := calculate(r)
  fmt.Println("Area of Rectangle:", rectangleArea)
}
```

**Output**

cannot use r (type Rectangle) as type Shape in argument to calculate:
	Rectangle does not implement Shape (missing perimeter method)

In the above example, the `Shape` interface has two methods: `area()` and `perimeter()`. Here, we are trying to implement the interface by the `Rectangle` struct.

However, the struct only provides an implementation for the `area()`. Since the struct doesn't implement all the methods of the interface, we get an error.

- [](https://www.programiz.com/golang/interface#introduction)
- [](https://www.programiz.com/golang/interface#implementation)
- [](https://www.programiz.com/golang/interface#multistruct-interface)