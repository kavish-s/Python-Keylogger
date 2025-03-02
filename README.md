# Python Keylogger

A simple Python-based keylogger that records keystrokes and saves them to a file (`keylog.txt`).

---

## Features

- Logs all keystrokes.
- Detects key combinations (e.g., `Ctrl + C`).
- Saves logs with timestamps.
- Runs in the background.
- Can be converted into an executable (`.exe`).

---

## Requirements

Before running the script, install the required dependencies:

```sh
pip install -r requirements.txt
```

### `requirements.txt`

```
keyboard
```

---

## Usage

### Running as a Python Script

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the script:
   ```sh
   python keylogger.py
   ```
3. The script will log keystrokes in `keylog.txt`.
4. Press `Esc` to stop the script.

---

## Converting Python Script to Executable (Windows)

To run the keylogger without opening a terminal, convert it into an `.exe` file.

### Using PyInstaller

1. Install PyInstaller:
   ```sh
   pip install pyinstaller
   ```
2. Convert the script to an executable:

   ```sh
   pyinstaller --onefile keylogger.py
   ```

   - `--onefile`: Creates a single `.exe` file.

3. The `.exe` file will be in the `dist/` folder.
4. Run `keylogger.exe`—it will execute in the background.

---

## Notes

- This script is for **educational and ethical use only**. Unauthorized use may violate laws.
- To stop the keylogger, press `Esc`.
- The script writes logs to `keylog.txt` in the same directory.

---

## License

This project is for ethical and educational purposes. Use responsibly.
