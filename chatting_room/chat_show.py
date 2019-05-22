from socket import *
import os, sys

ADDR = ("176.23.6.119", 8888)

# 发送消息
def send_msg(s, name):
    while True:
        try:
            test = input("发言:\n")
        except KeyboardInterrupt:
            test = "quit"
        # 退出聊天室
        if test == "quit":
            msg = "Q " + name
            s.sendto(msg.encode(), ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s" % (name, test)
        s.sendto(msg.encode(), ADDR)

# 接受消息
def recv_msg(s):
    while True:
        data, addr = s.recvfrom(2048)
        # 服务端发送EXIT表示让客户端退出
        if data.decode() == "EXIT":
            sys.exit()
        print(data.decode())

# 创建网络连接
def main():
    s = socket(AF_INET, SOCK_DGRAM)
    while True:
        name = input("请输入姓名:")
        msg = "L " + name
        s.sendto(msg.encode(), ADDR)
        # 等待回应
        data, addr = s.recvfrom(1024)
        if data.decode() == "OK":
            print("您已经入聊天室")
            break
        else:
            print(data.decode())

    # 创建新的进程
    pid = os.fork()
    if pid < 0:
        sys.exit("Error!")
    elif pid == 0:
        send_msg(s, name)
    else:
        recv_msg(s)


if __name__ == '__main__':
    main()