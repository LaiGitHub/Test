#!/usr/bin/python
# -*- coding: utf-8 -*-

from appium import webdriver

from base.test_base import TestBase
from utils.resource_util import ResourceUtils


class ClientBase(TestBase):

    # 开始测试前会调用，根据子类对象的setup_init()返回的attribute 生成相应driver list
    def setUp(self):
        super().setUp()
        self.drivers = []
        # 输出attributes设置
        self.attributes = self.setup_init()
        self.logger.info(' Driver Setting ')
        for i, v in self.attributes[0].items():
            self.logger.info("%s : %s" % (i, v))
        self.logger.info(' End Driver Setting ')

        for attr in self.attributes:
            # 默认端口 4723
            driver = webdriver.Remote("http://localhost:%s/wd/hub" % 4723, attr)
            # port += 2
            # 默认等待时间30秒
            driver.implicitly_wait(30)
            self.drivers.append(driver)
        # 将driver0取出方便使用
        self.driver0 = self.drivers[0]

    # 获取性能测试工具类
    def get_resource(self):
        attr = self.attributes[0]
        return ResourceUtils(attr)
