from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from day2.common.po.base_page import Base


class BaiduSearchPO(Base):
    def __init__(self, driver, config):
        super().__init__(driver, config)

    def search(self, keyword):
        # 找到搜索框并输入关键词
        search_box = self.driver.find_element(By.ID, 'kw')
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.ENTER)
        # 等待搜索结果加载
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'tsn_inner')))
        # 返回搜索结果，方便断言
        return self.driver.page_source.lower()