# Python Variables and Literals

In the previous tutorial you learned about [Python comments](https://www.programiz.com/python-programming/comments). Now, let's learn about variables and literals in Python.

## Python Variables

In programming, a variable is a container (storage area) to hold data. For example,

```
number = 10
```

Here, number is a variable storing the value **10**.

---

### Assigning values to Variables in Python

As we can see from the above example, we use the assignment operator `=` to assign a value to a variable.

```
# assign value to site_name variable
site_name = 'programiz.pro'

print(site_name)

# Output: programiz.pro
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

apple.com

In the above example, we assigned the value `programiz.pro` to the site_name variable. Then, we printed out the value assigned to site_name

**Note**: Python is a [type-inferred](https://en.wikipedia.org/wiki/Type_inference) language, so you don't have to explicitly define the variable type. It automatically knows that `programiz.pro` is a string and declares the `site_name` variable as a string.

---

### Changing the Value of a Variable in Python

```
site_name = 'programiz.pro'
print(site_name)

# assigning a new value to site_name
site_name = 'apple.com'

print(site_name)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

programiz.pro
apple.com

Here, the value of site_name is changed from `'programiz.pro'` to `'apple.com'`.

---

### Example: Assigning multiple values to multiple variables

```
a, b, c = 5, 3.2, 'Hello'

print (a)  # prints 5
print (b)  # prints 3.2
print (c)  # prints Hello 
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

If we want to assign the same value to multiple variables at once, we can do this as:

```
site1 = site2  = 'programiz.com'

print (x)  # prints programiz.com
print (y)  # prints programiz.com
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

Here, we have assigned the same string value `'programiz.com'` to both the variables site1 and site2.

Rules for Naming Python Variables

[](https://www.programiz.com/python-programming/keywords-identifier)

---

## Python Literals

Literals are representations of fixed values in a program. They can be numbers, characters, or strings, etc. For example, `'Hello, World!'`, `12`, `23.0`, `'C'`, etc.

Literals are often used to assign values to variables or constants. For example,

```
site_name = 'programiz.com'
```

In the above expression, site_name is a variable, and `'programiz.com'` is a literal.

There are different types of literals in Python. Let's discuss some of the commonly used types in detail.

---

## Python Numeric Literals

Numeric Literals are immutable (unchangeable). Numeric literals can belong to **3** different numerical types: `Integer`, `Float`, and `Complex`.

### 1. Integer Literals

Integer literals are numbers without decimal parts. It also consists of negative numbers. For example, `5`, `-11`, `0`, `12`, etc.

### 2. Floating-Point Literals

Floating-point literals are numbers that contain decimal parts.

Just like integers, floating-point numbers can also be both positive and negative. For example, `2.5`, `6.76`, `0.0`, `-9.45`, etc.

### 3. Complex Literals

Complex literals are numbers that represent complex numbers.

Here, numerals are in the form `a + bj`, where `a` is real and `b` is imaginary. For example, `6+9j`, `2+3j`.

---

## Python String Literals

In Python, texts wrapped inside quotation marks are called **string literals.**.

```
"This is a string."
```

We can also use single quotes to create strings.

```
'This is also a string.'
```

## More on Python Literals

Python Boolean Literals

Character Literals in Python

Special Literal in Python

[](https://www.programiz.com/python-programming/online-compiler)

Collection Literals