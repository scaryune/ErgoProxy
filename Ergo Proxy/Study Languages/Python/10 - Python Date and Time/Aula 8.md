# Python sleep()

The `sleep()` method suspends the execution of the program for a specified number of seconds.

### Example

```
import time

time.sleep(2)
print("Wait until 2 seconds.")

# Output: Wait until 2 seconds.
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

---

## Python sleep() Syntax

```
time.sleep(seconds)
```

Here, [time](https://www.programiz.com/python-programming/time) is a Python module that provides several time-handling methods.

---

## sleep() Parameters

The method takes a single parameter:

- **seconds** - the number of seconds for which the program will suspend

---

## sleep() Return Value

The method does not return any value.

---

## Example: sleep() Method

```
import time

print("Printed immediately.")
time.sleep(2.4)
print("Printed after 2.4 seconds.")
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

Printed immediately.
Printed after 2.4 seconds.

Here's how the above program works:

1. `"Printed immediately"` is printed.
2. `time.sleep(2.4)` suspends execution for 2.4 seconds.
3. `"Printed after 2.4 seconds"` is printed.

---

## Create a Digital Clock in Python

```
import time

while True:
    
    # get current local time as structured data
    current_time = time.localtime()
    # format the time in 12-hour clock with AM/PM
    formatted_time = time.strftime("%I:%M:%S %p", current_time)
    
    print(formatted_time)
    time.sleep(1)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

01:47:43 PM
01:47:44 PM
01:47:45 PM
01:47:46 PM
... ... ...

In the above example, we obtain and print the current local time inside an infinite [while loop](https://www.programiz.com/python-programming/while-loop).

Then, the program waits for **1** second before repeating the same process.