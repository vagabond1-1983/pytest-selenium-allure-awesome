import logging
import datetime
import os

from selenium.webdriver.support.events import AbstractEventListener

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

    def __init__(self, console_print=False):
        self.logger = logging.getLogger("selenium")
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

    def after_find(self, by, value, driver):
        self.logger.info(f"Element by {by} {value} found")

    def before_click(self, element, driver):
        if element.get_attribute("text") is None:
            self.logger.info(f"Clicking on {element.get_attribute('class')}")
        else:
            self.logger.info(f"Clicking on {element.get_attribute('text')}")

    def after_click(self, element, driver):
        text = element.get_attribute('text')
        if element.get_attribute("text") is None:
            self.logger.info(f"{element.get_attribute('class')} clicked")
            text = element.get_attribute('class')
        else:
            self.logger.info(f"{element.get_attribute('text')} clicked")
        ScreenShotExtensions.take_standard_screenshot(action_name=f"{text}_click", driver=driver)

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
