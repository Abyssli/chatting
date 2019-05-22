from socket import *

# 搭建UDP网络
def main():
    sockfd = socket(AF_INET,SOCK_DGRAM)
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(("0.0.0.0",8888))
    Users = {}
    user_name,addr = sockfd.recvfrom(1024)
    Users[user_name] = addr
    data = "%s进入聊天室"%user_name
    for key in Users:
        sockfd.sendto(data.encode(),Users[key])

while True:
    main()

