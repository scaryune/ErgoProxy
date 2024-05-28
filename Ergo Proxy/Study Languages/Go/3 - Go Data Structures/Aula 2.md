# Go Slice

Slice is a collection of similar types of data, just like arrays.

However, unlike arrays, slice doesn't have a fixed size. We can add or remove elements from the array.

### Create slice in Golang

Here's how we create a slice in Golang:

```
numbers := []int{1, 2, 3, 4, 5}
```

Here,

- `numbers` - the name of the slice
- `int` - represents that the slice only includes integer numbers
- `{1, 2, 3, 4, 5}` - elements of the slice

You might have noticed that we have left the `[]` notation empty. This is because we can add elements to a slice that will change its size.

**Note**: If we provide size inside the `[]` notation, it becomes an array. For example,

```
// this is an array
numbers := [5]int{1, 2, 3, 4, 5}

// this is a slice
numbers := []int{1, 2, 3, 4, 5}
```

---

## Example Golang Slice

```
// Program to create a slice and print its elements

package main
import "fmt"

func main() {

  // declare slice variable of type integer
  numbers := []int{1, 2, 3, 4, 5}

  // print the slice
  fmt.Println("Numbers: ", numbers)
}
```

**Output**

Numbers: [1 2 3 4 5]

In the above example, we have created a slice named numbers. Here, `int` specifies that the slice numbers can only store integers.

**Note:** We can also create a slice using the `var` keyword. For example,

```
var numbers = []int{1, 2, 3, 4}
```

---

## Create slice from an array in Golang

In Go programming, we can also create a slice from an existing array. For example,

Suppose we have an array of numbers

```
numbers := [8]int{10, 20, 30, 40, 50, 60, 70, 80}
```

Now, we can slice the specified elements from this array to create a new slice.

```
sliceNumbers = numbers[4, 7]
```

Here,

- **4** is the start index from where we are slicing the array element
- **7** is the end index up to which we want to get array elements

While creating a slice from an array, the start index is inclusive and the end index is exclusive. Hence, our slice will include elements `[50, 60, 70]`.

---

### Example: Create Slice from Array in Go

```
// Program to create a slice from an array

package main
import "fmt"

func main() {

  // an integer array
  numbers := [8]int{10, 20, 30, 40, 50, 60, 70, 80}

  // create slice from an array
  sliceNumbers := numbers[4 : 7]

  fmt.Println(sliceNumbers)

}
```

**Output**

[50, 60, 70]

---

## Slice Functions

In Go, slice provides various built-in functions that allow us to perform different operations on a slice.

|Functions|Descriptions|
|---|---|
|`append()`|adds element to a slice|
|`copy()`|copy elements of one slice to another|
|`Equal()`|compares two slices|
|`len()`|find the length of a slice|

---

## Adds Element to a Slice

We use the `append()` function to add elements to a slice. For example,

```
// Program to add elements to a slice

package main
import "fmt"

func main() {
  primeNumbers := []int{2, 3}
  
  // add elements 5, 7 to the slice
  primeNumbers = append(primeNumbers, 5, 7)
  fmt.Println("Prime Numbers:", primeNumbers)
}
```

**Output**

Prime Numbers: [2 3 5 7]

Here, the code

```
primeNumbers = append(primeNumbers, 5, 7)
```

adds elements **5** and **7** to the primeNumbers.

We can also add all elements of one slice to another slice using the `append()` function. For example,

```
// Program to add elements of one slice to another

package main
import "fmt"

func main() {
  
  // create two slices
  evenNumbers := []int{2, 4}
  oddNumbers := []int{1, 3}  
  
  // add elements of oddNumbers to evenNumbers
  evenNumbers = append(evenNumbers, oddNumbers...)
  fmt.Println("Numbers:", evenNumbers)
}
```

**Output**

Numbers: [2 4 1 3]

Here, we have used `append()` to add the elements of oddNumbers to the list of evenNumbers elements.

---

### Copy Golang Slice

We can use the `copy()` function to copy elements of one slice to another. For example,

```
// Program to copy one slice to another

package main
import "fmt"

func main() {

  // create two slices
  primeNumbers := []int{2, 3, 5, 7}
  numbers := []int{1, 2, 3}

  // copy elements of primeNumbers to numbers
  copy(numbers, primeNumbers)

  // print numbers
  fmt.Println("Numbers:", numbers)
}
```

**Output**

Numbers: [2 3 5]

In the above example, we are copying elements of primeNumbers to numbers.

```
copy(numbers, primeNumbers)
```

Here, only the first 3 elements of primeNumbers are copied to numbers. This is because the size of numbers is 3 and it can only hold 3 elements.

The `copy()` function replaces all the elements of the destination array with the elements.

---

## Find the Length of a Slice

We use the `len()` function to find the number of elements present inside the slice. For example,

```
// Program to find the length of a slice

package main
import "fmt"

func main() {

  // create a slice of numbers
  numbers := []int{1, 5, 8, 0, 3}

  // find the length of the slice
  length := len(numbers)

  fmt.Println("Length:", numbers)

}
```

**Output**

Length: 5

---

## Looping through Go Slice

In Go, we can use a `for` loop to iterate through a slice. For example,

```
// Program that loops over a slice using for loop

package main
import "fmt"

func main() {
  numbers := []int{2, 4, 6, 8, 10}

  // for loop that iterates through the slice
  for i := 0; i < len(numbers); i++ {
    fmt.Println(numbers[i])
  }

}
```

**Output**

2
4
6
8
10

Here, `len()` function returns the size of a slice. The size of a slice numbers is **5**, so the `for` loop iterates 5 times.

---

## Frequently Asked Questions

Access elements of a slice

![Elements of slice with its respective index.](https://www.programiz.com/sites/tutorial2program/files/go-slice-index.png "Elements of slice with its respective index.")

Change elements of a slice

Create a slice using make() function

Looping through a slice using for range