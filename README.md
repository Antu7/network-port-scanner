# Port Scanner

Networking is a crucial aspect of modern computing and understanding how to work with networks is a valuable skill for any developer. One of the fundamental tasks in networking is port scanning, which is the process of discovering open ports on a target machine. In this post, we will look at a Python script that can be used to scan open ports and identify the running services on a target machine.


This is a simple Python script for port scanning. It checks the availability of ports on a host and identifies the service running on the open ports.

## Requirements
- Python 3.x
- `tqdm` library for progress bar

## Usage

```bash 
$ python port_scanner.py 
```

You will be prompted to enter the host to scan and the protocol (TCP or UDP). After entering the required information, the script will check the availability of all ports on the host and identify the service running on the open ports.

## Features

- Identifies the hostname and operating system of the target host.
- Displays a progress bar while scanning all the ports.
- Reports open ports and the service running on them.

## Note

This script is not a substitute for a proper security assessment, and it should only be used for educational and testing purposes. The use of this script for malicious activities is strictly prohibited.


## Contributing

We welcome contributions to this project! Here are some ways you can contribute:

1. **Report bugs or suggest new features.** If you find a bug or have an idea for a new feature, open an issue on Github.

2. **Fix bugs or add new features.** If you are a developer, you can submit a pull request with your changes. Please make sure to follow the existing code style and write tests for your changes.

3. **Documentation.** If you see any unclear or incorrect documentation, feel free to suggest changes.

4. **Testing.** Test the code and make sure it works as expected on different systems and configurations. Report any issues you find.


Thank you for your contributions!

