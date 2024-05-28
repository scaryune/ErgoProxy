# Rust File Handling

In computer programming, file handling is a way to deal with data in a file. File handling enables us to open, read, write, create and update files on the local system.

File handling is commonly performed by many applications including databases, web servers. It is an important example of how I/O (Input/Output) operations work.

File handling is also generally known as File I/O.

---

## File Struct in Rust

In Rust, the `std::fs::File` struct represents a file. It allows us to perform read/write operations on a file.

The file I/O is performed through the `std::fs` module which provides functions for working with the file system.

All methods in the `File` struct return a variant of the `std:io::Result` or simply the `Result` enum.

Let's look at the basics of file I/O in Rust with these operations:

- Opening a file
- Reading from a file
- Writing to a file
- Removing a file
- Appending to a file

---

## Opening a File in Rust

To open a file in Rust, we use the `File::open()` method. This method takes a file path as an argument and returns a `File` object. If the file does not exist, it returns an error (`Err`).

Let's look at an example.

```
use std::fs::File;

fn main() {
    // Open a file in read only mode in the local file system
    let data_result = File::open("data.txt");

    // Reading a file returns a Result enum
    // Result can be a file or an error
    let data_file = match data_result {
        Ok(file) => file,
        Err(error) => panic!("Problem opening the data file: {:?}", error),
    };

    println!("Data file: {:?}", data_file);
}
```

**Output**

Data file: File { fd: 3, path: "/code/rust-practice/data.txt", read: true, write: false }

Here, we import the module `std::fs::File` on the top of the program to use the file I/O functions.

To open a file, we call `File::open("data.txt")` which reads the `data.txt` file in the local file system.

The `open()` function returns a `Result` enum which will return the `File` object or an `Err`.

Then, we pattern match the `data_result` variable and `panic!` if there is an error with opening the file. If opening the file doesn't error, we output the `File` object.

---

## Reading a File in Rust

To read a file in Rust, we use the `read_to_string()` method of the `std::io:Read` trait. This method reads all bytes until end of file (EOF) and copies it to a mutable string.

Here's an example.

```
use std::fs::File;
use std::io::Read;

fn main() {
    // Read a file in the local file system
    let mut data_file = File::open("data.txt").unwrap();

    // Create an empty mutable string
    let mut file_content = String::new();

    // Copy contents of file to a mutable string
    data_file.read_to_string(&mut file_content).unwrap();

    println!("File content: {:?}", file_content);
}
```

**Output**

File content: "The quick brown fox jumps over the lazy dog.\n"

Here, we import two modules: `std::fs::File` and `std::io::Read` for reading a file. We first open the file `data.txt` with `File::open("data.txt")` method call and bind its result to a variable `data_file`.

Once we open the file, we use the `read_to_string()` method which takes an empty mutable string `file_content` as an argument and copies the content of the file `data.txt` to `file_content`.

**Note:**

- We use `unwrap()` twice to get the result from the method calls. `unwrap()` is a utility method to work with `Option` and `Result` type. To learn more, visit [_Rust unwrap() and expect()_](https://www.programiz.com/rust/unwrap-and-expect).
- `read_to_string()` comes from the `std::io::Read` trait. To learn more, visit [_Rust Trait_](https://www.programiz.com/rust/trait).

---

## Writing to a File in Rust

To write to a file in Rust, we can use the `write()` method from the `std::io:Write` trait. This method writes contents to a file.

Let's look at an example.

```
use std::fs::File;
use std::io::Write;

fn main() {
    // Create a file
    let mut data_file = File::create("data.txt").expect("creation failed");

    // Write contents to the file
    data_file.write("Hello, World!".as_bytes()).expect("write failed");

    println!("Created a file data.txt");
}
```

**Output**

Created a file data.txt

Here, we import `std::fs::File` and `std::io::Write` modules for writing to a file. We first create a file `data.txt` with the `File::create("data.txt")` method and bind it to a mutable variable `data_file`.

After we create a file, we write to the file using the `write()` method with the content `"Hello, World!"`.

---

## Removing a File in Rust

To remove or delete a file in Rust, we can use the `remove_file()` method from the `std::fs` module.

For example,

```
use std::fs;

fn main() {
    // Remove a file
    fs::remove_file("data.txt").expect("could not remove file");
    
    println!("Removed file data.txt");
}
```

**Output**

Removed file data.txt

Here, we import the `std::fs` module for deleting a file. We use the `remove_file()` method to delete the file `data.txt`.

If the operation does not proceed, we return a custom message: `could not remove file` in case of an error.

If the file `data.txt` is not found or cannot be removed, we encounter an error.

thread 'main' panicked at 'could not remove file: Os { code: 2, kind: NotFound, message: "No such file or directory" }', src/main.rs:5:33

---

## Appending to a File in Rust

To append to a file in Rust, we should open the file in append mode. We can use the `append()` method in `std::fs::OpenOptions` which opens a file for appending.

Then, we can use the `write()` method in `std::io::Write` trait to write data to the file.

Let's look at an example.

```
use std::fs::OpenOptions;
use std::io::Write;

fn main() {
    // Open a file with append option
    let mut data_file = OpenOptions::new()
        .append(true)
        .open("data.txt")
        .expect("cannot open file");

    // Write to a file
    data_file
        .write("I am learning Rust!".as_bytes())
        .expect("write failed");

    println!("Appended content to a file");
}
```

**Output**

Appended to a file

Here, we import the `std::fs::OpenOptions` and `std::io::Write` modules for appending to a file.

The `OpenOptions::new()` and the `append(true)` method opens the file `data.txt` for appending.

Next, we use the `write()` method from the `File` object to write additional content `"I am learning Rust!"` to the file.

To deal with the errors, we chain the `expect()` method with a custom error message.

- [](https://www.programiz.com/rust/file-handling#introduction)
- [](https://www.programiz.com/rust/file-handling#file-struct)
- [](https://www.programiz.com/rust/file-handling#opening-a-file)
- [](https://www.programiz.com/rust/file-handling#reading-a-file)
- [](https://www.programiz.com/rust/file-handling#writing-to-a-file)
- [](https://www.programiz.com/rust/file-handling#removing-a-file)
- [](https://www.programiz.com/rust/file-handling#appending-to-a-file)