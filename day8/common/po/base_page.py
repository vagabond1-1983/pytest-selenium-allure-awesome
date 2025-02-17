from day8.utils.log import logger
import allure
from selenium.webdriver.common.by import By


class Base:
    @allure.step("pet网站登录")
    def __init__(self, driver, envs):
        # 打开Pet首页
        base_url = envs['global']['login_url']
        self.driver = driver
        driver.get(base_url)
        logger.info(f"打开Pet登录页：{base_url}")
        # 输入用户名和密码
        driver.find_element(by=By.CSS_SELECTOR, value="input[name='username']").send_keys(envs['global']['username'])
        password_input = driver.find_element(by=By.CSS_SELECTOR, value="input[name='password']")
        password_input.clear()
        password_input.send_keys(envs['global']['password'])
        logger.info(f"输入用户名：{envs['global']['username']}/密码：{envs['global']['password']}")
        try:
            driver.find_element(by=By.CSS_SELECTOR, value="input[name='signon']").click()
        except Exception as e:
            logger.error(f'发生错误{e}')
        logger.info(f"账户：{envs['global']['username']}进行登录操作")

        welcome_div_text = driver.find_element(by=By.ID, value="WelcomeContent").text
        logger.info(f"登录成功，欢迎您：{welcome_div_text}")
        assert f"Welcome {envs['global']['username']}" in welcome_div_text


