# Python Get Current time

There are a number of ways we can take to get current time in Python.

- Using the `datetime` object
- Using the `time` module

---

## Current time using the datetime object

```
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

Current Time = 07:41:19

In the above example, we have imported the `datetime` class from the [datetime](https://www.programiz.com/python-programming/datetime) module.

Then, we used the `now()` function to get a `datetime` object containing current date and time.

Using [datetime.strftime()](https://www.programiz.com/python-programming/datetime/strftime) function, we then created a [string](https://www.programiz.com/python-programming/string) representing current time.

---

## Current time using time module

In Python, we can also get the current time using the [time](https://www.programiz.com/python-programming/time) module.

```
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

07:46:58

---

## Current time of a Certain timezone

If we need to find the current time of a certain timezone, you can use [the pytZ module](http://pytz.sourceforge.net/).

```
from datetime import datetime
import pytz

# Get the timezone object for New York
tz_NY = pytz.timezone('America/New_York') 

# Get the current time in New York
datetime_NY = datetime.now(tz_NY)

# Format the time as a string and print it
print("NY time:", datetime_NY.strftime("%H:%M:%S"))

# Get the timezone object for London
tz_London = pytz.timezone('Europe/London')

# Get the current time in London
datetime_London = datetime.now(tz_London)

# Format the time as a string and print it
print("London time:", datetime_London.strftime("%H:%M:%S"))
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

NY time: 03:45:16
London time: 08:45:16

Here, we have used the `pytz` module to find the current time of a certain time zone.