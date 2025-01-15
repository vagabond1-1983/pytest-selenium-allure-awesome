import json
import logging
import os.path

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from day6.driver.webdriver_extended import WebDriverExtended
from day6.driver.webdriver_listener import WebDriverListener
from day6.utils.screenshot_extensions import ScreenShotExtensions

# ../../../testcases(conftest.py)
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
CONFIG_FILE = os.path.join(ROOT_PATH, 'config.json')
ENV_PATH = os.path.join(ROOT_PATH, 'config')
# 加载全局配置和环境配置
@pytest.fixture(scope='session')
def config():
    # 加载全局配置
    config_file = open(CONFIG_FILE)
    return json.load(config_file)

@pytest.fixture(scope='session')
def envs(config):
    env_file = os.path.join(ENV_PATH, f"config-{config['default']}.yaml")
    logging.info(f"load env file: {env_file}")
    return yaml.safe_load(open(env_file))

# 默认加载的 fixture
@pytest.fixture(scope='class')
def setup(config, envs):
    driver = init_driver(config, envs)
    yield driver
    # 测试结束后关闭浏览器
    driver.quit()


def init_driver(config, envs):
    # 设置 chrome 选项
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")  # 禁用扩展
    chrome_options.add_argument("--disable-gpu")  # 禁用 GPU 加速
    chrome_options.add_argument("--no-sandbox")  # 禁用沙盒模式
    if config['headless']:
        chrome_options.add_argument("--headless")  # 无头模式（可选）
    # 初始化 Chrome 浏览器
    driver = WebDriverExtended(
        webdriver.Chrome(options=chrome_options),  # 如果 ChromeDriver 不在 PATH 中，请指定其路径，例如：webdriver.Chrome(executable_path='/path/to/chromedriver')
        WebDriverListener(),
        config,
        envs
    )
    driver.maximize_window()
    driver.implicitly_wait(config['timeout'])
    logging.info('init browser')
    return driver


# 失败截图
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            ScreenShotExtensions.take_standard_screenshot(action_name="failure", driver=driver)
