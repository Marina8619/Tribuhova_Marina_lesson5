import socket
import uuid

ip_ = '127.0.0.1'
port_ = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Генерация уникального идентификатора
new_id = str(uuid.uuid4())

message = "The device is connected {}".format(new_id)
sock.sendto(message.encode(), ('127.0.0.1', 8888))
print("Sent message to UDP server: {}".format(message))




