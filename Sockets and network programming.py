#is the endpoint of the communication
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',55555))
s.listen()



while True:
    client,address = s.accept()
    print(f"Connected to {address}")
    client.send('you re connected'.encode())
    client.close()
    
