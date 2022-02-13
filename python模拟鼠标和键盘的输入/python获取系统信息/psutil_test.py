# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/2/13 21:33
import datetime
import pprint

import psutil
"""
sutil是一个开源切跨平台的库，其提供了便利的函数用来获取系统的信息，比如CPU，内存，磁盘，网络等。
此外，psutil还可以用来进行进程管理，包括判断进程是否存在、获取进程列表、获取进程详细信息等。
而且psutil还提供了许多命令行工具提供的功能，
包括：ps，top，lsof，netstat，ifconfig， who，df，kill，free，nice，ionice，iostat，iotop，uptime，pidof，tty，taskset，pmap。
"""
# 查看cpu个数
# pprint.pprint(psutil.cpu_count())#处理器，CPU逻辑数量
# pprint.pprint(psutil.cpu_count(logical=False))#内核，CPU物理核心
# pprint.pprint(psutil.cpu_times())# 统计CPU的用户／系统／空闲时间
# pprint.pprint(psutil.cpu_times(percpu=True))
# pprint.pprint(psutil.cpu_percent())#查看cpu的利用率
# pprint.pprint(psutil.cpu_percent(percpu=True))#每个处理器的利用率
# Memory内存相关
# virtual_memory()：以命名元组的形式返回内存使用情况，包括总内存，可用内存，内存利用率，buffer和cache等。单位为字节。
# pprint.pprint(psutil.virtual_memory())
# swap_memory()：以命名元组的形式返回swap/memory使用情况，包含swap中页的换入和换出。
# pprint.pprint(psutil.swap_memory())
#单位转换
def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return '%sB' % n


# pprint.pprint(bytes2human(psutil.virtual_memory().total))

# Disk相关：
# 函数 	描述
# psutil.disk_io_counters() 	disk_io_counters([perdisk])：以命名元组的形式返回磁盘io统计信息(汇总的)，包括读、写的次数，读、写的字节数等。
# 当perdisk的值为True，则分别列出单个磁盘的统计信息(字典：key为磁盘名称，value为统计的namedtuple)。
# psutil.disk_partitions() 	disk_partitions([all=False])：以命名元组的形式返回所有已挂载的磁盘，包含磁盘名称，挂载点，文件系统类型等信息。
# 当all等于True时，返回包含/proc等特殊文件系统的挂载信息
# psutil.disk_usage() 	disk_usage(path)：以命名元组的形式返回path所在磁盘的使用情况，包括磁盘的容量、已经使用的磁盘容量、磁盘的空间利用率等。
#
# pprint.pprint(psutil.disk_partitions())# 查看所有已挂在的磁盘
# pprint.pprint([device for device in psutil.disk_partitions() if device.mountpoint == '/'])# 使用列表表达式查询指定挂载点信息
# pprint.pprint( psutil.disk_usage('/'))# 查看磁盘使用情况
# pprint.pprint(psutil.disk_io_counters())# 查看磁盘io统计汇总
# pprint.pprint(psutil.disk_io_counters(perdisk=True))# 分别列出单个磁盘的统计信息
#
# Network相关：
# 函数 	详情
# psutil.net_io_counter([pernic]) 	以命名元组的形式返回当前系统中每块网卡的网络io统计信息，包括收发字节数，收发包的数量、出错的情况和删包情况。当pernic为True时，则列出所有网卡的统计信息。
# psutil.net_connections([kind]) 	以列表的形式返回每个网络连接的详细信息(namedtuple)。命名元组包含fd, family, type, laddr, raddr, status, pid等信息。kind表示过滤的连接类型，支持的值如下：(默认为inet)
# psutil.net_if_addrs() 	以字典的形式返回网卡的配置信息，包括IP地址和mac地址、子网掩码和广播地址。
# psutil.net_if_stats() 	返回网卡的详细信息，包括是否启动、通信类型、传输速度与mtu。
# psutil.users() 	以命名元组的方式返回当前登陆用户的信息，包括用户名，登陆时间，终端，与主机信息
# psutil.boot_time() 	以时间戳的形式返回系统的
# 启动时间

# 进程管理
#
# psutil还提供了作为进程管理的功能函数，包括获取进程列表，判断是否存在。
# 函数 	详情
# psutil.pids() 	以列表的形式返回当前正在运行的进程
# psutil.pid_exists(1) 	判断给点定的pid是否存在
# psutil.process_iter() 	迭代当前正在运行的进程，返回的是每个进程的Process对象
# psutil.Process() 	对进程进行封装，可以使用该类的方法获取进行的详细信息，或者给进程发送信号。
print(psutil.pids())
# print(*psutil.process_iter())
# print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))#开机时间
p = psutil.Process(1060)
# 进程名称
print(p.name())#获取进程交互环境
print(p.exe())#获取进程路径
print(p.cwd())#获取进程工作目录
print(p.cmdline())#获取进程启动的工作行
print( p.ppid())#获取父进程id
print( p.parent())#获取父进程
# p = psutil.Process(1000)
# print(p.children())#获取子进程
print(p.status())#获取进程状态
print(p.username())#获取进程用户名
print( p.create_time())#获取进程创建时间
print(p.terminal())#获取进程终端
print(p.cpu_times())#获取进程使用时间
print(p.memory_info())#获取进程使用内存
print( p.open_files())#获取进程打开的文件
print(p.connections())#获取进程相关的网络链接
print(p.num_threads())#获取进程的线程数量
print( p.threads())#获取所以线程信息
print( p.environ())#获取进程环境变量
print(p.terminate())#结束进程
print(psutil.test())#所有信息