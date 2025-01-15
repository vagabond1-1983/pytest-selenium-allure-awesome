import logging

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Base:
    @allure.step("打开首页")
    def __init__(self, driver, envs):
        # 打开百度首页
        base_url = envs['global']['base_url']
        self.driver = driver
        driver.get(base_url)
        logging.info(f"打开百度首页：{base_url}")
        # 当搜索框加载完毕则强制终止加载，因为百度还需要加载热搜等其他资源，耗时较长
        search_box = driver.find_element(By.ID, 'kw')
        search_box.send_keys(Keys.ESCAPE)
        logging.info("搜索框加载完毕 ，并且终止其他资源加载")


