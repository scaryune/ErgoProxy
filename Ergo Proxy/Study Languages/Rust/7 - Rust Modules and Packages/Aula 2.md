# Rust Crate and Package

A crate can contain one or more Rust modules, which in turn can contain code, such as functions, types, and constants.

A crate is of two types:

- Binary crate
- Library crate

A **binary crate** is a Rust program that compiles to an executable or multiple executables and has a `main()` function for each executable.

A **library crate** doesn't compile to an executable and doesn't have a `main()` function. A library crate generally defines a shared functionality that can be used in multiple projects.

Crates can be bundled together into a package.

---

## Creating a Package in Rust

Packages can be created using the [Cargo package manager](https://doc.rust-lang.org/cargo/), which is built into Rust. Cargo comes pre-installed with Rust.

We can use cargo to create a package. A **package** contains one or more crates that provides a set of functionality.

**Note:** A package can contain many binary crates, but at most only one library crate.

---

**Creating a Binary Package in Rust**

To create a binary package, we can use the `cargo` command in the terminal.

```
$ cargo new hello_world --bin
```

**Output**

Created binary (application) `hello_world` package

We create a binary package `hello_world` using `cargo` and the `--bin` option. It is the default cargo behavior.

Let's look at the contents of the `hello_world` package.

hello_world
├── Cargo.toml
└── src
    └── main.rs

Here,

- `hello_world` is the package directory
- `Cargo.toml` is a file that contains metadata about the crate, such as its name, version, and dependencies
- `src/main.rs` is the crate root and contains the source code of the binary package

---

**Creating a Library Package in Rust**

Similarly, we can create a library package in Rust using cargo.

```
$ cargo new hello_world_lib --lib
```

**Output**

Created library `hello_world_lib` package

We create a library package `hello_world_lib` using cargo and the `--lib` option.

Let's look at the contents of the `hello_world_lib` package.

hello_world_lib
├── Cargo.toml
└── src
    └── lib.rs

Here,

- `hello_world_lib` is the package directory
- `Cargo.toml` is a file that contains metadata about the crate, such as its name, version, and dependencies
- `src/lib.rs` is the crate root and contains the source code of the library package

A package can contain `src/main.rs` and `src/lib.rs`. In this case, it has two crates: a binary and a library, both with the same name as the package. For example,

hello_world
├── Cargo.toml
└── src
    └── lib.rs
    └── main.rs

**Note:** Cargo by convention passes the crate root files to the Rust compiler to build the library or binary.

- [](https://www.programiz.com/rust/crate-and-package#introduction)
- [](https://www.programiz.com/rust/crate-and-package#creating-a-package)