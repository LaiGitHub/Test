#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import time
import threading
from utils import test_util
import subprocess


# 性能工具类
# 推荐用Android7.0的手机开展性能测试
# 本脚本是用华为mate9(Android 7.0 )写的，适配华为8.0以下的手机，其他手机适配未知，测试前需检查数据是否准确
class ResourceUtils(object):
    # 传入参数 driver 的attribute
    def __init__(self, attr, intervals=0.1):
        self.package = attr['appPackage']
        self.activity = attr['appActivity']
        self.product = attr['product']
        self.cpus = []
        self.rams = []
        self.isCpu = True
        self.isRam = True
        self.intervals = intervals
        self.udid = attr['udid']
        if self.udid != "":
            self.udid = " -s " + self.udid

    # 通过adb命令（windows）获取内存
    def get_ram(self, package):
        l = self.run_cmd('adb %s shell dumpsys meminfo %s' % (self.udid, package))
        lines = l.splitlines()
        for line in lines:
            if re.findall('TOTAL', line):
                ram = float(line.split()[1]) / 1024.0
                return ram
        return 0.0

    # 通过adb命令（windows）获取cpu占用值
    # Android 7.0及以下
    def get_cpu(self, package):
        l = self.run_cmd('adb %s shell top -m 1000 -n 1 -s cpu -d 0.01| findstr %s' % (self.udid, package))
        if "%" not in l:
            return 0.0
        petten1 = "\d+%"
        cpus = re.findall(petten1, l)
        petten2 = "\d+"
        cpus_sum = 0
        for cpu in cpus:
            acpu = re.search(petten2, cpu)[0]
            if acpu.isalnum():
                cpus_sum += int(acpu)
        return cpus_sum

    # 循环获取内存，保存于rams
    def get_rams(self):
        while self.isRam:
            ram = self.get_ram(self.package)
            print("ram  " + str(ram))
            self.rams.append(ram)
            time.sleep(self.intervals)

    # 循环获取cpu占用，保存于cpu
    def get_cpus(self):
        while self.isCpu:
            cpu = self.get_cpu(self.package)
            self.cpus.append(cpu)
            self.cpus.sort()
            # if (cpu == self.cpus[-1]):
            #     self.run_cmd("adb " + self.udid + " shell screencap -p /sdcard/cpu/+" + str(cpu) + ".png")
            print("cpu  " + str(cpu))
            time.sleep(self.intervals)

    # 开启获取内存线程
    def ram_start(self):
        self.isRam = True
        thread_ram = threading.Thread(target=self.get_rams, name='mem')
        thread_ram.start()

    # 开启获取cpu线程
    def cpu_start(self):
        self.isCpu = True
        thread_cpu = threading.Thread(target=self.get_cpus, name='cpu')
        thread_cpu.start()

    # 停止获取cpu线程
    def cpu_stop(self):
        self.isCpu = False

    # 停止获取内存线程
    def ram_stop(self):
        self.isRam = False

    # 获取cpu峰值
    def cpu_get_max(self):
        self.cpus.sort()
        return self.cpus[-1]

    # 获取内存峰值
    def ram_get_max(self):
        self.rams.sort()
        return self.rams[-1]

    def run_cmd(self, cmd):
        # print(cmd)
        with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as process:
            cmd_str = process.stdout.read().decode("gbk")
        return cmd_str

    # 获取流量
    def get_flow(self):
        return self._get_all_flow(package=self.package, udid=self.udid)

    # 获取系统电量记录
    def get_power_record(self):
        pid = self.run_cmd("adb shell ps | findstr %s" % self.package).split(' ')[0].replace('_', '')
        # print(a)
        b = run_cmd("adb shell dumpsys batterystats %s |findstr %s" % (self.package, pid))
        pattern = ':\s\d+.\d+'
        p = re.search(pattern, b).group().split(' ')[1]
        return p

    # 清除系统电量记录
    def clean_power_record(self):
        os.system("adb %s shell dumpsys battery reset" % self.udid)
        os.system("adb %s shell dumpsys battery unplug" % self.udid)

    # 启动PowerTutor 开始记录电量数据
    @DeprecationWarning
    def start_PowerTutor_record(self, driver):
        # 启动PowerTutor
        time.sleep(10)
        test_util.adb_start_app(udid=self.udid, package='edu.umich.PowerTutor',
                                activity='edu.umich.PowerTutor.ui.UMLogger')
        time.sleep(5)
        ServiceStartButton = driver.find_element_by_id("edu.umich.PowerTutor:id/servicestartbutton")
        if (ServiceStartButton.text == "Stop Profiler"):
            ServiceStartButton.click()
        ServiceStartButton.click()
        test_util.adb_start_app(udid=self.udid, package=self.package,
                                activity=self.activity)

    # 获取PowerTutor电量记录
    @DeprecationWarning
    def get_PowerTutor_record(self, driver):
        # 启动PowerTutor
        test_util.adb_start_app(udid=self.udid, package='edu.umich.PowerTutor',
                                activity='edu.umich.PowerTutor.ui.UMLogger')
        product = self.product
        driver.find_element_by_id("edu.umich.PowerTutor:id/appviewerbutton").click()
        tvs = driver.find_elements_by_class_name("android.widget.TextView")
        power_value = ""
        for tv in tvs:
            if (product in tv.text):
                power_value = tv.text
                power_value = power_value.split('\n')[1]
                unit = power_value.split(" ")[1]
                power_value = float(power_value.split(" ")[0])
                if unit == 'mJ':
                    power_value /= 1000
                    print("典型业务运行耗电量")
        return power_value
        # TestUtil.adb_start_app(udid=self.udid, package=self.package,
        #                        activity=self.activity)

    # 返回 接收流量、发送流量
    def _get_flows(self, package, udid=""):
        # if udid != "":
        udid = " -s " + udid
        userid = \
            run_cmd("adb " + udid + " shell  dumpsys package " + package + " |findstr userId= ").split("=")[1]
        receive = 0
        send = 0
        flowstr = run_cmd("adb " + udid + " shell cat /proc/net/xt_qtaguid/stats | findstr " + userid).split(
            "\r\n")
        for s in flowstr:
            ls = s.split(" ")
            if len(ls) <= 1:
                continue
            receive += float(ls[5])
            send += float(ls[7])
        return receive / 1024, send / 1024

    # 获取全部流量
    def _get_all_flow(self, package, udid, ):
        up, download = self._get_flows(package, udid)
        print(up + download)
        return up + download


def run_cmd(cmd):
    with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as process:
        cmd_str = process.stdout.read().decode("gbk")
        print(cmd)
    return cmd_str


if __name__ == '__main__':
    # a = run_cmd("adb shell ps | findstr %s" % 'com.feinno.innervation').split(' ')[0].replace('_', '')
    # # print(a)
    # b = run_cmd("adb shell dumpsys batterystats %s |findstr %s" % ('com.feinno.innervation', a))
    # pattern = ':\s\d+.\d+'
    # p = re.search(pattern, b).group().split(' ')[1]
    # print(p)
    from setting.driver_setting import hework_attr

    ResourceUtils(hework_attr[0]).cpu_start()
