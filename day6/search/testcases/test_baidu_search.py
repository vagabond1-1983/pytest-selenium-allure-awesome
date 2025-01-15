import allure
import pytest

from day6.search.po.baidu_search import BaiduSearchPO


# @pytest.mark.usefixtures("setup")
class TestBaiduSearch:
    @allure.feature("百度搜索")
    @allure.story("搜索结果验证")
    @pytest.mark.parametrize('keyword, expected', [
        ('pytest', 'pytest123'),
        # ('selenium', 'selenium'),
        ('openai', 'chatgpt')
    ])
    def test_baidu_search(self, keyword, expected, setup, envs):
        driver = setup
        baiduSearchPO = BaiduSearchPO(driver, envs)
        # 验证搜索结果页面中是否包含关键词
        # print(f"搜索结果页面内容：{browser.page_source.lower()}")
        assert expected in baiduSearchPO.search(keyword=keyword), f"搜索结果中未找到关键词 {keyword}"
