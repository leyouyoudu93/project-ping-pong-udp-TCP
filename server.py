import socket


HOST = "127.0.0.1"  
PORT = 5656        


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


server_socket.bind((HOST, PORT))
print(f"Le serveur UDP écoute sur {HOST}:{PORT}...")


while True:
    
    message, client_address = server_socket.recvfrom(2048)  
    print(f"Message reçu de {client_address} : {message.decode()}")

    
    if message.decode().lower() == "ping":
        response = "pong"
        server_socket.sendto(response.encode(), client_address)
        print(f"Réponse envoyée à {client_address} : {response}")
