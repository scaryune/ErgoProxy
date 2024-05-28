# Go range

In Go, we use `range` with the for loop to iterate through the elements of array, string, or map.

Before you learn about `range`, make sure you know the working of [Golang for loop](http://www.programiz.com/golang/for-loop).

---

## Go for range with Array

We can use the `for range` loop to access the individual index and element of an array. For example,

```
// Program using range with array

package main
import "fmt"
 
func main() {
 
  // array of numbers
  numbers := [5]int{21, 24, 27, 30, 33}
 
  // use range to iterate over the elements of array
  for index, item := range numbers {
    fmt.Printf("numbers[%d] = %d \n", index, item)
  }

}
```

**Output**

numbers[0] = 21 
numbers[1] = 24 
numbers[2] = 27 
numbers[3] = 30 
numbers[4] = 33

In the above example, we have used the `for range`

```
for index, item := range numbers {
```

Here, the `range` keyword returns two items:

- **array index**: 0, 1, 2, and so on.
- **array element at corresponding index**: 21, 24, 27, and so on.

To learn more about arrays, visit [_Golang arrays_](https://www.programiz.com/golang/arrays)_._

---

## range with string in Golang

In Go, we can also use the `for range` keyword with string to access individual characters of a string along with their respective index. For example,

```
// Program using range with string

package main
import "fmt"

func main() {
  string := "Golang"
  fmt.Println("Index: Character")

  // i access index of each character
  // item access each character
  for i, item := range string {
    fmt.Printf("%d= %c \n", i, item)
  }

}
```

**Output**

Index: Character
0: G
1: o
2: l
3: a
4: n
5: g

In the above example, we have used the `for range` to access the individual characters of the string **Golang** along with their respective index.

To learn more about strings, visit [_Golang string_](https://www.programiz.com/golang/string).

---

## for range with Go map

In Go, we can also use the `for range` keyword with map to access key-value pairs. For example,

```
// Program using range with map

package main
import "fmt"

func main() {

  // create a map
  subjectMarks := map[string]float32{"Java": 80, "Python": 81, "Golang": 85}
  fmt.Println("Marks obtained:")

  // use for range to iterate through the key-value pair
  for subject, marks := range subjectMarks {
    fmt.Println(subject, ":", marks)
  }

}
```

**Output**

Marks Obtained:
Java: 80
Python: 81
Golang: 85

In every iteration, the loop iterates through the key-value pair of a map.

|Iteration|Subject|Marks|
|---|---|---|
|1|**Java**|**80**|
|2|**Python**|**81**|
|3|**Golang**|**85**|

To learn more about map, visit [_Golang map_](https://www.programiz.com/golang/map).

---

### Access keys of Map using Go range

We can also use the `for range` to only access the keys of a map. For example,

```
// Program to retrieve the keys of a map

package main
import "fmt"

func main() {

  // create a map
  subjectMarks := map[string]float32{"Java": 80, "Python": 81, "Golang": 85}

  fmt.Println("Subjects:")
  for subject := range subjectMarks {
    fmt.Println( subject)
  }
}
```

**Output**

Subjects:
Java
Python
Golang

Here, we have used `range` to retrieve just the keys **"Java"**, **"Python"**, **"Golang"** of a map subjectMarks.

- [](https://www.programiz.com/golang/range#range-arrays)
- [](https://www.programiz.com/golang/range#range-string)
- [](https://www.programiz.com/golang/range#range-map)
- [](https://www.programiz.com/golang/range#key-map)

[

  


](https://www.programiz.com/golang/while-loop "Go while Loop")