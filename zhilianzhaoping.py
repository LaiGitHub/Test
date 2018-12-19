#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hework_base
from setting import driver_setting
import unittest
import random


class Zhilianzhaopin(hework_base.HeworkBase):
    # 返回driver设置
    def setup_init(self):
        return driver_setting.zhilianzhaoping_attr

    def start_delay(self):
        print('start_delay')
        return random.random()

    def search_delay(self, key):
        print('search_delay %s' % key)
        return random.random()

    def detail_delay(self):
        print('detail_delay')
        return random.random()


if __name__ == '__main__':
    unittest.main()
