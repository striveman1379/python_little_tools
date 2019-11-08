# !/usr/bin/python
# -*- coding: UTF-8 -*-

'''
用python来发送电子邮件
可以读取指定文本的内容，添加到邮件正文
'''


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


smtpserver = "smtp.qq.com"          #设置服务器
user = "12345678@qq.com"           #用户名
password = "********"       #密码
sender = "12345678@qq.com"         #发件人
receivers = ["12345678@163.com","8765432@qq.com"]       #收件人列表




class MailHandler(object):

    @classmethod
    def sendemail(cls,sender,receivers,sub,content):    # sender：发件人；receivers：收件人；sub：标题；content：邮件内容


        msg=MIMEMultipart()
        msg['Subject'] = sub
        msg['From'] = sender
        msg['To'] = ";".join(receivers)
        msg.attach(MIMEText(content))


        s = smtplib.SMTP()
        try:
            s.connect(smtpserver)       # 连接smtp服务器
            s.login(user, password)         # 登陆服务器
            s.sendmail(sender, receivers, msg.as_string())          # 发送邮件

            return True
        except (Exception):
            print("失败...")
            return False
        finally:
            s.close()


if __name__ == '__main__':

    content = ""
    file_path = "/aaa/bbbb/ccccc/ddddd.txt"
    filename = file_path.split("/")[-1]
    with open(file_path, encoding="utf-8") as f:
        content += f.readline()

    if MailHandler.sendemail(sender, receivers,
                             sub="主题",
                             content=filename+"\n"*2+content):
        print("发送成功")
    else:
        print("发送失败")
