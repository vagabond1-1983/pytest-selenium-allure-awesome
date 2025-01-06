import pytest

from day2.search.po.BaiduSearchPO import BaiduSearchPO


# @pytest.mark.usefixtures("setup")
class TestBaiduSearch:
    @pytest.mark.parametrize('keyword, expected', [
        ('pytest', 'pytest'),
        # ('selenium', 'selenium'),
        ('openai', 'chatgpt')
    ])
    def test_baidu_search(self, keyword, expected, setup, config):
        driver = setup
        baiduSearchPO = BaiduSearchPO(driver, config)
        # 验证搜索结果页面中是否包含关键词
        # print(f"搜索结果页面内容：{browser.page_source.lower()}")
        assert expected in baiduSearchPO.search(keyword=keyword), f"搜索结果中未找到关键词 {keyword}"
