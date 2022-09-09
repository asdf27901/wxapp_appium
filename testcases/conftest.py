# -*- encoding: utf-8 -*-
# Author: Roger·J
# Date: 2022/9/2 22:55
# File: conftest.py


import os
import pytest
import sys

from utils.logger import log
from time import sleep
from utils.fileutils import get_yaml_data
from appium import webdriver
from utils.common import *
from pageobject.fixturePage import fixturePage

path = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


@pytest.fixture(scope="session")
def get_driver():
    """
    初始化一个driver搜索微信小程序助手，选择百茶台小程序进入
    Returns: 返回一个driver（进入了百茶台小程序选择角色页面）

    """

    # 判断是否连接到手机终端，没有连接到手机直接结束程序
    if run_cmd("adb devices")[0].__len__() <= 26:
        log.error("没有连接手机，请连接手机后重试")
        sys.exit(1)

    # 初始化driver
    android_caps = get_yaml_data(path(u'../config/android_caps.yaml'))
    fixture_xpath = get_yaml_data(path(u'../xpath_yaml/fixturepage.yaml'))

    driver = webdriver.Remote(command_executor=android_caps['EXECUTOR'],
                              desired_capabilities=android_caps[android_caps['DESCRIBE_CAPS']])

    # 设置查找元素组件静默等待10s

    driver.implicitly_wait(10)
    fixturepage = fixturePage(driver)

    # 获取手机屏幕长和宽
    width, height = fixturepage.get_driver_windows_size()

    # 从上到下滑动手机屏幕
    sleep(5)
    swipe_operate(width * 0.5, height * 0.14, width * 0.5, height * 0.8)

    # 根据测试的环境删除对应版本的小程序，TEST删除开发版，PRE删除体验版
    fixturepage.delete_wxapp_operate((width, height), android_caps['TEST_ENV'])

    # 返回上一页
    fixturepage.back()

    # 点击微信搜索按钮
    fixturepage.find_element_by_id('com.tencent.mm:id/f8y').click()
    fixturepage.find_element_by_xpath(fixture_xpath['search_icon']).send_keys('小程序助手')
    fixturepage.find_element_by_xpath(fixture_xpath['wxapp_assistant']).click()

    # 将上下文切换到小程序中
    fixturepage.switch_context(android_caps['CONTEXT_NAME'])
    fixturepage.find_element_by_xpath(fixture_xpath['version_view']).click()

    # 根据搜索条件切换窗口句柄
    fixturepage.switch_window_handle('版本查看')

    # 根据测试的环境选择不同版本的小程序，TEST打开开发版小程序，PRE打开体验版小程序
    if android_caps['TEST_ENV'] == 'TEST':
        fixturepage.find_element_by_xpath(fixture_xpath['beta_version']).click()
    else:
        fixturepage.find_element_by_xpath(fixture_xpath['trial_version']).click()

    sleep(10)
    yield driver

    driver.quit()
