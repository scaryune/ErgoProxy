# Rust Module

Modules in Rust help in splitting a program into logical units for better readability and organization.

Once a program gets larger, it is important to split it into multiple files or namespaces. Modules help in structuring our program.

A module is a collection of items: functions, structs and even other modules.

---

## Defining a Module in Rust

The `mod` keyword is used to define a module. The syntax of module is:

```
// syntax of a module
mod module_name {
  // code
}
```

Here, `module_name` is the name of the module.

Now, let's define a module.

```
// a module named config
mod config {
    // a function print inside of the module 
    fn print() {
        println!("config!");
    }
}
```

In the above example, we create a module named `config` using the `mod` keyword.

Inside the module we can define multiple items. Here, we have defined the `print()` function.

---

## Visibility of Items inside a Module in Rust

Items inside a module can be private or public. By default, a module is private. It means items inside the module cannot be accessed outside of the module.

The `pub` keyword can be used to give an item public visibility.

Let's look at an example.

```
mod config {
    // items in modules by default have private visibility
    fn select() {
        println!("called config::select");
    }

    // use the `pub` keyword to override private visibility
    pub fn print() {
        println!("called config::print");
    }
}
```

Here, we define a module named `config` with two functions `select()` and `print()`.

The `print()` function starts with the `pub` keyword which means it has public visibility. However, the `select()` function does not.

If we compile the above program, we don't get any output because we have not used the functions yet.

warning: function `select` is never used
 --> src/lib.rs:3:8
  |
3 |     fn select() {
  |        ^^^^^^
  |
  = note: `#[warn(dead_code)]` on by default

warning: function `print` is never used
 --> src/lib.rs:8:12
  |
8 |     pub fn print() {
  |            ^^^^^

Now, let's call the functions inside the module.

```
mod config {
    // items in modules by default have private visibility
    fn select() {
        println!("called config::select");
    }

    // use the `pub` keyword to override private visibility
    pub fn print() {
        println!("called config::print");
    }
}

fn main() {
    // public items inside module can be accessed outside the parent module
    // call public print function from display module
    config::print();
}
```

**Output**

called display::print

Here, we call the public function `print()` inside of the `config` module using the syntax `config::print()`. The `::` operator is used to separate the module name and the item to call inside the module.

However, private items inside of the module are not accessible outside the module. If we call the private function `select()` inside the `config` module, we get a compilation error.

```
mod config {
    // items in modules by default have private visibility
    fn select() {
        println!("called config::select");
    }

    // use the `pub` keyword to override private visibility
    pub fn print() {
        println!("called config::print");
    }
}

fn main() {
    // private items inside module cannot be accessed outside the parent module
    // calling private select function inside config module will cause a compilation error
    display::select();
}
```

**Error**

error[E0603]: function `select` is private
  --> src/main.rs:16:14
   |
16 |     display::select();
   |              ^^^^^^ private function

The error mentions that the ``function `select` is private``. Thus, visibility of items inside a module is an important design consideration.

**Note:** A module can also have public visibility when used together with the `pub` keyword.

---

### Example: Using Module in Rust

```
mod player {
    // private function
    fn focus() {
        println!("called player::focus");
    }

    // public function
    pub fn shift() {
        println!("called player::shift");
    }

    // public function
    pub fn jump() {
        // call private function focus and shift inside the module
        focus();
        shift();
        println!("called player::jump");
    }
}

fn main() {
    // call public function jump from player module
    player::jump();
}
```

**Output**

called player::focus
called player::shift
called player::jump

Here, we define multiple functions inside the `player` module. Notice that we are able to call the private function `focus()` in another function `jump()` inside the same module.

---

## Nested Modules

A module can be defined inside another module. This is known as module nesting.

Let's look at an example.

```
// nested module
pub mod player {
    pub mod sprite {
        pub fn create() {
            println!("called player::sprite::create");
        }
    }
}

fn main() {
    // call public function create from sprite module which is inside player module 
    player::sprite::create();
}
```

**Output**

called player::sprite::create

Here, we have a `sprite` module nested within the `player` module.

We define a public function `create()` inside of the `sprite` module which is called using `player::sprite::create()` outside the module in the `main()` function.

---

## The use keyword in Rust

We can use the `use` keyword to bring items inside a module into the current scope. The `use` keyword helps us eliminate writing out the full module path to call functions.

Let's rewrite our nested module example with the help of the `use` keyword.

```
// nested module
pub mod player {
    pub mod sprite {
        pub fn create() {
            println!("called player::sprite::create");
        }
    }
}

// bring the create function into scope
use player::sprite::create;

fn main() {
    // call public function directly
    create();
}
```

**Output**

called player::sprite::create

Here, we use the `use` keyword to bring the `create()` function into the current scope from the `sprite` module which is inside the `player` module. This allows us to call the `create()` function directly, without having to fully qualify the name as `player::sprite::create()`.
