# Getting Started with Go Programming

Go is an open-source programming language developed by Google. It was created with these things in mind:

- efficient execution
- efficient compilation
- ease of programming

That's why Go is very fast, expressive (easy to read and write code) and lightweight.

---

## Running Go

The simplest way of running Go code is by using an online Go compiler like [The Go Playground](https://play.golang.org/).

You can also easily install and run Go programming locally on your computer. For that, visit [Install Go on Windows, Linux, and macOS](https://golang.org/doc/install).

---

## Writing Our First Go Program

To get familiar with the basic syntax of Go programming, let's write our first program.

```
// Print "Hello World!" message

package main
import "fmt"

func main() {
  fmt.Println("Hello World!")
}
```

**Output**

Hello World!

Here are the different parts of this program.

**1. The main() function**

All Go programs start with the `main()` function.

```
func main() {
   // code goes here
}
```

To use this function, we must import the `main` package first using `package main`.

**Note:** The line that starts with `//` is a comment. Comments are used to help users understand the code; they are completely ignored by the Go compiler.

**2. Print a line of text**

To print a line of text in Go, we use the `fmt.Println()` function. The function displays the content from the parentheses `()`.

To use `fmt.Println()`, we must import the `fmt` package first using `import "fmt"`.

---

## Basic Structure of a Go Program

Here are the things to take away from this tutorial.

1. All Go programs start from the `main()` function.
2. The bare minimum code structure of a Go program is:

```
package main

fun main() {

} 
```

---

## Frequently Asked Questions

Is the language called Go or Golang?

What are the applications of Go Programming?

Why should I use Go programming?

Is Go an object-oriented language?