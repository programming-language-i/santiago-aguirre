import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect(("127.0.0.1", 8080))
    print("mi direccion ", cliente.getsockname())
    print("servidor:", cliente.getpeername())
    cliente.sendall("mensaje para el servidor".encode("utf-8"))
    print("respuesta del servidor # 2:", cliente.recv(1024).decode("utf-8"))
    
    