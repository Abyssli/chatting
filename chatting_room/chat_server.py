'''
    聊天室服务端
'''
from socket import *
import os

ADDR = ("0.0.0.0",8888)

users = {}

# 进入聊天室
def do_login(s,name,addr):
    if name in users or "管理员" in users:
        s.sendto("该用户名已存在".encode(),addr)
        return
    s.sendto(b"OK",addr)
    msg = "欢迎%s加入聊天室"%name
    for i in users:
        s.sendto(msg.encode(),users[i])

    users[name] = addr
    print(name,users[name])

# 聊天
def do_chat(name,data,s):
    for i in users:
        if i != name:
            data = "\n%s:%s"%(name,data)
            s.sendto(data.encode(),users[i])

# 退出聊天室
def do_quit(s,name):
    msg = "%s已退出聊天室" % name
    if name in users:
        for i in users:
            if i != name:
                s.sendto(msg.encode(),users[i])
            else:
                s.sendto(b"EXIT",users[i])
        del users[name]


# 接受客户端的请求
def do_request(s):
    while True:
        data,addr = s.recvfrom(1024)
        msg = data.decode().split(" ")
        if msg[0] == "L":
            name = msg[1]
            do_login(s,name,addr)
        elif msg[0] == "C":
            data = ' '.join(msg[2:])
            do_chat(msg[1],data,s)
        elif msg[0] == "Q":
            do_quit(s,msg[1])

# 搭建网络连接
def main():
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    pid = os.fork()
    if pid < 0:
        return
    elif pid == 0:
        do_request(s)
    else:
        try:
            while True:
                msg = input("管理员消息:")
                msg = "C 管理员消息:" + msg
                s.sendto(msg.encode(),ADDR)
        except:
            print()
            pass


if __name__ == '__main__':
    main()