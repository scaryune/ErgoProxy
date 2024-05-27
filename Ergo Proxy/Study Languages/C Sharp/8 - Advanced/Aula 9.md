# C# Files

C# provides the `File` class which is used to perform various operations like creating a file, opening a file, reading and writing a file etc.

---

## What are Files and Directory ?

A **file** is a named location that can be used to store related information. For example,

`program.cs` is a C# file that contains information about the C# program.

A **directory** is a collection of files and subdirectories. A directory inside a directory is known as a subdirectory.

---

## Working with Files in C#

C# provides a `System.IO` namespace that contains several classes that are used to perform operations on files and dictionaries.

![classes under system.io namespace that works with files and dictionaries](https://www.programiz.com/sites/tutorial2program/files/csharp-system-io-namespace.png "Some classes under System.IO namespace")

Some classes under System.IO namespace

The above image shows some of the classes under the `System.IO` namespace. Among these classes, we will learn about the `File` class and it's methods to work with files in C#.

---

## C# File Class and Its Methods

The `File` class provides us built-in methods that allow us to perform input / output operations on files. Some of the commonly used methods are:

|Methods|Use|
|---|---|
|`Create()`|Create or overwrite a file in the specified path.|
|`Open()`|Opens a `FileStream` on the specified path with read / write access|
|`WriteAllText()`|Create a new file, writes the specified string to the file, and then closes the file|
|`ReadAllText()`|Opens a text file, reads all lines of the file, and then closes the file.|
|`Copy()`|Copies an existing file to a new file. Overwriting a file of the same name is not allowed.|
|`AppendAllText()`|Opens a file, appends the specified string to the file, and then closes the file. If the file does not exist, this method creates a file, writes the specified string to the file, then closes the file.|

---

## Create a File in C#

We use the `Create()` method of the `File` class to create a new file in C#. For example,

```
// create a file at pathName
FileStream fs = File.Create(pathName);
```

Here, the `File` class creates a file at `pathName`.

**Note:** If the file already exists, the `Create()` method overwrites the file.

---

## Example: Create a File

```
using System;
using System.IO;
class Program
{
    static void Main()
    {
        // path of the file that we want to create
        string pathName = @"C:\Program\myFile.txt";

        // Create() creates a file at pathName 
        FileStream fs = File.Create(pathName);

        // check if myFile.txt file is created at the specified path 
        if (File.Exists(pathName))
        {
            Console.WriteLine("File is created.");
        }
        else
        {
            Console.WriteLine("File is not created.");
        }
    }
}
```

**Output**

File is created.

In the above example, we have created a file `myFile.txt` at `C:\Program` directory using the `Create()` method.

After creating the file, notice that we have used the `Exists()` method to check whether the file `myFile.txt` exists or not.

**Note:** The `"@"` in front of `"C:\Program\myFile.txt"` indicates this as a verbatim string. We use verbatim string to tell the compiler to ignore escape character `\`.

---

## Open a File

We use the `Open()` method of the `File` class to open an existing file in C#. The method opens a `FileStream` on the specified file. For example,

```
using System;
using System.IO;
class Program
{
    static void Main()
    {
        string pathName = @"C:\Program\myFile.txt";

       // open a file at pathName 
        FileStream fs = File.Open(pathName, FileMode.Open);
    }
}
```

In the above example, notice the code,

```
// opens the file at pathName
FileStream fs = File.Open(pathName, FileMode.Open);
```

Here, the `Open()` method opens `myFile.txt` file. Here, `FileMode.Open` specifies - **open the existing file**.

**Note:** A file stream is a sequence of bytes used to hold file data. Every file contains at least one file stream.

---

## Write to a File

We use the `WriteAllText()` method of the `File` class to write to a file. The method creates a new file and writes content to that file.

Let's see an example to write to a file in C#.

```
using System;
using System.IO;
class Program
{
    static void Main()
    {
        string pathName = @"C:\Program\myFile.txt";

        // create a file at pathName and write "Hello World" to the file
        File.WriteAllText(pathName, "Hello World");
    }
}
```

In the above example, notice the code,

```
File.WriteAllText(pathName, "Hello World");
```

Here, the `WriteAllText()` method creates `myFile.txt` at `C:\Program` directory and writes `"Hello World"` to the file.

![the method writes text in a file](https://www.programiz.com/sites/tutorial2program/files/csharp-write-in-file.png "Writing text in a File")

Writing text in a File

The above image shows the `myFile.txt` file that contains the text `"Hello World"`.

**Note:** If the file already exists, the `WriteAllText()` method overwrites the file.

---

## Read a File in C#

We use the `ReadAllText()` method of the `File` class to read contents of the file. The method returns a string containing all the text in the specified file.

Let's read the content of the file `myFile.txt` where we had written `"Hello World"`.

```
using System;
using System.IO;
class Program
{
    static void Main()
    {
        string pathName = @"C:\Program\myFile.txt";

        // read the content of myFile.txt file
        string readText = File.ReadAllText(pathName);

        Console.WriteLine(readText);
    }
}
```

**Output**

Hello World

In the above example, notice the code,

```
// read the content of myFile.txt file
string readText = File.ReadAllText(pathName);
```

The `ReadAllText()` method reads the file `myFile.txt` and returns `"Hello World"`.

- [](https://www.programiz.com/csharp-programming/files#introduction)
- [](https://www.programiz.com/csharp-programming/files#what-are-files)
- [](https://www.programiz.com/csharp-programming/files#working-with-files)
- [](https://www.programiz.com/csharp-programming/files#file-class-and-its-methods)
- [](https://www.programiz.com/csharp-programming/files#create-a-file)
- [](https://www.programiz.com/csharp-programming/files#example-create-a-file)
- [](https://www.programiz.com/csharp-programming/files#open-a-file)
- [](https://www.programiz.com/csharp-programming/files#write-to-a-file)
- [](https://www.programiz.com/csharp-programming/files#read-a-file)

[

  


](https://www.programiz.com/csharp-programming/regex "C# regex")