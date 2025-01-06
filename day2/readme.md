# 第二天
## PO 模式
Base Page 和 Page Model，作用是用 POM 进行封装
这样就变成了 CASE-PO 两层结构。CASE 负责串接流程，PO 负责具体操作
## CASE 的 conftest做初始化
setup 用于driver 初始化，Base Page 初始化用于打开首页
## pytest.fixture
1.fixture的scope参数为session，那么所有的测试文件执行前执行一次

2.fixture的scope参数为module，那么每一个测试文件执行前都会执行一次conftest文件中的fixture

3.fixture的scope参数为class，那么每一个测试文件中的测试类执行前都会执行一次conftest文件中的fixture

4.fixture的scope参数为function，那么所有文件的测试用例执行前都会执行一次conftest文件中的fixture