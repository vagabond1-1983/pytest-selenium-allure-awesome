import allure

from day7.pet.po.pet_order import PetOrderPO


class TestPetOrder:
    @allure.feature("pet 下单流程")
    @allure.story("单个商品下单流程")
    def test_pet_order(self, setup, envs):
        driver = setup
        petLoginPO = PetOrderPO(driver, envs)
        petLoginPO.order_single_good()
