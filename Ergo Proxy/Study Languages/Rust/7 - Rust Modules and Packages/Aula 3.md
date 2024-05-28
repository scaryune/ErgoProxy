# Rust Cargo

Cargo is the Rust package manager. It comes pre-installed with Rust and can be used to package dependencies, manage them as well as build and distribute our own packages/libraries.

---

## Features of Cargo in Rust

Cargo is a command line tool for Rust which comes with these features:

- **Dependency management**

Cargo makes it easy to manage the dependencies of our project, including adding, updating, and removing dependencies.

- **Building and packaging**

Cargo can automatically build and package our Rust projects, creating binary or library code that can be shared with others.

- **Document generation**

Cargo can automatically generate documentation for our code, making it easier for other developers to understand and use our library.

- **Download crates**  
    Cargo can download and install libraries from [crates.io](https://crates.io/), which is a central repository for Rust crates.
- **Run a binary or tests**  
    Cargo can build our source code, run the executable binary and also run our tests.

---

## Dependency Management with Cargo in Rust

One of the primary features of cargo is that it can download, manage external libraries.

Let's look at an example of how we can use an external crate from [crates.io](https://crates.io/). **crates.io** is a central repository where we can pull and publish shared libraries for Rust.

Start by creating a Rust project using cargo:

```
$ cargo new hello_world
```

Now,

- `Cargo.toml` file in the root of our project directory `hello_world` is used to manage the dependencies.

If we want to use the "[rand](https://crates.io/crates/rand)" crate, we add the following line to the `[dependencies]` section of the `Cargo.toml`.

```
[package]
```

```
name = "hello_world"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
rand = "0.8.5"
```

**Note**: We can also add dependency to our project using the command `cargo add rand`.

- Next, we'll need to import the crate in our `src/main.rs` Rust file. We can do this by using `extern crate <crate_name>` line at the top of the file.  
      
    
    ```
    extern crate rand;
    ```
    
- Now, we can use the "rand" crate to generate a random number between **1** and **6**. The `use` keyword is used here to import items (such as functions, types, and constants) from the "rand" crate in the current scope.  
      
    
    ```
    extern crate rand;
    ```
    

```
use rand::Rng;

fn main() {
    let mut rng = rand::thread_rng();

    // simulate rolling a die
    println!("roll = {}", rng.gen_range(1..=6));
}

# Output: roll = 5
```

---

## Building and Running Project with Cargo in Rust

We can use cargo to install, build and run our `hello_world` project with the "rand" crate. Here's how:

**Build the project**  
  

```
$ cargo build
```

**Output**

Compiling libc v0.2.139
Compiling cfg-if v1.0.0
Compiling ppv-lite86 v0.2.17
Compiling getrandom v0.2.8
Compiling rand_core v0.6.4
Compiling rand_chacha v0.3.1
Compiling rand v0.8.5
Compiling hello_world v0.1.0 (/experiments/rust-practice/hello_world)
  Finished dev [unoptimized + debuginfo] target(s) in 2.57s

The `cargo build` command first installs any crates that are in use inside the `src/` directory and then proceeds to compile the project.

---

**Run the project**

```
$ cargo run
```

**Output**

Finished dev [unoptimized + debuginfo] target(s) in 0.05s
    Running `target/debug/hello_world`
roll = 5

---

## Useful Cargo Commands in Rust

Cargo can do a bunch of repetitive tasks for us. Here are some of the commonly used cargo commands.

|Command|Description|
|---|---|
|`cargo new`|Create a new Rust project with basic directory structure|
|`cargo build`|Build (compile) the current project and generate a binary executable|
|`cargo run`|Build and run your current project (cargo build + run)|
|`cargo check`|Build the current project without generating a binary executable|
|`cargo add`|Add a new dependency and include it in `Cargo.toml` file|
|`cargo update`|Update all dependencies of current project to latest version|