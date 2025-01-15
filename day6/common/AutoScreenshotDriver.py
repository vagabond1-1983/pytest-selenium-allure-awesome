import os

from selenium.webdriver.remote.webdriver import WebDriver
import allure
import time


class AutoScreenshotDriver(WebDriver):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _take_screenshot(self, action_name):
        """自动截图并附加到 Allure 报告中"""
        print(f"正在执行截图操作：{action_name}")  # 调试日志
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        screenshot_path = os.path.join(screenshot_dir, f"screenshot_{action_name}_{int(time.time())}.png")
        self.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name=action_name, attachment_type=allure.attachment_type.PNG)

    def send_keys(self, *args, **kwargs):
        """重写输入方法，自动截图"""
        super().send_keys(*args, **kwargs)
        self._take_screenshot("send_keys")

    def click(self, **kwargs):
        """重写点击方法，自动截图"""
        super().click(**kwargs)
        self._take_screenshot("click")

