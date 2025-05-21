# Basic Port Checker
This project is intended to serve as a basic port scanner. It is a simple script meant to check if networks are open on a target IP. This should be obvious, but please don't use my code for anything illegal, this is only meant to help me improve my programming and cybersecurity skills. Not that it would be particularly useful for anything illegal anyway, but still.

## Table of Contents:
- [Purpose](#purpose)
  - [Features](#features)
  - [Future Features](#future-features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)


### Features-
- Able to take a domain or IP and scan it for any potential open ports.
- Gets the banner and service version of the target.
- Identifies the FTP 2.2.0 vulnerability, should it be there.

### Future Features-
- Cross-referencing vulnerability databases
- Rate-limiting
- More scan types
- Better scan results


## Tech Stack:
1. Python 3 - The main programming language used in this project.
2. [argparse](https://docs.python.org/3/library/argparse.html) - Creates the commands used for terminal use.
3. [socket](https://docs.python.org/3/library/socket.html) - Allows for lower level work with sockets.
4. [ThreadPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html) - Allows for threading work to speed up the scanning process.
5. [Termcolor](https://pypi.org/project/termcolor/) - Allows for coloring terminal lines. Makes it easier to understand results.
   
## Usage:
The main command is:
```
python portscanner.py --targets <target> (+ <target> + <target> ...) --port-range <port_range> --timeout <timeout>
```
While the shortened version is:
```
python portscanner.py -t <target> (+ <target> + <target> ...) -pr <port_range> -T <timeout>
```
