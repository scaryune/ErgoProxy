# Getting Started with Rust

Rust is an open-source systems programming language that is syntactically similar to C++.

It is a general purpose programming language that is extensively used to build:

- kernels for operating systems
- game engines for video games
- browser engines for web browsers like Chrome, Firefox, etc.
- command-line tools, and so on.

---

## Features of Rust Programming

Here're some of the major features of Rust that make it one of the most popular programming languages in recent times.

**1. Performance**

Just like C programming, Rust is fast and requires less memory. So, we are not compromising on performance with Rust.

**2. Memory Safety**

Rust prevents the crashing of programs by ensuring memory safety. Without memory safety, programs can crash unexpectedly.

**3. Safe Concurrency**

Rust allows multiple parts of the program to run simultaneously. However, they cannot modify the same value at the same time. This ensures different parts of the program can safely run concurrently.

**4. Platform Independent**

You can compile a Rust program on one platform, then take it to another platform and run it. Rust supports a large number of platforms/operating systems.

---

## Run Rust using an Online Compiler

The simplest way to start running rust code is by using an [online compiler](https://play.rust-lang.org/). You can just write code and start executing.

This way, you don't have to understand the installation process, which might be confusing and time-consuming, especially at the beginning.

Once you start understanding the basics of Rust, you can then install Rust on your PC.

---

## Install Rust on your Computer

To install rust on your PC, you first need a command-line installer called `rustup`. The installation process of `rustup` is different for different operating systems.

- **For Windows** - visit [rustup.rs](https://rustup.rs/#), download and run `rustup-init.exe`
- **For Unix/Linux/macOS** - open command terminal and run `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`

**Note:** In windows, you might need to include Rust in your `%PATH%` system variable. To learn how to add system variables in windows, visit [create and modify environment variables](https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html#GUID-DD6F9982-60D5-48F6-8270-A27EC53807D0).

Now, to check if we have correctly installed Rust, open the command terminal and write:

```
$ rustc --version
```

**Output**

rustc 1.59.0 (9d1b2106e 2022-02-23)

If you get this type of output, the installation is done correctly.

Here, `rustc` is short for Rust Compiler required to compile programs. It is automatically installed with `rustup`.

---

## Your First Rust Program

Let's write our first Rust program.

Create a file called `main.rs` on your computer and add the following lines. Rust program files end with a `.rs` extension.

```
fn main() {
    println!("Hello, World!");
}
```

This program prints `"Hello, World!"` to the screen.

Now, open your command terminal and enter the following commands to compile and run your Rust program file.

On Linux and MacOS,

```
$ rustc main.rs
$ ./main
Hello, World!
```

On Windows,

```
> rustc main.rs
> ./main.exe
Hello, World!
```

Here,

- `rustc main.rs` compiles your Rust program
- `./main` or `./main.exe` runs the program

Regardless of your operating system, you should see the string `"Hello, World!"` printed on your command terminal.

Congratulations! you have successfully written your first Rust program.