# Python Package

A package is a container that contains various functions to perform specific tasks. For example, the [math](https://www.programiz.com/python-programming/modules/math) package includes the `sqrt()` function to [perform the square root of a number](https://www.programiz.com/python-programming/examples/square-root).

While working on big projects, we have to deal with a large amount of code, and writing everything together in the same file will make our code look messy. Instead, we can separate our code into multiple files by keeping the related code together in packages.

Now, we can use the package whenever we need it in our projects. This way we can also reuse our code.

---

## Package Model Structure in Python Programming

Suppose we are developing a game. One possible organization of packages and [modules](https://www.programiz.com/python-programming/modules) could be as shown in the figure below.

![Package Model Structure](https://www.programiz.com/sites/tutorial2program/files/packages-in-python.png "Package Model Structure")

Game Package Model Structure

**Note**: A directory must contain a file named `__init__.py` in order for Python to consider it as a package. This file can be left empty but we generally place the initialization code for that package in this file.

---

## Importing module from a package

In Python, we can import modules from packages using the dot (.) operator.

For example, if we want to import the `start` module in the above example, it can be done as follows:

```
import Game.Level.start
```

Now, if this module contains a [function](https://www.programiz.com/python-programming/function) named `select_difficulty()`, we must use the full name to reference it.

```
Game.Level.start.select_difficulty(2)
```

#### Import Without Package Prefix

If this construct seems lengthy, we can import the module without the package prefix as follows:

```
from Game.Level import start
```

We can now call the function simply as follows:

```
start.select_difficulty(2)
```

#### Import Required Functionality Only

Another way of importing just the required function (or [class](https://www.programiz.com/python-programming/class) or [variable](https://www.programiz.com/python-programming/variables-constants-literals)) from a module within a package would be as follows:

```
from Game.Level.start import select_difficulty
```

Now we can directly call this function.

```
select_difficulty(2)
```

Although easier, this method is not recommended. Using the full [namespace](https://www.programiz.com/python-programming/namespace) avoids confusion and prevents two same [identifier](https://www.programiz.com/python-programming/keywords-identifier#identifiers) names from colliding.

While importing packages, Python looks in the list of directories defined in `sys.path`, similar as for [module search path](https://www.programiz.com/python-programming/modules#search).