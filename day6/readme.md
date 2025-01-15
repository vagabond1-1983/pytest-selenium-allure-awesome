# 第六天
## 框架在关键点截图
- 方案 1：AutoScreenshotDriver，失败原因是不能只重写 webdriver，还需要重写webelement，重写方法较多，比方 send_keys、click、execute等
~~1. 创建 AutoScreenshotDriver，继承 webdriver，并重写 click、send_keys方法，在方法中截图~~
~~2. 利用 pytest.fixture，在 init_driver的时候，先初始化原始 driver，再复制属性给AutoScreenshotDriver的实例，完成子类的构造~~
~~3. 运行脚本，验证 allure 报告中的截图~~
- 方案 2：在 webdriver 上添加事件监听器实现AbstractEventListener，通过钩子做截图、日志打印等。这种方式更加解耦，设计性更好
1. 创建WebDriverListener，在不同动作中做钩子，进行截图、日志打印等
2. 创建自己的EventFiringWebDriver，配置上listener 和 config
3. 实例化 webdriver 是通过以下方式进行：
```python
driver = WebDriverExtended(
        webdriver.Chrome(options=chrome_options),  # 如果 ChromeDriver 不在 PATH 中，请指定其路径，例如：webdriver.Chrome(executable_path='/path/to/chromedriver')
        WebDriverListener(),
        config,
        envs
    )
```
4. 运行脚本，验证 allure 报告中的截图
```shell
# 运行脚本
pytest -s day6/search/testcases/test_baidu_search.py -v --alluredir ./allure_results
# 生成 allure 报告
allure serve ./allure_results
# 清理报告和截图
rm -rf ./allure_results ./screenshots
```

以下是 AbstractEventListener 中常用的钩子方法：

方法名	描述
before_navigate_to(url, driver)	导航到某个 URL 之前触发。
after_navigate_to(url, driver)	导航到某个 URL 之后触发。
before_navigate_back(driver)	回退页面之前触发。
after_navigate_back(driver)	回退页面之后触发。
before_navigate_forward(driver)	前进页面之前触发。
after_navigate_forward(driver)	前进页面之后触发。
before_find(by, value, driver)	查找元素之前触发。
after_find(by, value, driver)	查找元素之后触发。
before_click(element, driver)	点击元素之前触发。
after_click(element, driver)	点击元素之后触发。
before_change_value_of(element, driver)	改变元素值之前触发。
after_change_value_of(element, driver)	改变元素值之后触发。
before_execute_script(script, driver)	执行脚本之前触发。
after_execute_script(script, driver)	执行脚本之后触发。
on_exception(exception, driver)	发生异常时触发。

## 失败截图
如果需要更细粒度的控制（例如仅在失败时截图），可以使用 pytest 的钩子函数 pytest_runtest_makereport：
注意：需要在 conftest.py 中注册pytest_runtest_makereport钩子函数，pytest 是默认加载的。如果写到其他文件中，需要在 conftest 中注册引入
```python
import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_path = f"screenshot_failure_{int(time.time())}.png"
            driver.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)
```