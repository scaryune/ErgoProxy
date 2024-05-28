# Go Channel

Channels in Go act as a medium for goroutines to communicate with each other.

We know that goroutines are used to create concurrent programs. Concurrent programs can run multiple processes at the same time.

However, sometimes there might be situations where two or more goroutines need to communicate with one another. In such situations, we use channels that allow goroutines to communicate and share resources with each other.

Before you learn about channels, make sure to understand how [Goroutines work in Go](https://www.programiz.com/golang/goroutines).

---

## Create Channel in Go

In Go, we use the `make()` function to create a channel. For example,

```
channelName := make(chan int)
```

Here,

- `channelName` - name of the channel
- `(chan int)` - indicates that the channel is of integer type

---

### Example: Go Channel

```
package main
import "fmt"

func main() {
  
  // create channel of integer type
   number := make(chan int)
 
  // access type and value of channel
  fmt.Printf("Channel Type: %T\n", number)
  fmt.Printf("Channel Value: %v", number)

}
```

**Output**

Channel Type: chan int
Channel Value: 0xc00007a060

In the above example, we have used the `make()` function to create a channel named number. Here, we have used format specifiers:

- `%T` - to print the type of the channel
- `%v` - to print the value of the channel

Since the channel is of integer type (specified by `chan int`), we get the same output.

Also, the value of a channel is a memory address, which acts as a medium through which goroutines send and receive data to communicate.

---

## Golang Channel Operations

Once we create a channel, we can send and receive data between different goroutines through the channel.

**1. Send data to the channel**

The syntax to send data to the channel is

```
channelName <- data
```

Here the data after the `<-` operator is sent to channelName.

Let's see some examples,

```
// send integer data to channel
number <- 15

// send string data
message <- "Learning Go Channel"
```

**2. Receive data from the channel**

The syntax to receive data from the channel is:

```
<- channelName
```

This accesses the data from channelName.

Let's see some example,

```
// receive data 15
<- number

// receive data "Learning Go Channel"
<- message
```

---

## Example: Go Channel Operations

```
package main
import "fmt"

func main() {

  // create channel
  number := make(chan int)
  message := make(chan string)

  // function call with goroutine
  go channelData(number, message)

  // retrieve channel data
  fmt.Println("Channel Data:", <-number)
  fmt.Println("Channel Data:", <-message)

}

func channelData(number chan int, message chan string) {

  // send data into channel
  number <- 15
  message <- "Learning Go channel"

}
```

**Output**

Channel Data: 15
Channel Data:  Learning Go Channel

In the above example, we have created two channels named number and message.

Here, we have used the `<-` operator to perform operations to send and receive data from the channel.

---

## Blocking Nature of Channel

In Go, the channel automatically blocks the send and receive operations depending on the status of goroutines.

**1. When a goroutine sends data into a channel, the operation is blocked until the data is received by another goroutine. For example,**

```
package main
import "fmt"

func main() {

  // create channel
  ch := make(chan string)
 
  // function call with goroutine
  go sendData(ch)

  // receive channel data
  fmt.Println(<-ch)

}

func sendData(ch chan string) {
 
  // data sent to the channel
   ch <- "Received. Send Operation Successful"
   fmt.Println("No receiver! Send Operation Blocked")

}
```

**Output**

No receiver! Send Operation Blocked
Received. Send Operation Successful

In the above example, we have created the `sendData()` goroutine to send data to the channel. The goroutine sends the string data to the channel.

If the channel is not ready to receive the message, it prints `"No receiver! Send Operation Blocked"`.

Inside the `main()` function, we are calling `sendData()` before receiving data from the channel. That's why the first `"No receiver..."` is printed.

And, when the channel is ready to receive data, the data sent by goroutine is printed.

**2.** **When a goroutine receives data from a channel, the operation is blocked until another goroutine sends the data to the channel. For example,**

```
package main
import "fmt"

func main() {

  // create channel
  ch := make(chan string)

  // function call with goroutine
  go receiveData(ch)

  fmt.Println("No data. Receive Operation Blocked")

  // send data to the channel 
  ch <- "Data Received. Receive Operation Successful" 

}

func receiveData(ch chan string) {
    
  // receive data from the channel
  fmt.Println(<-ch)

}
```

**Output**

No data. Receive Operation Blocked
Data Received. Receive Operation Successful

In the above example, we have created the `receiveData()` goroutine to receive data from the channel. The goroutine receives the string data from the channel.

If the channel hasn't yet sent the data, it prints `"No data. Receive Operation Blocked"`.

Inside the `main()` function, we are calling `receiveData()` before sending data to the channel. That's why the first `"No data..."` is printed.

And, when the channel sends data, the data received by goroutine is printed.

- [](https://www.programiz.com/golang/channel#introduction)
- [](https://www.programiz.com/golang/channel#channel)
- [](https://www.programiz.com/golang/channel#send-receive)
- [](https://www.programiz.com/golang/channel#blocking-nature)