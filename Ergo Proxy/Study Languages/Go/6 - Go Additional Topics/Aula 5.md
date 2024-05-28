# Go select

The select statement in Go allows us to execute a channel among many alternatives.

Before you learn about select, make sure you understand [Go Channel](http://www.programiz.com/golang/channel).

**Syntax of Select Statement**

```
select {

  case firstChannel:

  case secondChannel:

  case thirdChannel:

}
```

Here, each case of the select represents an individual channel. And, based on the availability of channel operations, the select statement executes a channel.

**Note**: The syntax of **select case** looks similar to that of the [Switch Case in Go](https://www.programiz.com/golang/switch). And, like the switch case, only one of the cases is executed by select.

---

## Example: Golang select Statement

```
package main
import "fmt"

func main() {

  // create two channels
  number := make(chan int)
  message := make(chan string)

  // function call with goroutine
  go channelNumber(number)
  go channelMessage(message)
  
  // selects and executes a channel
  select {

    case firstChannel := <- number:
      fmt.Println("Channel Data:", firstChannel)

    case secondChannel := <- message:
      fmt.Println("Channel Data:", secondChannel)
}

}

// goroutine to send integer data to channel
func channelNumber(number chan int) {
  number <- 15
}

// goroutine to send string data to channel
 func channelMessage(message chan string) {
   message <- "Learning Go select"
}
```

**Output**

Channel Data: Learning Go select

In the above example, we have created two channels `number` and message. Here, we have used the goroutines

- `channelNumber()` to send data to the number channel
- `channelMessage()` to send data to the message channel

The program includes two different channels, so we have used the select statement to execute one of the channels among the two.

```
select {

  case firstChannel := <- number:
    fmt.Println("Channel Data:", firstChannel)

  case secondChannel := <- message:
    fmt.Println("Channel Data:", secondChannel)
}
```

Here, the `case firstChannel` gets the value from the number channel and prints it. Similarly, the case `secondChannel` gets the value from the message channel and prints it.

When you run this program, you might get different outputs. In our example, both channels are ready for execution, so the select statement executes the channel randomly.

---

## Go select with one Channel Ready for Execution

We know that when both multiple channels are ready for execution, the select statement executes the channel randomly.

However, if only one of the channels is ready for execution, it executes that channel. For example,

```
package main
import (
  "fmt"
  "time"
)

func main() {

  // create channels
  number := make(chan int)
  message := make(chan string)

  // function call with goroutine
  go channelNumber(number)
  go channelMessage(message)

  // selects and executes a channel
  select {
    case firstChannel := <-number:
      fmt.Println("Channel Data:", firstChannel)

    case secondChannel := <-message:
      fmt.Println("Channel Data:", secondChannel)
  }

}

// goroutine to send data to the channel
func channelNumber(number chan int) {
  number <- 15
}

// goroutine to send data to the channel
func channelMessage(message chan string) {
  
  // sleeps the process by 2 seconds
  time.Sleep(2 * time.Second)

  message <- "Learning Go Select"
}
```

**Output**

Channel Data: 15

In the above example, we have created two goroutines,

- `channelNumber()` - sends data to the number channel
- `channelMessage()` - sends data to the message channel

Inside the `channelMessage()` goroutine, we have used the `time.Sleep()` method to make the message channel unavailable for execution.

Now, for the first **2** seconds, only the number channel is ready for execution. That's why the select statement executes the `case firstChannel` (number channel).

---

## Go select to block Channels

The select statement blocks all channels if they are not ready for execution. Suppose, in our previous example, if both the number and message channels are not ready for execution, select blocks both the channels for a certain time until one is available for execution.

Let's see an example.

```
package main
import (
  "fmt"
  "time"
)

func main() {

  // create channels
  number := make(chan int)
  message := make(chan string)

  // function call with goroutine
  go channelNumber(number)
  go channelMessage(message)

  // selects and executes a channel
  select {
    case firstChannel := <-number:
      fmt.Println("Channel Data:", firstChannel)

    case secondChannel := <-message:
      fmt.Println("Channel Data:", secondChannel)
  }

}

// goroutine to send data to the channel
func channelNumber(number chan int) {

  // sleeps the process for 2 seconds
  time.Sleep(2 * time.Second)

  number <- 15
}

// goroutine to send data to the channel
func channelMessage(message chan string) {

  // sleeps the process by 2 seconds
  time.Sleep(2 * time.Second)

  message <- "Learning Go Select"
}
```

**Output**

Channel Data: Learning Go Select

In the above example, we have used `time.Sleep()` method to make both the channels unavailable for execution for **2** seconds.

Now, the select statement will block both channels for the first **2** seconds. That's why we won't get any output for **2** seconds.

Then, it executes one of the channels randomly because both channels will be available after **2** seconds.

---

## Golang select with the default case

When none of the channels are ready, the select blocks the program. However, it's better to display some messages instead of blocking until the channels are ready.

For this, we use the `default` case, which is executed if none of the channels are ready for execution. For example,

```
package main

import (
  "fmt"
  "time"
)

func main() {

  // create channels
  number := make(chan int)
  message := make(chan string)

  // function call with goroutine
  go channelNumber(number)
  go channelMessage(message)

  // selects and executes a channel
  select {
    case firstChannel := <-number:
      fmt.Println("Channel Data:", firstChannel)

    case secondChannel := <-message:
      fmt.Println("Channel Data:", secondChannel)
	
    // default case 
    default:
      fmt.Println("Wait!! Channels are not ready for execution")
  }

}

// goroutine to send data to the channel
func channelNumber(number chan int) {
  
  // sleeps the process for 2 seconds
  time.Sleep(2 * time.Second)

  number <- 15
}

// goroutine to send data to the channel
func channelMessage(message chan string) {

  // sleeps the process by 2 seconds
  time.Sleep(2 * time.Second)
 
  message <- "Learning Go Select"
}
```

**Output**

Wait!! Channels are not ready for execution

In the above example, we have used the `default` case with select that prints `"Wait!! Channels are not ready for execution"` if both the channels are not ready.

Since both channels sleep for **2** seconds, they won't be available for execution for the first. That's why the statement of `default` case is executed.

After **2** seconds, both channels will be ready for execution, and one of them will be executed by select.

- [](https://www.programiz.com/golang/select#introduction)
- [](https://www.programiz.com/golang/select#select-example)
- [](https://www.programiz.com/golang/select#example-select)
- [](https://www.programiz.com/golang/select#block-select)
- [](https://www.programiz.com/golang/select#default-case)

[




