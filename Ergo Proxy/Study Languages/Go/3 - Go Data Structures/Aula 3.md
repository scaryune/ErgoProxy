# Go map

In Go, the map data structure stores elements in **key/value pairs**. Here, **keys** are unique identifiers that are associated with each **value** on a map.

**Create a map in Golang**

The syntax to create a Go map is:

```
subjectMarks := map[string]float32{"Golang": 85, "Java": 80, "Python": 81}
```

This code creates a map named subjectMarks. Here,

- `[string]` - indicates that keys of the map are of string type
- `float32` - indicates that values of the map are of float type
- `{Golang", "Java", "Python"}` - keys of the map
- `{85, 80, 81}` - values of the map

---

## Example: Map in Golang

```
// Program to create a map and print its keys and values

package main
import "fmt"

func main() {

  // create a map
  subjectMarks := map[string]float32{"Golang": 85, "Java": 80, "Python": 81}

  fmt.Println(subjectMarks)
}
```

**Output**

map[Golang:85 Java:80 Python:81]

Here, we have created a map and printed the key-values of a map.

**Note:** We can also create a map using `var` keyword. For example,

```
var subjectMarks = map[string]float32{"Golang": 85, "Java": 80, "Python": 81}
```

---

## Access Values of a Map in Golang

We can access the value of a map by using the corresponding key. For example,

```
package main
import "fmt"

func main() {

  // create a map
  flowerColor := map[string]string{"Sunflower": "Yellow", "Jasmine": "White", "Hibiscus": "Red"}

  // access value for key Sunflower
  fmt.Println(flowerColor["Sunflower"])  // Yellow

  // access value for key Hibiscus
  fmt.Println(flowerColor["Hibiscus"])  // Red

}
```

Here, we have used expressions

- `flowerColor["Sunflower"]` to access the value of the key `Sunflower`
- `flowerColor["Hibiscus"]` to access the value of the key `Hibiscus`

---

## Change value of a map in Golang

To change the value of a map, we can directly assign a new value to the corresponding key. For example,

```
package main
import "fmt"

func main() {

  // create a map
  capital := map[string]string{ "Nepal": "Kathmandu", "US": "New York"}
  fmt.Println("Initial Map: ", capital)

  // change value of US to Washington DC
  capital["US"] = "Washington DC"

  fmt.Println("Updated Map: ", capital)
}
```

**Output**

Initial Map:  map[Nepal: Kathmandu US: New York]
Updated Map:  map[Nepal: Kathmandu US: Washington DC]

In the above example, we have changed the value of a map by re-assigning the key **"US"** with a new value **"Washington DC"**

---

## Add Element of Go Map Element

So far, we have created a map with a predefined set of elements. However, we can also add elements to a map.

To add an element, we can assign a new value along with a new key. For example,

```
package main
import "fmt"

func main() {

  // create a map
  students := map[int]string{1: "John", 2: "Lily"}
  fmt.Println("Initial Map: ", students)

  // add element with key 3
  students[3] = "Robin"

  // add element with key 5
  students[5] = "Julie"

  fmt.Println("Updated Map: ", students)
}
```

**Output**

Initial Map:  map[1:John 2:Lily]
Updated Map:  map[1:John 2:Lily 3:Robin 5:Julie]

Here, the code

- `students[3] = "Robin"` - adds a new element with key **3** and value `Robin`
- `students[5] = "Julie"` - adds a new element with key **5** and value `Julie`

---

## Delete Element of Go Map Element

To delete an element of the map, we can use the `delete()` function. For example,

```
package main
import "fmt"

func main() {

  // create a map
  personAge := map[string]int{"Hermione": 21, "Harry": 20, "John": 25}
  fmt.Println("Initial Map: ", personAge)

  // remove element of map with key John
  delete(personAge, "John")

  fmt.Println("Updated Map: ", personAge)
}
```

**Output**

Initial Map:  map[Harry:20 Hermione:21 John:25]
Updated Map:  map[Harry:20 Hermione:21]

Here, we have used the `delete()` function to remove the element denoted by the key **"John"**.

```
delete(personAge, "John")
```

The function takes two arguments:

- `personAge` - name of the map
- `John` - key of the element which is to be deleted

**Note:** If the key passed to the `delete()` function is not present inside the map, the function does nothing.

---

## Looping through the map in Golang

We can use a [Go for range loop](https://www.programiz.com/golang/range) to iterate through each element of the map. For example,

```
package main
import "fmt"

func main() {

  // create a map
  squaredNumber := map[int]int{2: 4, 3: 9, 4: 16, 5: 25}

  // for-range loop to iterate through each key-value of map
  for number, squared := range squaredNumber {
    fmt.Printf("Square of %d is %d\n", number, squared)
  }

}
```

**Output**

Square of 2 is 4
Square of 3 is 9
Square of 4 is 16
Square of 5 is 25

In the above code, the for range loop accesses each key/value pair of the map.

**Working of the for range loop**

|Iteration|number|squared|
|---|---|---|
|1|**2**|**4**|
|2|**3**|**9**|
|3|**4**|**16**|
|4|**5**|**25**|

**Note:** We have used the [Printf()](https://www.programiz.com/golang/print-statement#go-printf) function to make our output look much cleaner and understandable.

---

## Frequently Asked Questions

Create Go Map using the make() function

Access Keys of a Golang Map

Access Values of a Go Map using blank identifier