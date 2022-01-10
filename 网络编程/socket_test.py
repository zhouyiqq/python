# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/1/15 16:13
#输出本地计算机名称和IP地址
import socket
import os
import struct
import sys
import threading
from ctypes import *
# IP协议
# IP协议负责把数据从一台计算机通过网络发送到另一台计算机。
# TCP协议
# TCP协议则是建立在IP协议之上的。TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达。TCP协议会通过3次握手建立可靠连接。
# UDP协议
# UDP协议是面向无连接的协议。使用UDP协议时，不需要建立链接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，数据无法保证一定到达。虽然用UDP传输数据不可靠，但它的优点是比TCP协议速度快。对于不要求可靠到达的数据，就可以使用UDP协议。
# bind()方法
# 将socket 对象绑定到一个地址，但这个地址必须是没有被占用的，否则会连接失败。这里的address 一般是一个ip,port 对，如(‘localhost’, 10000)
# listen()方法
# 监听，使得服务器能接收服务端连接，如果backlog指定了(最少是0，如果比0小，系统默认改成0)，限制可以连接的数量，如果没有指定，将指派一个默认的合理值。
# accept()方法
# 接受一个连接，但前提是socket 必须已经绑定了一个地址，在等待连接。返回值是一个( conn, addresss) 的值对，这里的conn是一个socket对象，可以用来改送或接收数据。而address是连接另一端绑定的地址，socket.getpeername()函数也能返回该地址。
# send()方法
# 发送数据到socket,前提是已经连接到远程socket,返回值是发送数据的量，检查数据是否发送完。
# TFTP
# TFTP是TCP/IP协议族中的一一个用来在客户端与服务器之间进行简单文件传输的协议。
# SNMP
# 简单网络管理协议(SNMP)，由一组网络管理的标准组成，包含一个应用层协议( application layer protocol)、数据库模型( database schema)和一组 资源对象。
# RIP
# 路由信息协议RIP ( Routing Information Protocol)是基于距离矢量算法的路由协议，利用跳数来作为计量标准。
# DNS
# DNS(DomainNameSystem,域名系统)，万维网上作为域名和IP地址相互映射的一个分布式数据库，能够使用户更方便的访问互联网，而不用去记住能够被机器直接读取的IP数串。

def local_computary_name_ip():
    """
     输出本地计算机名称和IP地址
    """
    host_name = socket.gethostname()
    print(f"你的计算机名称是{host_name}")
    host_ip = socket.gethostbyname(host_name)
    print(f"你的计算机ip是{host_ip}")
def remote_ip(host_name):
    """
    获取远程主机的IP地址
    大的互联网公司在不同的地区都有服务器所以不同地区ip地址不一样
    """
    host_ip = socket.gethostbyname(host_name)
    print(f"{host_name}:{host_ip}")
def namp_lisen():
    """
    模拟网络嗅探，检测网络流量和数据包收发情况，网卡模式为混杂模式
    """
    host_name = socket.gethostname()
    host = socket.gethostbyname(host_name)
    class IP(Structure):
        _fields_ =[
            ("ihl", c_ubyte, 4),
            ("version", c_ubyte, 4),
            ("tos", c_ubyte),
            ("len", c_ushort),
            ("id", c_ushort),
            ("offset", c_ubyte),
            ("ttl", c_ubyte),
            ("protocol_num", c_ubyte),
            ("sum", c_ushort),
            ("src", c_ulong),
            ("dst", c_ulong)
        ]

        def __new__(self, socket_buffer=None):
            return self.from_buffer_copy(socket_buffer)

        def __init__(self, socket_buffer=None):
            self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
            self.src_address = socket.inet_ntoa(struct.pack("<L", self.src))
            self.dst_address = socket.inet_ntoa(struct.pack("<L", self.dst))
            try:
                self.protocol = self.protocol_map[self.protocol_num]
            except:
                self.protocol = str(self.protocol_num)

    if os.name == "nt":  # WIN平台
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

    sniffer.bind((host, 0))

    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    # 在WIN平台上，需要设置IOCTL以启用混杂模式
    if os.name == "nt":
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    try:
        while True:
            raw_buffer = sniffer.recvfrom(65565)[0]
            ip_header = IP(raw_buffer[0:20])
            print("Protocol:%s %s -> %s" % (ip_header.protocol, ip_header.src_address, ip_header.dst_address))
    except KeyboardInterrupt:
        if os.name == "nt":
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
def namp_ip():
    list_of_name = []
    list_of_ip = []  # 存放结果
    thread_pool = []

    def showInfo():
        print("""
         命令格式：LAN_ip_hostname -all startip
                  LAN_ip_hostname -ip ipaddr
                  LAN_ip_hostname -hostname hostname
         说明：-all 扫描局域网中所有IP对应的hostname,需要起始IP，如192.168.0.1
              -ip 获取指定IP的hostname
              -hostname 根据主机名，得到其IP地址
               """)

    def lanAll(startip):
        index = startip.rfind('.')  # 找最右边的.的索引
        ipfirstpart = startip[0:index + 1]  # ip地址中前三位，如192.168.1
        intstart = int(startip[index + 1:])  # ip地址最后一位，转为int型

        f = range(intstart, 255)

        global g_mutex  # 互斥锁。不能定义称全局变量，否则，目标函数不认同
        g_mutex = threading.Lock()  # 初始化互斥锁

        for iplastpart in f:
            targetip = ipfirstpart + str(iplastpart)  # 拼接ip
            # 创建线程对象，存为thread。线程要执行的函数由target指定，args指定参数，可以是元组~。线程号从1开始
            thread = threading.Thread(target=lanIp2Name, args=(targetip,))
            thread_pool.append(thread)
            thread.start()

        # 阻塞主线程。collect all threads
        pos = intstart
        for pos in f:
            threading.Thread.join(thread_pool[pos - intstart])

        # 输出结果
        hosts = range(0, len(list_of_name))
        for host in hosts:
            print(list_of_ip[host], '  ====>   ', list_of_name[host])
        print('Find ', len(list_of_name), ' Hosts.Done!')

    def lanIp2Name(ip):
        try:
            (name, aliaslist, addresslist) = socket.gethostbyaddr(ip)
        except:
            return

        global g_mutex  # 再次声明
        g_mutex.acquire()
        ######################受互斥量保护区代码##################################
        list_of_name.append(name)
        list_of_ip.append(ip)
        ########################################################################
        g_mutex.release()

    def lanIpToName(ip):
        try:
            (name, aliaslist, addresslist) = socket.gethostbyaddr(ip)
        except:
            return
        print("%s====>%s" % (addresslist, name))

    def lanName2Ip(name):
        targetip = socket.gethostbyname(name)
        print(name, "    ====>   ", targetip)

    if '__main__' == __name__:
        '''
        sys.argv[]是用来获取命令行参数的，sys.argv[0]表示代码本身文件路径
        array.count(x)  返回出现的x的次数
        '''
        # if len(sys.argv) < 3:
        #     print("参数错误")
        #     showInfo()
        #     exit(1)

        cmds = ['-all', '-ip', '-hostname']

        # cmd = sys.argv[1]  # 命令格式
        # target = sys.argv[2]  # ip地址
        cmd = cmds[0]
        host_name = socket.gethostname()
        host = socket.gethostbyname(host_name)
        target = host

        if 0 == cmds.count(cmd):  # 判断参数数量
            print("参数错误啊")
            showInfo()
            exit(1)
        else:
            print('Start working,Please waiting...')
            if cmd == '-all':  # 输出所有IP和主机名
                lanAll(target)

            elif cmd == '-ip':  # 根据当前IP输出主机名
                lanIpToName(target)

            elif cmd == '-hostname':  # 根据当前主机名输出IP
                lanName2Ip(target)

if __name__ == "__main__":
    local_computary_name_ip()
    # remote_ip("www.baidu.com")
    # remote_ip("www.taobao.com")
    # remote_ip("www.fynu.edu.cn")
    # namp_lisen()
    namp_ip()