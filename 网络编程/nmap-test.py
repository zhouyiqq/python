# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/1/15 17:26
import os
import nmap
from 存储变量.pickle_test import load_variable, save_variable
#主机存活检测
def life(host="192.168.1.1/29"):
    n = nmap.PortScanner()
    n.scan(hosts=host, arguments="-sP")
    for x in n.all_hosts():
        print(x + ":" + n[x]["status"]["state"])
# 端口检测
def Port_detection():
    n = nmap.PortScanner()
    n.scan(hosts="192.168.85.1/30", arguments="-sV -p 1-1024")
    for x in n.all_hosts():
        print("Host: " + x)
        print("State: " + n[x].state())
        print("************************")
        for y in n[x].all_protocols():
            print("Protocols: " + y)
            print("↓↓↓↓↓↓↓↓↓")
            for z in n[x][y].keys():
                print("port: " + str(z) + " | name: " + n[x][y][z]["name"] + " | state: " + n[x][y][z]["state"])
        print("---------------------------")
def PortScannerYield_t():
    n = nmap.PortScannerYield()
    for x in n.scan(hosts="192.168.0.1/24", arguments="-sP"):
        print(x[0])
if __name__ == "__main__":
    PortScannerYield_t()