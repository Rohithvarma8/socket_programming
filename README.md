# Networking Client Socket Application

## Overview
This project implements a client socket application that connects to a server, processes arithmetic operations, and retrieves a flag upon successful completion.

## Features
- Establishes a TCP connection to the server.
- Processes mathematical problems (`+`, `-`, `*`, `/`) sent by the server.
- Handles communication with error-handling mechanisms.
- Displays a flag from the server upon completion.

## File Details
### clientSocket.py
This script contains:
- Connection setup with server `127.0.0.1` on port `8888`.
- Handshake by sending the username.
- Query processing for basic arithmetic problems.
- Graceful error handling for timeouts and connection failures.

### Output

```Server: DONE 3F823E7CC6958457B008E2E3E2388F67FF4AFCBE13960AEBCFE4E4C6D5C9CD05```

```Received Flag: 3F823E7CC6958457B008E2E3E2388F67FF4AFCBE13960AEBCFE4E4C6D5C9CD05```


## How to Run
1. Start the server on `127.0.0.1` with port `8888`.
2. Run the client script:
3. Enter your username when prompted.

## Requirements
- Python 3.10 or above.
- Built-in `socket` library.

## Error Handling
- Connection timeout if no server response within 15 seconds.
- Connection refused if the server is not running.
- General exceptions are logged with details.

## Contributor
Badrinath Rohith Varma Datla  


