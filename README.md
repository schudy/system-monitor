# System Monitor

A lightweight command-line system monitoring tool written in Python. It reports system resource usage, identifies high resource usage, and displays the processes using the most CPU.

## Features

- Displays operating system and machine information
- Monitors CPU usage
- Monitors memory usage
- Monitors disk usage
- Generates warnings when resource usage exceeds defined thresholds
- Displays the top five processes by CPU usage
- Handles processes that terminate or cannot be accessed during monitoring

## Example

```text
System: Darwin
Version: 21.6.0
Machine: x86_64
CPU Usage: 11.9 %
Memory Usage: 59.7 %
Disk Usage: 51.8 %

Top Processes by CPU Usage:
PID: 374 | CPU: 4.4 % | Name: WeChat
PID: 15082 | CPU: 3.9 % | Name: Google Chrome Helper (Renderer)
PID: 383 | CPU: 3.0 % | Name: Google Chrome
```

## Requirements

- Python 3
- psutil

Install the required package:

```bash
python3 -m pip install -r requirements.txt
```

## Run

```bash
python3 monitor.py
```

## Concepts Practiced

- Python functions and variables
- Conditional logic
- Loops
- Lists and dictionaries
- Exception handling
- Sorting data
- Process monitoring
- CPU, memory, and disk monitoring
- Third-party Python packages