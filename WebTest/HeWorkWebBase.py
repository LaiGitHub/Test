#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base.web_base import WebBase


class HeWorkWebBase(WebBase):

    def test_a(self):
        self.data["open_index_delay"] = self.open_index()
        self.data["detail_delay"] = self.open_detail()
