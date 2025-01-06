import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from day3.common.po.base_page import Base


class BaiduSearchPO(Base):
    def __init__(self, driver, envs):
        super().__init__(driver, envs)

    @allure.step("在搜索框中输入{keyword}，点击百度一下")
    def search(self, keyword):
        # 找到搜索框并输入关键词
        search_box = self.driver.find_element(By.ID, 'kw')
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.ENTER)
        # 等待搜索结果加载
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'tsn_inner')))
        # 返回搜索结果，方便断言
        return self.driver.page_source.lower()