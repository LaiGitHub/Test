#!/usr/bin/env python
# -*- coding: utf-8 -*-
from WebTest.HeWorkWebBase import HeWorkWebBase
import time
from setting.driver_setting import zhilianzhaoping_Web_attr


class HeworkWeb(HeWorkWebBase):

    # 返回driver设置
    def setup_init(self):
        return zhilianzhaoping_Web_attr

    def open_index(self):
        start = time.time()
        self.driver0.get("https://www.zhaopin.com/")
        return time.time() - start

    def open_detail(self):
        start = time.time()
        self.driver0.get("https://jobs.zhaopin.com/CC456246487J00254046801.htm")
        return time.time() - start
