
import socket


HOST = "127.0.0.1"  
PORT = 5656       


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


message = "ping"
client_socket.sendto(message.encode(), (HOST, PORT))
print(f"Message envoyé au serveur : {message}")


response, server_address = client_socket.recvfrom(2048)  
print(f"Réponse reçue du serveur : {response.decode()}")


client_socket.close()
print("fin de communication.")