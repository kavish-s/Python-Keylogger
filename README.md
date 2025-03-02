# Keylogger Script

## Overview

This script is a simple keylogger that records keystrokes and saves them to a log file (`keylog.txt`). It captures individual key presses and key combinations, along with timestamps, for each recorded event.

## Features

- Logs individual key presses
- Detects and logs key combinations
- Saves logs with timestamps
- Stops logging when the "esc" key is pressed

## Requirements

- Python 3.x
- `keyboard` module (install using `pip install keyboard`)

## Installation

1. Ensure Python is installed on your system.
2. Install the required module:
   ```sh
   pip install keyboard
   ```
3. Download or copy the script to your desired directory.

## Usage

1. Run the script using:
   ```sh
   python keylogger.py
   ```
2. The script will start logging keystrokes and save them in `keylog.txt`.
3. Press the "esc" key to stop the keylogger.

## File Structure

- `keylogger.py`: The main script that logs keystrokes.
- `keylog.txt`: The file where all recorded keystrokes are stored.

## Notes

- Running this script requires administrative privileges on some operating systems.
- Be ethical and responsible when using keyloggers. Unauthorized logging of keystrokes may violate privacy laws.

## Disclaimer

This script is for educational purposes only. The author is not responsible for any misuse of this tool.
