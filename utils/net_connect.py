#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from time import sleep
import traceback


# 南基外网连接脚本 ，Chrome浏览器
class NetConnect(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.accept_next_alert = True

    def test_nfjd(self):
        driver = self.driver
        account = "oudecheng"
        password = ""
        driver.get("https://auth.nfjd.gmcc.net/dana-na/auth/url_default/welcome.cgi")
        # driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(account)
        # driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_name("btnSubmit").click()
        try:
            driver.find_element_by_name("btnContinueSessionsToEnd").click()
        except:
            pass

    def tearDown(self):
        sleep(100)
        self.driver.quit()
        # self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    while True:
        try:
            unittest.main()
        except:
            pass
        sleep(60 * 15)
