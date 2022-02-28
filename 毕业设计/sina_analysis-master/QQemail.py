# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/2/28 10:18
# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/2/13 20:14
# 使用SMTP发送粉丝数量邮件提醒
#改写代码将生成的结果发生到QQ邮箱里
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

def send_email(theme, text):
    # SMTP的设置
    mail_host = "smtp.qq.com"
    mail_port = 465
    mail_pass = "ldeowtfgjqhidiie"
    # 接收和发送的邮箱
    sender = "2263167279@qq.com"
    receivers = ["914334405@qq.com","2246250681@qq.com"]
    receiver = ','.join(receivers)
    # receiver = "914334405@qq.com"
    # receiver = "2246250681@qq.com"
    # msg_to = ["2246250681@qq.com"]
    try:
        # 设置邮件收发信息
        # msg = MIMEText(text, 'plain', 'utf-8')
        msg = MIMEMultipart('mixed')
        msg['From'] = formataddr(("sender", sender))  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(("receiver", receiver))  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        # msg['To'] = ','.join(msg_to)
        msg['Subject'] = theme  # 邮件的主题
        ######## 添加附件 - rar/zip
        att_zip = MIMEText(open(r'./data/elsa_cy.png', 'rb').read(), 'base64', 'utf-8')
        att_zip["Content-Type"] = 'application/octet-stream'
        att_zip["Content-Disposition"] = 'attachment; filename="You.png"'
        msg.attach(att_zip)
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
switch = False#保证文件能够发送出去
while True:
    try:
        switch = send_email("任务已经完成，开始发送数据，时间是{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),"这里是数据")
    except:
        print("没有网络")
    if switch == True:
        break
# print("时间是{}".format(time.strftime("%Y年%m月%d日")))