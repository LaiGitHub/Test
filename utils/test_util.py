#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random
import smtplib
import time
from email import encoders
from email.mime.multipart import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from PIL import Image

import hashlib


# 生成图片，只有两种规格 100KB 1MB
# 将图片放入手机中
# adb发送广播，让系统图库更新
def put_image_to_phone(udid, size_kb=1024):
    print(udid)
    if udid:
        udid = " -s " + udid + " "
    else:
        udid = ""
    if size_kb == 1024:
        img = Image.new("RGB", size=(10005, 6700))  # 1MB
    else:
        img = Image.new("RGB", size=(9700, 670))  # 100K
    x = int(random.uniform(0, img.size[0] - 1))
    y = int(random.uniform(0, img.size[1] - 1))
    img.putpixel((x, y), int(random.uniform(0, 254)))
    # print(x, y)
    # print(os.path.getsize("./image/1.jpg"))
    img.save("./image/1.jpg")

    # print(GetFileMd5("./image/1.jpg"))
    os.system("adb" + udid +
              " push ./image/1.jpg storage/emulated/0/DCIM//1.jpg")
    os.system(
        "adb " + udid +
        "shell am broadcast "
        "-a android.intent.action.MEDIA_SCANNER_SCAN_FILE "
        "-d file:////storage/emulated/0/DCIM//1.jpg")


def put_video_to_phone(udid, floder="DCIM"):
    with open("./image/2M.mp4", 'rb') as v:
        with open("./image/2MB.mp4", 'wb+') as f:
            # print(v.read())
            b = bytearray(v.read())
            a = int(len(b) / 4)
            for i in range(10):
                b[a + int(random.random() * a * 2)] = int(random.random() * 255)
            f.write(bytes(b))
    udid = " -s " + udid + " "
    filename = str(int(time.time())) + "2MB.mp4"
    os.system("adb" + udid +
              " push ./image/2MB.mp4 storage/emulated/0/" + floder + "//" + filename)
    os.system(
        "adb " + udid +
        "shell am broadcast "
        "-a android.intent.action.MEDIA_SCANNER_SCAN_FILE "
        "-d file:////storage/emulated/0/" + floder + "//" + filename)


# adb 打开app
def adb_start_app(udid, package, activity):
    cmd = '''adb  %s shell am start -n %s/%s''' % (udid, package, activity)
    print(cmd)
    os.system(cmd)


# adb 关闭 app
def adb_stop_app(udid, package):
    os.system("adb %s shell am force-stop %s" % (udid, package))


products = \
    [
        {"product": "189邮箱", "user": "14715006970@189.cn", "password": "qwer1234", "smtp": "smtp.189.cn",
         "imap": "imap.189.cn", "time": 0},
        {"product": "网易邮箱", "user": "cmicqwer@163.com", "password": "wert1234", "smtp": "smtp.163.com",
         "imap": "imap.163.com", "time": 0},
        {"product": "139邮箱", "user": "13772425381@139.com", "password": "qwer1234", "smtp": "smtp.139.com",
         "imap": "imap.139.com", "time": 0},
        {"product": "qq邮箱", "user": "869125157@qq.com", "password": "xycwtamllrqabcdg", "smtp": "smtp.qq.com",
         "imap": "imap.qq.com", "time": 0},
        {"product": "新浪邮箱", "user": "14715006970@sina.cn", "password": "qwer1234", "smtp": "smtp.sina.cn",
         "imap": "imap.sina.cn", "time": 0},
    ]


# 发送邮件
def send_mail(mail, to_mail, subject, mail_text, attachment_size_MB):
    product = {}
    for p in products:
        if p["product"] == mail:
            product = p
    msg = MIMEMultipart()
    msg['From'] = product["user"]
    msg['To'] = to_mail
    msg['Subject'] = subject
    msg.attach(MIMEText(mail_text, 'plain', 'utf-8'))
    # 随机生成的文件
    filename = "./file/" + str(attachment_size_MB) + "M.rar"
    with open(filename, "wb") as f:
        f.write(os.urandom(1024 * 1024 * attachment_size_MB))
    with open(filename, 'rb') as f:
        # 设置附件的MIME和文件名，这里是rar类型:
        mime = MIMEBase('rar', 'rar', filename='1M.rar')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='1M.rar')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)
        server = smtplib.SMTP_SSL(product["smtp"], 465)  # SMTP协议默认端口是25 ,ssl 465
        server.set_debuglevel(0)
        server.login(product["user"], product["password"])
        server.sendmail(product["user"], to_mail, msg.as_string())

        server.quit()


# 获取文件md5
def get_md5_01(file_path):
    md5 = None
    if os.path.isfile(file_path):
        f = open(file_path, 'rb')
        md5_obj = hashlib.md5()
        md5_obj.update(f.read())
        hash_code = md5_obj.hexdigest()
        f.close()
        md5 = str(hash_code).lower()
    return md5


if __name__ == '__main__':
    # com.huawei.systemmanager/.power.ui.HwPowerManagerActivity
    # com.huawei.systemmanager/.power.ui.ConsumeLevelActivity
    adb_start_app(udid='-s 3HX7N16B02002600', package='com.huawei.systemmanager',
                  activity='.power.ui.HwPowerManagerActivity')
    # for i in range(1):
    #     img = Image.open("./image/3M.jpg")
    #     # img = Image.new("RGB", size=(5000, 6700))  # 1MB
    #     for i in range(1):
    #         x = int(random.uniform(0, img.size[0] - 1))
    #         y = int(random.uniform(0, img.size[1] - 1))
    #         img.putpixel((x, y), int(111))
    #         # print(x, y)
    #         # print(os.path.getsize("./image/1.jpg"))
    #     img.save("./image/" + '500_build' + ".jpg")
