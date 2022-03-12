# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/12 20:40
import win32gui, win32con
import time
import pyperclip


# 读文件 行读
def read_file(msg_file: str) -> list:
    with open(msg_file, encoding='utf8') as f:
        return ['' if i == '\n' else i for i in f.readlines()]


# 按重复次数发送消息
def form(messages):
    name = "周刚"
    t = 2
    pyperclip.init_no_clipboard()

    def sendMsger(name):
        # 自动定位聊天窗口
        hand = win32gui.FindWindow('TXGuiFoundation', name)
        print(hand)
        # 重复发送消息
        for msg in messages:
            pyperclip.copy(msg)
            win32gui.PostMessage(hand, win32con.WM_PASTE, 0, 0)  # 向窗口发送剪贴板内容
            win32gui.PostMessage(hand, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)  # 向窗口发送 回车键
            win32gui.PostMessage(hand, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
            time.sleep(t)
        print("运行完成!")

    time.sleep(1)
    print("开始发送")
    print('...')
    sendMsger(name)


def run():
    messages = read_file('messages2.txt')
    form(messages)


if __name__ == "__main__":
    while True:
        run()