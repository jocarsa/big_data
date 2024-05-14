#pip install sockets
import socket

def start_client():
    host = '192.168.1.37'  # The server's hostname or IP address
    port = 65432        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        while True:
            message = input("Enter message to send to server (or 'exit' to close): ")
            if message.lower() == 'exit':
                break
            s.sendall(message.encode())
            data = s.recv(1024)
            print(f"Received from server: {data.decode()}")

    print("Connection closed")

if __name__ == "__main__":
    start_client()
