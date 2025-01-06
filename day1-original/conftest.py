import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# 默认加载的 fixture
@pytest.fixture(scope='class')
def browser():
    # 设置 chrome 选项
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")  # 禁用扩展
    chrome_options.add_argument("--disable-gpu")  # 禁用 GPU 加速
    chrome_options.add_argument("--no-sandbox")  # 禁用沙盒模式
    # chrome_options.add_argument("--headless")  # 无头模式（可选）
    # 初始化 Chrome 浏览器
    driver = webdriver.Chrome(options=chrome_options)  # 如果 ChromeDriver 不在 PATH 中，请指定其路径，例如：webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.maximize_window()
    driver.implicitly_wait(10)
    logging.info('init browser')
    # 打开百度首页
    driver.get('https://www.baidu.com')
    # 当搜索框加载完毕则强制终止加载，因为百度还需要加载热搜等其他资源，耗时较长
    search_box = driver.find_element(By.ID, 'kw')
    search_box.send_keys(Keys.ESCAPE)
    yield driver
    # 测试结束后关闭浏览器
    driver.quit()
