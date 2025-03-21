# Python Keylogger

A Python-based keylogger that records keystrokes and can create and send files to a remote server for monitoring.

---

## Features

- Logs all keystrokes with timestamps.
- Detects and logs key combinations (e.g., `Ctrl + C`).
- Runs in the background until `Esc` is pressed.
- Sends the keylog file to a remote server.
- Can be converted into an executable (`.exe`).

---

## Requirements

Before running the script, install the required dependencies:

```sh
pip install keyboard
```

---

## Usage

### Running as a Python Script

1. Install dependencies:
   ```sh
   pip install keyboard
   ```
2. Run the keylogger:
   ```sh
   python keylogger.py
   ```
3. The script will log keystrokes in `keylog.txt`.
4. Press `Esc` to stop the script.
5. Once stopped, the script will send `keylog.txt` to the remote server.

### Running the Server

1. Navigate to the `server-side/` directory.
2. Run the server to receive the keylogs:
   ```sh
   python server.py
   ```
3. The server will listen for incoming connections and save the received logs as `received_keylog.txt`.

---

## Network Setup

To allow communication between a Windows 11 VirtualBox VM and the Windows 11 host machine, ensure the VM has:

- **Network Adapter 1** set to **Host-Only**
- **Network Adapter 2** set to **NAT Network**

Additionally, run the following command on the **virtual machine terminal**:

```sh
netsh advfirewall firewall add rule name="Allow ICMPv4" protocol=ICMPv4 dir=in action=allow
```

Ensure that both systems are on the same network and that firewalls or antivirus programs are not blocking the connection.

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
      pyinstaller --onefile --noconsole keylogger.py --exclude-module server-side
   ```
   - `--onefile`: Creates a single `.exe` file.
   - `--noconsole`: Runs the script silently in the background.
3. The `.exe` file will be in the `dist/` folder.
4. Run `keylogger.exe`—it will execute in the background.

---

## Notes

- **For educational and ethical use only.** Unauthorized use may violate laws.
- To stop the keylogger, press `Esc`.
- The script writes logs to `keylog.txt` in the same directory.
- The server must be running before stopping the keylogger for successful file transfer.
- Ensure that the firewall and antivirus settings allow the connection for proper functioning.

---

## License

This project is for ethical and educational purposes. Use responsibly.
