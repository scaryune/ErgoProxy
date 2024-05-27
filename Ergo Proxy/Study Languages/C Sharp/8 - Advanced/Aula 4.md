# C# generics

C# Generics allow us to create a single class or method that can be used with different types of data. This helps us to reuse our code.

Here, we will learn to create generics class and method in C#.

---

## C# generics Class

A generics class is used to create an instance of any data type. To define a generics class, we use angle brackets (`<>`) as,

```
class Student<T>
{
  // block of code 
}
```

Here, we have created a generics class named `Student`. `T` used inside the angle bracket is called the **type parameter**.

While creating an instance of the class, we specify the data type of the object which replaces the type parameter.

### Create an Instance of Generics Class

Let's create two instances of the generics class.

```
// create an instance with data type string
Student<string> studentName = new Student<string>();
```

```
// create an instance with data type int
Student<int> studentId = new Student<int>();
```

Here, we have created two instances named `studentName` and `studentId` with data types `string` and `int`, respectively.

During the time of compilation, the type parameter `T` of the `Student` class is replaced by,

- `string` - for instance `studentName`
- `int` - for instance `studentId`

---

## Example: C# generics Class

```
using System;
// define a generics class named Student
public class Student<T>
{
    // define a variable of type T 
    public T data;

    // define a constructor of the Student class 
    public Student(T data)
    {
        this.data = data;
        Console.WriteLine("Data passed: " + this.data);
    }
}

class Program
{
    static void Main()
    {
        // create an instance with data type string 
        Student<string> studentName = new Student<string>("Avicii");

        // create an instance with data type int
        Student<int> studentId = new Student<int>(23);
    }
}
```

**Output**

Data passed: Avicii
Data passed: 23

In the above example, we have created a generics class named `Student`. Also, we have defined a [constructor](https://www.programiz.com/csharp-programming/constructors) that prints `this` value.

Inside the `Main` class, we have created two instances of the `Student` classes: `studentName` and `studentId`.

The type parameter `T` of `Student<T>` is replaced by:

- `string` - in `studentName`
- `int` - in `studentId`

Here, the `Student` class works with both the `int` and the `string` data type.

---

## C# generics Method

Similar to the generics class, we can also create a method that can be used with any type of data. Such a class is known as the generics Method. For example,

```
public void displayData(T data) {
    Console.WriteLine("Data Passed: " + data);
}
```

Here,

- `displayData` - name of the generics method
- `T` - type parameter to specify the function can accept any type of data
- `data` - function parameter

Now we can use this function to work with any type of data. For example,

```
// calling function with integer data
obj.displayData(34);
```

```
// calling function with string data
obj.displayData("Tim");
```

---

## Example: C# generics Method

```
using System;
// define a generics class named Employee
class Employee<T>
{
    // define a generics method that displays the passed data  
    public void displayData(T data)
    {
        Console.WriteLine("The data passed is: " + data);
    }
}

class Program
{
    static void Main()
    {
        // create an instance of Employee class by specifying T as string 
        Employee<string> employeeName = new Employee<string>();

        // call displayData() generics method and pass a string value - "Jack" 
        employeeName.displayData("Jack");

        // create an instance of Employee class by specifying T as int  
        Employee<int> employeeId = new Employee<int>();

        // call displayData() generics method and pass an integer value 
        employeeId.displayData(123);
    }
}
```

**Output**

The data passed is: Jack
The data passed is: 123

In the above example, we have defined a generics method named `displayData()` inside the `Employee<T>` generics class.

---

## Example: Generics Method with Return Type

Earlier we defined a generics method without a return type. However, we can also define a generics method with a return type. For example,

```
using System;
// define a generics class named Employee
class Movie<T>
{
    // define a generics method that returns T type value    
    public T displayData(T data)
    {
        return data;
    }
}

class Program
{
    static void Main()
    {
        // create an instance with data type string 
        Movie<string> movieName = new Movie<string>();
        Console.WriteLine("Generics Method returns: " + movieName.displayData("Inception"));

        // create an instance with data type int  
        Movie<int> movieRating = new Movie<int>();
        Console.WriteLine("Generics Method returns: " + movieRating.displayData(9));
    }
}
```

**Output**

Generics Method returns: Inception
Generics Method returns: 9

In the above example, we have created a generics method named `displayData()`. Notice that, we have used `T` as a return type instead of void.

This means the method can return a value of any type.

```
public T displayData(T data) {...}
```

In our case, the method is returning,

- `string` data - `"Inception"`
- `int` data - **9**

---

## Advantages of Generics

### 1.Code Reusability

With the help of generics in C#, we can write code that will work with different types of data. For example,

```
public void displayData(T data) {...}
```

Here, we have created a generics method. This same method can be used to perform operations on integer data, string data, and so on.

### 2.Compile-time Type Checking

The type parameter of generics provides information about the type of data used in the generics code. For example,

```
// int type instance of GenericsClass
GenericsClass<int> list = new GenericsClass<>();
```

Here, we know that `GenericsClass` is working with `int` data only.

Now, if we try to pass data other than `int` to this class, the program will generate an error at compile time.

### 3.Used with Collections

The collections framework uses the concept of generics in C#. For example,

```
// create a string type List 
List<string> courseName = new List<string>();

// create an int type List 
List<int> courseId = new List<int>();
```

In the above example, we have used the same `[List](https://www.programiz.com/csharp-programming/list)` class to work with different types of data.

Similar to `List`, other collections (`[Queue](https://www.programiz.com/csharp-programming/queue)`, `[Stack](https://www.programiz.com/csharp-programming/stack)`, and so on) are also generic in C#.

---

## Frequently Asked Questions

C# Generics Method with Non-Generics Class

C# Generics Property