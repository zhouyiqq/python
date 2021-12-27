# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2021/12/27 20:05
from IPy import IP
from past.builtins import raw_input
def test1():
        var1 = IP('10.0.0.0/8').version()#显示IP类型(通过version方法可以的判断输入的IP是IPv4还是IPv6 )
        var2 = IP('::1').version()
        print(var1,var2)
        ip = IP('192.168.0.0/28')#输出这个网段的ip个数
        print(ip.len())
        for x in ip : print(x)#输出这个网段的所有ip地址清单
        ip = IP('192.168.1.20')
        #反向解析名称
        print(ip.reverseNames())
        #解析ip地址类型（private–私网地址；public–公网地址）
        print(ip.iptype())
        print(IP('8.8.8.8').iptype())
        #转换成整型格式
        IP('8.8.8.8').int()
        #134744072
        #转换成十六进制格式
        IP('8.8.8.8').strHex()
        #'0x8080808'
        #转换成二进制格式
        IP('8.8.8.8').strBin()
        #'00001000000010000000100000001000'
        #十六进制转换成ip格式
        print(IP(0x8080808))
        #8.8.8.8
        #支持网络地址转换。
        print (IP('192.168.1.0').make_net('255.255.255.0'))
        print (IP('192.168.1.0/255.255.255.0',make_net=True))
        print (IP('192.168.1.0-192.168.1.255',make_net=True))

        #一个自动识别IP地址、子网、方向解析、IP类型等信息的脚本
        ip_s = raw_input('please input an ip or net-range: ') ###输入一个IP地址或者网段
        ips = IP(ip_s) #定义元素
        if len(ips) > 1: #如果len出来的数字大于1，那么就是一个网段
                print ('net: %s' %ips.net()) #输出网络地址
                print ('netmask: %s' %ips.netmask()) #输出子网掩码
                print ('broadcast: %s' %ips.broadcast()) #输出网络广播地址
                print ('reverse address: %s' %ips.reverseNames()[0]) #输出ip反向解析
                print ('subnet: %s' %len(ips)) #输出网络子网数
        else: ###否则就是一个地址
                print ('reverse address: %s' %ips.reverseNames()[0]) #输出ip反向解析
                print ('hexadecimal: %s' %ips.strHex()) #输出16进制地址
                print ('binary ip: %s' %ips.strBin()) #输出二进制地址
                print ('iptype: %s' %ips.iptype())   #输出地址类型

def test2():
        print("1---已知网段数求掩码")
        print("2---已知网段内主机数求掩码")
        choice = input("请输入计算的情况：")

        if choice == "1" :
            Wangduan = input("请输入网段：")
            Yanma_num = int(input("请输入掩码如255.255.255.0直接输入24："))
            Huafen_num = int(input("请输入需要划分的网段数："))
            er_num = bin(Huafen_num) #转为2进制位数
            sum_num = Yanma_num+len(er_num)-2#掩码位数的总长度,-2是因为3 = “0b11”
            yan_num = sum_num//8#有多少个255掩码。
            ziwang_num = sum_num%8
            s = ""
            i = 0
            while i < 8-ziwang_num:
                s += "1"
                i +=1
            s2 = int(s,2)
            s3 = 255- s2
            list = ["255" for i in range(1,yan_num+1)]
            list.append(str(s3))
            ii = len(list)
            while ii < 4:
                list.append("0")
                ii += 1
            print("需要划分的掩码为："+list[0]+"."+list[1]+"."+list[2]+"."+list[3]+"/"+str(sum_num))
        elif choice == "2":
            Wangduan = input("请输入网段：")
            Yanma_num = int(input("请输入掩码如255.255.255.0直接输入24："))
            Huafen_num = int(input("请输入需要划分的网段内主机数："))
            er_num = bin(Huafen_num)
            sum_num = 32-len(er_num)+2#掩码位数的总长度
            yan_num = sum_num//8#有多少个255掩码。
            ziwang_num = sum_num%8
            s = ""
            i = 0
            while i < 8-ziwang_num:
                s += "1"
                i +=1
            s2 = int(s,2)
            s3 = 255- s2
            list = ["255" for i in range(1,yan_num+1)]
            list.append(str(s3))
            ii = len(list)
            while ii < 4:
                list.append("0")
                ii += 1
            print("需要划分的掩码为："+list[0]+"."+list[1]+"."+list[2]+"."+list[3]+"/"+str(sum_num))
        else:
            print("输入错误。")
if __name__ == "__main__":
        test2()