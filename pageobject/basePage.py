# -*- encoding: utf-8 -*-
# Author: Roger·J
# Date: 2022/9/9 10:34
# File: basePage.py

from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from typing import *


class basePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def back(self):
        """
            返回上一页
        Returns:

        """
        self.driver.back()

    def find_element_by_id(self, id_str: str) -> WebElement:
        """
            根据id查找元素
        Args:
            id_str: 字符串类型的id
        Returns:
            appium.webdriver.webelement.WebElement
        """
        return self.driver.find_element(By.ID, id_str)

    def find_element_by_name(self, name: str) -> WebElement:
        """
            根据name查找元素
        Args:
            name: 标签中name属性值
        Returns:
            appium.webdriver.webelement.WebElement
        """
        return self.driver.find_element(By.NAME, name)

    def find_element_by_xpath(self, xpath: str) -> WebElement:
        """
            根据xpath查找元素
        Args:
            xpath:
        Returns:
            appium.webdriver.webelement.WebElement
        """
        return self.driver.find_element(By.XPATH, xpath)



    def get_driver_windows_size(self) -> Tuple[Any, Any]:
        """
            获取手机屏幕长宽
        Args:

        Returns:
            width: 手机屏幕宽
            height: 手机屏幕长
        """
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        return width, height

    def switch_context(self, context_name: str):
        """
            切换小程序上下文，例如从原生app切换到微信小程序native_app -> WEBVIEW_com.tencent.mm:appbrand0
        Args:
            context_name: 需要切换的进程名
        Returns:

        """
        self.driver.switch_to.context(context_name)

    def switch_window_handle(self, search_condition: Any):
        """
            对于小程序中多级页面需要通过切换窗口句柄去获取页面源码
            通过轮询方式去切换每一个窗口句柄，但需要搜索条件确定切换到需要的窗口句柄
        Args:
            search_condition: 切换的指定的窗口所需的条件
        Returns:

        """
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.page_source.find(search_condition) != -1:
                break
