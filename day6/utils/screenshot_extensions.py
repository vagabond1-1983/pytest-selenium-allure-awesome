import os
import time

import allure

# ../../screeshots
ROOT_PATH = os.path.dirname(os.path.dirname(__file__))


class ScreenShotExtensions:
    @staticmethod
    def take_standard_screenshot(driver, action_name):
        """自动截图并附加到 Allure 报告中"""
        print(f"正在执行截图操作：{action_name}")  # 调试日志
        screenshot_dir = os.path.join(ROOT_PATH, "screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        screenshot_path = os.path.join(screenshot_dir, f"screenshot_{action_name}_{int(time.time())}.png")
        driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name=action_name, attachment_type=allure.attachment_type.PNG)
