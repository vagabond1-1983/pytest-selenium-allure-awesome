import logging

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Base:
    @allure.step("pet网站登录")
    def __init__(self, driver, envs):
        # 打开Pet首页
        base_url = envs['global']['login_url']
        self.driver = driver
        driver.get(base_url)
        logging.info(f"打开Pet登录页：{base_url}")
        # 输入用户名和密码
        driver.find_element(by=By.CSS_SELECTOR, value="input[name='username']").send_keys(envs['global']['username'])
        password_input = driver.find_element(by=By.CSS_SELECTOR, value="input[name='password']")
        password_input.clear()
        password_input.send_keys(envs['global']['password'])
        logging.info(f"输入用户名：{envs['global']['username']}/密码：{envs['global']['password']}")
        try:
            submit_button = driver.find_element(by=By.CSS_SELECTOR, value="input[name='signon']")
            print(f'submit button: {submit_button.is_enabled()} & {submit_button.is_displayed()}')
            submit_button.click()
        except Exception as e:
            print(f'发生错误{e}')
        logging.info(f"账户：{envs['global']['username']}进行登录操作")

        welcome_div_text = driver.find_element(by=By.ID, value="WelcomeContent").text
        logging.info(f"登录成功，欢迎您：{welcome_div_text}")
        assert f"Welcome {envs['global']['username']}" in welcome_div_text


