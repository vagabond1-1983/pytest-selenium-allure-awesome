import os
import time

import allure

# /
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# /screenshots/
SCREENSHOT_PATH = os.path.join(ROOT_PATH, "screenshots")

class ScreenShotExtensions:
    @staticmethod
    def take_standard_screenshot(driver, action_name):
        """自动截图并附加到 Allure 报告中"""
        print(f"正在执行截图操作：{action_name}")  # 调试日志
        if not os.path.exists(SCREENSHOT_PATH):
            os.makedirs(SCREENSHOT_PATH)

        screenshot_path = os.path.join(SCREENSHOT_PATH, f"screenshot_{action_name}_{int(time.time())}.png")
        driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name=action_name, attachment_type=allure.attachment_type.PNG)
