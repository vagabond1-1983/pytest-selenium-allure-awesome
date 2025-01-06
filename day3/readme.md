# 第三天
## 全局配置抽提到 config.json配置中
1. 在项目根目录下创建 config.json文件，并将 browser、headless、timeout 等全局配置项放到此文件中
2. 在 day3/conftest.py 中，将 config.json中的配置项读取出来，并赋值给全局变量，方便后续使用
3. 设定环境配置的默认标识，用于切换环境
## 环境配置 yaml
在 config 目录下创建多环境 yaml，存放自动化环境相关静态数据，比方 base_url，登录用户等，模块级数据也可以按照 结构存放在此
读取时通过 conftest进行默认环境配置读取，用 fixture 特性传递到每个 PO，来读取环境数据
## allure配置
1. 用 pytest 运行测试用例并启动 allure 结果生成
```commandline
pytest -s day3/search/testcases/testBaiduSearch.py -v --alluredir ./allure_result
```
2. 在线生成 allure 报告
```commandline
allure serve ./allure_result
```