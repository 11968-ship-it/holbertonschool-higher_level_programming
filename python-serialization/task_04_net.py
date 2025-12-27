#!/usr/bin/env python3
"""
Client-server application that serializes a Python dictionary
and sends it over a network connection.
"""

import socket
import json


def start_server(host='127.0.0.1', port=65432):
    """
    Start a TCP server that listens for a connection,
    receives serialized data, deserializes it, and prints it.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen(1)
            print(f"Server listening on {host}:{port}...")

            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")

                # Receive data in chunks and reconstruct the full message
                data = b""
                while True:
                    chunk = conn.recv(4096)
                    if not chunk:
                        break
                    data += chunk

                # Decode and deserialize JSON data
                try:
                    received_dict = json.loads(data.decode('utf-8'))
                    print("Received Dictionary from Client:")
                    print(received_dict)
                except json.JSONDecodeError:
                    print("Failed to decode JSON data.")

    except (OSError, socket.error) as e:
        print(f"Server error: {e}")


def send_data(dictionary, host='127.0.0.1', port=65432):
    """
    Connect to the server, serialize a Python dictionary, and send it.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))

            # Serialize dictionary to JSON and send it
            serialized_data = json.dumps(dictionary).encode('utf-8')
            client_socket.sendall(serialized_data)

    except (OSError, socket.error) as e:
        print(f"Client error: {e}")
