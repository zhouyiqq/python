# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/2/13 19:58
import pickle
from io import BytesIO
import socket

#接收数据
def Server_Recive(ip,port):
    socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_obj.bind((ip,port))
    socket_obj.listen(5)
    file_on = 1
    while True:
        connection,address = socket_obj.accept()
  #接受的数据
        recieved_message = b''
        recieved_message_fragment = connection.recv(1024)
        while recieved_message_fragment:
            recieved_message += recieved_message_fragment
            recieved_message_fragment = connection.recv(1024)

        try:
            obj = pickle.loads(recieved_message)
            print(obj['Key'],end=' ')
        except EOFError:
            file_name = 'recv_image_' + str(file_on) + '.bmp'
            recv_image = open(file_name,'wb')
            recv_image.write(recieved_message)
            file_on += 1
        connection.close()


if __name__ == '__main__':
    Server_IP = '0.0.0.0'
    Server_Port = 6666
    Server_Recive(Server_IP,Server_Port)