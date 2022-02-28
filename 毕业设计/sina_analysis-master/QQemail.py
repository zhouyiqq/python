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

import zipfile
import os
def to_zip(month_rank_dir):
    "打包文件夹"
    # month_rank_dir = "test_dir"
    zip_file_new = month_rank_dir + '.zip'
    if os.path.exists(month_rank_dir):
        print('正在为您压缩...')
        # 压缩后的名字
        zip = zipfile.ZipFile(zip_file_new, 'w', zipfile.ZIP_DEFLATED)
        for dir_path, dir_names, file_names in os.walk(month_rank_dir):
            # 去掉目标跟路径，只对目标文件夹下面的文件及文件夹进行压缩
            fpath = dir_path.replace(month_rank_dir, '')
            for filename in file_names:
                zip.write(os.path.join(dir_path, filename), os.path.join(fpath, filename))
        zip.close()
        print('该目录压缩成功！')
    else:
        print('您要压缩的目录不存在...')
def send_email(theme,text):
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
        # if os.path.exists("picture.zip"):
        to_zip("./picture")
        att_zip = MIMEText(open(r'./picture.zip', 'rb').read(), 'base64', 'utf-8')
        # else:
        #     to_zip("./picture")
        att_zip["Content-Type"] = 'application/octet-stream'
        att_zip["Content-Disposition"] = 'attachment; filename="You.zip"'
        msg.attach(MIMEText(text, 'plain', 'utf-8'))#这里发送文本内容
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
        switch = send_email("任务已经完成，开始发送数据，时间是{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),"hellw")
    except:
        print("没有网络")
    if switch == True:
        break
# print("时间是{}".format(time.strftime("%Y年%m月%d日")))