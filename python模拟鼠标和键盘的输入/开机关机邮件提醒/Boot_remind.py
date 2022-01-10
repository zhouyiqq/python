# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/2/13 20:14
# 使用SMTP发送粉丝数量邮件提醒
import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr

def send_email(theme, text):
    # SMTP的设置
    mail_host = "smtp.qq.com"
    mail_port = 465
    mail_pass = "ldeowtfgjqhidiie"
    # 接收和发送的邮箱
    sender = "2263167279@qq.com"
    receiver = "914334405@qq.com"
    # receiver = "2246250681@qq.com"
    # msg_to = ["2246250681@qq.com"]
    try:
        # 设置邮件收发信息
        msg = MIMEText(text, 'plain', 'utf-8')
        msg['From'] = formataddr(("sender", sender))  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(("receiver", receiver))  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        # msg['To'] = ','.join(msg_to)
        msg['Subject'] = theme  # 邮件的主题
        # 设置服务器用户信息
        server = smtplib.SMTP_SSL(mail_host, mail_port)
        server.login(sender, mail_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender, receiver, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件对象
        server.quit()  # 关闭连接
        print("邮件发送成功")
        return True
    except smtplib.SMTPException as e:
        print("邮件发送失败")
        print(e)
# 判断是否需要进行邮件提醒
switch = False
while True:
    try:
        switch = send_email("你的电脑已经开机","时间是{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    except:
        print("没有网络")
    if switch == True:
        break
# print("时间是{}".format(time.strftime("%Y年%m月%d日")))