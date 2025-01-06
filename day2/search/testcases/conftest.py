import json
import logging
import os.path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ../../../testcases(conftest.py)
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
CONFIG_FILE = os.path.join(ROOT_PATH, 'config.json')
# 加载全局配置和环境配置
@pytest.fixture(scope='session')
def config():
    # 加载全局配置
    config_file = open(CONFIG_FILE)
    return json.load(config_file)

# 默认加载的 fixture
@pytest.fixture(scope='function')
def setup(config):
    driver = init_driver(config)
    yield driver
    # 测试结束后关闭浏览器
    driver.quit()


def init_driver(config):
    # 设置 chrome 选项
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")  # 禁用扩展
    chrome_options.add_argument("--disable-gpu")  # 禁用 GPU 加速
    chrome_options.add_argument("--no-sandbox")  # 禁用沙盒模式
    if config['headless']:
        chrome_options.add_argument("--headless")  # 无头模式（可选）
    # 初始化 Chrome 浏览器
    driver = webdriver.Chrome(
        options=chrome_options)  # 如果 ChromeDriver 不在 PATH 中，请指定其路径，例如：webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.maximize_window()
    driver.implicitly_wait(config['timeout'])
    logging.info('init browser')
    return driver
