# C# Type Conversion

The process of converting the value of one type (int, float, double, etc.) to another type is known as type conversion.

In C#, there are two basic types of type conversion:

1. **Implicit Type Conversions**
2. **Explicit Type Conversions**

---

## 1. Implicit Type Conversion in C#

In implicit type conversion, the C# compiler automatically converts one type to another.

Generally, smaller types like `int` (having less memory size) are automatically converted to larger types like `double` (having larger memory size).

### Example: Implicit Type Conversion

```
using System;

namespace MyApplication {
  class Program {
    static void Main(string[] args) {
      int numInt = 500;

      // get type of numInt
      Type n = numInt.GetType();

      // Implicit Conversion
      double numDouble = numInt;

      // get type of numDouble
      Type n1 = numDouble.GetType();

      // Value before conversion
      Console.WriteLine("numInt value: "+numInt);
      Console.WriteLine("numInt Type: " + n);

      // Value after conversion
      Console.WriteLine("numDouble value: "+numDouble);
      Console.WriteLine("numDouble Type: " + n1);
      Console.ReadLine();
    }
  }
}
```

**Output**

numInt value: 500
numInt Type: System.Int32
numDouble value: 500
numDouble Type: System.Double

In the above example, we have created an `int` type variable named numInt.

Notice the line,

```
// Implicit Conversion
double numDouble = numInt;
```

Here, we are assigning the `int` type variable to a `double` type variable. In this case, the C# compiler automatically converts the `int` type value to `double`.

Notice that we have used the `GetType()` method to check the type of `numInt` and `numDouble` variables.

**Note**: In implicit type conversion, smaller types are converted to larger types. Hence, there is no loss of data during the conversion.

---

## 2. C# Explicit Type Conversion

In explicit type conversion, we explicitly convert one type to another.

Generally, larger types like `double` (having large memory size) are converted to smaller types like `int` (having small memory size).

### Example: Explicit Type Conversion

```
using System;

namespace MyApplication {
  class Program {
    static void Main(string[] args) {

      double numDouble = 1.23;

      // Explicit casting
      int numInt = (int) numDouble;  

      // Value before conversion
      Console.WriteLine("Original double Value: "+numDouble);

      // Value before conversion
      Console.WriteLine("Converted int Value: "+numInt);
      Console.ReadLine();
    }
  }
}
```

**Output**

Original double value: 1.23
Converted int value: 1

In the above example, we have created a `double` variable named numDouble. Notice the line,

```
// Explicit casting
int numInt = (int) numDouble;
```

Here, `(int)` is a **cast expression** that explicitly converts the `double` type to `int` type.

We can see the original value is **1.23** whereas the converted value is **1**. Here, some data is lost during the type conversion. This is because we are explicitly converting the larger data type `double` to a smaller type `int`.

**Note**: The explicit type conversion is also called type casting.

---

## C# Type Conversion using Parse()

In C#, we can also use the `Parse()` method to perform type conversion.

Generally, while performing type conversion between non-compatible types like `int` and `string`, we use `Parse()`.

### Example: Type Conversion using Parse()

```
using System;

namespace Conversion {
  class Program {
   
    static void Main(string[] args) {

      string n = "100";

      // converting string to int type
      int a = int.Parse(n);
      Console.WriteLine("Original string value: "+n);
      Console.WriteLine("Converted int value: "+a);
      Console.ReadLine();
    }
  }
}
```

**Output**

Original string value: 100
Converted int value: 100

In the above example, we have converted a `string` type to an `int` type.

```
// converting string to int type
int a = int.Parse(n);
```

Here, the `Parse()` method converts the numeric string **100** to an integer value.

**Note**: We cannot use `Parse()` to convert a textual string like "test" to an `int`. For example,

```
String str = "test";
int a = int.Parse(str);   // Error Code
```

---

## C# Type Conversion using Convert Class

In C#, we can use the `Convert` class to perform type conversion. The `Convert` class provides various methods to convert one type to another.

|   |   |
|---|---|
|**Method**|**Description**|
|`ToBoolean()`|converts a type to a `Boolean` value|
|`ToChar()`|converts a type to a `char` type|
|`ToDouble()`|converts a type to a `double` type|
|`ToInt16()`|converts a type to a 16-bit `int` type|
|`ToString()`|converts a type to a `string`|

Let us look at some examples:

### Example: Convert int to String and Double

```
using System;

using System;
namespace Conversion {
  class Program {
    static void Main(string[] args) {

      // create int variable
      int num = 100;
      Console.WriteLine("int value: " + num);

      // convert int to string
      string str = Convert.ToString(num);
      Console.WriteLine("string value: " + str);

      // convert int to Double
      Double doubleNum = Convert.ToDouble(num);
      Console.WriteLine("Double value: " + doubleNum);

      Console.ReadLine();
    }
  }
}
```

**Output**

int value: 100
string value: 100
Double value: 100

In the above example,

- **Convert.ToString(a)** - converts an `int` type num to `string`
- **Convert.ToDouble(a)** - converts num to the `Double` type

---

### Example: Convert string to Double and vice-versa

```
using System;

namespace Conversion {
  class Program {
    static void Main(string[] args) {

      // create string variable
      string str = "99.99";
      Console.WriteLine("Original string value: " + str);

      // convert string to double
      Double newDouble = Convert.ToDouble(str);
      Console.WriteLine("Converted Double value: " + newDouble);

      // create double variable
      double num = 88.9;
      Console.WriteLine("Original double value: " + num);

      // converting double to string 
      string newString = Convert.ToString(num);
      Console.WriteLine("Converted string value: " + newString);

      Console.ReadLine();
    }
  }
}
```

**Output**

Original string value: 99.99
Converted Double value: 99.99
Original double value: 88.9
Converted string value: 88.9

In the above example,

- **Convert.ToDouble(str)**- converts a `string` type str to `Double`
- **Convert.ToString(num)** - converts a `double` type num to the `string`

---

### Example 3: Convert int to Boolean

```
using System;

namespace Conversion {
  class Program {
    static void Main(string[] args) {

      // create int variables
      int num1 = 0;
      int num2 = 1;

      // convert int to Boolean
      Boolean bool1 = Convert.ToBoolean(num1);
      Boolean bool2 = Convert.ToBoolean(num2);

      Console.WriteLine("Boolean value of 0 is: " + bool1);
      Console.WriteLine("Boolean value of 1 is: " + bool2);

      Console.ReadLine();
    }
  }
}
```

**Output**

Boolean value of 0 is: False
Boolean value of 1 is: True

In the above example, we have created two integer variables: `num1` and `num2` with values **0** and **1** respectively. Here,

- **Convert.ToBoolean(num1)** - converts **0** to a `Boolean` value `False`
- **Convert.ToBoolean(num2)** - converts **1** to a `Boolean` value `True`

**Note**: In C#, the integer value **0** is considered `False` and all other values are considered `True`.