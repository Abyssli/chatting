'''
    聊天室客户端
'''
from socket import *
import os,sys

ADDR = ('176.23.6.120',8888)

# 接受服务器消息
def msg_recv(s):
    while True:
        data,addr = s.recvfrom(1024)
        if data.decode() == "EXIT":
            sys.exit("您已退出聊天室")
        print(data.decode())

# 向服务器发送消息
def msg_send(s,name):
    while True:
        try:
            msg = input("发言:")
        except:
            msg = "quit"
        # 退出聊天室
        if msg == "quit":
            msg = "Q " + name
            s.sendto(msg.encode(), ADDR)
            sys.exit("您已退出聊天室")
        data = "C %s %s"%(name,msg)
        s.sendto(data.encode(),ADDR)


# 搭建网络连接
def main():
    s = socket(AF_INET,SOCK_DGRAM)
    while True:
        name = input("请输入姓名:")
        msg = "L " + name
        s.sendto(msg.encode(),ADDR)
        # 阻塞等待回应
        data,addr = s.recvfrom(1024)
        if data.decode() == "OK":
            print("您已加入聊天室")
            break
        else:
            print(data.decode())

    # 创建新进程
    pid = os.fork()
    if pid < 0:
        sys.exit("Error")
    # 子进程收消息
    elif pid == 0:
        msg_recv(s)
    # 父进程发消息
    else:
        msg_send(s,name)

if __name__ == '__main__':
    main()