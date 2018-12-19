#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import 父类时，不能直接import类，要import 文件，不然unittest.main() 会将父类test方法运行
import hework_base

from setting import driver_setting
import unittest
import random


class Hework(hework_base.HeworkBase):
    # 返回driver设置
    def setup_init(self):
        return driver_setting.hework_attr

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
