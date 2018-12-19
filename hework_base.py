#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from base.client_base import ClientBase


# 继承ClientBase
# 编写逻辑，测试数据通过函数返回值返回
class HeworkBase(ClientBase):

    def test_bussiness(self):
        start_delay = self.start_delay()
        # time.sleep(30)  # 等待30秒
        resource = self.get_resource()
        resource.cpu_start()
        resource.ram_start()
        resource.clean_power_record()
        search_delay = self.search_delay('销售')
        detail_delay = self.detail_delay()
        # time.sleep(10)  # 等待10秒
        self.data['start_delay'] = start_delay
        self.data['search_delay'] = search_delay
        self.data['detail_delay'] = detail_delay
        time.sleep(10)
        power = resource.get_power_record()
        resource.cpu_stop()
        resource.ram_stop()
        self.data['power'] = power
        self.data["ram"] = resource.ram_get_max()
        self.data["cpu"] = resource.cpu_get_max()
