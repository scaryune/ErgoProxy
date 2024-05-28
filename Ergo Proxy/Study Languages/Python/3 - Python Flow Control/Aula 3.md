# Python while Loop

In Python, we use the `while` loop to repeat a block of code until a certain condition is met. For example,

```
number = 1

while number <= 3:
    print(number)
    number = number + 1
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

1
2
3

In the above example, we have used a `while` loop to print the numbers from **1** to **3**. The loop runs as long as the condition `number <= 3` is satisfied.

---

## while Loop Syntax

```
while condition:
    # body of while loop
```

Here,

1. The `while` loop evaluates the condition.
2. If the condition is true, **body of while loop** is executed. The condition is evaluated again.
3. This process continues until the condition is `False`.
4. Once the condition evaluates to `False`, the loop terminates.

---

## Flowchart of Python while Loop

![Flowchart of Python while Loop](https://www.programiz.com/sites/tutorial2program/files/python-while-loop-flowchart.png "Flowchart of Python while Loop")

Flowchart of Python while Loop

---

### Example: Python while Loop

```
# Calculate the sum of numbers until user enters 0
number = int(input('Enter a number: '))

total = 0

# iterate until the user enters 0
while number != 0:
    total += number
    number = int(input('Enter a number: '))

print('The sum is', total)
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

Enter a number: 3
Enter a number: 2
Enter a number: 1
Enter a number: -4
Enter a number: 0
The sum is 2

Here is how the above program works:

1. It asks the user to enter a number.
2. If the user enters a number other than **0**, it adds the number to the `total` and asks the user to enter a number again.
3. If the user enters **0**, the loop terminates and the program displays the total.

---

## Infinite while Loop

If the condition of a `while` loop is always `True`, the loop runs for infinite times, forming an **infinite while loop**. For example,

```
age = 32

# the test condition is always True
while age > 18:
    print('You can vote')
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)

**Output**

You can vote
You can vote
You can vote
.
.
.

The above program is equivalent to:

```
age = 32
    
# the test condition is always True
while True:
    print('You can vote')
```

[Run Code](https://www.programiz.com/python-programming/online-compiler)