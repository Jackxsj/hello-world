#coding=utf-8
#TCP服务器端程序
import socket
import time
import threading



def udplink(sock):
    while True:
        data,addr=sock.recvfrom(1024)
        print("accept new connection from %s:%s..." %addr)
        if data=='exit' or not data:
            break
        print(data)
    sock.close()
    print("Connection from %s:%s closed." % addr)


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # 创建一个基于ipv4 的TCP协议                                                                                        的socket

s.bind(('192.168.1.8',2000))  #监听端口

print("Waiting for connection......")

#while True:
#    udplink(s)

while True:
    data,addr=s.recvfrom(1024)
    print("accept new connection from %s:%s..." % addr)
    if data=='exit' or not data:
        break
    print(data)

print("Connection from %s:%s closed." % addr)