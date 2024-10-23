# Keylogger Using pynput
This project is a simple keylogger built with Python's pynput library. The keylogger records every keystroke on the keyboard and saves it to a text file.

## Features
- Captures and logs all key presses.
- Saves the logged keys into a file (keylog.txt).
- Runs silently in the background.

## Requirements
- Python 3.x
- pynput library

## How It Works
The keylogger works by monitoring all key presses using the pynput library and writes the keystrokes to a log file (keylog.txt). The logger runs continuously in the background until manually stopped.

## Usage
- After starting the script, it will log all key presses to the specified log file.
- You can stop the script by pressing Ctrl+C in the terminal.
