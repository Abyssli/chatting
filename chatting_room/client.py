from socket import *

sockfd = socket(AF_INET,SOCK_DGRAM)

HOST = "176.23.6.120"
PORT = 8888
ADDR = (HOST,PORT)

while True:
    data = input("请输入消息:")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    message, addr = sockfd.recvfrom(1024)
    print("From server:", message.decode())

sockfd.colse()

