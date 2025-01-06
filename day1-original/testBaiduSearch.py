import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize('keyword, expected', [
    ('pytest', 'pytest'),
    # ('selenium', 'selenium'),
    ('openai', 'chatgpt')
])
def test_baidu_search(keyword, expected, browser):
    # 找到搜索框并输入关键词
    search_box = browser.find_element(By.ID, 'kw')
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.ENTER)
    # 等待搜索结果加载
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'tsn_inner')))
    # 验证搜索结果页面中是否包含关键词
    # print(f"搜索结果页面内容：{browser.page_source.lower()}")
    assert expected in browser.page_source.lower(), f"搜索结果中未找到关键词 {keyword}"

