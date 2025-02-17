import allure
from selenium.webdriver.common.by import By

from day8.common.po.base_page import Base


class PetOrderPO(Base):
    def __init__(self, driver, envs):
        super().__init__(driver, envs)

    @allure.step("单件商品下单")
    def order_single_good(self):
        # 一级类目选 Fish
        self.driver.find_element(By.XPATH, value="//*[@id='SidebarContent']/a[1]").click()
        # 商品选择 FI-SW-01， 路径：Fish - FI-SW-01
        self.driver.find_element(By.XPATH, value="//div[@id='Catalog']//td/a[text()='FI-SW-01']").click()
        # 商品种类选择 EST-1， 路径：Fish - FI-SW-01 - EST-1
        self.driver.find_element(By.XPATH, value="//div[@id='Catalog']//td/a[text()='EST-1']").click()
        # 单件商品加入购物车
        self.driver.find_element(By.XPATH, value="//a[@class='Button' and text()='Add to Cart']").click()
        # 提交订单
        self.driver.find_element(By.XPATH, value="//a[@class='Button' and text()='Proceed to Checkout']").click()
        self.driver.find_element(By.XPATH, value="//input[@name='newOrder']").click()
        # 确认
        self.driver.find_element(By.XPATH, value="//a[@class='Button' and text()='Confirm']").click()
        return self.driver.find_element(By.XPATH, value="//div[@id='Content']/ul[@class='messages']").text

