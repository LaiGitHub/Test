#!/usr/bin/env python
# -*- coding: utf-8 -*-
# driver attribute 配置的地方

# adb devices
udids = [
    "3HX7N16B02002600",
    "6EB0217810002672",  # 荣耀7
]
# 新命令默认等待时间
newCommandTimeout = 3600

hework_header = ['start_delay', 'search_delay', 'detail_delay']

hework_attr = [
    {
        'appPackage': 'com.feinno.innervation',
        'appActivity': 'com.feinno.innervation.activity.SplashActivity',
        # 'appWaitActivity': 'com.cmcc.cmrcs.android.ui.activities.HomeActivity',
        'unicodeKeyboard': 'True',
        "product": "和工作",
        "deviceName": "Android",
        'platformName': 'Android',
        "newCommandTimeout": newCommandTimeout,
        "udid": udids[0],
        "noReset": "True",
    },
]

zhilianzhaoping_attr = [
    {
        'appPackage': 'com.zhaopin.social',
        'appActivity': 'com.zhaopin.social.SplashActivity',
        # 'appWaitActivity': 'com.cmcc.cmrcs.android.ui.activities.HomeActivity',
        'unicodeKeyboard': 'True',
        "product": "智联招聘",
        "deviceName": "Android",
        'platformName': 'Android',
        "newCommandTimeout": newCommandTimeout,
        "udid": udids[0],
        "noReset": "True",
    },
]

Hework_Web_attr = [
    {
        "product": "和工作",
        'platformName': 'Web',
        'network': '固网'
    }
]

zhilianzhaoping_Web_attr = [
    {
        "product": "智联招聘",
        'platformName': 'Web',
        'network': '固网'
    }
]
