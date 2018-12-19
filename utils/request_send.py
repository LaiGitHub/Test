# -*- coding: utf-8 -*-
import requests
import json


# 发送请求的类
class send:
    server = "http://47.106.113.118:1111/"

    # server = "http://127.0.0.1:8000/"

    @staticmethod
    def upload(filepath):
        try:
            url = 'http://116.196.88.223/img_upload'
            with open(filepath, "rb") as file:
                return requests.post(url, files={'file': file}).json()['imageurl']
        except:
            return None

    @staticmethod
    def send_request(data, path):
        datajson = json.dumps(data)
        url = send.server + path
        re = requests.post(url, datajson)
        print(re.json())
        if re.json()['code'] == 1:
            return True
        else:
            return False

    @staticmethod
    def send_test_data(product, version, platform, caseName, ispass, image):
        send.send_request(
            {'product': product, 'version': version, 'platform': platform, 'caseName': caseName, 'ispass': ispass,
             'image': image}, 'post_test_data2')

    @staticmethod
    def send_kqi_data(product_name, client, bussiness, data_type, data_value, image=None, id_delete='0'):
        send.send_request(
            {'product_name': product_name, 'client': client, 'bussiness': bussiness, 'data_type': data_type,
             'data_value': data_value, 'image': image, 'id_delete': id_delete}, 'kqi')

    @staticmethod
    def getsms(sender, receiver, message="", delay="300"):
        data = {"sender": sender, "receiver": receiver, "message": message}
        url = send.server + "/testutils/sms"
        re = requests.get(url, data)
        return re.json()

    @staticmethod
    def send_data(host, ip, caseName, testValue, remark):
        send.send_request(
            {'host': host, 'ip': ip, 'caseName': caseName, 'testValue': testValue, 'remark': remark
             }, 'postdata/')


if __name__ == '__main__':
    send.send_data('221.221.112.111', '114.114.114.114', "端到端网络时延", '111', 'remark')
