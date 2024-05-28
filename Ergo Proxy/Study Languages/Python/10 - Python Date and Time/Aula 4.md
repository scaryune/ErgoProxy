# How to get current date and time in Python?

There are a number of ways we can take to get the current date. We will use the `date` class of the [datetime](https://www.programiz.com/python-programming/datetime) module to accomplish this task.

---

## Example 1: Python get today's date

```
from datetime import date

today = date.today()
print("Today's date:", today)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

Today's date: 2022-12-27

Here, we imported the `date` class from the `datetime` module. Then, we used the `date.today()` method to get the current local date.

---

## Example 2: Current date in different formats

```
from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

d1 = 27/12/2022
d2 = December 27, 2022
d3 = 12/27/22
d4 = Dec-27-2022

---

## Get the current date and time in Python

If we need to get the current date and time, you can use the `datetime` class of the `datetime` module.

```
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

now = 2022-12-27 10:09:20.430322
date and time = 27/12/2022 10:09:20

Here, we have used `datetime.now()` to get the current date and time.

Then, we used [strftime()](https://www.programiz.com/python-programming/datetime/strftime) to create a [string](https://www.programiz.com/python-programming/string) representing date and time in another format.