![TCP Server Banner](https://user-images.githubusercontent.com/57842220/138709524-631cab35-60c2-47d8-9182-d12b00d69456.png)

The TCP (Transmission Control Protocol) protocol implements a service called end-to-end communication, that is, it provides a logical communication between application processes running on different hosts, and provides a reliable data transfer service. between transport services on the internet partner applications. This protocol guarantees that data is delivered error-free, sequentially and without loss or duplication.

It is connection-oriented and, for them to happen, a concept called sockets (IP address + port) is used. Allowing to establish a connection between a pair of sockets according to previously specified quality of service and security parameters.


### How to run the server? 🏃‍♀️

To run the program and encrypt the files:
```sh
python3.9 main.py
```

To use the decryption key you need to enter debugging the code as follows:
```sh
python3.9 main.py -d
```
