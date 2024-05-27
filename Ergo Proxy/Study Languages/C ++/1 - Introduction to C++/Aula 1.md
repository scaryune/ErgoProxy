# Getting Started With C++

C++ is a general-purpose programming language that supports object-oriented programming.

To compile a C++ code, you need to have a **C++ compiler** installed on your device. However, if you're looking for a quick start, you can use our free [online C++ compiler](https://www.programiz.com/cpp-programming/online-compiler/) that allows you to run code directly in your browser without any setup.

Now, for those who prefer to use C++ on their local machine, this guide will walk you through the installation process on Windows, macOS, and Linux (Ubuntu).

[Windows](https://www.programiz.com/cpp-programming/getting-started#windows)

[Mac](https://www.programiz.com/cpp-programming/getting-started#mac)

[Linux](https://www.programiz.com/cpp-programming/getting-started#linux)

## Install C++ on Windows

To setup a C++ programming environment on Windows, you'll need two main components:

- **VS Code**: A text editor to write your code,
- **MinGW**: A compiler that turns your C++ code into an executable program.

Follow the steps below to install C++ on Windows:

1. Install VS Code
2. Download MinGW Compiler
3. Run the Installer
4. Add MinGW to System PATH
5. Install C/C++ Extension in VS Code

Here's a detailed explanation of each of the steps.

### Step 1: Install VS Code

Go to the VS Code [Official website](https://code.visualstudio.com/download) and download the Windows installer. Once the download is complete, run the installer and follow the installation process.

Click **Finish** to complete the installation process.

### Step 2: Download MinGW Compiler

Go to [MinGW Compiler Download](https://sourceforge.net/projects/mingw/) and download the MinGW installation manager.

![C++ MinGW Installation](https://www.programiz.com/sites/tutorial2program/files/cpp-mingw-installation111.png "C++ MinGW Installation")

C++ MinGW Installation

### Step 3: Run the Installer

Now, go to your **downloads** folder and run the installer you just downloaded. You will be prompted to this screen.

![C++ Run MinGW Installer](https://www.programiz.com/sites/tutorial2program/files/mingw-installer11.png "C++ Run MinGW Installer")

C++ Run MinGW Installer

Click on **Continue** and wait till the download is completed.

**Include gcc-core package**

During installation, you will be prompted to select the components to install. Mark **mingw32-base and mingw32-gcc-g++** for installation, click on installation and apply changes.

![C++ GCC-Core Package Installation](https://www.programiz.com/sites/tutorial2program/files/gcc-core-package-installation-in-cpp%201.png "C++ GCC-Core Package Installation")

C++ GCC-Core Package Installation

### Step 4: Add MinGW to System PATH

Go to the folder and double click on the MinGW folder and copy its location.

```
C:\MinGW\bin
```

Search **environment variable** on the terminal. In system properties, click on environment variables. You will be prompted to the screen below.

![C++ Setting Environment Variables](https://www.programiz.com/sites/tutorial2program/files/setting-environment-variables11.png "C++ Setting Environment Variables")

C++ Setting Environment Variables

Then, find the **Path** variable in the System variables section and click on **Edit**. Click **New** and add the path to the bin directory within your MinGW installation (i.e. C:\MinGW\bin)

Finally, close all the dialogues with the **Ok** button.

### Step 5: Install C/C++ Extension in VS Code

Open VS Code and click on Extensions in the left side of the window.

Then, search for **C/C++** by Microsoft in the Extensions and click on install.

![Installing C++ Extension in Windows](https://www.programiz.com/sites/tutorial2program/files/extension-install-in-windows1-1.png "Installing C++ Extension in Windows")

Installing C++ Extension in Windows

Now, you are all set to run C++ code inside your VS Code.

## Run Your First C++ Program

First open VS Code, click on the File in the top menu and then select New File.

![Create a New File in VS Code](https://www.programiz.com/sites/tutorial2program/files/newfile-11.png "Create a New File in VS Code")

Create a New File in VS Code

Then, save this file with a .cpp extension by clicking on **File** again, then **Save As**, and type your filename ending in .cpp. (Here, we are saving it as hello.cpp)

Now, write the following code into your file:

```
#include <iostream>
int main() {
    std::cout << "Hello World";
    return 0;
}
```

[Run Code](https://www.programiz.com/cpp-programming/online-compiler)

Then click on the **run** button on the top right side of your screen.

![Hello World in C++](https://www.programiz.com/sites/tutorial2program/files/hello-cpp-run.png "Hello World in C++")

Hello World in C++

You should see Hello World printed to the command prompt.

**For Linux System**

To run your C++ program on Linux, go to the Terminal, navigate to the directory containing your file, and type:

```
g++ hello.cpp -o hello 
```

Run your program using

```
./hello 
```

Now that you have set everything up to run C++ programs on your computer, you'll be learning how the basic program works in C++ in the next tutorial.