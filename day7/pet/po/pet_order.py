import allure
from selenium.webdriver.common.by import By

from day7.pet.common.po.base_page import Base


class PetOrderPO(Base):
    def __init__(self, driver, envs):
        super().__init__(driver, envs)

    @allure.step("单件商品下单")
    def order_single_good(self):
        pass
