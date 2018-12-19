#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time

files = [
    "he_work.py.py",
]
for i in range(20):
    for f in files:
        print(os.system("python " + f))
