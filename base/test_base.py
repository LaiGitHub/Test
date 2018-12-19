#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import unittest

from setting.sql_setting import sql_setting
from utils import logger
from utils.db_helper import insert_data


class TestBase(unittest.TestCase):

    # 开始测试前会调用，根据子类对象的setup_init()返回的attribute 生成相应driver list
    def setUp(self):
        self.logger = logger.get_logger()
        self.logger.info(' Start Test ')
        self.data = {}

    # 结束测试时会调用将对象中的字典self.data数据存入数据库。
    def tearDown(self):
        table_name = sql_setting['table_name']
        self.logger.info('End Test  ')

        self.logger.info('Save Data To Table : %s  ' % table_name)
        datas = self.data
        for k, v in datas.items():
            self.logger.info("Save Data %s  : %s" % (k, v))
            if not (self.attributes[0]['platformName'] == 'Web' or self.attributes[0]['platformName'] == 'WEB'):
                network = self.driver0.network_connection
            else:
                network = self.attributes[0]['network']
            self.save_data(table_name, k, v, network)
        i = 0
        try:
            for driver in self.drivers:
                self.logger.info('Close Driver %s ' % i)
                driver.quit()
                i += 1
        except:
            pass
            # traceback.print_exc()

    def clickPopup(self, id):
        try:
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_id(id).click()
            self.logger.info("处理弹窗")
            self.driver.implicitly_wait(30)
        except:
            pass

    def save_data(self, table_name, business, data_value, network='wifi', data_type='delay'):
        attr = self.attributes[0]
        table = table_name
        # 插入的数据
        data_dict = {
            "product_name": attr["product"],
            "client": attr["platformName"],
            "bussiness": business,
            "data_type": data_type,
            "data_value": data_value,
            "network": network,
            "remark": "",
            "test_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        insert_data(table, data_dict)
