# sysprobe - Linux System Monitor

A lightweight Linux CLI tool for system monitoring and diagnostics.

## Features
- CPU, Memory, Disk monitoring
- Process inspection (top CPU processes)
- Log analysis (/var/log/syslog)
- System health report
- CLI-based architecture

## Inspired by
- htop
- top

## Installation
pip install -r requirements.txt

## Usage
python sysprobe.py --report
python sysprobe.py --processes
python sysprobe.py --logs

## Tech Stack
- Python
- psutil
- Linux system files (/proc, /var/log)