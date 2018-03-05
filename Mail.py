#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
------------------------------------
File Name:    Mail
Author:    Mrtutu
Date:    2018/3/5
Description:
------------------------------------

"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage


class Mail:
    def __init__(self, host_server, sender_qq_mail, sender_qq, pwd, receiver, title, content, image_inside, filelist):
        self.host_server = host_server
        self.sender_qq_mail = sender_qq_mail
        self.sender_qq = sender_qq
        self.pwd = pwd
        self.receiver = receiver
        self.title = title
        self.content = content
        self.image_inside = image_inside
        self.filelist = filelist
        print("邮件准备中...")
    def sendmail(self):

        # SSL登录
        smtp = SMTP_SSL(self.host_server)
        smtp.login(self.sender_qq, self.pwd)

        msg = MIMEMultipart()
        msg['Subject'] = Header(self.title, 'utf-8')
        msg['From'] = self.sender_qq_mail
        msg['To'] = self.receiver

        # 内嵌图片
        msg.attach(MIMEText(self.content, 'html', 'utf-8'))
        fp = open(self.image_inside, 'rb')
        msgImage = MIMEImage(fp.read())
        msgImage.add_header('Content-ID', '<image1>')
        msg.attach(msgImage)

        # 文本（正文部分）
        text = MIMEText(self.content, 'plain', 'utf-8')
        msg.attach(text)

        # 附件
        for file in self.filelist:
            attachment = MIMEApplication(open(file, 'rb').read())
            attachment.add_header('Content-Disposition', 'Attachment', filename=file)
            msg.attach(attachment)

        smtp.sendmail(self.sender_qq_mail, self.receiver, msg.as_string())
        smtp.quit()


def main():
    try:
        mymail = Mail(host_server, sender_qq_email, sender_qq, pwd, receiver, title, content, image_inside, filelist)
        mymail.sendmail()
        print("邮件发送成功...")
    except smtplib.SMTPException as e:
        print('Error ：邮件发送失败\n 原因：%s' % e)


# ------------
host_server = 'smtp.qq.com'

sender_qq_email = 'Mrtutu3.0@qq.com'

sender_qq = '3522305831'

pwd = 'hflimschcxrndbjh'

receiver = '714471407@qq.com'

title = 'Test via python_mail'

content = """
    <p>python邮件测试</p>
    <p><a href = "www.mrtutu.com">个人博客</a></p>
    <p><img src ="cid:image1"></p>
"""

image_inside = 'code.jpg'

filelist = ['code.jpg']
# ------------


if __name__ == '__main__':
    main()