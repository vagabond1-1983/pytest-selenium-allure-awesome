import logging
import datetime
import os

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.events import AbstractEventListener
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from day6.utils.screenshot_extensions import ScreenShotExtensions

# logs/xx.log
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
LOG_PATH = os.path.join(ROOT_PATH, 'logs')


class WebDriverListener(AbstractEventListener):
    log_filename = datetime.datetime.now().strftime("%Y%m%d")
    log_format = "%(asctime)s: %(levelname)s: %(message)s"
    logging.basicConfig(
        # log file will be created in "tests" directory. Feel free to change the path or filename
        filename=os.path.join(LOG_PATH, f"{log_filename}.log"),
        format=log_format,
        level=logging.INFO
    )

    def __init__(self, console_print=False, timeout=10):
        self.logger = logging.getLogger("selenium")
        self.timeout = timeout
        if console_print:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_handler.setFormatter(logging.Formatter(self.log_format))
            self.logger.addHandler(console_handler)

    def before_navigate_to(self, url, driver):
        self.logger.info(f"Navigating to {url}")

    def after_navigate_to(self, url, driver):
        self.logger.info(f"{url} opened")

    def before_find(self, by, value, driver):
        self.logger.info(f"Searching for element by {by} {value}")
        self.by = by
        self.locator = value
        WebDriverWait(driver, self.timeout).until(EC.presence_of_element_located((by, value)))


    def after_find(self, by, value, driver):
        self.logger.info(f"Element by {by} {value} found")

    def before_click(self, element, driver):
        self.logger.info(f"Clicking for element by {self.by} {self.locator}")
        element_id = self._get_element_id(element)
        self.logger.info(f"{element_id} is enabled and displayed")

        if element.get_attribute("text") is None and element.get_attribute("class") is None:
            self.logger.info(f"Clicking on {element_id}")
        elif element.get_attribute("class") is None:
            self.logger.info(f"Clicking on {element.get_attribute('text')}")
        else:
            self.logger.info(f"Clicking on {element.get_attribute('class')}")

    def after_click(self, element, driver):
        element_id = self._get_element_id(element)
        self.logger.info(f"{element_id} clicked")
        ScreenShotExtensions.take_standard_screenshot(action_name=f"{element_id}_click", driver=driver)

    def _get_element_id(self, element):
        # 尝试使用元素的 id 或 name 作为文件名的一部分
        try:
            element_id = element.get_attribute('id') or element.get_attribute('name') or element.tag_name
        except Exception as e:
            element_id = "t_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        return element_id

    def before_change_value_of(self, element, driver):
        self.logger.info(f"tag是{element.tag_name}的{element.get_attribute('name')}，原始值为：{element.get_attribute('text')}")

    def after_change_value_of(self, element, driver):
        self.logger.info(f"{element.get_attribute('text')} value changed")
        ScreenShotExtensions.take_standard_screenshot(action_name=f"{element.get_attribute('name')}_change_value",
                                                      driver=driver)

    def before_quit(self, driver):
        self.logger.info("Driver quitting")

    def after_quit(self, driver):
        self.logger.info("Driver quit")

    def on_exception(self, exception, driver):
        self.logger.info(exception)
        ScreenShotExtensions.take_standard_screenshot(action_name="exception", driver=driver)
