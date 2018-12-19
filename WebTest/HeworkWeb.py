#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

sys.path.append('../')

from WebTest import HeWorkWebBase
import time
from setting.driver_setting import Hework_Web_attr
import unittest


class HeworkWeb(HeWorkWebBase.HeWorkWebBase):

    # 返回driver设置
    def setup_init(self):
        return Hework_Web_attr

    def open_index(self):
        start = time.time()
        self.driver0.get("https://mjob.12582.cn/")
        return time.time() - start

    def open_detail(self):
        start = time.time()
        self.driver0.get("https://mjob.12582.cn/netjob/detail/?jobid=359794475")
        return time.time() - start




if __name__ == '__main__':
    unittest.main()
