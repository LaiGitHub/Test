#!/usr/bin/python
# -*- coding: utf-8 -*-
from base import test_base

from selenium import webdriver


class WebBase(test_base.TestBase):

    def setUp(self):
        super().setUp()
        self.drivers = []
        self.driver0 = webdriver.Chrome()
        self.driver0.implicitly_wait(30)
        self.drivers.append(self.driver0)
        self.attributes = self.setup_init()
