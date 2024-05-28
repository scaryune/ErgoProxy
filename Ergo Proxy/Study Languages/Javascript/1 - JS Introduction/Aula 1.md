# Getting Started With JavaScript

JavaScript is a popular programming language that has a wide range of applications.

JavaScript was previously used mainly for making webpages interactive such as form validation, animation, etc. Nowadays, JavaScript is also used in many other areas such as server-side development, mobile app development and so on.

Because of its wide range of applications, you can run JavaScript in several ways:

- Using console tab of web browsers
- Using Node.js
- By creating web pages

---

## 1. Using Console Tab of Web Browsers

All the popular web browsers have built-in JavaScript engines. Hence, you can run JavaScript on a browser. To run JavaScript on a browser,

1. Open your favorite browser (here we will use Google Chrome).
2. Open the developer tools by right clicking on an empty area and select Inspect. **Shortcut:** `F12`.
    
    ![Inspect Browser](https://www.programiz.com/sites/tutorial2program/files/inspect-browser.png "Inspect Browser")
    
    Inspect Browser
    
3. On the developer tools, go to the console tab. Then, write JavaScript code and press enter to run the code.
    
    ![Console tab in Browser](https://www.programiz.com/sites/tutorial2program/files/console-tab-browser.png "Console tab in Browser")
    
    Console tab in Browser
    

---

## Using Node.js

Node is a back-end run-time environment for executing JavaScript code. To run JS using Node.js, follow these steps:

1. Install the latest version of [Node.js](https://nodejs.org/en/).
2. Install an IDE/Text Editor like [Visual Studio Code](https://code.visualstudio.com/). In VS code, **create a file** > **write JS code** > **save it with .js extension**.
    
    ![Code in IDE](https://www.programiz.com/sites/tutorial2program/files/hello-node-ide.png "Code in IDE")
    
    Code in IDE
    
3. **Open up the terminal/command prompt** > **navigate to the file location** > **type** `**node hello.js**` > **hit enter**.
    
    ![Execute JS code in node](https://www.programiz.com/sites/tutorial2program/files/node-execute.png "Execute JS code in node")
    
    Execute JS code in node
    
4. You will get output on the terminal.

---

**Note**: It is also possible to run JavaScript on the terminal/command prompt directly. For that, simply type `node` and press enter. Then you can start writing JS code.

![Run JS code in node](https://www.programiz.com/sites/tutorial2program/files/run-node.png "Run JS code in node")

Run JS code in node

---

## By Creating Web Pages

JavaScript was initially created to make web pages interactive, that's why JavaScript and [HTML](https://www.programiz.com/html) go hand in hand. To run JS from a webpage, follow these steps:

1. **Open VS Code** > **Go to File** > **New File** > **Save it with .html extension**. For example, `main.html`.
2. Copy this doctype (minimum valid HTML code) and save it in the file.
    
    ```
    <!doctype html>
    
    <html lang="en">
    <head>
      <meta charset="utf-8">
    
      <title>Programiz</title>
    </head>
    
    <body>
      <script src=""></script>
    </body>
    </html>
    ```
    
3. Similarly create a JS file, write the following JS code and save it with **.js** extension like `main.js`.
    
    ```
    console.log('hello world');
    ```
    
    ![JS code in a file](https://www.programiz.com/sites/tutorial2program/files/main-js.png "JS code in a file")
    
    JS code in a file
    
4. From inside the HTML file, we need to link the `main.js` file to use it. You can achieve that by adding the following code in `main.html`.
    
    ```
    <script scr="main.js"></script>
    ```
    
    ![HTML code in a file](https://www.programiz.com/sites/tutorial2program/files/main-html.png "HTML code in a file")
    
    HTML code in a file
    
5. Open the `main.html` file using a browser.
6. To check if our JS code ran or not, **Right click on the web page > Inspect** > **Choose console tab**.
    
    ![Showing JS code in the console tab](https://www.programiz.com/sites/tutorial2program/files/console-tab.png "Showing JS code in the console tab")
    
    Showing JS code in the console tab
    

Now that you know how to run JavaScript, let's start learning the fundamentals of JavaScript from the next tutorial.