# 第一天
## mac 上下载 chromedriver并配置
先看下 chrome 的版本，确定了版本之后

下载相对应的驱动 chromedriver：https://googlechromelabs.github.io/chrome-for-testing/#s[table](https://googlechromelabs.github.io/chrome-for-testing/#stable)

放入 path 中：

```bash
sudo mv chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver
# 确认chromedriver可以启动
chromedriver --version
```
## 数据驱动
@pytest.mark.parametrize，用于数据驱动
## conftest
用于全局配置，hook（比方 setup、teardown等），基本跟@pytest.fixture混合使用
fixture 有几个 scope，常用的是 session、class 等
