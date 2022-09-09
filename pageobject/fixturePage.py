# -*- encoding: utf-8 -*-
# Author: Roger·J
# Date: 2022/9/9 10:58
# File: fixturePage.py
from selenium.webdriver import ActionChains

from pageobject.basePage import basePage
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import *
from typing import *


class fixturePage(basePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def delete_wxapp_operate(self, window_size: Tuple[int, int], test_nev: str):
        """
            根据测试的环境删除小程序图标，test_nev='TEST'删除开发版小程序，test_nev='PRE'删除体验版小程序
        Args:
            window_size: 屏幕大小 window_size[0]为宽度,window_size[1]为高度
            test_nev: 测试环境
        Returns:

        """
        actions = ActionChains(self.driver)  # 初始化动作链

        try:
            element1 = self.find_element_by_xpath('//*[@text="{}"]'.format('开发版' if test_nev == 'TEST' else '体验版'))

            actions.click_and_hold(element1) \
                .pause(2) \
                .move_by_offset(xoffset=window_size[0] / 2, yoffset=window_size[1] * 0.9) \
                .pause(2) \
                .release() \
                .perform()

        except NoSuchElementException:
            print("没有找到小程序图标，直接返回")
