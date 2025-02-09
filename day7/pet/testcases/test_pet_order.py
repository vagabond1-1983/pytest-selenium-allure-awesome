import allure

from day7.pet.po.pet_order import PetOrderPO


class TestPetOrder:
    @allure.feature("pet 下单流程")
    @allure.story("单个商品下单流程")
    def test_pet_order(self, setup, envs):
        driver = setup
        petLoginPO = PetOrderPO(driver, envs)
        order_msg = petLoginPO.order_single_good()
        print(f"message popup after order: {order_msg}")
        assert order_msg == "Thank you, your order has been submitted."
