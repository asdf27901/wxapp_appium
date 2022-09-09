# -*- encoding: utf-8 -*-
# Author: Roger·J
# Date: 2022/9/2 10:05
# File: test.py

import subprocess
import re
import time
import threading
import pytest
import yaml

from utils.common import *
from appium import webdriver
from selenium.webdriver.common.by import By
from utils.fileutils import get_yaml_data
from selenium.webdriver.common.action_chains import ActionChains

# adb指令连接安卓设备
# run_cmd("adb devices")
# stdout1 = run_cmd("adb shell dumpsys activity top | grep ACTIVITY")[0]
# print(stdout1)
# pattern_pid = r'/.plugin.appbrand.ui.AppBrandUI\d? [0-9a-z]+ pid=[0-9]+'
# re_result = re_search(pattern_pid, stdout1)
# pid = re_result.split('=')[1]
#
# stdout2 = run_cmd("adb shell ps {}".format(pid))[0]
# pattern_name = r'com.tencent.mm[0-9A-Za-z:]+'
# wxapp_name = re_search(pattern_name, stdout2)
# print(wxapp_name)


# 初始化driver
android_caps = get_yaml_data(u'config/android_caps.yaml')
driver = webdriver.Remote(command_executor=android_caps['EXECUTOR'],
                          desired_capabilities=android_caps[android_caps['DESCRIBE_CAPS']])

# 设置查找元素组件静默等待10s
driver.implicitly_wait(10)
# 获取手机屏幕长和宽
width = driver.get_window_size()['width']
height = driver.get_window_size()['height']
print(width, height)

time.sleep(7)
# 从上到下滑动手机屏幕
swipe_operate(500, 300, 500, 1700)
actions = ActionChains(driver)

time.sleep(4)
# 点击百茶台小程序开发版
element1 = driver.find_element(By.XPATH, '//*[@text="{}"]'.format('开发版' if android_caps['TEST_ENV'] == 'TEST' else '体验版'))


actions.click_and_hold(element1)\
        .pause(2)\
        .move_by_offset(xoffset=width / 2, yoffset=height*0.9)\
        .pause(2)\
        .release()\
        .perform()


# # 获取此时被测机的上下文
# contexts = driver.contexts
# print(contexts)
# # 将上下文切换到小程序中
# driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
# # 打印当前页面源码
# print(driver.page_source)
# # 需执行到此操作再退出appium-server，否则下次启动会报错
time.sleep(3)
driver.quit()

