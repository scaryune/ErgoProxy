# Rust Struct

Rust structs or structures are user-defined data types used to store different types of data together.

Suppose we want to store a person's name, age, and height. To do this, we can create variables for each property/field.

```
let personName: String = String::from("John Doe");
let personAge: u8 = 18;
let personHeight: u8 = 178;
```

The problem with this approach is we have to maintain all these variables separately. To store these fields for more than one person, we will have to create different variables for each person.

Instead, we can create a struct to store all the fields together as a single unit. For example,

```
struct Person {
    name: String,
    age: u8,
    height: u8
}
```

---

## Defining a Struct in Rust

In Rust, we use the `struct` keyword to define a structure. The syntax of a structure is:

```
struct struct_name {
    field1: data_type,
    field2: data_type,
    field3: data_type
}
```

Here,

- `struct` - keyword to define a structure
- `struct_name` - name of the structure
- `field1: data_type/field2: data_type` - name and data type of the fields inside the struct.

Let's look at an example.

```
struct Person {
    name: String,
    age: u8,
    height: u8
}
```

Here, we have defined a structure named `Person`. It contains three fields:

- `name` - with data type `String`
- `age` - with data type `u8`
- `height` - with data type `u8`

---

## Instantiating Rust Struct

To use a structure in Rust, we first have to create an instance of structures. For example,

```
// define a structure
struct Person {
    name: String
    age: u8,
    height: u8
}

// create an instance of Person struct
let person1 = Person {
    ...
};
```

Here, `Person {...}` creates an instance of the **Person struct**, and we have assigned it to the person1 variable.

We can also assign values to the struct fields while creating the instance. For example,

```
let person1 = Person {
    name: String::from("John Doe"),
    age: 18,
    height: 178
};
```

Here, we have initialized the values of the `name`, `age` and `height` fields of the Person struct. This process of initializing the values of struct fields is known as an **instantiation of a struct**.

**Note:** The struct definition is a template, and the struct instances fill in that template with data.

---

## Accessing Fields of a Struct

We can use the struct instance along with the dot `.` notation to access values of fields in a structure. For example,

```
fn main() {
    // define a Person struct
    struct Person {
        name: String,
        age: u8,
        height: u8
    }
    
    // instantiate Person struct
    let person = Person {
        name: String::from("John Doe"),
        age: 18,
        height: 178
    };
    
    // access value of name field in Person struct
    println!("Person name = {}", person.name);

    // access value of age field in Person struct
    println!("Person age = {}", person.age);

    // access value of height field in Person struct
    println!("Person height = {}", person.height);
}
```

**Output**

Person name = John Doe
Person age = 18
Person height = 178

Here,

- `person.name` - reads the field `name` of the Person struct (`John Doe`)
- `person.age` - reads the field `age` (`18`)
- `person.height` - reads the field `height` (`178`)

---

## Destructuring Fields of a Rust Struct

Destructuring is the process of breaking down fields of a data type (array, tuple, etc.) into smaller variables. We can break down the struct fields into smaller variables in Rust.

Suppose we have a struct and a struct instance,

```
struct Person {
    name: String,
    age: u8,
    height: u8
}

let person = Person {
    name: String::from("John Doe"),
    age: 18,
    height: 178
};
```

We can now perform destructuring using:

```
// destructuring the Person struct
let Person { name, age, height } = person;
```

Now, we access the `name`, `age` and `height` fields using the field names directly:

- `name` instead of `person.name`
- `age` instead of `person.age`
- `height` instead of `person.height`

However, you should note that the name of the variables while destructuring should be the same as the name of the fields.

---

### Example: Destructuring Fields of Struct

```
fn main() {
    // define a Person struct
    struct Person {
        name: String,
        age: u8,
        height: u8
    }
    
    // instantiate Person struct
    let person = Person {
        name: String::from("John Doe"),
        age: 18,
        height: 178
    };
    
    // destructure Person struct into name, age and height variables
    let Person { name, age, height } = person;
    
    println!("Person name = {}", name);
    println!("Person age = {}", age);
    println!("Person height = {}", height);
}
```

**Output**

Person name = John Doe
Person age = 18
Person height = 178

Here, the destructing happens with this expression,

```
let Person { name, age, height } = person;
```

The pattern on the left has declarations, and the right side of the expression has a struct instance.

On the left side of the expression, we are making `let` declarations for the `Person` struct with field `name`, `age` and `height`. On the right side of the expression, we assign the instantiated struct of the `Person`.

As a result, we get the `name`, `age` and `height` of the person and print it to the screen.

---

## Frequently Asked Questions

How to create a mutable struct in Rust?

What are tuple structs?

- [](https://www.programiz.com/rust/struct#introduction)
- [](https://www.programiz.com/rust/struct#defining-a-structure)
- [](https://www.programiz.com/rust/struct#instantiating-structures)
- [](https://www.programiz.com/rust/struct#accessing-fields)
- [](https://www.programiz.com/rust/struct#destructuring-fields)

[

  


](https://www.programiz.com/rust/tuple "Rust Tuple")