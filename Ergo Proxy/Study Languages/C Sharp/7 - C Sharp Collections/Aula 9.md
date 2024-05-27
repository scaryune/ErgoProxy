# C# Dictionary

A `Dictionary<TKey, TValue>` is a generic collection that consists of elements as key/value pairs that are not sorted in an order. For example,

```
Dictionary<int, string> country = new Dictionary<int, string>();
```

Here, `country` is a dictionary that contains `int` type keys and `string` type values.

---

## Create a Dictionary

To create a dictionary in C#, we need to use the `System.Collections.Generic` namespace. Here is how we can create a dictionary in C#.

```
// create a dictionary
Dictionary<dataType1, dataType2> dictionaryName = new Dictionary<dataType1, dataType2>();
```

Here,

- `dictionaryName` - name of the dictionary
- `dataType1` - datatype of keys
- `dataType2` - datatype of values

---

## Example: Create a Dictionary

```
using System;
using System.Collections;
class Program
{
    public static void Main()
    {
        // create a dictionary 
        Dictionary<int, string> country = new Dictionary<int, string>();

        // add items to dictionary
        country.Add(5, "Brazil");
        country.Add(3, "China");
        country.Add(4, "Usa");

        // print value having key is 3        
        Console.WriteLine("Value having key 3: " + country[3]);
    }
}
```

**Output**

Value having key 3: China

In the above example, we have created a dictionary named `country`.

The keys are of `int` type and values are of `string` type.

---

## Basic Operations on Dictionary

In C#, we can perform different operations on a dictionary. We will look at some commonly used `Dictionary<TKey, TValue>` operations in this tutorial:

- Add Elements
- Access Elements
- Change Elements
- Remove Elements

Let's see how we can perform these operations in detail.

---

## Add Elements in Dictionary

C# provides the `Add()` method using which we can add elements in the dictionary. For example,

```
using System;
using System.Collections;
class Program
{
    public static void Main()
    {
        // create a dictionary 
        Dictionary<string, string> mySongs = new Dictionary<string, string>();

        // add items to dictionary
        mySongs.Add("Queen", "Break Free");
        mySongs.Add("Free", "All right now");
        mySongs.Add("Pink Floyd", "The Wall");

    }
}
```

In the above example, we have created a `Dictionary<TKey, TValue>` named `mySongs`.

Here we have added key/value pairs using the `Add()` method where,

- keys - `"Queen"`, `"Free"` and `"Pink Floyd"`
- values - `"Break Free"`, `"All right now"` and `"The Wall"`

---

## Another way to add Elements to Dictionary

Add Elements in a dictionary without using`Add()`method

---

## Access Dictionary Elements

We can access the elements inside the dictionary using it's keys. For example,

```
using System;
using System.Collections;
class Program
{
    public static void Main()
    {
        // create a dictionary 
        Dictionary<string, string> student = new Dictionary<string, string>();

        // add items to dictionary
        student.Add("Name", "Susan");
        student.Add("Faculty", "History");

        // access the value having key "Name"
        Console.WriteLine(student["Name"]);

        // access the value having key "Faculty"
        Console.WriteLine(student["Faculty"]);
    }
}
```

**Output**

Susan
History

In the above example, we have accessed the values of the dictionary using their keys:

- `student["Name"]` - accesses the value whose key is `"Name"`
- `student["Faculty"]` - accesses the value whose key is `"Faculty"`

---

## Iterate through Dictionary

In C#, we can also loop through each element of the dictionary using a `foreach` loop. For example,

```
using System;
using System.Collections;
class Program
{
    public static void Main()
    {
        // create a dictionary 
        Dictionary<string, string> car = new Dictionary<string, string>();

        // add items to dictionary
        car.Add("Model", "Hyundai");
        car.Add("Price", "36K");

        // iterate through the car dictionary 
        foreach (KeyValuePair<string, string> items in car)
        {
            Console.WriteLine("{0} : {1}", items.Key, items.Value);
        }
    }
}
```

**Output**

Model : Hyundai
Price : 36K

In the above example, we have looped through `car` using a `foreach` loop.

Here, the `Key` and `Value` property returns a collection containing keys and values in the dictionary.

---

## Change Dictionary Elements

We can change the value of elements in dictionary as:

```
using System;
using System.Collections;
class Program
{
    public static void Main()
    {
        // create a dictionary 
        Dictionary<string, string> car = new Dictionary<string, string>();

        // add items to dictionary
        car.Add("Model", "Hyundai");
        car.Add("Price", "36K");

        // print the original value
        Console.WriteLine("Value of Model before changing: " + car["Model"]);

        // change the value of "Model" key to "Maruti"
        car["Model"] = "Maruti";

        // print new updated value of "Model"
        Console.WriteLine("Value of Model after changing: " + car["Model"]);
    }
}
```

**Output**

Value of Model before changing: Hyundai
Value of Model after changing: Maruti

Here, we have changed the value of the `"Model"` key in the `car` dictionary.

---

## Remove Dictionary Elements

To remove the elements inside the dictionary we use:

- `Remove()` - removes the key/value pair from the dictionary

For example,

```
using System;
using System.Collections;
class Program
{
    public static void Main()
    {
        // create a dictionary 
        Dictionary<string, string> employee = new Dictionary<string, string>();

        // add items to dictionary
        employee.Add("Name", "Marry");
        employee.Add("Role", "Manager");
        employee.Add("Address", "California");

        Console.WriteLine("Original Dictionary :");

        // iterate through the modified dictionary 
        foreach (KeyValuePair<string, string> items in employee)
        {
            Console.WriteLine("{0} : {1}", items.Key, items.Value);
        }

        // remove value with key "Role"
        employee.Remove("Role");

        Console.WriteLine("\nModified Dictionary :");

        // iterate through the modified dictionary 
        foreach (KeyValuePair<string, string> items in employee)
        {
            Console.WriteLine("{0} : {1}", items.Key, items.Value);
        }
    }
}
```

**Output**

Original Dictionary :
Name : Marry
Role : Manager
Address : California

Modified Dictionary :
Name : Marry
Address : California

In the above example, we have removed the element whose key is `"Role"`.

Here, `employee.Remove("Role")` removes the key/value pair `"Role" : "Manager"` from the `employee` dictionary.

So when we iterate through `employee` we get a modified dictionary.

**Note:** If you want to remove all the elements of the dictionary, use the `Clear()` method.

---

## Frequently Asked Questions

Another way to create a Dictionary