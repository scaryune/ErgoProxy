# JavaScript throw Statement

In the previous tutorial, you learned to handle exceptions using [JavaScript try..catch statement](https://www.programiz.com/javascript/try-catch-finally). The try and catch statements handle exceptions in a standard way which is provided by JavaScript. However, you can use the `throw` statement to pass user-defined exceptions.

In JavaScript, the `throw` statement handles user-defined exceptions. For example, if a certain number is divided by **0**, and if you need to consider `Infinity` as an exception, you can use the `throw` statement to handle that exception.

---

## JavaScript throw statement

The syntax of throw statement is:

```
throw expression;
```

Here, `expression` specifies the value of the exception.

For example,

```
const number = 5;
throw number/0; // generate an exception when divided by 0
```

**Note**: The expression can be [string](https://www.programiz.com/javascript/string), [boolean](https://www.programiz.com/javascript/booleans), [number](https://www.programiz.com/javascript/numbers), or [object](https://www.programiz.com/javascript/object) value.

---

## JavaScript throw with try...catch

The syntax of `try...catch...throw` is:

```
try {
    // body of try
    throw exception;
} 
catch(error) {
    // body of catch  
}
```

**Note**: When the throw statement is executed, it exits out of the block and goes to the `catch` block. And the code below the `throw` statement is not executed.

---

### Example 1: try...catch...throw Example

```
const number = 40;
try {
    if(number > 50) {
        console.log('Success');
    }
    else {

        // user-defined throw statement
        throw new Error('The number is low');
    }

    // if throw executes, the below code does not execute
    console.log('hello');
}
catch(error) {
    console.log('An error caught'); 
    console.log('Error message: ' + error);  
}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

An error caught
Error message: Error: The number is low

In the above program, a condition is checked. If the number is less than **51**, an error is thrown. And that error is thrown using the `throw` statement.

The `throw` statement specifies the string `The number is low` as an expression.

**Note**: You can also use other built-in error constructors for standard errors: `TypeError`, `SyntaxError`, `ReferenceError`, `EvalError`, `InternalError`, and `RangeError`.

For example,

```
throw new ReferenceError('this is reference error');
```

---

## Rethrow an Exception

You can also use `throw` statement inside the `catch` block to rethrow an exception. For example,

```
const number = 5;
try {
     // user-defined throw statement
     throw new Error('This is the throw');

}
catch(error) {
    console.log('An error caught');
    if( number + 8 > 10) {

        // statements to handle exceptions
         console.log('Error message: ' + error); 
        console.log('Error resolved');
    }
    else {
        // cannot handle the exception
        // rethrow the exception
        throw new Error('The value is low');
    }
}
```

[Run Code](https://www.programiz.com/javascript/online-compiler)

**Output**

An error caught
Error message: Error: This is the throw
Error resolved

In the above program, the `throw` statement is used within the `try` block to catch an exception. And the `throw` statement is rethrown in the `catch` block which gets executed if the `catch` block cannot handle the exception.

Here, the `catch` block handles the exception and no error occurs. Hence, the `throw` statement is not rethrown.

If the error was not handled by the catch block, the throw statement would be rethrown with error message Uncaught Error: The value is low